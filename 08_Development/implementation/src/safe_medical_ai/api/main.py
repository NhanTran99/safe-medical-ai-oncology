"""Minimal FastAPI application.

Exposes a health-check endpoint only. Per Task #002 scope, no retrieval,
generation, or output-validation business logic is wired into the API
layer. Orchestration/business logic must remain separable from this API
layer per TECH_STACK.md section 2.1.
"""

from __future__ import annotations

import json
import uuid
from pathlib import Path

from pydantic import BaseModel, Field

from ..cases import CaseResolutionOutcome, CaseResolutionResult, EvaluationCaseResolver
from ..cer import CEROutcome, CERRequest, CERResult, CERRuntime
from ..evidence import EvidenceItemProvenance, RTEPAssemblyContext
from ..integration import EvidenceState, RuntimeConstraints
from ..llm.base import LLMAdapter
from ..llm.openai_provider import OpenAIProvider
from ..models.output_contract import NavigationContextPlaceholder
from ..retrieval import FilesystemRepositorySource, RetrievalRequest
from ..safety import RiskClass, SafetyInput

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse

from ..config import get_settings
from ..logging_setup import configure_logging
from ..trace import set_trace_id
from .chat_ui import render_chat_page

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


# --- Phase 6 Stage 2 Track 1/2: Controlled Chat UI + generic case execution -
#
# `/chat` renders the Chat UI page with a controlled navigation catalog
# (Situation -> Topic -> Question Starter) built from the SAME manifest
# projection `EvaluationCaseResolver` uses. `/chat/query` and
# `/cer/evaluate` both submit an approved Evaluation Case through the SAME
# governed CER execution path (`_run_controlled_evaluation`), which
# resolves any approved `case_id` (EC-0001..EC-0239) via
# `EvaluationCaseResolver`. Neither endpoint accepts an arbitrary
# client-supplied `population_id`, and neither has any fixed/default
# `case_id` -- the browser always supplies the case_id selected via the
# controlled navigation catalog (Track 2 RC-1/RC-2).


def _projection_path() -> Path:
    repo_root = Path(__file__).resolve().parents[5]
    return (
        repo_root
        / "08_Development"
        / "implementation"
        / "data"
        / "evaluation_case_manifest_projection.json"
    )


def _default_case_resolver() -> EvaluationCaseResolver:
    return EvaluationCaseResolver(_projection_path())


def _situation_mapping_path() -> Path:
    repo_root = Path(__file__).resolve().parents[5]
    return (
        repo_root
        / "08_Development"
        / "implementation"
        / "data"
        / "b06_situation_navigation_mapping.json"
    )


def _load_situation_mapping() -> dict[str, list]:
    """Load the B06 governed Situation -> Topic navigation mapping.

    Navigation metadata only (see `data/B06_SITUATION_NAVIGATION_MAPPING_README.md`):
    every `case_id` referenced still resolves solely through
    `EvaluationCaseResolver` / the same manifest projection
    `_load_navigation_catalog()` reads -- this file never becomes a second
    PP/case authority, only a filter over the existing `CATALOG`.
    """
    try:
        raw = json.loads(_situation_mapping_path().read_text(encoding="utf-8"))
    except Exception:
        return {"situations": [], "mappings": []}
    return {
        "situations": raw.get("situations", []),
        "mappings": raw.get("mappings", []),
    }


def _primary_source_registry_path() -> Path:
    repo_root = Path(__file__).resolve().parents[5]
    return (
        repo_root
        / "08_Development"
        / "implementation"
        / "data"
        / "b09_primary_source_registry.json"
    )


def _load_primary_source_registry() -> dict[str, str]:
    """Load the B09 governed population_id -> Primary Source Set mapping.

    Display metadata only (see `data/B09_PRIMARY_SOURCE_REGISTRY_README.md`):
    this file never becomes a second PP/case authority -- it is consulted
    only after `population_id` has already been resolved through the
    existing retrieval path, purely to look up the human-readable source
    label for display. Values are copied verbatim from the governed
    Population Registry; nothing here is inferred, expanded, or invented.
    """
    try:
        raw = json.loads(_primary_source_registry_path().read_text(encoding="utf-8"))
    except Exception:
        return {}
    return {
        entry["population_id"]: entry["primary_source_set"]
        for entry in raw.get("entries", [])
        if entry.get("population_id") and entry.get("primary_source_set")
    }


def _format_primary_source_set(raw_primary_source_set: str) -> list[str]:
    """Split a governed Primary Source Set value into its constituent
    source labels, using the Registry's own `" + "` separator convention.

    Never expands an abbreviation to a full guideline name, never infers,
    and never invents additional text -- only surrounding whitespace is
    trimmed from each token, so any stray trailing character already
    present in the Registry value (a small number of entries end in a
    stray ".") is preserved rather than silently "corrected".
    """
    return [token.strip() for token in raw_primary_source_set.split(" + ") if token.strip()]


