"""Tests for the B12 Selected-PP Request Relevance boundary.

Pure module-level tests only -- no HTTP, no CER, no provider. Endpoint-
level integration (hard-block verification, B08 exemption, B11 boundary
presentation, B10 regression) lives in test_chat_ui.py and
test_track2_case_execution.py, alongside the existing tests for those
same paths.
"""

import pytest
from pydantic import ValidationError

from safe_medical_ai.relevance import (
    REQUEST_NOT_RELEVANT_RESPONSE_TEXT,
    RequestRelevanceOutcome,
    RequestRelevanceResult,
    evaluate_request_relevance,
)


def test_relevant_when_message_shares_significant_vocabulary_with_target():
    result = evaluate_request_relevance(
        "What is Gastric Cancer?",
        pp_title="What is Gastric Cancer?",
        controlled_question="What is Gastric Cancer?",
    )

    assert result.outcome is RequestRelevanceOutcome.RELEVANT
    assert result.score > 0.0
    assert result.message is None


def test_not_relevant_when_message_shares_no_significant_vocabulary_with_target():
    # Both strings are real, existing, already-governed controlled
    # questions from the frozen manifest -- only their pairing is
    # synthetic, no clinical content is invented.
    result = evaluate_request_relevance(
        "Please explain Genomic Biomarkers.",
        pp_title="What is Cancer?",
        controlled_question="What is Cancer?",
    )

    assert result.outcome is RequestRelevanceOutcome.NOT_RELEVANT
    assert result.score == 0.0
    assert result.message == REQUEST_NOT_RELEVANT_RESPONSE_TEXT


def test_not_relevant_message_never_invents_clinical_content():
    result = evaluate_request_relevance(
        "Please explain Genomic Biomarkers.",
        pp_title="What is Cancer?",
        controlled_question="What is Cancer?",
    )

    assert result.message == (
        "This request does not appear to relate to the selected topic. "
        "A response cannot be generated for it under the selected topic."
    )


def test_shared_stopwords_alone_do_not_count_as_evidence_of_relevance():
    # "What is" is shared, but stopword-filtered -- with no other overlap
    # this must still be NOT_RELEVANT, not a false RELEVANT from function
    # words alone.
    result = evaluate_request_relevance(
        "What is Genomic Biomarkers?",
        pp_title="What is Cancer?",
        controlled_question="What is Cancer?",
    )

    assert result.outcome is RequestRelevanceOutcome.NOT_RELEVANT


def test_fails_open_when_target_metadata_is_entirely_missing():
    # Missing pp_title/controlled_question is a data-availability gap,
    # not evidence the user's request is off-topic -- see resolver.py's
    # docstring for the full reasoning. Not observed in the real 239-entry
    # manifest projection; defensive only.
    result = evaluate_request_relevance(
        "anything at all",
        pp_title=None,
        controlled_question=None,
    )

    assert result.outcome is RequestRelevanceOutcome.RELEVANT
    assert result.score == 0.0


def test_score_is_always_between_zero_and_one():
    result = evaluate_request_relevance(
        "What is Gastric Cancer?",
        pp_title="What is Gastric Cancer?",
        controlled_question="What is Gastric Cancer?",
    )

    assert 0.0 <= result.score <= 1.0


def test_evaluate_request_relevance_is_deterministic():
    args = dict(
        message="What is Gastric Adenocarcinoma?",
        pp_title="What is Gastric Cancer?",
        controlled_question="What is Gastric Cancer?",
    )

    first = evaluate_request_relevance(**args)
    second = evaluate_request_relevance(**args)
    third = evaluate_request_relevance(**args)

    assert first.outcome == second.outcome == third.outcome
    assert first.score == second.score == third.score


def test_request_relevance_result_is_frozen():
    result = evaluate_request_relevance(
        "What is Cancer?", pp_title="What is Cancer?", controlled_question="What is Cancer?"
    )

    with pytest.raises(ValidationError):
        result.outcome = RequestRelevanceOutcome.NOT_RELEVANT


def test_request_relevance_outcome_vocabulary_is_distinct_from_other_layers():
    # Isolation convention already established by every other boundary in
    # this codebase (see e.g. test_validation_models.py) -- this
    # vocabulary must not literally collide with CaseResolutionOutcome or
    # CEROutcome member names.
    from safe_medical_ai.cases import CaseResolutionOutcome
    from safe_medical_ai.cer import CEROutcome

    relevance_members = set(RequestRelevanceOutcome.__members__)
    assert relevance_members.isdisjoint(set(CaseResolutionOutcome.__members__))
    assert relevance_members.isdisjoint(set(CEROutcome.__members__))
