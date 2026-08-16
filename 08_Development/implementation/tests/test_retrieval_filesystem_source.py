"""Tests for the Task #004 filesystem-backed RepositorySource.

Uses only bounded pytest `tmp_path` fixture trees — never the real
controlled repository — per the Task #004 testing boundary.
"""

import pytest

from safe_medical_ai.retrieval import (
    ArtifactType,
    FilesystemRepositorySource,
    RepositorySourceUnavailableError,
    RetrievalOutcome,
    RetrievalRequest,
    RetrievalService,
)

_CANONICAL_FILES = (
    "01_CKO.md",
    "02_KNOWLEDGE_PASSPORT.md",
    "03_PRIMARY_EVIDENCE_PACKAGE.md",
    "04_QA_REPORT.md",
)


def _make_pp_dir(root, dirname: str, filenames=_CANONICAL_FILES) -> None:
    pp_dir = root / dirname
    pp_dir.mkdir(parents=True)
    for filename in filenames:
        (pp_dir / filename).write_text(f"fixture content for {dirname}/{filename}\n", encoding="utf-8",)
    return pp_dir


@pytest.fixture
def population_packages_root(tmp_path):
    root = tmp_path / "population_packages"
    root.mkdir()

    # Real-repository naming convention: "PP-#### — Title", all 4 artifacts.
    _make_pp_dir(root, "PP-0001 — Sample_Title")

    # Fixture-style exact-name directory, only a partial artifact set.
    _make_pp_dir(root, "PP-0002", filenames=("01_CKO.md",))

    # Registered population with zero artifacts inside.
    (root / "PP-0003").mkdir()

    # Malformed metadata: 01_CKO.md exists as a directory, not a file.
    pp4 = _make_pp_dir(root, "PP-0004", filenames=("02_KNOWLEDGE_PASSPORT.md",))
    (pp4 / "01_CKO.md").mkdir()

    # Ambiguous: two directories both match the "PP-0005 — " prefix.
    _make_pp_dir(root, "PP-0005 — TitleA", filenames=("01_CKO.md",))
    _make_pp_dir(root, "PP-0005 — TitleB", filenames=("01_CKO.md",))

    return root


def _source(root):
    return FilesystemRepositorySource(
        root, provenance_prefix="03_Clinical_Knowledge/population/population_packages"
    )


# --- A. configured valid source root -> successful retrieval -------------


def test_successful_retrieval_via_prefix_matched_directory(population_packages_root):
    source = _source(population_packages_root)
    service = RetrievalService(source)

    response = service.retrieve(RetrievalRequest(population_id="PP-0001"))

    assert response.outcome == RetrievalOutcome.FOUND
    assert len(response.results) == 4
    assert [c.artifact_type for c in response.results] == [
        ArtifactType.CKO,
        ArtifactType.KNOWLEDGE_PASSPORT,
        ArtifactType.PRIMARY_EVIDENCE_PACKAGE,
        ArtifactType.QA_REPORT,
    ]


def test_successful_retrieval_via_exact_name_directory(population_packages_root):
    source = _source(population_packages_root)
    response = source.list_artifacts("PP-0002")

    assert response is not None
    assert len(response) == 1
    assert response[0].artifact_type == ArtifactType.CKO


# --- F. provenance ---------------------------------------------------------


def test_provenance_is_repository_relative_and_authoritative(population_packages_root):
    source = _source(population_packages_root)
    candidates = source.list_artifacts("PP-0001")

    for candidate in candidates:
        assert candidate.source_path.startswith(
            "03_Clinical_Knowledge/population/population_packages/PP-0001 — Sample_Title/"
        )
        assert not candidate.source_path.startswith(str(population_packages_root))


def test_title_is_extracted_from_prefix_matched_directory_name(population_packages_root):
    source = _source(population_packages_root)
    candidates = source.list_artifacts("PP-0001")

    assert all(c.title == "Sample_Title" for c in candidates)


