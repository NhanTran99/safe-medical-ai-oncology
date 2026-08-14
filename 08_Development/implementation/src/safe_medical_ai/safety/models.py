"""Typed Safety Enforcement contracts — Task #009."""

from __future__ import annotations

from datetime import datetime
from enum import Enum

from pydantic import BaseModel, ConfigDict, Field


class RiskClass(str, Enum):
    LOW = "LOW"
    MODERATE = "MODERATE"
    HIGH = "HIGH"
    EMERGENCY = "EMERGENCY"


class SafetyAction(str, Enum):
    ALLOW = "ALLOW"
    ALLOW_WITH_WARNING = "ALLOW_WITH_WARNING"
    ASK_CLARIFICATION = "ASK_CLARIFICATION"
    REDIRECT = "REDIRECT"
    ESCALATE = "ESCALATE"
    REJECT = "REJECT"


class SafetyDecision(BaseModel):
    model_config = ConfigDict(frozen=True)

    request_id: str = Field(min_length=1)
    decision_id: str = Field(min_length=1)
    policy_version: str = Field(min_length=1)
    risk_class: RiskClass
    reason_code: str = Field(min_length=1)
    action: SafetyAction
    timestamp: datetime


class SafetyInput(BaseModel):
    model_config = ConfigDict(frozen=True)

    request_id: str = Field(min_length=1)
    policy_version: str = Field(min_length=1)
    authorized: bool | None
    risk_class: RiskClass
    prohibited: bool = False
    warning_required: bool = False
    clarification_required: bool = False
    redirect_required: bool = False
    escalation_required: bool = False
