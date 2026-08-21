"""Phase 6 Stage 2 Track 2 tests: generic Evaluation Case execution.

Proves `/cer/evaluate` and `/chat/query` execute through the same governed
CER path for multiple, structurally different approved cases -- not just
PP-0002 -- and fail closed on invalid/unknown cases without ever falling
back to PP-0002. `test_app_cer.py` and `test_chat_ui.py`'s existing
PP-0002-specific tests are exercised too, via `case_id="EC-0002"`, so
Track 1's proven behavior remains covered under the new contract.
"""

import inspect

from fastapi.testclient import TestClient

from safe_medical_ai.api import main as main_module
from safe_medical_ai.api.main import app

client = TestClient(app)


# --- Gate 3: same governed CER mechanism across structurally different PP --


def test_cer_evaluate_executes_pp_0001_via_ec_0001():
    # B12: real, on-topic, existing governed controlled_question for this
    # exact case_id -- a semantically meaningless placeholder is no
    # longer sufficient once the selected-PP request-relevance boundary
    # exists (see relevance/README.md's test-fixture contract note).
    response = client.post(
        "/cer/evaluate", json={"request_text": "What is Cancer?", "case_id": "EC-0001"}
    )

    assert response.status_code == 200
    body = response.json()
    assert body["outcome"] == "COMPLETED"
    assert body["safety"] == "ALLOW"
    assert body["retrieval"] == "FOUND"
    assert body["validation"] == "VALID"


def test_cer_evaluate_executes_pp_0002_via_ec_0002():
    # B12: real, on-topic controlled_question -- see the note above.
    response = client.post(
        "/cer/evaluate", json={"request_text": "What is Gastric Cancer?", "case_id": "EC-0002"}
    )

    assert response.status_code == 200
    assert response.json()["outcome"] == "COMPLETED"


def test_cer_evaluate_executes_pp_0003_via_ec_0003():
    # B12: real, on-topic controlled_question -- see the note above.
    response = client.post(
        "/cer/evaluate", json={"request_text": "What is Gastric Adenocarcinoma?", "case_id": "EC-0003"}
    )

    assert response.status_code == 200
    assert response.json()["outcome"] == "COMPLETED"


def test_cer_evaluate_executes_pp_0147_via_ec_0147():
    # B12: real, on-topic controlled_question -- see the note above.
    response = client.post(
        "/cer/evaluate",
        json={
            "request_text": (
                "Please explain BS3 (Well-Established Functional Studies Show "
                "No Deleterious Effect on Gene or Gene Product)."
            ),
            "case_id": "EC-0147",
        },
    )

    assert response.status_code == 200
    body = response.json()
    assert body["outcome"] == "COMPLETED"
    assert body["retrieval_results"] == 1


def test_cer_evaluate_executes_pp_0239_via_ec_0239():
    # B12: real, on-topic controlled_question -- see the note above.
    response = client.post(
        "/cer/evaluate",
        json={"request_text": "Please explain Genomic Biomarkers.", "case_id": "EC-0239"},
    )

    assert response.status_code == 200
    assert response.json()["outcome"] == "COMPLETED"


def test_different_cases_retrieve_the_correct_distinct_pp_artifact():
    # RC-4: assert actual retrieved artifact/source identity, not merely
    # request/case-id cardinality -- proves EC-0001/EC-0003/EC-0147 each
    # retrieve their own genuinely distinct PP-000N CKO artifact, not a
    # PP-0002 (or any other) result reused/echoed back.
    from safe_medical_ai.api.main import ControlledEvaluationRequest, _run_controlled_evaluation

    expectations = {
        "EC-0001": "PP-0001",
        "EC-0003": "PP-0003",
        "EC-0147": "PP-0147",
    }
    # B12: real, on-topic controlled_question per case_id -- see the note
    # in the tests above.
    controlled_questions = {
        "EC-0001": "What is Cancer?",
        "EC-0003": "What is Gastric Adenocarcinoma?",
        "EC-0147": (
            "Please explain BS3 (Well-Established Functional Studies Show "
            "No Deleterious Effect on Gene or Gene Product)."
        ),
    }

    source_paths: dict[str, str] = {}
    for case_id, expected_pp in expectations.items():
        result = _run_controlled_evaluation(
            ControlledEvaluationRequest(request_text=controlled_questions[case_id], case_id=case_id)
        )
        assert result.retrieval_response is not None
        assert result.retrieval_response.outcome.value == "FOUND"
        assert len(result.retrieval_response.results) == 1

        candidate = result.retrieval_response.results[0]
        assert candidate.population_id == expected_pp
        assert candidate.artifact_type.value == "CKO"
        # The actual retrieved source path -- the real controlled-repository
        # pointer, not a synthesized/guessed string -- contains the correct
        # PP identity and the correct canonical CKO filename.
        assert f"{expected_pp} " in candidate.source_path or f"{expected_pp}/" in candidate.source_path
        assert candidate.source_path.endswith("01_CKO.md")

        source_paths[case_id] = candidate.source_path

    # Every retrieved source path is genuinely distinct -- no two cases
    # resolved to the same underlying artifact.
    assert len(set(source_paths.values())) == 3
    for case_id, expected_pp in expectations.items():
        for other_case_id, other_path in source_paths.items():
            if other_case_id == case_id:
                continue
            assert expected_pp not in other_path


