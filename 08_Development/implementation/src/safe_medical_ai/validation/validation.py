"""Validation boundary — Task #008.

Implements the locked B1-B4 behavioral requirements as one explicit,
deterministic entry point: `validate_candidate_response`.

This module:
- accepts a `ValidationInput` (`CandidateResponse` + authoritative
  RTEP/evidence + validation policy/version) and performs a local,
  read-only evaluation only;
- never constructs a `RepositorySource`, calls `RetrievalService`, or
  otherwise re-retrieves;
- never touches the filesystem or the network;
- never reranks, reorders, deduplicates, enriches, or repairs provenance;
- never calls an `LLMAdapter` provider, retries/regenerates a response, or
  performs clinical reasoning, diagnosis, treatment recommendation, or
  patient-specific safety adjudication;
- never mutates `CandidateResponse`, its upstream RTEP, evidence items,
  provenance, or generation/integration metadata.

`VALID` means only "this CandidateResponse satisfies the locked Validation
contract" — never that a diagnosis is correct, a treatment is appropriate,
or clinical/final approval has occurred (spec section 15).
"""

from __future__ import annotations

import logging
import uuid
from datetime import UTC, datetime

from ..integration import EvidenceState
from .models import CandidateValidationOutcome, ValidationInput, ValidationResult

logger = logging.getLogger(__name__)


def validate_candidate_response(validation_input: ValidationInput | None) -> ValidationResult:
    """Evaluate a `CandidateResponse` against the locked Validation contract.

    Atomic: each call returns exactly one authoritative `ValidationResult`
    (spec section 10) — never a partially-approved or hidden-failure state.
    Deterministic precedence (spec section 9): invalid input, then missing/
    insufficient evidence, then invalid candidate, then mechanism failure,
    then the semantic VALID/SAFE_FALLBACK decision.
    """
    if validation_input is None or validation_input.candidate_response is None:
        # A missing ValidationInput, or a defensively-checked missing
        # candidate_response (not reachable through the typed API, since
        # ValidationInput.candidate_response is a required field — see
        # test_validation.py's model_construct-based test), are both
        # "malformed/missing required validation input" (spec section 8.1).
        logger.warning("Validation failed: no ValidationInput/candidate_response supplied")
        return ValidationResult(
            outcome=CandidateValidationOutcome.INVALID_VALIDATION_INPUT,
            validation_id=uuid.uuid4().hex,
            validation_timestamp=datetime.now(UTC),
            findings=("no ValidationInput or candidate_response was supplied",),
            message="no validation performed: required validation input was not supplied",
        )

    try:
        return _evaluate(validation_input)
    except Exception:
        # Controlled unexpected/internal failure (spec section 8.5): the
        # validation mechanism itself failed technically. Never converted
        # to VALID.
        logger.exception("Validation failed: unexpected internal failure")
        candidate = validation_input.candidate_response
        return ValidationResult(
            outcome=CandidateValidationOutcome.VALIDATION_FAILURE,
            validation_id=uuid.uuid4().hex,
            validation_timestamp=datetime.now(UTC),
            validation_policy_version=validation_input.validation_policy_version,
            findings=("the validation mechanism failed technically",),
            candidate_response_id=candidate.candidate_response_id,
            integration_id=candidate.integration_id,
            retrieval_id=candidate.retrieval_id,
            navigation_context_id=candidate.navigation_context_id,
            evidence_package_id=candidate.evidence_package_id,
            message="no VALID/SAFE_FALLBACK outcome: validation mechanism failure",
        )


def _evaluate(validation_input: ValidationInput) -> ValidationResult:
    candidate = validation_input.candidate_response
    trace_ids = {
        "candidate_response_id": candidate.candidate_response_id,
        "integration_id": candidate.integration_id,
        "retrieval_id": candidate.retrieval_id,
        "navigation_context_id": candidate.navigation_context_id,
        "evidence_package_id": candidate.evidence_package_id,
    }

    def _result(outcome: CandidateValidationOutcome, findings: tuple[str, ...], message: str | None) -> ValidationResult:
        return ValidationResult(
            outcome=outcome,
            validation_id=uuid.uuid4().hex,
            validation_timestamp=datetime.now(UTC),
            validation_policy_version=validation_input.validation_policy_version,
            findings=findings,
            message=message,
            **trace_ids,
        )

    rtep = validation_input.rtep

    if rtep is None:
        logger.info("Validation: MISSING_EVIDENCE candidate_response_id=%s", candidate.candidate_response_id)
        return _result(
            CandidateValidationOutcome.MISSING_EVIDENCE,
            ("no authoritative RTEP/evidence context was supplied",),
            "no VALID/SAFE_FALLBACK outcome: evidence context is missing",
        )

    if candidate.evidence_state is EvidenceState.HAS_EVIDENCE and len(rtep.evidence) == 0:
        # The candidate claims to be evidence-backed, but the authoritative
        # RTEP it is being validated against carries no evidence items —
        # a genuine inconsistency, not a graduated sufficiency judgment
        # (no clinical/content adjudication of *which* evidence is needed).
        logger.info("Validation: INSUFFICIENT_EVIDENCE candidate_response_id=%s", candidate.candidate_response_id)
        return _result(
            CandidateValidationOutcome.INSUFFICIENT_EVIDENCE,
            ("candidate_response.evidence_state is HAS_EVIDENCE but the supplied RTEP has zero evidence items",),
            "no VALID/SAFE_FALLBACK outcome: RTEP does not satisfy the evidence prerequisite",
        )

    if not candidate.content or not candidate.content.strip():
        # Defensive: CandidateResponse.content already has a non-blank
        # Pydantic constraint, so this is not reachable through the typed
        # API — see test_validation.py's model_construct-based test.
        logger.warning("Validation: INVALID_CANDIDATE candidate_response_id=%s", candidate.candidate_response_id)
        return _result(
            CandidateValidationOutcome.INVALID_CANDIDATE,
            ("candidate_response.content is blank/malformed",),
            "no VALID/SAFE_FALLBACK outcome: candidate_response failed structural validation",
        )

    if candidate.evidence_state is EvidenceState.EMPTY:
        # Recognizes and passes through Generation's own locked
        # EMPTY_EVIDENCE policy response (spec section 8.6/8.7) as the safe
        # fallback state it already is — Validation does not re-adjudicate
        # or generate a clinical alternative for it.
        logger.info("Validation: SAFE_FALLBACK candidate_response_id=%s", candidate.candidate_response_id)
        return _result(
            CandidateValidationOutcome.SAFE_FALLBACK,
            ("candidate_response.evidence_state is EMPTY: candidate cannot be used as a normal answer",),
            None,
        )

    logger.info("Validation: VALID candidate_response_id=%s", candidate.candidate_response_id)
    return _result(CandidateValidationOutcome.VALID, (), None)
