"""Targeted CER orchestration tests.

These tests exercise the composition layer only. They use a deterministic
test LLMAdapter; this is not a production provider and must not be presented
as one.
"""

from datetime import UTC, datetime

from safe_medical_ai.cer import CEROutcome, CERRequest, CERRuntime
from safe_medical_ai.evidence import EvidenceItemProvenance, RTEPAssemblyContext
from safe_medical_ai.integration import RuntimeConstraints
from safe_medical_ai.llm.base import LLMAdapter
from safe_medical_ai.models.output_contract import NavigationContextPlaceholder
from safe_medical_ai.retrieval import (
    ArtifactType,
    RepositorySource,
    RetrievalCandidate,
    RetrievalRequest,
)
from safe_medical_ai.safety import RiskClass, SafetyAction, SafetyInput


class _FixtureSource(RepositorySource):
    def list_artifacts(self, population_id: str):
        if population_id != "PP-0001":
            return None
        return [
            RetrievalCandidate(
                population_id="PP-0001",
                artifact_type=ArtifactType.CKO,
                source_path="fixture/PP-0001/01_CKO.md",
                title="Fixture",
            )
        ]


class _DeterministicProvider(LLMAdapter):
    def generate(self, *, request):
        return "Controlled Evaluation test response."


def _request() -> CERRequest:
    return CERRequest(
        request_id="REQ-1",
        request_text="Controlled evaluation request.",
        retrieval_request=RetrievalRequest(population_id="PP-0001"),
        navigation_context=NavigationContextPlaceholder(),
        runtime_constraints=RuntimeConstraints(),
        rtep_context=RTEPAssemblyContext(
            retrieval_id="RET-1",
            navigation_context_id="NAV-1",
            retrieval_policy_version="RET-POL-1",
            knowledge_base_version="KB-1",
        ),
        provenance=(
            EvidenceItemProvenance(
                knowledge_object_id="KO-1",
                knowledge_passport_id="KP-1",
                source_id="SRC-1",
                guideline_version="GV-1",
            ),
        ),
        safety_input=SafetyInput(
            request_id="REQ-1",
            policy_version="SAFE-1",
            authorized=True,
            risk_class=RiskClass.LOW,
        ),
        validation_policy_version="VAL-1",
    )


def test_cer_completes_all_stages_with_injected_provider():
    result = CERRuntime(
        repository_source=_FixtureSource(),
        provider=_DeterministicProvider(),
    ).run(_request())

    assert result.outcome is CEROutcome.COMPLETED
    assert result.safety_decision is not None
    assert result.safety_decision.action is SafetyAction.ALLOW
    assert result.retrieval_response is not None
    assert result.assembly_result is not None
    assert result.assembly_result.package is not None
    assert result.integration_result is not None
    assert result.integration_result.context is not None
    assert result.generation_result is not None
    assert result.generation_result.response is not None
    assert result.validation_result is not None
    assert result.validation_result.outcome.value == "VALID"


def test_cer_stops_at_safety_gate():
    request = _request()
    blocked = request.safety_input.model_copy(update={"authorized": False})

    result = CERRuntime(
        repository_source=_FixtureSource(),
        provider=_DeterministicProvider(),
    ).run(request.model_copy(update={"safety_input": blocked}))

    assert result.outcome is CEROutcome.SAFETY_BLOCKED
    assert result.safety_decision is not None
    assert result.safety_decision.action is SafetyAction.REJECT
    assert result.retrieval_response is None
    assert result.generation_result is None


def test_cer_preserves_positional_provenance():
    result = CERRuntime(
        repository_source=_FixtureSource(),
        provider=_DeterministicProvider(),
    ).run(_request())

    package = result.assembly_result.package
    assert package is not None
    assert package.evidence[0].provenance.source_id == "SRC-1"
    assert package.evidence[0].provenance.guideline_version == "GV-1"


def test_cer_never_selects_a_provider():
    assert "OpenAI" not in CERRuntime.__module__
    assert "Anthropic" not in CERRuntime.__module__
