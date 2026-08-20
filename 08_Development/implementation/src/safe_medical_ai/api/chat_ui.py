"""Controlled Chat UI shell — Phase 6 Stage 2 Track 1A/1B/1C/2.

Browser-facing presentation boundary only: a static page (inline HTML/CSS/
vanilla JS, no new frontend framework/dependency) that lets a user type and
submit a question, and issues a request toward the backend chat boundary.

This module contains no clinical reasoning, no PP-selection/navigation
logic, no retrieval, no CER invocation, and no safety/validation logic —
those remain governed backend concerns.

Track 2 change: the page is no longer a single static string. `/chat`
(see `api/main.py`) renders it via `render_chat_page(catalog)`, embedding
a controlled navigation catalog derived from the same manifest projection
`EvaluationCaseResolver` uses (`case_id`, `pp_title`, `controlled_question`
only — never used for resolution/execution here, only for non-clinical
display labels and pre-approved question-starter text). The catalog is
read fresh by `main.py` on every `/chat` request; this module never reads
the projection file itself and never hardcodes any specific case.

`selectedCaseId` starts `null` — no implicit default case (Track 2 RC-5):
it becomes non-null only once the user explicitly selects a Topic, which
sets it from real, approved manifest data, never a fixed literal. Editing
the question text never changes it. Sending without a selected Topic is
blocked client-side (and would also fail closed server-side via the
required `case_id` field). Selecting a question starter only populates
`#question-input`; it never submits the form or calls `/chat/query` on
its own.

Situation cards (Tier 1) are unchanged, generic orientation labels — the
frozen manifest has no situation/category taxonomy, so a situation click
reveals the same full, searchable Topic list (Tier 2) rather than a
per-situation filtered subset; inventing such a filter would itself be a
content-curation/categorization decision outside this task's scope (see
`README.md` "Known simplification").
"""

from __future__ import annotations

import json


def render_chat_page(catalog: list[dict[str, str]]) -> str:
    """Render the Chat UI page, embedding `catalog` as the controlled
    navigation data (Situation -> Topic -> Question Starter, Track 2)."""
    # `</` inside title/question text (e.g. from manifest content) must not
    # be able to terminate the embedding <script> tag early.
    catalog_json = json.dumps(catalog).replace("</", "<\\/")

    return _PAGE_TEMPLATE.replace("__CATALOG_JSON__", catalog_json)


