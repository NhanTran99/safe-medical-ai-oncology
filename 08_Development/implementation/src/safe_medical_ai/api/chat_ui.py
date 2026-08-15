"""Controlled Chat UI shell — Phase 6 Stage 2 Track 1A/1B/1C.

Browser-facing presentation boundary only: a static page (inline HTML/CSS/
vanilla JS, no new frontend framework/dependency) that lets a user type and
submit a question, and issues a request toward the backend chat boundary.

This module contains no clinical reasoning, no PP-selection/navigation
logic, no retrieval, no CER invocation, and no safety/validation logic —
those remain governed backend concerns. As of Track 1B, `main.py`'s
`POST /chat/query` submits the question through the existing governed CER
execution path (PP-0002 + CKO); this presentation module is unchanged by
that integration and still only renders whatever `answer`/`status` it
receives back.

Track 1C adds a client-only "Situation -> Topic -> Question starter"
navigation aid (visual/UX presentation pattern selectively adapted from a
legacy reference UI, per governance instructions — no calculation/model/
clinical logic or React/Tailwind architecture was imported, only visual
design language reimplemented in plain CSS). Selecting a question starter
only populates `#question-input`; it never submits the form or calls
`/chat/query` on its own. The existing `#chat-form`/`#question-input`/
`#send-button`/`#chat-history`/`#chat-status` elements and their submit
JS are unchanged from Track 1B, so the existing Track 1A/1B tests remain
valid against this page unmodified.
"""

from __future__ import annotations

CHAT_PAGE_HTML = """<!doctype html>
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

      <div class="panel-card">
        <p class="panel-label">Your Situation</p>
        <div id="situation-list" class="situation-list"></div>
      </div>

      <div id="topic-panel" class="panel-card" hidden>
        <p class="panel-label">Topic</p>
        <div id="topic-list" class="topic-list"></div>
      </div>

      <div id="starter-panel" class="panel-card" hidden>
        <p class="panel-label">Question Starters</p>
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
      // --- Track 1C: client-only Situation -> Topic -> Question starter
      // navigation content. Presentation/orientation data only: no
      // clinical logic, no PP/navigation identifiers, no backend calls.
      var SITUATIONS = [
        {
          id: "diagnosed",
          label: "I was recently diagnosed",
          topics: [
            {
              id: "understanding-diagnosis",
              label: "Understanding my diagnosis",
              starters: [
                "What does my diagnosis mean?",
                "What are the different stages of gastric cancer?",
                "What questions should I ask my doctor?"
              ]
            },
            {
              id: "next-steps",
              label: "Next steps",
              starters: [
                "What typically happens after a diagnosis?",
                "What kinds of tests might come next?"
              ]
            }
          ]
        },
        {
          id: "treatment",
          label: "I'm receiving treatment",
          topics: [
            {
              id: "side-effects",
              label: "Side effects",
              starters: [
                "What side effects can this treatment cause?",
                "What symptoms should I discuss with my care team?"
              ]
            },
            {
              id: "treatment-overview",
              label: "Treatment overview",
              starters: [
                "What are common treatment approaches for gastric cancer?",
                "How is treatment progress typically monitored?"
              ]
            }
          ]
        },
        {
          id: "surgery",
          label: "I'm preparing for surgery",
          topics: [
            {
              id: "before-surgery",
              label: "Before surgery",
              starters: [
                "What kind of preparation is typically involved before surgery?",
                "What questions should I ask before surgery?"
              ]
            },
            {
              id: "recovery",
              label: "Recovery",
              starters: [
                "What does the recovery process typically look like?"
              ]
            }
          ]
        },
        {
          id: "recurrence",
          label: "I'm concerned about recurrence",
          topics: [
            {
              id: "understanding-recurrence",
              label: "Understanding recurrence",
              starters: [
                "What does cancer recurrence mean?",
                "What factors are associated with recurrence risk?"
              ]
            },
            {
              id: "monitoring",
              label: "Monitoring",
              starters: [
                "What kind of follow-up monitoring is typically used?"
              ]
            }
          ]
        },
        {
          id: "follow-up",
          label: "I'm in follow-up",
          topics: [
            {
              id: "follow-up-care",
              label: "Follow-up care",
              starters: [
                "What does typical follow-up care involve?",
                "How often are follow-up visits usually scheduled?"
              ]
            },
            {
              id: "what-to-watch-for",
              label: "What to watch for",
              starters: [
                "What symptoms should prompt me to contact my care team?"
              ]
            }
          ]
        },
        {
          id: "understand",
          label: "I want to understand my cancer",
          topics: [
            {
              id: "basics",
              label: "Gastric cancer basics",
              starters: [
                "What is gastric cancer?",
                "How does gastric cancer typically develop?"
              ]
            },
            {
              id: "risk-factors",
              label: "Risk factors",
              starters: [
                "What are known risk factors for gastric cancer?"
              ]
            }
          ]
        }
      ];

      var situationList = document.getElementById("situation-list");
      var topicPanel = document.getElementById("topic-panel");
      var topicList = document.getElementById("topic-list");
      var starterPanel = document.getElementById("starter-panel");
      var starterList = document.getElementById("starter-list");
      var input = document.getElementById("question-input");

      function clearChildren(el) {
        while (el.firstChild) {
          el.removeChild(el.firstChild);
        }
      }

      function renderSituations() {
        SITUATIONS.forEach(function (situation) {
          var btn = document.createElement("button");
          btn.type = "button";
          btn.className = "situation-card";
          btn.textContent = situation.label;
          btn.setAttribute("aria-pressed", "false");
          btn.addEventListener("click", function () {
            selectSituation(situation);
          });
          situationList.appendChild(btn);
        });
      }

      function selectSituation(situation) {
        Array.prototype.forEach.call(
          situationList.querySelectorAll(".situation-card"),
          function (el) {
            el.setAttribute("aria-pressed", el.textContent === situation.label ? "true" : "false");
          }
        );

        clearChildren(topicList);
        starterPanel.hidden = true;
        clearChildren(starterList);

        situation.topics.forEach(function (topic) {
          var btn = document.createElement("button");
          btn.type = "button";
          btn.className = "topic-chip";
          btn.textContent = topic.label;
          btn.setAttribute("aria-pressed", "false");
          btn.addEventListener("click", function () {
            selectTopic(topic, btn);
          });
          topicList.appendChild(btn);
        });

        topicPanel.hidden = false;
      }

      function selectTopic(topic, activeButton) {
        Array.prototype.forEach.call(
          topicList.querySelectorAll(".topic-chip"),
          function (el) {
            el.setAttribute("aria-pressed", el === activeButton ? "true" : "false");
          }
        );

        clearChildren(starterList);

        topic.starters.forEach(function (starterText) {
          var btn = document.createElement("button");
          btn.type = "button";
          btn.className = "starter-chip";
          btn.textContent = starterText;
          // Populate the existing input only. Never submits the form and
          // never calls /chat/query on its own -- the user must still
          // press Send.
          btn.addEventListener("click", function () {
            input.value = starterText;
            input.focus();
          });
          starterList.appendChild(btn);
        });

        starterPanel.hidden = false;
      }

      renderSituations();
    })();

    (function () {
      // --- Track 1B chat submission wiring (unchanged) -------------------
      var form = document.getElementById("chat-form");
      var input = document.getElementById("question-input");
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

        appendMessage("user", question);
        input.value = "";
        setLoading(true);

        fetch("/chat/query", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ message: question }),
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
