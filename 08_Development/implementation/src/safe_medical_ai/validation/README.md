# Validation Boundary (Task #008)

## What this is

The controlled downstream evaluator of a `CandidateResponse` (Task #007),
per the locked architecture:

```text
Generation
  ↓
CandidateResponse
  ↓
Validation                        (this module)
  ↓
ValidationResult
```

Validation is a **downstream evaluator**, never a second retrieval or
generation authority. It may inspect the `CandidateResponse`, the
authoritative RTEP, and traceability/policy-version context — it may not
initiate upstream operations. Dependency direction is strictly one-way:
`generation → validation`, `integration/evidence → validation` (read-only).

## `VALID` ≠ clinically safe

This is the single most important boundary this module enforces (spec
section 15):

> `VALID` means only that a `CandidateResponse` satisfies the locked
> Validation contract.

It does **not** mean a diagnosis is correct, a treatment is appropriate, a
patient-specific recommendation is safe, or clinical approval has
occurred. Clinical/safety adjudication and final delivery approval remain
outside this task entirely.

## Interfaces

- **`ValidationInput`** — `candidate_response` (required — a missing
  candidate is an *input* problem, section 8.1, not a *malformed
  candidate* problem, section 8.4), `rtep` (`RuntimeEvidencePackage | None`
  — `None` means no authoritative evidence context was supplied),
  `validation_policy_version` (required, non-blank).
- **`ValidationResult`** — `outcome`, `validation_id`/`validation_timestamp`
  (generated at validation time, the same "legitimately runtime-generated
  identity/timestamp" pattern established in every prior boundary),
  `validation_policy_version` (echoed from the input, for traceability),
  `findings` (a tuple of short reason strings), plus traceability
  identifiers (`candidate_response_id`, `integration_id`, `retrieval_id`,
  `navigation_context_id`, `evidence_package_id`) sourced from
  `candidate_response` — never fabricated when absent.
- **`CandidateValidationOutcome`** — `VALID` / `SAFE_FALLBACK` /
  `INVALID_VALIDATION_INPUT` / `MISSING_EVIDENCE` / `INSUFFICIENT_EVIDENCE`
  / `INVALID_CANDIDATE` / `VALIDATION_FAILURE`. See "Outcome vocabulary"
  below for why this is a distinct class from `models/output_contract.py`'s
  `ValidationOutcome`, and why it deliberately shares `SAFE_FALLBACK` with
  it while staying disjoint from every upstream pipeline outcome.
- **`validate_candidate_response(validation_input)`** — the one explicit,
  deterministic entry point (spec section 16).

## Outcome vocabulary

`CandidateValidationOutcome` is a new class, not a reuse of
`models/output_contract.py`'s `ValidationOutcome` (Task #002's
forward-looking OUTPUT_CONTRACT.md placeholder, `PASS`/`FAIL`/`SAFE_FALLBACK`)
— reusing that class name for this narrower, CandidateResponse-specific
vocabulary would shadow/confuse two distinct types across the codebase.

Spec section 7 requires disjointness from `RetrievalOutcome`,
`RTEPAssemblyOutcome`, `RuntimeIntegrationOutcome`, and `GenerationOutcome`
— but **not** from `ValidationOutcome`. That omission is intentional:
section 7 also requires the vocabulary to include `SAFE_FALLBACK`, the same
literal value `ValidationOutcome.SAFE_FALLBACK` already uses. This is the
one deliberate, spec-mandated exception to the "every layer's vocabulary is
fully disjoint from every other" convention every prior boundary follows —
tested explicitly by
`test_candidate_validation_outcome_shares_only_safe_fallback_with_validation_outcome`.

`INVALID_VALIDATION_INPUT` is spelled this way, not the spec's illustrative
bare `INVALID_INPUT`, because `RuntimeIntegrationOutcome` already has a
member literally named `INVALID_INPUT` — reusing it would be exactly the
"upstream enum literal collision" section 7 prohibits.

There is no bare `INVALID` member. Section 9's own failure-precedence list
never uses one — only the five specific values plus `VALID`/`SAFE_FALLBACK`.
Section 7's "VALID / INVALID / SAFE_FALLBACK minimum semantic vocabulary"
is satisfied by `VALID`/`SAFE_FALLBACK` as concrete successes and the five
specific failure values collectively representing every concrete "not
valid" reason — the same no-generic-catch-all pattern
`GenerationOutcome`/`RTEPAssemblyOutcome` already use.

## Decision logic (deterministic precedence, spec section 9)

1. `validation_input is None`, or (defensive-only, unreachable via the
   typed API) `validation_input.candidate_response is None` →
   `INVALID_VALIDATION_INPUT`.
2. `validation_input.rtep is None` → `MISSING_EVIDENCE`.
3. `candidate_response.evidence_state is HAS_EVIDENCE` but the RTEP has
   zero evidence items (a genuine input inconsistency, not a graduated
   sufficiency judgment) → `INSUFFICIENT_EVIDENCE`.
4. (defensive-only, unreachable via the typed API) `candidate_response.content`
   is blank → `INVALID_CANDIDATE`.
5. An unexpected exception anywhere in evaluation → `VALIDATION_FAILURE`
   (never silently converted to `VALID`).
6. `candidate_response.evidence_state is EMPTY` → `SAFE_FALLBACK`: this
   recognizes and passes through Generation's own locked EMPTY_EVIDENCE
   policy response (see `generation/README.md`'s "Locked EMPTY_EVIDENCE
   policy") as the safe fallback it already is. Validation does not
   re-adjudicate it or generate a clinical alternative (spec section 8.7).
7. Otherwise → `VALID`.

No step here inspects the *content* of `candidate_response.content` for
factual/citation correctness, clinical appropriateness, or safety — only
structural presence and the `evidence_state` signal Generation already
established. That is a deliberate scope boundary, not an oversight (spec
sections 3.3/15).

## Evidence-support boundary

When evaluating evidence sufficiency, Validation only ever inspects the
`RuntimeEvidencePackage` already supplied on `ValidationInput.rtep` — it
never retrieves additional evidence, reranks, deduplicates, or repairs
provenance (spec section 14). `rtep.evidence`'s ordering and every
`EvidenceItem`'s provenance are read, never modified.

## Immutability

Validation never mutates `CandidateResponse`, `RTEP`, `EvidenceItem`,
provenance, or generation/integration metadata — every one of those is
already an immutable (frozen) object from Tasks #005-#007; Validation only
reads them and constructs a brand-new `ValidationResult`.

## Not implemented by this task (deferred / out of scope)

- Clinical reasoning, diagnosis, treatment recommendation, patient-specific
  clinical safety adjudication, final clinical approval, human approval
  workflow.
- Factual/citation verification, hallucination detection, LLM-judge-based
  evaluation.
- Response regeneration, provider retry/switching.
- Deployment, monitoring, UI, production safety infrastructure.
- A concrete downstream `FinalResponse`/delivery type — `ValidationResult`
  is not converted into one here (spec section 6).
