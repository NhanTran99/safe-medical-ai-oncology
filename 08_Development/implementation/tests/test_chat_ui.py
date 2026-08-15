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
    html = client.get("/chat").text

    assert "Not sure what to ask? Start with your situation." in html
    for situation in (
        "I was recently diagnosed",
        "I'm receiving treatment",
        "I'm preparing for surgery",
        "I'm concerned about recurrence",
        "I'm in follow-up",
        "I want to understand my cancer",
    ):
        assert situation in html


def test_chat_page_contains_two_tier_topic_and_question_starter_structure():
    html = client.get("/chat").text

    assert 'id="situation-list"' in html
    assert 'id="topic-list"' in html
    assert 'id="starter-list"' in html
    # At least one concrete topic and one concrete question starter from
    # the navigation data.
    assert "Side effects" in html
    assert "What side effects can this treatment cause?" in html


def test_chat_page_question_starter_populates_input_without_auto_submitting():
    html = client.get("/chat").text

    # The starter-chip click handler sets the existing input's value...
    assert "input.value = starterText" in html
    # ...and nothing on the page ever programmatically submits the form or
    # calls /chat/query outside the existing Send-button submit handler.
    assert ".submit(" not in html


def test_chat_page_preserves_existing_form_input_and_send_ids():
    html = client.get("/chat").text

    assert 'id="chat-form"' in html
    assert 'id="question-input"' in html
    assert 'id="send-button"' in html


def test_chat_page_shows_research_controlled_evaluation_identity_and_disclaimer():
    html = client.get("/chat").text

    assert "Research / Controlled Evaluation" in html
    assert "Not clinically validated. Not for clinical decision-making." in html


# --- /chat/query: input contract (unchanged by Track 1B) -------------------


def test_chat_query_rejects_a_blank_message():
    response = client.post("/chat/query", json={"message": ""})

    assert response.status_code == 422


def test_chat_query_rejects_a_missing_message_field():
    response = client.post("/chat/query", json={})

    assert response.status_code == 422


# --- /chat/query: Track 1B reaches the real governed CER execution path ----


def test_chat_query_reaches_the_real_governed_cer_execution_path():
    response = client.post("/chat/query", json={"message": "What is gastric cancer?"})

    assert response.status_code == 200
    body = response.json()
    assert body["status"] == "COMPLETED"
    assert isinstance(body["answer"], str) and body["answer"]
    assert "placeholder" not in body["answer"].lower()
    assert "Track 1B" not in body["answer"]


def test_chat_query_answer_is_the_governed_generated_content():
    # DeterministicLocalProvider (already used by /cer/evaluate) always
    # returns this fixed, non-clinical text -- proving the real generation
    # stage of the existing CER path produced the answer, not new logic
    # invented in the chat endpoint.
    response = client.post("/chat/query", json={"message": "What is gastric cancer?"})

    body = response.json()
    assert body["answer"] == "Controlled Evaluation deterministic response. Not for clinical decision-making."


def test_chat_query_status_matches_the_same_outcome_as_cer_evaluate_for_the_same_question():
    question = "What is gastric cancer?"

    chat_response = client.post("/chat/query", json={"message": question}).json()
    cer_response = client.post(
        "/cer/evaluate", json={"request_text": question, "population_id": "PP-0002"}
    ).json()

    assert chat_response["status"] == cer_response["outcome"] == "COMPLETED"
    assert cer_response["safety"] == "ALLOW"
    assert cer_response["validation"] == "VALID"


def test_chat_query_ignores_a_population_id_field_and_still_executes_pp_0002():
    # ChatQueryRequest has no population/PP field; an extra field from a
    # client is silently dropped by Pydantic and never reaches the CER
    # request. An invalid population_id here would break retrieval if it
    # were honored -- COMPLETED proves it was not.
    response = client.post(
        "/chat/query", json={"message": "What is gastric cancer?", "population_id": "PP-9999"}
    )

    assert response.status_code == 200
    assert response.json()["status"] == "COMPLETED"


def test_chat_query_response_is_deterministic_and_independent_of_input_content():
    # The existing CER path (retrieval keyed only on the fixed PP-0002/CKO
    # target, and the deterministic provider) does not branch on question
    # content, so this Track 1A invariant still holds under real execution.
    first = client.post("/chat/query", json={"message": "question A"}).json()
    second = client.post("/chat/query", json={"message": "a completely different question B"}).json()

    assert first == second


# --- existing Stage 1 boundary is preserved ---------------------------------


def test_existing_cer_evaluate_route_remains_registered_and_unchanged():
    paths = {route.path for route in app.routes}
    assert "/cer/evaluate" in paths
    assert "/chat" in paths
    assert "/chat/query" in paths


def test_existing_cer_evaluate_endpoint_behavior_is_unaffected_by_chat_integration():
    response = client.post(
        "/cer/evaluate", json={"request_text": "What is gastric cancer?", "population_id": "PP-0002"}
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
