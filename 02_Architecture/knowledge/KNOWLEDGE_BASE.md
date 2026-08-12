DOCUMENT METADATA

Document ID

DOC-ARC-006

Version

1.0

Status

LOCKED

Authority

ARCHITECTURE

Owner

Project Coordinator

Strategist

ChatGPT

Implementation

Claude

Depends On

SYSTEM_ARCHITECTURE.md
CLINICAL_NAVIGATION_ENGINE.md
MEDICAL_GOVERNANCE.md
SAFETY_FRAMEWORK.md
RAG_ARCHITECTURE.md

Required By

GUIDELINE_POLICY.md
EVALUATION_FRAMEWORK.md
TECH_STACK.md

Last Updated

2026-08-02

1. PURPOSE

This document defines the logical Knowledge Base Architecture of the Safe Medical AI System for Oncology Patient Education.

The Knowledge Base serves as the governed repository of clinical knowledge used by the RAG subsystem. It specifies how medical knowledge is collected, organized, governed, versioned, and made available for evidence retrieval while remaining independent of implementation technology.

2. DESIGN PHILOSOPHY

The Knowledge Base is designed according to the following principles:

Knowledge before documents
Governance before retrieval
Clinical organization before file organization
Traceability before convenience
Lifecycle management before replacement
Semantic consistency before implementation
3. ROLE WITHIN THE SYSTEM

The Knowledge Base is a logical knowledge architecture rather than a technical database.

Its responsibilities are to:

organize clinical knowledge;
maintain approved knowledge sources;
govern knowledge quality;
manage lifecycle and versioning;
provide structured access for the RAG subsystem.
4. KNOWLEDGE LAYER ARCHITECTURE

The Knowledge Base consists of four logical layers.

Knowledge Collection

Responsible for identifying and ingesting candidate medical knowledge sources.

Knowledge Organization

Responsible for organizing knowledge into Clinical Knowledge Domains and Knowledge Objects.

Knowledge Governance

Responsible for approval, lifecycle management, versioning, and validation.

Knowledge Access

Responsible for exposing governed knowledge to downstream retrieval components.

5. CLINICAL KNOWLEDGE DOMAINS

Knowledge is organized by Clinical Knowledge Domains rather than source documents.

Illustrative domains include:

Diagnosis
Staging
Surgery
Systemic Therapy
Radiotherapy
Supportive Care
Follow-up
Recurrence
Palliative Care

Individual guideline documents may contribute knowledge to multiple domains.

6. KNOWLEDGE SOURCE REGISTRY

The Knowledge Base maintains a structured Knowledge Source Registry.

Illustrative metadata include:

Source Identifier
Organization
Guideline Version
Publication Date
Jurisdiction
License
Approval Status
Lifecycle Status

The registry functions as the authoritative inventory of approved knowledge sources.

7. KNOWLEDGE LIFECYCLE

Every knowledge source follows a governed lifecycle.

Candidate
        │
        ▼
Clinical Review
        │
        ▼
Approved
        │
        ▼
Active
        │
        ▼
Deprecated
        │
        ▼
Archived

Only approved and active knowledge is eligible for downstream retrieval.

8. GUIDELINE INDEPENDENCE

Each guideline preserves its own identity within the Knowledge Base.

Guidelines are not merged during storage.

Differences between authoritative sources are preserved for downstream evidence synthesis.

9. KNOWLEDGE VERSIONING

Version control is performed at the knowledge source level.

Previous guideline versions remain preserved to support:

traceability;
auditing;
historical comparison;
research reproducibility.
10. DOMAIN METADATA

Each Clinical Knowledge Domain maintains standardized metadata.

Illustrative fields include:

Domain Name
Cancer Type
Clinical Phase
Keywords
Related Domains
Supported Evidence Levels

Domain metadata supports efficient semantic retrieval.

11. CLINICAL KNOWLEDGE OBJECT

The Clinical Knowledge Object is the fundamental semantic unit of the Knowledge Base.

Illustrative components include:

Clinical Recommendation
Supporting Evidence
Citation
Clinical Applicability
Version Information
Knowledge Domain

Knowledge Objects replace document chunks as the primary retrieval unit.

12. KNOWLEDGE VALIDATION

Knowledge Objects undergo structured validation before becoming retrievable.

Illustrative validation states include:

Draft
Clinically Reviewed
Approved
Published

Validation status determines retrieval eligibility.

13. KNOWLEDGE TRACEABILITY

Every Knowledge Object maintains traceability to:

Source Guideline
Guideline Version
Recommendation
Supporting Citation

This ensures reproducibility and transparent evidence provenance.

14. KNOWLEDGE RELATIONSHIPS

Knowledge Objects maintain logical relationships with other Knowledge Objects.

Illustrative relationships include:

Related Concepts
Sequential Clinical Steps
Contraindications
Complementary Recommendations

These relationships are logical rather than implementation-specific.

15. KNOWLEDGE DEPRECATION

Knowledge Objects are never deleted solely because they become outdated.

Deprecated objects remain available for auditing while being excluded from active retrieval.

16. RETRIEVAL ELIGIBILITY

Knowledge Objects are eligible for retrieval only when all governance requirements are satisfied.

Minimum eligibility includes:

Clinically Reviewed
Approved
Active

Additional eligibility criteria may be introduced through future governance amendments.

17. KNOWLEDGE PASSPORT

Each Knowledge Object maintains a standardized Knowledge Passport.

Illustrative metadata include:

Knowledge Object Identifier
Source
Version
Clinical Domain
Evidence Level
Approval Status
Lifecycle Status
Last Review Date
Related Knowledge Objects

The Knowledge Passport functions as the governance identity of each Knowledge Object.

18. ARCHITECTURAL PRINCIPLES

The Knowledge Base follows the following architectural principles:

Knowledge-centered organization
Governance-driven lifecycle
Traceable evidence provenance
Modular extensibility
Semantic consistency
Technology independence
19. RELATED DOCUMENTS
Upstream
SYSTEM_ARCHITECTURE.md
CLINICAL_NAVIGATION_ENGINE.md
MEDICAL_GOVERNANCE.md
SAFETY_FRAMEWORK.md
RAG_ARCHITECTURE.md
Downstream
GUIDELINE_POLICY.md
EVALUATION_FRAMEWORK.md
TECH_STACK.md
20. AMENDMENT TRACEABILITY
Version 1.0

Initial Release.

Locked Decisions Incorporated

LD-0051 — Knowledge Base Role
LD-0052 — Knowledge Layer Hierarchy
LD-0053 — Clinical Knowledge Domains
LD-0054 — Knowledge Source Registry
LD-0055 — Knowledge Lifecycle
LD-0056 — Guideline Independence
LD-0057 — Knowledge Versioning
LD-0058 — Domain Metadata
LD-0059 — Clinical Knowledge Object
LD-0060 — Knowledge Validation
LD-0061 — Knowledge Traceability
LD-0062 — Knowledge Relationships
LD-0063 — Knowledge Deprecation
LD-0064 — Retrieval Eligibility
LD-0065 — Knowledge Passport