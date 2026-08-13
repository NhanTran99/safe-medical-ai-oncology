# Runtime Integration Boundary (Task #006)

## What this is

The controlled boundary between the immutable Runtime Evidence Package
(Task #005) and a future Generation layer, per the locked architecture:

```text
Request / Intent ───────┐
Navigation Context ─────┤
RTEP (immutable) ───────┤
Runtime Constraints ────┘
          ↓
Runtime Integration              (this module)
          ↓
GenerationContext
          ↓
[Generation — future task]
```

Dependency direction is `integration -> evidence -> retrieval` — nothing in
`retrieval/` or `evidence/` is imported *by* them from here, and neither is
modified by this module.

## Interfaces

- **`RuntimeIntegrationInput`** — explicit inputs: `request_text`,
  `navigation_context` (reuses `NavigationContextPlaceholder` from
  `models/output_contract.py` per the spec's "do not invent external
  schemas when an existing locked model can be reused" instruction —
  Task #006 does not add fields to it), `rtep` (`RuntimeEvidencePackage |
  None` — `None` means no RTEP is available), `runtime_constraints`.
- **`RuntimeConstraints`** — structural placeholder for applicable
  runtime/delivery constraints, deliberately empty for the same reason
  `NavigationContextPlaceholder` is empty: field-level schema is deferred
  (OUTPUT_CONTRACT.md §11), and this task only needs to prove constraints
  are carried through unchanged, not interpret their content.
- **`EvidenceState`** — `HAS_EVIDENCE` / `EMPTY`, carried on
  `GenerationContext` so a caller holding only the context (not the raw
  RTEP) can see whether it has evidence without separately inspecting
  `rtep.evidence`.
- **`GenerationContext`** — the immutable, derived context: `integration_id`
  and `integration_timestamp` (generated at integration time, the same
  "legitimately runtime-generated identity/timestamp" pattern Task #005
  established for `evidence_package_id`/`generation_timestamp`), plus
  `request_text`, `navigation_context`, `rtep` (the *same* immutable RTEP
  object — referenced, never copied or reconstructed), `runtime_constraints`,
  `evidence_state`. A derived orchestration object, not a second evidence
  authority.
- **`RuntimeIntegrationOutcome`** — `INTEGRATED` / `EMPTY_EVIDENCE` /
  `INVALID_INPUT` / `MISSING_RTEP` / `INTEGRATION_FAILURE`. A distinct
  vocabulary from `RetrievalOutcome`, `RTEPAssemblyOutcome`, and
  OUTPUT_CONTRACT's `ValidationOutcome` — never merged with any of them.
- **`RuntimeIntegrationResult`** — the atomic result: `outcome`, `context`
  (`None` unless `outcome` is `INTEGRATED` or `EMPTY_EVIDENCE`), `message`.
- **`integrate_runtime_context(integration_input)`** — the one explicit,
  deterministic entry point (spec section 5).

## Why `EMPTY_EVIDENCE` still produces a `GenerationContext`

Unlike a plain failure, an RTEP with zero evidence items is a legitimate,
valid state (Task #005 §8.2 / this spec §6.2): "do not convert EMPTY into
technical failure." So `EMPTY_EVIDENCE` still returns a complete, valid
`GenerationContext` (with `evidence_state=EMPTY`) — not `context=None` — so
a downstream caller can still proceed with a controlled
insufficient-evidence path (e.g. a future SAFE_FALLBACK) rather than losing
all context. `context=None` is reserved for the outcomes where integration
genuinely produced nothing usable: `INVALID_INPUT`, `MISSING_RTEP`,
`INTEGRATION_FAILURE`.

## Why `INTEGRATION_FAILURE` has no organic trigger through the typed API

Every field on `RuntimeIntegrationInput` is already validated (non-blank,
correctly typed) at its own construction time by Pydantic, so under normal
typed usage `GenerationContext` construction inside
`integrate_runtime_context` cannot fail. The `try`/`except ValidationError`
around it is a defensive completeness measure — an unexpected contract
violation fails as a controlled `INTEGRATION_FAILURE` rather than an
uncaught exception — and is tested via `pytest.monkeypatch` forcing the
construction call to raise, not via any input a typed caller could produce.

## Assembly semantics

| `integration_input` | `.rtep` | Result |
|---|---|---|
| `None` | — | `INVALID_INPUT`, no context |
| present | `None` | `MISSING_RTEP`, no context |
| present | present, `evidence == ()` | `EMPTY_EVIDENCE`, valid context (`evidence_state=EMPTY`) |
| present | present, non-empty | `INTEGRATED`, valid context (`evidence_state=HAS_EVIDENCE`) |
| present | present | (construction contract violation — not reachable via typed input) `INTEGRATION_FAILURE`, no context |

Integration never re-sorts, reranks, deduplicates, or repairs the RTEP it
receives — it references the same immutable object, and evidence
ordering/provenance/metadata are exactly what Task #005 already produced.

## Not implemented by this task (deferred / out of scope)

- Generation, LLM invocation, prompt construction, output validation,
  clinical/safety reasoning — everything downstream of `GenerationContext`.
- A real schema for `RuntimeConstraints` or richer Navigation Context
  fields — both remain the same deferred placeholders they already were.
- Any repository/filesystem/retrieval access — integration only transforms
  whatever `RuntimeIntegrationInput` it is given.