# --- Gate 1 (behavioral half): case_id, not population_id, drives execution -


def test_cer_evaluate_rejects_the_old_population_id_contract():
    # The pre-Track-2 request shape is now a 422 -- case_id is required and
    # population_id is not part of the contract at all.
    response = client.post(
        "/cer/evaluate", json={"request_text": "test question", "population_id": "PP-0002"}
    )
    assert response.status_code == 422


def test_cer_evaluate_ignores_an_extraneous_population_id_field():
    # Even if a caller supplies both, population_id is not read -- only
    # case_id determines the executed PP (Pydantic drops unknown extras).
    # B12: real, on-topic controlled_question for EC-0003 -- see the note
    # in the tests above.
    response = client.post(
        "/cer/evaluate",
        json={
            "request_text": "What is Gastric Adenocarcinoma?",
            "case_id": "EC-0003",
            "population_id": "PP-0002",
        },
    )
    assert response.status_code == 200
    body = response.json()
    assert body["outcome"] == "COMPLETED"


# --- Gate 4: fail closed at the API boundary, never falls back to PP-0002 --


def test_cer_evaluate_unknown_case_fails_closed_without_pp_0002_fallback():
    response = client.post("/cer/evaluate", json={"request_text": "test question", "case_id": "EC-9999"})

    assert response.status_code == 200
    body = response.json()
    assert body["outcome"] == "CASE_NOT_APPROVED"
    assert body["case_resolution"] == "UNKNOWN_CASE"
    assert body["retrieval"] is None
    assert body["retrieval_results"] == 0
    assert body["validation"] is None


def test_cer_evaluate_malformed_case_id_fails_closed():
    response = client.post("/cer/evaluate", json={"request_text": "test question", "case_id": "not-a-case"})

    assert response.status_code == 200
    body = response.json()
    assert body["outcome"] == "CASE_NOT_APPROVED"
    assert body["case_resolution"] == "MALFORMED_CASE_ID"


def test_cer_evaluate_missing_case_id_is_rejected():
    response = client.post("/cer/evaluate", json={"request_text": "test question"})
    assert response.status_code == 422


def test_chat_query_unknown_case_context_never_silently_becomes_pp_0002():
    # chat_query's own default is EC-0002 (documented, not a fallback from
    # failure) -- this proves the underlying mechanism itself, reached the
    # same way /chat/query reaches it, fails closed rather than silently
    # substituting PP-0002 for a bad case_id.
    from safe_medical_ai.api.main import ControlledEvaluationRequest, _run_controlled_evaluation
    from safe_medical_ai.cases import CaseResolutionOutcome, CaseResolutionResult

    outcome = _run_controlled_evaluation(
        ControlledEvaluationRequest(request_text="test question", case_id="EC-9999")
    )
    assert isinstance(outcome, CaseResolutionResult)
    assert outcome.outcome is CaseResolutionOutcome.UNKNOWN_CASE
    assert outcome.case is None


# --- Gate 1 (static half): no active generic execution path is fixed to PP-0002 -


def test_controlled_evaluation_request_no_longer_has_a_population_id_field():
    from safe_medical_ai.api.main import ControlledEvaluationRequest

    assert "population_id" not in ControlledEvaluationRequest.model_fields
    assert "case_id" in ControlledEvaluationRequest.model_fields


def test_chat_query_request_requires_case_id_with_no_default():
    # RC-1: case_id is required, not optional/defaulted -- the browser's
    # controlled navigation catalog always supplies it (see test_chat_ui.py).
    from safe_medical_ai.api.main import ChatQueryRequest

    assert "population_id" not in ChatQueryRequest.model_fields
    assert set(ChatQueryRequest.model_fields) == {"message", "case_id"}
    assert ChatQueryRequest.model_fields["case_id"].is_required()


def test_run_controlled_evaluation_source_contains_no_hard_coded_pp_0002_execution_constraint():
    source = inspect.getsource(main_module)
    assert 'population_id="PP-0002"' not in source
    assert 'default="PP-0002"' not in source
    assert 'pattern=r"^PP-0002$"' not in source


