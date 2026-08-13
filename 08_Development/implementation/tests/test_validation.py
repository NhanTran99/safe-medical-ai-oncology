"""Tests for the Task #008 Validation boundary (`validate_candidate_response`)."""

import inspect
from datetime import UTC, datetime

import pytest
from pydantic import ValidationError

from safe_medical_ai.evidence import EvidenceItem, EvidenceItemProvenance, RuntimeEvidenceMetadata, RuntimeEvidencePackage
from safe_medical_ai.generation import CandidateResponse
from safe_medical_ai.integration import EvidenceState
from safe_medical_ai.retrieval import ArtifactType
from safe_medical_ai.validation import CandidateValidationOutcome, ValidationInput, ValidationResult, validate_candidate_response
from safe_medical_ai.validation import validation as validation_module
from safe_medical_ai.validation import models as validation_models_module


# --- fixtures ------------------------------------------------------------------


def _metadata(retrieval_id: str = "RID-1") -> RuntimeEvidenceMetadata:
    return RuntimeEvidenceMetadata(
        evidence_package_id="EP-1",
        retrieval_id=retrieval_id,
        navigation_context_id="NAV-1",
        retrieval_policy_version="1.0",
        knowledge_base_version="1.0",
        generation_timestamp=datetime.now(UTC),
    )


def _evidence_item(suffix: str) -> EvidenceItem:
    return EvidenceItem(
        population_id="PP-0001",
        artifact_type=ArtifactType.CKO,
        source_path=f"03_Clinical_Knowledge/population/population_packages/PP-0001/01_CKO-{suffix}.md",
        title=f"title-{suffix}",
        provenance=EvidenceItemProvenance(
            knowledge_object_id=f"KO-{suffix}",
            knowledge_passport_id=f"KP-{suffix}",
            source_id=f"SRC-{suffix}",
            guideline_version=f"v{suffix}.0",
        ),
    )


def _rtep(evidence: tuple[EvidenceItem, ...] = ()) -> RuntimeEvidencePackage:
    return RuntimeEvidencePackage(metadata=_metadata(), evidence=evidence)


def _candidate(evidence_state: EvidenceState = EvidenceState.HAS_EVIDENCE, **overrides) -> CandidateResponse:
    fields = {
        "candidate_response_id": "CR-1",
        "generation_timestamp": datetime.now(UTC),
        "content": "some generated candidate text",
        "evidence_state": evidence_state,
        "provider_name": "FakeProvider",
        "integration_id": "INT-1",
        "retrieval_id": "RID-1",
        "navigation_context_id": "NAV-1",
        "evidence_package_id": "EP-1",
    }
    fields.update(overrides)
    return CandidateResponse(**fields)


_UNSET = object()


def _input(candidate: CandidateResponse | None = None, rtep=_UNSET, **overrides) -> ValidationInput:
    if candidate is None:
        candidate = _candidate()
    if rtep is _UNSET:
        rtep = _rtep((_evidence_item("a"), _evidence_item("b")))
    fields = {
        "candidate_response": candidate,
        "rtep": rtep,
        "validation_policy_version": "1.0",
    }
    fields.update(overrides)
    return ValidationInput(**fields)


# --- success: VALID --------------------------------------------------------------


def test_valid_candidate_with_evidence_backed_rtep_is_valid():
    validation_input = _input()
    result = validate_candidate_response(validation_input)

    assert result.outcome == CandidateValidationOutcome.VALID
    assert result.findings == ()
    assert result.message is None


def test_valid_result_carries_traceability_from_candidate():
    candidate = _candidate()
    validation_input = _input(candidate=candidate)

    result = validate_candidate_response(validation_input)

    assert result.candidate_response_id == candidate.candidate_response_id
    assert result.integration_id == candidate.integration_id
    assert result.retrieval_id == candidate.retrieval_id
    assert result.navigation_context_id == candidate.navigation_context_id
    assert result.evidence_package_id == candidate.evidence_package_id
    assert result.validation_policy_version == validation_input.validation_policy_version
    assert result.validation_id
    assert isinstance(result.validation_timestamp, datetime)


