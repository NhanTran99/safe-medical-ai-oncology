"""Minimal FastAPI application.

Exposes a health-check endpoint only. Per Task #002 scope, no retrieval,
generation, or output-validation business logic is wired into the API
layer. Orchestration/business logic must remain separable from this API
layer per TECH_STACK.md section 2.1.
"""

from __future__ import annotations

import uuid
from pathlib import Path

from pydantic import BaseModel, Field

from ..cer import CERRequest, CERRuntime
from ..evidence import EvidenceItemProvenance, RTEPAssemblyContext
from ..integration import RuntimeConstraints
from ..llm.base import LLMAdapter
from ..models.output_contract import NavigationContextPlaceholder
from ..retrieval import ArtifactType, FilesystemRepositorySource, RetrievalRequest
from ..safety import RiskClass, SafetyInput

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse

from ..config import get_settings
from ..logging_setup import configure_logging
from ..trace import set_trace_id
from .chat_ui import CHAT_PAGE_HTML

settings = get_settings()
configure_logging(settings.log_level)

app = FastAPI(title=settings.app_name)


@app.middleware("http")
async def trace_id_middleware(request: Request, call_next):
    incoming = request.headers.get("x-trace-id")
    trace_id = set_trace_id(incoming or uuid.uuid4().hex)
    response = await call_next(request)
    response.headers["x-trace-id"] = trace_id
    return response


@app.get("/health")
def health() -> dict[str, str]:
    """Liveness/readiness placeholder. Not a clinical or validation endpoint."""
    return {"status": "ok", "app": settings.app_name, "environment": settings.environment}


# --- Phase 6 Stage 2 Track 1: Controlled Chat UI ----------------------------
#
# `/chat` serves the Track 1A presentation-only page. `/chat/query`
# (Track 1B) submits the question through the SAME governed CER execution
# path `/cer/evaluate` already uses — `_run_controlled_evaluation`, fixed to
# PP-0002 + CKO — rather than a second CER implementation or an internal
# HTTP call. `ChatQueryRequest` carries no population/PP field, so there is
# no way for a chat submission to select or influence which PP is executed.


@app.get("/chat", response_class=HTMLResponse)
def chat_ui() -> HTMLResponse:
    """Controlled Chat UI shell. Presentation only — no business logic."""
    return HTMLResponse(content=CHAT_PAGE_HTML)


class ChatQueryRequest(BaseModel):
    """Track 1B chat-submission request. No population/PP field by design —
    PP-0002 remains the sole, fixed execution target (Track 1B boundary)."""
    message: str = Field(min_length=1)


class ChatQueryResponse(BaseModel):
    """Track 1B chat-submission response.

    `status` carries the same `CEROutcome` value space `/cer/evaluate`
    returns as `outcome`. `answer` is the governed generated content when
    one exists, or the governed CER stage message otherwise — never text
    invented by this endpoint.
    """
    answer: str
    status: str


@app.post("/chat/query", response_model=ChatQueryResponse)
def chat_query(request: ChatQueryRequest) -> ChatQueryResponse:
    """Track 1B: submit the question through the existing governed CER
    execution path (PP-0002 + CKO), reusing `_run_controlled_evaluation`
    exactly as `/cer/evaluate` does. No second CER implementation and no
    new retrieval/generation/validation/safety logic is introduced here.
    """
    result = _run_controlled_evaluation(ControlledEvaluationRequest(request_text=request.message))

    if result.generation_result is not None and result.generation_result.response is not None:
        answer = result.generation_result.response.content
    else:
        answer = result.message or "No response was produced for this request."

    return ChatQueryResponse(answer=answer, status=result.outcome.value)


class ControlledEvaluationRequest(BaseModel):
    """Minimal Phase 6 controlled-trial request."""
    request_text: str = Field(min_length=1)
    population_id: str = Field(default="PP-0002", pattern=r"^PP-0002$")


class DeterministicLocalProvider(LLMAdapter):
    """Development / Controlled Evaluation only. Not a clinical provider."""

    def generate(self, *, request):
        return (
            "Controlled Evaluation deterministic response. "
            "Not for clinical decision-making."
        )


def _run_controlled_evaluation(request: ControlledEvaluationRequest):
    repo_root = Path(__file__).resolve().parents[5]
    source_root = (
        repo_root
        / "03_Clinical_Knowledge"
        / "population"
        / "population_packages"
    )

    request_id = f"WEB-CER-PP-0002-{uuid.uuid4().hex[:12]}"
    retrieval_id = f"{request_id}-RET"
    navigation_id = f"{request_id}-NAV"

    cer_request = CERRequest(
        request_id=request_id,
        request_text=request.request_text,
        retrieval_request=RetrievalRequest(
            population_id="PP-0002",
            artifact_type=ArtifactType.CKO,
        ),
        navigation_context=NavigationContextPlaceholder(),
        runtime_constraints=RuntimeConstraints(),
        rtep_context=RTEPAssemblyContext(
            retrieval_id=retrieval_id,
            navigation_context_id=navigation_id,
            retrieval_policy_version="1.0",
            knowledge_base_version="1.0",
        ),
        provenance=(
            EvidenceItemProvenance(
                knowledge_object_id="CKO-PP-0002",
                knowledge_passport_id="KP-PP-0002",
                source_id="PP-0002-LAYER-A",
                guideline_version="1.0",
            ),
        ),
        safety_input=SafetyInput(
            request_id=request_id,
            policy_version="1.0",
            authorized=True,
            risk_class=RiskClass.LOW,
        ),
        validation_policy_version="1.0",
    )

    return CERRuntime(
        repository_source=FilesystemRepositorySource(
            source_root,
            provenance_prefix="03_Clinical_Knowledge/population/population_packages",
        ),
        provider=DeterministicLocalProvider(),
    ).run(cer_request)


@app.post("/cer/evaluate")
def controlled_evaluate(request: ControlledEvaluationRequest):
    """Phase 6 development / controlled-evaluation endpoint only."""
    result = _run_controlled_evaluation(request)

    return {
        "outcome": result.outcome.value,
        "message": result.message,
        "safety": (
            result.safety_decision.action.value
            if result.safety_decision else None
        ),
        "retrieval": (
            result.retrieval_response.outcome.value
            if result.retrieval_response else None
        ),
        "retrieval_results": (
            len(result.retrieval_response.results)
            if result.retrieval_response else 0
        ),
        "assembly": (
            "PASS" if result.assembly_result and result.assembly_result.package
            else None
        ),
        "integration": (
            "PASS" if result.integration_result and result.integration_result.context
            else None
        ),
        "generation": (
            "PASS" if result.generation_result and result.generation_result.response
            else None
        ),
        "validation": (
            result.validation_result.outcome.value
            if result.validation_result else None
        ),
        "boundary": {
            "mode": "RESEARCH / DEVELOPMENT / CONTROLLED EVALUATION ONLY",
            "formal_validation": "NOT STARTED",
            "execution_authorization": "NOT GRANTED",
            "vc_clin": "DEFERRED",
        },
    }
