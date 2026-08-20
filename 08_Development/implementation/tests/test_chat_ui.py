"""Tests for the Phase 6 Stage 2 Track 1A/1B/1C Controlled Chat UI.

Track 1A tests verify the page renders with the required elements. Track 1B
tests verify `/chat/query` reaches the same governed CER execution path
(PP-0002 + CKO) that `/cer/evaluate` already uses, rather than a placeholder
or a second implementation. Track 1C tests verify the added client-only
Situation -> Topic -> Question starter navigation aid, and that it never
bypasses the existing Send-driven `/chat/query` submission.
"""

from fastapi.testclient import TestClient

from safe_medical_ai.api.main import app

client = TestClient(app)


# --- /chat: browser page renders ---------------------------------------------


def test_chat_route_returns_an_html_page():
    response = client.get("/chat")

    assert response.status_code == 200
    assert "text/html" in response.headers["content-type"]


def test_chat_route_disables_browser_caching():
    # Defensive: a stale cached /chat response (with stale embedded catalog
    # data or stale navigation JS) must never be served from browser cache
    # across reloads/deploys.
    response = client.get("/chat")

    assert response.headers.get("cache-control") == "no-store"


def test_chat_page_contains_the_question_input_and_submit_control():
    html = client.get("/chat").text

    assert 'id="question-input"' in html
    assert 'id="send-button"' in html
    assert "Send" in html


def test_chat_page_contains_a_response_history_area():
    html = client.get("/chat").text

    assert 'id="chat-history"' in html


def test_chat_page_declares_idle_loading_and_error_states():
    html = client.get("/chat").text

    # Loading state toggling and an explicit error-status element/handler.
    assert "setLoading" in html
    assert 'id="chat-status"' in html
    assert "catch" in html  # fetch() error handling present


def test_chat_page_wires_the_submit_request_toward_the_chat_query_endpoint():
    html = client.get("/chat").text

    assert "/chat/query" in html
    assert "fetch(" in html


def test_chat_page_does_not_contain_pp_selection_or_navigation_logic():
    # The brief is explicit: no PP-selection/navigation logic belongs in the
    # UI shell -- the browser does not ask the user to choose a PP.
    html = client.get("/chat").text

    assert "population_id" not in html
    assert "PP-0002" not in html
    assert "PP-" not in html


# --- Track 1C: Situation -> Topic -> Question starter navigation aid -------


def test_chat_page_contains_situation_cards():
    # B06 Test A: exactly the five locked/approved Situations are present,
    # and the pre-B06 sixth Track 1C string (never an approved B06
    # Situation) is not.
    html = client.get("/chat").text

    assert "Not sure what to ask? Start with your situation." in html
    for situation in (
        "I was recently diagnosed",
        "I'm receiving treatment",
        "I'm preparing for surgery",
        "I'm concerned about recurrence",
        "I'm in follow-up",
    ):
        assert situation in html
    assert "I want to understand my cancer" not in html


def test_chat_page_situation_count_is_exactly_five():
    # B06 Test A: the embedded governed mapping itself carries exactly
    # five Situation entries -- not just five labels happening to appear
    # in the HTML text. `"label"` only occurs once per Situation entry
    # (mapping entries carry only situation_id/case_id, no label).
    html = client.get("/chat").text

    assert html.count('"label"') == 5


def test_chat_page_situation_selection_filters_topics_to_the_governed_mapping():
    # B06 Test D: a Situation click must filter the Topic list to only
    # that Situation's governed case_ids, reusing the existing CATALOG
    # and selectTopic() -- not an unfiltered reveal of all 239 entries
    # (the pre-B06 Track 1C behavior).
    html = client.get("/chat").text

    assert "activeAllowedCaseIds = SITUATION_CASE_IDS[situation.situation_id]" in html
    assert "renderTopics(filterText, allowedCaseIds)" in html
    assert "if (allowedCaseIds && !allowedCaseIds[item.case_id])" in html


def test_chat_page_random_topic_remains_unfiltered_by_situation():
    # B06 Test I: Random Topic (B05) must keep drawing from the full,
    # unfiltered CATALOG regardless of any Situation filter in effect --
    # confirmed by the handler explicitly clearing activeAllowedCaseIds
    # before rendering, and still calling the same selectTopic().
    html = client.get("/chat").text

    assert "activeAllowedCaseIds = null;" in html
    assert "selectTopic(item, activeButton)" in html


