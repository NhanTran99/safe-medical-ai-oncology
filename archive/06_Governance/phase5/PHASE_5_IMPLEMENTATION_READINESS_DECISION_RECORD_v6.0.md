# PHASE 5 IMPLEMENTATION READINESS DECISION RECORD

Status: **LOCKED — consolidated through Task #005 specification B4 / approved IR23**

## Recording Rule

Update this record after every approved IR batch when that batch introduces a new locked decision.

Do not create one artifact per individual decision.

At governance milestone / package close / phase close / thread handover, this record must be reviewed so that the current Phase 5 implementation state, locked IR decisions, task closeouts, and authoritative commits remain synchronized.

---

# IR5 — Implementation Readiness Gate

- `TECH_STACK.md` must be authored/approved before retrieval/runtime implementation.
- `OUTPUT_CONTRACT.md` must be authored/approved before runtime/generation implementation.
- Retrieval Ready (RR-1…RR-5) requires an explicit assessment before retrieval implementation.
- Claude Code does not independently make governance, clinical, or safety decisions.
- Implementation scope must remain task-bounded and evidence-driven.

# IR6 — Phase 5 Execution Plan

Locked pipeline:

**readiness → retrieval → runtime integration → evidence/output validation → technical validation → clinical/safety validation → remediation → closure**

Task boundaries may be decomposed into sub-tasks when evidence requires it, without autonomous scope expansion.

# IR7 — Technology Stack

### Locked core stack

- Python 3.12
- FastAPI
- Pydantic 2.x
- pytest
- `uv` + `pyproject.toml`
- PostgreSQL as structured runtime storage direction
- Provider-agnostic LLM adapter
- Environment-variable configuration + `.env.example`
- Structured logging and trace IDs
- Implementation target: `08_Development/specifications/` and `08_Development/implementation/`

### Locked architecture principles

- Hybrid retrieval architecture.
- Navigation-first / hierarchical retrieval.
- Retrieval components behind abstractions.
- Runtime business logic separated from API layer.
- Testing from the beginning.

### Intentionally deferred

- Exact package patch/minor versions.
- Exact embedding model.
- Exact vector database/vector engine.
- Exact LLM provider/model.
- Detailed runtime schemas and implementation filenames.

# IR8 — Output Contract

`OUTPUT_CONTRACT.md` is the governed interface between response generation and output validation.

Locked principles:

- Required runtime inputs include user intent, Navigation Context, Runtime Evidence Package, applicable safety/governance context, and delivery constraints.
- Meaningful clinical factual claims require traceable evidence from the Runtime Evidence Package.
- Canonical output includes content, evidence/provenance references, safety/validation metadata, uncertainty/limitation state, and delivery status.
- Controlled outcomes: `PASS`, `FAIL`, `SAFE_FALLBACK`.
- Generation, validation, and final delivery decision remain separate.
- Exact implementation schema remains downstream and must remain consistent with the contract.

# IR9–IR11 — Retrieval Ready

- RR-1 Gold Integrity: **PASS**
- RR-2 Repository Verification: **PASS**
- RR-3 Registry Verification: **PASS**
- RR-4 Traceability: **PASS**
- RR-5 Required Integration Metadata: **PASS**
- Existing Population Integration Manifest + Knowledge Asset Registry provide the relevant integration metadata.
- Formal consolidated Retrieval Ready assessment was created.
- **RETRIEVAL READY = PASS**

This is a knowledge/repository readiness gate, not runtime, clinical/safety, or deployment validation.

# IR12 — TECH_STACK Artifact

`TECH_STACK.md` is locked as the controlled Phase 5 technology-stack specification.

The exact retrieval engine, embedding model, vector engine, LLM provider/model, detailed runtime database schema, and other implementation-specific vendor choices remain deferred until justified by implementation evidence/compatibility.

# IR13 — OUTPUT_CONTRACT Artifact

`OUTPUT_CONTRACT.md` is locked as the governed runtime output interface.

