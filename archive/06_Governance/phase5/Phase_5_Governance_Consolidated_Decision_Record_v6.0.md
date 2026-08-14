# Phase 5 Governance Consolidated Decision Record

Status: **LOCKED — v6.0 — consolidated through Task #005 specification close / B4 approval**

Purpose: Single governance handover/reference for Phase 5.

---

# 1. Project State

Phase 3: **CLOSED**

Phase 4: **CLOSED / PASS**

Phase 3 immutable baseline:

`a838a9423fc3d14c46f8cd176bafed3b691e65c0`

Phase 4 closing commit:

`70067d020420eb1792419bb7d7308da524f0031c`

Post-integration archive correction:

`d4c2994e390d746c37276b7d29d0ba57ebae0d53`

Phase 5 implementation branch:

`phase5/task002-scaffolding`

Current remote Phase 5 implementation HEAD:

`c28b498b6f13066253940291bdcbc6ed3f2f4e2c`

`main` remains:

`71e84f3514d35d76c53a36b48d7a14220c4d633e`

No Phase 5 tag/release has been created.

---

# 2. Phase 5 Definition

Phase 5 = **System Implementation & Validation**.

Locked pipeline:

**readiness → retrieval → runtime integration → evidence/output validation → technical validation → clinical/safety validation → remediation → closure**

Phase 5 implementation is task-bounded. A task must not silently expand into the next architectural layer.

---

# 3. Governance Packages A–D

## Package A — Phase 5 Scope / Responsibilities / Claude Boundary

Locked:

- Phase 5 implementation is controlled through bounded tasks.
- Claude Code implements approved specifications; it does not make governance,
  clinical, safety, or architecture decisions.
- ChatGPT owns strategy, governance interpretation, task specification,
  scope review and closeout decision.
- VS Code/local Git performs controlled patch application, explicit staging,
  commit, push and remote verification.
- `git add .` is prohibited.
- Main remains protected unless explicitly authorized.
- Gold/governance-controlled materials are not modified by implementation
  unless explicitly authorized.

## Package B — Retrieval Ready / Evidence / KAR-PIM

Locked:

- Gold does not automatically mean Retrieval Ready.
- Retrieval Ready is a controlled derived gate, not a lifecycle state.
- RR-1 through RR-5 are PASS.
- Repository-level Retrieval Ready is PASS.
- Retrieval Ready is a knowledge/repository readiness gate, not clinical,
  safety, deployment, or generation validation.
- Existing Population Integration Manifest and Knowledge Asset Registry remain
  distinct authorities.
- Provenance and traceability must remain preserved.

## Package C — Repository Lifecycle / Archive / Release

Locked:

- Repository commit is authoritative.
- Tags/releases are optional and never auto-created.
- Working, Controlled and Archive materials remain distinct.
- Generated/local artifacts must not be swept into controlled commits.
- Clinical copyrighted source documents must not be pushed without
  redistribution rights.
- Controlled closeout sequence:
  inventory → classify → canonical paths → explicit staging →
  staged diff review → tests → commit → local verification →
  push → remote verification.

## Package D — Post-Gold Amendment Governance

Locked:

- Post-Gold changes require governed amendment and proportionate downstream
  verification.
- Gold Population Packages remain controlled knowledge products.
- Implementation code must not silently amend clinical knowledge or governance.
- Changes affecting provenance, lifecycle, integration, retrieval readiness,
  or governed knowledge require appropriate governance handling.

---

# 4. Locked Phase 5 Technology / Runtime Decisions

## TECH_STACK — IR12

Locked:

- Python 3.12
- FastAPI
- Pydantic 2.x
- pytest
- `uv` + `pyproject.toml`
- PostgreSQL as structured runtime-storage direction
- provider-agnostic LLM adapter
- environment-variable configuration + `.env.example`
- structured logging + trace IDs

Deferred:

- exact embedding model;
- exact vector database/vector engine;
- exact LLM provider/model;
- detailed runtime database schema;
- exact package patch/minor versions unless justified by implementation evidence.

## OUTPUT_CONTRACT — IR13

Locked:

- Required generation inputs include user request/intent, Navigation Context,
  Runtime Evidence Package, applicable safety/governance context, and delivery
  constraints.