def test_main_source_contains_no_hard_coded_default_case_literal():
    # RC-1: the earlier _CHAT_UI_DEFAULT_CASE_ID = "EC-0002" pattern (a
    # hard-coded execution target one level up from population_id) must
    # not exist anywhere in the active generic execution path.
    source = inspect.getsource(main_module)
    assert "_CHAT_UI_DEFAULT_CASE_ID" not in source
    assert '"EC-0002"' not in source
    assert "'EC-0002'" not in source


# --- Gate 5 (evidence): resolved case/PP identity flows into CER evidence --


def test_evidence_provenance_reflects_the_resolved_pp_not_pp_0002():
    from safe_medical_ai.api.main import ControlledEvaluationRequest, _run_controlled_evaluation

    # B12: real, on-topic controlled_question for EC-0003 -- see the note
    # in the tests above.
    result = _run_controlled_evaluation(
        ControlledEvaluationRequest(request_text="What is Gastric Adenocarcinoma?", case_id="EC-0003")
    )
    assert result.assembly_result is not None
    assert result.assembly_result.package is not None
    item = result.assembly_result.package.evidence[0]
    assert item.population_id == "PP-0003"
    assert "PP-0003" in item.provenance.source_id
    assert "PP-0002" not in item.provenance.source_id


def test_traceability_ids_reflect_the_resolved_pp():
    from safe_medical_ai.api.main import ControlledEvaluationRequest, _run_controlled_evaluation

    # B12: real, on-topic controlled_question for EC-0147 -- see the note
    # in the tests above.
    result = _run_controlled_evaluation(
        ControlledEvaluationRequest(
            request_text=(
                "Please explain BS3 (Well-Established Functional Studies Show "
                "No Deleterious Effect on Gene or Gene Product)."
            ),
            case_id="EC-0147",
        )
    )
    assert result.retrieval_response.request.population_id == "PP-0147"


# --- Track 3 BATCH 01: actual governed clinical content reaches evidence ---


def test_real_pp_0003_cko_content_reaches_the_assembled_evidence_package():
    # Proves the real repository artifact's actual text -- not merely its
    # identity/provenance -- flows through the real, unmocked retrieval and
    # assembly boundary for a real approved case (EC-0003 -> PP-0003).
    from pathlib import Path

    from safe_medical_ai.api.main import ControlledEvaluationRequest, _run_controlled_evaluation

    repo_root = Path(__file__).resolve().parents[3]
    cko_path = (
        repo_root
        / "03_Clinical_Knowledge"
        / "population"
        / "population_packages"
        / "PP-0003 — What is Gastric Adenocarcinoma"
        / "01_CKO.md"
    )
    expected_content = cko_path.read_text(encoding="utf-8")
    assert expected_content  # sanity: the real fixture artifact is non-empty

    # B12: real, on-topic controlled_question for EC-0003 -- see the note
    # in the tests above.
    result = _run_controlled_evaluation(
        ControlledEvaluationRequest(request_text="What is Gastric Adenocarcinoma?", case_id="EC-0003")
    )

    assert result.assembly_result is not None
    assert result.assembly_result.package is not None
    item = result.assembly_result.package.evidence[0]
    assert item.content == expected_content


# --- B12: selected-PP request relevance hard block --------------------------


def test_not_relevant_request_never_constructs_cer_request_or_calls_cer_runtime(monkeypatch):
    from safe_medical_ai.api.main import ControlledEvaluationRequest, _run_controlled_evaluation
    from safe_medical_ai.relevance import RequestRelevanceOutcome, RequestRelevanceResult

    class _ExplodingCERRuntime:
        def __init__(self, *args, **kwargs):
            raise AssertionError("CERRuntime must never be constructed for a NOT_RELEVANT request")

    monkeypatch.setattr(main_module, "CERRuntime", _ExplodingCERRuntime)

    # EC-0002's own topic is "What is Gastric Cancer?" -- paired here with
    # EC-0239's real, materially different governed controlled_question.
    # Both strings are real governed text already shipped in the frozen
    # manifest; only the pairing (not the content) is synthetic -- no
    # clinical content is invented.
    result = _run_controlled_evaluation(
        ControlledEvaluationRequest(
            request_text="Please explain Genomic Biomarkers.",
            case_id="EC-0002",
        )
    )

    assert isinstance(result, RequestRelevanceResult)
    assert result.outcome is RequestRelevanceOutcome.NOT_RELEVANT


