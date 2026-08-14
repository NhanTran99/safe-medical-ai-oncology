from datetime import UTC, datetime

import pytest
from pydantic import ValidationError

from safe_medical_ai.safety import RiskClass, SafetyAction, SafetyDecision, SafetyInput


def test_risk_vocabulary_is_exact():
    assert {x.value for x in RiskClass} == {"LOW", "MODERATE", "HIGH", "EMERGENCY"}


def test_action_vocabulary_is_exact():
    assert {x.value for x in SafetyAction} == {
        "ALLOW", "ALLOW_WITH_WARNING", "ASK_CLARIFICATION",
        "REDIRECT", "ESCALATE", "REJECT",
    }


def test_emergency_is_not_an_action():
    assert "EMERGENCY" not in {x.value for x in SafetyAction}


def test_decision_is_immutable():
    decision = SafetyDecision(
        request_id="r1",
        decision_id="d1",
        policy_version="p1",
        risk_class=RiskClass.LOW,
        reason_code="OK",
        action=SafetyAction.ALLOW,
        timestamp=datetime.now(UTC),
    )
    with pytest.raises(ValidationError):
        decision.action = SafetyAction.REJECT


def test_input_is_immutable():
    value = SafetyInput(
        request_id="r1",
        policy_version="p1",
        authorized=True,
        risk_class=RiskClass.LOW,
    )
    with pytest.raises(ValidationError):
        value.authorized = False
