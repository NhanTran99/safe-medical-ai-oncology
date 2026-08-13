"""Minimal typed placeholders reflecting OUTPUT_CONTRACT.md.

`ValidationOutcome` encodes the locked controlled vocabulary from
OUTPUT_CONTRACT.md section 8 (PASS / FAIL / SAFE FALLBACK) — this is
governance vocabulary, not an implementation decision, so it is safe to
fix here.

The remaining classes are intentionally empty structural placeholders.
Field-level schema for the Navigation Context, Runtime Evidence Package,
and generated-response models is explicitly deferred per
OUTPUT_CONTRACT.md section 11 and TECH_STACK.md section 4, and must not be
locked by this scaffolding task.
"""

from __future__ import annotations

from enum import Enum

from pydantic import BaseModel


class ValidationOutcome(str, Enum):
    """Controlled output-validation outcomes (OUTPUT_CONTRACT.md §8)."""

    PASS = "PASS"
    FAIL = "FAIL"
    SAFE_FALLBACK = "SAFE_FALLBACK"


class NavigationContextPlaceholder(BaseModel):
    """Structural placeholder for the future Navigation Context model.

    Field-level schema is deferred; do not add fields without an
    approved implementation specification.
    """


class RuntimeEvidencePackagePlaceholder(BaseModel):
    """Structural placeholder for the future Runtime Evidence Package model.

    See EVIDENCE_PACKAGE_SPECIFICATION.md. Field-level schema is deferred.
    """


class GeneratedResponsePlaceholder(BaseModel):
    """Structural placeholder for the future generated-response model.

    See OUTPUT_CONTRACT.md §4 (canonical output structure). Field-level
    schema is deferred.
    """
