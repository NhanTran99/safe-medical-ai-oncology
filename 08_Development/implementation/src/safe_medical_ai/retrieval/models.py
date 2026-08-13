"""Typed domain models for the Task #003 retrieval foundation.

These models are intentionally separate from `models/output_contract.py`.
`RetrievalOutcome` is retrieval-result vocabulary (did navigation/hierarchical
resolution find something), not output-validation vocabulary. OUTPUT_CONTRACT's
`ValidationOutcome` (PASS / FAIL / SAFE_FALLBACK) governs a later, distinct
concern — whether a *generated response* is eligible for delivery — and is not
redefined or overloaded here.
"""

from __future__ import annotations

import re
from enum import Enum

from pydantic import BaseModel, Field

#: Navigation-key format shared by every navigation-first entry point
#: (RetrievalService and any RepositorySource implementation) so validation
#: stays identical wherever a population_id is accepted.
POPULATION_ID_PATTERN = re.compile(r"^PP-\d{4}$")


class ArtifactType(str, Enum):
    """The four canonical Gold Population Package artifacts.

    Mirrors the controlled artifact set defined by the Phase 3 Gold
    Population Package standard (01_CKO.md .. 04_QA_REPORT.md).
    """

    CKO = "CKO"
    KNOWLEDGE_PASSPORT = "KNOWLEDGE_PASSPORT"
    PRIMARY_EVIDENCE_PACKAGE = "PRIMARY_EVIDENCE_PACKAGE"
    QA_REPORT = "QA_REPORT"


_ARTIFACT_TYPE_ORDER: dict[ArtifactType, int] = {
    ArtifactType.CKO: 1,
    ArtifactType.KNOWLEDGE_PASSPORT: 2,
    ArtifactType.PRIMARY_EVIDENCE_PACKAGE: 3,
    ArtifactType.QA_REPORT: 4,
}


def artifact_type_sort_key(artifact_type: ArtifactType) -> int:
    """Canonical 01..04 ordering used for deterministic result ordering."""
    return _ARTIFACT_TYPE_ORDER[artifact_type]


class RetrievalOutcome(str, Enum):
    """Controlled retrieval-result classification.

    Distinct from and not a substitute for OUTPUT_CONTRACT's
    ValidationOutcome (PASS / FAIL / SAFE_FALLBACK).
    """

    FOUND = "FOUND"
    EMPTY = "EMPTY"
    INVALID_REQUEST = "INVALID_REQUEST"
    NOT_FOUND = "NOT_FOUND"


class RetrievalRequest(BaseModel):
    """A navigation-first retrieval request.

    `population_id` is the required top-level navigation key (hierarchical
    level: Population / PP). `artifact_type` optionally narrows to a single
    canonical artifact; omitted, all known artifacts for the population are
    returned.
    """

    population_id: str
    artifact_type: ArtifactType | None = None


class RetrievalCandidate(BaseModel):
    """A single located artifact, with provenance sufficient for traceability."""

    population_id: str
    artifact_type: ArtifactType
    source_path: str = Field(
        description="Authoritative controlled-repository path or equivalent controlled identifier."
    )
    title: str | None = None


class RetrievalResponse(BaseModel):
    """The structured result of a retrieval request."""

    outcome: RetrievalOutcome
    request: RetrievalRequest
    results: list[RetrievalCandidate] = Field(default_factory=list)
    trace_id: str | None = None
    message: str | None = None
