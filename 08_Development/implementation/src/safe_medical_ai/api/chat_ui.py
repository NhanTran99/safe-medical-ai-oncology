"""Controlled Chat UI shell — Phase 6 Stage 2 Track 1A/1B/1C/2/3 (B05/B06).

Browser-facing presentation boundary only: a static page (inline HTML/CSS/
vanilla JS, no new frontend framework/dependency) that lets a user type and
submit a question, and issues a request toward the backend chat boundary.

This module contains no clinical reasoning, no CER invocation, no
retrieval, and no safety/validation logic — those remain governed backend
concerns. It does contain non-clinical navigation/filtering logic (Situation
-> Topic), which is presentation/navigation only: it never resolves a
`case_id`, never invokes the CER path itself, and never carries clinical
content.

Track 2 change: the page is no longer a single static string. `/chat`
(see `api/main.py`) renders it via `render_chat_page(catalog,
situation_mapping)`, embedding a controlled navigation catalog derived
from the same manifest projection `EvaluationCaseResolver` uses
(`case_id`, `pp_title`, `controlled_question` only — never used for
resolution/execution here, only for non-clinical display labels and
pre-approved question-starter text). The catalog is read fresh by
`main.py` on every `/chat` request; this module never reads the
projection file itself and never hardcodes any specific case.

`selectedCaseId` starts `null` — no implicit default case (Track 2 RC-5):
it becomes non-null only once the user explicitly selects a Topic, which
sets it from real, approved manifest data, never a fixed literal. Editing
the question text never changes it. Sending without a selected Topic is
blocked client-side (and would also fail closed server-side via the
required `case_id` field). Selecting a question starter only populates
`#question-input`; it never submits the form or calls `/chat/query` on
its own.

B06 change: Situation cards (Tier 1) are now rendered from
`situation_mapping["situations"]` (the five approved B06 Situations, see
`data/B06_SITUATION_NAVIGATION_MAPPING_README.md`), and a Situation click
filters the Topic list (Tier 2) to only that Situation's mapped
`case_id`s via `situation_mapping["mappings"]`, instead of the prior
Track 1C simplification where every situation click revealed the full,
unfiltered 239-entry catalog. Random Topic (B05, `#random-topic-button`)
is unaffected: it still draws from the full, unfiltered `CATALOG` and
still calls the same `selectTopic()` every Topic chip and every Situation
match already use.
"""

from __future__ import annotations

import json


