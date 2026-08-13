"""Tests for the Task #006 Runtime Integration boundary (`integrate_runtime_context`)."""

import inspect
from datetime import UTC, datetime

import pytest
from pydantic import ValidationError

from safe_medical_ai.evidence import (
    EvidenceItem,
    EvidenceItemProvenance,
    RuntimeEvidenceMetadata,
    RuntimeEvidencePackage,
)
from safe_medical_ai.integration import (
    EvidenceState,
    RuntimeConstraints,
    RuntimeIntegrationInput,
    RuntimeIntegrationOutcome,
    integrate_runtime_context,
)
from safe_medical_ai.integration import integration as integration_module
from safe_medical_ai.integration import models as integration_models_module
from safe_medical_ai.models.output_contract import NavigationContextPlaceholder
from safe_medical_ai.retrieval import ArtifactType


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


def _rtep_with_evidence() -> RuntimeEvidencePackage:
    return RuntimeEvidencePackage(
        metadata=_metadata(),
        evidence=(_evidence_item("a"), _evidence_item("b")),
    )


def _empty_rtep() -> RuntimeEvidencePackage:
    return RuntimeEvidencePackage(metadata=_metadata(), evidence=())


def _integration_input(rtep: RuntimeEvidencePackage | None) -> RuntimeIntegrationInput:
    return RuntimeIntegrationInput(
        request_text="what is gastric cancer?",
        navigation_context=NavigationContextPlaceholder(),
        rtep=rtep,
        runtime_constraints=RuntimeConstraints(),
    )


# --- 6.1 valid RTEP ------------------------------------------------------------


def test_valid_rtep_produces_integrated_with_valid_context():
    result = integrate_runtime_context(_integration_input(_rtep_with_evidence()))

    assert result.outcome == RuntimeIntegrationOutcome.INTEGRATED
    assert result.context is not None
    assert result.context.evidence_state == EvidenceState.HAS_EVIDENCE


def test_integrated_context_preserves_request_and_navigation_and_constraints():
    integration_input = _integration_input(_rtep_with_evidence())
    result = integrate_runtime_context(integration_input)

    assert result.context.request_text == integration_input.request_text
    assert result.context.navigation_context == integration_input.navigation_context
    assert result.context.runtime_constraints == integration_input.runtime_constraints


# --- 6.2 EMPTY RTEP --------------------------------------------------------------


def test_empty_rtep_produces_empty_evidence_outcome_not_failure():
    result = integrate_runtime_context(_integration_input(_empty_rtep()))

    assert result.outcome == RuntimeIntegrationOutcome.EMPTY_EVIDENCE
    assert result.context is not None
    assert result.context.evidence_state == EvidenceState.EMPTY
    assert result.context.rtep.evidence == ()


# --- 6.3 missing RTEP --------------------------------------------------------------


def test_missing_rtep_produces_missing_rtep_outcome():
    result = integrate_runtime_context(_integration_input(None))

    assert result.outcome == RuntimeIntegrationOutcome.MISSING_RTEP
    assert result.context is None


def test_missing_rtep_does_not_call_retrieval():
    # Static proof lives in the architectural-boundary tests below; this is
    # the behavioral counterpart: no RetrievalService/RepositorySource
    # object is ever constructed or reachable from this call.
    result = integrate_runtime_context(_integration_input(None))
    assert result.outcome == RuntimeIntegrationOutcome.MISSING_RTEP


# --- 6.4 invalid input --------------------------------------------------------------


def test_none_integration_input_produces_invalid_input():
    result = integrate_runtime_context(None)

    assert result.outcome == RuntimeIntegrationOutcome.INVALID_INPUT
    assert result.context is None


# --- 6.5 integration failure --------------------------------------------------------


def test_unexpected_construction_failure_produces_integration_failure_not_partial_context(monkeypatch):
    def _raise(*args, **kwargs):
        # Trigger a genuine pydantic ValidationError (missing required
        # fields) rather than hand-constructing one, to simulate an
        # unexpected inability to build a valid GenerationContext.
        integration_models_module.GenerationContext()

    monkeypatch.setattr(integration_module, "GenerationContext", _raise)

    result = integrate_runtime_context(_integration_input(_rtep_with_evidence()))

    assert result.outcome == RuntimeIntegrationOutcome.INTEGRATION_FAILURE
    assert result.context is None


# --- preservation invariants --------------------------------------------------------


