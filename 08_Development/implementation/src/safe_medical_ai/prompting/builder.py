"""Governed Prompt Builder — Track 3 BATCH 03.

Instantiates the LOCKED `PROMPTING_STRATEGY.md` as one explicit,
deterministic entry point: `build_prompt`. Model-independent: imports
nothing from `llm/`, `generation/`, `cer/`, `integration/`, or `api/`, and
knows nothing about any concrete provider/vendor/model.

Per PROMPTING_STRATEGY.md §12 (Prompt Contract), Navigation Context, Safety
Decision, and Evidence Package are all mandatory: any one missing/empty
blocks prompt construction entirely (no partial/best-effort
`PromptSpecification` is ever returned) — the same atomic-result convention
every other boundary in this codebase already uses (`RTEPAssemblyResult`,
`RuntimeIntegrationResult`, `GenerationResult`).

Never retrieves evidence, touches the filesystem, accesses the Gold
Population Package corpus or Knowledge Source Registry, adjudicates safety,
modifies evidence, or invents clinical knowledge — consumes only the
already-governed objects it is given, unchanged.
"""

from __future__ import annotations

import logging
from datetime import UTC, datetime

from ..evidence import RuntimeEvidencePackage
from ..models.output_contract import NavigationContextPlaceholder
from ..safety import SafetyDecision
from .models import (
    PROMPT_SPECIFICATION_VERSION,
    SYSTEM_LAYER_EXECUTION_AUTHORIZATION,
    SYSTEM_LAYER_FORMAL_VALIDATION,
    SYSTEM_LAYER_MODE,
    SYSTEM_LAYER_VC_CLIN,
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

logger = logging.getLogger(__name__)


def build_prompt(
    *,
    navigation_context: NavigationContextPlaceholder | None,
    safety_decision: SafetyDecision | None,
    evidence_package: RuntimeEvidencePackage | None,
    request_text: str,
) -> PromptBuilderResult:
    """Build one governed `PromptSpecification`, or block deterministically.

    Atomic: `outcome == BUILT` implies a complete `PromptSpecification`;
    every other outcome implies `specification is None`.
    """
    if navigation_context is None:
        logger.warning("Prompt construction blocked: missing Navigation Context")
        return PromptBuilderResult(
            outcome=PromptBuilderOutcome.MISSING_NAVIGATION_CONTEXT,
            message="no PromptSpecification: Navigation Context was not supplied",
        )

    if safety_decision is None:
        logger.warning("Prompt construction blocked: missing Safety Decision")
        return PromptBuilderResult(
            outcome=PromptBuilderOutcome.MISSING_SAFETY_DECISION,
            message="no PromptSpecification: Safety Decision was not supplied",
        )

    if evidence_package is None or len(evidence_package.evidence) == 0:
        logger.warning("Prompt construction blocked: missing or empty Evidence Package")
        return PromptBuilderResult(
            outcome=PromptBuilderOutcome.MISSING_EVIDENCE_PACKAGE,
            message="no PromptSpecification: Evidence Package was not supplied or was empty",
        )

    system = SystemLayer(
        mode=SYSTEM_LAYER_MODE,
        formal_validation=SYSTEM_LAYER_FORMAL_VALIDATION,
        execution_authorization=SYSTEM_LAYER_EXECUTION_AUTHORIZATION,
        vc_clin=SYSTEM_LAYER_VC_CLIN,
    )

    governance = GovernanceLayer(
        decision_id=safety_decision.decision_id,
        risk_class=safety_decision.risk_class,
        action=safety_decision.action,
        reason_code=safety_decision.reason_code,
    )

    evidence = EvidenceLayer(
        items=tuple(
            EvidenceLayerItem(
                population_id=item.population_id,
                artifact_type=item.artifact_type,
                title=item.title,
                content=item.content,
                provenance=item.provenance,
            )
            for item in evidence_package.evidence
        )
    )

    communication = CommunicationLayer(
        request_text=request_text,
        navigation_context=navigation_context,
    )

    record = PromptRecord(
        prompt_version=PROMPT_SPECIFICATION_VERSION,
        # Explicit "no identifier available" under the current locked
        # NavigationContextPlaceholder contract -- not a fabricated
        # reference, and not evidence that navigation_context (already
        # validated above) was skipped or rejected. See PromptRecord's
        # own docstring for the full governance note.
        navigation_context_reference=None,
        safety_decision_id=safety_decision.decision_id,
        evidence_package_id=evidence_package.metadata.evidence_package_id,
        generation_timestamp=datetime.now(UTC),
    )

    specification = PromptSpecification(
        system=system,
        governance=governance,
        evidence=evidence,
        communication=communication,
        record=record,
    )

    logger.info(
        "Prompt built: prompt_version=%s safety_decision_id=%s evidence_package_id=%s evidence_count=%d",
        PROMPT_SPECIFICATION_VERSION,
        safety_decision.decision_id,
        evidence_package.metadata.evidence_package_id,
        len(evidence_package.evidence),
    )

    return PromptBuilderResult(outcome=PromptBuilderOutcome.BUILT, specification=specification)
