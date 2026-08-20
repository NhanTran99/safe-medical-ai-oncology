"""B07 execution/evidence preparation layer.

Public interface: `execute_case`, `record_execution_result`,
`read_execution_results`, `CampaignExecutionResult`, `EvidenceCaptureOutcome`.

This package implements no CER, retrieval, evidence, prompt, provider, or
validation logic of its own -- it only invokes the existing governed
execution path once per approved `case_id` (`harness.py`) and durably
records what happened (`capture.py`). See `README.md` for the full
boundary and non-authority statement.
"""

from .capture import read_execution_results, record_execution_result
from .harness import execute_case
from .models import CampaignExecutionResult, EvidenceCaptureOutcome

__all__ = [
    "CampaignExecutionResult",
    "EvidenceCaptureOutcome",
    "execute_case",
    "read_execution_results",
    "record_execution_result",
]
