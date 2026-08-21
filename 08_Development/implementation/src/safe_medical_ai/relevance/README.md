# Selected-PP Request Relevance (Phase 6 Stage 2 Track 3)

## What this is

A bounded, deterministic, provider-independent check answering exactly
one question:

```text
Given the PP the user already selected (identity already resolved by the
existing, unchanged EvaluationCaseResolver), does the actual submitted
request text share enough vocabulary with that PP's own governed
title/question to proceed?
```

It is **not** a classifier that decides *which* of the 239 PPs a request
belongs to -- that question is never asked. `case_id` remains the sole
identity authority (`cases/resolver.py`, untouched by this package).

## What this is NOT

- **not** a replacement for `EvaluationCaseResolver` -- case identity
  resolution is completely unchanged; this runs strictly after it
  succeeds;
- **not** a 239-way capability classifier or a new capability taxonomy;
- **not** a safety engine -- shares no vocabulary, no trigger conditions,
  and no response text with `safety/`;
- **not** an LLM/embedding classifier -- pure standard-library string/set
  operations, no network call, no API key;
- **not** a second evidence/CER authority -- when the outcome is
  `NOT_RELEVANT`, no `CERRequest` is ever constructed and `CERRuntime` is
  never invoked (see `api/main.py:_run_controlled_evaluation`);
- **not** clinically validated and makes no clinical-quality claim.

## Mechanism

`evaluate_request_relevance(message, *, pp_title, controlled_question)`
computes a coverage score: the fraction of the message's own significant
(stopword-filtered) tokens that also appear in `pp_title` +
`controlled_question`'s own token set. `RELEVANT` whenever that score is
greater than zero (at least one shared significant term); `NOT_RELEVANT`
whenever it is exactly zero (no shared significant term at all).

## Threshold status -- explicitly NOT YET GOVERNED beyond the zero-overlap rule

A genuine, empirically-calibrated numeric acceptance threshold (e.g. "at
least 30% overlap") could **not** be responsibly derived from existing
governed material. The only positive-example construction available from
governed data (a case's own `controlled_question` used as the message
against its own target) is a trivial self-identical match -- it always
scores `1.0` and carries no information about what score a legitimately
*differently phrased* on-topic question should receive. Per the locked
instruction not to invent a threshold the evidence cannot support, no
such number was chosen. The rule actually shipped (`score > 0`) requires
no calibration because it is the structural minimum evidentiary bar, not
an empirically-tuned cutoff -- see
`data/B12_REQUEST_RELEVANCE_CALIBRATION.md` for the full evaluation
(positive/negative distributions over the real 239-entry manifest,
observed false-allow rate, and this exact limitation, recorded rather
than hidden).

## Fail-open / fail-closed boundary

- Missing `pp_title`/`controlled_question` for the resolved case (not
  observed in the shipped 239-entry projection, defensive only): fails
  **open** (`RELEVANT`) -- a data-availability gap is not evidence the
  user's request is off-topic.
- Zero shared significant vocabulary: fails **closed** (`NOT_RELEVANT`)
  -- per the locked anti-force-mapping principle, absence of evidence is
  treated as insufficient evidence, not as a presumption of relevance.

## B08 follow-up handling

A B08-composed follow-up message contains fixed prior-context markers
(`[Previous question]: ... [Previous answer]: ... [Follow-up question]:
...`), constructed client-side only when `hasFollowupContext()` is true --
which itself requires a real prior COMPLETED exchange on this exact
`case_id` (B08/B11's own existing gating). Such a request's topical
continuity with the selected PP is therefore already established before
this module would ever see it. `api/main.py` detects the marker's
presence and does not call `evaluate_request_relevance` at all for such
requests -- scoring only a short new-question segment in isolation (e.g.
"Can you clarify?") would almost always show zero shared topic
vocabulary and wrongly block a legitimate follow-up. This is a deliberate
scope decision, not a weakening: the check is scoped to the class of
request it was designed for (a fresh, non-follow-up question against the
selected PP), and B08's own existing gating already covers the follow-up
case. This package itself has no B08-specific logic; the marker check is
a small helper in `api/main.py`, right where the composed text already
arrives.

## Test-fixture contract note

Any test that submits a request expecting normal governed execution
(`COMPLETED`) must use real, on-topic request text for the `case_id`
under test (e.g. that case's own `controlled_question` from
`data/evaluation_case_manifest_projection.json`) -- a semantically
meaningless placeholder (`"test question"`, `"q1"`, etc.) is, correctly,
no longer sufficient once this boundary exists. This is a test-fixture
contract, not a change to any other module's behavior.
