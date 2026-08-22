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


def test_root_route_renders_the_same_chat_page_as_chat():
    # 0036: `/` is the same chat_ui() handler as `/chat` (stacked route
    # decorators, not a redirect and not a duplicated implementation) --
    # both must render identically, and `/chat` must keep working unchanged.
    root_response = client.get("/")
    chat_response = client.get("/chat")

    assert root_response.status_code == 200
    assert root_response.text == chat_response.text


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
    # B12: real, on-topic controlled_question for EC-0003 -- a
    # semantically meaningless placeholder is no longer sufficient once
    # the selected-PP request-relevance boundary exists.
    response = client.post(
        "/chat/query", json={"message": "What is Gastric Adenocarcinoma?", "case_id": "EC-0003"}
    )

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


# --- B08: bounded same-session follow-up ------------------------------------


def test_chat_page_contains_a_hidden_followup_label():
    # AC-01: the follow-up affordance exists, but is not shown until a
    # real exchange has completed (RC-5-style: no implicit "you can follow
    # up now" before anything has actually happened).
    html = client.get("/chat").text

    assert 'id="followup-label"' in html
    assert "Continue exploring" in html


def test_chat_page_reveals_followup_label_only_after_a_completed_exchange():
    html = client.get("/chat").text

    assert '<p id="followup-label" hidden>Continue exploring</p>' in html
    assert "followupLabel.hidden = false;" in html


def test_chat_page_resets_followup_label_on_topic_change():
    # A newly selected topic (manual, Situation-filtered, or Random Topic
    # -- all funnel through selectTopic()) must not carry over a stale
    # "you're following up" affordance from a different case_id.
    html = client.get("/chat").text

    assert "followupLabel.hidden = true;" in html


def test_chat_page_follow_up_context_is_gated_on_the_same_case_id():
    # AC-03/AC-08: bounded context is only reused when the follow-up is
    # asked about the SAME case_id that produced it -- never fabricated
    # or carried across an unrelated topic/case.
    html = client.get("/chat").text

    assert "function hasFollowupContext()" in html
    assert "lastCaseId === selectedCaseId" in html


def test_chat_page_follow_up_composes_bounded_prior_exchange_only():
    # AC-02/AC-03: the composed follow-up text carries exactly one prior
    # question/answer pair -- not an unbounded history.
    html = client.get("/chat").text

    assert "[Previous question]" in html
    assert "[Previous answer]" in html
    assert "[Follow-up question]" in html


def test_chat_page_follow_up_never_updates_context_on_a_failed_exchange():
    # AC-08: a failed/errored turn must not overwrite the last known-good
    # follow-up context with nothing.
    html = client.get("/chat").text

    then_index = html.index("lastQuestion = question;")
    catch_index = html.index(".catch(function (err) {")
    assert then_index < catch_index, (
        "lastQuestion/lastAnswer must only be set in the success (.then) "
        "branch, before the .catch branch"
    )


def test_chat_page_follow_up_still_uses_only_the_existing_chat_query_endpoint():
    # AC-04/AC-05: no second/alternate endpoint or direct provider call is
    # introduced for the follow-up path.
    html = client.get("/chat").text

    assert html.count('fetch("/chat/query"') == 1


def test_chat_query_accepts_a_composed_follow_up_and_completes():
    # Simulates exactly what the browser sends for a genuine follow-up
    # (built the same way hasFollowupContext()'s composed text is) --
    # proves the existing /chat/query contract requires no change: the
    # bounded prior context is carried entirely inside the existing
    # `message` field.
    initial = client.post(
        "/chat/query", json={"message": "What is TNM staging?", "case_id": "EC-0008"}
    )
    assert initial.status_code == 200
    assert initial.json()["status"] == "COMPLETED"

    composed = (
        "[Previous question]: What is TNM staging?\n"
        f"[Previous answer]: {initial.json()['answer']}\n"
        "[Follow-up question]: I still don't understand this part."
    )
    follow_up = client.post(
        "/chat/query", json={"message": composed, "case_id": "EC-0008"}
    )

    assert follow_up.status_code == 200
    body = follow_up.json()
    assert body["status"] == "COMPLETED"
    assert body["answer"]


