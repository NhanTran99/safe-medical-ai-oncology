# TASK #005 — CLAUDE IMPLEMENTATION HANDOFF

## Handoff Status

**AUTHORIZED FOR IMPLEMENTATION**

You are the implementation executor for Task #005 of the Safe Medical AI
Oncology Phase 5 project.

Do not restart project discovery.

Do not redesign the architecture.

Do not make governance decisions.

The approved Task #005 specification is the controlling implementation scope.

---

# 1. Read These First

Read in this order:

1. `TASK_005_IMPLEMENTATION_SPECIFICATION_v1.0.md`
2. `PHASE_5_IMPLEMENTATION_READINESS_DECISION_RECORD_v6.0.md`
3. `Phase_5_Governance_Consolidated_Decision_Record_v6.0.md`
4. `TECH_STACK.md`
5. `OUTPUT_CONTRACT.md`
6. `EVIDENCE_PACKAGE_SPECIFICATION.md` v1.1
7. `RETRIEVAL_POLICY.md`
8. `RAG_ARCHITECTURE.md` v1.1
9. `RESPONSE_GENERATION_ARCHITECTURE.md` v1.1
10. `OUTPUT_VALIDATION_FRAMEWORK.md`
11. current `08_Development/implementation/` code and tests

If a current implementation detail differs from the specification, stop and
report the discrepancy rather than silently changing the specification.

---

# 2. Current Git State

Authoritative branch:

`phase5/task002-scaffolding`

Current remote HEAD:

`c28b498b6f13066253940291bdcbc6ed3f2f4e2c`

Main:

`71e84f3514d35d76c53a36b48d7a14220c4d633e`

Do not rename, recreate, rebase, or otherwise alter branch topology.

---

# 3. What You Are Implementing

Implement only:

**Retrieval Result → Runtime Evidence Package**

The boundary is:

```text
RetrievalResponse
      ↓
RTEP Assembly
      ↓
RuntimeEvidencePackage
```

Do not implement Generation.

Do not implement Validation.

---

# 4. Hard Scope Boundary

Allowed:

`08_Development/**`

Not allowed:

- governance documents;
- architecture documents;
- Gold PP;
- Population Package files;
- Project Status/Roadmap;
- repository-map;
- sources;
- archive;
- main branch;
- unrelated project files.

Do not use `git add .`.

Do not commit or push in this task.

---

# 5. Non-Negotiable Constraints

Do NOT introduce:

- LLM;
- embeddings;
- vector DB;
- semantic retrieval;
- prompt generation;
- response generation;
- clinical reasoning;
- output validation;
- autonomous indexing;
- heuristic reranking;
- silent provenance repair;
- generation fallback.

Do not change existing Task #003/#004 retrieval semantics.

---

# 6. Required Implementation

Implement:

### RTEP contract

Two logical components:

```text
Evidence Content
Evidence Metadata
```

Metadata:

- `evidence_package_id`
- `retrieval_id`
- `navigation_context_id`
- `retrieval_policy_version`
- `knowledge_base_version`
- `generation_timestamp`

Provenance:

- `knowledge_object_id`
- `knowledge_passport_id`
- `source_id`
- `guideline_version`

Use Pydantic 2.x typed models.

### Assembly

Input:

completed RetrievalResponse + required runtime metadata.

Output:

immutable RuntimeEvidencePackage.

Behavior:

- preserve ordering;
- preserve provenance;
- EMPTY → valid empty RTEP;
- NOT_FOUND → no RTEP;
- INVALID_REQUEST → no RTEP;
- ambiguous → deterministic failure;
- malformed/incomplete evidence → atomic failure;
- missing metadata/provenance → failure;
- no repair/retrieve/rerank/reorder.

---

# 7. Testing

Add focused tests for:

- contract;
- valid assembly;
- EMPTY;
- NOT_FOUND;
- INVALID_REQUEST;
- ambiguity;
- malformed evidence;
- missing metadata;
- incomplete provenance;
- ordering;
- immutability;
- provenance value preservation;
- architectural boundaries;
- full regression.

Run:

```text
uv sync --extra dev
pytest
git diff --check
```

Do not stop at only the new tests.

---

# 8. Before You Finish

Inspect the final diff.

Report:

1. exact changed files;
2. exact tests added/changed;
3. test command and result;
4. `git diff --check` result;
5. confirmation that only `08_Development/**` changed;
6. confirmation that no prohibited functionality was introduced;
7. patch/export location;
8. any ambiguity/blocker.

Do not claim:

- commit complete;
- push complete;
- remote verified;
- Task #005 closed

because those steps are handled separately.

---

# 9. Required Output

Your final response must be a concise implementation report plus the exported
patch.

Preferred structure:

## Implementation Summary

...

## Changed Files

...

## Tests

...

## Scope Verification

...

## Patch

...

## Blockers / Decisions Needed

...

END HANDOFF
