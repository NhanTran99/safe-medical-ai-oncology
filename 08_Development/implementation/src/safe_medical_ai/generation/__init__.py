"""Generation boundary — Task #007.

Public interface: `CandidateResponse`, `GenerationOutcome`, `GenerationResult`,
`ProviderGenerationRequest`, `EMPTY_EVIDENCE_POLICY_RESPONSE_TEXT`,
`generate_candidate_response`, `ProviderError`, `ProviderTimeoutError`,
`ProviderPartialOutputError`.

Consumes an authoritative `GenerationContext` (Task #006) plus an explicit
`LLMAdapter` provider (Task #002) and produces a typed `CandidateResponse`,
never labeled final/clinically validated/safety approved/citation verified.
The provider receives the authoritative governed evidence from
`GenerationContext.rtep` via `ProviderGenerationRequest`, not only raw
request text. Does not implement Validation, clinical reasoning, or safety
adjudication. See `generation/README.md` for the full contract, the locked
EMPTY_EVIDENCE policy, and deferred scope.
"""

from .generation import (
    ProviderError,
    ProviderPartialOutputError,
    ProviderTimeoutError,
    generate_candidate_response,
)
from .models import (
    EMPTY_EVIDENCE_POLICY_RESPONSE_TEXT,
    CandidateResponse,
    GenerationOutcome,
    GenerationResult,
    ProviderGenerationRequest,
)

__all__ = [
    "EMPTY_EVIDENCE_POLICY_RESPONSE_TEXT",
    "CandidateResponse",
    "GenerationOutcome",
    "GenerationResult",
    "ProviderError",
    "ProviderGenerationRequest",
    "ProviderPartialOutputError",
    "ProviderTimeoutError",
    "generate_candidate_response",
]