def test_chat_page_uses_request_time_case_id_not_live_selected_case_id_for_followup_context():
    # B08 race-condition regression (D-F2). selectedCaseId is never
    # disabled/locked while a request is pending -- Topic/Situation/Random
    # Topic controls remain clickable during setLoading(true) -- so the
    # following sequence is possible:
    #   1. Case A selected -> selectedCaseId = A.
    #   2. Question A submitted. A per-request `requestCaseId` is captured
    #      from selectedCaseId at THIS moment (A), before the fetch is
    #      sent, and used for the outbound case_id.
    #   3. While Case A's request is still pending, the user switches to
    #      Case B -> selectedCaseId becomes B.
    #   4. Case A's response arrives. If the response handler re-read the
    #      live selectedCaseId here, lastCaseId would become B and Case
    #      A's Q/A would be wrongly recorded as valid follow-up context
    #      for Case B. The fix stores lastCaseId from the SAME
    #      requestCaseId captured in step 2, so it stays A regardless of
    #      what selectedCaseId has since become.
    #   5. A later follow-up asked while Case B is selected must NOT
    #      inherit Case A's Q/A: hasFollowupContext()'s
    #      `lastCaseId(A) === selectedCaseId(B)` check correctly
    #      evaluates false.
    #
    # This is a structural regression guard over the exact code shape
    # that prevents the race (the existing test suite's established way
    # of covering client-side JS behavior, since no async-DOM-timing test
    # runner is part of this repository's existing test framework).
    html = client.get("/chat").text

    assert "var requestCaseId = selectedCaseId;" in html
    assert "case_id: requestCaseId" in html
    assert "lastCaseId = requestCaseId;" in html
    # The specific regression: selectedCaseId must never be read again
    # inside the response handler to set lastCaseId.
    assert "lastCaseId = selectedCaseId;" not in html


# --- B09: bounded evidence transparency (Sources) ---------------------------


def test_chat_query_response_includes_the_governed_primary_source_set():
    # EC-0001 -> PP-0001; PP-0001's governed Registry value is
    # "NCI + ACS + NCCN Patient" (Population Registry2 sheet, Primary
    # Source Set column) -- proves a valid Registry mapping produces the
    # expected human-readable source list.
    response = client.post("/chat/query", json={"message": "What is Cancer?", "case_id": "EC-0001"})

    assert response.status_code == 200
    body = response.json()
    assert body["status"] == "COMPLETED"
    assert body["sources"] == ["NCI", "ACS", "NCCN Patient"]


def test_chat_query_sources_are_human_readable_never_a_pp_identifier():
    response = client.post("/chat/query", json={"message": "What is gastric cancer?", "case_id": "EC-0002"})

    body = response.json()
    assert body["sources"]
    for source in body["sources"]:
        assert not source.startswith("PP-")
        assert "PP-" not in source


def test_chat_query_sources_correspond_to_the_population_id_actually_used():
    # EC-0001 -> PP-0001 and EC-0147 -> PP-0147 have distinct governed
    # Primary Source Set values -- the returned sources must track whichever
    # PP's evidence actually produced the answer, never a fixed/shared value.
    # B12: real, on-topic controlled_question per case_id -- see the note
    # above.
    first = client.post(
        "/chat/query", json={"message": "What is Cancer?", "case_id": "EC-0001"}
    ).json()
    second = client.post(
        "/chat/query",
        json={
            "message": (
                "Please explain BS3 (Well-Established Functional Studies Show "
                "No Deleterious Effect on Gene or Gene Product)."
            ),
            "case_id": "EC-0147",
        },
    ).json()

    assert first["sources"] == ["NCI", "ACS", "NCCN Patient"]
    assert second["sources"] == [
        "ACMG",
        "AMP",
        "ClinGen SVI",
        "ClinGen VCEPs",
        "CAP",
        "NCI",
        "NCCN",
        "ASCO",
        "ACS",
        "ESMO",
    ]
    assert first["sources"] != second["sources"]


def test_chat_query_sources_is_none_when_case_resolution_fails():
    # No evidence/PP identity is ever associated with an unresolved case --
    # sources must be None (not [], which is reserved for "evidence was
    # used but no valid source mapping exists"), and no separate UI note
    # is warranted since the CaseResolutionResult message already explains
    # the failure.
    response = client.post("/chat/query", json={"message": "irrelevant", "case_id": "EC-9999"})

    body = response.json()
    assert body["status"] == "UNKNOWN_CASE"
    assert body["sources"] is None


