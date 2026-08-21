"""B07 execution/evidence preparation layer, with B10 coverage/reproducibility
aggregation.

Public interface: `execute_case`, `record_execution_result`,
`read_execution_results`, `CampaignExecutionResult`, `EvidenceCaptureOutcome`,
`CampaignCoverageSummary`, `summarize_campaign_coverage`.

This package implements no CER, retrieval, evidence, prompt, provider, or
validation logic of its own -- it only invokes the existing governed
execution path once per approved `case_id` (`harness.py`), durably records
what happened (`capture.py`), and aggregates already-recorded results
(`coverage.py`). See `README.md` for the full boundary and non-authority
statement.
"""

from .capture import read_execution_results, record_execution_result
from .coverage import CampaignCoverageSummary, summarize_campaign_coverage
from .harness import execute_case
from .models import CampaignExecutionResult, EvidenceCaptureOutcome

__all__ = [
    "CampaignCoverageSummary",
    "CampaignExecutionResult",
    "EvidenceCaptureOutcome",
    "execute_case",
    "read_execution_results",
    "record_execution_result",
    "summarize_campaign_coverage",
]