def _resolve_primary_source_set(result: CERResult) -> list[str] | None:
    """B09: resolve the governed, human-readable Primary Source Set
    associated with the evidence actually used to generate this answer.

    Three-state result (never conflated, per B09's locked missing-source
    behavior):

    - `None`: no real generation evidence applies to this outcome (a
      safety block, or a retrieval/assembly/integration/generation/
      validation failure, or the locked EMPTY_EVIDENCE_RESPONSE branch --
      that branch's fixed response text already discloses "no evidence was
      retrieved", so no separate source note is added here).
    - `[]` (empty list): real evidence WAS used for generation, but no
      valid Primary Source Set mapping exists for its population_id in the
      governed Registry (or the evidence chain's own identity could not be
      confirmed -- see the `evidence_package_id` check below). The Chat UI
      shows the honest "Evidence information unavailable" fallback for
      this case, never a fabricated or PP-ID-based source label.
    - non-empty list: the governed Primary Source Set values for the PP
      whose evidence was actually used to generate this answer.

    Provenance integrity: `response.evidence_package_id` is asserted equal
    to the `evidence_package_id` of the RTEP this same result actually
    assembled (`assembly_result.package.metadata`) before the
    `population_id` used for the Registry lookup is trusted -- the same
    identity the evidence chain already carries end to end (RTEP Assembly
    -> Runtime Integration -> Generation), never re-derived here.
    """
    if result.outcome is not CEROutcome.COMPLETED:
        return None

    generation_result = result.generation_result
    response = generation_result.response if generation_result is not None else None
    if response is None or response.evidence_state is not EvidenceState.HAS_EVIDENCE:
        return None

    assembly_result = result.assembly_result
    package = assembly_result.package if assembly_result is not None else None
    retrieval_response = result.retrieval_response
    if (
        package is None
        or retrieval_response is None
        or response.evidence_package_id != package.metadata.evidence_package_id
    ):
        return []

    population_id = retrieval_response.request.population_id
    raw_primary_source_set = _load_primary_source_registry().get(population_id)
    if not raw_primary_source_set:
        return []

    return _format_primary_source_set(raw_primary_source_set)


def _load_navigation_catalog() -> list[dict[str, str]]:
    """Load the Chat UI's controlled navigation catalog from the same
    manifest projection `EvaluationCaseResolver` uses.

    Only `case_id` / `pp_title` / `controlled_question` are extracted --
    never used for case *resolution* (that is `EvaluationCaseResolver`'s
    job alone), only for rendering non-clinical navigation labels and
    pre-approved question-starter text. Never a second manifest: this is
    the same projection file, read again for a different (display) purpose.
    """
    try:
        raw = json.loads(_projection_path().read_text(encoding="utf-8"))
    except Exception:
        return []
    return [
        {
            "case_id": entry["case_id"],
            "pp_title": entry["pp_title"],
            "controlled_question": entry["controlled_question"],
        }
        for entry in raw.get("cases", [])
    ]


@app.get("/chat", response_class=HTMLResponse)
def chat_ui() -> HTMLResponse:
    """Controlled Chat UI shell. Presentation only — no business logic.

    `Cache-Control: no-store` is defensive only: it stops a browser from
    ever serving a stale cached copy of this page (with stale embedded
    catalog data or stale navigation JS) across reloads/deploys. It is not
    a substitute for restarting the dev server after an in-place code
    change -- Python does not hot-reload a running process's already-
    imported module code.
    """
    return HTMLResponse(
        content=render_chat_page(_load_navigation_catalog(), _load_situation_mapping()),
        headers={"Cache-Control": "no-store"},
    )


class ChatQueryRequest(BaseModel):
    """Chat-submission request (Track 2).

    `case_id` is required, with no default of any kind: the browser's
    controlled navigation catalog (Situation -> Topic -> Question Starter,
    see `chat_ui.py`) always supplies an approved `case_id` selected from
    real manifest data. There is no PP-selection field, and no fixed/
    default case anywhere in this contract or `chat_query()` below.
    """
    message: str = Field(min_length=1)
    case_id: str = Field(min_length=1)


class ChatQueryResponse(BaseModel):
    """Chat-submission response.

    `status` carries the same outcome value space `/cer/evaluate` returns
    as `outcome` (either a `CEROutcome` value, or a `CaseResolutionOutcome`
    value if resolution itself failed). `answer` is the governed generated
    content when one exists, or the governed stage message otherwise —
    never text invented by this endpoint.

    `sources` (B09) is the governed, human-readable Primary Source Set for
    the evidence actually used to generate `answer` -- see
    `_resolve_primary_source_set()`'s three-state contract: `None` when no
    real generation evidence applies to this outcome, `[]` when evidence
    was used but no valid Registry mapping was found (Chat UI shows an
    honest "unavailable" fallback), or a populated list of source labels.
    Never a PP identifier.
    """
    answer: str
    status: str
    sources: list[str] | None = None


