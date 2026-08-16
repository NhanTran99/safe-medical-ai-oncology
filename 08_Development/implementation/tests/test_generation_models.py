"""Contract tests for the Task #007 Generation models."""

from datetime import UTC, datetime

import pytest
from pydantic import ValidationError

from safe_medical_ai.evidence import RTEPAssemblyOutcome
from safe_medical_ai.generation import CandidateResponse, GenerationOutcome, GenerationResult
from safe_medical_ai.integration import EvidenceState, RuntimeIntegrationOutcome
from safe_medical_ai.models.output_contract import ValidationOutcome
from safe_medical_ai.retrieval import RetrievalOutcome


def _candidate_response(**overrides) -> CandidateResponse:
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


# --- controlled vocabulary --------------------------------------------------


def test_generation_outcome_vocabulary():
    assert {o.value for o in GenerationOutcome} == {
        "GENERATED",
        "EMPTY_EVIDENCE_RESPONSE",
        "INVALID_CONTEXT",
        "CONTEXT_MISSING_RTEP",
        "PROVIDER_FAILURE",
        "PROVIDER_TIMEOUT",
        "MALFORMED_PROVIDER_OUTPUT",
        "PARTIAL_GENERATION",
        "INTERNAL_FAILURE",
        "PROMPT_BLOCKED",
    }


def test_generation_outcome_is_distinct_from_every_other_vocabulary():
    assert set(GenerationOutcome.__members__) & set(RetrievalOutcome.__members__) == set()
    assert set(GenerationOutcome.__members__) & set(RTEPAssemblyOutcome.__members__) == set()
    assert set(GenerationOutcome.__members__) & set(RuntimeIntegrationOutcome.__members__) == set()
    assert set(GenerationOutcome.__members__) & set(ValidationOutcome.__members__) == set()


# --- required fields ---------------------------------------------------------


@pytest.mark.parametrize(
    "field",
    ["candidate_response_id", "content", "integration_id", "retrieval_id", "navigation_context_id", "evidence_package_id"],
)
def test_candidate_response_requires_non_blank_fields(field):
    with pytest.raises(ValidationError):
        _candidate_response(**{field: ""})


def test_candidate_response_provider_name_is_optional():
    response = _candidate_response(provider_name=None)
    assert response.provider_name is None


def test_candidate_response_requires_all_fields():
    with pytest.raises(ValidationError):
        CandidateResponse(candidate_response_id="CR-1", generation_timestamp=datetime.now(UTC))


# --- immutability ------------------------------------------------------------


def test_candidate_response_is_frozen():
    response = _candidate_response()
    with pytest.raises(ValidationError):
        response.content = "MUTATED"


def test_generation_result_is_frozen():
    result = GenerationResult(outcome=GenerationOutcome.INVALID_CONTEXT, response=None)
    with pytest.raises(ValidationError):
        result.outcome = GenerationOutcome.GENERATED


# --- typed result semantics ---------------------------------------------------


def test_result_with_failure_outcome_has_no_response():
    result = GenerationResult(outcome=GenerationOutcome.PROVIDER_FAILURE)
    assert result.response is None


def test_result_with_success_outcome_carries_a_response():
    result = GenerationResult(outcome=GenerationOutcome.GENERATED, response=_candidate_response())
    assert result.response is not None
