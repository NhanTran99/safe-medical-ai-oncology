"""Runtime Integration boundary — Task #006.

Public interface: `RuntimeIntegrationInput`, `RuntimeConstraints`,
`GenerationContext`, `EvidenceState`, `RuntimeIntegrationOutcome`,
`RuntimeIntegrationResult`, `integrate_runtime_context`.

Consumes an immutable Runtime Evidence Package (Task #005) plus explicit
runtime inputs and produces a typed `GenerationContext`. Does not implement
Generation, LLM invocation, output validation, or clinical reasoning. See
`integration/README.md` for the full contract and deferred scope.
"""

from .integration import integrate_runtime_context
from .models import (
    EvidenceState,
    GenerationContext,
    RuntimeConstraints,
    RuntimeIntegrationInput,
    RuntimeIntegrationOutcome,
    RuntimeIntegrationResult,
)

__all__ = [
    "EvidenceState",
    "GenerationContext",
    "RuntimeConstraints",
    "RuntimeIntegrationInput",
    "RuntimeIntegrationOutcome",
    "RuntimeIntegrationResult",
    "integrate_runtime_context",
]