@app.post("/chat/query", response_model=ChatQueryResponse)
def chat_query(request: ChatQueryRequest) -> ChatQueryResponse:
    """Submit the question through the existing governed CER execution
    path, reusing `_run_controlled_evaluation` exactly as `/cer/evaluate`
    does. No second CER implementation and no new retrieval/generation/
    validation/safety logic is introduced here.
    """
    outcome = _run_controlled_evaluation(
        ControlledEvaluationRequest(request_text=request.message, case_id=request.case_id)
    )

    if isinstance(outcome, CaseResolutionResult):
        return ChatQueryResponse(
            answer=outcome.message or "This request could not be resolved to an approved case.",
            status=outcome.outcome.value,
        )

    result = outcome
    if result.generation_result is not None and result.generation_result.response is not None:
        answer = result.generation_result.response.content
    else:
        answer = result.message or "No response was produced for this request."

    return ChatQueryResponse(
        answer=answer,
        status=result.outcome.value,
        sources=_resolve_primary_source_set(result),
    )


class ControlledEvaluationRequest(BaseModel):
    """Governed controlled-execution request (Track 2).

    Carries an approved `case_id` (`EC-0001`..`EC-0239`), never a
    client-supplied `population_id`: the executed PP is always resolved
    internally from the frozen Evaluation Case Manifest projection via
    `EvaluationCaseResolver`, never accepted as arbitrary caller authority.
    """
    request_text: str = Field(min_length=1)
    case_id: str = Field(min_length=1)


class DeterministicLocalProvider(LLMAdapter):
    """Development / Controlled Evaluation only. Not a clinical provider."""

    def generate(self, *, request):
        return (
            "Controlled Evaluation deterministic response. "
            "Not for clinical decision-making."
        )


def _select_provider() -> LLMAdapter:
    """Minimal provider selection (Track 3 BATCH 02).

    The OpenAI provider is used only when `settings.openai_api_key` is
    explicitly configured; otherwise `DeterministicLocalProvider` is used
    unchanged, so offline/no-key development and the existing test suite
    remain unaffected by default. This is a single explicit choice, not a
    plugin/provider registry.
    """
    if settings.openai_api_key:
        return OpenAIProvider(api_key=settings.openai_api_key, model=settings.openai_model)
    return DeterministicLocalProvider()


def _run_controlled_evaluation(request: ControlledEvaluationRequest, *, provider: LLMAdapter | None = None):
    """Resolve `request.case_id` and, only on success, run the existing
    governed CER path for the resolved PP. Returns a `CaseResolutionResult`
    (never `RESOLVED`) if resolution fails -- fail-closed, no fallback to
    any specific case.

    `provider` is optional and defaults to the existing `_select_provider()`
    choice (unchanged behavior for both existing HTTP callers, neither of
    which pass it). B07's campaign harness (`campaign/harness.py`) is the
    only caller that supplies it explicitly, so it can inject a specific
    provider (e.g. the deterministic provider for reproducible tests)
    without depending on process environment state -- this is the same
    single execution path, not a second one.
    """
    resolution = _default_case_resolver().resolve(request.case_id)
    if resolution.outcome is not CaseResolutionOutcome.RESOLVED:
        return resolution

    resolved_case = resolution.case

    repo_root = Path(__file__).resolve().parents[5]
    source_root = (
        repo_root
        / "03_Clinical_Knowledge"
        / "population"
        / "population_packages"
    )

    request_id = f"WEB-CER-{resolved_case.population_id}-{uuid.uuid4().hex[:12]}"
    retrieval_id = f"{request_id}-RET"
    navigation_id = f"{request_id}-NAV"
    artifact_type_value = resolved_case.expected_primary_artifact_type.value

    cer_request = CERRequest(
        request_id=request_id,
        request_text=request.request_text,
        retrieval_request=RetrievalRequest(
            population_id=resolved_case.population_id,
            artifact_type=resolved_case.expected_primary_artifact_type,
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
                knowledge_object_id=f"{artifact_type_value}-{resolved_case.population_id}",
                knowledge_passport_id=f"KP-{resolved_case.population_id}",
                source_id=f"{resolved_case.population_id}-LAYER-A",
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
        provider=provider if provider is not None else _select_provider(),
    ).run(cer_request)


@app.post("/cer/evaluate")
def controlled_evaluate(request: ControlledEvaluationRequest):
    """Phase 6 development / controlled-evaluation endpoint only.

    Internal controlled execution boundary (Track 2): accepts an approved
    `case_id`, never an arbitrary `population_id` -- the executed PP is
    always resolved from the frozen Evaluation Case Manifest projection.
    """
    outcome = _run_controlled_evaluation(request)

    if isinstance(outcome, CaseResolutionResult):
        return {
            "outcome": "CASE_NOT_APPROVED",
            "case_resolution": outcome.outcome.value,
            "message": outcome.message,
            "safety": None,
            "retrieval": None,
            "retrieval_results": 0,
            "assembly": None,
            "integration": None,
            "generation": None,
            "validation": None,
            "boundary": {
                "mode": "RESEARCH / DEVELOPMENT / CONTROLLED EVALUATION ONLY",
                "formal_validation": "NOT STARTED",
                "execution_authorization": "NOT GRANTED",
                "vc_clin": "DEFERRED",
            },
        }

    result = outcome
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
