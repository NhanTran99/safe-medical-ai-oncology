"""Runtime Integration boundary — Task #006.

Implements the locked B1-B4 behavioral requirements as one explicit,
deterministic entry point: `integrate_runtime_context`.

This module:
- accepts a `RuntimeIntegrationInput` (or `None`) and performs a pure,
  local transformation into a `RuntimeIntegrationResult` only;
- never constructs a `RepositorySource`, calls `RetrievalService`, or
  otherwise re-retrieves;
- never touches the filesystem;
- never reranks, reorders, deduplicates, enriches, or repairs provenance;
- never invokes an LLM, builds a prompt, generates a response, or performs
  output validation / clinical reasoning.
"""

from __future__ import annotations

import logging
import uuid
from datetime import UTC, datetime

from pydantic import ValidationError

from .models import (
    EvidenceState,
    GenerationContext,
    RuntimeIntegrationInput,
    RuntimeIntegrationOutcome,
    RuntimeIntegrationResult,
)

logger = logging.getLogger(__name__)


def integrate_runtime_context(
    integration_input: RuntimeIntegrationInput | None,
) -> RuntimeIntegrationResult:
    """Integrate explicit runtime inputs into a `GenerationContext`.

    Atomic: `outcome in {INTEGRATED, EMPTY_EVIDENCE}` implies a complete
    `GenerationContext`; every other outcome implies `context is None`.

    `integration_input is None` represents "no valid runtime input could be
    constructed by the caller" and deterministically produces
    `INVALID_INPUT`. A present `integration_input` with `rtep is None`
    deterministically produces the more specific `MISSING_RTEP` — this
    function never retrieves to obtain one.
    """
    if integration_input is None:
        logger.warning("Runtime Integration failed: no RuntimeIntegrationInput supplied")
        return RuntimeIntegrationResult(
            outcome=RuntimeIntegrationOutcome.INVALID_INPUT,
            context=None,
            message="no GenerationContext: RuntimeIntegrationInput was not supplied",
        )

    if integration_input.rtep is None:
        logger.info("Runtime Integration: no RTEP available")
        return RuntimeIntegrationResult(
            outcome=RuntimeIntegrationOutcome.MISSING_RTEP,
            context=None,
            message="no GenerationContext: no Runtime Evidence Package was supplied",
        )

    rtep = integration_input.rtep
    evidence_state = EvidenceState.EMPTY if len(rtep.evidence) == 0 else EvidenceState.HAS_EVIDENCE

    try:
        context = GenerationContext(
            integration_id=uuid.uuid4().hex,
            integration_timestamp=datetime.now(UTC),
            request_text=integration_input.request_text,
            navigation_context=integration_input.navigation_context,
            rtep=rtep,
            runtime_constraints=integration_input.runtime_constraints,
            evidence_state=evidence_state,
        )
    except ValidationError:
        # Defensive: under the current typed contracts every field here is
        # already validated at RuntimeIntegrationInput construction time, so
        # this branch is not reachable through normal typed usage — it
        # exists so an unexpected inability to construct a valid
        # GenerationContext fails as a controlled INTEGRATION_FAILURE
        # rather than an uncaught exception (spec section 6.5).
        logger.warning("Runtime Integration failed: unable to construct a valid GenerationContext")
        return RuntimeIntegrationResult(
            outcome=RuntimeIntegrationOutcome.INTEGRATION_FAILURE,
            context=None,
            message="no GenerationContext: contract violation constructing GenerationContext",
        )

    if evidence_state is EvidenceState.EMPTY:
        logger.info(
            "Runtime Integration: EMPTY_EVIDENCE integration_id=%s retrieval_id=%s",
            context.integration_id,
            rtep.metadata.retrieval_id,
        )
        return RuntimeIntegrationResult(
            outcome=RuntimeIntegrationOutcome.EMPTY_EVIDENCE,
            context=context,
            message="GenerationContext constructed with empty evidence: no evidence was retrieved",
        )

    logger.info(
        "Runtime Integration: INTEGRATED integration_id=%s retrieval_id=%s evidence_count=%d",
        context.integration_id,
        rtep.metadata.retrieval_id,
        len(rtep.evidence),
    )
    return RuntimeIntegrationResult(
        outcome=RuntimeIntegrationOutcome.INTEGRATED,
        context=context,
        message=None,
    )
