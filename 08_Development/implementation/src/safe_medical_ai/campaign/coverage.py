"""B10 coverage/reproducibility aggregation.

Pure, read-only reporting over already-recorded `CampaignExecutionResult`
data (typically the output of `capture.read_execution_results()`). This
module implements NO execution, retrieval, evidence, provider, or
validation logic of its own -- it only counts values already present on
records it is given.

It never re-executes a case, never reads a results file itself, and never
infers, estimates, or projects a result for any case_id/population_id
that is not present in the records it was handed. It makes no
representative/exhaustive coverage claim and no clinical-quality
judgment -- only plain tallies of the existing, already-governed outcome
vocabularies (`CaseResolutionOutcome`, `CEROutcome`,
`CandidateValidationOutcome`), unchanged and unmerged, per the same
isolation convention every other boundary in this codebase follows.
"""

from __future__ import annotations

from collections import Counter
from collections.abc import Sequence

from pydantic import BaseModel, ConfigDict

from .models import CampaignExecutionResult


class CampaignCoverageSummary(BaseModel):
    """Read-only aggregate over a supplied set of `CampaignExecutionResult`s.

    Every count is a plain tally over exactly the records supplied -- not
    a projection, estimate, or claim about any case NOT present in that
    set. Whether the supplied records constitute representative or
    exhaustive coverage of the governed 239-PP population is a
    governance/strategy question this summary neither answers nor implies
    an answer to.
    """

    model_config = ConfigDict(frozen=True)

    total_execution_records: int
    distinct_case_ids: int
    distinct_population_ids: int
    case_resolution_outcome_counts: dict[str, int]
    cer_outcome_counts: dict[str, int]
    validation_outcome_counts: dict[str, int]


def summarize_campaign_coverage(
    results: Sequence[CampaignExecutionResult],
) -> CampaignCoverageSummary:
    """Aggregate coverage/outcome counts over already-recorded results.

    `results` is typically `capture.read_execution_results(path)`'s
    return value, but this function itself never reads a file -- it is
    pure over whatever sequence it is given, so it can equally summarize
    a subset, a single run's output, or a combined set from multiple
    output files a caller has already merged.

    `resolved_population_id` entries that are `None` (case resolution
    failed, so no PP was ever reached) are excluded from
    `distinct_population_ids` -- counting `None` as a "population" would
    misrepresent coverage of the governed PP surface.
    """
    case_ids = {result.case_id for result in results}
    population_ids = {
        result.resolved_population_id
        for result in results
        if result.resolved_population_id is not None
    }

    return CampaignCoverageSummary(
        total_execution_records=len(results),
        distinct_case_ids=len(case_ids),
        distinct_population_ids=len(population_ids),
        case_resolution_outcome_counts=dict(
            Counter(result.case_resolution_outcome.value for result in results)
        ),
        cer_outcome_counts=dict(
            Counter(result.cer_outcome.value for result in results if result.cer_outcome is not None)
        ),
        validation_outcome_counts=dict(
            Counter(
                result.validation_outcome.value
                for result in results
                if result.validation_outcome is not None
            )
        ),
    )