def test_chat_query_sources_falls_back_honestly_when_no_registry_mapping_exists(monkeypatch):
    # The real Registry has 239/239 coverage (no PP is naturally missing a
    # mapping), so the "missing mapping" branch is exercised deterministically
    # by monkeypatching the registry loader for this one request -- the rest
    # of the real governed CER path (retrieval/assembly/integration/
    # generation/validation) still runs unmodified and unmocked.
    import safe_medical_ai.api.main as main_module

    monkeypatch.setattr(main_module, "_load_primary_source_registry", lambda: {})

    response = client.post("/chat/query", json={"message": "What is Cancer?", "case_id": "EC-0001"})

    body = response.json()
    assert body["status"] == "COMPLETED"
    assert body["answer"]
    # Real evidence was used for generation, but the (mocked) Registry has
    # no mapping -- the empty-list "unavailable" state, never None (which
    # would imply no evidence was used at all) and never a fabricated value.
    assert body["sources"] == []


def test_format_primary_source_set_splits_on_registry_separator_without_altering_tokens():
    from safe_medical_ai.api.main import _format_primary_source_set

    assert _format_primary_source_set("NCI + ACS + NCCN Patient + ESMO") == [
        "NCI",
        "ACS",
        "NCCN Patient",
        "ESMO",
    ]
    # A stray trailing "." already present in a small number of real
    # Registry values is preserved verbatim, never silently "corrected" --
    # only surrounding whitespace is trimmed.
    assert _format_primary_source_set("NCCN + ESMO + ASCO + NCI.") == [
        "NCCN",
        "ESMO",
        "ASCO",
        "NCI.",
    ]


def test_chat_page_renders_sources_in_an_element_distinct_from_the_answer():
    # Structural regression guard (this repository's established way of
    # covering client-side JS behavior -- see the D-F2 test above): the
    # Sources line must be its own element/class, not appended into the
    # `.chat-message.assistant` bubble's text.
    html = client.get("/chat").text

    assert "chat-sources" in html
    assert "function appendSources(sources)" in html
    assert "data.sources" in html
    assert "Evidence information unavailable" in html


def test_chat_query_response_still_returns_answer_and_status_alongside_sources():
    # Existing callers reading only `answer`/`status` remain unaffected --
    # `sources` is a purely additive field.
    response = client.post("/chat/query", json={"message": "What is gastric cancer?", "case_id": "EC-0002"})

    body = response.json()
    assert isinstance(body["answer"], str) and body["answer"]
    assert isinstance(body["status"], str) and body["status"]
    assert "sources" in body


# --- B11: bounded answer-boundary UX + follow-up-context gating ------------


def test_chat_page_renders_a_boundary_notice_for_non_completed_statuses():
    # Structural regression guard (this repository's established way of
    # covering client-side JS behavior -- see the D-F2 test above): a
    # dedicated element/function/CSS class exists for non-COMPLETED
    # statuses, distinct from the plain assistant-answer bubble.
    html = client.get("/chat").text

    assert "chat-boundary" in html
    assert "function appendBoundaryNotice(status)" in html
    assert 'if (data.status !== "COMPLETED")' in html
    assert "appendBoundaryNotice(data.status);" in html


def test_chat_page_boundary_messages_distinguish_status_categories():
    # Locked requirement: do not collapse every non-COMPLETED status into
    # one generic "out of scope" label -- SAFE_FALLBACK (evidence-absent),
    # a case-resolution failure, and a technical pipeline failure must
    # each carry genuinely distinct, bounded, non-clinical wording, never
    # the raw internal status token.
    html = client.get("/chat").text

    assert "SAFE_FALLBACK:" in html
    assert "No governed evidence was available to answer this question." in html
    assert "UNKNOWN_CASE:" in html
    assert "This question could not be matched to an approved topic." in html
    assert "RETRIEVAL_FAILURE:" in html
    assert "This request could not be completed due to a system issue. Please try again." in html
    # Every distinct message text must appear at least once -- confirms
    # SAFE_FALLBACK/UNKNOWN_CASE/RETRIEVAL_FAILURE are not all mapped to
    # one identical string.
    boundary_messages = {
        "No governed evidence was available to answer this question.",
        "This question could not be matched to an approved topic.",
        "This request could not be completed due to a system issue. Please try again.",
    }
    assert len(boundary_messages) == 3


def test_chat_page_never_shows_a_generic_out_of_scope_label_for_every_status():
    html = client.get("/chat").text

    assert "OUT-OF-SCOPE" not in html
    assert "OUT OF SCOPE" not in html


