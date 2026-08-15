"""Controlled Evaluation Runtime (CER) typed orchestration contracts.

This package composes existing locked boundaries. It does not redefine
retrieval, evidence, integration, generation, safety, or validation rules.
"""

from __future__ import annotations

from enum import Enum

from pydantic import BaseModel, ConfigDict, Field

from ..evidence import EvidenceItemProvenance, RTEPAssemblyContext, RTEPAssemblyResult
from ..generation import GenerationResult
from ..integration import RuntimeConstraints, RuntimeIntegrationResult
from ..models.output_contract import NavigationContextPlaceholder
from ..retrieval import RetrievalRequest, RetrievalResponse
from ..safety import SafetyDecision, SafetyInput
from ..validation import ValidationResult


class CEROutcome(str, Enum):
    """Orchestration-level outcome vocabulary, distinct from all stage outcomes."""

    COMPLETED = "COMPLETED"
    SAFE_FALLBACK = "SAFE_FALLBACK"
    SAFETY_BLOCKED = "SAFETY_BLOCKED"
    RETRIEVAL_FAILURE = "RETRIEVAL_FAILURE"
    EVIDENCE_ASSEMBLY_FAILURE = "EVIDENCE_ASSEMBLY_FAILURE"
    INTEGRATION_FAILURE = "INTEGRATION_FAILURE"
    GENERATION_FAILURE = "GENERATION_FAILURE"
    VALIDATION_FAILURE = "VALIDATION_FAILURE"


class CERRequest(BaseModel):
    """All explicit inputs required to run one controlled CER attempt.

    No safety/risk decision is inferred by orchestration. No evidence
    provenance is synthesized. No provider is selected implicitly.
    """

    model_config = ConfigDict(frozen=True)

    request_id: str = Field(min_length=1)
    request_text: str = Field(min_length=1)
    retrieval_request: RetrievalRequest
    navigation_context: NavigationContextPlaceholder
    runtime_constraints: RuntimeConstraints
    rtep_context: RTEPAssemblyContext
    provenance: tuple[EvidenceItemProvenance, ...]
    safety_input: SafetyInput
    validation_policy_version: str = Field(min_length=1)


class CERResult(BaseModel):
    """Atomic snapshot of one CER orchestration attempt."""

    model_config = ConfigDict(frozen=True)

    outcome: CEROutcome
    safety_decision: SafetyDecision | None = None
    retrieval_response: RetrievalResponse | None = None
    assembly_result: RTEPAssemblyResult | None = None
    integration_result: RuntimeIntegrationResult | None = None
    generation_result: GenerationResult | None = None
    validation_result: ValidationResult | None = None
    message: str | None = None
