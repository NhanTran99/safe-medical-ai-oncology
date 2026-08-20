# B07 Execution/Evidence Preparation Layer (Phase 6 Stage 2 Track 3, B07)

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
  `GenerationOutcome`, `CandidateValidationOutcome`, `CEROutcome`) — none
  is duplicated or reinterpreted.
- `harness.py` — `execute_case(case_id, request_text, *, provider=None)`:
  one execution attempt, one result, always returned (even for a failed
  resolution). `provider` is optional; omitting it preserves the existing
  `_select_provider()` default (deterministic unless
  `SMA_OPENAI_API_KEY` is configured), so calling this with no `provider`
  argument is deterministic and makes no real external API call.
- `capture.py` — `record_execution_result(result, path)` appends one JSON
  line to `path` (creating parent directories as needed) and returns the
  result with `evidence_capture_status` set to what actually happened
  (`CAPTURED` or `WRITE_FAILED` — never silently assumed). Append-only:
  an existing recorded line is never rewritten. `read_execution_results(path)`
  reads them back.

## Reproducibility fields

`CampaignExecutionResult.repository_commit` is a best-effort `git
rev-parse HEAD` (see `harness._best_effort_repository_commit`), `None`
when it cannot be safely determined (e.g. no `.git` present) — never
fabricated. `execution_id` (fresh per call) and `execution_timestamp`
distinguish repeated executions of the same `case_id` from each other.
`trace_id` reuses the existing `trace.py` mechanism the HTTP layer already
uses, so a campaign execution's logs correlate the same way an HTTP
request's logs already do.

## Where results live

This package does not hardcode a default output location — the caller
supplies `path` to `record_execution_result`/`read_execution_results`.
Choosing and creating a permanent, governed location for campaign
evidence (e.g. under `09_Evaluation/validation/phase6/`) is a decision
for the future campaign-execution task itself, not this preparation
layer — nothing under that directory is created by this package.

## Example (illustrative only — this package does not run this itself)

```python
from pathlib import Path
from safe_medical_ai.campaign import execute_case, record_execution_result

result = execute_case("EC-0001", "What is Cancer?")
result = record_execution_result(result, Path("path/chosen/by/caller.jsonl"))
```
