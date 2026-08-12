# KNOWLEDGE_OBJECT_SPECIFICATION

---

# DOCUMENT METADATA

Document ID:
DOC-KNW-002

Version:
1.0

Status:
LOCKED

Authority:
KNOWLEDGE

Owner:
Project Coordinator

Strategist:
ChatGPT

Implementation:
Claude

Depends On:
SYSTEM_ARCHITECTURE.md
KNOWLEDGE_BASE.md
KNOWLEDGE_INGESTION_WORKFLOW.md

Required By:
KNOWLEDGE_PASSPORT.md
RAG_IMPLEMENTATION.md
EVALUATION_FRAMEWORK.md
TECH_STACK.md

Last Updated:
2026-08-03

---

# 1. PURPOSE

This document defines the specification of the Clinical Knowledge Object (CKO), the fundamental semantic knowledge unit within the Safe Medical AI System.

The specification standardizes how clinical knowledge is represented, governed, versioned, and retrieved independently of implementation technology.

---

# 2. DESIGN PHILOSOPHY

Clinical Knowledge Objects follow the principles:

- Atomic knowledge representation
- One recommendation per object
- Governance before retrieval
- Semantic consistency
- Evidence transparency
- Traceability by design

---

# 3. ROLE

Clinical Knowledge Objects serve as the primary governed knowledge unit of the Knowledge Base.

They replace document chunks as the fundamental retrieval entity.

---

# 4. KNOWLEDGE OBJECT GRANULARITY

One Clinical Knowledge Object shall represent one atomic clinical recommendation.

Examples include:

- HER2 testing recommendation
- MSI testing recommendation
- PD-L1 testing recommendation
- Follow-up recommendation
- Surgery recommendation

Entire guideline sections shall not become a single Knowledge Object.

---

# 5. KNOWLEDGE OBJECT STRUCTURE

Each Knowledge Object contains standardized logical components.

Mandatory sections include:

- Knowledge Object Identifier
- Clinical Domain
- Knowledge Type
- Clinical Recommendation
- Recommendation Strength
- Supporting Evidence
- Evidence Level
- Clinical Applicability
- Exceptions
- Source Guideline
- Guideline Version
- References
- Related Knowledge Objects

---

# 6. KNOWLEDGE SOURCE RELATIONSHIP

One guideline may generate multiple Knowledge Objects.

Each Knowledge Object belongs to exactly one guideline version.

Knowledge originating from different guideline versions shall remain independent.

---

# 7. RECOMMENDATION FIDELITY

Clinical recommendations shall preserve the original meaning of the source guideline.

Interpretation for patient communication occurs during downstream response generation rather than within the Knowledge Base.

---

# 8. CLINICAL APPLICABILITY

Each Knowledge Object shall define standardized applicability metadata.

Illustrative metadata include:

- Cancer Type
- Disease Stage
- Treatment Phase
- Biomarker
- Patient Population
- Contraindications

---

# 9. KNOWLEDGE RELATIONSHIPS

Knowledge Objects maintain explicit logical relationships.

Illustrative relationship types include:

- prerequisite
- related recommendation
- complementary recommendation
- follow-up step
- contraindication

Relationships are maintained independently from recommendation text.

---

# 10. IMMUTABILITY

Published Knowledge Objects are immutable.

When recommendations change:

Current Object

↓

Deprecated

↓

New Version Created

Historical objects remain available for auditing.

---

# 11. KNOWLEDGE TYPE

Each Knowledge Object represents exactly one knowledge type.

Illustrative types include:

- Recommendation
- Definition
- Diagnostic Criterion
- Treatment Principle
- Follow-up Schedule
- Warning
- Contraindication

---

# 12. SELF-CONTAINED DESIGN

Each Knowledge Object shall be understandable independently.

Related Knowledge Objects extend context but shall not contain mandatory information required to interpret the current object.

---

# 13. EVIDENCE MODEL

Recommendation content shall remain structurally separated from supporting evidence.

Minimum evidence components include:

- Clinical Recommendation
- Supporting Evidence
- Evidence Level
- Recommendation Strength

---

# 14. HUMAN & MACHINE READABILITY

Knowledge Objects are designed for:

- Clinical review
- AI retrieval
- Rule engines
- APIs
- Evaluation pipelines

No implementation technology is assumed.

---

# 15. KNOWLEDGE OBJECT IDENTIFIER

Every Knowledge Object shall possess a permanent identifier.

Illustrative format:

CKO-GC-DIAG-0001

Version identifiers remain independent of Knowledge Object identifiers.

---

# 16. RETRIEVAL UNIT

Clinical Knowledge Objects constitute the smallest semantic retrieval unit.

Multiple Knowledge Objects may be assembled into a downstream Evidence Package according to the Navigation Context.

---

# 17. ARCHITECTURAL PRINCIPLES

The specification follows:

- Atomicity
- Explainability
- Traceability
- Immutability
- Semantic consistency
- Governance-first design
- Technology independence

---

# 18. RELATED DOCUMENTS

Upstream

- KNOWLEDGE_BASE.md
- KNOWLEDGE_INGESTION_WORKFLOW.md

Downstream

- KNOWLEDGE_PASSPORT.md
- RAG_IMPLEMENTATION.md
- EVALUATION_FRAMEWORK.md
- TECH_STACK.md

---

# 19. AMENDMENT TRACEABILITY

Version 1.0

Initial Release.

Locked Decisions Incorporated

LD-0095 — Knowledge Object Granularity

LD-0096 — Knowledge Object Structure

LD-0097 — One Source, Many Objects

LD-0098 — Recommendation Fidelity

LD-0099 — Clinical Applicability Metadata

LD-0100 — Knowledge Relationship Graph

LD-0101 — Immutable Clinical Content

LD-0102 — Knowledge Object Scope

LD-0103 — Knowledge Object Independence

LD-0104 — Evidence Separation

LD-0105 — Human-readable & Machine-readable Design

LD-0106 — Stable Knowledge Object Identifier

LD-0107 — Retrieval Atomicity