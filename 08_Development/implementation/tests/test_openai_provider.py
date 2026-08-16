"""Tests for the Track 3 BATCH 02 OpenAI provider adapter (`OpenAIProvider`).

Never calls the real network and never uses a real API key: a fake OpenAI
SDK client is substituted onto `OpenAIProvider._client`, following the same
"fakes live entirely in the test module" convention `generation/README.md`
already establishes for `LLMAdapter` implementations. `httpx2.Request`/
`httpx2.Response` objects are constructed only because the real `openai`
exception classes require them structurally -- no network I/O occurs.
"""

from __future__ import annotations

import uuid
from datetime import UTC, datetime

import httpx2
import openai
import pytest

from safe_medical_ai.evidence import (
    EvidenceItem,
    EvidenceItemProvenance,
    RuntimeEvidenceMetadata,
    RuntimeEvidencePackage,
)
from safe_medical_ai.generation import (
    ProviderError,
    ProviderGenerationRequest,
    ProviderPartialOutputError,
    ProviderTimeoutError,
    generate_candidate_response,
)
from safe_medical_ai.integration import EvidenceState, GenerationContext, RuntimeConstraints
from safe_medical_ai.llm.openai_provider import DEFAULT_OPENAI_MODEL, OpenAIProvider
from safe_medical_ai.models.output_contract import NavigationContextPlaceholder
from safe_medical_ai.prompting import build_prompt
from safe_medical_ai.retrieval import ArtifactType
from safe_medical_ai.safety import RiskClass, SafetyAction, SafetyDecision

_FAKE_API_KEY = "sk-test-not-a-real-key-000000000000000000"


# --- fake OpenAI SDK client (test boundary only) ----------------------------


class _FakeResponse:
    def __init__(self, output_text: str, status: str = "completed"):
        self.output_text = output_text
        self.status = status


class _FakeResponsesEndpoint:
    def __init__(self, output_text: str = "a substantive answer", status: str = "completed", exception=None):
        self._output_text = output_text
        self._status = status
        self._exception = exception
        self.received_kwargs: dict | None = None

    def create(self, **kwargs):
        self.received_kwargs = kwargs
        if self._exception is not None:
            raise self._exception
        return _FakeResponse(self._output_text, self._status)


class _FakeOpenAIClient:
    def __init__(self, responses_endpoint: _FakeResponsesEndpoint):
        self.responses = responses_endpoint


def _provider_with_fake_client(responses_endpoint: _FakeResponsesEndpoint) -> OpenAIProvider:
    provider = OpenAIProvider(api_key=_FAKE_API_KEY, model=DEFAULT_OPENAI_MODEL)
    provider._client = _FakeOpenAIClient(responses_endpoint)
    return provider


def _fake_request() -> httpx2.Request:
    return httpx2.Request("POST", "https://api.openai.com/v1/responses")


# --- fixtures ----------------------------------------------------------------


def _evidence_item(content: str | None) -> EvidenceItem:
    return EvidenceItem(
        population_id="PP-0003",
        artifact_type=ArtifactType.CKO,
        source_path="03_Clinical_Knowledge/population/population_packages/PP-0003/01_CKO.md",
        title="What is Gastric Adenocarcinoma?",
        provenance=EvidenceItemProvenance(
            knowledge_object_id="KO-1",
            knowledge_passport_id="KP-1",
            source_id="SRC-1",
            guideline_version="1.0",
        ),
        content=content,
    )


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


def _provider_request(content: str | None = "actual governed clinical prose about gastric adenocarcinoma") -> ProviderGenerationRequest:
    evidence_metadata = RuntimeEvidenceMetadata(
        evidence_package_id="EP-1",
        retrieval_id="RID-1",
        navigation_context_id="NAV-1",
        retrieval_policy_version="1.0",
        knowledge_base_version="1.0",
        generation_timestamp=datetime.now(UTC),
    )
    evidence_item = _evidence_item(content)
    navigation_context = NavigationContextPlaceholder()
    # Track 3 BATCH 03: build a real PromptSpecification via the actual
    # Prompt Builder (not a hand-rolled test double) so this fixture stays
    # a genuine, valid ProviderGenerationRequest.
    prompt_result = build_prompt(
        navigation_context=navigation_context,
        safety_decision=_safety_decision(),
        evidence_package=RuntimeEvidencePackage(metadata=evidence_metadata, evidence=(evidence_item,)),
        request_text="What is Gastric Adenocarcinoma?",
    )
    return ProviderGenerationRequest(
        request_text="What is Gastric Adenocarcinoma?",
        navigation_context=navigation_context,
        evidence=(evidence_item,),
        evidence_metadata=evidence_metadata,
        runtime_constraints=RuntimeConstraints(),
        prompt_specification=prompt_result.specification,
    )