def render_chat_page(catalog: list[dict[str, str]], situation_mapping: dict) -> str:
    """Render the Chat UI page, embedding `catalog` as the controlled
    navigation data (Situation -> Topic -> Question Starter) and
    `situation_mapping` (B06) as the governed Situation -> Topic filter.

    `situation_mapping` carries the five approved Situations and their
    `(situation_id, case_id)` relationships (see
    `data/B06_SITUATION_NAVIGATION_MAPPING_README.md`) -- it never carries
    clinical content and never redefines `case_id`/PP identity, only
    references it.
    """
    # `</` inside title/question text (e.g. from manifest content) must not
    # be able to terminate the embedding <script> tag early.
    catalog_json = json.dumps(catalog).replace("</", "<\\/")
    situation_mapping_json = json.dumps(situation_mapping).replace("</", "<\\/")

    return (
        _PAGE_TEMPLATE.replace("__CATALOG_JSON__", catalog_json).replace(
            "__SITUATION_MAPPING_JSON__", situation_mapping_json
        )
    )


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
  .about-toggle {
    background: rgba(255, 255, 255, 0.1);
    border: 1px solid rgba(255, 255, 255, 0.15);
    color: rgba(255, 255, 255, 0.85);
    font-size: 0.72rem;
    font-weight: 600;
    letter-spacing: 0.02em;
    border-radius: 0.5rem;
    padding: 0.35rem 0.7rem;
    cursor: pointer;
  }
  .about-toggle:hover { background: rgba(255, 255, 255, 0.18); }
  .about-toggle:focus { outline: 2px solid #fff; outline-offset: 2px; }

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
  .panel-label { margin: 0 0 0.6rem; }
  .panel-label .step-number {
    display: block;
    font-size: 0.62rem;
    font-weight: 600;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    color: var(--slate-400);
  }
  .panel-label .step-title {
    display: block;
    font-size: 0.78rem;
    font-weight: 600;
    color: var(--slate-600);
    margin-top: 0.1rem;
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

  /* --- About drawer ---------------------------------------------------- */

  .about-backdrop {
    position: fixed;
    inset: 0;
    background: rgba(10, 37, 64, 0.35);
    z-index: 40;
  }
  .about-drawer {
    position: fixed;
    top: 0;
    right: 0;
    height: 100vh;
    width: min(440px, 92vw);
    background: #fff;
    border-left: 1px solid var(--slate-200);
    box-shadow: -4px 0 24px rgba(15, 23, 42, 0.12);
    z-index: 41;
    display: flex;
    flex-direction: column;
  }
  .about-drawer-header {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 1rem 1.25rem;
    border-bottom: 1px solid var(--slate-200);
    flex-shrink: 0;
  }
  .about-drawer-header h2 { font-size: 1rem; font-weight: 600; color: var(--slate-700); margin: 0; }
  .about-close {
    background: none;
    border: none;
    font-size: 1.3rem;
    line-height: 1;
    color: var(--slate-400);
    cursor: pointer;
    padding: 0.25rem;
  }
  .about-close:hover { color: var(--slate-700); }
  .about-close:focus { outline: 2px solid var(--blue-500); outline-offset: 2px; }

  .about-drawer-body { padding: 1.25rem; overflow-y: auto; flex: 1; }
  .about-section { margin: 0 0 1.5rem; }
  .about-section:last-child { margin-bottom: 0; }
  .about-section h3 { margin: 0; }
  .about-accordion-trigger {
    display: flex;
    align-items: center;
    justify-content: space-between;
    width: 100%;
    background: none;
    border: none;
    padding: 0;
    font: inherit;
    font-size: 0.68rem;
    font-weight: 700;
    letter-spacing: 0.1em;
    text-transform: uppercase;
    color: var(--slate-400);
    text-align: left;
    cursor: pointer;
  }
  .about-accordion-trigger:hover { color: var(--slate-600); }
  .about-accordion-trigger:focus { outline: 2px solid var(--blue-500); outline-offset: 2px; }
  .about-accordion-icon {
    flex-shrink: 0;
    margin-left: 0.75rem;
    font-size: 0.7rem;
    transition: transform 0.12s;
  }
  .about-accordion-trigger[aria-expanded="true"] .about-accordion-icon { transform: rotate(180deg); }
  .about-accordion-panel { margin-top: 0.5rem; }
  .about-section p { font-size: 0.85rem; line-height: 1.55; color: var(--slate-600); margin: 0 0 0.5rem; }
  .about-section p:last-child { margin-bottom: 0; }
  .about-section ul, .about-section ol {
    margin: 0 0 0.5rem;
    padding-left: 1.15rem;
    font-size: 0.85rem;
    line-height: 1.55;
    color: var(--slate-600);
  }
  .about-section li { margin: 0 0 0.3rem; }
  .about-note { font-size: 0.78rem; font-style: italic; color: var(--slate-400); }

  .about-scope-grid { display: grid; grid-template-columns: 1fr; gap: 0.75rem; }
  @media (min-width: 480px) {
    .about-scope-grid { grid-template-columns: 1fr 1fr; }
  }
  .about-scope-card {
    border: 1px solid var(--slate-200);
    border-radius: 0.75rem;
    padding: 0.75rem 0.85rem;
    background: var(--slate-50);
  }
  .about-scope-heading {
    font-size: 0.68rem;
    font-weight: 700;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    color: var(--slate-600);
    margin: 0 0 0.5rem;
  }
  .about-scope-card ul { margin: 0; padding-left: 1.1rem; }
  .about-scope-card li { font-size: 0.8rem; margin: 0 0 0.25rem; }
  .about-scope-card li:last-child { margin-bottom: 0; }

  .about-safety-label {
    display: inline-block;
    font-size: 0.68rem;
    font-weight: 700;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    color: var(--slate-600);
    background: var(--slate-100);
    border-radius: 0.4rem;
    padding: 0.2rem 0.5rem;
    margin: 0 0 0.5rem;
  }
  .about-team-label {
    font-size: 0.72rem;
    font-weight: 600;
    color: var(--slate-700);
    margin: 0 0 0.35rem;
  }
  .about-system-info { margin: 0; font-size: 0.85rem; color: var(--slate-600); }
  .about-system-info dt { font-weight: 600; color: var(--slate-700); margin: 0.5rem 0 0.15rem; }
  .about-system-info dt:first-child { margin-top: 0; }
  .about-system-info dd { margin: 0; line-height: 1.5; }

  /* --- main chat area -------------------------------------------------- */

  main.chat-main {
    flex: 1;
    display: flex;
    flex-direction: column;
    padding: 1.25rem 1.5rem 1.5rem;
    min-width: 0;
  }

  #chat-history, #chat-form, #followup-label, #followup-suggestions, #chat-status {
    max-width: 900px;
    width: 100%;
    margin-left: auto;
    margin-right: auto;
  }
  /* R2: align Continue-exploring/suggestions/the chat form's content edge
     with #chat-history's own inner content edge (padding: 1rem 1.15rem
     below) -- the shared max-width/centering above only aligns the outer
     column, not the inset text inside the bordered #chat-history card. */
  #followup-label, #followup-suggestions, #chat-form {
    padding-left: 1.15rem;
    padding-right: 1.15rem;
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
  .chat-message.user {
    font-weight: 600;
    color: var(--slate-700);
    background: var(--blue-50);
    border: 1px solid var(--blue-500);
    border-radius: 0.65rem;
    padding: 0.55rem 0.8rem;
  }
  .chat-message.assistant { color: var(--slate-600); font-size: 1rem; line-height: 1.6; }
  .chat-message.error { color: var(--red-600); }
  .chat-answer-paragraph { margin: 0 0 0.75rem; }
  .chat-answer-paragraph:last-child { margin-bottom: 0; }
  .chat-answer-list { margin: 0 0 0.75rem; padding-left: 1.25rem; }
  .chat-answer-list:last-child { margin-bottom: 0; }
  .chat-answer-list li { margin: 0 0 0.35rem; }
  .chat-answer-list li:last-child { margin-bottom: 0; }
  .chat-sources { margin: -0.3rem 0 0.9rem; }
  .chat-sources:last-child { margin-bottom: 0; }
  .chat-sources-label {
    font-size: 0.62rem;
    font-weight: 600;
    letter-spacing: 0.1em;
    text-transform: uppercase;
    color: var(--slate-400);
    margin: 0 0 0.35rem;
  }
  .chat-sources-chips { display: flex; flex-wrap: wrap; gap: 0.4rem; }
  .source-chip {
    display: inline-block;
    font-size: 0.72rem;
    font-weight: 600;
    color: var(--slate-600);
    background: var(--slate-100);
    border: 1px solid var(--slate-200);
    border-radius: 0.4rem;
    padding: 0.18rem 0.55rem;
  }
  .chat-sources-unavailable { font-size: 0.78rem; font-style: italic; color: var(--slate-400); margin: 0; }
  .chat-boundary {
    margin: 0 0 0.9rem;
    padding: 0.2rem 0;
    font-size: 0.78rem;
    color: var(--amber-800);
  }
  .chat-boundary:last-child { margin-bottom: 0; }

  #followup-label {
    font-size: 0.78rem;
    font-weight: 600;
    color: var(--slate-600);
    margin-bottom: 0.4rem;
  }
  .followup-suggestions { display: flex; flex-wrap: wrap; gap: 0.4rem; margin: 0 0 0.5rem; }
  .suggestion-chip {
    background: #fff;
    border: 1px solid var(--slate-200);
    border-radius: 999px;
    padding: 0.35rem 0.75rem;
    font-size: 0.78rem;
    color: var(--blue-600);
    cursor: pointer;
  }
  .suggestion-chip:hover { background: var(--blue-50); border-color: var(--blue-500); }
  .suggestion-chip:focus { outline: 2px solid var(--blue-500); outline-offset: 1px; }

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
    <button type="button" id="about-toggle" class="about-toggle" aria-haspopup="dialog" aria-expanded="false" aria-controls="about-drawer">About &#9662;</button>
  </header>

  <div class="app-body">
    <aside class="nav-panel">
      <h2 class="nav-prompt">Not sure what to ask? Start with your situation.</h2>

      <button type="button" id="random-topic-button" class="random-topic-button">Explore a topic</button>

      <div class="panel-card">
        <p class="panel-label"><span class="step-number">Step 1</span><span class="step-title">Your situation</span></p>
        <div id="situation-list" class="situation-list"></div>
      </div>

      <div id="topic-panel" class="panel-card" hidden>
        <p class="panel-label"><span class="step-number">Step 2</span><span class="step-title">Choose a topic</span></p>
        <input type="search" id="topic-search" placeholder="Search approved topics..." aria-label="Search approved topics">
        <div id="topic-list" class="topic-list"></div>
      </div>

      <div id="starter-panel" class="panel-card" hidden>
        <p class="panel-label"><span class="step-number">Step 3</span><span class="step-title">Start exploring</span></p>
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

      <p id="followup-label" hidden>Continue exploring</p>
      <div id="followup-suggestions" class="followup-suggestions" hidden>
        <button type="button" class="suggestion-chip" data-suggestion="Explain more simply">Explain more simply</button>
        <button type="button" class="suggestion-chip" data-suggestion="What does this mean?">What does this mean?</button>
        <button type="button" class="suggestion-chip" data-suggestion="Tell me more">Tell me more</button>
      </div>

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

  <div id="about-backdrop" class="about-backdrop" hidden></div>
  <aside id="about-drawer" class="about-drawer" hidden role="dialog" aria-modal="true" aria-labelledby="about-drawer-title">
    <div class="about-drawer-header">
      <h2 id="about-drawer-title">About this Research Interface</h2>
      <button type="button" id="about-close" class="about-close" aria-label="Close About panel">&times;</button>
    </div>
    <div class="about-drawer-body">
      <section class="about-section">
        <h3><button type="button" class="about-accordion-trigger" aria-expanded="false" aria-controls="about-panel-1" id="about-trigger-1">What is this<span class="about-accordion-icon" aria-hidden="true">&#9662;</span></button></h3>
        <div id="about-panel-1" class="about-accordion-panel" role="region" aria-labelledby="about-trigger-1" hidden>
          <p>Safe Medical AI Oncology is a research interface for exploring evidence-grounded oncology information through a controlled conversational experience.</p>
          <p>The system is designed to help users, mostly patients, explore approved oncology topics, understand medical concepts in accessible language, and trace answers to curated evidence sources.</p>
        </div>
      </section>
      <section class="about-section">
        <h3><button type="button" class="about-accordion-trigger" aria-expanded="false" aria-controls="about-panel-2" id="about-trigger-2">Objective<span class="about-accordion-icon" aria-hidden="true">&#9662;</span></button></h3>
        <div id="about-panel-2" class="about-accordion-panel" role="region" aria-labelledby="about-trigger-2" hidden>
          <p>To explore how evidence-grounded AI can support safer, understandable, and traceable access to oncology information while maintaining explicit boundaries between educational information and clinical decision-making.</p>
        </div>
      </section>
      <section class="about-section">
        <h3><button type="button" class="about-accordion-trigger" aria-expanded="false" aria-controls="about-panel-3" id="about-trigger-3">Scope<span class="about-accordion-icon" aria-hidden="true">&#9662;</span></button></h3>
        <div id="about-panel-3" class="about-accordion-panel" role="region" aria-labelledby="about-trigger-3" hidden>
          <div class="about-scope-grid">
            <div class="about-scope-card">
              <p class="about-scope-heading">In scope</p>
              <ul>
                <li>Evidence-grounded oncology education</li>
                <li>Approved knowledge topics</li>
                <li>Patient-friendly explanations</li>
                <li>Follow-up educational questions</li>
                <li>Source transparency</li>
                <li>Controlled research evaluation</li>
              </ul>
            </div>
            <div class="about-scope-card">
              <p class="about-scope-heading">Out of scope</p>
              <ul>
                <li>Diagnosis</li>
                <li>Individual treatment recommendations</li>
                <li>Patient-specific clinical decisions</li>
                <li>Emergency medical advice</li>
                <li>Clinical deployment</li>
              </ul>
            </div>
          </div>
        </div>
      </section>
      <section class="about-section">
        <h3><button type="button" class="about-accordion-trigger" aria-expanded="false" aria-controls="about-panel-4" id="about-trigger-4">How to use<span class="about-accordion-icon" aria-hidden="true">&#9662;</span></button></h3>
        <div id="about-panel-4" class="about-accordion-panel" role="region" aria-labelledby="about-trigger-4" hidden>
          <ol>
            <li><strong>Choose your situation</strong> &mdash; Select the context that best matches what you want to explore.</li>
            <li><strong>Choose an approved topic</strong> &mdash; Start with a curated oncology topic.</li>
            <li><strong>Read the answer</strong> &mdash; Review the explanation and its cited sources.</li>
            <li><strong>Ask a follow-up</strong> &mdash; Ask for clarification or explore the topic further.</li>
          </ol>
          <p class="about-note">Please do not enter identifiable patient information or other sensitive personal data.</p>
        </div>
      </section>
      <section class="about-section">
        <h3><button type="button" class="about-accordion-trigger" aria-expanded="false" aria-controls="about-panel-5" id="about-trigger-5">Evidence &amp; Sources<span class="about-accordion-icon" aria-hidden="true">&#9662;</span></button></h3>
        <div id="about-panel-5" class="about-accordion-panel" role="region" aria-labelledby="about-trigger-5" hidden>
          <p>Responses are generated from a curated oncology knowledge base populated from selected authoritative and clinically relevant sources.</p>
          <p>Sources may include:</p>
          <ul>
            <li>NCI</li>
            <li>NCCN Patient</li>
            <li>ESMO</li>
            <li>American Cancer Society</li>
            <li>Other approved evidence materials</li>
          </ul>
        </div>
      </section>
      <section class="about-section">
        <h3><button type="button" class="about-accordion-trigger" aria-expanded="false" aria-controls="about-panel-6" id="about-trigger-6">Safety boundary<span class="about-accordion-icon" aria-hidden="true">&#9662;</span></button></h3>
        <div id="about-panel-6" class="about-accordion-panel" role="region" aria-labelledby="about-trigger-6" hidden>
          <p class="about-safety-label">Research / Controlled Evaluation</p>
          <p>This interface has not been clinically validated and is not intended for diagnosis, treatment selection, or patient-specific clinical decision-making.</p>
        </div>
      </section>
      <section class="about-section">
        <h3><button type="button" class="about-accordion-trigger" aria-expanded="false" aria-controls="about-panel-7" id="about-trigger-7">Research &amp; Evaluation<span class="about-accordion-icon" aria-hidden="true">&#9662;</span></button></h3>
        <div id="about-panel-7" class="about-accordion-panel" role="region" aria-labelledby="about-trigger-7" hidden>
          <p>This interface is developed as part of a controlled research workflow focusing on:</p>
          <p>Evidence fidelity &middot; Safety boundaries &middot; Human interaction &middot; Traceability &middot; Validation</p>
        </div>
      </section>
      <section class="about-section">
        <h3><button type="button" class="about-accordion-trigger" aria-expanded="false" aria-controls="about-panel-8" id="about-trigger-8">About the team<span class="about-accordion-icon" aria-hidden="true">&#9662;</span></button></h3>
        <div id="about-panel-8" class="about-accordion-panel" role="region" aria-labelledby="about-trigger-8" hidden>
          <p>This research project integrates perspectives from medicine, oncology, health informatics, computational methods, and AI system design.</p>
          <p>The interface is developed as a research and controlled-evaluation platform for studying safe, evidence-grounded medical AI.</p>
          <p class="about-team-label">Team members</p>
          <ul>
            <li>Nhan Tran, MD, MSc.</li>
            <li>Quy Nguyen Hoang, MD, PhD.</li>
          </ul>
        </div>
      </section>
      <section class="about-section">
        <h3><button type="button" class="about-accordion-trigger" aria-expanded="false" aria-controls="about-panel-9" id="about-trigger-9">Model / System Information<span class="about-accordion-icon" aria-hidden="true">&#9662;</span></button></h3>
        <div id="about-panel-9" class="about-accordion-panel" role="region" aria-labelledby="about-trigger-9" hidden>
        <dl class="about-system-info">
          <dt>System</dt>
          <dd>Safe Medical AI Oncology</dd>
          <dt>Interface type</dt>
          <dd>Controlled research / evaluation interface</dd>
          <dt>Knowledge approach</dt>
          <dd>Evidence-grounded oncology knowledge from approved/curated sources</dd>
          <dt>Interaction</dt>
          <dd>Controlled conversational exploration of approved topics</dd>
          <dt>Primary research concerns</dt>
          <dd>Evidence fidelity, safety boundaries, traceability, human interaction, validation</dd>
          <dt>Clinical status</dt>
          <dd>Not clinically validated. Not for diagnosis. Not for treatment selection. Not for patient-specific clinical decision-making. Not clinically deployed.</dd>
        </dl>
        </div>
      </section>
    </div>
  </aside>

  <script>
    (function () {
      // --- Track 2: controlled navigation catalog, embedded server-side
      // from the SAME manifest projection EvaluationCaseResolver uses
      // (case_id/pp_title/controlled_question only). No PP/EC identifiers
      // are ever displayed to the user -- only pp_title and
      // controlled_question. Never hard-coded, never a second manifest.
      var CATALOG = __CATALOG_JSON__;

      // B06: the five approved Situations and their governed Topic
      // mapping, embedded server-side from the SAME single authoritative
      // artifact main.py reads (see
      // data/B06_SITUATION_NAVIGATION_MAPPING_README.md). Never
      // hard-coded here, never a second mapping source.
      var SITUATION_MAPPING = __SITUATION_MAPPING_JSON__;
      var SITUATIONS = SITUATION_MAPPING.situations;

      // situation_id -> { case_id: true, ... }, built once from the
      // embedded mapping's (situation_id, case_id) pairs.
      var SITUATION_CASE_IDS = {};
      SITUATION_MAPPING.mappings.forEach(function (m) {
        if (!SITUATION_CASE_IDS[m.situation_id]) {
          SITUATION_CASE_IDS[m.situation_id] = {};
        }
        SITUATION_CASE_IDS[m.situation_id][m.case_id] = true;
      });

      // The Topic filter currently in effect (a SITUATION_CASE_IDS entry),
      // or null when unfiltered (Random Topic, or no Situation chosen
      // yet). Only renderSituations()'s click handler and the Random
      // Topic handler below ever set this.
      var activeAllowedCaseIds = null;

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
        SITUATIONS.forEach(function (situation) {
          var btn = document.createElement("button");
          btn.type = "button";
          btn.className = "situation-card";
          btn.textContent = situation.label;
          btn.setAttribute("aria-pressed", "false");
          btn.addEventListener("click", function () {
            Array.prototype.forEach.call(
              situationList.querySelectorAll(".situation-card"),
              function (el) { el.setAttribute("aria-pressed", el === btn ? "true" : "false"); }
            );
            // Governed Situation -> Topic filter (B06): only this
            // Situation's mapped case_ids are shown, via the same
            // CATALOG/selectTopic() every other Topic entry point uses.
            activeAllowedCaseIds = SITUATION_CASE_IDS[situation.situation_id] || {};
            topicPanel.hidden = false;
            topicSearch.value = "";
            topicSearch.focus();
            renderTopics("", activeAllowedCaseIds);
          });
          situationList.appendChild(btn);
        });
      }

      function renderTopics(filterText, allowedCaseIds) {
        clearChildren(topicList);
        var needle = filterText.trim().toLowerCase();
        CATALOG.filter(function (item) {
          if (allowedCaseIds && !allowedCaseIds[item.case_id]) {
            return false;
          }
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
        // B08: selecting any topic (manually, via a Situation, or via
        // Random Topic -- all funnel through this one function) starts a
        // fresh interaction; the follow-up affordance only reappears once
        // a real exchange completes on this newly selected case_id (see
        // hasFollowupContext()).
        followupLabel.hidden = true;
        followupSuggestions.hidden = true;

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
        renderTopics(topicSearch.value, activeAllowedCaseIds);
      });

      // Random Topic: a navigation convenience only, unaffected by B06.
      // Picks one entry from the SAME, unfiltered CATALOG the Topic list
      // already renders from (no second source of truth), then routes it
      // through the exact same selectTopic() function manual Topic
      // clicks and Situation-filtered Topic clicks both use --
      // selectedCaseId is set the same way in every case.
      var randomTopicButton = document.getElementById("random-topic-button");
      randomTopicButton.addEventListener("click", function () {
        if (!CATALOG.length) {
          return;
        }
        var item = CATALOG[Math.floor(Math.random() * CATALOG.length)];

        activeAllowedCaseIds = null;
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
      var followupLabel = document.getElementById("followup-label");
      var followupSuggestions = document.getElementById("followup-suggestions");

      // Follow-up suggestion chips (fixed, non-clinical UI copy): populate
      // the existing question input only -- same pattern as a question
      // starter chip (selectTopic() above). Never submits the form, never
      // calls fetch, never introduces new state.
      Array.prototype.forEach.call(
        document.querySelectorAll(".suggestion-chip"),
        function (btn) {
          btn.addEventListener("click", function () {
            input.value = btn.getAttribute("data-suggestion");
            input.focus();
          });
        }
      );

      // --- About drawer: presentation-only, no backend request -----------
      var aboutToggle = document.getElementById("about-toggle");
      var aboutDrawer = document.getElementById("about-drawer");
      var aboutBackdrop = document.getElementById("about-backdrop");
      var aboutClose = document.getElementById("about-close");

      function openAboutDrawer() {
        aboutDrawer.hidden = false;
        aboutBackdrop.hidden = false;
        aboutToggle.setAttribute("aria-expanded", "true");
        aboutClose.focus();
      }

      function closeAboutDrawer() {
        aboutDrawer.hidden = true;
        aboutBackdrop.hidden = true;
        aboutToggle.setAttribute("aria-expanded", "false");
        aboutToggle.focus();
      }

      aboutToggle.addEventListener("click", function () {
        if (aboutDrawer.hidden) {
          openAboutDrawer();
        } else {
          closeAboutDrawer();
        }
      });
      aboutClose.addEventListener("click", closeAboutDrawer);
      aboutBackdrop.addEventListener("click", closeAboutDrawer);
      document.addEventListener("keydown", function (event) {
        if (event.key === "Escape" && !aboutDrawer.hidden) {
          closeAboutDrawer();
        }
      });

      // R3: each About section's heading is an accessible accordion
      // trigger toggling its own panel only -- existing hidden/aria-*
      // convention, no new interaction pattern. Content itself (inside
      // each panel) is unchanged from the prior non-collapsible markup.
      Array.prototype.forEach.call(
        document.querySelectorAll(".about-accordion-trigger"),
        function (trigger) {
          trigger.addEventListener("click", function () {
            var panel = document.getElementById(trigger.getAttribute("aria-controls"));
            var expanded = trigger.getAttribute("aria-expanded") === "true";
            trigger.setAttribute("aria-expanded", expanded ? "false" : "true");
            panel.hidden = expanded;
          });
        }
      );

      // B08: bounded, same-session-only follow-up context -- the single
      // most recent exchange only, held purely in this page's JS memory.
      // Never written to localStorage/sessionStorage/cookies/a server
      // database, so it is lost on reload and never crosses sessions.
      // Only ever set from a real completed exchange (never fabricated),
      // and only ever used when the follow-up is asked about the SAME
      // case_id that produced it -- switching Topic/Random Topic changes
      // selectedCaseId, which makes hasFollowupContext() false again
      // until a new exchange completes under the new case.
      var lastQuestion = null;
      var lastAnswer = null;
      var lastCaseId = null;

      function hasFollowupContext() {
        return lastQuestion !== null && lastAnswer !== null && lastCaseId === selectedCaseId;
      }

      // P0: a small, bounded, safe Markdown-SUBSET renderer for assistant
      // answer text only -- **bold**, *italic*, paragraph breaks, and
      // simple "- "/"1. " lists. Builds DOM nodes directly via
      // createElement/createTextNode/textContent throughout; never sets
      // innerHTML with answer content and never evaluates anything, so
      // governed-but-still-external LLM-generated text can never inject
      // arbitrary markup. Not a general Markdown implementation -- only
      // the bounded subset actually observed in answer content.
      function appendInlineFormatted(parent, text) {
        var pattern = /\\*\\*([^*]+)\\*\\*|\\*([^*]+)\\*/g;
        var lastIndex = 0;
        var match;
        while ((match = pattern.exec(text)) !== null) {
          if (match.index > lastIndex) {
            parent.appendChild(document.createTextNode(text.slice(lastIndex, match.index)));
          }
          if (match[1] !== undefined) {
            var strong = document.createElement("strong");
            strong.textContent = match[1];
            parent.appendChild(strong);
          } else {
            var em = document.createElement("em");
            em.textContent = match[2];
            parent.appendChild(em);
          }
          lastIndex = pattern.lastIndex;
        }
        if (lastIndex < text.length) {
          parent.appendChild(document.createTextNode(text.slice(lastIndex)));
        }
      }

      function renderFormattedAnswer(container, text) {
        var lines = String(text).split("\\n");
        var i = 0;
        while (i < lines.length) {
          if (lines[i].trim() === "") {
            i++;
            continue;
          }
          var orderedMatch = /^\\s*\\d+\\.\\s+(.*)$/.exec(lines[i]);
          var unorderedMatch = /^\\s*-\\s+(.*)$/.exec(lines[i]);
          if (orderedMatch || unorderedMatch) {
            var isOrdered = !!orderedMatch;
            var listEl = document.createElement(isOrdered ? "ol" : "ul");
            listEl.className = "chat-answer-list";
            while (i < lines.length) {
              var itemMatch = isOrdered
                ? /^\\s*\\d+\\.\\s+(.*)$/.exec(lines[i])
                : /^\\s*-\\s+(.*)$/.exec(lines[i]);
              if (!itemMatch) {
                break;
              }
              var li = document.createElement("li");
              appendInlineFormatted(li, itemMatch[1]);
              listEl.appendChild(li);
              i++;
            }
            container.appendChild(listEl);
            continue;
          }

          var paraLines = [];
          while (
            i < lines.length &&
            lines[i].trim() !== "" &&
            !/^\\s*-\\s+/.test(lines[i]) &&
            !/^\\s*\\d+\\.\\s+/.test(lines[i])
          ) {
            paraLines.push(lines[i]);
            i++;
          }
          var p = document.createElement("p");
          p.className = "chat-answer-paragraph";
          paraLines.forEach(function (paraLine, idx) {
            if (idx > 0) {
              p.appendChild(document.createElement("br"));
            }
            appendInlineFormatted(p, paraLine);
          });
          container.appendChild(p);
        }
        if (!container.hasChildNodes()) {
          container.appendChild(document.createTextNode(text));
        }
      }

      function appendMessage(role, text) {
        var el = document.createElement("div");
        el.className = "chat-message " + role;
        if (role === "assistant") {
          renderFormattedAnswer(el, text);
        } else {
          el.textContent = text;
        }
        history.appendChild(el);
        history.scrollTop = history.scrollHeight;
      }

      // B09: `sources` follows the /chat/query response's three-state
      // contract -- null means no evidence-based source concept applies
      // to this answer (nothing rendered, unchanged prior behavior); an
      // empty array means real evidence was used but no governed source
      // label could be resolved (the honest "unavailable" fallback, never
      // "No evidence" and never a PP ID); a populated array is the
      // governed, human-readable Primary Source Set for this answer.
      function appendSources(sources) {
        var el = document.createElement("div");
        el.className = "chat-sources";
        if (sources.length === 0) {
          var unavailable = document.createElement("p");
          unavailable.className = "chat-sources-unavailable";
          unavailable.textContent = "Evidence information unavailable";
          el.appendChild(unavailable);
        } else {
          var label = document.createElement("p");
          label.className = "chat-sources-label";
          label.textContent = "Evidence Sources";
          el.appendChild(label);

          var chips = document.createElement("div");
          chips.className = "chat-sources-chips";
          sources.forEach(function (source) {
            var chip = document.createElement("span");
            chip.className = "source-chip";
            chip.textContent = source;
            chips.appendChild(chip);
          });
          el.appendChild(chips);
        }
        history.appendChild(el);
        history.scrollTop = history.scrollHeight;
      }

      // B11: bounded, honest wording per distinct governed `status` value
      // -- never the raw internal status token shown to the user, and
      // never a single generic label collapsing every non-COMPLETED
      // status into one undifferentiated "out of scope" message. The
      // underlying `data.answer` text (already governed -- e.g.
      // SAFE_FALLBACK's locked no-evidence text) is never rewritten by
      // this notice; it is only an additional, clearly distinguishable
      // element alongside it. Any status not explicitly listed here
      // (there is none today, but this stays defensive) falls back to a
      // bounded, non-specific notice rather than silently rendering
      // nothing or exposing the raw status string.
      var STATUS_BOUNDARY_MESSAGES = {
        SAFE_FALLBACK: "No governed evidence was available to answer this question.",
        UNKNOWN_CASE: "This question could not be matched to an approved topic.",
        MALFORMED_CASE_ID: "This question could not be matched to an approved topic.",
        PROJECTION_UNAVAILABLE: "This question could not be matched to an approved topic.",
        RETRIEVAL_FAILURE: "This request could not be completed due to a system issue. Please try again.",
        EVIDENCE_ASSEMBLY_FAILURE: "This request could not be completed due to a system issue. Please try again.",
        INTEGRATION_FAILURE: "This request could not be completed due to a system issue. Please try again.",
        GENERATION_FAILURE: "This request could not be completed due to a system issue. Please try again.",
        VALIDATION_FAILURE: "This request could not be completed due to a system issue. Please try again.",
        SAFETY_BLOCKED: "This request could not be completed.",
        NOT_RELEVANT: "This request does not appear to relate to the selected topic."
      };

      function appendBoundaryNotice(status) {
        var el = document.createElement("div");
        el.className = "chat-boundary";
        el.textContent = STATUS_BOUNDARY_MESSAGES[status] ||
          "This response has a limitation that could not be described in more detail.";
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

        // B08 race-condition fix: capture the case_id this specific
        // request is actually being sent for, at send time. selectedCaseId
        // itself is not disabled/locked while a request is pending (Topic/
        // Situation/Random Topic selection remains clickable), so it can
        // change before this request's response arrives. requestCaseId is
        // a per-call local, unaffected by any later change to
        // selectedCaseId, so both the outbound request and the eventual
        // response handling stay associated with the case that was
        // actually selected when THIS request was sent -- never whatever
        // happens to be selected when the response later arrives.
        var requestCaseId = selectedCaseId;

        // B08: when this question follows a completed exchange on the
        // SAME case_id, include that single bounded prior exchange so the
        // user can naturally refer to it (e.g. "explain that part again")
        // without restating it. The displayed history above always shows
        // only the raw `question` the user typed -- this composed text is
        // only what is sent through the existing governed request_text
        // field, unchanged from every other question's contract.
        var requestText = question;
        if (hasFollowupContext()) {
          requestText =
            "[Previous question]: " + lastQuestion +
            "\\n[Previous answer]: " + lastAnswer +
            "\\n[Follow-up question]: " + question;
        }

        fetch("/chat/query", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ message: requestText, case_id: requestCaseId }),
        })
          .then(function (response) {
            if (!response.ok) {
              throw new Error("Request failed with status " + response.status);
            }
            return response.json();
          })
          .then(function (data) {
            setLoading(false);
            if (data.status === "COMPLETED") {
            appendMessage("assistant", data.answer);
            }
            // B11: a non-COMPLETED status (SAFE_FALLBACK, a resolution
            // failure, a technical pipeline failure, etc.) still arrives
            // here as a normal 200 response -- the boundary notice makes
            // that distinction visible without altering data.answer
            // itself (already governed text, e.g. SAFE_FALLBACK's locked
            // no-evidence response).
            if (data.status !== "COMPLETED") {
              appendBoundaryNotice(data.status);
            }
            if (data.sources !== null && data.sources !== undefined) {
              appendSources(data.sources);
            }
            // B11: only a real COMPLETED exchange ever updates the bounded
            // follow-up context -- a non-COMPLETED status (this still
            // arrives as a normal 200 response, not the .catch() below)
            // must never be recorded as valid prior substantive context,
            // so a later follow-up can never silently build on a
            // SAFE_FALLBACK/failure response as if it were a real answer.
            // A prior good exchange is also never overwritten with a
            // non-COMPLETED one. lastCaseId is set from requestCaseId
            // (captured above at send time), never from selectedCaseId
            // here -- selectedCaseId may already have changed to a
            // different topic while this request was pending, and the
            // recorded context must stay associated with the case that
            // actually produced it.
            if (data.status === "COMPLETED") {
              lastQuestion = question;
              lastAnswer = data.answer;
              lastCaseId = requestCaseId;
              followupLabel.hidden = false;
              followupSuggestions.hidden = false;
            }
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
