"""Deterministic Evaluation Case resolution — Phase 6 Stage 2 Track 2.

`EvaluationCaseResolver` is the sole mechanism by which a `case_id`
(`EC-0001`..`EC-0239`) resolves to an approved `population_id`
(AD-1 / AD-2). It is a static, manifest-projection-backed dictionary
lookup:

- deterministic: the same `case_id` always resolves to the same
  `population_id`;
- manifest-backed: every entry originates from the frozen Evaluation Case
  Manifest via a regenerable, auditable projection (see
  `scripts/generate_evaluation_case_manifest_projection.py` and
  `README.md`) — never a second, independently editable manifest;
- auditable: every resolved `EvaluationCase` carries the source manifest's
  identity, version, and hash;
- minimal: no LLM, no clinical reasoning, no dynamic PP inference, no
  patient state.

Fails closed: an unknown, malformed, or unresolvable `case_id` never falls
back to any specific case (including `EC-0002` / `PP-0002`) — it always
returns an explicit non-`RESOLVED` outcome.
"""

from __future__ import annotations

import json
import logging
import re
from pathlib import Path

from ..retrieval import ArtifactType
from .models import CaseResolutionOutcome, CaseResolutionResult, EvaluationCase

logger = logging.getLogger(__name__)

CASE_ID_PATTERN = re.compile(r"^EC-\d{4}$")


class EvaluationCaseResolver:
    """Resolves an approved `case_id` against the manifest projection.

    `projection_path` is an explicit, caller-supplied path (the same
    dependency-injection pattern `FilesystemRepositorySource` uses for its
    `source_root`) — this class never guesses or hardcodes a location.
    """

    def __init__(self, projection_path: Path):
        self._projection_path = Path(projection_path)
        self._cases: dict[str, EvaluationCase] | None = None
        self._load_error: str | None = None
        self._load()

    def _load(self) -> None:
        try:
            raw = json.loads(self._projection_path.read_text(encoding="utf-8"))
            source_manifest = raw["source_manifest"]
            source_manifest_version = raw["source_manifest_version"]
            source_manifest_sha256 = raw["source_manifest_sha256"]

            cases: dict[str, EvaluationCase] = {}
            for entry in raw["cases"]:
                case = EvaluationCase(
                    case_id=entry["case_id"],
                    population_id=entry["population_id"],
                    expected_primary_artifact_type=ArtifactType(entry["expected_primary_artifact_type"]),
                    source_manifest=source_manifest,
                    source_manifest_version=source_manifest_version,
                    source_manifest_sha256=source_manifest_sha256,
                )
                cases[case.case_id] = case
            self._cases = cases
        except Exception:
            logger.exception("EvaluationCaseResolver: failed to load manifest projection")
            self._cases = None
            self._load_error = f"manifest projection at '{self._projection_path}' could not be loaded"

    def resolve(self, case_id: str | None) -> CaseResolutionResult:
        """Return one authoritative `CaseResolutionResult`. Never raises."""
        if self._cases is None:
            logger.warning("Case resolution failed: projection unavailable")
            return CaseResolutionResult(
                outcome=CaseResolutionOutcome.PROJECTION_UNAVAILABLE,
                message=self._load_error or "manifest projection unavailable",
            )

        if case_id is None or not CASE_ID_PATTERN.match(case_id):
            logger.warning("Case resolution failed: malformed case_id=%r", case_id)
            return CaseResolutionResult(
                outcome=CaseResolutionOutcome.MALFORMED_CASE_ID,
                message=f"'{case_id}' is not a well-formed Evaluation Case identifier",
            )

        case = self._cases.get(case_id)
        if case is None:
            logger.warning("Case resolution failed: unknown case_id=%r", case_id)
            return CaseResolutionResult(
                outcome=CaseResolutionOutcome.UNKNOWN_CASE,
                message=f"'{case_id}' is not an approved Evaluation Case",
            )

        logger.info("Case resolution: RESOLVED case_id=%s population_id=%s", case.case_id, case.population_id)
        return CaseResolutionResult(outcome=CaseResolutionOutcome.RESOLVED, case=case)
