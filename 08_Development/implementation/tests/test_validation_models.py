"""Contract tests for the Task #008 Validation models."""

from datetime import UTC, datetime

import pytest
from pydantic import ValidationError

from safe_medical_ai.evidence import RTEPAssemblyOutcome, RuntimeEvidenceMetadata, RuntimeEvidencePackage
from safe_medical_ai.generation import CandidateResponse, GenerationOutcome
from safe_medical_ai.integration import EvidenceState, RuntimeIntegrationOutcome
from safe_medical_ai.models.output_contract import ValidationOutcome
from safe_medical_ai.retrieval import RetrievalOutcome
from safe_medical_ai.validation import CandidateValidationOutcome, ValidationInput, ValidationResult


def _candidate(**overrides) -> CandidateResponse:
    fields = {
        "candidate_response_id": "CR-1",
        "generation_timestamp": datetime.now(UTC),
        "content": "some generated text",
        "evidence_state": EvidenceState.HAS_EVIDENCE,
        "provider_name": "FakeProvider",
        "integration_id": "INT-1",
        "retrieval_id": "RID-1",
        "navigation_context_id": "NAV-1",
        "evidence_package_id": "EP-1",
    }
    fields.update(overrides)
    return CandidateResponse(**fields)


def _rtep(evidence=()) -> RuntimeEvidencePackage:
    metadata = RuntimeEvidenceMetadata(
        evidence_package_id="EP-1",
        retrieval_id="RID-1",
        navigation_context_id="NAV-1",
        retrieval_policy_version="1.0",
        knowledge_base_version="1.0",
        generation_timestamp=datetime.now(UTC),
    )
    return RuntimeEvidencePackage(metadata=metadata, evidence=evidence)


def _validation_result(**overrides) -> ValidationResult:
    fields = {
        "outcome": CandidateValidationOutcome.VALID,
        "validation_id": "VAL-1",
        "validation_timestamp": datetime.now(UTC),
    }
    fields.update(overrides)
    return ValidationResult(**fields)


# --- controlled vocabulary --------------------------------------------------


def test_candidate_validation_outcome_vocabulary():
    assert {o.value for o in CandidateValidationOutcome} == {
        "VALID",
        "SAFE_FALLBACK",
        "INVALID_VALIDATION_INPUT",
        "MISSING_EVIDENCE",
        "INSUFFICIENT_EVIDENCE",
        "INVALID_CANDIDATE",
        "VALIDATION_FAILURE",
    }


def test_candidate_validation_outcome_is_disjoint_from_upstream_pipeline_outcomes():
    assert set(CandidateValidationOutcome.__members__) & set(RetrievalOutcome.__members__) == set()
    assert set(CandidateValidationOutcome.__members__) & set(RTEPAssemblyOutcome.__members__) == set()
    assert set(CandidateValidationOutcome.__members__) & set(RuntimeIntegrationOutcome.__members__) == set()
    assert set(CandidateValidationOutcome.__members__) & set(GenerationOutcome.__members__) == set()


def test_candidate_validation_outcome_shares_only_safe_fallback_with_validation_outcome():
    # Intentional exception (spec section 7): SAFE_FALLBACK is shared with
    # OUTPUT_CONTRACT's ValidationOutcome by design; nothing else overlaps.
    assert set(CandidateValidationOutcome.__members__) & set(ValidationOutcome.__members__) == {"SAFE_FALLBACK"}


# --- required fields ---------------------------------------------------------


def test_validation_input_requires_candidate_response():
    with pytest.raises(ValidationError):
        ValidationInput(rtep=None, validation_policy_version="1.0")


def test_validation_input_allows_none_rtep():
    validation_input = ValidationInput(
        candidate_response=_candidate(), rtep=None, validation_policy_version="1.0"
    )
    assert validation_input.rtep is None


def test_validation_input_requires_non_blank_policy_version():
    with pytest.raises(ValidationError):
        ValidationInput(candidate_response=_candidate(), rtep=None, validation_policy_version="")


def test_validation_result_requires_non_blank_validation_id():
    with pytest.raises(ValidationError):
        ValidationResult(
            outcome=CandidateValidationOutcome.VALID, validation_id="", validation_timestamp=datetime.now(UTC)
        )


def test_validation_result_traceability_fields_are_optional():
    result = _validation_result()
    assert result.candidate_response_id is None
    assert result.integration_id is None


# --- immutability ------------------------------------------------------------


def test_validation_input_is_frozen():
    validation_input = ValidationInput(
        candidate_response=_candidate(), rtep=None, validation_policy_version="1.0"
    )
    with pytest.raises(ValidationError):
        validation_input.validation_policy_version = "MUTATED"


def test_validation_result_is_frozen():
    result = _validation_result()
    with pytest.raises(ValidationError):
        result.outcome = CandidateValidationOutcome.SAFE_FALLBACK