- Meaningful clinical factual claims require traceable evidence.
- Runtime must distinguish evidence sufficient from evidence insufficient.
- Controlled outcomes: `PASS`, `FAIL`, `SAFE_FALLBACK`.
- Generation, validation and final delivery decision remain separate.
- Exact downstream JSON/Pydantic/API schema remains an implementation
  specification consistent with the contract.

---

# 5. Retrieval Readiness State

RR-1 Gold Integrity: **PASS**

RR-2 Repository Verification: **PASS**

RR-3 Registry Verification: **PASS**

RR-4 Traceability: **PASS**

RR-5 Required Integration Metadata: **PASS**

Formal repository-level Retrieval Ready: **PASS**

This does not imply:

- Generation Ready;
- Runtime Evidence Package Ready;
- Clinical/Safety Ready;
- Deployment Ready.

---

# 6. Task Closeout State

## Task #002 — CLOSED / PASS

Commit:

`c98d170`

## Task #003 — CLOSED / PASS

Historical upstream SHA:

`a7b52465d6fa451faae6830c6f6c4b4fb4f80640`

The recreated local authoritative history may show:

`f197b80`

These represent the same Task #003 implementation and must not be
treated as two separate implementations.

## Task #004 — CLOSED / PASS / REMOTE VERIFIED

Commit:

`c28b498b6f13066253940291bdcbc6ed3f2f4e2c`

Current implementation boundary:

**Repository → Population/PP → canonical Gold artifacts**

Task #004 did not implement Runtime Evidence Package assembly,
generation, validation, embeddings/vector DB, LLM, or clinical reasoning.

---

# 7. Task #005 Architecture / Scope Gate

Status:

**APPROVED / LOCKED**

Locked boundary:

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

Core architectural decisions:

- Retrieval Result is not equivalent to Runtime Evidence Package.
- RTEP Assembly is a controlled boundary separate from Generation.
- RTEP contains governed evidence plus governance/provenance metadata.
- Navigation Context is upstream context and is referenced by controlled
  identifier/metadata; it is not copied into Evidence Content.
- Task #005 does not implement Generation, Validation, semantic/vector
  retrieval, embeddings/vector DB, LLM, clinical reasoning, deployment,
  or production runtime database implementation.

---

# 8. Task #005 Implementation Specification — B1

Status:

**APPROVED / LOCKED**

Locked B1 decisions:

- B1-01: implement Retrieval Result → Runtime Evidence Package transformation.
- B1-02: RTEP Assembly is a separate architectural boundary.
- B1-03: `RetrievalResponse` ≠ `RuntimeEvidencePackage`.
- B1-04: RTEP contains governed evidence and provenance/metadata only.
- B1-05: Navigation Context is referenced, not embedded as Evidence Content.
- B1-06: prohibited scope expansion remains excluded.

---

# 9. Task #005 Implementation Specification — B2

Status:

**APPROVED / LOCKED**

RTEP has two logical components:

```text
Runtime Evidence Package
├── Evidence Content
└── Evidence Metadata
```

Minimum metadata:

- `evidence_package_id`
- `retrieval_id`
- `navigation_context_id`
- `retrieval_policy_version`
- `knowledge_base_version`
- `generation_timestamp`

Minimum provenance:

- `knowledge_object_id`
- `knowledge_passport_id`
- `source_id`
- `guideline_version`

Locked:

- preserve retrieval ordering;
- RTEP is immutable after assembly;
- no prompt/generation/model-generated content;
- typed Pydantic 2.x implementation;
- Primary Evidence Package ≠ Runtime Evidence Package.

---

# 10. Task #005 Implementation Specification — B3

Status:

**APPROVED / LOCKED**

Locked assembly semantics:

- B3-01: Assembly accepts completed `RetrievalResponse`; no second retrieval.
- B3-02: successful assembly produces a complete contract-valid RTEP.
- B3-03: `EMPTY` produces an empty-but-valid RTEP; insufficiency handling is downstream.
- B3-04: `NOT_FOUND` produces no RTEP.
- B3-05: `INVALID_REQUEST` produces no RTEP and is propagated.
- B3-06: malformed/incomplete required evidence causes atomic assembly failure.
- B3-07: missing required metadata/provenance causes assembly failure.
- B3-08: ambiguity is not heuristically resolved.
- B3-09: no repair, enrichment, reranking, heuristic deduplication or re-retrieval.
- B3-10: retrieval outcomes, assembly failures and downstream output outcomes
  remain separate layers.