def test_title_is_none_for_exact_name_directory_not_fabricated(population_packages_root):
    source = _source(population_packages_root)
    candidates = source.list_artifacts("PP-0002")

    assert candidates[0].title is None


# --- content (Track 3 BATCH 01) ---------------------------------------------


def test_content_is_loaded_from_the_actual_artifact_file(population_packages_root):
    source = _source(population_packages_root)
    candidates = source.list_artifacts("PP-0001")

    for candidate in candidates:
        filename = candidate.source_path.rsplit("/", 1)[-1]
        assert candidate.content == f"fixture content for PP-0001 — Sample_Title/{filename}\n"


# --- B. valid population, no matching artifacts -> EMPTY -------------------


def test_empty_outcome_for_population_with_zero_artifacts(population_packages_root):
    service = RetrievalService(_source(population_packages_root))
    response = service.retrieve(RetrievalRequest(population_id="PP-0003"))

    assert response.outcome == RetrievalOutcome.EMPTY
    assert response.results == []


def test_empty_outcome_when_artifact_type_filter_matches_nothing(population_packages_root):
    service = RetrievalService(_source(population_packages_root))
    response = service.retrieve(
        RetrievalRequest(population_id="PP-0002", artifact_type=ArtifactType.QA_REPORT)
    )

    assert response.outcome == RetrievalOutcome.EMPTY


# --- C. well-formed but unregistered/missing population -> NOT_FOUND -------


def test_not_found_for_well_formed_unregistered_population(population_packages_root):
    service = RetrievalService(_source(population_packages_root))
    response = service.retrieve(RetrievalRequest(population_id="PP-9999"))

    assert response.outcome == RetrievalOutcome.NOT_FOUND


def test_not_found_for_ambiguous_prefix_match(population_packages_root):
    # Two directories match "PP-0005 — " -> must not guess.
    source = _source(population_packages_root)
    assert source.list_artifacts("PP-0005") is None


# --- D. missing/unavailable source root -> safe deterministic failure ------


def test_missing_source_root_raises_at_construction(tmp_path):
    missing_root = tmp_path / "does-not-exist"

    with pytest.raises(RepositorySourceUnavailableError):
        FilesystemRepositorySource(missing_root, provenance_prefix="irrelevant")


def test_source_root_removed_after_construction_raises_deterministically(tmp_path):
    root = tmp_path / "root"
    root.mkdir()
    source = FilesystemRepositorySource(root, provenance_prefix="irrelevant")

    root.rmdir()

    with pytest.raises(RepositorySourceUnavailableError):
        source.list_artifacts("PP-0001")


# --- E. malformed/missing artifact metadata: safe handling, no fabrication -


def test_malformed_artifact_entry_is_skipped_not_fabricated(population_packages_root):
    source = _source(population_packages_root)
    candidates = source.list_artifacts("PP-0004")

    # 01_CKO.md exists only as a directory (malformed); must be skipped.
    assert [c.artifact_type for c in candidates] == [ArtifactType.KNOWLEDGE_PASSPORT]


# --- G. deterministic ordering ---------------------------------------------


def test_result_ordering_is_deterministic_across_repeated_calls(population_packages_root):
    service = RetrievalService(_source(population_packages_root))
    request = RetrievalRequest(population_id="PP-0001")

    first = [c.source_path for c in service.retrieve(request).results]
    for _ in range(5):
        again = [c.source_path for c in service.retrieve(request).results]
        assert again == first


# --- H. path-traversal defense-in-depth (bypassing RetrievalService) -------


@pytest.mark.parametrize("unsafe_id", ["../../etc", "PP-0001/../../etc", "PP-0001/subdir", ""])
def test_unsafe_population_id_is_rejected_even_when_calling_source_directly(
    population_packages_root, unsafe_id
):
    source = _source(population_packages_root)
    assert source.list_artifacts(unsafe_id) is None