_PAGE_TEMPLATE = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Safe Medical AI Oncology — Controlled Research Interface</title>
<style>
  :root {
    --navy: #0A2540;
    --slate-50: #f8fafc;
    --slate-100: #f1f5f9;
    --slate-200: #e2e8f0;
    --slate-400: #94a3b8;
    --slate-600: #475569;
    --slate-700: #334155;
    --blue-50: #eff6ff;
    --blue-500: #3b82f6;
    --blue-600: #2563eb;
    --blue-700: #1d4ed8;
    --amber-50: #fffbeb;
    --amber-200: #fde68a;
    --amber-600: #d97706;
    --amber-800: #92400e;
    --red-600: #dc2626;
  }

  * { box-sizing: border-box; }

  body {
    font-family: system-ui, -apple-system, "Segoe UI", sans-serif;
    margin: 0;
    color: var(--slate-700);
    background: var(--slate-50);
    min-height: 100vh;
  }

  /* --- header ------------------------------------------------------- */

  header.app-header {
    background: var(--navy);
    padding: 0.9rem 1.5rem;
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 1rem;
    flex-wrap: wrap;
  }
  .app-identity { display: flex; align-items: center; gap: 0.75rem; }
  .app-identity-icon {
    width: 1.75rem;
    height: 1.75rem;
    border-radius: 0.375rem;
    background: rgba(255, 255, 255, 0.1);
    border: 1px solid rgba(255, 255, 255, 0.15);
    display: flex;
    align-items: center;
    justify-content: center;
    flex-shrink: 0;
  }
  .app-identity-icon svg { width: 0.9rem; height: 0.9rem; }
  .app-title { color: #fff; font-size: 0.85rem; font-weight: 600; letter-spacing: 0.02em; margin: 0; line-height: 1.2; }
  .app-subtitle { color: rgba(255, 255, 255, 0.55); font-size: 0.7rem; margin: 0.2rem 0 0; line-height: 1.2; }
  .status-badge {
    font-size: 0.6rem;
    font-weight: 600;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    color: rgba(255, 255, 255, 0.7);
    background: rgba(255, 255, 255, 0.1);
    border: 1px solid rgba(255, 255, 255, 0.15);
    border-radius: 999px;
    padding: 0.3rem 0.75rem;
    white-space: nowrap;
  }

  /* --- overall layout: fixed-width sidebar + main chat --------------- */

  .app-body {
    display: flex;
    flex-direction: column;
    align-items: stretch;
    min-height: calc(100vh - 3.2rem);
  }
  @media (min-width: 900px) {
    .app-body { flex-direction: row; }
  }

  aside.nav-panel {
    background: #fff;
    border-right: 1px solid var(--slate-200);
    width: 100%;
    padding: 1.25rem;
    display: flex;
    flex-direction: column;
    gap: 1rem;
  }
  @media (min-width: 900px) {
    aside.nav-panel { width: 320px; flex-shrink: 0; overflow-y: auto; }
  }

  .nav-panel h2.nav-prompt {
    font-size: 0.95rem;
    font-weight: 600;
    color: var(--slate-700);
    margin: 0 0 0.25rem;
  }

  .panel-card {
    border: 1px solid var(--slate-200);
    background: #fff;
    border-radius: 1rem;
    padding: 1rem 1.1rem;
  }
  .panel-label {
    font-size: 0.62rem;
    font-weight: 600;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    color: var(--slate-400);
    margin: 0 0 0.6rem;
  }

  .situation-list, .topic-list, .starter-list {
    display: flex;
    flex-direction: column;
    gap: 0.4rem;
  }
  .topic-list { max-height: 220px; overflow-y: auto; }

  button.situation-card, button.topic-chip {
    text-align: left;
    background: var(--slate-50);
    border: 1px solid var(--slate-200);
    border-radius: 0.65rem;
    padding: 0.55rem 0.75rem;
    font-size: 0.82rem;
    color: var(--slate-700);
    cursor: pointer;
    transition: border-color 0.12s, background 0.12s;
  }
  button.situation-card:hover, button.topic-chip:hover {
    background: var(--blue-50);
    border-color: var(--blue-500);
  }
  button.situation-card[aria-pressed="true"], button.topic-chip[aria-pressed="true"] {
    background: var(--blue-50);
    border-color: var(--blue-600);
    color: var(--blue-700);
    font-weight: 600;
  }

  button.starter-chip {
    text-align: left;
    background: #fff;
    border: 1px dashed var(--slate-200);
    border-radius: 0.65rem;
    padding: 0.55rem 0.75rem;
    font-size: 0.8rem;
    color: var(--slate-600);
    cursor: pointer;
  }
  button.starter-chip:hover { border-color: var(--blue-500); color: var(--blue-700); }

  .random-topic-button {
    text-align: center;
    background: #fff;
    border: 1px solid var(--slate-200);
    border-radius: 0.65rem;
    padding: 0.5rem 0.75rem;
    font-size: 0.78rem;
    font-weight: 600;
    color: var(--blue-600);
    cursor: pointer;
  }
  .random-topic-button:hover { background: var(--blue-50); border-color: var(--blue-500); }

  #topic-search {
    width: 100%;
    padding: 0.45rem 0.6rem;
    font-size: 0.8rem;
    border: 1px solid var(--slate-200);
    border-radius: 0.5rem;
    margin-bottom: 0.5rem;
  }
  #topic-search:focus { outline: 2px solid var(--blue-500); outline-offset: 1px; }

  .selected-topic-note {
    font-size: 0.72rem;
    color: var(--slate-400);
    margin: 0 0 0.6rem;
  }
  .selected-topic-note strong { color: var(--slate-600); }

  [hidden] { display: none !important; }

  .disclaimer {
    display: flex;
    gap: 0.6rem;
    background: var(--amber-50);
    border: 1px solid var(--amber-200);
    border-radius: 0.65rem;
    padding: 0.7rem 0.85rem;
    margin-top: auto;
  }
  .disclaimer-icon { color: var(--amber-600); flex-shrink: 0; font-size: 0.9rem; line-height: 1; }
  .disclaimer p {
    font-size: 0.72rem;
    line-height: 1.45;
    color: var(--amber-800);
    margin: 0;
  }
  .disclaimer strong { font-weight: 600; }

  /* --- main chat area -------------------------------------------------- */

  main.chat-main {
    flex: 1;
    display: flex;
    flex-direction: column;
    padding: 1.25rem 1.5rem 1.5rem;
    min-width: 0;
  }

  #chat-history {
    border: 1px solid var(--slate-200);
    border-radius: 1rem;
    background: #fff;
    min-height: 320px;
    max-height: 55vh;
    overflow-y: auto;
    padding: 1rem 1.15rem;
    margin-bottom: 0.85rem;
  }
  #chat-history:empty::before {
    content: "Ask a question below, or start from a situation on the left.";
    color: var(--slate-400);
    font-size: 0.85rem;
  }
  .chat-message { margin: 0 0 0.9rem; white-space: pre-wrap; line-height: 1.5; font-size: 0.88rem; }
  .chat-message:last-child { margin-bottom: 0; }
  .chat-message.user { font-weight: 600; color: var(--slate-700); }
  .chat-message.assistant { color: var(--slate-600); }
  .chat-message.error { color: var(--red-600); }

  #chat-form { display: flex; gap: 0.6rem; }
  #question-input {
    flex: 1;
    padding: 0.65rem 0.85rem;
    font-size: 0.9rem;
    font-family: inherit;
    border: 1px solid var(--slate-200);
    border-radius: 0.65rem;
    resize: vertical;
    min-height: 2.75rem;
  }
  #question-input:focus { outline: 2px solid var(--blue-500); outline-offset: 1px; }
  #send-button {
    padding: 0.65rem 1.4rem;
    font-size: 0.9rem;
    font-weight: 600;
    color: #fff;
    background: var(--blue-600);
    border: none;
    border-radius: 0.65rem;
    cursor: pointer;
  }
  #send-button:hover { background: var(--blue-700); }
  #send-button:disabled { cursor: not-allowed; opacity: 0.6; }
  #chat-status { margin-top: 0.5rem; font-size: 0.8rem; color: var(--slate-400); min-height: 1.2em; }
  #chat-status.error { color: var(--red-600); }