Runtime Evidence Package, generation, validation, safety/governance, and final decision remain separate controlled components.

# IR14 — Controlled Implementation Specification Bundle

- Phase 5 implementation specifications must be provided as a consistent controlled baseline before implementation tasks.
- Claude receives the authoritative handover plus relevant locked specifications/material map.
- Implementation tasks remain bounded by approved scope and file boundaries.

# IR15 — Claude Task #002 Specification

Task #002 was locked to implementation scaffolding only:

- `08_Development/**`
- `pyproject.toml`
- `uv.lock`
- `.env.example` when required.

Excluded retrieval, vector search, embeddings, LLM provider/model, response-generation business logic, clinical logic, output-validation business logic, UI/deployment, and changes to Gold/governance/architecture/status materials.

# IR16 — Repository Hygiene / Controlled Commit Gate

Locked closeout sequence:

**inventory → classify → canonical paths → explicit staging → staged diff review → tests → commit → local verification → push → remote verification**

- `git add .` is prohibited.
- No automatic tags/releases.
- Generated local artifacts must remain excluded.
- Commit/push is a separate controlled closeout operation from implementation.

# IR17 — Task #002 Closeout + Task #003 Specification

## Task #002 — CLOSED / PASS

- Commit: `c98d170`
- Message: `feat(phase5): establish implementation scaffolding`
- Parent/baseline: `71e84f3514d35d76c53a36b48d7a14220c4d633e`
- 21 files / 912 insertions.
- `git diff --check`: PASS.
- Environment reproduced using `uv sync --extra dev`.
- Tests: **13/13 PASS**, one non-blocking Starlette/httpx warning.
- Remote branch: `origin/phase5/task002-scaffolding`.
- `main`: unchanged.
- No tag/release.

## Task #003 — Specification

Approved as the first retrieval foundation:

- explicit retrieval domain interfaces;
- deterministic navigation-first retrieval;
- repository-source abstraction;
- hierarchical repository → population → PP/asset → artifact/evidence target;
- provenance/traceability;
- deterministic empty/invalid/not-found semantics;
- automated tests;
- no embeddings/vector DB/LLM/clinical reasoning/production generation.

# IR18 — Task #003 Closeout + Task #004 Specification

## Task #003 — CLOSED / PASS

Authoritative implementation branch:

`phase5/task002-scaffolding`

Task #003 commit:

`a7b52465d6fa451faae6830c6f6c4b4fb4f80640`

Message:

`feat(phase5): establish retrieval foundation`

Parent:

`c98d170dd3b25f63cf555fce69dd759c1f57d812`

Verification:

- **36/36 tests PASS**
- `git diff --check`: PASS
- Authorized implementation scope only (`08_Development/**`)
- No Gold PP/governance-controlled material modified
- `main` unchanged
- No tag/release
- Remote verification:
  - `origin/phase5/task002-scaffolding` → `a7b52465d6fa451faae6830c6f6c4b4fb4f80640`
  - `origin/main` → `71e84f3514d35d76c53a36b48d7a14220c4d633e`

## Task #004 — Specification

Approved objective:

Advance the Task #003 retrieval abstraction to the first controlled repository-backed `RepositorySource`, preserving deterministic navigation-first behavior and provenance without introducing embeddings/vector infrastructure/LLM/clinical logic.

Authorized implementation area:

`08_Development/**`

Explicitly excluded:

- embeddings/vector DB;
- semantic-search provider;
- LLM provider/model;
- clinical reasoning/medical decision logic;
- Runtime Evidence Package assembly;
- response generation/output validation;
- autonomous repository-wide ingestion/indexing;
- Gold PP/governance changes;
- production DB schema/ORM;
- deployment/UI.

# IR19 — Task #004 Closeout

## Task #004 — CLOSED / PASS

Objective achieved:

