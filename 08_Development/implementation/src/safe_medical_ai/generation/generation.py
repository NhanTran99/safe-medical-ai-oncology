"""Generation boundary — Task #007.

Implements the locked B1-B4 behavioral requirements as one explicit,
deterministic entry point: `generate_candidate_response`.

This module:
- accepts an authoritative `GenerationContext` (Task #006) and an explicit
  `LLMAdapter` provider (Task #002's provider-agnostic interface — reused,
  not reinvented) and performs a local orchestration only;
- calls the governed Prompt Builder (`prompting.build_prompt`, Track 3
  BATCH 03) to produce a `PromptSpecification` before ever constructing a
  provider request — this module does not itself construct a prompt or
  adjudicate the locked Prompt Contract, it only invokes that boundary and
  returns `PROMPT_BLOCKED` if it declines;
- passes the authoritative governed evidence from `context.rtep` to the
  provider through a typed `ProviderGenerationRequest` (Change Request
  review fix — see `models.py`), not merely the raw request text;
- never constructs a `RepositorySource`, calls `RetrievalService`, or
  otherwise re-retrieves;
- never touches the filesystem;
- never reranks, reorders, deduplicates, enriches, or repairs provenance —
  the evidence handed to the provider is the exact `context.rtep.evidence`
  tuple, unmodified;
- never imports or calls anything from a Validation layer (none exists yet);
- never performs clinical reasoning, safety adjudication, citation
  verification, or hallucination detection — those remain downstream,
  out of scope here.
"""

from __future__ import annotations

import logging
import uuid
from datetime import UTC, datetime

from ..integration import EvidenceState, GenerationContext
from ..llm.base import LLMAdapter
from ..prompting import PromptBuilderOutcome, build_prompt
from .models import (
    EMPTY_EVIDENCE_POLICY_RESPONSE_TEXT,
    CandidateResponse,
    GenerationOutcome,
    GenerationResult,
    ProviderGenerationRequest,
)

logger = logging.getLogger(__name__)


class ProviderError(Exception):
    """Base class for provider-boundary failures raised by an `LLMAdapter`."""


class ProviderTimeoutError(ProviderError):
    """Raised by a provider implementation when it times out or is unavailable."""


class ProviderPartialOutputError(ProviderError):
    """Raised by a provider implementation when generation was interrupted/incomplete."""


