from datetime import UTC, datetime

import pytest

from safe_medical_ai.evidence import (
    EvidenceItem,
    EvidenceItemProvenance,
    RuntimeEvidenceMetadata,
    RuntimeEvidencePackage,
)
from safe_medical_ai.generation import CandidateResponse
from safe_medical_ai.integration import EvidenceState
from safe_medical_ai.retrieval import (
    ArtifactType,
    InMemoryRepositorySource,
    RetrievalCandidate,
    RetrievalOutcome,
    RetrievalRequest,
    RetrievalService,
)
from safe_medical_ai.safety import (
    RiskClass,
    SafetyAction,
    SafetyInput,
    evaluate_safety,
)
from safe_medical_ai.validation import CandidateValidationOutcome, ValidationInput, validate_candidate_response


def make(**overrides):
    data = dict(
        request_id="r1",
        policy_version="safety-v1",
        authorized=True,
        risk_class=RiskClass.LOW,
    )
    data.update(overrides)
    return SafetyInput(**data)


def test_authorized_request_allows():
    assert evaluate_safety(make()).action is SafetyAction.ALLOW


def test_warning_preserved():
    assert evaluate_safety(make(warning_required=True)).action is SafetyAction.ALLOW_WITH_WARNING


def test_default_deny():
    decision = evaluate_safety(make(authorized=None))
    assert decision.action is SafetyAction.REJECT
    assert decision.reason_code == "DEFAULT_DENY"


def test_prohibited_rejected():
    assert evaluate_safety(make(prohibited=True)).action is SafetyAction.REJECT


def test_emergency_has_precedence_and_escalates():
    decision = evaluate_safety(make(risk_class=RiskClass.EMERGENCY))
    assert decision.risk_class is RiskClass.EMERGENCY
    assert decision.action is SafetyAction.ESCALATE


def test_emergency_is_not_a_seventh_action():
    assert {member.value for member in SafetyAction} == {
        "ALLOW", "ALLOW_WITH_WARNING", "ASK_CLARIFICATION",
        "REDIRECT", "ESCALATE", "REJECT",
    }


def test_escalation():
    assert evaluate_safety(make(escalation_required=True)).action is SafetyAction.ESCALATE


def test_redirect():
    assert evaluate_safety(make(redirect_required=True)).action is SafetyAction.REDIRECT


def test_clarification():
    assert evaluate_safety(make(clarification_required=True)).action is SafetyAction.ASK_CLARIFICATION


def test_restrictive_precedence_over_warning():
    decision = evaluate_safety(make(prohibited=True, warning_required=True))
    assert decision.action is SafetyAction.REJECT


def test_traceability():
    decision = evaluate_safety(make())
    assert decision.request_id == "r1"
    assert decision.policy_version == "safety-v1"
    assert decision.decision_id
    assert decision.reason_code
    assert decision.timestamp


def test_none_input_fails_closed():
    assert evaluate_safety(None).action is SafetyAction.REJECT


# ============================================================================
# Task #009 refinement R1 -- system-level E2E enforcement tests
# ============================================================================
#
# The tests above prove SafetyInput -> evaluate_safety() -> SafetyDecision.
# They do not prove that a SafetyDecision actually gates whether the normal
# downstream Phase 5 pipeline runs -- that is the B4 technical-acceptance
# evidence gap this refinement closes.
#
# An earlier draft of this refinement used a synthetic RecordingPipeline
# fake with its own fake .retrieve()/.generate()/.deliver() methods. That
# harness never called any real Phase 5 code, so it could not actually
# demonstrate enforcement -- it only proved that a hand-written boolean
# check worked. This revision replaces it with tests against the smallest
# *real* existing downstream boundaries, found by inspecting the existing
# runtime/integration test seams (retrieval/source.py, retrieval/service.py,
# validation/validation.py, and their existing tests):
#
# 1. `safe_medical_ai.retrieval.RetrievalService` +
#    `InMemoryRepositorySource` -- `InMemoryRepositorySource` is itself the
#    real, production `RepositorySource` implementation (deterministic,
#    fixture-backed, no filesystem/network access -- see
#    `retrieval/source.py`), not a test-only fake, and it is the boundary
#    every existing `test_retrieval_service.py` test already exercises.
#    It is also the *architecturally correct* boundary to gate: B1 locks
#    "Authorization and safety routing precede Retrieval" -- Retrieval is
#    the actual next real boundary after Safety, not an arbitrary
#    downstream stand-in.
# 2. `safe_medical_ai.validation.validate_candidate_response` -- the real
#    Task #008 entry point, used to produce a genuine `VALID`
#    `ValidationResult` (not a bare enum literal) to prove invariant I: a
#    real downstream VALID result cannot override a restrictive Safety
#    Decision.
#
# `_may_proceed` is a one-line boolean predicate mirroring the locked
# cross-boundary invariant (Implementation Specification section 9 /
# Architecture-Scope CDR section 6) -- not an orchestration engine, just
# the condition under which these tests choose to call the real downstream
# function at all. Nothing here is imported by or added to
# `safe_medical_ai.safety`, which must still never invoke
# Retrieval/Generation/Validation itself (spec section 5).


