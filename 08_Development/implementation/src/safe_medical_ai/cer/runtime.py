"""Controlled Evaluation Runtime orchestration.

This is a thin composition layer around the already-locked boundaries:

Safety -> Retrieval -> RTEP Assembly -> Runtime Integration ->
Generation -> Validation.

The orchestrator owns sequencing and atomic stage disposition only. It does
not implement clinical reasoning, retrieval ranking, evidence repair, safety
adjudication, generation, or validation logic.
"""

from __future__ import annotations

import logging

from ..evidence import assemble_runtime_evidence_package
from ..generation import GenerationOutcome, generate_candidate_response
from ..integration import RuntimeIntegrationInput, integrate_runtime_context
from ..llm.base import LLMAdapter
from ..retrieval import RetrievalOutcome, RetrievalService, RepositorySource
from ..safety import SafetyAction, evaluate_safety
from ..validation import CandidateValidationOutcome, ValidationInput, validate_candidate_response
from .models import CEROutcome, CERRequest, CERResult

logger = logging.getLogger(__name__)


class CERRuntime:
    """Thin dependency-injected orchestrator for controlled evaluation."""

    def __init__(self, *, repository_source: RepositorySource, provider: LLMAdapter):
        self._retrieval = RetrievalService(repository_source)
        self._provider = provider

    def run(self, request: CERRequest) -> CERResult:
        """Run one explicit CER attempt; fail closed at every boundary."""

        if request.safety_input.request_id != request.request_id:
            return CERResult(
                outcome=CEROutcome.SAFETY_BLOCKED,
                message="request_id mismatch between CERRequest and SafetyInput",
            )

        safety_decision = evaluate_safety(request.safety_input)
        if safety_decision.action not in {
            SafetyAction.ALLOW,
            SafetyAction.ALLOW_WITH_WARNING,
        }:
            return CERResult(
                outcome=CEROutcome.SAFETY_BLOCKED,
                safety_decision=safety_decision,
                message="CER stopped at safety gate; generation was not attempted",
            )

        retrieval_response = self._retrieval.retrieve(request.retrieval_request)
        if retrieval_response.outcome in {
            RetrievalOutcome.INVALID_REQUEST,
            RetrievalOutcome.NOT_FOUND,
        }:
            return CERResult(
                outcome=CEROutcome.RETRIEVAL_FAILURE,
                safety_decision=safety_decision,
                retrieval_response=retrieval_response,
                message=retrieval_response.message,
            )

        assembly_result = assemble_runtime_evidence_package(
            retrieval_response,
            context=request.rtep_context,
            provenance=request.provenance,
        )
        if assembly_result.package is None:
            return CERResult(
                outcome=CEROutcome.EVIDENCE_ASSEMBLY_FAILURE,
                safety_decision=safety_decision,
                retrieval_response=retrieval_response,
                assembly_result=assembly_result,
                message=assembly_result.message,
            )

        integration_result = integrate_runtime_context(
            RuntimeIntegrationInput(
                request_text=request.request_text,
                navigation_context=request.navigation_context,
                rtep=assembly_result.package,
                runtime_constraints=request.runtime_constraints,
                safety_decision=safety_decision,
            )
        )
        if integration_result.context is None:
            return CERResult(
                outcome=CEROutcome.INTEGRATION_FAILURE,
                safety_decision=safety_decision,
                retrieval_response=retrieval_response,
                assembly_result=assembly_result,
                integration_result=integration_result,
                message=integration_result.message,
            )

        generation_result = generate_candidate_response(
            integration_result.context,
            self._provider,
        )
        if generation_result.response is None:
            return CERResult(
                outcome=CEROutcome.GENERATION_FAILURE,
                safety_decision=safety_decision,
                retrieval_response=retrieval_response,
                assembly_result=assembly_result,
                integration_result=integration_result,
                generation_result=generation_result,
                message=generation_result.message,
            )

        validation_result = validate_candidate_response(
            ValidationInput(
                candidate_response=generation_result.response,
                rtep=assembly_result.package,
                validation_policy_version=request.validation_policy_version,
            )
        )

        if validation_result.outcome is CandidateValidationOutcome.SAFE_FALLBACK:
            return CERResult(
                outcome=CEROutcome.SAFE_FALLBACK,
                safety_decision=safety_decision,
                retrieval_response=retrieval_response,
                assembly_result=assembly_result,
                integration_result=integration_result,
                generation_result=generation_result,
                validation_result=validation_result,
                message=validation_result.message,
            )

        if validation_result.outcome is not CandidateValidationOutcome.VALID:
            return CERResult(
                outcome=CEROutcome.VALIDATION_FAILURE,
                safety_decision=safety_decision,
                retrieval_response=retrieval_response,
                assembly_result=assembly_result,
                integration_result=integration_result,
                generation_result=generation_result,
                validation_result=validation_result,
                message=validation_result.message,
            )

        return CERResult(
            outcome=CEROutcome.COMPLETED,
            safety_decision=safety_decision,
            retrieval_response=retrieval_response,
            assembly_result=assembly_result,
            integration_result=integration_result,
            generation_result=generation_result,
            validation_result=validation_result,
            message=None,
        )
