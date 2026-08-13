# Retrieval Foundation (Task #003)

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
- **`InMemoryRepositorySource`** — the only concrete `RepositorySource`
  shipped by this task: a deterministic, fixture-backed implementation for
  tests/local development. It performs no filesystem or network access and
  does not read the actual controlled repository.
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

## Deliberately deferred (not implemented by this task)

- A real filesystem- or database-backed `RepositorySource` that reads the
  actual controlled `03_Clinical_Knowledge/population/population_packages/`
  content. Only the fixture-backed `InMemoryRepositorySource` exists so far;
  autonomous ingestion of the real 239-PP repository is explicitly out of
  scope for Task #003.
- Embeddings, vector database/engine, semantic-search provider, hybrid
  ranking.
- LLM provider/model integration.
- Navigation Context / clinical-domain selection (RAG_ARCHITECTURE.md's
  full navigation-first flow above the Population/PP level).
- Cross-population listing, pagination, or free-text query support.
- Assembly into the Runtime Evidence Package (EVIDENCE_PACKAGE_SPECIFICATION.md)
  — this foundation produces `RetrievalResponse`, not an Evidence Package.
- Clinical reasoning, safety logic, response generation, output validation.
