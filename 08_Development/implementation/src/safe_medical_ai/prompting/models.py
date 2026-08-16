"""Typed Governed Prompt Builder contracts — Track 3 BATCH 03.

Instantiates the LOCKED `PROMPTING_STRATEGY.md` as executable,
model-independent types: a `PromptSpecification` carrying the four locked
logical layers (System, Governance, Evidence, Communication — §7),
assembled only from already-governed upstream objects (Navigation Context,
Safety Decision, Evidence Package) — never re-derived, re-adjudicated, or
invented here.

`PromptBuilderOutcome` is a distinct new vocabulary — not merged with
`RetrievalOutcome`, `RTEPAssemblyOutcome`, `RuntimeIntegrationOutcome`, or
`GenerationOutcome` — per the project's established per-boundary isolation
convention.

Dependency direction: `prompting -> {evidence, retrieval, safety,
models.output_contract}`. Nothing in those modules is modified by this
package, and nothing here imports from `llm/`, `generation/`, `cer/`,
`integration/`, or `api/` — Prompt Builder is model-independent and does
not know about Generation's orchestration or any concrete provider.
"""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import Final

from pydantic import BaseModel, ConfigDict, Field

from ..evidence import EvidenceItemProvenance
from ..models.output_contract import NavigationContextPlaceholder
from ..retrieval import ArtifactType
from ..safety import RiskClass, SafetyAction

#: Stable Prompt Specification version (PROMPTING_STRATEGY.md §10).
#: Distinct from source_manifest_version / retrieval_policy_version /
#: knowledge_base_version -- identifies this Prompt Specification's own
#: structure/logic, never an upstream governed-content version.
PROMPT_SPECIFICATION_VERSION: Final[str] = "1.0"

#: System Layer operational-context statement (PROMPTING_STRATEGY.md §7) --
#: reused verbatim from the boundary object already shipped in
#: `api/main.py`'s `/cer/evaluate` response, not a newly invented claim.
SYSTEM_LAYER_MODE: Final[str] = "RESEARCH / DEVELOPMENT / CONTROLLED EVALUATION ONLY"
SYSTEM_LAYER_FORMAL_VALIDATION: Final[str] = "NOT STARTED"
SYSTEM_LAYER_EXECUTION_AUTHORIZATION: Final[str] = "NOT GRANTED"
SYSTEM_LAYER_VC_CLIN: Final[str] = "DEFERRED"


class PromptBuilderOutcome(str, Enum):
    """Controlled Prompt Builder result classification (Prompt Contract, §12)."""

    BUILT = "BUILT"
    MISSING_NAVIGATION_CONTEXT = "MISSING_NAVIGATION_CONTEXT"
    MISSING_SAFETY_DECISION = "MISSING_SAFETY_DECISION"
    MISSING_EVIDENCE_PACKAGE = "MISSING_EVIDENCE_PACKAGE"


class SystemLayer(BaseModel):
    """System identity / operational context (PROMPTING_STRATEGY.md §7)."""

    model_config = ConfigDict(frozen=True)

    mode: str
    formal_validation: str
    execution_authorization: str
    vc_clin: str


class GovernanceLayer(BaseModel):
    """Permissions/restrictions/safety requirements (§7), derived unchanged
    from the supplied SafetyDecision -- never independently re-adjudicated."""

    model_config = ConfigDict(frozen=True)

    decision_id: str = Field(min_length=1)
    risk_class: RiskClass
    action: SafetyAction
    reason_code: str = Field(min_length=1)


class EvidenceLayerItem(BaseModel):
    """One governed evidence item as carried into the prompt (§7/§11:
    Evidence Package). Identity/provenance preserved for traceability;
    `content` is the actual governed clinical text (Track 3 BATCH 01)."""

    model_config = ConfigDict(frozen=True)

    population_id: str
    artifact_type: ArtifactType
    title: str | None
    content: str | None
    provenance: EvidenceItemProvenance


class EvidenceLayer(BaseModel):
    """Evidence Package content (§7). Order preserved exactly as supplied."""

    model_config = ConfigDict(frozen=True)

    items: tuple[EvidenceLayerItem, ...] = Field(default_factory=tuple)


class CommunicationLayer(BaseModel):
    """Patient-centered communication style / educational presentation
    (§7). The locked strategy defines no additional concrete requirement
    beyond carrying the user's question and the supplied Navigation
    Context unchanged (§13's Response Composition is explicitly
    illustrative, not mandated -- not instantiated here)."""

    model_config = ConfigDict(frozen=True)

    request_text: str = Field(min_length=1)
    navigation_context: NavigationContextPlaceholder


class PromptRecord(BaseModel):
    """Minimum traceability record (PROMPTING_STRATEGY.md §11).

    `navigation_context_reference` exists because the locked Prompt
    Strategy requires Navigation Context traceability alongside the Safety
    Decision and Evidence Package identifiers below. Its current value is
    `None` under the present, locked upstream contract -- an explicit
    representation of "no identifier is available", never a fabricated
    one. This does not mean Navigation Context was rejected or ignored by
    the Prompt Builder (it is still a required, checked input — see
    `PromptBuilderOutcome.MISSING_NAVIGATION_CONTEXT`); it means
    `NavigationContextPlaceholder` (`models/output_contract.py`) currently
    carries no identifier of its own to reference. This field is not
    authorization to add one: `NavigationContextPlaceholder` remains
    unchanged and out of scope for this module. A future, separately
    approved Navigation Context contract can populate this same field
    without any change to `PromptRecord`'s shape or the Prompt Builder
    contract.
    """

    model_config = ConfigDict(frozen=True)

    prompt_version: str = Field(min_length=1)
    navigation_context_reference: str | None = Field(
        description=(
            "The Navigation Context's own identifier, when one exists. `None` "
            "under the current locked NavigationContextPlaceholder contract "
            "(no identifier available) -- not a fabricated value, and not a "
            "sign the Prompt Builder skipped or rejected Navigation Context."
        )
    )
    safety_decision_id: str = Field(min_length=1)
    evidence_package_id: str = Field(min_length=1)
    generation_timestamp: datetime


class PromptSpecification(BaseModel):
    """The immutable governed Prompt Specification (PROMPTING_STRATEGY.md
    §5-§7), model-independent -- carries no vendor/model-specific shape."""

    model_config = ConfigDict(frozen=True)

    system: SystemLayer
    governance: GovernanceLayer
    evidence: EvidenceLayer
    communication: CommunicationLayer
    record: PromptRecord


class PromptBuilderResult(BaseModel):
    """The atomic result of one `build_prompt` call.

    `outcome == BUILT` if and only if `specification` is the one complete
    `PromptSpecification` produced; every other outcome implies
    `specification is None` -- the Prompt Builder never returns a partial
    specification (Prompt Contract, §12).
    """

    model_config = ConfigDict(frozen=True)

    outcome: PromptBuilderOutcome
    specification: PromptSpecification | None = None
    message: str | None = None