- Repository-backed `FilesystemRepositorySource` added behind the existing `RepositorySource` abstraction.
- Explicit/configurable source-root boundary.
- Bounded, non-recursive population directory resolution.
- Canonical four-artifact discovery.
- Repository-relative provenance preservation.
- Deterministic handling of success, empty, not-found, ambiguous, malformed, and missing-source conditions.
- Existing Task #003 contracts preserved.
- No embeddings, vector DB, semantic search, LLM, clinical reasoning, Runtime Evidence Package assembly, response generation, or output validation introduced.

### Verification

- `uv sync --extra dev`: PASS
- Full implementation suite: **53/53 PASS**
- `git diff --check`: PASS
- Only `08_Development/**` changed.
- No Gold PP/governance-controlled material modified.
- No `main` modification.
- No tag/release.

### Authoritative commit

`c28b498b6f13066253940291bdcbc6ed3f2f4e2c`

Message:

`feat(phase5): establish filesystem repository source`

Parent:

`f197b80` — Task #003 commit as applied locally/authoritatively in the current branch history.

### Remote verification

- `origin/phase5/task002-scaffolding` → `c28b498b6f13066253940291bdcbc6ed3f2f4e2c`
- `origin/main` → `71e84f3514d35d76c53a36b48d7a14220c4d633e`
- Remote and local Task #004 commit match.
- `main` remains unchanged.

Task #004 is therefore **CLOSED / PASS / REMOTE VERIFIED**.


---

# IR20 — Task #005 Implementation Specification — Batch B1

## Batch Status

**APPROVED / LOCKED**

Task #005 is authorized to implement the controlled transformation:

**Retrieval Result → Runtime Evidence Package**

A dedicated Runtime Evidence Package (RTEP) assembly boundary is introduced
between Retrieval and Generation.

### Locked B1 Decisions

- **B1-01:** Task #005 implements Retrieval Result → Runtime Evidence Package transformation.
- **B1-02:** RTEP Assembly is a controlled architectural boundary separate from Generation.
- **B1-03:** `RetrievalResponse` is not equivalent to `RuntimeEvidencePackage`; RTEP is assembled through a controlled contract.
- **B1-04:** RTEP contains governed evidence plus governance/provenance metadata only; it does not contain prompting or generation content.
- **B1-05:** Navigation Context is upstream context and is referenced by controlled identifier/metadata; it is not embedded as Evidence Content.
- **B1-06:** Task #005 does not expand into Generation, Validation, semantic/vector retrieval, embeddings/vector DB, LLM, clinical reasoning, deployment, or production database implementation.

### Architectural Boundary

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

---

# IR21 — Task #005 Implementation Specification — Batch B2

## Batch Status

**APPROVED / LOCKED**

B2 locks the Runtime Evidence Package contract as the implementation
representation of the existing governed Evidence Package Specification.

### Locked B2 Decisions

- **B2-01:** RTEP has two logical components: Evidence Content and Evidence Metadata.
- **B2-02:** Each Evidence Item represents a retrieved Clinical Knowledge Object with complete minimum provenance.
- **B2-03:** Minimum Evidence Metadata contains:
  - `evidence_package_id`
  - `retrieval_id`
  - `navigation_context_id`
  - `retrieval_policy_version`
  - `knowledge_base_version`
  - `generation_timestamp`
- **B2-04:** Minimum provenance contains:
  - `knowledge_object_id`
  - `knowledge_passport_id`
  - `source_id`
  - `guideline_version`
- **B2-05:** Navigation Context is linked through `navigation_context_id`; the full Navigation Context is not copied into Evidence Content.
- **B2-06:** Evidence ordering is preserved exactly as produced by the Retrieval Layer; downstream RTEP assembly does not reorder, rerank, or heuristically deduplicate evidence.
- **B2-07:** RTEP is immutable after assembly; changed retrieval results produce a new RTEP rather than mutating an existing package.
- **B2-08:** RTEP does not contain prompt instructions, prompt templates, model directives, generated responses, or model-generated clinical interpretation.
- **B2-09:** The implementation uses typed Pydantic 2.x models; exact downstream API/JSON serialization remains outside this batch unless separately authorized.
- **B2-10:** Primary Evidence Package and Runtime Evidence Package remain distinct artifacts with distinct lifecycle roles.

