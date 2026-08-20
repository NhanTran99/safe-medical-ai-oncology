"""Typed B07 campaign execution-result contracts.

`CampaignExecutionResult` is a durable, structured record of one attempt
to run the *existing* governed execution path
(`api.main._run_controlled_evaluation`) for one approved `case_id`. It
reuses every existing typed outcome vocabulary by reference
(`CaseResolutionOutcome`, `SafetyAction`, `RetrievalOutcome`,
`GenerationOutcome`, `CandidateValidationOutcome`, `CEROutcome`) rather
than duplicating or reinterpreting any of them (D04/Principle 3).

This module implements no execution logic itself (see `harness.py`) and
carries no clinical content, clinical judgment, or clinical-quality score
of its own -- it only records which of the existing, already-governed
outcome values occurred for one execution attempt.
"""

from __future__ import annotations

from datetime import datetime
from enum import Enum

from pydantic import BaseModel, ConfigDict, Field

from ..cases import CaseResolutionOutcome
from ..cer import CEROutcome
from ..generation import GenerationOutcome
from ..retrieval import RetrievalOutcome
from ..safety import SafetyAction
from ..validation import CandidateValidationOutcome


class EvidenceCaptureOutcome(str, Enum):
    """Whether a `CampaignExecutionResult` was durably persisted.

    This is a mechanical capture-status signal only -- never a clinical
    outcome, and never merged with any other layer's outcome vocabulary
    (same isolation convention every existing boundary in this codebase
    follows).
    """

    CAPTURED = "CAPTURED"
    WRITE_FAILED = "WRITE_FAILED"


class CampaignExecutionResult(BaseModel):
    """Atomic, immutable record of one B07 execution attempt.

    Frozen: a result is never mutated in place. A re-execution of the same
    `case_id` produces a new `CampaignExecutionResult` with a new
    `execution_id`, appended alongside (never replacing) any prior result
    for that `case_id` -- failures are never rewritten into successes
    (D10/Principle 7), and a durable store built from these records is
    append-only by construction (see `capture.py`).

    Every field that could not be established without either fabricating
    data or re-implementing/duplicating an existing boundary is left
    `None` rather than guessed -- e.g. `resolved_population_id` is `None`
    whenever case resolution itself failed, and `repository_commit` is
    `None` when it cannot be safely determined (see
    `harness._best_effort_repository_commit`).
    """

    model_config = ConfigDict(frozen=True)

    # Execution identity (D08, Principle 6 / Design Question F): distinct
    # per attempt, so repeated executions of the same case_id are always
    # separately identifiable.
    execution_id: str = Field(min_length=1)
    execution_timestamp: datetime
    trace_id: str | None = None

    # Reproducibility baseline (Principle 6 / Design Question G): only
    # real, safely-available repository/runtime metadata -- never an
    # invented evaluator/clinical-validation/baseline version.
    repository_commit: str | None = None

    # Execution authority (D03/Principle 2): the approved case_id is
    # always recorded, even when resolution itself failed.
    case_id: str = Field(min_length=1)
    resolved_population_id: str | None = None

    # Stage-level outcomes (D04/Principle 3), each reusing the existing
    # typed vocabulary unchanged. `None` means that stage was never
    # reached (e.g. a resolution failure means every later stage is None),
    # exactly mirroring how `CERResult`'s own optional fields behave.
    case_resolution_outcome: CaseResolutionOutcome
    safety_action: SafetyAction | None = None
    retrieval_outcome: RetrievalOutcome | None = None
    retrieval_result_count: int | None = None
    generation_outcome: GenerationOutcome | None = None
    provider_name: str | None = None
    validation_outcome: CandidateValidationOutcome | None = None
    cer_outcome: CEROutcome | None = None

    # Mechanical capture status (D08) -- set by `capture.record_execution_result`,
    # not by the harness itself (a result is constructed before anyone has
    # attempted to persist it).
    evidence_capture_status: EvidenceCaptureOutcome | None = None

    # Whatever message the failing (or succeeding) stage already provided
    # -- never a fabricated explanation.
    message: str | None = None
