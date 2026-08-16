"""Tests for the Phase 6 Stage 2 Track 2 `EvaluationCaseResolver`."""

import json
from pathlib import Path

import pytest

from safe_medical_ai.cases import CaseResolutionOutcome, EvaluationCaseResolver
from safe_medical_ai.retrieval import ArtifactType

_REAL_PROJECTION_PATH = (
    Path(__file__).resolve().parents[1] / "data" / "evaluation_case_manifest_projection.json"
)


def _write_projection(tmp_path: Path, cases=None) -> Path:
    if cases is None:
        cases = [
            {"case_id": "EC-0001", "population_id": "PP-0001", "expected_primary_artifact_type": "CKO"},
            {"case_id": "EC-0002", "population_id": "PP-0002", "expected_primary_artifact_type": "CKO"},
            {"case_id": "EC-0003", "population_id": "PP-0003", "expected_primary_artifact_type": "CKO"},
            {"case_id": "EC-0147", "population_id": "PP-0147", "expected_primary_artifact_type": "CKO"},
            {"case_id": "EC-0239", "population_id": "PP-0239", "expected_primary_artifact_type": "CKO"},
        ]
    projection = {
        "source_manifest": "PHASE6_STAGE2_EVALUATION_CASE_MANIFEST_v1.0_FROZEN.xlsx",
        "source_manifest_version": "1.0-FROZEN",
        "source_manifest_sha256": "deadbeef",
        "generated_by": "test fixture",
        "case_count": len(cases),
        "cases": cases,
    }
    path = tmp_path / "projection.json"
    path.write_text(json.dumps(projection))
    return path


# --- Gate 2: deterministic resolution -------------------------------------


@pytest.mark.parametrize(
    "case_id,expected_pp",
    [
        ("EC-0001", "PP-0001"),
        ("EC-0002", "PP-0002"),
        ("EC-0003", "PP-0003"),
        ("EC-0147", "PP-0147"),
        ("EC-0239", "PP-0239"),
    ],
)
def test_deterministic_ec_to_pp_resolution(tmp_path, case_id, expected_pp):
    resolver = EvaluationCaseResolver(_write_projection(tmp_path))
    result = resolver.resolve(case_id)

    assert result.outcome is CaseResolutionOutcome.RESOLVED
    assert result.case.case_id == case_id
    assert result.case.population_id == expected_pp
    assert result.case.expected_primary_artifact_type is ArtifactType.CKO


def test_resolution_is_repeatable(tmp_path):
    resolver = EvaluationCaseResolver(_write_projection(tmp_path))
    first = resolver.resolve("EC-0003")
    second = resolver.resolve("EC-0003")

    assert first.case.population_id == second.case.population_id == "PP-0003"


def test_resolved_case_carries_source_manifest_identity(tmp_path):
    resolver = EvaluationCaseResolver(_write_projection(tmp_path))
    result = resolver.resolve("EC-0002")

    assert result.case.source_manifest == "PHASE6_STAGE2_EVALUATION_CASE_MANIFEST_v1.0_FROZEN.xlsx"
    assert result.case.source_manifest_version == "1.0-FROZEN"
    assert result.case.source_manifest_sha256 == "deadbeef"


# --- Gate 4: fail closed, never falls back to any specific case -----------


def test_unknown_case_id_fails_closed(tmp_path):
    resolver = EvaluationCaseResolver(_write_projection(tmp_path))
    result = resolver.resolve("EC-9999")

    assert result.outcome is CaseResolutionOutcome.UNKNOWN_CASE
    assert result.case is None


@pytest.mark.parametrize(
    "malformed",
    ["", "PP-0002", "EC-2", "ec-0002", "EC-00021", None, "DROP TABLE cases"],
)
def test_malformed_case_id_fails_closed(tmp_path, malformed):
    resolver = EvaluationCaseResolver(_write_projection(tmp_path))
    result = resolver.resolve(malformed)

    assert result.outcome is CaseResolutionOutcome.MALFORMED_CASE_ID
    assert result.case is None


def test_missing_projection_file_fails_closed(tmp_path):
    resolver = EvaluationCaseResolver(tmp_path / "does-not-exist.json")
    result = resolver.resolve("EC-0002")

    assert result.outcome is CaseResolutionOutcome.PROJECTION_UNAVAILABLE
    assert result.case is None


@pytest.mark.parametrize("bad_input", ["EC-9999", "not-a-case", None, "PP-0002"])
def test_no_failure_outcome_ever_resolves_to_a_case(tmp_path, bad_input):
    resolver = EvaluationCaseResolver(_write_projection(tmp_path))
    result = resolver.resolve(bad_input)

    assert result.outcome is not CaseResolutionOutcome.RESOLVED
    assert result.case is None


# --- against the real shipped projection (not a test fixture) -------------


@pytest.mark.parametrize(
    "case_id,expected_pp",
    [
        ("EC-0001", "PP-0001"),
        ("EC-0002", "PP-0002"),
        ("EC-0003", "PP-0003"),
        ("EC-0147", "PP-0147"),
        ("EC-0239", "PP-0239"),
    ],
)
def test_real_shipped_projection_resolves_deterministically(case_id, expected_pp):
    resolver = EvaluationCaseResolver(_REAL_PROJECTION_PATH)
    result = resolver.resolve(case_id)

    assert result.outcome is CaseResolutionOutcome.RESOLVED
    assert result.case.population_id == expected_pp
    assert result.case.expected_primary_artifact_type is ArtifactType.CKO


def test_real_shipped_projection_has_all_239_cases_with_no_gaps():
    resolver = EvaluationCaseResolver(_REAL_PROJECTION_PATH)
    resolved = [resolver.resolve(f"EC-{i:04d}") for i in range(1, 240)]

    assert all(r.outcome is CaseResolutionOutcome.RESOLVED for r in resolved)
    assert {r.case.population_id for r in resolved} == {f"PP-{i:04d}" for i in range(1, 240)}
    assert all(r.case.expected_primary_artifact_type is ArtifactType.CKO for r in resolved)


def test_real_shipped_projection_rejects_ec_0240():
    # EC-0001..EC-0239 only -- one past the end is genuinely unknown.
    resolver = EvaluationCaseResolver(_REAL_PROJECTION_PATH)
    result = resolver.resolve("EC-0240")

    assert result.outcome is CaseResolutionOutcome.UNKNOWN_CASE
    assert result.case is None
