"""Tests for the Track 3 BATCH 03 Governed Prompt Builder (`build_prompt`)."""

from __future__ import annotations

import inspect
import uuid
from datetime import UTC, datetime

from safe_medical_ai.evidence import (
    EvidenceItem,
    EvidenceItemProvenance,
    RuntimeEvidenceMetadata,
    RuntimeEvidencePackage,
)
from safe_medical_ai.models.output_contract import NavigationContextPlaceholder
from safe_medical_ai.prompting import (
    PROMPT_SPECIFICATION_VERSION,
    PromptBuilderOutcome,
    build_prompt,
)
from safe_medical_ai.prompting import builder as builder_module
from safe_medical_ai.prompting import models as prompting_models_module
from safe_medical_ai.retrieval import ArtifactType
from safe_medical_ai.safety import RiskClass, SafetyAction, SafetyDecision


def _safety_decision() -> SafetyDecision:
    return SafetyDecision(
        request_id="REQ-1",
        decision_id=uuid.uuid4().hex,
        policy_version="1.0",
        risk_class=RiskClass.LOW,
        reason_code="AUTHORIZED_REQUEST",
        action=SafetyAction.ALLOW,
        timestamp=datetime.now(UTC),
    )


def _evidence_item(suffix: str, content: str | None = None) -> EvidenceItem:
    return EvidenceItem(
        population_id="PP-0001",
        artifact_type=ArtifactType.CKO,
        source_path=f"03_Clinical_Knowledge/population/population_packages/PP-0001/01_CKO-{suffix}.md",
        title=f"title-{suffix}",
        provenance=EvidenceItemProvenance(
            knowledge_object_id=f"KO-{suffix}",
            knowledge_passport_id=f"KP-{suffix}",
            source_id=f"SRC-{suffix}",
            guideline_version=f"v{suffix}.0",
        ),
        content=content,
    )


def _evidence_package(*items: EvidenceItem) -> RuntimeEvidencePackage:
    return RuntimeEvidencePackage(
        metadata=RuntimeEvidenceMetadata(
            evidence_package_id="EP-1",
            retrieval_id="RID-1",
            navigation_context_id="NAV-1",
            retrieval_policy_version="1.0",
            knowledge_base_version="1.0",
            generation_timestamp=datetime.now(UTC),
        ),
        evidence=items,
    )


_UNSET = object()


def _build(
    navigation_context=NavigationContextPlaceholder(),
    safety_decision=_UNSET,
    evidence_package=_UNSET,
    request_text="What is Gastric Adenocarcinoma?",
):
    if safety_decision is _UNSET:
        safety_decision = _safety_decision()
    if evidence_package is _UNSET:
        evidence_package = _evidence_package(_evidence_item("a", content="real clinical content"))
    return build_prompt(
        navigation_context=navigation_context,
        safety_decision=safety_decision,
        evidence_package=evidence_package,
        request_text=request_text,
    )


# --- A. Prompt Contract: valid inputs -> PromptSpecification ------------------


def test_valid_inputs_produce_a_built_prompt_specification():
    result = _build()

    assert result.outcome is PromptBuilderOutcome.BUILT
    assert result.specification is not None
    assert result.message is None


# --- A. Prompt Contract: missing mandatory inputs block -----------------------


def test_missing_navigation_context_blocks_prompt_construction():
    result = _build(navigation_context=None)

    assert result.outcome is PromptBuilderOutcome.MISSING_NAVIGATION_CONTEXT
    assert result.specification is None


def test_missing_safety_decision_blocks_prompt_construction():
    result = _build(safety_decision=None)

    assert result.outcome is PromptBuilderOutcome.MISSING_SAFETY_DECISION
    assert result.specification is None


def test_missing_evidence_package_blocks_prompt_construction():
    result = _build(evidence_package=None)

    assert result.outcome is PromptBuilderOutcome.MISSING_EVIDENCE_PACKAGE
    assert result.specification is None


def test_empty_evidence_package_blocks_prompt_construction():
    result = _build(evidence_package=_evidence_package())

    assert result.outcome is PromptBuilderOutcome.MISSING_EVIDENCE_PACKAGE
    assert result.specification is None


# --- B. Layer assembly ---------------------------------------------------------


def test_system_layer_is_present_and_matches_the_existing_boundary_statement():
    result = _build()

    system = result.specification.system
    assert system.mode == "RESEARCH / DEVELOPMENT / CONTROLLED EVALUATION ONLY"
    assert system.formal_validation == "NOT STARTED"
    assert system.execution_authorization == "NOT GRANTED"
    assert system.vc_clin == "DEFERRED"


def test_governance_layer_is_derived_from_the_supplied_safety_decision():
    decision = _safety_decision()
    result = _build(safety_decision=decision)

    governance = result.specification.governance
    assert governance.decision_id == decision.decision_id
    assert governance.risk_class == decision.risk_class
    assert governance.action == decision.action
    assert governance.reason_code == decision.reason_code


def test_evidence_layer_contains_the_supplied_evidence_content():
    package = _evidence_package(_evidence_item("a", content="a specific unique clinical sentence"))
    result = _build(evidence_package=package)

    evidence = result.specification.evidence
    assert len(evidence.items) == 1
    assert evidence.items[0].content == "a specific unique clinical sentence"


