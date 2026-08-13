"""Tests for the Task #005 RTEP assembly boundary (`assemble_runtime_evidence_package`).

Provenance is supplied positionally (parallel to `retrieval_response.results`),
not keyed by `source_path` — see Change Request RC-01: the locked retrieval
contract never guarantees `source_path` uniqueness, so a source_path-keyed
association could not unambiguously distinguish two candidates that happen to
share the same source_path.
"""

import inspect

import pytest

from safe_medical_ai.evidence import (
    EvidenceItemProvenance,
    RTEPAssemblyContext,
    RTEPAssemblyOutcome,
    assemble_runtime_evidence_package,
)
from safe_medical_ai.evidence import assembly as assembly_module
from safe_medical_ai.evidence import models as evidence_models_module
from safe_medical_ai.retrieval import (
    ArtifactType,
    InMemoryRepositorySource,
    RetrievalCandidate,
    RetrievalOutcome,
    RetrievalRequest,
    RetrievalResponse,
    RetrievalService,
)


def _candidate(population_id: str, artifact_type: ArtifactType, suffix: str = "1") -> RetrievalCandidate:
    return RetrievalCandidate(
        population_id=population_id,
        artifact_type=artifact_type,
        source_path=f"03_Clinical_Knowledge/population/population_packages/{population_id}/{artifact_type.value}-{suffix}.md",
        title=f"{population_id} {artifact_type.value} title",
    )


def _provenance(suffix: str = "1") -> EvidenceItemProvenance:
    return EvidenceItemProvenance(
        knowledge_object_id=f"KO-{suffix}",
        knowledge_passport_id=f"KP-{suffix}",
        source_id=f"SRC-{suffix}",
        guideline_version=f"v{suffix}.0",
    )


def _provenance_for(results: list[RetrievalCandidate]) -> list[EvidenceItemProvenance]:
    """Build a positional provenance list, one distinct entry per candidate."""
    return [_provenance(str(i)) for i in range(len(results))]


def _context() -> RTEPAssemblyContext:
    return RTEPAssemblyContext(
        retrieval_id="RID-1",
        navigation_context_id="NAV-1",
        retrieval_policy_version="1.0",
        knowledge_base_version="1.0",
    )


def _fixture_service() -> RetrievalService:
    source = InMemoryRepositorySource(
        {
            "PP-0001": [
                _candidate("PP-0001", ArtifactType.CKO),
                _candidate("PP-0001", ArtifactType.KNOWLEDGE_PASSPORT),
            ],
            "PP-0002": [],
        }
    )
    return RetrievalService(source)


# --- successful assembly -----------------------------------------------------


def test_valid_retrieval_response_assembles_to_complete_rtep():
    service = _fixture_service()
    response = service.retrieve(RetrievalRequest(population_id="PP-0001"))

    result = assemble_runtime_evidence_package(
        response, context=_context(), provenance=_provenance_for(response.results)
    )

    assert result.outcome == RTEPAssemblyOutcome.ASSEMBLED
    assert result.package is not None
    assert len(result.package.evidence) == 2


def test_evidence_content_and_metadata_are_preserved():
    service = _fixture_service()
    response = service.retrieve(RetrievalRequest(population_id="PP-0001"))
    context = _context()

    result = assemble_runtime_evidence_package(
        response, context=context, provenance=_provenance_for(response.results)
    )

    package = result.package
    assert package.metadata.retrieval_id == context.retrieval_id
    assert package.metadata.navigation_context_id == context.navigation_context_id
    assert package.metadata.retrieval_policy_version == context.retrieval_policy_version
    assert package.metadata.knowledge_base_version == context.knowledge_base_version
    assert package.metadata.evidence_package_id  # generated, non-empty
    assert package.metadata.generation_timestamp is not None

    for candidate, item in zip(response.results, package.evidence, strict=True):
        assert item.population_id == candidate.population_id
        assert item.artifact_type == candidate.artifact_type
        assert item.source_path == candidate.source_path
        assert item.title == candidate.title


