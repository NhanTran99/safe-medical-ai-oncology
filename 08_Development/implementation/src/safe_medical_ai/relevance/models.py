"""Typed Selected-PP Request Relevance contracts.

`RequestRelevanceOutcome` is a distinct vocabulary from every other
layer's outcome enum (the same isolation convention every prior boundary
in this codebase follows) -- never merged with `CaseResolutionOutcome`,
`CEROutcome`, `SafetyAction`, or any evidence/generation/validation
vocabulary. It answers exactly one narrow question: does the actual
submitted request text sufficiently relate to the PP the user has
already selected (identity already resolved by the existing, unchanged
`EvaluationCaseResolver`)? It is not a second case/PP authority, not a
239-way classifier, and not a safety/clinical judgment of any kind.
"""

from __future__ import annotations

from enum import Enum

from pydantic import BaseModel, ConfigDict, Field


class RequestRelevanceOutcome(str, Enum):
    """Controlled selected-PP request-relevance classification.

    `RELEVANT`: the request shares at least one significant term with the
    selected PP's own governed title/question text -- some evidence of
    relevance exists.

    `NOT_RELEVANT`: the request shares no significant term with the
    selected PP's own governed title/question text -- no evidence of
    relevance exists. Per the locked anti-force-mapping principle,
    absence of evidence is treated as insufficient evidence, not as a
    presumption of relevance.
    """

    RELEVANT = "RELEVANT"
    NOT_RELEVANT = "NOT_RELEVANT"


class RequestRelevanceResult(BaseModel):
    """The atomic result of one selected-PP relevance evaluation.

    `score` is retained only for internal traceability/logging (spec:
    "explainable at least through internal score/decision data") -- it is
    never returned to the browser and never displayed to the user (B11
    presents only the governed `outcome`-derived boundary text, never a
    raw internal score).
    """

    model_config = ConfigDict(frozen=True)

    outcome: RequestRelevanceOutcome
    score: float = Field(ge=0.0, le=1.0)
    message: str | None = None
