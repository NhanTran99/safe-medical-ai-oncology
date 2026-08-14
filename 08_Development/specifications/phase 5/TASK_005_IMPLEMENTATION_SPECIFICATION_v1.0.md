# TASK #005 — IMPLEMENTATION SPECIFICATION v1.0

Status: **APPROVED — READY FOR CLAUDE IMPLEMENTATION**

Project:
Safe Medical AI Oncology

Phase:
Phase 5 — System Implementation & Validation

Task:
#005 — Runtime Evidence Package Boundary / Assembly

Current authoritative branch:

`phase5/task002-scaffolding`

Current remote HEAD:

`c28b498b6f13066253940291bdcbc6ed3f2f4e2c`

Main:

`71e84f3514d35d76c53a36b48d7a14220c4d633e`

---

# 1. Objective

Implement the controlled transformation:

**Retrieval Result → Runtime Evidence Package**

The implementation must establish a deterministic, typed, traceable and
immutable Runtime Evidence Package boundary between the existing Retrieval
Layer and future Generation Layer.

Task #005 does NOT implement Generation.

---

# 2. Locked Architecture

```text
Navigation Context
        ↓
Retrieval Layer
        ↓
Retrieval Result
        ↓
RTEP Assembly
        ↓
Immutable Runtime Evidence Package
        ↓
Generation
```

Task #005 owns only the RTEP boundary.

`RetrievalResponse` and `RuntimeEvidencePackage` are distinct contracts.

---

# 3. Authoritative Inputs

Claude must treat these as locked sources of truth:

1. `TECH_STACK.md` — IR12
2. `OUTPUT_CONTRACT.md` — IR13
3. Formal Retrieval Ready Assessment
4. `EVIDENCE_PACKAGE_SPECIFICATION.md` v1.1
5. `RETRIEVAL_POLICY.md`
6. `RAG_ARCHITECTURE.md` v1.1
7. `RESPONSE_GENERATION_ARCHITECTURE.md` v1.1
8. `OUTPUT_VALIDATION_FRAMEWORK.md`
9. `Phase_5_Governance_Consolidated_Decision_Record.md` v6.0
10. `PHASE_5_IMPLEMENTATION_READINESS_DECISION_RECORD.md` v6.0
11. current implementation under `08_Development/`
12. this Task #005 specification

If implementation convenience conflicts with a locked specification, the locked
specification wins. Do not silently reinterpret governance.

---

# 4. Implementation Scope

Authorized area:

`08_Development/**`

The implementation should introduce a clearly isolated RTEP contract/assembly
surface within the existing implementation package.

Exact filename is not governance-locked. Follow existing package conventions.

Do not modify governed architecture/governance/clinical documents as part of
the implementation.

---

# 5. RTEP Contract

## 5.1 Logical structure

```text
Runtime Evidence Package
├── Evidence Content
└── Evidence Metadata
```

## 5.2 Minimum Evidence Metadata

The implementation must represent:

- `evidence_package_id`
- `retrieval_id`
- `navigation_context_id`
- `retrieval_policy_version`
- `knowledge_base_version`
- `generation_timestamp`

## 5.3 Evidence Item provenance

Each evidence item must preserve:

- `knowledge_object_id`
- `knowledge_passport_id`
- `source_id`
- `guideline_version`

## 5.4 Evidence content

Evidence Content represents retrieved Clinical Knowledge Objects.

Do not add:

- prompt instructions;
- prompt templates;
- model directives;
- generated response;
- model-generated clinical interpretation;
- clinical reasoning.

## 5.5 Primary vs Runtime Evidence Package

Do not confuse:

Primary Evidence Package:
governed Population Package artifact.

Runtime Evidence Package:
runtime representation supplied downstream to Generation.

They have different lifecycle roles.

---

# 6. Type System

Use the locked Phase 5 stack:

- Python 3.12
- Pydantic 2.x
- pytest

Canonical RTEP representation must be typed and contract-validated.

An untyped `dict[str, Any]` is not the authoritative RTEP model.

Exact API/JSON serialization is not required by this task unless already naturally
supported by the implementation; do not invent a public API contract.

---

# 7. Assembly Boundary

Implement one explicit, testable assembly boundary.

Conceptually:

```text
RetrievalResponse
        +
required runtime metadata
        ↓
RTEP Assembly
        ↓
RuntimeEvidencePackage
```

