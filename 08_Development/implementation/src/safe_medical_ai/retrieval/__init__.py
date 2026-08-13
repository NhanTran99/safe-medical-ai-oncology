"""Task #003 controlled repository retrieval foundation.

Public interface: `RetrievalRequest`, `RetrievalCandidate`, `RetrievalResponse`,
`RetrievalOutcome`, `ArtifactType`, `RepositorySource`, `InMemoryRepositorySource`,
`RetrievalService`. See `retrieval/README.md` for usage and deferred scope.
"""

from .models import (
    ArtifactType,
    RetrievalCandidate,
    RetrievalOutcome,
    RetrievalRequest,
    RetrievalResponse,
    artifact_type_sort_key,
)
from .service import RetrievalService
from .source import InMemoryRepositorySource, RepositorySource

__all__ = [
    "ArtifactType",
    "InMemoryRepositorySource",
    "RepositorySource",
    "RetrievalCandidate",
    "RetrievalOutcome",
    "RetrievalRequest",
    "RetrievalResponse",
    "RetrievalService",
    "artifact_type_sort_key",
]
