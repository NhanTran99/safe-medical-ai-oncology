# Generation Boundary (Task #007)

## What this is

The controlled boundary between the immutable `GenerationContext`
(Task #006) and downstream Validation (not yet implemented), per the
locked architecture:

```text
Repository
  ↓
Retrieval
  ↓
Runtime Evidence Package
  ↓
Runtime Integration
  ↓
GenerationContext
  ↓
Generation                        (this module)
  ↓
CandidateResponse
  ↓
Validation (future/downstream)
```

Generation is **not** Validation, clinical/safety adjudication, retrieval,
or final response approval. A `CandidateResponse` is never labeled final,
clinically validated, safety approved, or citation verified.

## Interfaces

- **`GenerationOutcome`** — `GENERATED` / `EMPTY_EVIDENCE_RESPONSE` /
  `INVALID_CONTEXT` / `CONTEXT_MISSING_RTEP` / `PROVIDER_FAILURE` /
  `PROVIDER_TIMEOUT` / `MALFORMED_PROVIDER_OUTPUT` / `PARTIAL_GENERATION` /
  `INTERNAL_FAILURE`. A distinct vocabulary from `RetrievalOutcome`,
  `RTEPAssemblyOutcome`, `RuntimeIntegrationOutcome`, and OUTPUT_CONTRACT's
  `ValidationOutcome` — deliberately spelled differently from
  `RuntimeIntegrationOutcome.EMPTY_EVIDENCE`/`.MISSING_RTEP` even though
  they describe related upstream states, so no two layers ever share a
  literal outcome name.
- **`CandidateResponse`** — `candidate_response_id`, `generation_timestamp`
  (both generated at creation, the same "legitimately runtime-generated
  identity/timestamp" pattern established in Tasks #005/#006), `content`,
  `evidence_state` (carried from `GenerationContext`), `provider_name`
  (`None` for the policy branch), plus traceability identifiers
  (`integration_id`, `retrieval_id`, `navigation_context_id`,
  `evidence_package_id`) sourced from the upstream context/RTEP — never the
  full context/RTEP/evidence objects re-embedded.
- **`GenerationResult`** — the atomic result: `outcome`, `response`
  (`None` unless `outcome` is `GENERATED` or `EMPTY_EVIDENCE_RESPONSE`),
  `message`.
- **`ProviderGenerationRequest`** — the typed, locked contract passed to the
  provider: `request_text`, `navigation_context`, `evidence`
  (`tuple[EvidenceItem, ...]`, the exact `context.rtep.evidence` — the
  authoritative governed evidence), `evidence_metadata`
  (`context.rtep.metadata`), `runtime_constraints`. See "Provider boundary"
  below.
- **`generate_candidate_response(context, provider)`** — the one explicit,
  deterministic entry point (spec section 5). `provider` is an `LLMAdapter`
  (Task #002's existing provider-agnostic interface — reused, not
  reinvented, per the handoff's "reuse existing types" instruction).
- **`ProviderError`** / **`ProviderTimeoutError`** / **`ProviderPartialOutputError`**
  — the typed exceptions a concrete `LLMAdapter` implementation raises to
  signal the corresponding `GenerationOutcome`. No concrete provider
  implementation exists in this module (spec section 7): production
  provider selection/credentials/endpoints remain deferred.
- **`EMPTY_EVIDENCE_POLICY_RESPONSE_TEXT`** — the locked policy response
  text. See "Locked EMPTY_EVIDENCE policy" below.

## Locked EMPTY_EVIDENCE policy

Status: **LOCKED**. This is a governed policy decision, not an
implementation detail left to per-call discretion.

When `context.evidence_state is EvidenceState.EMPTY`:

1. **No provider is called.** The provider never sees this request at all.
2. **`CandidateResponse.content` is exactly `EMPTY_EVIDENCE_POLICY_RESPONSE_TEXT`**
   (exported from `safe_medical_ai.generation`), a fixed constant string —
   never model-generated, never templated per-request, never varied by
   `request_text`.
3. **`CandidateResponse.provider_name` is `None`** and
   `GenerationResult.outcome` is `EMPTY_EVIDENCE_RESPONSE`, distinguishing
   this from a real, evidence-backed `GENERATED` response.
4. `test_empty_evidence_produces_fixed_policy_response_without_calling_provider`
   proves the provider is never invoked (an exploding fake provider that
   raises if called), and
   `test_empty_evidence_policy_response_content_is_deterministic_across_calls`
   proves the text is identical across repeated calls.

Rationale (spec section 6): "Do not convert EMPTY into technical failure"
(the same principle Tasks #005/#006 already applied to
`RTEPAssemblyOutcome`/`RuntimeIntegrationOutcome`) — an empty-evidence
`GenerationContext` is a legitimate, valid state, not an error, so a
`CandidateResponse` is still produced. But Generation must not silently
answer an unsupported clinical question from model knowledge, so the
*only* implemented behavior for this branch is the one fixed policy
response above — no graduated evidence-sufficiency adjudication is
implemented or should be added without a separate, explicit governance
decision.

**Changing `EMPTY_EVIDENCE_POLICY_RESPONSE_TEXT` is a policy change**, not
a routine code edit, and requires the same governance approval as any
other locked B1-B4 decision.

## Why `CONTEXT_MISSING_RTEP` has no organic trigger through the typed API

`GenerationContext.rtep` is a required (non-`Optional`) field — Runtime
Integration only ever produces a `GenerationContext` when an RTEP is
present (an integration result with a missing RTEP is `MISSING_RTEP` at
*that* layer, with `context=None`, never a `GenerationContext`). The
`context.rtep is None` check in `generate_candidate_response` is therefore
a defensive completeness measure, not a normally reachable path. It is
tested via `GenerationContext.model_construct(...)` (Pydantic's
validation-bypass constructor) rather than any input a typed caller could
produce — see `test_generation.py`.

## Provider boundary

`generate_candidate_response` depends only on the abstract `LLMAdapter`
interface (`llm/base.py`), never a concrete vendor SDK, endpoint, or
credential. `provider.generate(request=provider_request)` is the only call
made, where `provider_request` is a `ProviderGenerationRequest` carrying:

- `request_text` — the user request/intent;
- `evidence` — the *exact* `context.rtep.evidence` tuple: the authoritative
  governed `EvidenceItem`s (with their provenance), referenced unchanged,
  in the exact order Retrieval/RTEP Assembly already produced them — never
  reranked, reordered, deduplicated, or repaired;
- `evidence_metadata` — the *exact* `context.rtep.metadata` object;
- `navigation_context`, `runtime_constraints` — carried through unchanged.

This is the fix for a reviewed architectural blocker: an earlier version of
this module called `provider.generate(prompt=context.request_text)` alone,
which did not actually supply the governed evidence to Generation. A
provider now always receives the full governed evidence structure (not its
clinical text content, which `EvidenceItem` does not carry yet — see
`evidence/README.md`'s deferred-items list — but its identity, provenance,
and ordering) alongside the request text, whenever `evidence_state` is
`HAS_EVIDENCE`. Nothing is fabricated: constructing `ProviderGenerationRequest`
is pure data assembly (referencing existing immutable objects), not a new
retrieval, ranking, or evidence-construction layer.
`test_provider_receives_authoritative_rtep_evidence` and
`test_provider_receives_evidence_in_original_order_without_reranking` prove
this end-to-end. A minimal fake provider used for tests (`FakeLLMAdapter`
and friends) lives entirely inside `test_generation.py`; no test-only or
placeholder provider configuration is shipped in this module.

## Assembly semantics

| `context` | `.rtep` | `.evidence_state` | provider call | Result |
|---|---|---|---|---|
| `None` | — | — | no | `INVALID_CONTEXT`, no response |
| present | `None` (defensive-only) | — | no | `CONTEXT_MISSING_RTEP`, no response |
| present | present | `EMPTY` | no | `EMPTY_EVIDENCE_RESPONSE`, fixed policy response |
| present | present | `HAS_EVIDENCE` | yes, raises `ProviderTimeoutError` | `PROVIDER_TIMEOUT`, no response |
| present | present | `HAS_EVIDENCE` | yes, raises `ProviderPartialOutputError` | `PARTIAL_GENERATION`, no response |
| present | present | `HAS_EVIDENCE` | yes, raises `ProviderError` (other) | `PROVIDER_FAILURE`, no response |
| present | present | `HAS_EVIDENCE` | yes, raises any other exception | `INTERNAL_FAILURE`, no response |
| present | present | `HAS_EVIDENCE` | yes, returns non-`str`/blank | `MALFORMED_PROVIDER_OUTPUT`, no response |
| present | present | `HAS_EVIDENCE` | yes, returns non-blank `str` | `GENERATED`, complete response |

Generation never mutates `GenerationContext`, its RTEP, evidence items,
provenance, runtime metadata, or Navigation Context — every one of those
is already an immutable (frozen) object from Tasks #005/#006; Generation
only ever reads them and constructs a brand-new `CandidateResponse`.

## Not implemented by this task (deferred / out of scope)

- Validation, clinical/safety adjudication, final response approval,
  citation/factual verification, hallucination detection.
- Any concrete `LLMAdapter` provider implementation, credentials, endpoint,
  or production model/vendor selection.
- Real prompt construction from evidence content (`PROMPTING_STRATEGY.md`)
  — `EvidenceItem` carries no clinical text to build a richer prompt from
  yet (same deferred item `evidence/README.md` already lists).
- Reranking, deduplication, provenance repair, re-retrieval, embeddings,
  vector search, external web search, autonomous/multi-agent orchestration.