- B3-11: assembly is atomic.
- B3-12: assembly is deterministic.
- B3-13: assembly failures are traceable through structured identifiers without
  unnecessary clinical-content logging.

---

# 11. Task #005 Implementation Specification — B4

Status:

**APPROVED / LOCKED**

Locked implementation/acceptance decisions:

- B4-01: implementation limited to `08_Development/**`.
- B4-02: isolated RTEP contract/assembly surface within existing package.
- B4-03: preserve Task #002–#004 retrieval contracts and source semantics.
- B4-04: canonical RTEP is typed/validated, not an authoritative untyped dict.
- B4-05: one explicit testable RTEP assembly boundary.
- B4-06: tests cover contract, success, empty, failures, boundaries.
- B4-07: ordering preservation is explicitly tested.
- B4-08: immutability is behaviorally tested.
- B4-09: provenance values are tested for preservation.
- B4-10: no generation/LLM/clinical reasoning/output validation introduced.
- B4-11: all existing and new tests plus scope checks must pass.
- B4-12: full regression suite mandatory.
- B4-13: existing controlled implementation/commit/push/remote verification workflow.
- B4-14: Task #005 PASS means RTEP boundary readiness only.
- B4-15: prohibited scope expansion is an automatic acceptance failure unless
  separately authorized.

---

# 12. Task #005 Current Status

**SPECIFICATION COMPLETE — B1/B2/B3/B4 APPROVED / LOCKED**

Implementation status:

**NOT YET IMPLEMENTED**

Current remote remains:

`phase5/task002-scaffolding @ c28b498b6f13066253940291bdcbc6ed3f2f4e2c`

No Task #005 commit exists yet.

---

# 13. Locked Working Method

**Task specification → Claude implementation → Claude export patch → ChatGPT review → VS Code apply → tests → controlled commit → push → remote verify → close task**

Claude:

- reads the project and locked specifications;
- implements only approved scope;
- runs tests;
- exports patch;
- reports exact file list and state;
- does not make governance/clinical/safety/architecture decisions;
- does not independently alter locked decisions.

ChatGPT:

- owns strategy;
- governance interpretation;
- task specification;
- implementation review;
- acceptance/closeout decision.

VS Code/local Git:

- applies patch;
- verifies;
- explicitly stages;
- reviews staged diff;
- commits;
- pushes;
- verifies remote.

---

# 14. Thread Handover / Recording Rules

`PHASE_5_IMPLEMENTATION_READINESS_DECISION_RECORD.md`:

- update after every approved IR batch that creates a locked decision set;
- record task closeouts and authoritative commits.

`Phase_5_Governance_Consolidated_Decision_Record.md`:

- do not update after every IR batch;
- update at governance milestone, package close, phase close, or thread/phase handover;
- when updated, consolidate all A–D governance decisions plus all IR decisions
  locked through that point;
- synchronize project status/roadmap/repository-map when a milestone materially
  changes project state.

Current v6.0 is the governance milestone/Task #005 specification close
consolidation point.

---

# 15. Next Controlled Milestone

**Task #005 Claude Implementation**

Before implementation:

1. hand Claude the complete Task #005 implementation specification;
2. provide the authoritative locked documents listed in the handover;
3. instruct Claude to inspect the current implementation before editing;
4. require a patch-only implementation response;
5. require tests and exact changed-file report;
6. prohibit commit/push unless a separate explicit closeout instruction is given.

After Claude returns:

**Claude patch → ChatGPT review → VS Code apply → tests → controlled commit → push → remote verification**

No Task #005 implementation is considered closed before that sequence completes.

---

# Amendment History

## Version 6.0

Updated at Task #005 specification close / B4 approval.

Major updates:

- Consolidated all Package A–D governance decisions through the current
  Phase 5 state.
- Incorporated Task #005 Architecture/Scope Gate approval.
- Incorporated Task #005 B1, B2, B3 and B4 locked decisions.
- Recorded Task #005 specification as complete and implementation-handoff ready.
- Preserved current authoritative branch and remote HEAD from Task #004.
- Confirmed that Task #005 has not yet been implemented.
- Reaffirmed the controlled Claude → patch → ChatGPT review → VS Code/local Git
  workflow.
- Reaffirmed deferred generation, validation, semantic retrieval, embeddings,
  vector DB, LLM, clinical reasoning and deployment boundaries.

No implementation commit was created by this governance update.