### Implementation Interpretation Rule

B2 is an implementation interpretation of the locked
`EVIDENCE_PACKAGE_SPECIFICATION.md` and related runtime architecture.
It does not reopen or redefine those governed specifications.

---


---

# IR22 — Task #005 Implementation Specification — Batch B3

## Batch Status

**APPROVED / LOCKED**

B3 locks the controlled Runtime Evidence Package assembly and failure
semantics.

### Locked B3 Decisions

- **B3-01:** RTEP Assembly accepts a completed `RetrievalResponse` and performs a downstream transformation; it does not retrieve again.
- **B3-02:** Successful assembly produces a complete contract-valid RTEP; partial/best-effort RTEP is not a successful assembly.
- **B3-03:** `EMPTY` retrieval is a valid RTEP state and produces an empty-but-valid RTEP; evidence-insufficiency handling remains downstream.
- **B3-04:** `NOT_FOUND` produces no RTEP and propagates the deterministic retrieval outcome.
- **B3-05:** `INVALID_REQUEST` produces no RTEP and is propagated unchanged.
- **B3-06:** A malformed/incomplete required evidence candidate causes atomic assembly failure; candidates are not silently dropped.
- **B3-07:** Missing required metadata or provenance causes assembly failure; placeholders are not invented.
- **B3-08:** Ambiguous retrieval state causes deterministic failure; assembly does not resolve ambiguity heuristically.
- **B3-09:** Assembly does not repair, enrich, rerank, deduplicate heuristically, or re-retrieve.
- **B3-10:** Retrieval outcomes, assembly failures, and downstream `PASS`/`FAIL`/`SAFE_FALLBACK` remain distinct layers.
- **B3-11:** Assembly is atomic: success produces one complete package; failure produces zero RTEP.
- **B3-12:** Assembly is deterministic and side-effect free with respect to knowledge retrieval.
- **B3-13:** Assembly failures remain traceable through existing runtime identifiers and structured failure classification without unnecessary clinical-content logging.

---

# IR23 — Task #005 Implementation Specification — Batch B4

## Batch Status

**APPROVED / LOCKED**

B4 locks the implementation surface, tests, acceptance criteria, and
controlled closeout boundary for Task #005.

### Locked B4 Decisions

- **B4-01:** Implementation is strictly bounded to `08_Development/**`.
- **B4-02:** Task #005 introduces a clearly isolated RTEP contract/assembly surface within the existing implementation package; exact filename follows existing package conventions.
- **B4-03:** Existing Task #002–#004 retrieval contracts and repository-source semantics remain preserved.
- **B4-04:** Canonical RTEP representation is typed and contract-validated; an untyped dictionary is not the authoritative representation.
- **B4-05:** RTEP assembly is exposed through one explicit, testable assembly boundary governed by B2/B3.
- **B4-06:** Tests cover contract, successful assembly, empty retrieval, deterministic failures, and architectural boundaries.
- **B4-07:** Evidence ordering is explicitly regression-tested as sequence preservation.
- **B4-08:** RTEP immutability is behaviorally tested.
- **B4-09:** Provenance tests verify value preservation, not only schema presence.
- **B4-10:** Acceptance verifies that no generation, LLM, clinical-reasoning, or output-validation behavior is introduced.
- **B4-11:** All existing and new tests plus scope checks must pass.
- **B4-12:** The full regression suite is mandatory.
- **B4-13:** Task #005 follows the existing controlled implementation, commit, push, and remote-verification workflow.
- **B4-14:** Task #005 PASS establishes RTEP-boundary readiness only; it does not imply Generation Ready, Validation Ready, Clinical/Safety Ready, or Deployment Ready.
- **B4-15:** Any prohibited scope-expanding behavior is an automatic Task #005 acceptance failure unless separately authorized.

