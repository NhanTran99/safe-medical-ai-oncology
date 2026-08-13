"""Typed Generation contracts — Task #007.

Implements the locked B1-B4 decision set: Generation consumes an
authoritative `GenerationContext` (Task #006) and produces a typed
`CandidateResponse`, or an explicit typed failure — never a mutated
upstream object, never a claim of finality/clinical validation/safety
approval/citation verification (spec section 5).

Dependency direction (locked): `generation -> integration -> evidence ->
retrieval`. Nothing in `retrieval/`, `evidence/`, or `integration/` is
modified by this module.
"""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import Final

from pydantic import BaseModel, ConfigDict, Field

from ..evidence import EvidenceItem, RuntimeEvidenceMetadata
from ..integration import EvidenceState, RuntimeConstraints
from ..models.output_contract import NavigationContextPlaceholder

#: The single, locked, non-provider-generated response for the
#: EMPTY_EVIDENCE policy branch (spec section 6). This is a governed
#: policy decision, not an implementation detail: Generation must not
#: silently answer an unsupported clinical question from model knowledge
#: when no evidence was retrieved, and the exact wording is fixed rather
#: than left to per-call discretion. Changing this text is a policy change
#: and requires the same governance approval as any other locked B1-B4
#: decision — it must not be silently edited as part of an unrelated code
#: change.
EMPTY_EVIDENCE_POLICY_RESPONSE_TEXT: Final[str] = (
    "No governed evidence was retrieved for this request. A candidate "
    "response cannot be generated without supporting evidence."
)


class GenerationOutcome(str, Enum):
    """Controlled Generation-result classification.

    A distinct vocabulary from `RetrievalOutcome`, `RTEPAssemblyOutcome`,
    `RuntimeIntegrationOutcome`, and OUTPUT_CONTRACT's `ValidationOutcome`
    — never merged with any of them (same isolation principle established
    by every prior boundary). In particular, member names are deliberately
    distinct in spelling from `RuntimeIntegrationOutcome.EMPTY_EVIDENCE` /
    `.MISSING_RTEP` even though they describe related upstream states —
    `EMPTY_EVIDENCE_RESPONSE` and `CONTEXT_MISSING_RTEP` below — so no two
    layers ever share a literal outcome name.

    `GENERATED` and `EMPTY_EVIDENCE_RESPONSE` are the two outcomes that
    produce a `CandidateResponse` (spec section 5's atomicity rule extended
    to the locked EMPTY_EVIDENCE policy branch, which is a valid controlled
    output, not a failure — spec section 6: "Do not convert EMPTY into
    technical failure" carried forward from Task #005/#006's identical
    principle). Every other outcome implies no `CandidateResponse`.
    """

    GENERATED = "GENERATED"
    EMPTY_EVIDENCE_RESPONSE = "EMPTY_EVIDENCE_RESPONSE"
    INVALID_CONTEXT = "INVALID_CONTEXT"
    CONTEXT_MISSING_RTEP = "CONTEXT_MISSING_RTEP"
    PROVIDER_FAILURE = "PROVIDER_FAILURE"
    PROVIDER_TIMEOUT = "PROVIDER_TIMEOUT"
    MALFORMED_PROVIDER_OUTPUT = "MALFORMED_PROVIDER_OUTPUT"
    PARTIAL_GENERATION = "PARTIAL_GENERATION"
    INTERNAL_FAILURE = "INTERNAL_FAILURE"


class ProviderGenerationRequest(BaseModel):
    """The typed, locked contract Generation passes to an `LLMAdapter` provider.

    This is the fix for the reviewed architectural blocker: a provider must
    receive the authoritative governed evidence from `GenerationContext.rtep`,
    not only the raw request text. `evidence` and `evidence_metadata` are
    the *same* immutable objects already produced by RTEP Assembly
    (Task #005) and carried by `GenerationContext` (Task #006) — referenced
    here, never copied, reordered, reranked, deduplicated, or repaired.
    Constructing this object is pure data assembly with no retrieval calls
    and no new retrieval/ranking layer.
    """

    model_config = ConfigDict(frozen=True)

    request_text: str
    navigation_context: NavigationContextPlaceholder
    evidence: tuple[EvidenceItem, ...]
    evidence_metadata: RuntimeEvidenceMetadata
    runtime_constraints: RuntimeConstraints


class CandidateResponse(BaseModel):
    """A candidate generation output.

    Never labeled or treated as final, clinically validated, safety
    approved, or citation verified (spec section 5) — those are downstream
    Validation-layer concerns this module does not implement or claim.

    Carries traceability identifiers back to its generation attempt and
    upstream runtime evidence/context (spec section 9), without re-embedding
    the full `GenerationContext`/RTEP/evidence objects themselves — a
    `CandidateResponse` is a new, independent output object, not a
    decorated copy of its inputs.
    """

    model_config = ConfigDict(frozen=True)

    candidate_response_id: str = Field(min_length=1)
    generation_timestamp: datetime
    content: str = Field(min_length=1)
    evidence_state: EvidenceState
    provider_name: str | None = None

    # Traceability identifiers (spec section 9), sourced from the
    # GenerationContext/RTEP this candidate was generated from.
    integration_id: str = Field(min_length=1)
    retrieval_id: str = Field(min_length=1)
    navigation_context_id: str = Field(min_length=1)
    evidence_package_id: str = Field(min_length=1)


class GenerationResult(BaseModel):
    """The atomic result of one Generation attempt.

    `outcome in {GENERATED, EMPTY_EVIDENCE_RESPONSE}` if and only if
    `response` is a complete `CandidateResponse`; every other outcome
    implies `response is None` — Generation never returns a partial or
    interrupted `CandidateResponse` as success (spec section 5/8).
    """

    model_config = ConfigDict(frozen=True)

    outcome: GenerationOutcome
    response: CandidateResponse | None = None
    message: str | None = None
