"""Runtime Evidence Package (RTEP) boundary — Task #005.

Public interface: `RuntimeEvidencePackage`, `RuntimeEvidenceMetadata`,
`EvidenceItem`, `EvidenceItemProvenance`, `RTEPAssemblyContext`,
`RTEPAssemblyOutcome`, `RTEPAssemblyResult`,
`assemble_runtime_evidence_package`.

Does not implement Generation, Validation, semantic/vector retrieval,
embeddings, an LLM, or clinical reasoning. See `EVIDENCE_PACKAGE_SPECIFICATION.md`
and the Task #005 Implementation Specification for the governed contract this
module implements.
"""

from .assembly import assemble_runtime_evidence_package
from .models import (
    EvidenceItem,
    EvidenceItemProvenance,
    RTEPAssemblyContext,
    RTEPAssemblyOutcome,
    RTEPAssemblyResult,
    RuntimeEvidenceMetadata,
    RuntimeEvidencePackage,
)

__all__ = [
    "EvidenceItem",
    "EvidenceItemProvenance",
    "RTEPAssemblyContext",
    "RTEPAssemblyOutcome",
    "RTEPAssemblyResult",
    "RuntimeEvidenceMetadata",
    "RuntimeEvidencePackage",
    "assemble_runtime_evidence_package",
]
