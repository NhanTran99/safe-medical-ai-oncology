# TASK #006 IMPLEMENTATION SPECIFICATION v1.0

**Title:** Runtime Integration / Generation Context Boundary
**Phase:** Phase 5 — System Implementation & Validation
**Status:** READY FOR CLAUDE HANDOFF after governance approval
**Scope source:** Task #006 B1–B4 locked decision set

---

# 1. Objective

Implement the Runtime Integration layer that consumes an immutable Runtime Evidence Package and explicit runtime inputs, then produces a typed GenerationContext suitable for the downstream Generation layer.

This task does **not** implement Generation, LLM invocation, Validation, clinical reasoning, safety adjudication, or deployment.

---

# 2. Locked Architecture

```text
Request / Intent ───────┐
Navigation Context ─────┤
RTEP (immutable) ───────┤
Runtime Constraints ────┘
          ↓
Runtime Integration
          ↓
GenerationContext
          ↓
[Generation — future task]
          ↓
Candidate Response
          ↓
Validation
```

Dependency direction:

`integration → evidence → retrieval contracts`

No reverse dependency.

---

# 3. Authorized Implementation Surface

Create only within:

```text
08_Development/implementation/src/safe_medical_ai/integration/
    __init__.py
    models.py
    integration.py
    README.md

08_Development/implementation/tests/
    test_integration_models.py
    test_integration.py
```

A minimal update to:

```text
08_Development/implementation/README.md
```

is allowed to document the new module.

Do not modify retrieval/evidence contracts unless a genuine blocker is discovered and explicitly escalated.

Do not modify Gold, governance, project-management or clinical knowledge materials.

---

# 4. Required Typed Contracts

## 4.1 RuntimeIntegrationInput

Must explicitly contain:

- request / intent;
- Navigation Context;
- Runtime Evidence Package;
- applicable Runtime Constraints.

Use the existing project contract conventions. Do not invent external schemas when an existing locked model can be reused.

## 4.2 GenerationContext

Must preserve or reference:

- request / intent;
- Navigation Context;
- RTEP;
- runtime constraints;
- explicit evidence state;
- traceability identifiers.

GenerationContext is a derived orchestration/context object, not a second evidence authority.

## 4.3 RuntimeIntegrationOutcome

Minimum controlled states:

- `INTEGRATED`
- `EMPTY_EVIDENCE`
- `INVALID_INPUT`
- `MISSING_RTEP`
- `INTEGRATION_FAILURE`

Use the existing project naming conventions where compatible.

## 4.4 RuntimeIntegrationResult

Must be typed and atomic enough that a successful `INTEGRATED` result contains a valid GenerationContext and failure outcomes do not silently contain a partially valid context.

---

# 5. Integration API

Provide one explicit deterministic entry point, e.g.:

`integrate_runtime_context(...)`

or an equivalent typed service method.

Requirements:

- explicit inputs;
- typed output;
- no hidden global state;
- no filesystem access;
- no repository access;
- no retrieval calls;
- no LLM calls.

---

# 6. Behavioral Requirements

## 6.1 Valid RTEP

Valid RTEP + valid required context:

→ `INTEGRATED` + valid GenerationContext.

## 6.2 EMPTY RTEP

Valid EMPTY RTEP:

→ `EMPTY_EVIDENCE` + explicit empty evidence state.

Do not convert EMPTY into technical failure.

Do not infer permission to answer without evidence.

## 6.3 Missing RTEP

Missing RTEP:

→ `MISSING_RTEP`.

Do not retrieve again.

## 6.4 Invalid input

Invalid required input:

→ `INVALID_INPUT`.

## 6.5 Integration failure

Unexpected deterministic inability to construct a valid GenerationContext:

→ `INTEGRATION_FAILURE`.

Do not return a partially valid GenerationContext as success.

---

# 7. Preservation Invariants

The implementation must preserve:

- RTEP immutability;
- evidence ordering;
- per-item provenance;
- RTEP metadata;
- retrieval traceability;
- Navigation Context relationship;
- runtime constraints.

No reranking, reordering, deduplication, enrichment or provenance repair.

---

# 8. Determinism

For the same logical RuntimeIntegrationInput, the logical GenerationContext must be identical.

Do not introduce random evidence selection or hidden external state.

