"""Evaluation Case resolution boundary — Phase 6 Stage 2 Track 2.

Public interface: `EvaluationCase`, `CaseResolutionOutcome`,
`CaseResolutionResult`, `EvaluationCaseResolver`, `CASE_ID_PATTERN`. See
`README.md` for the manifest-projection design and deferred scope.
"""

from .models import CaseResolutionOutcome, CaseResolutionResult, EvaluationCase
from .resolver import CASE_ID_PATTERN, EvaluationCaseResolver

__all__ = [
    "CASE_ID_PATTERN",
    "CaseResolutionOutcome",
    "CaseResolutionResult",
    "EvaluationCase",
    "EvaluationCaseResolver",
]
