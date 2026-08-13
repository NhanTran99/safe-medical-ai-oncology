"""Trace-ID foundation for request/interaction traceability.

Per OUTPUT_CONTRACT.md §10, the implementation must preserve a
request/interaction trace identifier. This module provides the minimal
context-local trace-ID mechanism used by the logging foundation and the API
layer; it does not implement audit storage or downstream propagation
policy.
"""

from __future__ import annotations

import uuid
from contextvars import ContextVar

_trace_id_var: ContextVar[str | None] = ContextVar("trace_id", default=None)


def new_trace_id() -> str:
    """Generate a new trace identifier."""
    return uuid.uuid4().hex


def set_trace_id(trace_id: str | None = None) -> str:
    """Set (or generate) the trace id for the current context and return it."""
    resolved = trace_id or new_trace_id()
    _trace_id_var.set(resolved)
    return resolved


def get_trace_id() -> str | None:
    """Return the trace id for the current context, if any."""
    return _trace_id_var.get()