def test_not_relevant_request_never_selects_or_invokes_a_provider(monkeypatch):
    from safe_medical_ai.api.main import ControlledEvaluationRequest, _run_controlled_evaluation

    def _fail_if_called():
        raise AssertionError("_select_provider() must never be called for a NOT_RELEVANT request")

    monkeypatch.setattr(main_module, "_select_provider", _fail_if_called)

    result = _run_controlled_evaluation(
        ControlledEvaluationRequest(
            request_text="Please explain Genomic Biomarkers.",
            case_id="EC-0002",
        )
    )

    assert result.outcome.value == "NOT_RELEVANT"


def test_relevant_request_still_reaches_completed_unaffected():
    response = client.post(
        "/cer/evaluate", json={"request_text": "What is Gastric Cancer?", "case_id": "EC-0002"}
    )

    assert response.status_code == 200
    assert response.json()["outcome"] == "COMPLETED"


def test_cer_evaluate_returns_not_relevant_for_a_mismatched_request():
    response = client.post(
        "/cer/evaluate",
        json={"request_text": "Please explain Genomic Biomarkers.", "case_id": "EC-0002"},
    )

    assert response.status_code == 200
    body = response.json()
    assert body["outcome"] == "NOT_RELEVANT"
    assert body["retrieval"] is None
    assert body["retrieval_results"] == 0
    assert body["generation"] is None
    assert body["validation"] is None


# --- B11 bounded verification surface: case-resolution failures also never
# reach CERRuntime/provider selection, mirroring the NOT_RELEVANT guards
# above. Resolution (`_default_case_resolver().resolve`) runs before the
# B12 relevance check, so this is the same early-return shape, just for
# CaseResolutionOutcome.UNKNOWN_CASE / MALFORMED_CASE_ID instead of
# RequestRelevanceOutcome.NOT_RELEVANT. ------------------------------------


def test_unknown_case_never_constructs_cer_request_or_calls_cer_runtime(monkeypatch):
    from safe_medical_ai.api.main import ControlledEvaluationRequest, _run_controlled_evaluation
    from safe_medical_ai.cases import CaseResolutionOutcome, CaseResolutionResult

    class _ExplodingCERRuntime:
        def __init__(self, *args, **kwargs):
            raise AssertionError("CERRuntime must never be constructed for an UNKNOWN_CASE request")

    monkeypatch.setattr(main_module, "CERRuntime", _ExplodingCERRuntime)

    result = _run_controlled_evaluation(
        ControlledEvaluationRequest(request_text="What is Cancer?", case_id="EC-9999")
    )

    assert isinstance(result, CaseResolutionResult)
    assert result.outcome is CaseResolutionOutcome.UNKNOWN_CASE


def test_unknown_case_never_selects_or_invokes_a_provider(monkeypatch):
    from safe_medical_ai.api.main import ControlledEvaluationRequest, _run_controlled_evaluation

    def _fail_if_called():
        raise AssertionError("_select_provider() must never be called for an UNKNOWN_CASE request")

    monkeypatch.setattr(main_module, "_select_provider", _fail_if_called)

    result = _run_controlled_evaluation(
        ControlledEvaluationRequest(request_text="What is Cancer?", case_id="EC-9999")
    )

    assert result.outcome.value == "UNKNOWN_CASE"


def test_malformed_case_id_never_constructs_cer_request_or_calls_cer_runtime(monkeypatch):
    from safe_medical_ai.api.main import ControlledEvaluationRequest, _run_controlled_evaluation
    from safe_medical_ai.cases import CaseResolutionOutcome, CaseResolutionResult

    class _ExplodingCERRuntime:
        def __init__(self, *args, **kwargs):
            raise AssertionError("CERRuntime must never be constructed for a MALFORMED_CASE_ID request")

    monkeypatch.setattr(main_module, "CERRuntime", _ExplodingCERRuntime)

    result = _run_controlled_evaluation(
        ControlledEvaluationRequest(request_text="What is Cancer?", case_id="not-a-case")
    )

    assert isinstance(result, CaseResolutionResult)
    assert result.outcome is CaseResolutionOutcome.MALFORMED_CASE_ID


def test_malformed_case_id_never_selects_or_invokes_a_provider(monkeypatch):
    from safe_medical_ai.api.main import ControlledEvaluationRequest, _run_controlled_evaluation

    def _fail_if_called():
        raise AssertionError("_select_provider() must never be called for a MALFORMED_CASE_ID request")

    monkeypatch.setattr(main_module, "_select_provider", _fail_if_called)

    result = _run_controlled_evaluation(
        ControlledEvaluationRequest(request_text="What is Cancer?", case_id="not-a-case")
    )

    assert result.outcome.value == "MALFORMED_CASE_ID"