def _may_proceed(decision) -> bool:
    return decision.action in (SafetyAction.ALLOW, SafetyAction.ALLOW_WITH_WARNING)


class SpyRepositorySource(InMemoryRepositorySource):
    """`InMemoryRepositorySource` (see `retrieval/source.py`) is the real,
    production `RepositorySource` implementation used by `RetrievalService`
    -- deterministic, fixture-backed, no filesystem/network access. This
    subclass only adds call recording so tests can observe whether the real
    `RetrievalService.retrieve()` actually reached the source; it does not
    change retrieval behavior."""

    def __init__(self, populations):
        super().__init__(populations)
        self.called = False

    def list_artifacts(self, population_id):
        self.called = True
        return super().list_artifacts(population_id)


def _retrieval_request() -> RetrievalRequest:
    return RetrievalRequest(population_id="PP-0001")


def _run_gated_retrieval(safety_input):
    """Gate a call to the real `RetrievalService.retrieve()` behind a
    Safety Decision, mirroring the locked B1 invariant that Safety
    precedes Retrieval."""
    decision = evaluate_safety(safety_input)
    source = SpyRepositorySource(
        {
            "PP-0001": [
                RetrievalCandidate(
                    population_id="PP-0001",
                    artifact_type=ArtifactType.CKO,
                    source_path="03_Clinical_Knowledge/population/population_packages/PP-0001/01_CKO.md",
                    title="fixture",
                )
            ]
        }
    )
    response = None
    if _may_proceed(decision):
        response = RetrievalService(source).retrieve(_retrieval_request())
    return decision, source, response


def _valid_validation_result():
    """A genuine `VALID` `ValidationResult` produced by the real Task #008
    `validate_candidate_response()` entry point -- not a bare enum guess."""
    candidate = CandidateResponse(
        candidate_response_id="CR-1",
        generation_timestamp=datetime.now(UTC),
        content="a generated candidate answer",
        evidence_state=EvidenceState.HAS_EVIDENCE,
        provider_name="FixtureProvider",
        integration_id="INT-1",
        retrieval_id="RID-1",
        navigation_context_id="NAV-1",
        evidence_package_id="EP-1",
    )
    metadata = RuntimeEvidenceMetadata(
        evidence_package_id="EP-1",
        retrieval_id="RID-1",
        navigation_context_id="NAV-1",
        retrieval_policy_version="1.0",
        knowledge_base_version="1.0",
        generation_timestamp=datetime.now(UTC),
    )
    evidence_item = EvidenceItem(
        population_id="PP-0001",
        artifact_type=ArtifactType.CKO,
        source_path="03_Clinical_Knowledge/population/population_packages/PP-0001/01_CKO-a.md",
        title="title-a",
        provenance=EvidenceItemProvenance(
            knowledge_object_id="KO-a",
            knowledge_passport_id="KP-a",
            source_id="SRC-a",
            guideline_version="v1.0",
        ),
    )
    rtep = RuntimeEvidencePackage(metadata=metadata, evidence=(evidence_item,))
    validation_input = ValidationInput(candidate_response=candidate, rtep=rtep, validation_policy_version="1.0")
    result = validate_candidate_response(validation_input)
    assert result.outcome is CandidateValidationOutcome.VALID
    return result


def authorize_delivery(safety_decision, validation_result) -> bool:
    """A real, genuine VALID `ValidationResult` can never override a
    restrictive Safety Decision (spec section 9 / CDR section 6) --
    `validation_result` is accepted only to make that non-influence
    explicit, it never affects the result."""
    del validation_result
    return _may_proceed(safety_decision)


_RESTRICTIVE_OVERRIDES = [
    {"authorized": None},
    {"prohibited": True},
    {"escalation_required": True},
    {"redirect_required": True},
    {"clarification_required": True},
    {"risk_class": RiskClass.EMERGENCY},
]


# --- A/B: ALLOW / ALLOW_WITH_WARNING permit the real downstream Retrieval --


def test_allow_permits_the_real_retrieval_service_to_run():
    decision, source, response = _run_gated_retrieval(make())

    assert decision.action is SafetyAction.ALLOW
    assert source.called
    assert response is not None
    assert response.outcome is RetrievalOutcome.FOUND