Runtime observability IDs/timestamps, if required by existing conventions, must not alter logical evidence/context content.

---

# 9. Explicitly Prohibited Functionality

The implementation MUST NOT contain:

- `RepositorySource` access;
- filesystem repository access;
- `RetrievalService` calls;
- `.retrieve(...)`;
- semantic/vector retrieval;
- re-retrieval;
- evidence reconstruction;
- provenance synthesis/repair;
- reranking;
- heuristic deduplication;
- LLM/provider SDK invocation;
- prompt generation;
- response generation;
- output validation;
- clinical reasoning;
- clinical/safety adjudication;
- autonomous fallback retrieval.

Static architectural tests should enforce the highest-value prohibitions.

---

# 10. Tests Required

At minimum:

### Contract/model tests
- required fields;
- controlled outcome vocabulary;
- invalid/blank required inputs;
- immutability;
- typed result semantics.

### Integration tests
- valid RTEP;
- EMPTY RTEP;
- missing RTEP;
- invalid input;
- integration failure;
- preservation of evidence;
- preservation of ordering;
- preservation of provenance;
- preservation of metadata/traceability;
- runtime constraints preservation.

### Immutability tests
- source RTEP cannot be mutated through integration;
- nested evidence/provenance does not leak mutable state.

### Determinism tests
- repeated calls with equivalent logical input produce equivalent logical output.

### Architectural boundary tests
Static or behavioral checks proving no:
- repository access;
- retrieval calls;
- filesystem access;
- LLM/vector dependency;
- generation/validation logic.

### Regression
Run the complete existing suite under:

```bash
uv sync --extra dev
uv run pytest 08_Development/implementation/tests -v
```

All pre-existing tests must remain green.

---

# 11. Acceptance Criteria

Task #006 implementation is PASS only if:

1. All locked B1–B4 decisions are implemented.
2. Runtime Integration is isolated in `integration/`.
3. Existing retrieval/evidence contracts remain intact.
4. RTEP remains authoritative and immutable.
5. EMPTY, missing and invalid states are distinguishable.
6. Provenance/order/traceability are preserved.
7. No prohibited functionality exists.
8. New tests cover all required categories.
9. Full regression passes.
10. `git diff --check` passes.
11. All changes remain inside the authorized implementation scope.
12. No commit/push is claimed by Claude unless explicitly requested by the controlled Git workflow.

---

# 12. Claude Git Boundary

Claude should:

- inspect the authoritative baseline;
- implement only the specification;
- run tests;
- export a working-tree patch;
- report changed files, tests, diff-check and scope.

Claude must **not**:

- commit;
- push;
- modify governance records;
- modify Gold materials;
- expand scope;
- silently reinterpret B1–B4.

---

# 13. Review / Handoff Protocol

After Claude implementation:

1. ChatGPT reviews implementation summary.
2. Resolve genuine blockers/CRs.
3. Claude exports final patch.
4. User applies patch in VS Code.
5. Full verification is run.
6. Controlled staging.
7. ChatGPT reviews staged diff.
8. Controlled commit.
9. Push.
10. Remote SHA verification.
11. Task closeout.

No direct implementation-to-commit shortcut.

---

# 14. Definition of Done

**TASK #006 IMPLEMENTATION PASS** means:

`RTEP → Runtime Integration → GenerationContext`

is implemented, tested and verified.

It does **not** mean:

- Generation implemented;
- LLM integration implemented;
- Validation implemented;
- Clinical/safety approval achieved;
- deployment ready.

---

# 15. Claude Handoff Opening

Use the following opening when handing this specification to Claude:

> You are implementing Task #006 of Phase 5.
>
> The Task #006 Architecture / Scope Gate is complete and B1–B4 are LOCKED.
>
> Implement only `TASK_006_IMPLEMENTATION_SPECIFICATION_v1.0.md`.
>
> Do not reopen B1–B4 unless you identify a genuine implementation blocker that makes the locked specification internally inconsistent with the existing codebase.
>
> First inspect the authoritative baseline and the existing `retrieval/` and `evidence/` contracts. Then implement the isolated `integration/` layer, tests, and minimal README update exactly within the authorized surface.
>
> Do not commit or push. Export a working-tree patch and report verification results for ChatGPT review.