def test_chat_page_boundary_notice_does_not_replace_the_governed_answer_text():
    # The existing appendMessage("assistant", data.answer) call for the
    # governed answer text is untouched -- the boundary notice is only an
    # additional, separate element, never a substitute for it.
    html = client.get("/chat").text

    assert 'appendMessage("assistant", data.answer);' in html


def test_chat_page_follow_up_context_is_only_updated_for_completed_status():
    # B11 fix: the previously-unconditional follow-up-context update is
    # now gated on data.status === "COMPLETED", so a SAFE_FALLBACK/failure
    # response is never recorded as valid prior substantive context for a
    # later follow-up question.
    html = client.get("/chat").text

    assert 'if (data.status === "COMPLETED") {' in html
    assert "lastQuestion = question;" in html
    assert "followupLabel.hidden = false;" in html


def test_chat_query_reaches_the_real_governed_cer_execution_path_unaffected_by_b11():
    # B11 is a UI-only change -- the existing /chat/query backend contract
    # and behavior (B04/B08/B09) must be completely unaffected.
    response = client.post("/chat/query", json={"message": "What is gastric cancer?", "case_id": "EC-0002"})

    assert response.status_code == 200
    body = response.json()
    assert body["status"] == "COMPLETED"
    assert isinstance(body["answer"], str) and body["answer"]
    assert body["sources"] == ["NCI", "ACS", "NCCN Patient", "ESMO"]


def test_chat_query_unknown_case_status_is_unaffected_by_b11():
    # A representative non-COMPLETED status: the backend's own outcome
    # value/semantics are completely unchanged by the UI-only B11 amendment.
    response = client.post("/chat/query", json={"message": "irrelevant", "case_id": "EC-9999"})

    assert response.status_code == 200
    body = response.json()
    assert body["status"] == "UNKNOWN_CASE"
    assert body["sources"] is None


# --- B12: selected-PP request relevance -------------------------------------


def test_chat_query_returns_not_relevant_for_a_mismatched_request():
    # EC-0002's own topic is "What is Gastric Cancer?" -- paired here with
    # EC-0239's real, materially different governed controlled_question.
    # Both strings are real governed text; only the pairing is synthetic.
    response = client.post(
        "/chat/query",
        json={"message": "Please explain Genomic Biomarkers.", "case_id": "EC-0002"},
    )

    assert response.status_code == 200
    body = response.json()
    assert body["status"] == "NOT_RELEVANT"
    assert body["sources"] is None
    assert "Genomic Biomarkers" not in body["answer"]


def test_chat_query_relevant_request_still_completes_unaffected():
    response = client.post(
        "/chat/query", json={"message": "What is Gastric Cancer?", "case_id": "EC-0002"}
    )

    assert response.status_code == 200
    assert response.json()["status"] == "COMPLETED"


def test_chat_page_renders_the_not_relevant_boundary_mapping():
    # B11's existing STATUS_BOUNDARY_MESSAGES lookup gains exactly one
    # additive entry -- no other B11 code/gating logic changes.
    html = client.get("/chat").text

    assert "NOT_RELEVANT:" in html
    assert "This request does not appear to relate to the selected topic." in html
    # The B11 gating logic itself (from the prior batch) is unmodified.
    assert 'if (data.status !== "COMPLETED")' in html
    assert 'if (data.status === "COMPLETED") {' in html


def test_chat_query_b08_composed_followup_is_exempt_from_relevance_check():
    # A short, legitimate follow-up ("Can you clarify?") shares no
    # significant vocabulary with any PP's title/question in isolation --
    # B08's own existing gating (hasFollowupContext(), only ever true
    # after a real prior COMPLETED exchange on this exact case_id)
    # already establishes topical continuity, so the composed follow-up
    # message must bypass the relevance check entirely, not be scored on
    # its trailing segment alone.
    composed = (
        "[Previous question]: What is Gastric Cancer?\n"
        "[Previous answer]: some prior governed answer\n"
        "[Follow-up question]: Can you clarify?"
    )
    response = client.post("/chat/query", json={"message": composed, "case_id": "EC-0002"})

    assert response.status_code == 200
    assert response.json()["status"] == "COMPLETED"


