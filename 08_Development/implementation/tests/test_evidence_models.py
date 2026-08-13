"""Contract tests for the Task #005 RTEP models."""

from datetime import UTC, datetime

import pytest
from pydantic import ValidationError

from safe_medical_ai.evidence import (
    EvidenceItem,
    EvidenceItemProvenance,
    RTEPAssemblyContext,
    RTEPAssemblyOutcome,
    RTEPAssemblyResult,
    RuntimeEvidenceMetadata,
    RuntimeEvidencePackage,
)
from safe_medical_ai.models.output_contract import ValidationOutcome
from safe_medical_ai.retrieval import ArtifactType, RetrievalOutcome


def _provenance(suffix: str = "1") -> EvidenceItemProvenance:
    return EvidenceItemProvenance(
        knowledge_object_id=f"KO-{suffix}",
        knowledge_passport_id=f"KP-{suffix}",
        source_id=f"SRC-{suffix}",
        guideline_version=f"v{suffix}.0",
    )


def _item(suffix: str = "1") -> EvidenceItem:
    return EvidenceItem(
        population_id="PP-0001",
        artifact_type=ArtifactType.CKO,
        source_path=f"03_Clinical_Knowledge/population/population_packages/PP-0001/01_CKO.md",
        title=None,
        provenance=_provenance(suffix),
    )


def _metadata() -> RuntimeEvidenceMetadata:
    return RuntimeEvidenceMetadata(
        evidence_package_id="EP-1",
        retrieval_id="RID-1",
        navigation_context_id="NAV-1",
        retrieval_policy_version="1.0",
        knowledge_base_version="1.0",
        generation_timestamp=datetime.now(UTC),
    )


# --- controlled vocabulary --------------------------------------------------


def test_rtep_assembly_outcome_vocabulary():
    assert {o.value for o in RTEPAssemblyOutcome} == {
        "ASSEMBLED",
        "RETRIEVAL_NOT_FOUND",
        "RETRIEVAL_INVALID_REQUEST",
        "MISSING_METADATA",
        "INVALID_EVIDENCE_ITEM",
        "INCOMPLETE_PROVENANCE",
    }


def test_rtep_assembly_outcome_is_distinct_from_retrieval_and_validation_outcome():
    assert RTEPAssemblyOutcome is not RetrievalOutcome
    assert RTEPAssemblyOutcome is not ValidationOutcome
    assert set(RTEPAssemblyOutcome.__members__) & set(RetrievalOutcome.__members__) == set()
    assert set(RTEPAssemblyOutcome.__members__) & set(ValidationOutcome.__members__) == set()


# --- required metadata / provenance ----------------------------------------


@pytest.mark.parametrize(
    "field", ["knowledge_object_id", "knowledge_passport_id", "source_id", "guideline_version"]
)
def test_evidence_item_provenance_requires_non_blank_fields(field):
    kwargs = {
        "knowledge_object_id": "KO-1",
        "knowledge_passport_id": "KP-1",
        "source_id": "SRC-1",
        "guideline_version": "v1.0",
    }
    kwargs[field] = ""
    with pytest.raises(ValidationError):
        EvidenceItemProvenance(**kwargs)


def test_evidence_item_provenance_missing_field_rejected():
    with pytest.raises(ValidationError):
        EvidenceItemProvenance(knowledge_object_id="KO-1", knowledge_passport_id="KP-1", source_id="SRC-1")


@pytest.mark.parametrize(
    "field", ["retrieval_id", "navigation_context_id", "retrieval_policy_version", "knowledge_base_version"]
)
def test_rtep_assembly_context_requires_non_blank_fields(field):
    kwargs = {
        "retrieval_id": "RID-1",
        "navigation_context_id": "NAV-1",
        "retrieval_policy_version": "1.0",
        "knowledge_base_version": "1.0",
    }
    kwargs[field] = ""
    with pytest.raises(ValidationError):
        RTEPAssemblyContext(**kwargs)


def test_runtime_evidence_metadata_requires_all_minimum_fields():
    with pytest.raises(ValidationError):
        RuntimeEvidenceMetadata(
            evidence_package_id="EP-1",
            retrieval_id="RID-1",
            # navigation_context_id intentionally omitted
            retrieval_policy_version="1.0",
            knowledge_base_version="1.0",
            generation_timestamp=datetime.now(UTC),
        )


# --- immutability (contract-level) ------------------------------------------


def test_evidence_item_provenance_is_frozen():
    provenance = _provenance()
    with pytest.raises(ValidationError):
        provenance.knowledge_object_id = "MUTATED"


def test_evidence_item_is_frozen():
    item = _item()
    with pytest.raises(ValidationError):
        item.title = "MUTATED"


def test_runtime_evidence_metadata_is_frozen():
    metadata = _metadata()
    with pytest.raises(ValidationError):
        metadata.evidence_package_id = "MUTATED"


def test_runtime_evidence_package_is_frozen():
    package = RuntimeEvidencePackage(metadata=_metadata(), evidence=(_item(),))
    with pytest.raises(ValidationError):
        package.metadata = _metadata()


def test_runtime_evidence_package_evidence_is_a_tuple_not_a_list():
    package = RuntimeEvidencePackage(metadata=_metadata(), evidence=(_item(),))
    assert isinstance(package.evidence, tuple)
    # tuples have no in-place mutation method such as .append
    assert not hasattr(package.evidence, "append")


def test_rtep_assembly_result_is_frozen():
    result = RTEPAssemblyResult(outcome=RTEPAssemblyOutcome.ASSEMBLED, package=None)
    with pytest.raises(ValidationError):
        result.outcome = RTEPAssemblyOutcome.MISSING_METADATA


def test_empty_runtime_evidence_package_is_valid():
    package = RuntimeEvidencePackage(metadata=_metadata(), evidence=())
    assert package.evidence == ()
