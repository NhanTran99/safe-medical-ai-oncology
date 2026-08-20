"""B07 durable execution-result capture.

Append-only JSON Lines (one `CampaignExecutionResult` per line). Chosen as
the smallest additive, dependency-free, structured, machine-readable
format consistent with this repository's existing convention of plain
JSON governed data files (e.g. `data/evaluation_case_manifest_projection.json`)
-- no database, queue, or new service boundary is introduced (Principle 8).

Append-only by construction (D10): `record_execution_result` only ever
opens the target file in append mode and writes one new line -- it never
seeks, rewrites, or deletes an existing line, so an existing recorded
outcome can never be silently overwritten by a later execution attempt.
A re-execution of the same `case_id` simply produces one more line with a
new `execution_id`.
"""

from __future__ import annotations

import logging
from pathlib import Path

from .models import CampaignExecutionResult, EvidenceCaptureOutcome

logger = logging.getLogger(__name__)


def record_execution_result(result: CampaignExecutionResult, path: Path) -> CampaignExecutionResult:
    """Durably append `result` to the JSON Lines file at `path`.

    Returns a copy of `result` with `evidence_capture_status` set to
    reflect what actually happened: `CAPTURED` only if the write to disk
    genuinely succeeded, `WRITE_FAILED` otherwise. `result` itself is
    frozen and is never mutated in place.

    Never raises on a write failure -- a capture failure is itself an
    observable, recorded outcome (DETECT), not something this function
    hides or retries (no automatic remediation, D05/D11).
    """
    try:
        path.parent.mkdir(parents=True, exist_ok=True)
        captured = result.model_copy(update={"evidence_capture_status": EvidenceCaptureOutcome.CAPTURED})
        with path.open("a", encoding="utf-8") as f:
            f.write(captured.model_dump_json())
            f.write("\n")
        return captured
    except OSError:
        logger.exception(
            "record_execution_result: failed to persist execution_id=%s to %s",
            result.execution_id,
            path,
        )
        return result.model_copy(update={"evidence_capture_status": EvidenceCaptureOutcome.WRITE_FAILED})


def read_execution_results(path: Path) -> list[CampaignExecutionResult]:
    """Read back every `CampaignExecutionResult` durably recorded at `path`.

    Returns an empty list if `path` does not exist yet -- reading before
    any execution has been recorded is not an error.
    """
    if not path.exists():
        return []

    results: list[CampaignExecutionResult] = []
    with path.open("r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            results.append(CampaignExecutionResult.model_validate_json(line))
    return results
