"""Selected-PP Request Relevance boundary.

Public interface: `RequestRelevanceOutcome`, `RequestRelevanceResult`,
`evaluate_request_relevance`, `REQUEST_NOT_RELEVANT_RESPONSE_TEXT`. See
`README.md` for the locked single-target design and threshold-calibration
status.
"""

from .models import RequestRelevanceOutcome, RequestRelevanceResult
from .resolver import REQUEST_NOT_RELEVANT_RESPONSE_TEXT, evaluate_request_relevance

__all__ = [
    "REQUEST_NOT_RELEVANT_RESPONSE_TEXT",
    "RequestRelevanceOutcome",
    "RequestRelevanceResult",
    "evaluate_request_relevance",
]
