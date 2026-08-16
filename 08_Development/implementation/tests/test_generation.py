"""Tests for the Task #007 Generation boundary (`generate_candidate_response`).

Fake/in-memory `LLMAdapter` providers used for testing live entirely in
this test module, per spec section 7 — no test-only provider configuration
is shipped inside `generation/`.
"""

import inspect
import uuid
from datetime import UTC, datetime
from typing import Any

import pytest
from pydantic import ValidationError

from safe_medical_ai.evidence import (
    EvidenceItem,
    EvidenceItemProvenance,
    RuntimeEvidenceMetadata,
    RuntimeEvidencePackage,
)
from safe_medical_ai.generation import (
    GenerationOutcome,
    ProviderError,
    ProviderPartialOutputError,
    ProviderTimeoutError,
    generate_candidate_response,
)
from safe_medical_ai.generation import generation as generation_module
from safe_medical_ai.generation import models as generation_models_module
from safe_medical_ai.integration import EvidenceState, GenerationContext, RuntimeConstraints
from safe_medical_ai.llm.base import LLMAdapter
from safe_medical_ai.models.output_contract import NavigationContextPlaceholder
from safe_medical_ai.retrieval import ArtifactType
from safe_medical_ai.safety import RiskClass, SafetyAction, SafetyDecision


# --- fake providers (test boundary only) --------------------------------------


class FakeLLMAdapter(LLMAdapter):
    def __init__(self, output: str = "a generated candidate answer"):
        self._output = output

    def generate(self, *args: Any, **kwargs: Any) -> Any:
        return self._output


class FakeTimeoutProvider(LLMAdapter):
    def generate(self, *args: Any, **kwargs: Any) -> Any:
        raise ProviderTimeoutError("simulated timeout")


class FakePartialOutputProvider(LLMAdapter):
    def generate(self, *args: Any, **kwargs: Any) -> Any:
        raise ProviderPartialOutputError("simulated interruption")


class FakeFailingProvider(LLMAdapter):
    def generate(self, *args: Any, **kwargs: Any) -> Any:
        raise ProviderError("simulated provider failure")


class FakeUnexpectedlyBrokenProvider(LLMAdapter):
    def generate(self, *args: Any, **kwargs: Any) -> Any:
        raise RuntimeError("simulated unexpected internal error, not a ProviderError")


class FakeMalformedOutputProvider(LLMAdapter):
    def __init__(self, output: Any):
        self._output = output

    def generate(self, *args: Any, **kwargs: Any) -> Any:
        return self._output


class CapturingProvider(LLMAdapter):
    """Records the kwargs it was called with, for asserting provider input."""

    def __init__(self, output: str = "captured-output"):
        self._output = output
        self.received_kwargs: dict[str, Any] = {}

    def generate(self, *args: Any, **kwargs: Any) -> Any:
        self.received_kwargs = kwargs
        return self._output


# --- fixtures ------------------------------------------------------------------


