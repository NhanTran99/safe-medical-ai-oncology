"""Baseline tests for the Task #003 RetrievalService.

Uses only deterministic, synthetic fixture data via InMemoryRepositorySource
— no reading of the actual controlled 239-PP repository.
"""

import pytest

from safe_medical_ai.retrieval import (
    ArtifactType,
    InMemoryRepositorySource,
    RetrievalCandidate,
    RetrievalOutcome,
    RetrievalRequest,
    RetrievalService,
)
from safe_medical_ai.trace import set_trace_id


def _candidate(population_id: str, artifact_type: ArtifactType) -> RetrievalCandidate:
    return RetrievalCandidate(
        population_id=population_id,
        artifact_type=artifact_type,
        source_path=(
            f"03_Clinical_Knowledge/population/population_packages/"
            f"{population_id}/{artifact_type.value}.md"
        ),
        title=f"{population_id} {artifact_type.value} (fixture)",
    )


def _fixture_service() -> RetrievalService:
    # Deliberately registered out of canonical order to prove sorting works.
    source = InMemoryRepositorySource(
        {
            "PP-0001": [
                _candidate("PP-0001", ArtifactType.QA_REPORT),
                _candidate("PP-0001", ArtifactType.CKO),
                _candidate("PP-0001", ArtifactType.PRIMARY_EVIDENCE_PACKAGE),
                _candidate("PP-0001", ArtifactType.KNOWLEDGE_PASSPORT),
            ],
            "PP-0002": [
                _candidate("PP-0002", ArtifactType.CKO),
            ],
            "PP-0003": [],
        }
    )
    return RetrievalService(source)


def test_valid_navigation_retrieval_returns_all_artifacts_in_canonical_order():
    service = _fixture_service()
    response = service.retrieve(RetrievalRequest(population_id="PP-0001"))

    assert response.outcome == RetrievalOutcome.FOUND
    assert [c.artifact_type for c in response.results] == [
        ArtifactType.CKO,
        ArtifactType.KNOWLEDGE_PASSPORT,
        ArtifactType.PRIMARY_EVIDENCE_PACKAGE,
        ArtifactType.QA_REPORT,
    ]


def test_hierarchical_filtering_by_artifact_type():
    service = _fixture_service()
    response = service.retrieve(
        RetrievalRequest(population_id="PP-0001", artifact_type=ArtifactType.QA_REPORT)
    )

    assert response.outcome == RetrievalOutcome.FOUND
    assert len(response.results) == 1
    assert response.results[0].artifact_type == ArtifactType.QA_REPORT
    assert response.results[0].population_id == "PP-0001"


def test_provenance_is_preserved_on_every_result():
    service = _fixture_service()
    response = service.retrieve(RetrievalRequest(population_id="PP-0001"))

    assert response.outcome == RetrievalOutcome.FOUND
    for candidate in response.results:
        assert candidate.population_id == "PP-0001"
        assert candidate.source_path.startswith(
            "03_Clinical_Knowledge/population/population_packages/PP-0001/"
        )
        assert candidate.artifact_type.value in candidate.source_path


def test_result_ordering_is_deterministic_across_repeated_calls():
    service = _fixture_service()
    request = RetrievalRequest(population_id="PP-0001")

    first = [c.source_path for c in service.retrieve(request).results]
    for _ in range(5):
        again = [c.source_path for c in service.retrieve(request).results]
        assert again == first


def test_empty_result_when_filter_matches_nothing():
    service = _fixture_service()
    # PP-0002 only has a CKO artifact registered.
    response = service.retrieve(
        RetrievalRequest(population_id="PP-0002", artifact_type=ArtifactType.QA_REPORT)
    )

    assert response.outcome == RetrievalOutcome.EMPTY
    assert response.results == []
    assert response.message is not None


def test_empty_result_when_population_has_zero_registered_artifacts():
    service = _fixture_service()
    response = service.retrieve(RetrievalRequest(population_id="PP-0003"))

    assert response.outcome == RetrievalOutcome.EMPTY
    assert response.results == []


@pytest.mark.parametrize("bad_population_id", ["PP-1", "pp-0001", "PP-abcd", "", "PP-00001", "0001"])
def test_invalid_request_rejects_malformed_population_id(bad_population_id):
    service = _fixture_service()
    response = service.retrieve(RetrievalRequest(population_id=bad_population_id))

    assert response.outcome == RetrievalOutcome.INVALID_REQUEST
    assert response.results == []
    assert response.message is not None


def test_not_found_for_well_formed_but_unregistered_population_id():
    service = _fixture_service()
    response = service.retrieve(RetrievalRequest(population_id="PP-9999"))

    assert response.outcome == RetrievalOutcome.NOT_FOUND
    assert response.results == []
    assert response.message is not None


def test_response_echoes_the_original_request():
    service = _fixture_service()
    request = RetrievalRequest(population_id="PP-0001", artifact_type=ArtifactType.CKO)
    response = service.retrieve(request)

    assert response.request == request


def test_trace_id_is_propagated_into_the_response():
    service = _fixture_service()
    set_trace_id("fixed-trace-for-retrieval-test")

    response = service.retrieve(RetrievalRequest(population_id="PP-0001"))

    assert response.trace_id == "fixed-trace-for-retrieval-test"
