# Governed Prompt Builder (Track 3 BATCH 03)

## What this is

The executable instantiation of the LOCKED `PROMPTING_STRATEGY.md`
(`02_Architecture/knowledge/PROMPTING_STRATEGY.md`), per the locked
architecture:

```text
GenerationContext
  ↓
Navigation Context + Safety Decision + Evidence Package
  ↓
Prompt Builder                    (this module)
  ↓
PromptSpecification
  ↓
Generation -> provider (model-specific rendering happens downstream)
```

Model-independent: this module imports nothing from `llm/`, `generation/`,
`cer/`, `integration/`, or `api/`, and knows nothing about any concrete
provider/vendor/model. Turning a `PromptSpecification` into a specific
provider's literal API request text remains that provider's own
responsibility (see `llm/openai_provider.py`).

## Interfaces

- **`build_prompt(navigation_context, safety_decision, evidence_package, request_text)`**
  — the one explicit, deterministic entry point.
- **`PromptBuilderOutcome`** — `BUILT` / `MISSING_NAVIGATION_CONTEXT` /
  `MISSING_SAFETY_DECISION` / `MISSING_EVIDENCE_PACKAGE`. A distinct
  vocabulary from every other boundary's outcome enum in this codebase.
- **`PromptBuilderResult`** — the atomic result: `outcome`, `specification`
  (`None` unless `outcome is BUILT`), `message`.
- **`PromptSpecification`** — the four locked logical layers
  (PROMPTING_STRATEGY.md §7) plus a `PromptRecord`:
  - `system: SystemLayer` — the system identity/operational-context
    statement already used elsewhere in this codebase (`api/main.py`'s
    `/cer/evaluate` boundary object: `RESEARCH / DEVELOPMENT / CONTROLLED
    EVALUATION ONLY`, etc.) — reused verbatim, not reinvented.
  - `governance: GovernanceLayer` — derived unchanged from the supplied
    `SafetyDecision` (`decision_id`, `risk_class`, `action`,
    `reason_code`). Never independently re-adjudicated here.
  - `evidence: EvidenceLayer` — the supplied `EvidenceItem`s' identity,
    provenance, and governed `content` (Track 3 BATCH 01), in the exact
    order supplied — never reordered, reranked, or modified.
  - `communication: CommunicationLayer` — the user's `request_text` and
    the supplied `NavigationContextPlaceholder`, unchanged.
  - `record: PromptRecord` — `prompt_version`,
    `navigation_context_reference` (`None` — see below),
    `safety_decision_id`, `evidence_package_id`, `generation_timestamp`.

## Locked Prompt Contract (§12)

Navigation Context, Safety Decision, and Evidence Package are all
mandatory. Any one missing (or an Evidence Package present but empty)
blocks prompt construction entirely — `build_prompt` never returns a
partial/best-effort `PromptSpecification`. This mirrors the atomic-result
convention already used by every other boundary in this codebase
(`RTEPAssemblyResult`, `RuntimeIntegrationResult`, `GenerationResult`).

## Why `navigation_context_reference` is `None`

The field exists because the locked Prompt Strategy requires Navigation
Context traceability alongside the Safety Decision and Evidence Package
identifiers. `NavigationContextPlaceholder` (`models/output_contract.py`)
is a deliberately empty scaffold — it carries no fields, and therefore no
identifier of its own — so the current value is `None`: an explicit
representation of "no identifier is available", never a fabricated one.

This does **not** mean Navigation Context was rejected or ignored:
`navigation_context` is still a mandatory, checked Prompt Contract input
(a missing one still produces `MISSING_NAVIGATION_CONTEXT`). It also does
**not** authorize adding an identifier field to
`NavigationContextPlaceholder` — that remains unchanged and out of scope
here. A future, separately approved Navigation Context contract can
populate this same `PromptRecord` field later without any change to the
Prompt Builder's own contract.

## What this module does not do

- Does not retrieve evidence, touch the filesystem, or access the Gold
  Population Package corpus, Knowledge Base, or Knowledge Source Registry.
- Does not adjudicate safety, generate a new `SafetyDecision`, or modify
  the one it is given.
- Does not modify, reorder, or rerank the supplied `EvidenceItem`s.
- Does not invent clinical knowledge, communication style rules, or
  Navigation Context fields/semantics.
- Does not render a `PromptSpecification` into any provider-specific API
  request shape — that remains the concrete provider's job.
- Does not implement `PROMPTING_STRATEGY.md`'s `Response Composition`
  (§13) or `Output Contract` (§14) — both are explicitly downstream,
  post-generation concerns, out of this module's scope.