---

# Phase 5 Current Implementation State

| Task | Status | Commit |
|---|---|---|
| #002 | CLOSED / PASS | `c98d170` |
| #003 | CLOSED / PASS | `f197b80` |
| #004 | CLOSED / PASS | `c28b498` |
| #005 | SPECIFICATION COMPLETE — B1/B2/B3/B4 APPROVED; IMPLEMENTATION HANDOFF READY | — |

Authoritative implementation branch:

`phase5/task002-scaffolding`

Current remote implementation HEAD:

`c28b498b6f13066253940291bdcbc6ed3f2f4e2c`

`main` remains:

`71e84f3514d35d76c53a36b48d7a14220c4d633e`

---

# Phase 5 Working Method — LOCKED

The operational workflow for subsequent tasks is:

**Task specification → Claude implementation → Claude export patch → ChatGPT review → VS Code apply → tests → controlled commit → push → remote verify → close task**

This workflow is independent of Claude Code's GitHub write permission.

Claude Code is the implementation/testing/patch-export executor.

ChatGPT is the strategy, governance, review, decision, and task-specification authority.

VS Code/local Git is the controlled integration, commit, push, and remote-verification environment.

Claude must not independently change locked governance, clinical, safety, architecture, or technology decisions.

---

# Phase 5 Specification Workflow — LOCKED

Task #005 implementation specification is developed through four controlled decision batches:

**B1 Scope/Architecture Boundary → B2 Runtime Evidence Package Contract → B3 Assembly/Failure Semantics → B4 Implementation Surface/Tests/Acceptance**

Each batch follows:

**proposal → Project Coordinator review → approval → locked decision set → next batch**

No batch is considered locked until explicitly approved.

After every approved IR batch that creates a new locked decision set, `PHASE_5_IMPLEMENTATION_READINESS_DECISION_RECORD.md` must be updated.

`Phase_5_Governance_Consolidated_Decision_Record.md` is not updated after every IR batch. It is reviewed/updated at governance milestone, package close, phase close, or thread handover, and must then consolidate the full A–D governance state plus all IR decisions locked at that point.

---

# Thread Handover Rule

At thread/phase handover:

1. Update this Implementation Readiness Decision Record after each approved IR batch; at handover ensure it contains the complete current locked state.
2. Update `Phase_5_Governance_Consolidated_Decision_Record.md` so it consolidates A–D + all locked IR decisions through the handover point.
3. Ensure project-management status/roadmap/repository-map materials reflect the current Phase 5 state where required.
4. Carry forward the authoritative branch, current remote HEAD, task state, locked artifacts, and workflow.
5. Educate the new thread using the Phase 5 master handover prompt.


---

# Amendment History

## Version 5.0

Updated following approval of Task #005 Implementation Specification B1 and B2.

Major updates include:

- B1 Scope & Architecture Boundary approved and locked as IR20.
- B2 Runtime Evidence Package Contract approved and locked as IR21.
- Task #005 specification workflow formally recorded as:
  B1 → B2 → B3 → B4.
- Batch-based approval workflow recorded as a locked Phase 5 working method.
- Recording rule reaffirmed: update this IR record after every approved IR batch.
- Governance Consolidated Decision Record update cadence clarified:
  governance milestone / package close / phase close / thread handover.
- Task #005 remains specification-in-progress; no implementation authorization
  has yet been issued.


---

# Amendment History

## Version 6.0

Updated following approval and locking of Task #005 specification B3 and B4.

Major updates include:

- IR22 — B3 Assembly + Failure Semantics approved and locked.
- IR23 — B4 Implementation Surface + Tests + Acceptance approved and locked.
- Task #005 specification B1–B4 is now complete and implementation-handoff ready.
- Task #005 remains unimplemented; no implementation commit or remote HEAD change
  has occurred as a result of the specification work.
- Current authoritative Phase 5 implementation branch and remote HEAD remain
  unchanged from Task #004.
