"""Baseline tests for the Task #003 retrieval domain models."""

import pytest
from pydantic import ValidationError

from safe_medical_ai.models.output_contract import ValidationOutcome
from safe_medical_ai.retrieval import (
    ArtifactType,
    RetrievalCandidate,
    RetrievalOutcome,
    RetrievalRequest,
    artifact_type_sort_key,
)


def test_artifact_type_vocabulary():
    assert {a.value for a in ArtifactType} == {
        "CKO",
        "KNOWLEDGE_PASSPORT",
        "PRIMARY_EVIDENCE_PACKAGE",
        "QA_REPORT",
    }


def test_artifact_type_sort_key_is_canonical_order():
    ordered = sorted(ArtifactType, key=artifact_type_sort_key)
    assert ordered == [
        ArtifactType.CKO,
        ArtifactType.KNOWLEDGE_PASSPORT,
        ArtifactType.PRIMARY_EVIDENCE_PACKAGE,
        ArtifactType.QA_REPORT,
    ]


def test_retrieval_outcome_vocabulary():
    assert {o.value for o in RetrievalOutcome} == {
        "FOUND",
        "EMPTY",
        "INVALID_REQUEST",
        "NOT_FOUND",
    }


def test_retrieval_outcome_is_distinct_from_validation_outcome():
    # Retrieval-result vocabulary must not be merged with or substitute for
    # OUTPUT_CONTRACT's output-validation vocabulary.
    assert RetrievalOutcome is not ValidationOutcome
    assert set(RetrievalOutcome.__members__) & set(ValidationOutcome.__members__) == set()


def test_retrieval_request_defaults_artifact_type_to_none():
    request = RetrievalRequest(population_id="PP-0001")
    assert request.artifact_type is None


def test_retrieval_request_accepts_explicit_artifact_type():
    request = RetrievalRequest(population_id="PP-0001", artifact_type=ArtifactType.QA_REPORT)
    assert request.artifact_type == ArtifactType.QA_REPORT


def test_retrieval_candidate_requires_core_fields():
    with pytest.raises(ValidationError):
        RetrievalCandidate()  # missing population_id / artifact_type / source_path


def test_retrieval_candidate_title_is_optional():
    candidate = RetrievalCandidate(
        population_id="PP-0001",
        artifact_type=ArtifactType.CKO,
        source_path="03_Clinical_Knowledge/population/population_packages/PP-0001/01_CKO.md",
    )
    assert candidate.title is None