# --- construction / configuration --------------------------------------------


def test_default_model_is_the_locked_gpt_5_4_mini():
    assert DEFAULT_OPENAI_MODEL == "gpt-5.4-mini"


def test_provider_uses_the_locked_default_model_when_not_overridden():
    provider = OpenAIProvider(api_key=_FAKE_API_KEY)
    assert provider._model == "gpt-5.4-mini"


# --- Test A: request text is mapped correctly --------------------------------


def test_request_text_reaches_the_openai_call():
    fake = _FakeResponsesEndpoint(output_text="answer")
    provider = _provider_with_fake_client(fake)

    provider.generate(request=_provider_request())

    assert "What is Gastric Adenocarcinoma?" in fake.received_kwargs["input"]


# --- Test B: evidence content is mapped correctly ----------------------------


def test_evidence_content_reaches_the_openai_call():
    fake = _FakeResponsesEndpoint(output_text="answer")
    provider = _provider_with_fake_client(fake)

    provider.generate(request=_provider_request(content="a specific unique clinical sentence about gastric cancer"))

    assert "a specific unique clinical sentence about gastric cancer" in fake.received_kwargs["input"]


def test_locked_model_is_used_in_the_openai_call():
    fake = _FakeResponsesEndpoint(output_text="answer")
    provider = _provider_with_fake_client(fake)

    provider.generate(request=_provider_request())

    assert fake.received_kwargs["model"] == DEFAULT_OPENAI_MODEL


# --- Test C: generated text is returned as plain str -------------------------


def test_generated_text_is_returned_as_plain_str():
    fake = _FakeResponsesEndpoint(output_text="a real substantive answer about gastric adenocarcinoma")
    provider = _provider_with_fake_client(fake)

    result = provider.generate(request=_provider_request())

    assert isinstance(result, str)
    assert result == "a real substantive answer about gastric adenocarcinoma"


# --- Test D: authentication/configuration failure -----------------------------


def test_authentication_failure_maps_to_provider_error():
    exc = openai.AuthenticationError(
        "invalid api key", response=httpx2.Response(401, request=_fake_request()), body=None
    )
    provider = _provider_with_fake_client(_FakeResponsesEndpoint(exception=exc))

    with pytest.raises(ProviderError):
        provider.generate(request=_provider_request())


# --- Test E: timeout / network failure -----------------------------------------


def test_timeout_maps_to_provider_timeout_error():
    exc = openai.APITimeoutError(request=_fake_request())
    provider = _provider_with_fake_client(_FakeResponsesEndpoint(exception=exc))

    with pytest.raises(ProviderTimeoutError):
        provider.generate(request=_provider_request())


def test_connection_failure_maps_to_provider_timeout_error():
    exc = openai.APIConnectionError(request=_fake_request())
    provider = _provider_with_fake_client(_FakeResponsesEndpoint(exception=exc))

    with pytest.raises(ProviderTimeoutError):
        provider.generate(request=_provider_request())


# --- Test F: provider / API failure (including rate limit) --------------------


def test_rate_limit_maps_to_provider_error():
    exc = openai.RateLimitError(
        "rate limited", response=httpx2.Response(429, request=_fake_request()), body=None
    )
    provider = _provider_with_fake_client(_FakeResponsesEndpoint(exception=exc))

    with pytest.raises(ProviderError):
        provider.generate(request=_provider_request())


def test_generic_api_error_maps_to_provider_error():
    exc = openai.APIError("unexpected API error", _fake_request(), body=None)
    provider = _provider_with_fake_client(_FakeResponsesEndpoint(exception=exc))

    with pytest.raises(ProviderError):
        provider.generate(request=_provider_request())


# --- Test G: empty/invalid output handled per existing semantics --------------


