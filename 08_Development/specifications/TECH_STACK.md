# TECH_STACK.md

Status: **LOCKED — Phase 5 Implementation Readiness**
Decision: **IR12 APPROVED**
Purpose: Controlled technology-stack specification for Phase 5 System Implementation & Validation.

## 1. Core Runtime Stack

| Area | Locked choice | Boundary |
|---|---|---|
| Language | Python 3.12 | Primary implementation language |
| API/runtime framework | FastAPI | API boundary; not business-logic container |
| Data/schema validation | Pydantic 2.x | Runtime contracts and validation models |
| Testing | pytest | Unit, integration and contract testing |
| Dependency/environment management | `uv` + `pyproject.toml` | Primary dependency authority |
| Structured runtime storage | PostgreSQL direction | Exact schema deferred |
| LLM integration | Provider-agnostic adapter | Provider/model deferred |
| Configuration | Environment variables + `.env.example` | No secrets committed |
| Logging/traceability | Structured logging + trace IDs | Runtime observability foundation |

## 2. Architecture Principles

### 2.1 Separation of concerns

```text
API
 ↓
Orchestration
 ↓
Retrieval / Evidence
 ↓
Generation
 ↓
Validation
```

Business logic must remain separable from the API layer.

### 2.2 Retrieval

Retrieval follows the approved navigation-first / hierarchical philosophy and is implemented behind abstractions.

Baseline conceptual flow:

```text
Navigation
 ↓
Metadata / structured filtering
 ↓
Lexical retrieval
 ↓
Semantic retrieval
 ↓
Evidence assembly
```

The exact retrieval engine is intentionally not locked by this document.

### 2.3 Evidence and output

Runtime Evidence Package, response generation and output validation remain separate governed components.

`TECH_STACK.md` does not replace:
- `EVIDENCE_PACKAGE_SPECIFICATION`
- `OUTPUT_CONTRACT`
- `OUTPUT_VALIDATION_FRAMEWORK`

## 3. Development Structure

Implementation target:

```text
08_Development/
├── specifications/
└── implementation/
```

Task #002 will establish the implementation scaffolding and dependency/testing foundation. No functional retrieval/runtime implementation is implied by this document alone.

## 4. Deferred Decisions

The following are intentionally **NOT LOCKED**:

- exact package patch/minor versions;
- exact embedding model;
- exact vector database/vector engine;
- exact LLM provider;
- exact LLM model;
- detailed runtime database schema;
- detailed retrieval index schema;
- detailed implementation filenames.

These must be decided only when implementation evidence/compatibility requirements justify them.

## 5. Security / Repository Rules

- Secrets must not be committed.
- Use environment configuration and `.env.example`.
- Controlled repository changes follow the project's explicit staging/review/commit workflow.
- Claude Code may implement within this specification but may not independently change locked technology decisions.

## 6. Acceptance

This document establishes the **core Phase 5 technology stack** required before implementation scaffolding.

Implementation-specific dependency versions and vendor/model selections remain controlled downstream decisions.
