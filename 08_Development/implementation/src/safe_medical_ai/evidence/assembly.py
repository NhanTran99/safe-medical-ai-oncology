"""RTEP Assembly boundary — Task #005.

Implements the locked B3 assembly/failure semantics (IR22) as one explicit,
testable function (B4-05): `assemble_runtime_evidence_package`.

Per spec section 7, this module:
- accepts a completed `RetrievalResponse` (+ caller-supplied runtime
  metadata/provenance) and performs a downstream transformation only;
- never constructs a `RepositorySource` or calls `RetrievalService` again;
- never re-retrieves, reranks, reorders, deduplicates, repairs missing
  provenance, enriches clinical content, calls an LLM, or generates
  prompts/responses.
"""

from __future__ import annotations

import logging
import uuid
from collections.abc import Sequence
from datetime import UTC, datetime

from ..retrieval import RetrievalOutcome, RetrievalResponse
from .models import (
    EvidenceItem,
    EvidenceItemProvenance,
    RTEPAssemblyContext,
    RTEPAssemblyOutcome,
    RTEPAssemblyResult,
    RuntimeEvidenceMetadata,
    RuntimeEvidencePackage,
)

logger = logging.getLogger(__name__)


def assemble_runtime_evidence_package(
    retrieval_response: RetrievalResponse,
    *,
    context: RTEPAssemblyContext | None,
    provenance: Sequence[EvidenceItemProvenance] | None = None,
) -> RTEPAssemblyResult:
    """Assemble a `RuntimeEvidencePackage` from a completed `RetrievalResponse`.

    Atomic (B3-11): returns exactly one outcome. `outcome == ASSEMBLED`
    implies a complete package; every other outcome implies no package.

    `context` carries the runtime metadata assembly cannot itself know
    (retrieval_id, navigation_context_id, retrieval_policy_version,
    knowledge_base_version) — pass `None` if it is unavailable, which
    deterministically produces `MISSING_METADATA` rather than an invented
    placeholder (spec sections 8.7 / 13).

    `provenance` supplies each evidence candidate's minimum provenance,
    **positionally parallel** to `retrieval_response.results`: item `i` of
    `provenance` belongs to candidate `i` of `retrieval_response.results`.

    Association is deliberately by index, not by `RetrievalCandidate.source_path`
    (Change Request RC-01): the locked upstream retrieval contract never
    establishes `source_path` as a unique evidence identity, so two distinct
    candidates may legitimately share the same `source_path` — keying a
    provenance mapping by `source_path` would then make their provenance
    unavoidably ambiguous (both would resolve to whichever entry occupied
    that key). Positional association keeps every candidate's provenance
    unambiguously one-to-one regardless of `source_path` duplication.

    A length mismatch (missing/extra provenance entries relative to
    `retrieval_response.results`) causes atomic assembly failure
    (`INCOMPLETE_PROVENANCE`) rather than a silently dropped/fabricated
    candidate (spec section 8.6/8.7).
    """
    request = retrieval_response.request

    if retrieval_response.outcome == RetrievalOutcome.NOT_FOUND:
        logger.info(
            "RTEP assembly: no package (retrieval NOT_FOUND) trace_id=%s",
            retrieval_response.trace_id,
        )
        return RTEPAssemblyResult(
            outcome=RTEPAssemblyOutcome.RETRIEVAL_NOT_FOUND,
            package=None,
            request=request,
            message="no RTEP: underlying retrieval outcome was NOT_FOUND",
        )

    if retrieval_response.outcome == RetrievalOutcome.INVALID_REQUEST:
        logger.info(
            "RTEP assembly: no package (retrieval INVALID_REQUEST) trace_id=%s",
            retrieval_response.trace_id,
        )
        return RTEPAssemblyResult(
            outcome=RTEPAssemblyOutcome.RETRIEVAL_INVALID_REQUEST,
            package=None,
            request=request,
            message="no RTEP: underlying retrieval outcome was INVALID_REQUEST",
        )

    # From here, retrieval_response.outcome is FOUND or EMPTY: assembly is
    # attempted (an EMPTY retrieval still requires valid metadata to produce
    # an empty-but-valid RTEP — spec section 8.2).
    if context is None:
        logger.warning(
            "RTEP assembly failed: missing required metadata trace_id=%s",
            retrieval_response.trace_id,
        )
        return RTEPAssemblyResult(
            outcome=RTEPAssemblyOutcome.MISSING_METADATA,
            package=None,
            request=request,
            message="no RTEP: required runtime metadata (RTEPAssemblyContext) was not supplied",
        )

    provenance_sequence = provenance if provenance is not None else ()

    if len(provenance_sequence) != len(retrieval_response.results):
        logger.warning(
            "RTEP assembly failed: provenance count (%d) does not match evidence count (%d) retrieval_id=%s",
            len(provenance_sequence),
            len(retrieval_response.results),
            context.retrieval_id,
        )
        return RTEPAssemblyResult(
            outcome=RTEPAssemblyOutcome.INCOMPLETE_PROVENANCE,
            package=None,
            request=request,
            message=(
                f"no RTEP: {len(provenance_sequence)} provenance entries supplied for "
                f"{len(retrieval_response.results)} evidence candidates"
            ),
        )

    evidence_items: list[EvidenceItem] = []

    for candidate, item_provenance in zip(retrieval_response.results, provenance_sequence, strict=True):
        if not candidate.source_path or not candidate.population_id:
            logger.warning(
                "RTEP assembly failed: invalid evidence item retrieval_id=%s navigation_context_id=%s",
                context.retrieval_id,
                context.navigation_context_id,
            )
            return RTEPAssemblyResult(
                outcome=RTEPAssemblyOutcome.INVALID_EVIDENCE_ITEM,
                package=None,
                request=request,
                message="no RTEP: a retrieval candidate failed minimum structural validation",
            )

        evidence_items.append(
            EvidenceItem(
                population_id=candidate.population_id,
                artifact_type=candidate.artifact_type,
                source_path=candidate.source_path,
                title=candidate.title,
                provenance=item_provenance,
            )
        )

    metadata = RuntimeEvidenceMetadata(
        evidence_package_id=uuid.uuid4().hex,
        retrieval_id=context.retrieval_id,
        navigation_context_id=context.navigation_context_id,
        retrieval_policy_version=context.retrieval_policy_version,
        knowledge_base_version=context.knowledge_base_version,
        generation_timestamp=datetime.now(UTC),
    )

    package = RuntimeEvidencePackage(metadata=metadata, evidence=tuple(evidence_items))

    logger.info(
        "RTEP assembled: evidence_package_id=%s retrieval_id=%s item_count=%d",
        metadata.evidence_package_id,
        context.retrieval_id,
        len(evidence_items),
    )

    return RTEPAssemblyResult(
        outcome=RTEPAssemblyOutcome.ASSEMBLED,
        package=package,
        request=request,
        message=None,
    )