def test_empty_output_text_is_returned_unchanged_for_generation_to_classify():
    # Generation's own MALFORMED_PROVIDER_OUTPUT check (a non-blank str
    # requirement) already handles this -- the adapter must not invent a
    # second empty-output policy of its own.
    fake = _FakeResponsesEndpoint(output_text="")
    provider = _provider_with_fake_client(fake)

    result = provider.generate(request=_provider_request())

    assert result == ""


def test_incomplete_response_status_maps_to_provider_partial_output_error():
    fake = _FakeResponsesEndpoint(output_text="a partial answer that got cut off", status="incomplete")
    provider = _provider_with_fake_client(fake)

    with pytest.raises(ProviderPartialOutputError):
        provider.generate(request=_provider_request())


# --- Test H: no credential exposed in the request object or logging path ------


def test_api_key_is_not_included_in_the_openai_call_kwargs():
    fake = _FakeResponsesEndpoint(output_text="answer")
    provider = _provider_with_fake_client(fake)

    provider.generate(request=_provider_request())

    assert _FAKE_API_KEY not in repr(fake.received_kwargs)
    assert "api_key" not in fake.received_kwargs


def test_api_key_is_not_logged(caplog):
    fake = _FakeResponsesEndpoint(output_text="answer")
    provider = _provider_with_fake_client(fake)

    with caplog.at_level("DEBUG"):
        provider.generate(request=_provider_request())

    assert _FAKE_API_KEY not in caplog.text


def test_api_key_is_not_logged_on_failure(caplog):
    exc = openai.AuthenticationError(
        "invalid api key", response=httpx2.Response(401, request=_fake_request()), body=None
    )
    provider = _provider_with_fake_client(_FakeResponsesEndpoint(exception=exc))

    with caplog.at_level("DEBUG"):
        with pytest.raises(ProviderError):
            provider.generate(request=_provider_request())

    assert _FAKE_API_KEY not in caplog.text


# --- Track 3 BATCH 03: the BATCH 02 temporary bridge is no longer active -----


def test_temporary_bridge_method_no_longer_exists():
    assert not hasattr(OpenAIProvider, "_build_temporary_bridge_input")


def test_generate_renders_from_the_governed_prompt_specification():
    fake = _FakeResponsesEndpoint(output_text="answer")
    provider = _provider_with_fake_client(fake)
    request = _provider_request(content="a distinctive marker only present via the Prompt Specification")

    provider.generate(request=request)

    # The rendered input reflects the PromptSpecification's own content
    # (governance/system layers included), not an independently
    # reconstructed string from raw request.evidence.
    assert "a distinctive marker only present via the Prompt Specification" in fake.received_kwargs["input"]
    assert "[System]" in fake.received_kwargs["input"]
    assert "[Governance]" in fake.received_kwargs["input"]


# --- mocked integration test: ProviderGenerationRequest -> adapter ------------
# -> mocked OpenAI SDK -> plain str -> existing generation response path ------


def test_mocked_end_to_end_generation_path_produces_a_generated_candidate_response():
    fake = _FakeResponsesEndpoint(output_text="a real substantive answer, not the deterministic placeholder")
    provider = _provider_with_fake_client(fake)

    evidence_item = _evidence_item(content="actual governed clinical prose about gastric adenocarcinoma")
    context = GenerationContext(
        integration_id="INT-1",
        integration_timestamp=datetime.now(UTC),
        request_text="What is Gastric Adenocarcinoma?",
        navigation_context=NavigationContextPlaceholder(),
        rtep=RuntimeEvidencePackage(
            metadata=RuntimeEvidenceMetadata(
                evidence_package_id="EP-1",
                retrieval_id="RID-1",
                navigation_context_id="NAV-1",
                retrieval_policy_version="1.0",
                knowledge_base_version="1.0",
                generation_timestamp=datetime.now(UTC),
            ),
            evidence=(evidence_item,),
        ),
        runtime_constraints=RuntimeConstraints(),
        evidence_state=EvidenceState.HAS_EVIDENCE,
        safety_decision=_safety_decision(),
    )

    result = generate_candidate_response(context, provider)

    assert result.outcome.value == "GENERATED"
    assert result.response is not None
    assert result.response.content == "a real substantive answer, not the deterministic placeholder"
    assert result.response.provider_name == "OpenAIProvider"
    # Proves the real evidence content actually reached the OpenAI call.
    assert "actual governed clinical prose about gastric adenocarcinoma" in fake.received_kwargs["input"]
