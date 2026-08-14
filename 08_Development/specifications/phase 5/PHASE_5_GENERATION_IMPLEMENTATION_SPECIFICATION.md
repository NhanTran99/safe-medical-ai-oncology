# PHASE 5 — GENERATION IMPLEMENTATION SPECIFICATION

Status: **APPROVED SPECIFICATION — READY FOR CLAUDE IMPLEMENTATION**

## 1. Purpose

Implement the controlled Generation boundary downstream of Runtime Integration.

The implementation must transform an authoritative `GenerationContext` into a
typed `CandidateResponse` or an explicit typed generation failure.

Generation is not Validation, clinical/safety adjudication, retrieval, or final
response approval.

## 2. Locked Architectural Boundary

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
Generation
  ↓
CandidateResponse
  ↓
Validation (future/downstream)
```

Generation must not cross upstream or downstream boundaries.

## 3. Authorized Scope

Create an isolated:

```text
08_Development/implementation/src/safe_medical_ai/generation/
```

with package/module structure following existing project conventions.

Expected surface:

- `__init__.py`
- `models.py`
- `generation.py`
- `README.md`

Tests:

- `08_Development/implementation/tests/test_generation_models.py`
- `08_Development/implementation/tests/test_generation.py`

Exact filenames may follow existing conventions only if they preserve the locked
surface; do not expand scope.

## 4. Input Contract

Generation accepts an authoritative `GenerationContext`.

It must preserve/access, as already supplied by Runtime Integration:

- request/intent;
- Navigation Context relationship;
- Runtime Evidence Package;
- explicit evidence state;
- runtime constraints;
- traceability/runtime identifiers.

Do not reconstruct or independently validate upstream RTEP.

Do not accept RepositorySource, RetrievalRequest, RetrievalResponse, raw Gold
artifacts, filesystem paths, or arbitrary evidence files as Generation inputs.

## 5. Output Contract

Primary successful output:

```text
CandidateResponse
```

Generation must never label its result as:

- final;
- clinically validated;
- safety approved;
- citation verified.

Use a typed `GenerationResult` with atomic semantics:

```text
success → CandidateResponse present
failure → CandidateResponse absent
```

Include sufficient generation/runtime trace metadata for downstream traceability.

## 6. Evidence Semantics

Evidence state is authoritative from GenerationContext.

At minimum preserve:

- evidence-present;
- empty-evidence;
- blocked/invalid.

For `EMPTY_EVIDENCE`, implement only the explicitly locked policy branch.
Do not silently answer unsupported clinical questions from model knowledge.

Do not invent a new evidence-sufficiency adjudication layer.

## 7. Provider Boundary

Define an explicit provider abstraction so Generation core is not vendor-coupled.

Provider-specific details remain deferred unless required to make the contract
testable. Do not hard-code credentials, production endpoints, or a production
model choice.

If a minimal fake/in-memory provider is needed for tests, keep it inside the
test boundary and do not introduce production provider configuration.

## 8. Failure Semantics

Implement typed outcomes for the locked B3 cases, at minimum:

- invalid/blocked context;
- missing RTEP;
- explicit EMPTY_EVIDENCE policy outcome;
- provider failure;
- timeout/unavailable provider;
- malformed provider output;
- partial/interrupted generation;
- controlled unexpected/internal failure.

Rules:

- no CandidateResponse on failure;
- no silent fallback;
- no hidden retrieval;
- no evidence fabrication;
- no silent output repair;
- failures retain required trace identity.

Keep generation failures distinct from retrieval, integration, and validation
outcomes.

## 9. Immutability and Traceability

Generation must not mutate:

- GenerationContext;
- RTEP;
- EvidenceItem;
- provenance;
- runtime metadata;
- Navigation Context.

Tests must prove no mutation/leak.

CandidateResponse must be a newly created output object.

Preserve the ability to trace a CandidateResponse back to its generation attempt
and upstream runtime evidence/context identifiers.

## 10. Explicit Prohibitions

The implementation must not introduce:

- RepositorySource access;
- filesystem access;
- RetrievalService calls;
- re-retrieval;
- reranking;
- evidence deduplication;
- provenance repair/fabrication;
- vector database;
- embeddings;
- semantic retrieval;
- external web search;
- autonomous agents;
- multi-agent orchestration;
- clinical reasoning engine;
- clinical decision-making;
- factual/citation validation;
- hallucination detection;
- safety adjudication;
- final response approval;
- Validation imports/calls.

## 11. Tests / Acceptance

Minimum tests must cover:

1. valid GenerationContext;
2. evidence-present generation;
3. EMPTY_EVIDENCE branch;
4. invalid/blocked context;
5. missing RTEP;
6. provider failure;
7. timeout/unavailable provider;
8. malformed provider output;
9. partial/interrupted generation;
10. atomic success/failure;
11. traceability;
12. immutability;
13. no retrieval;
14. no filesystem/repository access;
15. no Validation coupling;
16. no vector/embedding prohibited path;
17. deterministic orchestration behavior;
18. regression compatibility with Tasks #002–#006.

Run:

```bash
uv sync --extra dev
uv run pytest 08_Development/implementation/tests -v
git diff --check
```

Acceptance target:

- all existing tests pass;
- all new Generation tests pass;
- no prohibited architectural dependency;
- no scope outside `08_Development/**`.

## 12. Implementation / Git Boundary

Claude must:

1. inspect the current implementation and locked specifications;
2. implement only this specification;
3. run the complete test suite;
4. run diff/scope checks;
5. report exact changed files;
6. export a working-tree patch only;
7. not commit;
8. not push;
9. not modify governance/project-management/clinical materials.

Then:

```text
Claude patch
  ↓
ChatGPT review
  ↓
VS Code apply
  ↓
full verification
  ↓
controlled commit
  ↓
push
  ↓
remote verification
```

## 13. Claude Handoff Instructions

Tell Claude explicitly:

> Treat B1–B4 as LOCKED governance decisions. Do not reinterpret them.
> Inspect the current `retrieval/`, `evidence/`, and `integration/` contracts before
> writing code. Reuse existing types where appropriate. Do not invent upstream
> schemas. Implement only the Generation boundary specified here. Do not commit
> or push. Return the implementation summary, exact changed-file list, test
> results, diff-check/scope results, and an exportable patch.

## 14. Current Baseline

Authoritative branch:

`phase5/task002-scaffolding`

Current remote HEAD:

`91162133e9f0496e1c19ad7e09a82d1f592178e0`

Main:

`71e84f3514d35d76c53a36b48d7a14220c4d633e`

Do not reset/rebase/rename the branch.

## 15. Acceptance Gate

Generation is not considered implemented/closed until:

**implementation → ChatGPT review → VS Code apply → tests → controlled commit → push → remote verification**

has completed successfully.
