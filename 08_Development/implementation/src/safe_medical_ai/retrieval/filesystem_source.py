"""Filesystem-backed `RepositorySource` (Task #004).

Resolves population/PP artifact locations under an explicit, configured
`source_root` boundary. This class performs no proactive, whole-repository
ingestion or indexing: each `list_artifacts` call does a single, bounded,
non-recursive lookup scoped to `source_root` and (at most) one resolved PP
directory beneath it.

Directory-naming compatibility (both observed in the controlled repository
and used directly by this implementation, not invented):
- exact match: a directory named exactly `population_id` (used by this
  task's test fixtures for simplicity and determinism);
- prefix match: a directory named `"{population_id} — {title}"`, matching
  the naming convention actually used under
  `03_Clinical_Knowledge/population/population_packages/` (e.g.
  `"PP-0001 — What_is_Cancer"`).

Canonical artifact filenames (`01_CKO.md` .. `04_QA_REPORT.md`) are the
controlled Gold Population Package filenames defined by
`FREEZE GOLD POPULATION PACKAGE SPECIFICATION v1.1.md` and observed
directly in the repository; they are not invented by this module.
"""

from __future__ import annotations

from pathlib import Path

from .models import POPULATION_ID_PATTERN, ArtifactType, RetrievalCandidate
from .source import RepositorySource

_ARTIFACT_FILENAMES: dict[str, ArtifactType] = {
    "01_CKO.md": ArtifactType.CKO,
    "02_KNOWLEDGE_PASSPORT.md": ArtifactType.KNOWLEDGE_PASSPORT,
    "03_PRIMARY_EVIDENCE_PACKAGE.md": ArtifactType.PRIMARY_EVIDENCE_PACKAGE,
    "04_QA_REPORT.md": ArtifactType.QA_REPORT,
}

_TITLE_SEPARATOR = " — "


class RepositorySourceError(Exception):
    """Base class for RepositorySource configuration/availability failures."""


class RepositorySourceUnavailableError(RepositorySourceError):
    """Raised when the configured source root does not exist or is not a directory.

    This is a configuration/availability failure, distinct from a retrieval
    outcome (NOT_FOUND / EMPTY apply to a *population*, not to the source
    itself being unusable) — it is raised rather than silently returning
    `None`, so a missing source root is never mistaken for "population not
    registered".
    """


class FilesystemRepositorySource(RepositorySource):
    """`RepositorySource` backed by an explicit, configured directory boundary."""

    def __init__(self, source_root: Path, *, provenance_prefix: str):
        self._source_root = Path(source_root)
        self._provenance_prefix = provenance_prefix.rstrip("/")
        self._require_available()

    def _require_available(self) -> None:
        if not self._source_root.is_dir():
            raise RepositorySourceUnavailableError(
                f"repository source root '{self._source_root}' does not exist or is not a directory"
            )

    def list_artifacts(self, population_id: str) -> list[RetrievalCandidate] | None:
        self._require_available()

        # Defense in depth: never join an unsafe/malformed identifier onto a
        # filesystem path, even if a caller bypasses RetrievalService's own
        # navigation-format validation.
        if not POPULATION_ID_PATTERN.match(population_id):
            return None

        population_dir = self._resolve_population_dir(population_id)
        if population_dir is None:
            return None

        candidates: list[RetrievalCandidate] = []
        title = self._extract_title(population_dir, population_id)

        for filename, artifact_type in _ARTIFACT_FILENAMES.items():
            artifact_path = population_dir / filename
            if not artifact_path.is_file():
                # Missing or malformed (e.g. a directory in its place)
                # artifact: skip deterministically rather than fabricate it.
                continue
            try:
                content = artifact_path.read_text(encoding="utf-8")
            except OSError:
                # Unreadable despite passing is_file() (e.g. a permissions
                # error or a removal race): the same "skip deterministically
                # rather than fabricate it" principle applies as above —
                # never substitute fabricated/partial content.
                continue
            candidates.append(
                RetrievalCandidate(
                    population_id=population_id,
                    artifact_type=artifact_type,
                    source_path=f"{self._provenance_prefix}/{population_dir.name}/{filename}",
                    title=title,
                    content=content,
                )
            )

        return candidates

    def _resolve_population_dir(self, population_id: str) -> Path | None:
        exact = self._source_root / population_id
        if exact.is_dir():
            return exact

        prefix = f"{population_id}{_TITLE_SEPARATOR}"
        matches = [
            entry
            for entry in self._source_root.iterdir()
            if entry.is_dir() and entry.name.startswith(prefix)
        ]

        # Zero or ambiguous (>1) matches are treated as unresolved rather
        # than guessing which directory was intended.
        if len(matches) == 1:
            return matches[0]
        return None

    @staticmethod
    def _extract_title(population_dir: Path, population_id: str) -> str | None:
        if population_dir.name == population_id:
            return None
        _, _, remainder = population_dir.name.partition(_TITLE_SEPARATOR)
        return remainder or None
