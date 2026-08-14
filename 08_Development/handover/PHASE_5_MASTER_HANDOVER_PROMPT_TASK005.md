# MASTER HANDOVER — SAFE MEDICAL AI ONCOLOGY
## Phase 5 Continuation — Task #005

You are entering an existing Safe Medical AI Oncology project thread. Treat this prompt as the authoritative working-context handover. Do not restart discovery from zero and do not ask the user to re-explain the project unless a genuine contradiction/blocker is found.

---

# 1. PROJECT IDENTITY

Project:
**Safe Medical AI Oncology**

Goal:
Build a governed, traceable, evidence-grounded medical AI system whose implementation is constrained by the project's locked architecture, clinical knowledge governance, safety framework, output contract, and repository controls.

This is NOT a generic chatbot project.

The system must preserve:
- governed clinical knowledge;
- provenance and traceability;
- retrieval readiness;
- evidence-grounded runtime behavior;
- explicit output validation;
- clinical/safety governance;
- reproducibility and auditability.

The project already has:
- locked governance/architecture foundations;
- 239 Gold Population Packages / 956 canonical Gold artifacts from earlier phases;
- verified repository/integration evidence;
- Phase 5 implementation specifications;
- an implementation scaffold and retrieval foundation already committed.

Do not modify Gold PP or governance-controlled materials unless explicitly authorized.

---

# 2. PHASE 5 OBJECTIVE

Phase 5 follows this locked pipeline:

readiness
→ retrieval
→ runtime integration
→ evidence/output validation
→ technical validation
→ clinical/safety validation
→ remediation
→ closure

Each task is intentionally small, testable, auditable, and may have controlled sub-tasks if evidence requires them.

Current position:
**Phase 5 — Task #005 specification**

Tasks already closed:

Task #002 — implementation scaffolding
Commit: c98d170

Task #003 — retrieval foundation
Commit: a7b5246 / local authoritative history may show f197b80 if the patch was applied locally and recommitted

Task #004 — filesystem-backed repository source
Commit: c28b498

Authoritative remote branch:
`phase5/task002-scaffolding`

Current remote HEAD:
`c28b498b6f13066253940291bdcbc6ed3f2f4e2c`

Main:
`71e84f3514d35d76c53a36b48d7a14220c4d633e`

Do not rename/recreate branch topology without explicit instruction.

---

# 3. LOCKED PHASE 5 DECISIONS

## TECH_STACK.md — IR12 APPROVED

Locked core:
- Python 3.12
- FastAPI
- Pydantic 2.x
- pytest
- uv + pyproject.toml
- PostgreSQL direction for structured runtime storage
- provider-agnostic LLM adapter
- environment-variable configuration + .env.example
- structured logging + trace IDs

Architecture:
API
→ orchestration
→ retrieval/evidence
→ generation
→ validation

Retrieval:
navigation-first
→ metadata/structured filtering
→ lexical retrieval
→ semantic retrieval
→ evidence assembly

Exact embedding model, vector engine, LLM provider/model, detailed runtime schemas, and exact package versions remain deferred unless a later evidence-based decision explicitly locks them.

## OUTPUT_CONTRACT.md — IR13 APPROVED

Runtime generation requires:
- user request/intent;
- Navigation Context;
- Runtime Evidence Package;
- applicable safety/governance context;
- delivery constraints.

Meaningful clinical factual claims require traceable evidence.

Controlled output outcomes:
- PASS
- FAIL
- SAFE_FALLBACK

Generation, validation, and final delivery decision are separate concerns.

## RETRIEVAL READY — IR9–IR11 APPROVED

RR-1 through RR-5:
**PASS**

Repository-level Retrieval Ready:
**PASS**

This means knowledge/repository readiness, NOT clinical validation, runtime validation, deployment readiness, or safety approval.

---

# 4. CURRENT IMPLEMENTATION

## Task #002 — CLOSED

Scaffold:
- 08_Development/
- Python package foundation
- config
- trace IDs
- structured logging
- FastAPI health endpoint
- Pydantic foundation
- provider-agnostic LLM adapter seam
- pytest
- pyproject.toml
- uv.lock
- .env.example
- .gitignore

13/13 tests passed.

## Task #003 — CLOSED

Retrieval foundation:
- RetrievalRequest
- RetrievalCandidate
- RetrievalResponse
- RepositorySource abstraction
- InMemoryRepositorySource
- RetrievalService
- navigation-first population ID validation
- hierarchical retrieval
- deterministic artifact ordering
- provenance
- explicit FOUND / EMPTY / NOT_FOUND / INVALID_REQUEST outcomes

36/36 tests passed.

## Task #004 — CLOSED

Filesystem-backed repository source:
- FilesystemRepositorySource
- explicit configurable source root
- bounded non-recursive population resolution
- exact-name / controlled prefix-name resolution
- canonical four-artifact discovery
- repository-relative provenance
- safe handling of missing source, ambiguity, empty population, malformed artifact entry
- no autonomous repository-wide indexing
- no embeddings/vector DB/LLM