Requirements:

- accepts completed retrieval output;
- does not call RepositorySource;
- does not call RetrievalService again;
- does not re-retrieve;
- does not rerank;
- does not reorder;
- does not heuristically deduplicate;
- does not repair missing provenance;
- does not enrich clinical content;
- does not call an LLM;
- does not generate prompts;
- does not generate responses.

---

# 8. Assembly Semantics

## 8.1 Successful assembly

A successful assembly must produce:

**one complete, contract-valid, immutable RTEP.**

Partial/best-effort RTEP is not a successful assembly.

## 8.2 EMPTY

`EMPTY` is a valid retrieval state.

It must produce:

**an empty-but-valid RTEP**

with valid required metadata.

Evidence-insufficiency handling belongs downstream.

## 8.3 NOT_FOUND

`NOT_FOUND` produces:

**no RTEP**

and propagates the deterministic retrieval outcome.

## 8.4 INVALID_REQUEST

`INVALID_REQUEST` produces:

**no RTEP**

and is propagated unchanged.

## 8.5 Ambiguous retrieval

Ambiguity is not resolved heuristically.

Result:

**no RTEP / deterministic assembly failure.**

## 8.6 Malformed or incomplete evidence

If a required evidence candidate cannot satisfy the RTEP contract:

**atomic assembly failure**

Do not silently drop the candidate.

## 8.7 Missing metadata/provenance

Required metadata/provenance must not be replaced by invented placeholders.

Result:

**assembly failure.**

---

# 9. Atomicity

Assembly is atomic:

```text
success → exactly one complete RTEP
failure  → zero RTEP
```

Do not implement partial RTEP.

---

# 10. Determinism

Given the same valid RetrievalResponse and equivalent runtime metadata,
assembly must produce semantically identical:

- evidence content;
- evidence ordering;
- provenance;
- metadata,

apart from legitimately runtime-generated identity/timestamp fields.

No randomization or model-assisted transformation.

---

# 11. Ordering

Preserve the exact sequence returned by Retrieval Layer.

Example:

```text
RetrievalResponse:
A → B → C

RTEP:
A → B → C
```

Do not:

- sort;
- rerank;
- deduplicate heuristically;
- reorder by clinical intuition.

Ordering must be explicitly tested.

---

# 12. Immutability

After assembly:

**RTEP is immutable.**

Implementation must prevent mutation of the package and its nested contract
objects to the extent required by the chosen typed model.

Behavioral tests must verify:

1. direct mutation is rejected;
2. post-assembly mutation of source structures cannot silently mutate the
   already-created RTEP.

---

# 13. Provenance

Provenance must preserve actual values, not merely field presence.

Test value preservation for:

- knowledge object ID;
- knowledge passport ID;
- source ID;
- guideline version.

Do not synthesize missing provenance.

---

# 14. Failure Taxonomy

Retrieval-originated outcomes remain distinct:

- `INVALID_REQUEST`
- `NOT_FOUND`
- `EMPTY`
- `AMBIGUOUS` where applicable

Assembly-originated failures may use a small internal taxonomy such as:

- invalid retrieval response;
- missing required metadata;
- invalid evidence item;
- incomplete provenance;
- assembly contract violation.

Do not use downstream output outcomes:

- `PASS`
- `FAIL`
- `SAFE_FALLBACK`

as RTEP assembly statuses.

Those belong to the governed output/validation layer.

---

# 15. Traceability / Logging

Assembly failures should remain traceable using available runtime identifiers,
including where available:

- trace ID;
- retrieval ID;
- navigation context ID;
- assembly failure category.

Do not log unnecessary clinical evidence content.

Use existing structured logging / trace-ID foundations.

---

# 16. Compatibility Requirements

The implementation must preserve:

- existing `RetrievalRequest`;
- existing `RetrievalCandidate`;
- existing `RetrievalResponse`;
- existing `RetrievalService`;
- existing `RepositorySource`;
- existing `FilesystemRepositorySource`;
- existing Task #002–#004 behavior.

Task #005 is additive.

Do not redefine existing retrieval semantics.

---

# 17. Tests

All existing tests must continue to pass.

Add tests for:

### Contract

- valid RTEP construction;
- required metadata;
- required provenance;
- invalid/missing fields;
- immutability.

### Successful assembly

