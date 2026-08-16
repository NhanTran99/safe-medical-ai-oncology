"""Governed Prompt Builder — Track 3 BATCH 03.

Public interface: `PromptSpecification`, `SystemLayer`, `GovernanceLayer`,
`EvidenceLayer`, `EvidenceLayerItem`, `CommunicationLayer`, `PromptRecord`,
`PromptBuilderOutcome`, `PromptBuilderResult`, `PROMPT_SPECIFICATION_VERSION`,
`build_prompt`.

Instantiates the LOCKED `PROMPTING_STRATEGY.md` as an executable,
model-independent component. Does not implement Generation, LLM invocation,
retrieval, evidence loading, or safety adjudication. See `builder.py`,
`models.py`, and `README.md` for the full contract and deferred scope.
"""

from .builder import build_prompt
from .models import (
    PROMPT_SPECIFICATION_VERSION,
    CommunicationLayer,
    EvidenceLayer,
    EvidenceLayerItem,
    GovernanceLayer,
    PromptBuilderOutcome,
    PromptBuilderResult,
    PromptRecord,
    PromptSpecification,
    SystemLayer,
)

__all__ = [
    "PROMPT_SPECIFICATION_VERSION",
    "CommunicationLayer",
    "EvidenceLayer",
    "EvidenceLayerItem",
    "GovernanceLayer",
    "PromptBuilderOutcome",
    "PromptBuilderResult",
    "PromptRecord",
    "PromptSpecification",
    "SystemLayer",
    "build_prompt",
]
