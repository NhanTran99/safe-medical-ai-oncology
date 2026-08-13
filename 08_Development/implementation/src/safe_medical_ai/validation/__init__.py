"""Validation boundary — Task #008.

Public interface: `ValidationInput`, `ValidationResult`,
`CandidateValidationOutcome`, `validate_candidate_response`.

Consumes a `CandidateResponse` (Task #007) plus the authoritative
RTEP/evidence context and produces a typed `ValidationResult`. `VALID`
means only that a `CandidateResponse` satisfies the locked Validation
contract — never that it is clinically safe, diagnostically correct, or
finally approved. Does not implement retrieval, generation, clinical
reasoning, or final delivery/approval. See `validation/README.md` for the
full contract, failure semantics, and deferred scope.
"""

from .models import CandidateValidationOutcome, ValidationInput, ValidationResult
from .validation import validate_candidate_response

__all__ = [
    "CandidateValidationOutcome",
    "ValidationInput",
    "ValidationResult",
    "validate_candidate_response",
]