</style>
</head>
<body>
  <header class="app-header">
    <div class="app-identity">
      <div class="app-identity-icon">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="color: rgba(255,255,255,0.8);">
          <path d="M9 2v6l-5.5 9.5A2 2 0 0 0 5.2 21h13.6a2 2 0 0 0 1.7-3.5L15 8V2"></path>
          <path d="M9 2h6"></path>
        </svg>
      </div>
      <div>
        <p class="app-title">Safe Medical AI Oncology</p>
        <p class="app-subtitle">Controlled Research Interface</p>
      </div>
    </div>
    <span class="status-badge">Research / Controlled Evaluation</span>
  </header>

  <div class="app-body">
    <aside class="nav-panel">
      <h2 class="nav-prompt">Not sure what to ask? Start with your situation.</h2>

      <button type="button" id="random-topic-button" class="random-topic-button">Random Topic</button>

      <div class="panel-card">
        <p class="panel-label">Your Situation</p>
        <div id="situation-list" class="situation-list"></div>
      </div>

      <div id="topic-panel" class="panel-card" hidden>
        <p class="panel-label">Approved Topic</p>
        <input type="search" id="topic-search" placeholder="Search approved topics..." aria-label="Search approved topics">
        <div id="topic-list" class="topic-list"></div>
      </div>

      <div id="starter-panel" class="panel-card" hidden>
        <p class="panel-label">Question Starter</p>
        <p id="selected-topic-note" class="selected-topic-note"></p>
        <div id="starter-list" class="starter-list"></div>
      </div>

      <div class="disclaimer">
        <span class="disclaimer-icon">&#9888;</span>
        <p><strong>Not clinically validated. Not for clinical decision-making.</strong> This interface is for controlled research and educational use only and does not provide diagnosis, treatment recommendations, or patient-specific clinical guidance.</p>
      </div>
    </aside>

    <main class="chat-main">
      <div id="chat-history" aria-live="polite"></div>

      <form id="chat-form">
        <textarea
          id="question-input"
          name="question"
          placeholder="Enter a question, or pick a question starter on the left..."
          required
          aria-label="Question"
        ></textarea>
        <button id="send-button" type="submit">Send</button>
      </form>
      <div id="chat-status" role="status"></div>
    </main>
  </div>

  <script>
    (function () {
      // --- Track 2: controlled navigation catalog, embedded server-side
      // from the SAME manifest projection EvaluationCaseResolver uses
      // (case_id/pp_title/controlled_question only). No PP/EC identifiers
      // are ever displayed to the user -- only pp_title and
      // controlled_question. Never hard-coded, never a second manifest.
      var CATALOG = __CATALOG_JSON__;

      // Deliberately generic orientation labels only -- the frozen manifest
      // has no situation/category taxonomy, so every situation reveals the
      // same full, searchable Topic list rather than an invented subset.
      var SITUATIONS = [
        "I was recently diagnosed",
        "I'm receiving treatment",
        "I'm preparing for surgery",
        "I'm concerned about recurrence",
        "I'm in follow-up",
        "I want to understand my cancer"
      ];

      var situationList = document.getElementById("situation-list");
      var topicPanel = document.getElementById("topic-panel");
      var topicSearch = document.getElementById("topic-search");
      var topicList = document.getElementById("topic-list");
      var starterPanel = document.getElementById("starter-panel");
      var starterList = document.getElementById("starter-list");
      var selectedTopicNote = document.getElementById("selected-topic-note");
      var input = document.getElementById("question-input");

      // The approved Evaluation Case identity currently associated with the
      // question box. No implicit default: null until the user explicitly
      // selects a Topic from the manifest-backed catalog (selectTopic()
      // below is the only place that ever sets it). Editing the question
      // text never changes it.
      var selectedCaseId = null;

      function clearChildren(el) {
        while (el.firstChild) {
          el.removeChild(el.firstChild);
        }
      }

      function renderSituations() {
        SITUATIONS.forEach(function (label) {
          var btn = document.createElement("button");
          btn.type = "button";
          btn.className = "situation-card";
          btn.textContent = label;
          btn.setAttribute("aria-pressed", "false");
          btn.addEventListener("click", function () {
            Array.prototype.forEach.call(
              situationList.querySelectorAll(".situation-card"),
              function (el) { el.setAttribute("aria-pressed", el === btn ? "true" : "false"); }
            );
            topicPanel.hidden = false;
            topicSearch.focus();
            renderTopics("");
          });
          situationList.appendChild(btn);
        });
      }

      function renderTopics(filterText) {
        clearChildren(topicList);
        var needle = filterText.trim().toLowerCase();
        CATALOG.filter(function (item) {
          return !needle || item.pp_title.toLowerCase().indexOf(needle) !== -1;
        }).forEach(function (item) {
          var btn = document.createElement("button");
          btn.type = "button";
          btn.className = "topic-chip";
          btn.textContent = item.pp_title;
          btn.setAttribute("aria-pressed", item.case_id === selectedCaseId ? "true" : "false");
          btn.addEventListener("click", function () {
            selectTopic(item, btn);
          });
          topicList.appendChild(btn);
        });
      }

      function selectTopic(item, activeButton) {
        selectedCaseId = item.case_id;

        Array.prototype.forEach.call(
          topicList.querySelectorAll(".topic-chip"),
          function (el) { el.setAttribute("aria-pressed", el === activeButton ? "true" : "false"); }
        );

        selectedTopicNote.textContent = "Selected topic: " + item.pp_title;

        clearChildren(starterList);
        var starterBtn = document.createElement("button");
        starterBtn.type = "button";
        starterBtn.className = "starter-chip";
        starterBtn.textContent = item.controlled_question;
        // Populate the existing input only. Never submits the form and
        // never calls /chat/query on its own -- the user must still press
        // Send. Selecting a starter never changes selectedCaseId (it was
        // already set by selectTopic above).
        starterBtn.addEventListener("click", function () {
          input.value = item.controlled_question;
          input.focus();
        });
        starterList.appendChild(starterBtn);

        starterPanel.hidden = false;
      }

      topicSearch.addEventListener("input", function () {
        renderTopics(topicSearch.value);
      });

      // Random Topic: a navigation convenience only. Picks one entry from
      // the SAME CATALOG the Topic list already renders from (no second
      // source of truth), then routes it through the exact same
      // selectTopic() function manual Topic clicks use -- selectedCaseId
      // is set the same way either way.
      var randomTopicButton = document.getElementById("random-topic-button");
      randomTopicButton.addEventListener("click", function () {
        if (!CATALOG.length) {
          return;
        }
        var item = CATALOG[Math.floor(Math.random() * CATALOG.length)];

        topicPanel.hidden = false;
        topicSearch.value = "";
        renderTopics("");

        var activeButton = null;
        Array.prototype.forEach.call(
          topicList.querySelectorAll(".topic-chip"),
          function (el) {
            if (el.textContent === item.pp_title) {
              activeButton = el;
            }
          }
        );

        selectTopic(item, activeButton);
      });

      renderSituations();

      // --- chat submission wiring (shares selectedCaseId above) ---------
      var form = document.getElementById("chat-form");
      var button = document.getElementById("send-button");
      var history = document.getElementById("chat-history");
      var status = document.getElementById("chat-status");

      function appendMessage(role, text) {
        var el = document.createElement("div");
        el.className = "chat-message " + role;
        el.textContent = text;
        history.appendChild(el);
        history.scrollTop = history.scrollHeight;
      }

      function setLoading(isLoading) {
        input.disabled = isLoading;
        button.disabled = isLoading;
        status.classList.remove("error");
        status.textContent = isLoading ? "Sending..." : "";
      }

      function setError(message) {
        status.classList.add("error");
        status.textContent = message;
      }

      form.addEventListener("submit", function (event) {
        event.preventDefault();
        var question = input.value.trim();
        if (!question) {
          return;
        }
        if (!selectedCaseId) {
          setError("Please select an approved topic before sending.");
          return;
        }

        appendMessage("user", question);
        input.value = "";
        setLoading(true);

        fetch("/chat/query", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ message: question, case_id: selectedCaseId }),
        })
          .then(function (response) {
            if (!response.ok) {
              throw new Error("Request failed with status " + response.status);
            }
            return response.json();
          })
          .then(function (data) {
            setLoading(false);
            appendMessage("assistant", data.answer);
          })
          .catch(function (err) {
            setLoading(false);
            appendMessage("error", "Error: could not get a response.");
            setError(err.message || "Request failed.");
          });
      });
    })();
  </script>
</body>
</html>
"""