# --- evidence states: MISSING_EVIDENCE / INSUFFICIENT_EVIDENCE -------------------


def test_none_rtep_produces_missing_evidence():
    validation_input = _input(rtep=None)

    result = validate_candidate_response(validation_input)

    assert result.outcome == CandidateValidationOutcome.MISSING_EVIDENCE
    assert result.findings


def test_has_evidence_candidate_with_empty_rtep_produces_insufficient_evidence():
    candidate = _candidate(evidence_state=EvidenceState.HAS_EVIDENCE)
    validation_input = _input(candidate=candidate, rtep=_rtep(()))

    result = validate_candidate_response(validation_input)

    assert result.outcome == CandidateValidationOutcome.INSUFFICIENT_EVIDENCE
    assert result.findings


def test_missing_evidence_takes_precedence_over_insufficient_evidence():
    # rtep is None (missing), never reaches the HAS_EVIDENCE/zero-items check.
    validation_input = _input(rtep=None)

    result = validate_candidate_response(validation_input)

    assert result.outcome == CandidateValidationOutcome.MISSING_EVIDENCE


# --- candidate states: SAFE_FALLBACK / INVALID_CANDIDATE -------------------------


def test_empty_evidence_state_candidate_produces_safe_fallback():
    candidate = _candidate(evidence_state=EvidenceState.EMPTY)
    validation_input = _input(candidate=candidate, rtep=_rtep(()))

    result = validate_candidate_response(validation_input)

    assert result.outcome == CandidateValidationOutcome.SAFE_FALLBACK
    assert result.findings


def test_safe_fallback_does_not_produce_a_clinical_answer_message():
    # SAFE_FALLBACK is a semantic pass-through state, not a re-adjudication:
    # this validate call does not invent/alter clinical content of its own.
    candidate = _candidate(evidence_state=EvidenceState.EMPTY, content="No governed evidence was retrieved.")
    validation_input = _input(candidate=candidate, rtep=_rtep(()))

    result = validate_candidate_response(validation_input)

    assert result.outcome == CandidateValidationOutcome.SAFE_FALLBACK
    # ValidationResult never carries/re-derives clinical content of its own.
    assert not hasattr(result, "content")


def test_blank_candidate_content_produces_invalid_candidate_via_model_construct():
    # Defensive-only: CandidateResponse.content has a locked min_length=1
    # constraint, so this state is not reachable through the typed
    # construction API — model_construct() bypasses validation to exercise
    # the defensive branch directly.
    broken_candidate = CandidateResponse.model_construct(
        candidate_response_id="CR-1",
        generation_timestamp=datetime.now(UTC),
        content="   ",
        evidence_state=EvidenceState.HAS_EVIDENCE,
        provider_name="FakeProvider",
        integration_id="INT-1",
        retrieval_id="RID-1",
        navigation_context_id="NAV-1",
        evidence_package_id="EP-1",
    )
    validation_input = _input(candidate=broken_candidate)

    result = validate_candidate_response(validation_input)

    assert result.outcome == CandidateValidationOutcome.INVALID_CANDIDATE


# --- invalid input: INVALID_VALIDATION_INPUT --------------------------------------


def test_none_validation_input_produces_invalid_validation_input():
    result = validate_candidate_response(None)

    assert result.outcome == CandidateValidationOutcome.INVALID_VALIDATION_INPUT
    assert result.candidate_response_id is None


def test_missing_candidate_response_via_model_construct_produces_invalid_validation_input():
    # Defensive-only: ValidationInput.candidate_response is required, so
    # this is not reachable through the typed construction API.
    broken_input = ValidationInput.model_construct(
        candidate_response=None, rtep=None, validation_policy_version="1.0"
    )

    result = validate_candidate_response(broken_input)

    assert result.outcome == CandidateValidationOutcome.INVALID_VALIDATION_INPUT


