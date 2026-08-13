"""Repository-source abstraction for the Task #003 retrieval foundation.

`RepositorySource` is the seam that keeps `RetrievalService` provider/engine
agnostic. Later hybrid/semantic retrieval, or a real filesystem/database-backed
implementation, can be introduced as additional `RepositorySource`
implementations without changing the retrieval contract or the service.

Only a deterministic, fixture-backed implementation
(`InMemoryRepositorySource`) is provided by this task. A real
repository-reading implementation is explicitly deferred — see
`retrieval/README.md`.
"""

from __future__ import annotations

from abc import ABC, abstractmethod

from .models import RetrievalCandidate


class RepositorySource(ABC):
    """Abstraction over where controlled repository artifacts are located."""

    @abstractmethod
    def list_artifacts(self, population_id: str) -> list[RetrievalCandidate] | None:
        """Return all known artifacts for `population_id`.

        Returns `None` if `population_id` is not registered in this source
        at all (distinct from an empty list, which means the population is
        known but currently has no matching artifacts).
        """
        raise NotImplementedError


class InMemoryRepositorySource(RepositorySource):
    """Deterministic, fixture-backed `RepositorySource`.

    Intended for tests and local development only. Populations/artifacts are
    supplied explicitly by the caller; this class performs no filesystem or
    network access and does not read the actual controlled repository.
    """

    def __init__(self, populations: dict[str, list[RetrievalCandidate]]):
        self._populations = populations

    def list_artifacts(self, population_id: str) -> list[RetrievalCandidate] | None:
        return self._populations.get(population_id)