- valid RetrievalResponse → valid RTEP;
- evidence content preserved;
- metadata preserved;
- provenance preserved;
- ordering preserved.

### EMPTY

- EMPTY retrieval → valid empty RTEP.

### Retrieval failures

- INVALID_REQUEST → no RTEP;
- NOT_FOUND → no RTEP;
- ambiguous result → no RTEP / deterministic failure.

### Assembly failures

- malformed candidate;
- incomplete provenance;
- missing required metadata;
- contract violation.

### Boundary

Verify Task #005 does not:

- re-retrieve;
- access repository directly;
- rerank;
- reorder;
- heuristically deduplicate;
- repair missing provenance;
- call LLM;
- generate prompts;
- generate responses;
- implement clinical reasoning;
- implement output validation.

---

# 18. Acceptance Criteria

Task #005 implementation is acceptable only when all are true:

1. RTEP typed contract implemented.
2. RTEP metadata implemented.
3. Evidence provenance implemented.
4. RTEP assembly boundary implemented.
5. EMPTY semantics implemented.
6. NOT_FOUND / INVALID_REQUEST semantics preserved.
7. Ambiguity handled deterministically.
8. Atomicity implemented.
9. Ordering preserved.
10. Immutability implemented and tested.
11. Provenance values preserved and tested.
12. Existing Task #002–#004 tests pass.
13. New Task #005 tests pass.
14. `uv sync --extra dev` passes.
15. `git diff --check` passes.
16. Only authorized implementation scope is changed.
17. No prohibited functionality is introduced.
18. No Gold/governance/architecture/status material is modified.
19. No tag/release is created.
20. Task #005 PASS is interpreted only as RTEP-boundary readiness.

Task #005 PASS does NOT mean:

- Generation Ready;
- Validation Ready;
- Clinical/Safety Ready;
- Deployment Ready.

---

# 19. Automatic Rejection Conditions

Reject the patch if it introduces any of:

- LLM invocation;
- embedding generation;
- vector database;
- semantic retrieval;
- prompt generation;
- response generation;
- clinical reasoning;
- output validation;
- autonomous repository-wide indexing;
- silent provenance repair;
- heuristic reranking;
- generation fallback;
- unauthorized governance/clinical document changes;
- unauthorized Git history changes.

---

# 20. Git / Commit Boundary

Claude should:

- inspect;
- implement;
- test;
- export patch;
- report exact changed files;
- report test results;
- report diff summary.

Claude should NOT commit/push unless a separate explicit commit/push instruction
is provided.

Controlled closeout remains:

```text
Claude implementation
→ patch export
→ ChatGPT review
→ VS Code apply
→ tests
→ explicit staging
→ staged diff review
→ controlled commit
→ push
→ remote verify
```

Never use `git add .`.

---

# 21. Required Claude Final Report

Claude must return:

1. implementation summary;
2. exact changed file list;
3. exact new/modified tests;
4. test command(s);
5. complete test result;
6. `git diff --check` result;
7. confirmation that only `08_Development/**` changed;
8. confirmation that no prohibited scope was introduced;
9. patch/export location;
10. any blocker or ambiguity requiring governance decision.

Do not claim task closure or remote verification unless actually performed.

---

# 22. Task #005 Completion Definition

Task #005 is:

**IMPLEMENTATION COMPLETE — PENDING CHATGPT REVIEW**

only after Claude has produced the implementation and patch/test report.

It becomes:

**CLOSED / PASS**

only after:

- ChatGPT implementation review PASS;
- VS Code patch application;
- full tests PASS;
- controlled staging/diff review PASS;
- controlled commit;
- push;
- remote verification.

---

# 23. Locked Decision Provenance

This specification implements the decisions approved through:

- Task #005 Architecture/Scope Gate;
- B1 — Scope & Architecture Boundary;
- B2 — Runtime Evidence Package Contract;
- B3 — Assembly + Failure Semantics;
- B4 — Implementation Surface + Tests + Acceptance.

IR recording:

- IR20 — B1
- IR21 — B2
- IR22 — B3
- IR23 — B4

Governance consolidation:

`Phase_5_Governance_Consolidated_Decision_Record.md` v6.0

---

# 24. End State Before Implementation

Current:

**Task #005 SPECIFICATION COMPLETE / APPROVED**

Next:

**Claude implementation → patch export**

No Task #005 implementation commit exists yet.