def test_invalid_validation_input_produces_no_traceability_identifiers():
    result = validate_candidate_response(None)

    assert result.candidate_response_id is None
    assert result.integration_id is None
    assert result.retrieval_id is None
    assert result.navigation_context_id is None
    assert result.evidence_package_id is None


# --- technical failure: VALIDATION_FAILURE ----------------------------------------


def test_unexpected_internal_exception_produces_validation_failure_not_a_crash(monkeypatch):
    def _broken_evaluate(_validation_input):
        raise RuntimeError("simulated unexpected internal error")

    monkeypatch.setattr(validation_module, "_evaluate", _broken_evaluate)

    validation_input = _input()
    result = validate_candidate_response(validation_input)

    assert result.outcome == CandidateValidationOutcome.VALIDATION_FAILURE
    assert result.candidate_response_id == validation_input.candidate_response.candidate_response_id
    assert result.message is not None


def test_validation_failure_is_never_silently_converted_to_valid(monkeypatch):
    def _broken_evaluate(_validation_input):
        raise ValueError("boom")

    monkeypatch.setattr(validation_module, "_evaluate", _broken_evaluate)

    result = validate_candidate_response(_input())

    assert result.outcome != CandidateValidationOutcome.VALID
    assert result.outcome == CandidateValidationOutcome.VALIDATION_FAILURE


# --- atomicity ----------------------------------------------------------------------


@pytest.mark.parametrize(
    "validation_input_factory",
    [
        lambda: _input(),
        lambda: _input(rtep=None),
        lambda: _input(candidate=_candidate(evidence_state=EvidenceState.EMPTY), rtep=_rtep(())),
        lambda: _input(candidate=_candidate(evidence_state=EvidenceState.HAS_EVIDENCE), rtep=_rtep(())),
    ],
)
def test_every_call_returns_exactly_one_authoritative_outcome(validation_input_factory):
    result = validate_candidate_response(validation_input_factory())

    assert isinstance(result, ValidationResult)
    assert isinstance(result.outcome, CandidateValidationOutcome)


def test_no_partial_or_hidden_approval_state_exists():
    # ValidationResult has no field representing a partial/graduated
    # approval state distinct from `outcome` — every result is exactly one
    # of the seven controlled CandidateValidationOutcome values.
    assert set(ValidationResult.model_fields) == {
        "outcome",
        "validation_id",
        "validation_timestamp",
        "validation_policy_version",
        "findings",
        "candidate_response_id",
        "integration_id",
        "retrieval_id",
        "navigation_context_id",
        "evidence_package_id",
        "message",
    }


# --- determinism ----------------------------------------------------------------------


def test_repeated_calls_with_equivalent_input_produce_equivalent_outcome():
    validation_input = _input()

    first = validate_candidate_response(validation_input)
    second = validate_candidate_response(validation_input)

    assert first.outcome == second.outcome == CandidateValidationOutcome.VALID
    assert first.candidate_response_id == second.candidate_response_id
    assert first.findings == second.findings
    # validation_id/validation_timestamp are legitimately runtime-generated
    # identity/timestamp fields and may differ between calls.
    assert isinstance(first.validation_id, str)
    assert isinstance(second.validation_id, str)


def test_repeated_calls_for_safe_fallback_produce_equivalent_outcome():
    candidate = _candidate(evidence_state=EvidenceState.EMPTY)
    validation_input = _input(candidate=candidate, rtep=_rtep(()))

    first = validate_candidate_response(validation_input)
    second = validate_candidate_response(validation_input)

    assert first.outcome == second.outcome == CandidateValidationOutcome.SAFE_FALLBACK


# --- immutability ----------------------------------------------------------------------