def test_chat_page_contains_two_tier_topic_and_question_starter_structure():
    html = client.get("/chat").text

    assert 'id="situation-list"' in html
    assert 'id="topic-panel"' in html
    assert 'id="topic-list"' in html
    assert 'id="topic-search"' in html
    assert 'id="starter-panel"' in html
    assert 'id="starter-list"' in html


def test_chat_page_contains_a_random_topic_control_wired_to_the_existing_catalog_and_selection():
    # B05: Random Topic is a navigation convenience only -- it must pick
    # from the SAME CATALOG the Topic list renders from (no second source
    # of truth) and route through the SAME selectTopic() function manual
    # Topic clicks already use (no new selection path).
    html = client.get("/chat").text

    assert 'id="random-topic-button"' in html
    assert "CATALOG[Math.floor(Math.random() * CATALOG.length)]" in html
    assert "selectTopic(item, activeButton)" in html


def test_chat_page_navigation_catalog_is_derived_from_the_real_manifest_projection():
    # Track 2: the catalog embedded in the page is NOT a small hand-written
    # list -- it is the real 239-case manifest projection (case_id,
    # pp_title, controlled_question), the same one EvaluationCaseResolver
    # consumes for execution.
    html = client.get("/chat").text

    assert '"case_id": "EC-0001"' in html or '"case_id":"EC-0001"' in html
    assert '"case_id": "EC-0239"' in html or '"case_id":"EC-0239"' in html
    assert html.count('"case_id"') >= 239


def test_chat_page_question_starter_populates_input_without_auto_submitting():
    html = client.get("/chat").text

    # The starter-chip click handler sets the existing input's value from
    # the selected topic's real controlled_question...
    assert "input.value = item.controlled_question" in html
    # ...and nothing on the page ever programmatically submits the form or
    # calls /chat/query outside the existing Send-button submit handler.
    assert ".submit(" not in html


def test_chat_page_selecting_a_topic_sets_case_identity_independent_of_editing():
    html = client.get("/chat").text

    # selectedCaseId is set only by selectTopic(); editing the textarea
    # never touches it.
    assert "selectedCaseId = item.case_id" in html


def test_chat_page_has_no_implicit_default_evaluation_case():
    # RC-5: no implicit default case on page load -- selectedCaseId starts
    # null and only becomes non-null via explicit Topic selection. Send is
    # blocked (and never reaches /chat/query) until a Topic is chosen.
    html = client.get("/chat").text

    assert "var selectedCaseId = null;" in html
    assert "CATALOG[0].case_id" not in html
    assert "CATALOG.length > 0 ? CATALOG[0]" not in html
    assert "if (!selectedCaseId)" in html
    assert "Please select an approved topic before sending." in html


def test_chat_ui_module_source_never_hard_codes_a_specific_case_literal():
    # RC-1 static check: no EC-XXXX literal anywhere in the UI module's
    # own source (as opposed to data flowing through it at runtime).
    import inspect

    from safe_medical_ai.api import chat_ui as chat_ui_module

    source = inspect.getsource(chat_ui_module)
    assert "EC-0002" not in source
    assert "EC-0001" not in source


def test_chat_page_preserves_existing_form_input_and_send_ids():
    html = client.get("/chat").text

    assert 'id="chat-form"' in html
    assert 'id="question-input"' in html
    assert 'id="send-button"' in html


def test_chat_page_shows_research_controlled_evaluation_identity_and_disclaimer():
    html = client.get("/chat").text

    assert "Research / Controlled Evaluation" in html
    assert "Not clinically validated. Not for clinical decision-making." in html


# --- /chat/query: input contract (Track 2: case_id is now required) -------


def test_chat_query_rejects_a_blank_message():
    response = client.post("/chat/query", json={"message": "", "case_id": "EC-0002"})

    assert response.status_code == 422


def test_chat_query_rejects_a_missing_message_field():
    response = client.post("/chat/query", json={"case_id": "EC-0002"})

    assert response.status_code == 422


