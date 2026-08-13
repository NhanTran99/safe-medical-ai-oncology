"""Navigation-first retrieval orchestrator for the Task #003 foundation.

`RetrievalService` implements:
- navigation-first retrieval: `population_id` is a required, explicit
  navigation key (no free-text/semantic query in this foundation);
- hierarchical resolution: Repository -> Population/PP -> Artifact, via
  `RepositorySource.list_artifacts` followed by optional `artifact_type`
  filtering;
- deterministic ordering: results are always sorted into canonical
  01..04 artifact order;
- explicit, deterministic result semantics (FOUND / EMPTY /
  INVALID_REQUEST / NOT_FOUND) instead of exceptions for expected
  domain conditions.

`RetrievalService` depends only on the `RepositorySource` abstraction, so it
remains provider/engine agnostic: swapping in a different `RepositorySource`
implementation (e.g. a future filesystem-backed or hybrid/semantic source)
does not require changing this class or its callers.
"""

from __future__ import annotations

import re

from ..trace import get_trace_id
from .models import RetrievalOutcome, RetrievalRequest, RetrievalResponse, artifact_type_sort_key
from .source import RepositorySource

_POPULATION_ID_PATTERN = re.compile(r"^PP-\d{4}$")


class RetrievalService:
    """Deterministic navigation-first retrieval orchestrator."""

    def __init__(self, source: RepositorySource):
        self._source = source

    def retrieve(self, request: RetrievalRequest) -> RetrievalResponse:
        trace_id = get_trace_id()

        if not _POPULATION_ID_PATTERN.match(request.population_id):
            return RetrievalResponse(
                outcome=RetrievalOutcome.INVALID_REQUEST,
                request=request,
                results=[],
                trace_id=trace_id,
                message=(
                    f"population_id '{request.population_id}' does not match "
                    "the required 'PP-####' navigation format"
                ),
            )

        artifacts = self._source.list_artifacts(request.population_id)

        if artifacts is None:
            return RetrievalResponse(
                outcome=RetrievalOutcome.NOT_FOUND,
                request=request,
                results=[],
                trace_id=trace_id,
                message=f"population_id '{request.population_id}' was not found in the repository source",
            )

        if request.artifact_type is not None:
            artifacts = [a for a in artifacts if a.artifact_type == request.artifact_type]

        ordered = sorted(artifacts, key=lambda candidate: artifact_type_sort_key(candidate.artifact_type))

        if not ordered:
            return RetrievalResponse(
                outcome=RetrievalOutcome.EMPTY,
                request=request,
                results=[],
                trace_id=trace_id,
                message="no matching artifacts were found for the given request",
            )

        return RetrievalResponse(
            outcome=RetrievalOutcome.FOUND,
            request=request,
            results=ordered,
            trace_id=trace_id,
            message=None,
        )