def generate_candidate_response(
    context: GenerationContext | None,
    provider: LLMAdapter,
) -> GenerationResult:
    """Generate a `CandidateResponse` from an authoritative `GenerationContext`.

    Atomic: `outcome in {GENERATED, EMPTY_EVIDENCE_RESPONSE}` implies a
    complete `CandidateResponse`; every other outcome implies
    `response is None`.

    `context is None` represents "no valid GenerationContext is available"
    and deterministically produces `INVALID_CONTEXT`. `context.rtep is None`
    is not reachable through the current typed `GenerationContext` contract
    (its `rtep` field is required) but is defensively checked anyway and
    produces `CONTEXT_MISSING_RTEP` rather than an uncaught `AttributeError`
    — the same defensive-completeness pattern used for `INTEGRATION_FAILURE`
    in Task #006.

    Does not reconstruct or independently validate the upstream RTEP: the
    evidence state is read directly from `context.evidence_state`, exactly
    as Runtime Integration already determined it (spec section 6).

    When `context.evidence_state` is `HAS_EVIDENCE`, the provider is called
    with a `ProviderGenerationRequest` carrying the authoritative
    `context.rtep.evidence`/`context.rtep.metadata` unchanged (see
    `models.ProviderGenerationRequest`) — the provider never receives only
    bare request text without the governed evidence behind it.
    """
    if context is None:
        logger.warning("Generation failed: no GenerationContext supplied")
        return GenerationResult(
            outcome=GenerationOutcome.INVALID_CONTEXT,
            response=None,
            message="no CandidateResponse: GenerationContext was not supplied",
        )

    if context.rtep is None:
        logger.warning("Generation failed: GenerationContext has no RTEP")
        return GenerationResult(
            outcome=GenerationOutcome.CONTEXT_MISSING_RTEP,
            response=None,
            message="no CandidateResponse: GenerationContext has no Runtime Evidence Package",
        )

    trace_ids = {
        "integration_id": context.integration_id,
        "retrieval_id": context.rtep.metadata.retrieval_id,
        "navigation_context_id": context.rtep.metadata.navigation_context_id,
        "evidence_package_id": context.rtep.metadata.evidence_package_id,
    }

    if context.evidence_state is EvidenceState.EMPTY:
        logger.info("Generation: EMPTY_EVIDENCE_RESPONSE integration_id=%s", context.integration_id)
        response = CandidateResponse(
            candidate_response_id=uuid.uuid4().hex,
            generation_timestamp=datetime.now(UTC),
            content=EMPTY_EVIDENCE_POLICY_RESPONSE_TEXT,
            evidence_state=context.evidence_state,
            provider_name=None,
            **trace_ids,
        )
        return GenerationResult(
            outcome=GenerationOutcome.EMPTY_EVIDENCE_RESPONSE,
            response=response,
            message="CandidateResponse is the fixed no-evidence policy response, not a provider generation",
        )

    # Track 3 BATCH 03: build the governed PromptSpecification via the
    # Prompt Builder before ever constructing a provider request. The
    # Prompt Builder enforces the locked Prompt Contract (Navigation
    # Context / Safety Decision / Evidence Package all mandatory) and
    # blocks deterministically rather than falling back to any ad-hoc
    # construction.
    prompt_result = build_prompt(
        navigation_context=context.navigation_context,
        safety_decision=context.safety_decision,
        evidence_package=context.rtep,
        request_text=context.request_text,
    )
    if prompt_result.outcome is not PromptBuilderOutcome.BUILT:
        logger.warning(
            "Generation failed: prompt construction blocked (%s) integration_id=%s",
            prompt_result.outcome.value,
            context.integration_id,
        )
        return GenerationResult(
            outcome=GenerationOutcome.PROMPT_BLOCKED,
            response=None,
            message=prompt_result.message,
        )

    # Pass the authoritative governed evidence through to the provider as
    # part of the typed request — not just the raw request text. `evidence`
    # and `evidence_metadata` are the same immutable objects already on
    # `context.rtep`, referenced unchanged: no reranking, reordering,
    # deduplication, or provenance repair happens here.
    provider_request = ProviderGenerationRequest(
        request_text=context.request_text,
        navigation_context=context.navigation_context,
        evidence=context.rtep.evidence,
        evidence_metadata=context.rtep.metadata,
        runtime_constraints=context.runtime_constraints,
        prompt_specification=prompt_result.specification,
    )

    try:
        raw_output = provider.generate(request=provider_request)
    except ProviderTimeoutError:
        logger.warning("Generation failed: provider timeout/unavailable integration_id=%s", context.integration_id)
        return GenerationResult(
            outcome=GenerationOutcome.PROVIDER_TIMEOUT,
            response=None,
            message="no CandidateResponse: provider timed out or was unavailable",
        )
    except ProviderPartialOutputError:
        logger.warning("Generation failed: partial/interrupted generation integration_id=%s", context.integration_id)
        return GenerationResult(
            outcome=GenerationOutcome.PARTIAL_GENERATION,
            response=None,
            message="no CandidateResponse: generation was interrupted/incomplete",
        )
    except ProviderError:
        logger.warning("Generation failed: provider error integration_id=%s", context.integration_id)
        return GenerationResult(
            outcome=GenerationOutcome.PROVIDER_FAILURE,
            response=None,
            message="no CandidateResponse: the provider raised an error",
        )
    except Exception:
        # Controlled unexpected/internal failure (spec section 8): anything
        # not raised as a typed ProviderError is treated as Generation's own
        # defensive safety net, not a provider-boundary failure.
        logger.exception("Generation failed: unexpected internal failure integration_id=%s", context.integration_id)
        return GenerationResult(
            outcome=GenerationOutcome.INTERNAL_FAILURE,
            response=None,
            message="no CandidateResponse: an unexpected internal failure occurred",
        )

    if not isinstance(raw_output, str) or not raw_output.strip():
        logger.warning("Generation failed: malformed provider output integration_id=%s", context.integration_id)
        return GenerationResult(
            outcome=GenerationOutcome.MALFORMED_PROVIDER_OUTPUT,
            response=None,
            message="no CandidateResponse: provider output was not a non-blank string",
        )

    response = CandidateResponse(
        candidate_response_id=uuid.uuid4().hex,
        generation_timestamp=datetime.now(UTC),
        content=raw_output,
        evidence_state=context.evidence_state,
        provider_name=type(provider).__name__,
        **trace_ids,
    )

    logger.info(
        "Generation: GENERATED candidate_response_id=%s integration_id=%s",
        response.candidate_response_id,
        context.integration_id,
    )
    return GenerationResult(outcome=GenerationOutcome.GENERATED, response=response, message=None)