53/53 tests passed.

Task #004 commit:
`c28b498b6f13066253940291bdcbc6ed3f2f4e2c`

---

# 5. CRITICAL ARCHITECTURAL DISTINCTIONS

Never confuse:

**Primary Evidence Package**
= governed knowledge-population artifact.

**Runtime Evidence Package**
= future runtime representation/context supplied to generation.

Never treat Gold PP = Retrieval Ready automatically.

Never let implementation code silently change governance decisions.

Never let model knowledge substitute for governed runtime evidence.

Never couple retrieval to an LLM provider or prematurely lock a vector engine.

---

# 6. WORKING METHOD — LOCKED

Use this workflow for every subsequent task:

**Task specification
→ Claude implementation
→ Claude export patch
→ ChatGPT review
→ VS Code apply
→ tests
→ controlled commit
→ push
→ remote verify
→ close task**

Reason:
Claude Code currently cannot reliably push to the GitHub repository from its own session.

Therefore:

Claude:
- reads project;
- implements;
- tests;
- exports patch;
- reports exact SHA/file list/state.

ChatGPT:
- designs task;
- reviews implementation;
- controls scope;
- makes governance/architecture decisions;
- approves/rejects closeout;
- designs next task.

VS Code/local Git:
- applies patch;
- verifies;
- stages explicitly;
- reviews staged diff;
- commits;
- pushes;
- verifies remote.

NEVER use `git add .` for controlled closeout.

Do not combine independent tasks into one commit merely for convenience. Each task should normally have its own auditable commit.

---

# 7. GIT / REPOSITORY RULES

Authoritative implementation branch:
`phase5/task002-scaffolding`

Do not modify:
- main;
- 01_Foundation/
- 02_Architecture/
- 03_Clinical_Knowledge/
- 04_Knowledge_Governance/
- 05_Operations/
- 06_Governance/
- 07_Project_Management/
- 09_Evaluation/
- archive/

unless explicitly authorized by the task.

Working/local materials such as:
- working/
- sources/
- archive/
- .vscode/
- local .rar files
must not be swept into commits.

The repository is a controlled project state, not a mirror of every local material.

Clinical copyrighted source documents must not be pushed unless redistribution rights are explicitly established.

---

# 8. RESPONSE FORMAT — LOCKED

At the end of every response use exactly these two sections:

## Bạn cần làm gì
Give the exact immediate action for the user, preferably copy/pasteable.

## Đang ở đâu
State:
- current Phase;
- current Task/IR gate;
- current status;
- next step.

Keep this concise and operational.

When handing over to another thread, preserve this format and educate the new thread to use it.

---

# 9. RECORD / GOVERNANCE UPDATE RULES

`PHASE_5_IMPLEMENTATION_READINESS_DECISION_RECORD.md`:
- update after every approved IR batch when it introduces a locked decision;
- record task closeouts and authoritative commits;
- current record is locked through Task #004 closeout / IR19.

`Phase_5_Governance_Consolidated_Decision_Record.md`:
DO NOT update after every IR batch.

Update at:
- governance milestone;
- package close;
- phase close;
- thread/phase handover.

When updated, consolidate:
- all A–D locked decisions;
- all IR decisions locked through that point;
- current task/implementation state;
- current authoritative branch/commit where relevant.

Also keep project-management status/roadmap/repository-map materials synchronized when a milestone materially changes repository/project state.

---

# 10. CURRENT HANDOVER MATERIALS

Authoritative/essential:
1. PHASE_5_IMPLEMENTATION_READINESS_DECISION_RECORD.md
2. TECH_STACK.md
3. OUTPUT_CONTRACT.md
4. Formal Retrieval Ready Assessment Record
5. Phase_5_Governance_Consolidated_Decision_Record.md
6. relevant locked architecture/policy:
   - RAG_ARCHITECTURE v1.1
   - RETRIEVAL_POLICY
   - EVIDENCE_PACKAGE_SPECIFICATION v1.1
   - RESPONSE_GENERATION_ARCHITECTURE v1.1
   - OUTPUT_VALIDATION_FRAMEWORK
7. current Claude Task specification if one exists
8. current implementation README / retrieval README
9. latest task commit history / remote verification
10. this master handover prompt

Do not upload the entire 239-PP corpus to the new thread unless a task specifically requires content-level inspection.

---

# 11. IMPORTANT CURRENT STATE

Task #004 is CLOSED / PASS / REMOTE VERIFIED.

Current remote:
`phase5/task002-scaffolding @ c28b498`

Main remains:
`71e84f3`

Next:
**Task #005 must be specified and reviewed before implementation.**

Do not assume the old pre-Phase-5 roadmap's Task #005 label is still binding. The actual executed sequence has evolved from the approved IR/task decisions. Determine the next task from the current architecture, implementation state, and Phase 5 pipeline.

Do not start implementation merely because a future task is mentioned.

First:
**review current state → design Task #005 → discuss/approve → produce Claude Task #005 specification → implement → export patch → review → apply locally → test → controlled closeout.**

END HANDOVER.