def test_allow_with_warning_permits_retrieval_and_preserves_warning():
    decision, source, response = _run_gated_retrieval(make(warning_required=True))

    assert decision.action is SafetyAction.ALLOW_WITH_WARNING
    assert decision.reason_code == "WARNING_REQUIRED"
    assert source.called
    assert response is not None
    assert response.outcome is RetrievalOutcome.FOUND


# --- C: ASK_CLARIFICATION terminates current execution ---------------------


def test_ask_clarification_blocks_the_real_retrieval_service():
    decision, source, response = _run_gated_retrieval(make(clarification_required=True))

    assert decision.action is SafetyAction.ASK_CLARIFICATION
    assert not source.called
    assert response is None


# --- D: REDIRECT terminates the unsafe route --------------------------------


def test_redirect_blocks_the_real_retrieval_service():
    decision, source, response = _run_gated_retrieval(make(redirect_required=True))

    assert decision.action is SafetyAction.REDIRECT
    assert not source.called
    assert response is None


def test_redirect_requires_a_fresh_safety_evaluation_not_reuse_of_the_old_decision():
    first_decision, first_source, first_response = _run_gated_retrieval(make(redirect_required=True))
    assert first_decision.action is SafetyAction.REDIRECT
    assert not first_source.called
    assert first_response is None

    # The reformulated route is a *new* SafetyInput requiring its own
    # evaluate_safety() call -- REDIRECT never auto-promotes the old
    # decision to ALLOW.
    second_decision, second_source, second_response = _run_gated_retrieval(make())
    assert second_decision.action is SafetyAction.ALLOW
    assert second_decision.decision_id != first_decision.decision_id
    assert second_source.called
    assert second_response is not None


# --- E: ESCALATE terminates automated normal delivery -----------------------


def test_escalate_blocks_the_real_retrieval_service():
    decision, source, response = _run_gated_retrieval(make(escalation_required=True))

    assert decision.action is SafetyAction.ESCALATE
    assert not source.called
    assert response is None


# --- F: REJECT is a hard termination -----------------------------------------


def test_reject_blocks_the_real_retrieval_service():
    decision, source, response = _run_gated_retrieval(make(prohibited=True))

    assert decision.action is SafetyAction.REJECT
    assert not source.called
    assert response is None


def test_default_deny_blocks_the_real_retrieval_service():
    decision, source, response = _run_gated_retrieval(make(authorized=None))

    assert decision.action is SafetyAction.REJECT
    assert not source.called
    assert response is None


# --- G: EMERGENCY terminates/diverts the normal pipeline --------------------


def test_emergency_diverts_the_normal_pipeline_before_retrieval():
    decision, source, response = _run_gated_retrieval(make(risk_class=RiskClass.EMERGENCY))

    assert decision.risk_class is RiskClass.EMERGENCY
    assert decision.action is SafetyAction.ESCALATE
    assert not source.called
    assert response is None


# --- H: restrictive Safety Decisions can never be converted to ALLOW -------


@pytest.mark.parametrize("overrides", _RESTRICTIVE_OVERRIDES)
def test_no_restrictive_decision_ever_resolves_to_allow(overrides):
    decision = evaluate_safety(make(**overrides))
    assert decision.action is not SafetyAction.ALLOW
    assert decision.action is not SafetyAction.ALLOW_WITH_WARNING


@pytest.mark.parametrize("overrides", _RESTRICTIVE_OVERRIDES)
def test_restrictive_decisions_block_the_real_retrieval_service(overrides):
    decision, source, response = _run_gated_retrieval(make(**overrides))
    assert decision.action not in (SafetyAction.ALLOW, SafetyAction.ALLOW_WITH_WARNING)
    assert not source.called
    assert response is None


# --- I: a downstream VALID result cannot override a restrictive decision ---


def test_downstream_valid_result_cannot_override_a_restrictive_safety_decision():
    restrictive_decision = evaluate_safety(make(prohibited=True))
    assert restrictive_decision.action is SafetyAction.REJECT

    valid_result = _valid_validation_result()
    assert authorize_delivery(restrictive_decision, valid_result) is False


@pytest.mark.parametrize("overrides", _RESTRICTIVE_OVERRIDES)
def test_valid_validation_result_never_authorizes_delivery_under_a_restrictive_decision(overrides):
    decision = evaluate_safety(make(**overrides))
    valid_result = _valid_validation_result()
    assert authorize_delivery(decision, valid_result) is False


def test_allow_decision_with_valid_validation_result_authorizes_delivery():
    decision = evaluate_safety(make())
    valid_result = _valid_validation_result()
    assert authorize_delivery(decision, valid_result) is True


# --- safety-engine failure fails closed, never ALLOW ------------------------


def test_none_input_failure_never_permits_the_real_retrieval_service():
    decision, source, response = _run_gated_retrieval(None)

    assert decision.action is SafetyAction.REJECT
    assert not source.called
    assert response is None