def test_validate_candidate_response_does_not_mutate_candidate_or_rtep():
    candidate = _candidate()
    rtep = _rtep((_evidence_item("a"),))
    validation_input = _input(candidate=candidate, rtep=rtep)

    validate_candidate_response(validation_input)

    with pytest.raises(ValidationError):
        candidate.content = "MUTATED"
    with pytest.raises(ValidationError):
        rtep.evidence[0].title = "MUTATED"
    with pytest.raises(ValidationError):
        validation_input.validation_policy_version = "MUTATED"


# --- boundary protection: no retrieval/repository/filesystem access (static) ------


def test_validation_module_does_not_access_repository_or_retrieval():
    source = inspect.getsource(validation_module)
    assert "RepositorySource(" not in source
    assert ".list_artifacts(" not in source
    assert "RetrievalService(" not in source
    assert ".retrieve(" not in source


def test_validation_module_does_not_touch_filesystem_or_network():
    source = inspect.getsource(validation_module)
    assert "open(" not in source
    assert "Path(" not in source
    assert "pathlib" not in source
    assert "requests" not in source
    assert "urllib" not in source


@pytest.mark.parametrize(
    "forbidden_token",
    [
        "openai",
        "anthropic",
        "sentence_transformers",
        "faiss",
        "chromadb",
        "pinecone",
        "import torch",
    ],
)
def test_validation_does_not_reference_llm_vendor_libraries(forbidden_token):
    source = inspect.getsource(validation_module) + inspect.getsource(validation_models_module)
    assert forbidden_token.lower() not in source.lower()


def test_validation_does_not_import_llm_adapter_or_call_generate():
    # Check the actual module namespace, not raw source text: the module's
    # own docstring legitimately *mentions* LLMAdapter/.generate( in prose
    # (explaining what Validation deliberately does not do), which would
    # false-positive a plain substring search — same pattern as Task #007's
    # ValidationOutcome docstring-mention fix.
    assert "LLMAdapter" not in dir(validation_module)
    assert "LLMAdapter" not in dir(validation_models_module)
    source = inspect.getsource(validation_module)
    assert "import llm" not in source.lower()
    assert "from ..llm" not in source


def test_validation_does_not_reference_clinical_reasoning_functions():
    source = inspect.getsource(validation_module)
    for forbidden in ("diagnose", "recommend_treatment", "clinical_reasoning"):
        assert forbidden not in source.lower()


# --- regression: full outcome vocabulary is reachable ------------------------------


def test_all_seven_outcomes_are_reachable_through_the_public_entry_point(monkeypatch):
    reached = set()

    reached.add(validate_candidate_response(None).outcome)
    reached.add(validate_candidate_response(_input(rtep=None)).outcome)
    reached.add(
        validate_candidate_response(
            _input(candidate=_candidate(evidence_state=EvidenceState.HAS_EVIDENCE), rtep=_rtep(()))
        ).outcome
    )
    reached.add(
        validate_candidate_response(
            _input(candidate=_candidate(evidence_state=EvidenceState.EMPTY), rtep=_rtep(()))
        ).outcome
    )
    reached.add(validate_candidate_response(_input()).outcome)

    broken_candidate = CandidateResponse.model_construct(
        candidate_response_id="CR-1",
        generation_timestamp=datetime.now(UTC),
        content="",
        evidence_state=EvidenceState.HAS_EVIDENCE,
        provider_name="FakeProvider",
        integration_id="INT-1",
        retrieval_id="RID-1",
        navigation_context_id="NAV-1",
        evidence_package_id="EP-1",
    )
    reached.add(validate_candidate_response(_input(candidate=broken_candidate)).outcome)

    def _broken_evaluate(_validation_input):
        raise RuntimeError("simulated")

    monkeypatch.setattr(validation_module, "_evaluate", _broken_evaluate)
    reached.add(validate_candidate_response(_input()).outcome)

    assert reached == set(CandidateValidationOutcome)