def test_provenance_values_are_preserved_exactly():
    service = _fixture_service()
    response = service.retrieve(RetrievalRequest(population_id="PP-0001"))
    provenance_list = _provenance_for(response.results)

    result = assemble_runtime_evidence_package(response, context=_context(), provenance=provenance_list)

    for expected, item in zip(provenance_list, result.package.evidence, strict=True):
        assert item.provenance.knowledge_object_id == expected.knowledge_object_id
        assert item.provenance.knowledge_passport_id == expected.knowledge_passport_id
        assert item.provenance.source_id == expected.source_id
        assert item.provenance.guideline_version == expected.guideline_version


def test_ordering_is_preserved_exactly_and_not_sorted():
    # Deliberately construct a RetrievalResponse whose results are NOT in
    # canonical artifact-type order, to prove assembly does not re-sort.
    candidates = [
        _candidate("PP-0001", ArtifactType.QA_REPORT, "a"),
        _candidate("PP-0001", ArtifactType.CKO, "b"),
        _candidate("PP-0001", ArtifactType.PRIMARY_EVIDENCE_PACKAGE, "c"),
    ]
    response = RetrievalResponse(
        outcome=RetrievalOutcome.FOUND,
        request=RetrievalRequest(population_id="PP-0001"),
        results=candidates,
    )

    result = assemble_runtime_evidence_package(
        response, context=_context(), provenance=_provenance_for(candidates)
    )

    assert [item.source_path for item in result.package.evidence] == [c.source_path for c in candidates]


def test_duplicate_source_paths_are_not_heuristically_deduplicated():
    duplicate_path = "03_Clinical_Knowledge/population/population_packages/PP-0001/01_CKO.md"
    candidates = [
        RetrievalCandidate(
            population_id="PP-0001", artifact_type=ArtifactType.CKO, source_path=duplicate_path, title="first"
        ),
        RetrievalCandidate(
            population_id="PP-0001", artifact_type=ArtifactType.CKO, source_path=duplicate_path, title="second"
        ),
    ]
    response = RetrievalResponse(
        outcome=RetrievalOutcome.FOUND,
        request=RetrievalRequest(population_id="PP-0001"),
        results=candidates,
    )

    result = assemble_runtime_evidence_package(
        response, context=_context(), provenance=_provenance_for(candidates)
    )

    assert result.outcome == RTEPAssemblyOutcome.ASSEMBLED
    assert len(result.package.evidence) == 2
    assert result.package.evidence[0].title == "first"
    assert result.package.evidence[1].title == "second"


def test_duplicate_source_paths_retain_unambiguous_distinct_provenance():
    """Regression test for Change Request RC-01.

    Two candidates sharing the same source_path must each keep their own,
    correctly associated provenance — never the same entry for both, and
    never conflated/overwritten because they share a source_path.
    """
    duplicate_path = "03_Clinical_Knowledge/population/population_packages/PP-0001/01_CKO.md"
    candidates = [
        RetrievalCandidate(
            population_id="PP-0001", artifact_type=ArtifactType.CKO, source_path=duplicate_path, title="first"
        ),
        RetrievalCandidate(
            population_id="PP-0001", artifact_type=ArtifactType.CKO, source_path=duplicate_path, title="second"
        ),
    ]
    response = RetrievalResponse(
        outcome=RetrievalOutcome.FOUND,
        request=RetrievalRequest(population_id="PP-0001"),
        results=candidates,
    )
    first_provenance = _provenance("first-item")
    second_provenance = _provenance("second-item")

    result = assemble_runtime_evidence_package(
        response, context=_context(), provenance=[first_provenance, second_provenance]
    )

    assert result.outcome == RTEPAssemblyOutcome.ASSEMBLED
    assert len(result.package.evidence) == 2
    assert result.package.evidence[0].source_path == duplicate_path
    assert result.package.evidence[1].source_path == duplicate_path
    # Same source_path, but each item unambiguously keeps its OWN provenance.
    assert result.package.evidence[0].provenance.knowledge_object_id == "KO-first-item"
    assert result.package.evidence[1].provenance.knowledge_object_id == "KO-second-item"
    assert result.package.evidence[0].provenance != result.package.evidence[1].provenance


# --- EMPTY -------------------------------------------------------------------


