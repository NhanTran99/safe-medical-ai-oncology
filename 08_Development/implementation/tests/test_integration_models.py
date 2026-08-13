"""Contract tests for the Task #006 Runtime Integration models."""

from datetime import UTC, datetime

import pytest
from pydantic import ValidationError

from safe_medical_ai.evidence import RuntimeEvidenceMetadata, RuntimeEvidencePackage
from safe_medical_ai.integration import (
    EvidenceState,
    GenerationContext,
    RuntimeConstraints,
    RuntimeIntegrationInput,
    RuntimeIntegrationOutcome,
    RuntimeIntegrationResult,
)
from safe_medical_ai.models.output_contract import NavigationContextPlaceholder, ValidationOutcome
from safe_medical_ai.retrieval import RetrievalOutcome


def _metadata() -> RuntimeEvidenceMetadata:
    return RuntimeEvidenceMetadata(
        evidence_package_id="EP-1",
        retrieval_id="RID-1",
        navigation_context_id="NAV-1",
        retrieval_policy_version="1.0",
        knowledge_base_version="1.0",
        generation_timestamp=datetime.now(UTC),
    )


def _rtep() -> RuntimeEvidencePackage:
    return RuntimeEvidencePackage(metadata=_metadata(), evidence=())


def _generation_context() -> GenerationContext:
    return GenerationContext(
        integration_id="INT-1",
        integration_timestamp=datetime.now(UTC),
        request_text="what is gastric cancer?",
        navigation_context=NavigationContextPlaceholder(),
        rtep=_rtep(),
        runtime_constraints=RuntimeConstraints(),
        evidence_state=EvidenceState.EMPTY,
    )


# --- controlled vocabulary --------------------------------------------------


def test_runtime_integration_outcome_vocabulary():
    assert {o.value for o in RuntimeIntegrationOutcome} == {
        "INTEGRATED",
        "EMPTY_EVIDENCE",
        "INVALID_INPUT",
        "MISSING_RTEP",
        "INTEGRATION_FAILURE",
    }


def test_runtime_integration_outcome_is_distinct_from_other_vocabularies():
    from safe_medical_ai.evidence import RTEPAssemblyOutcome

    assert set(RuntimeIntegrationOutcome.__members__) & set(RetrievalOutcome.__members__) == set()
    assert set(RuntimeIntegrationOutcome.__members__) & set(RTEPAssemblyOutcome.__members__) == set()
    assert set(RuntimeIntegrationOutcome.__members__) & set(ValidationOutcome.__members__) == set()


def test_evidence_state_vocabulary():
    assert {s.value for s in EvidenceState} == {"HAS_EVIDENCE", "EMPTY"}


# --- required fields ---------------------------------------------------------


def test_runtime_integration_input_requires_non_blank_request_text():
    with pytest.raises(ValidationError):
        RuntimeIntegrationInput(
            request_text="",
            navigation_context=NavigationContextPlaceholder(),
            rtep=None,
            runtime_constraints=RuntimeConstraints(),
        )


def test_runtime_integration_input_allows_none_rtep():
    integration_input = RuntimeIntegrationInput(
        request_text="q",
        navigation_context=NavigationContextPlaceholder(),
        rtep=None,
        runtime_constraints=RuntimeConstraints(),
    )
    assert integration_input.rtep is None


def test_runtime_integration_input_requires_navigation_context():
    with pytest.raises(ValidationError):
        RuntimeIntegrationInput(request_text="q", rtep=None, runtime_constraints=RuntimeConstraints())


def test_runtime_integration_input_requires_runtime_constraints():
    with pytest.raises(ValidationError):
        RuntimeIntegrationInput(request_text="q", navigation_context=NavigationContextPlaceholder(), rtep=None)


def test_generation_context_requires_all_fields():
    with pytest.raises(ValidationError):
        GenerationContext(
            integration_id="INT-1",
            integration_timestamp=datetime.now(UTC),
            request_text="q",
            navigation_context=NavigationContextPlaceholder(),
            # rtep intentionally omitted
            runtime_constraints=RuntimeConstraints(),
            evidence_state=EvidenceState.EMPTY,
        )


def test_generation_context_requires_non_blank_integration_id():
    with pytest.raises(ValidationError):
        GenerationContext(
            integration_id="",
            integration_timestamp=datetime.now(UTC),
            request_text="q",
            navigation_context=NavigationContextPlaceholder(),
            rtep=_rtep(),
            runtime_constraints=RuntimeConstraints(),
            evidence_state=EvidenceState.EMPTY,
        )


# --- immutability ------------------------------------------------------------


def test_runtime_integration_input_is_frozen():
    integration_input = RuntimeIntegrationInput(
        request_text="q",
        navigation_context=NavigationContextPlaceholder(),
        rtep=None,
        runtime_constraints=RuntimeConstraints(),
    )
    with pytest.raises(ValidationError):
        integration_input.request_text = "MUTATED"


def test_runtime_constraints_is_frozen():
    constraints = RuntimeConstraints()
    # A frozen model rejects any attribute assignment, even for a name that
    # isn't a declared field — Pydantic checks frozen status first.
    with pytest.raises(ValidationError):
        constraints.anything = "x"


def test_generation_context_is_frozen():
    context = _generation_context()
    with pytest.raises(ValidationError):
        context.request_text = "MUTATED"


def test_runtime_integration_result_is_frozen():
    result = RuntimeIntegrationResult(outcome=RuntimeIntegrationOutcome.INVALID_INPUT, context=None)
    with pytest.raises(ValidationError):
        result.outcome = RuntimeIntegrationOutcome.INTEGRATED


# --- typed result semantics ---------------------------------------------------


def test_result_with_non_success_outcome_can_still_type_check_with_none_context():
    result = RuntimeIntegrationResult(outcome=RuntimeIntegrationOutcome.MISSING_RTEP)
    assert result.context is None
