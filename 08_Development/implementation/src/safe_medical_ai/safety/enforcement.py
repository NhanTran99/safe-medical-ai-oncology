"""Deterministic Safety Enforcement boundary — Task #009."""

from __future__ import annotations

import uuid
from datetime import UTC, datetime

from .models import RiskClass, SafetyAction, SafetyDecision, SafetyInput


def evaluate_safety(safety_input: SafetyInput | None) -> SafetyDecision:
    """Return one immutable, fail-closed SafetyDecision."""
    if safety_input is None:
        return _decision(
            "unknown-request",
            "safety-unknown",
            RiskClass.HIGH,
            SafetyAction.REJECT,
            reason="SAFETY_ENGINE_FAILURE",
        )

    # Emergency is a risk class, not a seventh action.
    if safety_input.risk_class is RiskClass.EMERGENCY:
        return _decision(
            safety_input.request_id,
            safety_input.policy_version,
            RiskClass.EMERGENCY,
            SafetyAction.ESCALATE,
            reason="EMERGENCY_PRECEDENCE",
        )

    # Default deny: only explicit authorization can enter the normal path.
    if safety_input.authorized is not True:
        return _decision(
            safety_input.request_id,
            safety_input.policy_version,
            safety_input.risk_class,
            SafetyAction.REJECT,
            reason="DEFAULT_DENY",
        )

    if safety_input.prohibited:
        return _decision(
            safety_input.request_id,
            safety_input.policy_version,
            safety_input.risk_class,
            SafetyAction.REJECT,
            reason="PROHIBITED_CAPABILITY",
        )

    if safety_input.escalation_required:
        return _decision(
            safety_input.request_id,
            safety_input.policy_version,
            safety_input.risk_class,
            SafetyAction.ESCALATE,
            reason="ESCALATION_REQUIRED",
        )

    if safety_input.redirect_required:
        return _decision(
            safety_input.request_id,
            safety_input.policy_version,
            safety_input.risk_class,
            SafetyAction.REDIRECT,
            reason="REDIRECT_REQUIRED",
        )

    if safety_input.clarification_required:
        return _decision(
            safety_input.request_id,
            safety_input.policy_version,
            safety_input.risk_class,
            SafetyAction.ASK_CLARIFICATION,
            reason="CLARIFICATION_REQUIRED",
        )

    if safety_input.warning_required:
        return _decision(
            safety_input.request_id,
            safety_input.policy_version,
            safety_input.risk_class,
            SafetyAction.ALLOW_WITH_WARNING,
            reason="WARNING_REQUIRED",
        )

    return _decision(
        safety_input.request_id,
        safety_input.policy_version,
        safety_input.risk_class,
        SafetyAction.ALLOW,
        reason="AUTHORIZED_REQUEST",
    )


def _decision(
    request_id: str,
    policy_version: str,
    risk_class: RiskClass,
    action: SafetyAction,
    *,
    reason: str,
) -> SafetyDecision:
    return SafetyDecision(
        request_id=request_id,
        decision_id=uuid.uuid4().hex,
        policy_version=policy_version,
        risk_class=risk_class,
        reason_code=reason,
        action=action,
        timestamp=datetime.now(UTC),
    )