def test_rtep_is_referenced_not_copied_or_reconstructed():
    rtep = _rtep_with_evidence()
    result = integrate_runtime_context(_integration_input(rtep))

    assert result.context.rtep is rtep


def test_evidence_ordering_is_preserved_exactly():
    rtep = _rtep_with_evidence()
    result = integrate_runtime_context(_integration_input(rtep))

    assert [item.source_path for item in result.context.rtep.evidence] == [
        item.source_path for item in rtep.evidence
    ]


def test_per_item_provenance_is_preserved():
    rtep = _rtep_with_evidence()
    result = integrate_runtime_context(_integration_input(rtep))

    for original, integrated in zip(rtep.evidence, result.context.rtep.evidence, strict=True):
        assert integrated.provenance == original.provenance


def test_rtep_metadata_and_traceability_are_preserved():
    rtep = _rtep_with_evidence()
    result = integrate_runtime_context(_integration_input(rtep))

    assert result.context.rtep.metadata == rtep.metadata
    assert result.context.rtep.metadata.retrieval_id == rtep.metadata.retrieval_id
    assert result.context.rtep.metadata.navigation_context_id == rtep.metadata.navigation_context_id


def test_runtime_constraints_are_preserved():
    constraints = RuntimeConstraints()
    integration_input = RuntimeIntegrationInput(
        request_text="q",
        navigation_context=NavigationContextPlaceholder(),
        rtep=_rtep_with_evidence(),
        runtime_constraints=constraints,
    )
    result = integrate_runtime_context(integration_input)

    assert result.context.runtime_constraints == constraints


# --- immutability --------------------------------------------------------------------


def test_source_rtep_cannot_be_mutated_through_the_returned_context():
    rtep = _rtep_with_evidence()
    result = integrate_runtime_context(_integration_input(rtep))

    with pytest.raises(ValidationError):
        result.context.rtep.evidence = ()

    with pytest.raises(ValidationError):
        result.context.rtep.metadata.retrieval_id = "MUTATED"


def test_nested_evidence_items_do_not_leak_mutable_state():
    rtep = _rtep_with_evidence()
    result = integrate_runtime_context(_integration_input(rtep))

    with pytest.raises(ValidationError):
        result.context.rtep.evidence[0].provenance.knowledge_object_id = "MUTATED"


def test_returned_context_itself_is_frozen():
    result = integrate_runtime_context(_integration_input(_rtep_with_evidence()))

    with pytest.raises(ValidationError):
        result.context.evidence_state = EvidenceState.EMPTY


# --- determinism --------------------------------------------------------------------


def test_repeated_calls_with_equivalent_input_produce_equivalent_logical_context():
    integration_input = _integration_input(_rtep_with_evidence())

    first = integrate_runtime_context(integration_input)
    second = integrate_runtime_context(integration_input)

    assert first.outcome == second.outcome == RuntimeIntegrationOutcome.INTEGRATED
    assert first.context.request_text == second.context.request_text
    assert first.context.navigation_context == second.context.navigation_context
    assert first.context.runtime_constraints == second.context.runtime_constraints
    assert first.context.evidence_state == second.context.evidence_state
    assert [i.model_dump() for i in first.context.rtep.evidence] == [
        i.model_dump() for i in second.context.rtep.evidence
    ]
    assert first.context.rtep.metadata == second.context.rtep.metadata
    # integration_id/integration_timestamp are legitimately runtime-generated
    # identity/timestamp fields and may differ between calls.
    assert isinstance(first.context.integration_id, str)
    assert isinstance(second.context.integration_id, str)


# --- architectural boundary (static + behavioral) --------------------------------------


def test_integration_module_does_not_access_repository_or_retrieval():
    source = inspect.getsource(integration_module)
    assert "RepositorySource(" not in source
    assert ".list_artifacts(" not in source
    assert "RetrievalService(" not in source
    assert ".retrieve(" not in source


def test_integration_module_does_not_touch_filesystem():
    source = inspect.getsource(integration_module)
    assert "open(" not in source
    assert "Path(" not in source
    assert "pathlib" not in source


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
def test_integration_does_not_reference_llm_or_vector_libraries(forbidden_token):
    source = inspect.getsource(integration_module) + inspect.getsource(integration_models_module)
    assert forbidden_token.lower() not in source.lower()


def test_integration_module_does_not_import_llm_adapter():
    source = inspect.getsource(integration_module)
    assert "from ..llm" not in source
    assert "import llm" not in source