def test_chat_query_b08_followup_still_updates_context_after_relevance_bypass():
    # Full round trip: an initial COMPLETED exchange, then a composed
    # follow-up that bypasses the relevance check -- existing B08/B11
    # follow-up-context behavior (gated on status === COMPLETED) is
    # unaffected by B12.
    initial = client.post(
        "/chat/query", json={"message": "What is Gastric Cancer?", "case_id": "EC-0002"}
    )
    assert initial.json()["status"] == "COMPLETED"

    composed = (
        "[Previous question]: What is Gastric Cancer?\n"
        f"[Previous answer]: {initial.json()['answer']}\n"
        "[Follow-up question]: Can you clarify?"
    )
    follow_up = client.post("/chat/query", json={"message": composed, "case_id": "EC-0002"})

    assert follow_up.status_code == 200
    assert follow_up.json()["status"] == "COMPLETED"


# --- R1-R3: bounded UI refinement (visual distinction, alignment, About accordion) --


def test_chat_page_user_message_has_a_distinct_light_blue_treatment():
    # R1: .chat-message.user gets a light-blue background + border, reusing
    # existing design tokens -- .chat-message.assistant stays neutral/white.
    html = client.get("/chat").text

    assert "background: var(--blue-50);" in html
    assert "border: 1px solid var(--blue-500);" in html


def test_chat_page_followup_and_form_align_with_chat_history_inner_padding():
    # R2: #followup-label/#followup-suggestions/#chat-form get the same
    # horizontal padding as #chat-history's own inner content inset, so
    # their content edges line up rather than only sharing the outer
    # max-width column.
    html = client.get("/chat").text

    assert "#followup-label, #followup-suggestions, #chat-form {" in html
    assert "padding-left: 1.15rem;" in html


def test_chat_page_about_accordion_has_all_nine_headings_present():
    # R3: all nine existing section headings remain present, unrenamed.
    html = client.get("/chat").text

    for heading in [
        "What is this",
        "Objective",
        "Scope",
        "How to use",
        "Evidence &amp; Sources",
        "Safety boundary",
        "Research &amp; Evaluation",
        "About the team",
        "Model / System Information",
    ]:
        assert heading in html


def test_chat_page_about_accordion_panels_start_collapsed():
    # R3: every one of the nine panels is hidden by default (collapsed),
    # and every trigger starts aria-expanded="false".
    html = client.get("/chat").text

    for n in range(1, 10):
        assert f'id="about-panel-{n}" class="about-accordion-panel" role="region" aria-labelledby="about-trigger-{n}" hidden>' in html
        assert f'aria-controls="about-panel-{n}" id="about-trigger-{n}"' in html
        assert html.count(f'aria-expanded="false" aria-controls="about-panel-{n}"') == 1


def test_chat_page_about_accordion_expand_collapse_is_wired():
    # R3: a click handler toggles aria-expanded and the matching panel's
    # hidden state -- represents the expand/collapse behavior itself.
    html = client.get("/chat").text

    assert 'document.querySelectorAll(".about-accordion-trigger")' in html
    assert 'trigger.setAttribute("aria-expanded", expanded ? "false" : "true");' in html
    assert "panel.hidden = expanded;" in html


def test_chat_page_about_accordion_preserves_existing_content_verbatim():
    # R3: representative existing facts from each kind of internal
    # structure (plain paragraphs, the scope two-card grid, the ordered
    # how-to-use list, the team list, and the Model/System <dl>) are still
    # present, unrewritten -- proves content was wrapped, not replaced.
    html = client.get("/chat").text

    assert "Please do not enter identifiable patient information or other sensitive personal data." in html
    assert "Evidence-grounded oncology education" in html
    assert "Emergency medical advice" in html
    assert "Choose your situation" in html
    assert "Nhan Tran, MD, MSc." in html
    assert "Quy Nguyen Hoang, MD, PhD." in html
    assert "<dt>Clinical status</dt>" in html
    assert (
        "Not clinically validated. Not for diagnosis. Not for treatment selection. "
        "Not for patient-specific clinical decision-making. Not clinically deployed."
    ) in html


# --- B11 bounded verification surface --------------------------------------


def test_chat_query_not_relevant_answer_never_contains_the_raw_status_token():
    # The displayed answer bubble text (data.answer, rendered verbatim by
    # appendMessage) must always be governed, human-readable copy -- the
    # raw internal status token ("NOT_RELEVANT") must never leak into it,
    # even though that same token is the correct, separate `status` field
    # value used only for the boundary-notice lookup.
    response = client.post(
        "/chat/query",
        json={"message": "Please explain Genomic Biomarkers.", "case_id": "EC-0002"},
    )

    assert response.status_code == 200
    body = response.json()
    assert body["status"] == "NOT_RELEVANT"
    assert "NOT_RELEVANT" not in body["answer"]
