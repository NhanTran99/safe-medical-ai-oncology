# Retrieval Foundation (Task #003 + Task #004)

## What this is

A deterministic, provider/engine-agnostic **navigation-first retrieval
foundation**. It implements the hierarchical resolution step of the approved
retrieval flow:

```text
controlled repository
        ↓
navigation-first retrieval          (RetrievalRequest.population_id)
        ↓
hierarchical resolution             (Population/PP -> Artifact, via RepositorySource)
        ↓
provenance / traceability           (RetrievalCandidate.source_path, .title)
        ↓
structured retrieval result         (RetrievalResponse)
```

It is **not** the semantic/vector retrieval implementation. No embeddings,
vector database, semantic-search engine, or LLM are used or referenced here.
See `TECH_STACK.md` §4 for the still-deferred technology choices this
foundation deliberately does not lock.

## Interfaces

- **`RetrievalRequest`** — navigation-first query: required `population_id`
  (e.g. `"PP-0001"`), optional `artifact_type` filter.
- **`RetrievalCandidate`** — one located artifact: `population_id`,
  `artifact_type`, `source_path` (provenance), optional `title`.
- **`RetrievalResponse`** — `outcome` (`RetrievalOutcome`), the echoed
  `request`, ordered `results`, `trace_id`, optional `message`.
- **`RetrievalOutcome`** — `FOUND` / `EMPTY` / `INVALID_REQUEST` /
  `NOT_FOUND`. This is retrieval-result vocabulary, deliberately **separate**
  from OUTPUT_CONTRACT's `ValidationOutcome` (`PASS` / `FAIL` /
  `SAFE_FALLBACK`), which governs a distinct, later concern — whether a
  *generated response* is eligible for delivery. The two vocabularies are not
  merged or reused for each other's purpose.
- **`RepositorySource`** (ABC) — the seam that keeps `RetrievalService`
  provider/engine agnostic. `list_artifacts(population_id)` returns the known
  artifacts for a population, or `None` if the population is not registered
  in the source at all.
- **`InMemoryRepositorySource`** — deterministic, fixture-backed
  `RepositorySource` for tests/local development. Performs no filesystem or
  network access and does not read the actual controlled repository.
- **`FilesystemRepositorySource`** (Task #004) — the first repository-backed
  `RepositorySource`. See "Filesystem-backed source" below.
- **`RetrievalService`** — orchestrator; `retrieve(request) -> RetrievalResponse`.
  Validates the request, resolves via the injected `RepositorySource`,
  applies hierarchical filtering, and returns a deterministically ordered
  result.

## Result semantics

| Condition | Outcome |
|---|---|
| `population_id` doesn't match the `PP-####` navigation format | `INVALID_REQUEST` |
| `population_id` well-formed but unknown to the source | `NOT_FOUND` |
| `population_id` known, but no artifacts match (after any `artifact_type` filter) | `EMPTY` |
| `population_id` known and at least one artifact matches | `FOUND` |

Ordering, when multiple artifacts are returned, is always canonical
`CKO -> KNOWLEDGE_PASSPORT -> PRIMARY_EVIDENCE_PACKAGE -> QA_REPORT`
(`artifact_type_sort_key`), independent of the order artifacts were
registered in the source.

## Usage

```python
from safe_medical_ai.retrieval import (
    ArtifactType,
    InMemoryRepositorySource,
    RetrievalCandidate,
    RetrievalRequest,
    RetrievalService,
)

source = InMemoryRepositorySource({
    "PP-0001": [
        RetrievalCandidate(
            population_id="PP-0001",
            artifact_type=ArtifactType.CKO,
            source_path="03_Clinical_Knowledge/population/population_packages/PP-0001/01_CKO.md",
        ),
    ],
})

service = RetrievalService(source)
response = service.retrieve(RetrievalRequest(population_id="PP-0001"))
# response.outcome == RetrievalOutcome.FOUND
```

## Filesystem-backed source (Task #004)

`FilesystemRepositorySource(source_root, *, provenance_prefix)` resolves
population/PP artifact locations under an explicit, configured `source_root`
directory boundary — e.g. it could be pointed at
`03_Clinical_Knowledge/population/population_packages/` in a real
deployment, or at a bounded temporary fixture tree in tests.

It performs **no proactive, whole-repository ingestion or indexing**: each
`list_artifacts(population_id)` call does one bounded, non-recursive lookup
scoped to `source_root` and, at most, one resolved PP directory beneath it.

Directory-name resolution (both conventions observed directly in the
controlled repository or used by this task's own fixtures, not invented):
1. **exact match** — a directory named exactly `population_id`;
2. **prefix match** — a directory named `"{population_id} — {title}"`,
   matching the real repository's `"PP-0001 — What_is_Cancer"` convention.
   Zero or ambiguous (>1) prefix matches resolve to "not found" rather than
   guessing.

Within a resolved PP directory, only the four canonical Gold artifact
filenames (`01_CKO.md` .. `04_QA_REPORT.md`, per
`FREEZE GOLD POPULATION PACKAGE SPECIFICATION v1.1.md`) are recognized. A
missing or malformed entry (e.g. a directory in place of a file) is skipped
deterministically — never fabricated.

`source_path` provenance is always `f"{provenance_prefix}/{pp_dir_name}/{filename}"`
— repository-relative, never an absolute local filesystem path.

A missing or unavailable `source_root` raises `RepositorySourceUnavailableError`
(checked at construction and again on every `list_artifacts` call) rather
than silently returning "not found" — a broken/missing source is a
configuration failure, distinct from a population genuinely being absent.

`list_artifacts` also independently re-validates `population_id` against the
same navigation-format pattern `RetrievalService` uses, so a caller invoking
`FilesystemRepositorySource` directly (bypassing `RetrievalService`) still
cannot path-traverse outside `source_root`.

Not wired into `api/main.py` or any default configuration by this task —
using it in a running service remains a later, explicitly authorized step.

## Deliberately deferred (not implemented by this task)

- Wiring `FilesystemRepositorySource` into the API layer or a default
  production configuration.
- Embeddings, vector database/engine, semantic-search provider, hybrid
  ranking.
- LLM provider/model integration.
- Navigation Context / clinical-domain selection (RAG_ARCHITECTURE.md's
  full navigation-first flow above the Population/PP level).
- Cross-population listing, pagination, or free-text query support.
- Assembly into the Runtime Evidence Package (EVIDENCE_PACKAGE_SPECIFICATION.md)
  — this foundation produces `RetrievalResponse`, not an Evidence Package.
- Clinical reasoning, safety logic, response generation, output validation.