def test_empty_retrieval_produces_valid_empty_rtep():
    service = _fixture_service()
    response = service.retrieve(RetrievalRequest(population_id="PP-0002"))
    assert response.outcome == RetrievalOutcome.EMPTY  # sanity check on the fixture

    result = assemble_runtime_evidence_package(response, context=_context(), provenance=[])

    assert result.outcome == RTEPAssemblyOutcome.ASSEMBLED
    assert result.package is not None
    assert result.package.evidence == ()
    assert result.package.metadata.retrieval_id == "RID-1"


def test_empty_retrieval_with_provenance_omitted_entirely_still_succeeds():
    service = _fixture_service()
    response = service.retrieve(RetrievalRequest(population_id="PP-0002"))

    result = assemble_runtime_evidence_package(response, context=_context())

    assert result.outcome == RTEPAssemblyOutcome.ASSEMBLED
    assert result.package.evidence == ()


def test_empty_retrieval_without_metadata_still_fails():
    service = _fixture_service()
    response = service.retrieve(RetrievalRequest(population_id="PP-0002"))

    result = assemble_runtime_evidence_package(response, context=None)

    assert result.outcome == RTEPAssemblyOutcome.MISSING_METADATA
    assert result.package is None


# --- retrieval-originated failures propagate unchanged ------------------------


def test_not_found_produces_no_rtep():
    service = _fixture_service()
    response = service.retrieve(RetrievalRequest(population_id="PP-9999"))
    assert response.outcome == RetrievalOutcome.NOT_FOUND

    result = assemble_runtime_evidence_package(response, context=_context(), provenance=[])

    assert result.outcome == RTEPAssemblyOutcome.RETRIEVAL_NOT_FOUND
    assert result.package is None


def test_invalid_request_produces_no_rtep():
    service = _fixture_service()
    response = service.retrieve(RetrievalRequest(population_id="not-a-valid-id"))
    assert response.outcome == RetrievalOutcome.INVALID_REQUEST

    result = assemble_runtime_evidence_package(response, context=_context(), provenance=[])

    assert result.outcome == RTEPAssemblyOutcome.RETRIEVAL_INVALID_REQUEST
    assert result.package is None


# --- assembly-originated failures --------------------------------------------


def test_missing_metadata_causes_assembly_failure():
    service = _fixture_service()
    response = service.retrieve(RetrievalRequest(population_id="PP-0001"))

    result = assemble_runtime_evidence_package(response, context=None, provenance=[])

    assert result.outcome == RTEPAssemblyOutcome.MISSING_METADATA
    assert result.package is None


def test_incomplete_provenance_causes_atomic_assembly_failure():
    service = _fixture_service()
    response = service.retrieve(RetrievalRequest(population_id="PP-0001"))
    # Deliberately provide provenance for none of the candidates.
    result = assemble_runtime_evidence_package(response, context=_context(), provenance=[])

    assert result.outcome == RTEPAssemblyOutcome.INCOMPLETE_PROVENANCE
    assert result.package is None


def test_partially_missing_provenance_still_fails_atomically_not_partially():
    service = _fixture_service()
    response = service.retrieve(RetrievalRequest(population_id="PP-0001"))
    assert len(response.results) == 2
    # Provenance supplied for only one of the two candidates.
    result = assemble_runtime_evidence_package(response, context=_context(), provenance=[_provenance()])

    assert result.outcome == RTEPAssemblyOutcome.INCOMPLETE_PROVENANCE
    assert result.package is None  # not a partial package containing only the first item


def test_excess_provenance_entries_also_causes_incomplete_provenance():
    service = _fixture_service()
    response = service.retrieve(RetrievalRequest(population_id="PP-0001"))
    assert len(response.results) == 2
    # More provenance entries supplied than there are candidates.
    result = assemble_runtime_evidence_package(
        response, context=_context(), provenance=_provenance_for(response.results) + [_provenance("extra")]
    )

    assert result.outcome == RTEPAssemblyOutcome.INCOMPLETE_PROVENANCE
    assert result.package is None


