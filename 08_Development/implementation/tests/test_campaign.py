"""Tests for the B07 execution/evidence preparation layer.

Uses only the deterministic provider (the existing test-suite default, see
`conftest.py`) -- no test in this file makes a real external API call, so
the default test suite remains fully deterministic (Section 9).
"""

import json

from safe_medical_ai.campaign import (
    CampaignExecutionResult,
    EvidenceCaptureOutcome,
    execute_case,
    read_execution_results,
    record_execution_result,
)
from safe_medical_ai.cases import CaseResolutionOutcome
from safe_medical_ai.cer import CEROutcome
from safe_medical_ai.generation import GenerationOutcome
from safe_medical_ai.validation import CandidateValidationOutcome


# --- 1/2/3: approved case_id executes through the harness, case authority
# resolves through the existing manifest, result contains case_id + PP ----


def test_execute_case_runs_an_approved_case_through_the_existing_path():
    result = execute_case("EC-0003", "What is Gastric Adenocarcinoma?")

    assert isinstance(result, CampaignExecutionResult)
    assert result.case_id == "EC-0003"
    assert result.resolved_population_id == "PP-0003"
    assert result.case_resolution_outcome == CaseResolutionOutcome.RESOLVED


def test_execute_case_reaches_completed_via_the_deterministic_provider():
    result = execute_case("EC-0001", "What is Cancer?")

    assert result.cer_outcome == CEROutcome.COMPLETED
    assert result.validation_outcome == CandidateValidationOutcome.VALID


# --- 4/5: existing typed stage outcomes preserved, GenerationOutcome not
# collapsed -----------------------------------------------------------------


def test_execute_case_preserves_the_detailed_generation_outcome():
    result = execute_case("EC-0002", "What is Gastric Cancer?")

    # The detailed GenerationOutcome (10 possible values) is preserved,
    # not collapsed to a PASS/None boolean the way /cer/evaluate's HTTP
    # JSON currently is.
    assert result.generation_outcome == GenerationOutcome.GENERATED
    assert result.provider_name == "DeterministicLocalProvider"


def test_execute_case_preserves_retrieval_and_safety_outcomes():
    result = execute_case("EC-0147", "test question")

    assert result.retrieval_outcome is not None
    assert result.retrieval_outcome.value == "FOUND"
    assert result.retrieval_result_count == 1
    assert result.safety_action is not None
    assert result.safety_action.value == "ALLOW"


# --- 6: durable result is actually written and machine-readable -----------


def test_record_execution_result_writes_a_machine_readable_json_line(tmp_path):
    result = execute_case("EC-0003", "What is Gastric Adenocarcinoma?")
    path = tmp_path / "results.jsonl"

    captured = record_execution_result(result, path)

    assert captured.evidence_capture_status == EvidenceCaptureOutcome.CAPTURED
    assert path.exists()

    lines = path.read_text(encoding="utf-8").strip().splitlines()
    assert len(lines) == 1
    parsed = json.loads(lines[0])
    assert parsed["case_id"] == "EC-0003"
    assert parsed["evidence_capture_status"] == "CAPTURED"


def test_read_execution_results_round_trips_the_recorded_result(tmp_path):
    result = execute_case("EC-0003", "What is Gastric Adenocarcinoma?")
    path = tmp_path / "results.jsonl"
    captured = record_execution_result(result, path)

    read_back = read_execution_results(path)

    assert len(read_back) == 1
    assert read_back[0] == captured


def test_read_execution_results_returns_empty_list_when_file_does_not_exist(tmp_path):
    assert read_execution_results(tmp_path / "does-not-exist.jsonl") == []


def test_record_execution_result_is_append_only(tmp_path):
    path = tmp_path / "results.jsonl"
    first = record_execution_result(execute_case("EC-0001", "q1"), path)
    second = record_execution_result(execute_case("EC-0002", "q2"), path)

    results = read_execution_results(path)

    assert len(results) == 2
    assert {r.case_id for r in results} == {"EC-0001", "EC-0002"}
    # The first record is untouched by the second append.
    assert results[0] == first
    assert results[1] == second


# --- 7: failure outcomes are preserved as failures, never rewritten -------


def test_unknown_case_failure_is_preserved_not_rewritten_to_success(tmp_path):
    result = execute_case("EC-9999", "irrelevant question")

    assert result.case_resolution_outcome == CaseResolutionOutcome.UNKNOWN_CASE
    assert result.resolved_population_id is None
    assert result.cer_outcome is None
    assert result.retrieval_outcome is None
    assert result.generation_outcome is None
    assert result.validation_outcome is None

    captured = record_execution_result(result, tmp_path / "results.jsonl")
    assert captured.case_resolution_outcome == CaseResolutionOutcome.UNKNOWN_CASE
    read_back = read_execution_results(tmp_path / "results.jsonl")
    assert read_back[0].case_resolution_outcome == CaseResolutionOutcome.UNKNOWN_CASE


# --- 8: re-executions are separately identifiable --------------------------


def test_repeated_executions_of_the_same_case_are_separately_identifiable():
    first = execute_case("EC-0003", "What is Gastric Adenocarcinoma?")
    second = execute_case("EC-0003", "What is Gastric Adenocarcinoma?")

    assert first.execution_id != second.execution_id
    assert first.case_id == second.case_id == "EC-0003"


# --- 9/10: invalid/unknown case IDs fail closed; no population_id bypass --


def test_malformed_case_id_fails_closed():
    result = execute_case("not-a-case-id", "irrelevant")

    assert result.case_resolution_outcome == CaseResolutionOutcome.MALFORMED_CASE_ID
    assert result.resolved_population_id is None


def test_execute_case_has_no_population_id_parameter():
    # D03/Principle 2: case_id is the sole execution authority -- there is
    # no way to pass an arbitrary population_id into the harness at all.
    import inspect

    params = inspect.signature(execute_case).parameters
    assert "population_id" not in params
    assert "case_id" in params


# --- reproducibility / capture-status fields -------------------------------


def test_execution_result_carries_reproducibility_identity():
    result = execute_case("EC-0003", "What is Gastric Adenocarcinoma?")

    assert result.execution_id
    assert result.execution_timestamp is not None
    assert result.trace_id
    # evidence_capture_status is only set once record_execution_result has
    # actually attempted persistence -- a freshly executed (not yet
    # recorded) result must not claim a capture status it hasn't earned.
    assert result.evidence_capture_status is None


def test_record_execution_result_reports_write_failure_without_raising(tmp_path):
    result = execute_case("EC-0003", "What is Gastric Adenocarcinoma?")
    # A path whose parent cannot be created (a file, not a directory) --
    # forces a genuine OSError instead of simulating one.
    blocking_file = tmp_path / "blocked"
    blocking_file.write_text("not a directory", encoding="utf-8")
    bad_path = blocking_file / "results.jsonl"

    captured = record_execution_result(result, bad_path)

    assert captured.evidence_capture_status == EvidenceCaptureOutcome.WRITE_FAILED
    assert not bad_path.exists()
