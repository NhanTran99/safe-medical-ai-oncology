"""Typed Runtime Evidence Package (RTEP) contract — Task #005.

Implements the locked B1/B2 decisions (IR20/IR21) and
`EVIDENCE_PACKAGE_SPECIFICATION.md` §5-11: the RTEP is the runtime
representation of governed evidence supplied to a future Generation layer.
It is distinct from, and never equated with, the Primary Evidence Package
(Artifact 03 of a Gold Population Package) or with `RetrievalResponse`.

All models here are frozen (immutable after construction) per B2-07 /
EVIDENCE_PACKAGE_SPECIFICATION.md §11. Evidence is stored as a `tuple`
rather than a `list` so the sequence itself cannot be mutated in place
after assembly (a plain mutable list nested in a frozen model would still
be append-able).
"""

from __future__ import annotations

from datetime import datetime
from enum import Enum

from pydantic import BaseModel, ConfigDict, Field

from ..retrieval import ArtifactType, RetrievalRequest


class RTEPAssemblyOutcome(str, Enum):
    """Controlled RTEP-assembly result classification.

    Distinct new vocabulary — neither `RetrievalOutcome`
    (FOUND/EMPTY/INVALID_REQUEST/NOT_FOUND) nor OUTPUT_CONTRACT's
    `ValidationOutcome` (PASS/FAIL/SAFE_FALLBACK) are reused or redefined
    here, per spec section 14.

    `RETRIEVAL_NOT_FOUND` / `RETRIEVAL_INVALID_REQUEST` are retrieval-
    originated: they mean assembly was never attempted because the input
    `RetrievalResponse` itself was NOT_FOUND / INVALID_REQUEST, and that
    outcome is propagated unchanged (spec sections 8.3/8.4).

    The remaining values are assembly-originated failures (spec section 14's
    "small internal taxonomy"): the retrieval succeeded (FOUND or EMPTY) but
    RTEP assembly itself could not produce a contract-valid package.

    There is no `AMBIGUOUS` value: the current, locked `RetrievalOutcome`
    contract (Task #003/#004, preserved unmodified per spec section 16) has
    no ambiguous state of its own — `FilesystemRepositorySource` already
    resolves an ambiguous population match to `NOT_FOUND` rather than
    surfacing ambiguity to callers. Spec section 14 lists `AMBIGUOUS` as
    "where applicable"; it is not applicable given the preserved upstream
    contract, so no dead/unreachable enum value is added for it.
    """

    ASSEMBLED = "ASSEMBLED"
    RETRIEVAL_NOT_FOUND = "RETRIEVAL_NOT_FOUND"
    RETRIEVAL_INVALID_REQUEST = "RETRIEVAL_INVALID_REQUEST"
    MISSING_METADATA = "MISSING_METADATA"
    INVALID_EVIDENCE_ITEM = "INVALID_EVIDENCE_ITEM"
    INCOMPLETE_PROVENANCE = "INCOMPLETE_PROVENANCE"


class EvidenceItemProvenance(BaseModel):
    """Minimum per-item provenance (spec section 5.3 / B2-04).

    Supplied by the caller of assembly (see `RTEPAssemblyContext` /
    `assemble_runtime_evidence_package`'s `provenance_by_source_path`
    argument) — never derived, guessed, or synthesized by assembly itself
    (spec section 13: "Do not synthesize missing provenance").
    """

    model_config = ConfigDict(frozen=True)

    knowledge_object_id: str = Field(min_length=1)
    knowledge_passport_id: str = Field(min_length=1)
    source_id: str = Field(min_length=1)
    guideline_version: str = Field(min_length=1)


class EvidenceItem(BaseModel):
    """One retrieved Clinical Knowledge Object reference plus its provenance.

    Identity/pointer fields carried forward unchanged from the originating
    `RetrievalCandidate`. `content` (Track 3 BATCH 01) is likewise carried
    forward unchanged from `RetrievalCandidate.content` when the source
    `RepositorySource` loaded it — never independently (re-)loaded, derived,
    or fabricated by assembly itself (see `assembly.py`). Deliberately still
    excludes prompt instructions, prompt templates, model directives,
    generated responses, or model-generated interpretation.
    """

    model_config = ConfigDict(frozen=True)

    population_id: str
    artifact_type: ArtifactType
    source_path: str
    title: str | None
    provenance: EvidenceItemProvenance
    content: str | None = None


class RTEPAssemblyContext(BaseModel):
    """Caller-supplied runtime metadata required to assemble an RTEP.

    Deliberately excludes `evidence_package_id` and `generation_timestamp`:
    per spec section 10, those are legitimately runtime-generated
    identity/timestamp fields produced by assembly itself, not values a
    caller could supply in advance (there is no package identity before
    assembly exists).
    """

    model_config = ConfigDict(frozen=True)

    retrieval_id: str = Field(min_length=1)
    navigation_context_id: str = Field(min_length=1)
    retrieval_policy_version: str = Field(min_length=1)
    knowledge_base_version: str = Field(min_length=1)


class RuntimeEvidenceMetadata(BaseModel):
    """Minimum Evidence Metadata (spec section 5.2 / B2-03), fully populated.

    Combines the caller-supplied `RTEPAssemblyContext` with the two fields
    assembly itself generates at package-creation time.
    """

    model_config = ConfigDict(frozen=True)

    evidence_package_id: str = Field(min_length=1)
    retrieval_id: str = Field(min_length=1)
    navigation_context_id: str = Field(min_length=1)
    retrieval_policy_version: str = Field(min_length=1)
    knowledge_base_version: str = Field(min_length=1)
    generation_timestamp: datetime


class RuntimeEvidencePackage(BaseModel):
    """The immutable Runtime Evidence Package (RTEP).

    Two logical components per spec section 5.1 / B1-04 / B2-01:
    `metadata` (Evidence Metadata) and `evidence` (Evidence Content).
    Evidence ordering is exactly the order assembly received it in — see
    `assembly.py` — never sorted, reranked, or deduplicated here.
    """

    model_config = ConfigDict(frozen=True)

    metadata: RuntimeEvidenceMetadata
    evidence: tuple[EvidenceItem, ...] = Field(default_factory=tuple)


class RTEPAssemblyResult(BaseModel):
    """The atomic result of one assembly call (B3-11).

    `outcome == ASSEMBLED` if and only if `package` is the one complete
    RTEP produced; every other outcome implies `package is None` (zero
    RTEP) — assembly never returns a partial/best-effort package.
    """

    model_config = ConfigDict(frozen=True)

    outcome: RTEPAssemblyOutcome
    package: RuntimeEvidencePackage | None = None
    request: RetrievalRequest | None = None
    message: str | None = None