def test_malformed_candidate_with_blank_source_path_causes_invalid_evidence_item():
    candidate = RetrievalCandidate(population_id="PP-0001", artifact_type=ArtifactType.CKO, source_path="", title=None)
    response = RetrievalResponse(
        outcome=RetrievalOutcome.FOUND,
        request=RetrievalRequest(population_id="PP-0001"),
        results=[candidate],
    )

    result = assemble_runtime_evidence_package(response, context=_context(), provenance=[_provenance()])

    assert result.outcome == RTEPAssemblyOutcome.INVALID_EVIDENCE_ITEM
    assert result.package is None


# --- immutability (behavioral) ------------------------------------------------


def test_direct_mutation_of_assembled_package_is_rejected():
    service = _fixture_service()
    response = service.retrieve(RetrievalRequest(population_id="PP-0001"))
    result = assemble_runtime_evidence_package(
        response, context=_context(), provenance=_provenance_for(response.results)
    )

    from pydantic import ValidationError

    with pytest.raises(ValidationError):
        result.package.evidence = ()


def test_mutating_source_candidate_after_assembly_does_not_affect_rtep():
    service = _fixture_service()
    response = service.retrieve(RetrievalRequest(population_id="PP-0001"))

    result = assemble_runtime_evidence_package(
        response, context=_context(), provenance=_provenance_for(response.results)
    )
    original_titles = [item.title for item in result.package.evidence]

    # RetrievalCandidate is not frozen; mutate it after assembly completed.
    response.results[0].title = "MUTATED-AFTER-ASSEMBLY"
    # Also mutate the results list itself.
    response.results.append(
        RetrievalCandidate(population_id="PP-0001", artifact_type=ArtifactType.QA_REPORT, source_path="injected", title="x")
    )

    assert [item.title for item in result.package.evidence] == original_titles
    assert len(result.package.evidence) == 2


def test_mutating_provenance_list_after_assembly_does_not_affect_rtep():
    service = _fixture_service()
    response = service.retrieve(RetrievalRequest(population_id="PP-0001"))
    provenance_list = _provenance_for(response.results)

    result = assemble_runtime_evidence_package(response, context=_context(), provenance=provenance_list)
    original_guideline_versions = [item.provenance.guideline_version for item in result.package.evidence]

    provenance_list.clear()  # mutate the list the caller passed in

    assert [item.provenance.guideline_version for item in result.package.evidence] == original_guideline_versions


# --- determinism ---------------------------------------------------------------


def test_assembly_is_deterministic_apart_from_identity_and_timestamp_fields():
    service = _fixture_service()
    response = service.retrieve(RetrievalRequest(population_id="PP-0001"))
    provenance_list = _provenance_for(response.results)
    context = _context()

    first = assemble_runtime_evidence_package(response, context=context, provenance=provenance_list)
    second = assemble_runtime_evidence_package(response, context=context, provenance=provenance_list)

    assert first.outcome == second.outcome == RTEPAssemblyOutcome.ASSEMBLED
    assert [i.model_dump() for i in first.package.evidence] == [i.model_dump() for i in second.package.evidence]
    assert first.package.metadata.retrieval_id == second.package.metadata.retrieval_id
    assert first.package.metadata.navigation_context_id == second.package.metadata.navigation_context_id
    assert first.package.metadata.retrieval_policy_version == second.package.metadata.retrieval_policy_version
    assert first.package.metadata.knowledge_base_version == second.package.metadata.knowledge_base_version
    # Identity/timestamp fields are legitimately runtime-generated and may differ.
    assert isinstance(first.package.metadata.evidence_package_id, str)
    assert isinstance(second.package.metadata.evidence_package_id, str)


# --- architectural boundary (static) --------------------------------------------


def test_assembly_module_does_not_re_retrieve_or_access_repository_directly():
    source = inspect.getsource(assembly_module)
    assert "RepositorySource(" not in source
    assert ".list_artifacts(" not in source
    assert "RetrievalService(" not in source
    assert ".retrieve(" not in source


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
def test_assembly_and_models_do_not_reference_llm_or_vector_libraries(forbidden_token):
    source = inspect.getsource(assembly_module) + inspect.getsource(evidence_models_module)
    assert forbidden_token.lower() not in source.lower()


def test_assembly_module_does_not_import_llm_adapter():
    source = inspect.getsource(assembly_module)
    assert "from ..llm" not in source
    assert "import llm" not in source