def test_chat_query_rejects_a_missing_case_id_field():
    # RC-1: there is no default case_id -- omitting it is a client error,
    # never a silent fallback to any specific case.
    response = client.post("/chat/query", json={"message": "What is gastric cancer?"})

    assert response.status_code == 422


# --- /chat/query: reaches the real governed CER execution path -------------


def test_chat_query_reaches_the_real_governed_cer_execution_path():
    response = client.post("/chat/query", json={"message": "What is gastric cancer?", "case_id": "EC-0002"})

    assert response.status_code == 200
    body = response.json()
    assert body["status"] == "COMPLETED"
    assert isinstance(body["answer"], str) and body["answer"]
    assert "placeholder" not in body["answer"].lower()


def test_chat_query_answer_is_the_governed_generated_content():
    # DeterministicLocalProvider (already used by /cer/evaluate) always
    # returns this fixed, non-clinical text -- proving the real generation
    # stage of the existing CER path produced the answer, not new logic
    # invented in the chat endpoint.
    response = client.post("/chat/query", json={"message": "What is gastric cancer?", "case_id": "EC-0002"})

    body = response.json()
    assert body["answer"] == "Controlled Evaluation deterministic response. Not for clinical decision-making."


def test_chat_query_status_matches_the_same_outcome_as_cer_evaluate_for_the_same_question():
    question = "What is gastric cancer?"

    chat_response = client.post("/chat/query", json={"message": question, "case_id": "EC-0002"}).json()
    cer_response = client.post(
        "/cer/evaluate", json={"request_text": question, "case_id": "EC-0002"}
    ).json()

    assert chat_response["status"] == cer_response["outcome"] == "COMPLETED"
    assert cer_response["safety"] == "ALLOW"
    assert cer_response["validation"] == "VALID"


def test_chat_query_executes_a_non_pp_0002_case():
    # RC-1: chat_query is no longer fixed to EC-0002/PP-0002 -- proves the
    # exact user-facing endpoint the browser calls can reach a different
    # approved case end-to-end.
    response = client.post("/chat/query", json={"message": "test question", "case_id": "EC-0003"})

    assert response.status_code == 200
    assert response.json()["status"] == "COMPLETED"


def test_chat_query_unknown_case_fails_closed_via_the_chat_endpoint():
    response = client.post("/chat/query", json={"message": "test question", "case_id": "EC-9999"})

    assert response.status_code == 200
    body = response.json()
    assert body["status"] == "UNKNOWN_CASE"


def test_chat_query_ignores_an_extraneous_population_id_field():
    # ChatQueryRequest has no population field at all; an extra field from
    # a client is silently dropped by Pydantic and never reaches the CER
    # request. An invalid population_id here would break retrieval if it
    # were somehow honored -- COMPLETED proves it was not.
    response = client.post(
        "/chat/query",
        json={"message": "What is gastric cancer?", "case_id": "EC-0002", "population_id": "PP-9999"},
    )

    assert response.status_code == 200
    assert response.json()["status"] == "COMPLETED"


def test_chat_query_response_is_deterministic_and_independent_of_input_content():
    # The existing CER path (retrieval keyed only on the selected case's
    # fixed CKO target, and the deterministic provider) does not branch on
    # question content, so this invariant still holds under real execution.
    first = client.post("/chat/query", json={"message": "question A", "case_id": "EC-0002"}).json()
    second = client.post(
        "/chat/query", json={"message": "a completely different question B", "case_id": "EC-0002"}
    ).json()

    assert first == second


# --- existing Stage 1 boundary is preserved ---------------------------------


def test_existing_cer_evaluate_route_remains_registered_and_unchanged():
    paths = {route.path for route in app.routes}
    assert "/cer/evaluate" in paths
    assert "/chat" in paths
    assert "/chat/query" in paths


def test_existing_cer_evaluate_endpoint_behavior_is_unaffected_by_chat_integration():
    response = client.post(
        "/cer/evaluate", json={"request_text": "What is gastric cancer?", "case_id": "EC-0002"}
    )

    assert response.status_code == 200
    body = response.json()
    assert body["outcome"] == "COMPLETED"
    assert body["safety"] == "ALLOW"
    assert body["retrieval"] == "FOUND"
    assert body["validation"] == "VALID"


def test_health_endpoint_still_works():
    response = client.get("/health")
    assert response.status_code == 200