def _metadata(retrieval_id: str = "RID-1") -> RuntimeEvidenceMetadata:
    return RuntimeEvidenceMetadata(
        evidence_package_id="EP-1",
        retrieval_id=retrieval_id,
        navigation_context_id="NAV-1",
        retrieval_policy_version="1.0",
        knowledge_base_version="1.0",
        generation_timestamp=datetime.now(UTC),
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


def _safety_decision() -> SafetyDecision:
    # Track 3 BATCH 03: a valid ALLOW decision -- generation tests are not
    # about safety adjudication, so this is a fixed, deterministic ALLOW
    # fixture, not a re-implementation of safety policy.
    return SafetyDecision(
        request_id="REQ-1",
        decision_id=uuid.uuid4().hex,
        policy_version="1.0",
        risk_class=RiskClass.LOW,
        reason_code="AUTHORIZED_REQUEST",
        action=SafetyAction.ALLOW,
        timestamp=datetime.now(UTC),
    )


def _context(
    evidence_state: EvidenceState,
    rtep: RuntimeEvidencePackage | None = None,
    safety_decision: SafetyDecision | None | str = "default",
) -> GenerationContext:
    if rtep is None:
        evidence = (_evidence_item("a"), _evidence_item("b")) if evidence_state is EvidenceState.HAS_EVIDENCE else ()
        rtep = RuntimeEvidencePackage(metadata=_metadata(), evidence=evidence)
    if safety_decision == "default":
        safety_decision = _safety_decision()
    return GenerationContext(
        integration_id="INT-1",
        integration_timestamp=datetime.now(UTC),
        request_text="what is gastric cancer?",
        navigation_context=NavigationContextPlaceholder(),
        rtep=rtep,
        runtime_constraints=RuntimeConstraints(),
        evidence_state=evidence_state,
        safety_decision=safety_decision,
    )


# --- 1/2. valid context, evidence-present generation --------------------------


def test_evidence_present_generation_succeeds():
    result = generate_candidate_response(_context(EvidenceState.HAS_EVIDENCE), FakeLLMAdapter("a real answer"))

    assert result.outcome == GenerationOutcome.GENERATED
    assert result.response is not None
    assert result.response.content == "a real answer"
    assert result.response.evidence_state == EvidenceState.HAS_EVIDENCE
    assert result.response.provider_name == "FakeLLMAdapter"


# --- regression: provider receives the authoritative governed RTEP evidence ----
# (Change Request review fix — a prior version only passed `prompt=request_text`)


def test_provider_receives_authoritative_rtep_evidence():
    context = _context(EvidenceState.HAS_EVIDENCE)
    provider = CapturingProvider()

    generate_candidate_response(context, provider)

    request = provider.received_kwargs.get("request")
    assert request is not None
    assert request.evidence == context.rtep.evidence
    assert request.evidence_metadata == context.rtep.metadata
    assert request.request_text == context.request_text
    assert request.navigation_context == context.navigation_context
    assert request.runtime_constraints == context.runtime_constraints
    # Value-level check, not just structural presence: provenance actually
    # reached the provider.
    assert [item.provenance.knowledge_object_id for item in request.evidence] == [
        item.provenance.knowledge_object_id for item in context.rtep.evidence
    ]
    assert [item.provenance.guideline_version for item in request.evidence] == [
        item.provenance.guideline_version for item in context.rtep.evidence
    ]


def test_provider_receives_the_governed_prompt_specification():
    # Track 3 BATCH 03: the provider request must also carry the governed
    # PromptSpecification the Prompt Builder produced -- not just the raw
    # evidence/context fields the pre-BATCH-03 contract already carried.
    context = _context(EvidenceState.HAS_EVIDENCE)
    provider = CapturingProvider()

    generate_candidate_response(context, provider)

    request = provider.received_kwargs.get("request")
    assert request.prompt_specification is not None
    assert request.prompt_specification.communication.request_text == context.request_text
    assert request.prompt_specification.governance.decision_id == context.safety_decision.decision_id
    assert len(request.prompt_specification.evidence.items) == len(context.rtep.evidence)


def test_provider_receives_evidence_in_original_order_without_reranking():
    # Deliberately not in any "natural"/alphabetical/canonical order.
    items = (_evidence_item("z"), _evidence_item("a"), _evidence_item("m"))
    rtep = RuntimeEvidencePackage(metadata=_metadata(), evidence=items)
    context = _context(EvidenceState.HAS_EVIDENCE, rtep=rtep)
    provider = CapturingProvider()

    generate_candidate_response(context, provider)

    request = provider.received_kwargs.get("request")
    assert [item.source_path for item in request.evidence] == [item.source_path for item in items]


def test_provider_receives_the_evidence_items_actual_content():
    # Track 3 BATCH 01: the provider must receive EvidenceItem.content
    # unchanged (present, non-empty for a content-bearing item), not only
    # identity/provenance -- generation itself requires no redesign to carry
    # it, since ProviderGenerationRequest.evidence already references the
    # exact EvidenceItem tuple unchanged.
    rtep = RuntimeEvidencePackage(
        metadata=_metadata(),
        evidence=(_evidence_item("a", content="real clinical prose for evidence item a"),),
    )
    context = _context(EvidenceState.HAS_EVIDENCE, rtep=rtep)
    provider = CapturingProvider()

    generate_candidate_response(context, provider)

    request = provider.received_kwargs.get("request")
    assert request.evidence[0].content == "real clinical prose for evidence item a"


def test_provider_request_evidence_items_are_the_same_objects_not_reconstructed():
    # Pydantic validation builds a new *tuple container* when constructing
    # ProviderGenerationRequest (an ordinary consequence of `tuple(...)`),
    # but with the default `revalidate_instances="never"` behavior each
    # already-valid EvidenceItem/RuntimeEvidenceMetadata *instance* inside
    # is reused as-is, not rebuilt — that per-item identity is what actually
    # proves no reconstruction/repair happened, so it's what this test checks.
    context = _context(EvidenceState.HAS_EVIDENCE)
    provider = CapturingProvider()

    generate_candidate_response(context, provider)

    request = provider.received_kwargs.get("request")
    assert request.evidence == context.rtep.evidence
    for original, passed in zip(context.rtep.evidence, request.evidence, strict=True):
        assert passed is original
    assert request.evidence_metadata is context.rtep.metadata


# --- 3. EMPTY_EVIDENCE branch --------------------------------------------------


def test_empty_evidence_produces_fixed_policy_response_without_calling_provider():
    class ExplodingProvider(LLMAdapter):
        def generate(self, *args: Any, **kwargs: Any) -> Any:
            raise AssertionError("provider must not be called for EMPTY evidence_state")

    result = generate_candidate_response(_context(EvidenceState.EMPTY), ExplodingProvider())

    assert result.outcome == GenerationOutcome.EMPTY_EVIDENCE_RESPONSE
    assert result.response is not None
    assert result.response.evidence_state == EvidenceState.EMPTY
    assert result.response.provider_name is None
    assert "no" in result.response.content.lower() or "evidence" in result.response.content.lower()


def test_empty_evidence_never_reaches_a_non_raising_capturing_provider():
    # Complements the exploding-provider test above with positive evidence
    # (an empty capture) rather than only a negative one (a raised error).
    context = _context(EvidenceState.EMPTY)
    provider = CapturingProvider()

    generate_candidate_response(context, provider)

    assert provider.received_kwargs == {}


def test_empty_evidence_policy_response_content_is_deterministic_across_calls():
    context = _context(EvidenceState.EMPTY)
    first = generate_candidate_response(context, FakeLLMAdapter())
    second = generate_candidate_response(context, FakeLLMAdapter())

    assert first.response.content == second.response.content


def test_empty_evidence_policy_response_matches_the_locked_public_constant():
    from safe_medical_ai.generation import EMPTY_EVIDENCE_POLICY_RESPONSE_TEXT

    result = generate_candidate_response(_context(EvidenceState.EMPTY), FakeLLMAdapter())

    assert result.response.content == EMPTY_EVIDENCE_POLICY_RESPONSE_TEXT


# --- 4. invalid/blocked context -------------------------------------------------


def test_none_context_produces_invalid_context():
    result = generate_candidate_response(None, FakeLLMAdapter())

    assert result.outcome == GenerationOutcome.INVALID_CONTEXT
    assert result.response is None


# --- 5. missing RTEP (defensive-only, via model_construct bypass) --------------


def test_context_with_missing_rtep_produces_context_missing_rtep():
    broken_context = GenerationContext.model_construct(
        integration_id="INT-1",
        integration_timestamp=datetime.now(UTC),
        request_text="q",
        navigation_context=NavigationContextPlaceholder(),
        rtep=None,
        runtime_constraints=RuntimeConstraints(),
        evidence_state=EvidenceState.HAS_EVIDENCE,
    )

    result = generate_candidate_response(broken_context, FakeLLMAdapter())

    assert result.outcome == GenerationOutcome.CONTEXT_MISSING_RTEP
    assert result.response is None


# --- 5b. Prompt Contract blocked (Track 3 BATCH 03) -----------------------------


def test_missing_safety_decision_produces_prompt_blocked_not_generated():
    context = _context(EvidenceState.HAS_EVIDENCE, safety_decision=None)
    provider = CapturingProvider()

    result = generate_candidate_response(context, provider)

    assert result.outcome == GenerationOutcome.PROMPT_BLOCKED
    assert result.response is None


def test_prompt_blocked_never_calls_the_provider():
    context = _context(EvidenceState.HAS_EVIDENCE, safety_decision=None)
    provider = CapturingProvider()

    generate_candidate_response(context, provider)

    assert provider.received_kwargs == {}


# --- 6/7/8/9. provider failure modes --------------------------------------------


def test_provider_failure_produces_no_response():
    result = generate_candidate_response(_context(EvidenceState.HAS_EVIDENCE), FakeFailingProvider())

    assert result.outcome == GenerationOutcome.PROVIDER_FAILURE
    assert result.response is None


def test_provider_timeout_produces_no_response():
    result = generate_candidate_response(_context(EvidenceState.HAS_EVIDENCE), FakeTimeoutProvider())

    assert result.outcome == GenerationOutcome.PROVIDER_TIMEOUT
    assert result.response is None


def test_provider_partial_output_produces_no_response():
    result = generate_candidate_response(_context(EvidenceState.HAS_EVIDENCE), FakePartialOutputProvider())

    assert result.outcome == GenerationOutcome.PARTIAL_GENERATION
    assert result.response is None


@pytest.mark.parametrize("malformed_output", [None, "", "   ", 12345, ["not", "a", "string"]])
def test_malformed_provider_output_produces_no_response(malformed_output):
    result = generate_candidate_response(
        _context(EvidenceState.HAS_EVIDENCE), FakeMalformedOutputProvider(malformed_output)
    )

    assert result.outcome == GenerationOutcome.MALFORMED_PROVIDER_OUTPUT
    assert result.response is None


def test_unexpected_provider_exception_produces_internal_failure_not_a_crash():
    result = generate_candidate_response(_context(EvidenceState.HAS_EVIDENCE), FakeUnexpectedlyBrokenProvider())

    assert result.outcome == GenerationOutcome.INTERNAL_FAILURE
    assert result.response is None


# --- 10. atomic success/failure -------------------------------------------------


@pytest.mark.parametrize(
    "outcome,provider",
    [
        (GenerationOutcome.PROVIDER_FAILURE, FakeFailingProvider()),
        (GenerationOutcome.PROVIDER_TIMEOUT, FakeTimeoutProvider()),
        (GenerationOutcome.PARTIAL_GENERATION, FakePartialOutputProvider()),
        (GenerationOutcome.MALFORMED_PROVIDER_OUTPUT, FakeMalformedOutputProvider(None)),
        (GenerationOutcome.INTERNAL_FAILURE, FakeUnexpectedlyBrokenProvider()),
    ],
)
def test_every_failure_outcome_has_no_response(outcome, provider):
    result = generate_candidate_response(_context(EvidenceState.HAS_EVIDENCE), provider)
    assert result.outcome == outcome
    assert result.response is None


def test_every_success_outcome_has_a_complete_response():
    generated = generate_candidate_response(_context(EvidenceState.HAS_EVIDENCE), FakeLLMAdapter())
    empty = generate_candidate_response(_context(EvidenceState.EMPTY), FakeLLMAdapter())

    assert generated.outcome == GenerationOutcome.GENERATED and generated.response is not None
    assert empty.outcome == GenerationOutcome.EMPTY_EVIDENCE_RESPONSE and empty.response is not None


# --- 11. traceability -------------------------------------------------------------


def test_generated_response_carries_traceability_identifiers():
    context = _context(EvidenceState.HAS_EVIDENCE)
    result = generate_candidate_response(context, FakeLLMAdapter())

    response = result.response
    assert response.integration_id == context.integration_id
    assert response.retrieval_id == context.rtep.metadata.retrieval_id
    assert response.navigation_context_id == context.rtep.metadata.navigation_context_id
    assert response.evidence_package_id == context.rtep.metadata.evidence_package_id
    assert response.candidate_response_id  # generated, non-empty


# --- 12. immutability --------------------------------------------------------------


def test_generation_does_not_mutate_the_context_or_its_rtep():
    context = _context(EvidenceState.HAS_EVIDENCE)
    generate_candidate_response(context, FakeLLMAdapter())

    with pytest.raises(ValidationError):
        context.request_text = "MUTATED"
    with pytest.raises(ValidationError):
        context.rtep.evidence = ()
    with pytest.raises(ValidationError):
        context.rtep.metadata.retrieval_id = "MUTATED"


def test_generation_does_not_mutate_evidence_items_or_provenance():
    context = _context(EvidenceState.HAS_EVIDENCE)
    generate_candidate_response(context, FakeLLMAdapter())

    with pytest.raises(ValidationError):
        context.rtep.evidence[0].title = "MUTATED"
    with pytest.raises(ValidationError):
        context.rtep.evidence[0].provenance.knowledge_object_id = "MUTATED"


def test_candidate_response_is_a_newly_created_object_not_the_context():
    context = _context(EvidenceState.HAS_EVIDENCE)
    result = generate_candidate_response(context, FakeLLMAdapter())

    assert result.response is not context
    assert not hasattr(result.response, "rtep")


# --- 13/14. no retrieval, no filesystem/repository access (static) ----------------


def test_generation_module_does_not_access_repository_or_retrieval():
    source = inspect.getsource(generation_module)
    assert "RepositorySource(" not in source
    assert ".list_artifacts(" not in source
    assert "RetrievalService(" not in source
    assert ".retrieve(" not in source


def test_generation_module_does_not_touch_filesystem():
    source = inspect.getsource(generation_module)
    assert "open(" not in source
    assert "Path(" not in source
    assert "pathlib" not in source


# --- 15. no Validation coupling ---------------------------------------------------


def test_generation_does_not_import_or_reference_validation():
    # Check the actual module namespace, not raw source text: both modules'
    # docstrings legitimately *mention* ValidationOutcome in prose (explaining
    # why GenerationOutcome is a distinct vocabulary from it), which would
    # false-positive a plain substring search.
    assert "ValidationOutcome" not in dir(generation_module)
    assert "ValidationOutcome" not in dir(generation_models_module)
    source = inspect.getsource(generation_module) + inspect.getsource(generation_models_module)
    assert "import validation" not in source.lower()
    assert "from ..validation" not in source


# --- 16. no vector/embedding/LLM-vendor prohibited path ---------------------------


@pytest.mark.parametrize(
    "forbidden_token",
    [
        "openai",
        "anthropic",
        "sentence_transformers",
        "faiss",
        "chromadb",
        "pinecone",
        "import torch",
        "import requests",
        "urllib",
    ],
)
def test_generation_does_not_reference_llm_vendor_or_web_libraries(forbidden_token):
    source = inspect.getsource(generation_module) + inspect.getsource(generation_models_module)
    assert forbidden_token.lower() not in source.lower()


# --- 17. deterministic orchestration behavior -------------------------------------


def test_repeated_calls_with_equivalent_input_and_deterministic_provider_produce_equivalent_output():
    context = _context(EvidenceState.HAS_EVIDENCE)

    first = generate_candidate_response(context, FakeLLMAdapter("stable output"))
    second = generate_candidate_response(context, FakeLLMAdapter("stable output"))

    assert first.outcome == second.outcome == GenerationOutcome.GENERATED
    assert first.response.content == second.response.content
    assert first.response.evidence_state == second.response.evidence_state
    assert first.response.integration_id == second.response.integration_id
    assert first.response.retrieval_id == second.response.retrieval_id
    # candidate_response_id/generation_timestamp are legitimately
    # runtime-generated identity/timestamp fields and may differ.
    assert isinstance(first.response.candidate_response_id, str)
    assert isinstance(second.response.candidate_response_id, str)
