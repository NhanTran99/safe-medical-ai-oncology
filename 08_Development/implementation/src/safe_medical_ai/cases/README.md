# Evaluation Case Resolution (Phase 6 Stage 2 Track 2)

## What this is

The controlled boundary that resolves an approved `case_id`
(`EC-0001`..`EC-0239`) to an approved `population_id`, per the locked
architecture decisions (AD-1/AD-2):

```text
authoritative frozen manifest
  ↓
deterministic runtime projection (this module's input)
  ↓
EvaluationCaseResolver                (this module)
  ↓
approved EvaluationCase (PP + expected primary artifact)
```

This is the sole mechanism by which `api/main.py` turns a `case_id` into a
`population_id` for the existing governed CER path. It never performs
retrieval, generation, validation, safety, or clinical reasoning — it is a
static, deterministic dictionary lookup.

## Manifest authority (locked)

`PHASE6_STAGE2_EVALUATION_CASE_MANIFEST_v1.0_FROZEN.xlsx` is the sole
authoritative Evaluation Case Manifest. This module never edits it, never
reinterprets its case definitions, and never becomes a second,
independently editable manifest.

The FastAPI runtime does **not** parse XLSX. Instead:

```text
data/PHASE6_STAGE2_EVALUATION_CASE_MANIFEST_v1.0_FROZEN.xlsx   (authoritative, frozen)
  ↓  scripts/generate_evaluation_case_manifest_projection.py    (dev-time only, uses openpyxl)
data/evaluation_case_manifest_projection.json                   (runtime-consumed, this module's input)
```

The projection contains only what the resolver needs — `case_id`,
`population_id`, `expected_primary_artifact_type` — plus the source
manifest's name, version, and SHA-256 hash for traceability. It is
**regenerated, never hand-edited**: any change to the frozen manifest must
flow through re-running the generator script. `EvaluationCaseResolver`
copies that same source identity/version/hash onto every `EvaluationCase`
it resolves, so every resolved case is fully auditable back to the
specific frozen manifest file it came from.

**The raw frozen `.xlsx` itself is not included in this patch** (a binary
file cannot be represented in a text patch) — place your copy of
`PHASE6_STAGE2_EVALUATION_CASE_MANIFEST_v1.0_FROZEN.xlsx` at
`08_Development/implementation/data/` before running the generator script.
The `evaluation_case_manifest_projection.json` delivered with this patch
was already generated from that exact frozen file (SHA-256
`29463ad268f2b9718201758a14b1c464d8d47e2691a83fd3e6cf6dd93714c167`,
matching the "Manifest SHA-256" recorded on the manifest's own "Freeze
Record" sheet), so no regeneration is required unless the manifest itself
changes.

## Interface

- **`EvaluationCaseResolver(projection_path)`** — dependency-injected,
  same pattern as `FilesystemRepositorySource(source_root)`: loads the
  projection JSON at construction, builds an in-memory `case_id ->
  EvaluationCase` dictionary.
- **`.resolve(case_id)`** — the one explicit, deterministic entry point.
  Never raises. Validates `case_id` against `CASE_ID_PATTERN`
  (`^EC-\\d{4}$`) before lookup.
- **`CaseResolutionOutcome`** — `RESOLVED` / `UNKNOWN_CASE` /
  `MALFORMED_CASE_ID` / `PROJECTION_UNAVAILABLE`. Disjoint from every
  other layer's outcome vocabulary (`RetrievalOutcome`, `CEROutcome`,
  etc.), following the same isolation convention as every prior boundary.
- **`EvaluationCase`** — `case_id`, `population_id`,
  `expected_primary_artifact_type`, plus `source_manifest` /
  `source_manifest_version` / `source_manifest_sha256` for traceability.

## Fail-closed guarantee

`resolve()` never falls back to any specific case — including `EC-0002` /
`PP-0002` — on failure. An unknown `case_id`, a malformed `case_id`, or an
unavailable projection all produce an explicit non-`RESOLVED` outcome with
`case is None`. Callers (see `api/main.py`) must check `outcome ==
CaseResolutionOutcome.RESOLVED` before proceeding; there is no ambiguous
"default" case to accidentally fall through to.

## Not implemented by this module (deferred / out of scope)

- Clinical reasoning, PP selection by clinical meaning, LLM-based case
  inference.
- Patient-state persistence, session/navigation-context tracking.
- Batch/campaign execution across multiple cases.
- Editing or re-authoring the frozen manifest itself.
- Parsing XLSX at runtime (dev-time generator script only).
