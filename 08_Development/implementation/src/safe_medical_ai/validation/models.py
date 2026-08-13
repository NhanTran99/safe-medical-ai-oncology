"""Typed Validation contracts — Task #008.

Implements the locked B1-B4 decision set: Validation consumes a
`CandidateResponse` (Task #007) plus the authoritative RTEP/evidence
context and produces a typed `ValidationResult`. Validation is a
downstream evaluator, never a second retrieval/generation authority
(spec section 4).

Dependency direction (locked): `validation -> generation -> integration ->
evidence -> retrieval`. Nothing in `retrieval/`, `evidence/`,
`integration/`, or `generation/` is modified by this module.
"""

from __future__ import annotations

from datetime import datetime
from enum import Enum

from pydantic import BaseModel, ConfigDict, Field

from ..evidence import RuntimeEvidencePackage
from ..generation import CandidateResponse


class CandidateValidationOutcome(str, Enum):
    """Controlled Validation-result classification (spec sections 7-8).

    Deliberately named `CandidateValidationOutcome`, not `ValidationOutcome`
    — `models/output_contract.py` already defines a `ValidationOutcome`
    class (Task #002's forward-looking OUTPUT_CONTRACT.md placeholder,
    PASS/FAIL/SAFE_FALLBACK). Reusing that exact class name here for a
    different, narrower member set (this is CandidateResponse-level
    validation, not the final OUTPUT_CONTRACT delivery decision) would
    shadow/confuse two distinct types across the codebase.

    Spec section 7 requires disjointness from `RetrievalOutcome`,
    `RTEPAssemblyOutcome`, `RuntimeIntegrationOutcome`, and
    `GenerationOutcome` — but *not* from `ValidationOutcome`. That omission
    is deliberate: section 7 also requires this vocabulary to include
    `SAFE_FALLBACK`, which is the same literal value OUTPUT_CONTRACT.md's
    `ValidationOutcome.SAFE_FALLBACK` already uses. This is the one
    intentional, spec-mandated exception to the "every layer's vocabulary
    is fully disjoint from every other" rule established by every prior
    boundary — see `test_candidate_validation_outcome_shares_only_safe_fallback_with_validation_outcome`.

    `INVALID_VALIDATION_INPUT` is spelled this way, not the spec's
    illustrative bare `INVALID_INPUT`, because `RuntimeIntegrationOutcome`
    already has a member literally named `INVALID_INPUT` — reusing it here
    would be exactly the "upstream enum literal collision" section 7
    prohibits.

    There is no bare `INVALID` member: section 9's own failure-precedence
    list never uses it, only the five specific values below plus `VALID`/
    `SAFE_FALLBACK` — section 7's "VALID / INVALID / SAFE_FALLBACK minimum
    semantic vocabulary" is satisfied by `VALID` and `SAFE_FALLBACK` as
    concrete successes and the five specific values below collectively
    representing every concrete "not valid" reason, exactly mirroring how
    `GenerationOutcome`/`RTEPAssemblyOutcome` have no generic catch-all
    failure member either.
    """

    VALID = "VALID"
    SAFE_FALLBACK = "SAFE_FALLBACK"
    INVALID_VALIDATION_INPUT = "INVALID_VALIDATION_INPUT"
    MISSING_EVIDENCE = "MISSING_EVIDENCE"
    INSUFFICIENT_EVIDENCE = "INSUFFICIENT_EVIDENCE"
    INVALID_CANDIDATE = "INVALID_CANDIDATE"
    VALIDATION_FAILURE = "VALIDATION_FAILURE"


class ValidationInput(BaseModel):
    """Explicit input required to attempt validation of a `CandidateResponse`.

    `rtep` is `None` to represent "no authoritative RTEP/evidence context
    is available" (spec section 8.2 / `MISSING_EVIDENCE`) — Validation
    never retrieves one itself. `candidate_response` is required (not
    `Optional`): a missing candidate is a missing-required-input case
    (spec section 8.1), not the narrower "candidate present but malformed"
    case (section 8.4).
    """

    model_config = ConfigDict(frozen=True)

    candidate_response: CandidateResponse
    rtep: RuntimeEvidencePackage | None
    validation_policy_version: str = Field(min_length=1)


class ValidationResult(BaseModel):
    """The atomic result of one validation attempt (spec section 10).

    Every outcome carries whatever traceability identifiers are available
    from `candidate_response` (spec section 12) — never fabricated when
    absent (e.g. when the input itself was invalid and no candidate could
    be inspected at all).
    """

    model_config = ConfigDict(frozen=True)

    outcome: CandidateValidationOutcome
    validation_id: str = Field(min_length=1)
    validation_timestamp: datetime
    validation_policy_version: str | None = None
    findings: tuple[str, ...] = Field(default_factory=tuple)

    # Traceability identifiers (spec section 12), sourced from the
    # CandidateResponse this result evaluates — never fabricated.
    candidate_response_id: str | None = None
    integration_id: str | None = None
    retrieval_id: str | None = None
    navigation_context_id: str | None = None
    evidence_package_id: str | None = None

    message: str | None = None
