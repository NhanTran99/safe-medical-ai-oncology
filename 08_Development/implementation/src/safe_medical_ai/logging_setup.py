"""Structured logging foundation.

Provides JSON-structured log records that include the current trace id
(see `trace.py`). Uses only the standard library so this scaffolding does
not lock in a third-party logging vendor — a deferred decision beyond the
scope of Task #002.
"""

from __future__ import annotations

import json
import logging
import sys
from typing import Any

from .trace import get_trace_id


class StructuredFormatter(logging.Formatter):
    """Renders log records as single-line JSON with trace-id context."""

    def format(self, record: logging.LogRecord) -> str:
        payload: dict[str, Any] = {
            "timestamp": self.formatTime(record, "%Y-%m-%dT%H:%M:%S%z"),
            "level": record.levelname,
            "logger": record.name,
            "message": record.getMessage(),
            "trace_id": get_trace_id(),
        }
        if record.exc_info:
            payload["exception"] = self.formatException(record.exc_info)
        return json.dumps(payload)


def configure_logging(level: str = "INFO") -> None:
    """Configure root logging with the structured JSON formatter.

    Idempotent: safe to call multiple times (e.g. once per test) without
    duplicating handlers.
    """
    root = logging.getLogger()
    root.setLevel(level)

    handler = logging.StreamHandler(stream=sys.stdout)
    handler.setFormatter(StructuredFormatter())

    root.handlers = [handler]
