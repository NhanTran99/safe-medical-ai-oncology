"""Tests for the B10 coverage/reproducibility aggregation module.

Uses only the deterministic provider (the existing test-suite default,
see conftest.py) -- no test in this file makes a real external API call.
`summarize_campaign_coverage` itself is pure (no I/O), so most tests here
exercise it directly over hand-built `CampaignExecutionResult` records
produced by the real `execute_case()`/`record_execution_result()` path,
never fabricated dictionaries pretending to be results.
"""

import pytest
from pydantic import ValidationError

from safe_medical_ai.campaign import (
    CampaignCoverageSummary,
    execute_case,
    read_execution_results,
    record_execution_result,
    summarize_campaign_coverage,
)


def test_summarize_campaign_coverage_over_an_empty_sequence():
    summary = summarize_campaign_coverage([])

    assert isinstance(summary, CampaignCoverageSummary)
    assert summary.total_execution_records == 0
    assert summary.distinct_case_ids == 0
    assert summary.distinct_population_ids == 0
    assert summary.case_resolution_outcome_counts == {}
    assert summary.cer_outcome_counts == {}
    assert summary.validation_outcome_counts == {}


def test_summarize_campaign_coverage_counts_distinct_case_and_population_ids(tmp_path):
    path = tmp_path / "results.jsonl"
    record_execution_result(execute_case("EC-0001", "q1"), path)
    record_execution_result(execute_case("EC-0003", "q2"), path)
    # A repeated execution of the same case_id/population_id must not
    # inflate the distinct counts, even though it does add a new record.
    record_execution_result(execute_case("EC-0003", "q3"), path)

    summary = summarize_campaign_coverage(read_execution_results(path))

    assert summary.total_execution_records == 3
    assert summary.distinct_case_ids == 2
    assert summary.distinct_population_ids == 2


def test_summarize_campaign_coverage_excludes_unresolved_cases_from_population_count(tmp_path):
    path = tmp_path / "results.jsonl"
    record_execution_result(execute_case("EC-0001", "q1"), path)
    # An unresolved case_id never reaches a population_id -- it must be
    # counted in total_execution_records and case_resolution_outcome_counts,
    # but never as a "distinct population" (None is not a PP identity).
    record_execution_result(execute_case("EC-9999", "irrelevant"), path)

    summary = summarize_campaign_coverage(read_execution_results(path))

    assert summary.total_execution_records == 2
    assert summary.distinct_case_ids == 2
    assert summary.distinct_population_ids == 1
    assert summary.case_resolution_outcome_counts == {"RESOLVED": 1, "UNKNOWN_CASE": 1}


def test_summarize_campaign_coverage_groups_by_existing_cer_and_validation_outcomes(tmp_path):
    path = tmp_path / "results.jsonl"
    record_execution_result(execute_case("EC-0001", "q1"), path)
    record_execution_result(execute_case("EC-0003", "q2"), path)

    summary = summarize_campaign_coverage(read_execution_results(path))

    # The deterministic provider always reaches COMPLETED/VALID for an
    # approved case -- this asserts the aggregation reuses the *existing*
    # CEROutcome/CandidateValidationOutcome values verbatim, never a
    # reinterpreted or renamed vocabulary of its own.
    assert summary.cer_outcome_counts == {"COMPLETED": 2}
    assert summary.validation_outcome_counts == {"VALID": 2}


def test_summarize_campaign_coverage_is_pure_over_a_caller_supplied_subset(tmp_path):
    # summarize_campaign_coverage never reads a file itself -- it can
    # summarize any caller-supplied sequence, including a subset of a
    # larger recorded set.
    path = tmp_path / "results.jsonl"
    record_execution_result(execute_case("EC-0001", "q1"), path)
    record_execution_result(execute_case("EC-0003", "q2"), path)
    all_results = read_execution_results(path)

    subset_summary = summarize_campaign_coverage(all_results[:1])
    full_summary = summarize_campaign_coverage(all_results)

    assert subset_summary.total_execution_records == 1
    assert full_summary.total_execution_records == 2


def test_campaign_coverage_summary_is_frozen():
    summary = summarize_campaign_coverage([])

    with pytest.raises(ValidationError):
        summary.total_execution_records = 99
