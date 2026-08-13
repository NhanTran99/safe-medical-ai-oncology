# 08_Development/implementation/

Python implementation package for the Safe Medical AI Oncology system,
established as Phase 5 Task #002 scaffolding and extended by Task #003 with
a controlled repository retrieval foundation.

## Scope of the Task #002 scaffolding

This package contains **no runtime generation or clinical business logic**.
It establishes only:

- a reproducible Python 3.12 project (`uv` + `pyproject.toml` at the
  repository root);
- an environment-variable configuration skeleton (`config.py`);
- a structured logging foundation (`logging_setup.py`);
- a trace-ID foundation (`trace.py`);
- a minimal FastAPI application exposing a health-check endpoint only
  (`api/main.py`);
- minimal typed placeholder models (`models/`) reflecting controlled
  vocabulary from `OUTPUT_CONTRACT.md` (e.g. the PASS / FAIL / SAFE_FALLBACK
  validation outcome enum) and empty structural placeholders for the future
  Navigation Context, Runtime Evidence Package and generated-response
  models. Field-level schema for these remains an intentionally deferred
  decision (see `OUTPUT_CONTRACT.md` §11 and `TECH_STACK.md` §4) and is
  **not** locked by this scaffolding;
- a minimal provider-agnostic LLM adapter interface (`llm/base.py`) with
  no concrete provider implementation;
- a pytest baseline (`tests/`) proving the scaffold imports and runs.

## Scope of the Task #003 retrieval foundation

`retrieval/` adds a deterministic, provider/engine-agnostic navigation-first
retrieval foundation (no embeddings, vector search, or LLM integration — see
`retrieval/README.md` for the full interface description, result semantics,
and deferred scope).

## Directory layout

```text
08_Development/implementation/
├── src/
│   └── safe_medical_ai/
│       ├── __init__.py
│       ├── config.py
│       ├── logging_setup.py
│       ├── trace.py
│       ├── models/
│       │   ├── __init__.py
│       │   └── output_contract.py
│       ├── llm/
│       │   ├── __init__.py
│       │   └── base.py
│       ├── retrieval/
│       │   ├── __init__.py
│       │   ├── README.md
│       │   ├── models.py
│       │   ├── source.py
│       │   └── service.py
│       └── api/
│           ├── __init__.py
│           └── main.py
└── tests/
    ├── __init__.py
    ├── test_imports.py
    ├── test_config.py
    ├── test_trace.py
    ├── test_app.py
    ├── test_retrieval_models.py
    └── test_retrieval_service.py
```

## Running

From the repository root (where `pyproject.toml` lives):

```bash
uv sync --extra dev
uv run pytest 08_Development/implementation/tests -v
```
