"""B07 bounded execution harness.

`execute_case` orchestrates ONE call to the existing, unmodified governed
execution path (`api.main._run_controlled_evaluation`, the same function
`/cer/evaluate` and `/chat/query` already both call) for one approved
`case_id`, and maps its result onto a durable `CampaignExecutionResult`.

This module implements NO CER logic, NO retrieval, NO evidence assembly,
NO prompt construction, NO provider call, and NO validation of its own --
it only invokes the existing boundary and observes/records what happened
(DETECT). It never retries, substitutes, or repairs a failure (no
CLASSIFY-time or RECORD-time remediation) -- see `capture.py` for RECORD,
and the calling campaign process (not this module) for any later ASSESS
step.

This module is NOT the 239-case execution campaign itself. It is the
capability a future, separately-authorized campaign run would call, once
per approved case_id it has been told to execute.
"""

from __future__ import annotations

import logging
import subprocess
import uuid
from datetime import UTC, datetime
from pathlib import Path

from ..api.main import ControlledEvaluationRequest, _run_controlled_evaluation
from ..cases import CaseResolutionOutcome, CaseResolutionResult
from ..config import get_settings
from ..llm.base import LLMAdapter
from ..trace import set_trace_id
from .models import CampaignExecutionResult

logger = logging.getLogger(__name__)


def _best_effort_repository_commit() -> str | None:
    """Return the current git commit hash, or `None` if it cannot be
    safely determined (e.g. not a git checkout, `git` unavailable).

    Never fabricated: a `None` here means the repository/runtime
    environment genuinely could not supply this baseline field, not that
    it was skipped or guessed.
    """
    repo_root = Path(__file__).resolve().parents[5]
    try:
        completed = subprocess.run(
            ["git", "rev-parse", "HEAD"],
            cwd=repo_root,
            capture_output=True,
            text=True,
            timeout=5,
            check=True,
        )
        commit = completed.stdout.strip()
        return commit or None
    except Exception:
        logger.warning("execute_case: repository commit not safely available", exc_info=True)
        return None


def _configured_provider_model(provider_name: str | None) -> str | None:
    """B10 (I4): the exact configured model string, when applicable.

    Only meaningful for `OpenAIProvider` -- `DeterministicLocalProvider`
    has no configured model, so this is `None` for it (never a fabricated
    placeholder). Read from the existing settings/configuration path
    (`config.get_settings().openai_model`) rather than reaching into the
    provider instance: `OpenAIProvider` is not amended to expose this, per
    the locked I4 boundary ("Do NOT redesign OpenAIProvider").

    This reflects the currently *configured* model, which matches what
    was actually used whenever `provider` came from the existing
    `_select_provider()` default (the path every existing caller of this
    harness uses) -- a provider a caller explicitly injects with a
    different model string is not separately distinguished here.
    """
    if provider_name != "OpenAIProvider":
        return None
    return get_settings().openai_model


def execute_case(
    case_id: str,
    request_text: str,
    *,
    provider: LLMAdapter | None = None,
) -> CampaignExecutionResult:
    """Execute one approved `case_id` through the existing governed path.

    `case_id` is the sole execution authority (D03/Principle 2): it is
    resolved through the existing `EvaluationCaseResolver` inside
    `_run_controlled_evaluation`, exactly as `/cer/evaluate` already does
    -- this function never accepts or honors an arbitrary `population_id`.

    `provider` is optional; when omitted, `_run_controlled_evaluation`
    falls back to its existing `_select_provider()` choice (the
    deterministic provider unless `SMA_OPENAI_API_KEY` is configured),
    so calling this with no arguments is deterministic by default.

    Returns a `CampaignExecutionResult` unconditionally -- including for a
    failed case resolution -- so every execution attempt is observable
    (DETECT), never silently dropped.
    """
    execution_id = uuid.uuid4().hex
    execution_timestamp = datetime.now(UTC)
    trace_id = set_trace_id()
    repository_commit = _best_effort_repository_commit()

    outcome = _run_controlled_evaluation(
        ControlledEvaluationRequest(request_text=request_text, case_id=case_id),
        provider=provider,
    )

    if isinstance(outcome, CaseResolutionResult):
        logger.info(
            "execute_case: case resolution %s case_id=%s execution_id=%s",
            outcome.outcome.value,
            case_id,
            execution_id,
        )
        return CampaignExecutionResult(
            execution_id=execution_id,
            execution_timestamp=execution_timestamp,
            trace_id=trace_id,
            repository_commit=repository_commit,
            case_id=case_id,
            resolved_population_id=None,
            case_resolution_outcome=outcome.outcome,
            message=outcome.message,
        )

    result = outcome  # CERResult -- resolution succeeded to reach this point.
    resolved_population_id = (
        result.retrieval_response.request.population_id if result.retrieval_response else None
    )
    generation_response = (
        result.generation_result.response if result.generation_result else None
    )
    provider_name = generation_response.provider_name if generation_response else None

    logger.info(
        "execute_case: CER outcome=%s case_id=%s execution_id=%s",
        result.outcome.value,
        case_id,
        execution_id,
    )

    return CampaignExecutionResult(
        execution_id=execution_id,
        execution_timestamp=execution_timestamp,
        trace_id=trace_id,
        repository_commit=repository_commit,
        case_id=case_id,
        resolved_population_id=resolved_population_id,
        case_resolution_outcome=CaseResolutionOutcome.RESOLVED,
        safety_action=result.safety_decision.action if result.safety_decision else None,
        retrieval_outcome=result.retrieval_response.outcome if result.retrieval_response else None,
        retrieval_result_count=(
            len(result.retrieval_response.results) if result.retrieval_response else None
        ),
        generation_outcome=result.generation_result.outcome if result.generation_result else None,
        provider_name=provider_name,
        validation_outcome=result.validation_result.outcome if result.validation_result else None,
        cer_outcome=result.outcome,
        # B10 (I3): the same evidence_package_id already threaded through
        # RTEP Assembly -> Generation (see evidence/models.py's
        # RuntimeEvidenceMetadata.evidence_package_id and
        # generation/models.py's CandidateResponse.evidence_package_id) --
        # not a second evidence-identity system, just this durable record
        # now also carrying the identifier that was already there.
        evidence_package_id=generation_response.evidence_package_id if generation_response else None,
        provider_model=_configured_provider_model(provider_name),
        message=result.message,
    )