def test_communication_layer_is_present():
    result = _build(request_text="What is Gastric Adenocarcinoma?")

    communication = result.specification.communication
    assert communication.request_text == "What is Gastric Adenocarcinoma?"
    assert communication.navigation_context == NavigationContextPlaceholder()


# --- C. Evidence integrity ------------------------------------------------------


def test_evidence_order_is_preserved():
    items = (_evidence_item("z"), _evidence_item("a"), _evidence_item("m"))
    result = _build(evidence_package=_evidence_package(*items))

    assert [i.population_id for i in result.specification.evidence.items] == [
        "PP-0001",
        "PP-0001",
        "PP-0001",
    ]
    assert [i.provenance.knowledge_object_id for i in result.specification.evidence.items] == [
        item.provenance.knowledge_object_id for item in items
    ]


def test_evidence_content_is_unchanged():
    item = _evidence_item("a", content="exact original governed clinical text")
    result = _build(evidence_package=_evidence_package(item))

    assert result.specification.evidence.items[0].content == item.content


def test_evidence_provenance_and_identity_are_preserved():
    item = _evidence_item("a", content="content")
    result = _build(evidence_package=_evidence_package(item))

    layer_item = result.specification.evidence.items[0]
    assert layer_item.population_id == item.population_id
    assert layer_item.artifact_type == item.artifact_type
    assert layer_item.title == item.title
    assert layer_item.provenance == item.provenance


# --- D. Determinism --------------------------------------------------------------


def test_same_structured_inputs_produce_the_same_specification_except_timestamp():
    decision = _safety_decision()
    package = _evidence_package(_evidence_item("a", content="content"))

    first = _build(safety_decision=decision, evidence_package=package)
    second = _build(safety_decision=decision, evidence_package=package)

    assert first.specification.system == second.specification.system
    assert first.specification.governance == second.specification.governance
    assert first.specification.evidence == second.specification.evidence
    assert first.specification.communication == second.specification.communication
    assert first.specification.record.prompt_version == second.specification.record.prompt_version
    assert first.specification.record.safety_decision_id == second.specification.record.safety_decision_id
    assert first.specification.record.evidence_package_id == second.specification.record.evidence_package_id
    # generation_timestamp is legitimately runtime-generated and may differ.
    assert isinstance(first.specification.record.generation_timestamp, datetime)
    assert isinstance(second.specification.record.generation_timestamp, datetime)


# --- E. Model independence -------------------------------------------------------


def test_prompt_builder_does_not_import_openai_or_any_provider():
    source = inspect.getsource(builder_module) + inspect.getsource(prompting_models_module)
    forbidden = ["openai", "anthropic", "OpenAIProvider", "from ..llm", "import llm"]
    lowered = source.lower()
    for token in forbidden:
        assert token.lower() not in lowered


def test_prompt_builder_does_not_import_generation_cer_or_api():
    source = inspect.getsource(builder_module) + inspect.getsource(prompting_models_module)
    assert "from ..generation" not in source
    assert "from ..cer" not in source
    assert "from ..api" not in source


# --- G. Prompt Record ------------------------------------------------------------


def test_prompt_record_contains_the_required_traceability_fields():
    decision = _safety_decision()
    package = _evidence_package(_evidence_item("a", content="content"))
    result = _build(safety_decision=decision, evidence_package=package)

    record = result.specification.record
    assert record.prompt_version == PROMPT_SPECIFICATION_VERSION
    assert record.safety_decision_id == decision.decision_id
    assert record.evidence_package_id == package.metadata.evidence_package_id
    assert record.generation_timestamp is not None


def test_prompt_record_navigation_context_reference_is_honestly_none():
    # NavigationContextPlaceholder carries no identifier of its own -- this
    # module does not fabricate one (see prompting/README.md).
    result = _build()

    assert result.specification.record.navigation_context_reference is None


def test_current_navigation_context_placeholder_is_accepted_not_rejected():
    # A missing navigation_context still blocks (proven elsewhere); the
    # current, valid NavigationContextPlaceholder() must NOT block, and
    # None-identifier traceability must not be mistaken for that.
    result = _build(navigation_context=NavigationContextPlaceholder())

    assert result.outcome is PromptBuilderOutcome.BUILT
    assert result.specification is not None
    assert result.specification.communication.navigation_context == NavigationContextPlaceholder()


def test_none_navigation_reference_does_not_fabricate_an_identifier_and_other_traceability_fields_remain_populated():
    decision = _safety_decision()
    package = _evidence_package(_evidence_item("a", content="content"))
    result = _build(safety_decision=decision, evidence_package=package)

    record = result.specification.record
    # The one honest gap: no fabricated string, no placeholder ID.
    assert record.navigation_context_reference is None
    # Every other traceability field is still genuinely populated from the
    # real supplied objects -- the None above is a narrow, explicit gap,
    # not evidence that the record itself is incomplete/broken.
    assert record.prompt_version == PROMPT_SPECIFICATION_VERSION
    assert record.safety_decision_id == decision.decision_id
    assert record.evidence_package_id == package.metadata.evidence_package_id
    assert record.generation_timestamp is not None


# --- boundary: never touches the filesystem or re-retrieves ---------------------


def test_prompt_builder_module_does_not_touch_filesystem_or_retrieve():
    source = inspect.getsource(builder_module)
    assert "open(" not in source
    assert "Path(" not in source
    assert "RepositorySource(" not in source
    assert ".list_artifacts(" not in source
    assert "RetrievalService(" not in source
    assert ".retrieve(" not in source
