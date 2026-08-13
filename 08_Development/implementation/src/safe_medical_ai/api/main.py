"""Minimal FastAPI application.

Exposes a health-check endpoint only. Per Task #002 scope, no retrieval,
generation, or output-validation business logic is wired into the API
layer. Orchestration/business logic must remain separable from this API
layer per TECH_STACK.md section 2.1.
"""

from __future__ import annotations

import uuid

from fastapi import FastAPI, Request

from ..config import get_settings
from ..logging_setup import configure_logging
from ..trace import set_trace_id

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
