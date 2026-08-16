"""Typed Evaluation Case contracts — Phase 6 Stage 2 Track 2.

An `EvaluationCase` is the canonical controlled-execution unit (AD-1): one
approved `case_id` resolves, via the frozen Evaluation Case Manifest (a
governed artifact this module never edits or reinterprets), to exactly one
approved `population_id` and its expected primary execution artifact
(AD-2). This module defines only the typed resolution contracts —
resolution logic lives in `resolver.py`; the manifest projection a caller
loads is a derived, regenerable, non-authoritative binding (see
`README.md`) — never treated as an independent source of truth.
"""

from __future__ import annotations

from enum import Enum

from pydantic import BaseModel, ConfigDict, Field

from ..retrieval import ArtifactType


class CaseResolutionOutcome(str, Enum):
    """Controlled case-resolution result classification.

    A distinct vocabulary from every other layer's outcome enum (the same
    isolation convention every prior boundary follows in this codebase) —
    never merged with `RetrievalOutcome`, `CEROutcome`, etc.
    """

    RESOLVED = "RESOLVED"
    UNKNOWN_CASE = "UNKNOWN_CASE"
    MALFORMED_CASE_ID = "MALFORMED_CASE_ID"
    PROJECTION_UNAVAILABLE = "PROJECTION_UNAVAILABLE"


class EvaluationCase(BaseModel):
    """One resolved, approved controlled-execution unit (AD-1 / AD-2).

    Carries the manifest-derived identity needed to construct a governed
    execution request, plus full traceability back to the authoritative
    frozen manifest this binding was derived from — every resolved case
    can be audited back to a specific manifest file, version, and hash.
    """

    model_config = ConfigDict(frozen=True)

    case_id: str = Field(min_length=1)
    population_id: str = Field(min_length=1)
    expected_primary_artifact_type: ArtifactType
    source_manifest: str = Field(min_length=1)
    source_manifest_version: str = Field(min_length=1)
    source_manifest_sha256: str = Field(min_length=1)


class CaseResolutionResult(BaseModel):
    """The atomic result of one case-resolution attempt.

    `outcome == RESOLVED` if and only if `case` is populated; every other
    outcome implies `case is None` — resolution never returns a partial or
    guessed case (fail-closed, spec section E/O).
    """

    model_config = ConfigDict(frozen=True)

    outcome: CaseResolutionOutcome
    case: EvaluationCase | None = None
    message: str | None = None
