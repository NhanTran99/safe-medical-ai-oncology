"""Controlled repository retrieval foundation (Task #003 + Task #004).

Public interface: `RetrievalRequest`, `RetrievalCandidate`, `RetrievalResponse`,
`RetrievalOutcome`, `ArtifactType`, `RepositorySource`, `InMemoryRepositorySource`,
`FilesystemRepositorySource`, `RepositorySourceError`,
`RepositorySourceUnavailableError`, `RetrievalService`. See `retrieval/README.md`
for usage and deferred scope.
"""

from .filesystem_source import (
    FilesystemRepositorySource,
    RepositorySourceError,
    RepositorySourceUnavailableError,
)
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
    "FilesystemRepositorySource",
    "InMemoryRepositorySource",
    "RepositorySource",
    "RepositorySourceError",
    "RepositorySourceUnavailableError",
    "RetrievalCandidate",
    "RetrievalOutcome",
    "RetrievalRequest",
    "RetrievalResponse",
    "RetrievalService",
    "artifact_type_sort_key",
]
