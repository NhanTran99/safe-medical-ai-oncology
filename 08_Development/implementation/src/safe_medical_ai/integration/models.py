"""Typed Runtime Integration contracts — Task #006.

Implements the locked B1-B4 decision set: the Runtime Integration boundary
consumes an immutable Runtime Evidence Package (Task #005) plus explicit
runtime inputs, and produces a typed `GenerationContext` for a future
Generation layer. This module defines no Generation, LLM, validation, or
clinical-reasoning behavior — only the typed contracts and their
construction rules live here (construction logic lives in `integration.py`).

Dependency direction (locked): `integration -> evidence -> retrieval`.
Nothing in `retrieval/` or `evidence/` is modified by this module.
"""

from __future__ import annotations

from datetime import datetime
from enum import Enum

from pydantic import BaseModel, ConfigDict, Field

from ..evidence import RuntimeEvidencePackage
from ..models.output_contract import NavigationContextPlaceholder


class RuntimeConstraints(BaseModel):
    """Structural placeholder for applicable runtime/delivery constraints.

    Field-level schema for response/delivery constraints is explicitly
    deferred (OUTPUT_CONTRACT.md section 11), the same way
    `NavigationContextPlaceholder` deferred Navigation Context schema in
    Task #002. This module only needs to prove constraints are explicitly
    carried through integration unchanged (section 7); it does not need to
    interpret their content, so no fields are added here without a
    separate, approved specification.
    """

    model_config = ConfigDict(frozen=True)


class EvidenceState(str, Enum):
    """Explicit evidence-presence state carried on `GenerationContext`.

    Distinct from `RetrievalOutcome` and `RTEPAssemblyOutcome` — this is a
    third, narrower vocabulary describing only whether the RTEP embedded in
    a successfully constructed `GenerationContext` has any evidence items,
    so a caller holding only the `GenerationContext` does not need to
    re-inspect `rtep.evidence` length to make the same distinction section
    6.2 requires downstream.
    """

    HAS_EVIDENCE = "HAS_EVIDENCE"
    EMPTY = "EMPTY"


class RuntimeIntegrationOutcome(str, Enum):
    """Controlled Runtime Integration result classification.

    A distinct vocabulary from `RetrievalOutcome`, `RTEPAssemblyOutcome`,
    and OUTPUT_CONTRACT's `ValidationOutcome` — never merged with any of
    them (same isolation principle as Task #005's `RTEPAssemblyOutcome`).
    """

    INTEGRATED = "INTEGRATED"
    EMPTY_EVIDENCE = "EMPTY_EVIDENCE"
    INVALID_INPUT = "INVALID_INPUT"
    MISSING_RTEP = "MISSING_RTEP"
    INTEGRATION_FAILURE = "INTEGRATION_FAILURE"


class RuntimeIntegrationInput(BaseModel):
    """Explicit runtime inputs required to attempt Runtime Integration.

    `rtep` is `None` to represent "no Runtime Evidence Package available"
    (spec section 6.3 / `MISSING_RTEP`) — the caller must construct this
    object either way; integration never re-retrieves to obtain one.
    """

    model_config = ConfigDict(frozen=True)

    request_text: str = Field(min_length=1, description="The user request/intent.")
    navigation_context: NavigationContextPlaceholder
    rtep: RuntimeEvidencePackage | None
    runtime_constraints: RuntimeConstraints


class GenerationContext(BaseModel):
    """The immutable, derived context handed to a future Generation layer.

    A derived orchestration/context object, not a second evidence
    authority (spec section 4.2): `rtep` is the same immutable
    `RuntimeEvidencePackage` object produced by RTEP Assembly, referenced
    here rather than copied or reconstructed.
    """

    model_config = ConfigDict(frozen=True)

    integration_id: str = Field(min_length=1)
    integration_timestamp: datetime
    request_text: str
    navigation_context: NavigationContextPlaceholder
    rtep: RuntimeEvidencePackage
    runtime_constraints: RuntimeConstraints
    evidence_state: EvidenceState


class RuntimeIntegrationResult(BaseModel):
    """The atomic result of one `integrate_runtime_context` call.

    `outcome in {INTEGRATED, EMPTY_EVIDENCE}` if and only if `context` is a
    complete, valid `GenerationContext`; every other outcome implies
    `context is None` — integration never returns a partially valid
    context (spec sections 4.4 / 6.5).
    """

    model_config = ConfigDict(frozen=True)

    outcome: RuntimeIntegrationOutcome
    context: GenerationContext | None = None
    message: str | None = None
