# B07 Execution/Evidence Preparation Layer (Phase 6 Stage 2 Track 3, B07 + B10)

## What this is

B07 is the bounded **capability** to invoke the existing governed
execution path for one approved `case_id` and durably record what
happened, stage by stage. It is a preparation layer, not a campaign:

```text
case_id
  -> api.main._run_controlled_evaluation()   (existing, unmodified path)
  -> CampaignExecutionResult                  (harness.py: DETECT)
  -> record_execution_result()                (capture.py: RECORD)
```

Nothing in this package decides *which* case_ids to run, *when*, or *how
many* — that is an external caller's decision (a future, separately
authorized campaign run), not something this package encodes or defaults.
**This package does not execute a 239-case campaign and makes no claim
that one has occurred.**

## What this is NOT

- **not** a second CER implementation — `harness.execute_case()` calls
  `api.main._run_controlled_evaluation()`, the exact same function
  `/cer/evaluate` and `/chat/query` already both call. No retrieval,
  evidence assembly, prompt construction, provider invocation, or
  validation logic is reimplemented here.
- **not** a second PP/case authority — `execute_case()` accepts only a
  `case_id`; it has no `population_id` parameter and cannot bypass
  `EvaluationCaseResolver`.
- **not** an automatic remediation system — a failed execution is
  recorded as a failure. Nothing in this package retries, substitutes
  evidence/prompt/provider, or otherwise repairs a failure. Any
  reassessment of a recorded failure is a separate, later, human/governed
  step (ASSESS), not something this package performs.
- **not** a clinical validation, clinical effectiveness, or clinical
  deployment claim of any kind. `CampaignExecutionResult` records only
  which existing, already-governed typed outcome occurred at each stage
  — it contains no clinical-quality score, and none is computed anywhere
  in this package.
- **not** a database, queue, or new service. Durable capture is a plain
  append-only JSON Lines file (see `capture.py`).

## Components

- `models.py` — `CampaignExecutionResult` (the durable record schema) and
  `EvidenceCaptureOutcome` (mechanical persistence status only). Every
  clinical/stage outcome field reuses an existing typed enum by reference
  (`CaseResolutionOutcome`, `SafetyAction`, `RetrievalOutcome`,
  `GenerationOutcome`, `CandidateValidationOutcome`, `CEROutcome`,
  `RequestRelevanceOutcome`) — none is duplicated or reinterpreted.
- `harness.py` — `execute_case(case_id, request_text, *, provider=None)`:
  one execution attempt, one result, always returned (even for a failed
  resolution or a `NOT_RELEVANT` request -- see "B12 compatibility" below).
  `provider` is optional; omitting it preserves the existing
  `_select_provider()` default (deterministic unless
  `SMA_OPENAI_API_KEY` is configured), so calling this with no `provider`
  argument is deterministic and makes no real external API call.
- `capture.py` — `record_execution_result(result, path)` appends one JSON
  line to `path` (creating parent directories as needed) and returns the
  result with `evidence_capture_status` set to what actually happened
  (`CAPTURED` or `WRITE_FAILED` — never silently assumed). Append-only:
  an existing recorded line is never rewritten. `read_execution_results(path)`
  reads them back.
- `coverage.py` (B10) — `summarize_campaign_coverage(results)`: a pure,
  read-only aggregation over an already-recorded sequence of
  `CampaignExecutionResult`s. See "B10: coverage aggregation" below.

## Reproducibility fields

`CampaignExecutionResult.repository_commit` is a best-effort `git
rev-parse HEAD` (see `harness._best_effort_repository_commit`), `None`
when it cannot be safely determined (e.g. no `.git` present) — never
fabricated. `execution_id` (fresh per call) and `execution_timestamp`
distinguish repeated executions of the same `case_id` from each other.
`trace_id` reuses the existing `trace.py` mechanism the HTTP layer already
uses, so a campaign execution's logs correlate the same way an HTTP
request's logs already do.

B10 additionally threads through two fields that were already produced
during execution but not previously carried into the durable record:
`evidence_package_id` is exactly the same identifier RTEP Assembly
produced and Generation carried forward (`evidence/models.py`'s
`RuntimeEvidenceMetadata.evidence_package_id`, `generation/models.py`'s
`CandidateResponse.evidence_package_id`) — not a second/independent
evidence-identity system. `provider_model` is the exact configured model
string (`config.get_settings().openai_model`) when the provider used was
`OpenAIProvider`, and `None` for the deterministic provider (which has no
configured model) — see `harness._configured_provider_model`.

## Where results live

This package does not hardcode a default output location — the caller
supplies `path` to `record_execution_result`/`read_execution_results`,
and B10's `scripts/run_campaign_execution.py` (below) keeps that the same
way: its `--output` argument is required, with no default. Choosing and
creating a permanent, governed location for campaign evidence (e.g. under
`09_Evaluation/validation/phase6/`) remains a decision for a separately
authorized campaign run, not this preparation layer or its runner —
nothing under that directory is created by this package.

## B10: coverage aggregation (`coverage.py`)

`summarize_campaign_coverage(results)` is a pure, read-only function over
an already-recorded sequence of `CampaignExecutionResult`s (typically
`read_execution_results()`'s return value). It counts total records,
distinct `case_id`/`resolved_population_id` values, and tallies the
existing `case_resolution_outcome`/`cer_outcome`/`validation_outcome`
vocabularies unchanged — it never re-executes anything, never reads a
file itself, and never claims coverage of any case_id/population_id that
is not present in the records it was given.

## B10: dev-time orchestration runner (`scripts/run_campaign_execution.py`)

A thin script, following the same convention as
`scripts/generate_evaluation_case_manifest_projection.py` (plain
`argparse`, never imported by the FastAPI runtime), that calls
`execute_case()` and `record_execution_result()` once per externally
supplied `case_id` (via `--case-id`/`--case-ids-file`) and prints a
`summarize_campaign_coverage()` summary of the resulting `--output` file.
It selects, samples, and defaults no case set of its own, and it prints
per-case-request text either from the caller's own `--request-text`
override or from that case's existing governed `controlled_question` (the
same text already used by the Chat UI's navigation catalog) — never
invented question text.

## B12 compatibility: selected-PP request relevance

`_run_controlled_evaluation()` (the shared boundary `execute_case()`
calls) can now return a `relevance.RequestRelevanceResult` instead of a
CER result, when the request was genuinely unrelated to the resolved PP
(see `relevance/README.md`). `execute_case()` recognizes this exact
outcome and returns a `CampaignExecutionResult` with
`case_resolution_outcome=RESOLVED` (identity resolution genuinely
succeeded), `request_relevance_outcome=NOT_RELEVANT`, and
`resolved_population_id=None` (no population-level result exists to
report) — never a fabricated retrieval/evidence/generation result, and
never CER/retrieval/generation/provider work for that execution. This is
a pure consumption of the already-decided governed outcome: no relevance
logic is duplicated here.

## Example (illustrative only — this package does not run this itself)

```python
from pathlib import Path
from safe_medical_ai.campaign import execute_case, record_execution_result

result = execute_case("EC-0001", "What is Cancer?")
result = record_execution_result(result, Path("path/chosen/by/caller.jsonl"))
```
