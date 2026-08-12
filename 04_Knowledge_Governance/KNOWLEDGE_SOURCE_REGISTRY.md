# KNOWLEDGE_SOURCE_REGISTRY

---

# DOCUMENT METADATA

Document ID:
DOC-KNW-004

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
KNOWLEDGE_BASE.md
KNOWLEDGE_INGESTION_WORKFLOW.md

Required By:
KNOWLEDGE_SOURCE_APPROVAL_POLICY.md
EVALUATION_FRAMEWORK.md
TECH_STACK.md

Last Updated:
2026-08-03

---

# 1. PURPOSE

This document defines the Knowledge Source Registry (KSR), the authoritative inventory of all Knowledge Sources used within the Safe Medical AI System.

The registry governs the identity, metadata, authority, lifecycle, and approval status of knowledge sources before they enter the Knowledge Ingestion Workflow.

---

# 2. DESIGN PHILOSOPHY

The Knowledge Source Registry follows the principles of:

- Governance before ingestion
- One source, one record
- Permanent source identity
- Standardized metadata
- Traceability by design
- Technology independence

---

# 3. ROLE

The Knowledge Source Registry serves as the governance layer for knowledge sources.

Its responsibilities include:

- registering candidate knowledge sources
- maintaining authoritative metadata
- managing source lifecycle
- tracking approval status
- supporting governance auditing

The registry does not store Clinical Knowledge Objects or clinical recommendations.

---

# 4. ONE SOURCE, ONE RECORD

Each Knowledge Source shall have exactly one Registry Record.

Illustrative examples:

- NCCN Gastric Cancer Guidelines Version 2026
- ESMO Gastric Cancer Clinical Practice Guideline 2024
- ASCO Biomarker Guideline

Duplicate registry records are prohibited.

---

# 5. SOURCE IDENTIFIER

Every Knowledge Source shall maintain a permanent Source Identifier.

Illustrative format:

KS-GC-000001

The Source Identifier remains stable throughout the lifecycle of the source.

Version management is performed independently.

---

# 6. MANDATORY METADATA

Every Registry Record shall contain standardized metadata.

Minimum metadata include:

- Source Identifier
- Source Name
- Organization
- Cancer Type
- Document Type
- Source Classification
- Jurisdiction
- Publication Year
- Guideline Version
- Language
- License
- Approval Status
- Lifecycle Status

Additional metadata may be introduced through governed amendments.

---

# 7. SOURCE CLASSIFICATION

Each Knowledge Source shall be assigned one standardized classification.

Illustrative classifications include:

- Clinical Guideline
- Consensus Statement
- Position Paper
- Systematic Review
- Clinical Trial
- Regulatory Guidance
- Educational Resource

Classification supports downstream governance and retrieval policies.

---

# 8. AUTHORITATIVE ORGANIZATION

Every Registry Record shall record the authoritative organization independently from the source title.

Illustrative organizations include:

- NCCN
- ESMO
- ASCO
- NICE
- CSCO
- WHO

Authority metadata supports evidence governance and source prioritization.

---

# 9. SOURCE LIFECYCLE

Knowledge Sources follow a governed lifecycle.

Candidate

↓

Registered

↓

Clinically Reviewed

↓

Approved

↓

Active

↓

Deprecated

↓

Archived

The lifecycle of a Knowledge Source is independent from the lifecycle of Clinical Knowledge Objects derived from that source.

---

# 10. APPROVAL STATUS

Approval status shall be maintained independently from lifecycle status.

Illustrative approval states include:

- Pending Review
- Under Clinical Review
- Approved
- Rejected

Only approved sources are eligible for knowledge extraction.

---

# 11. TRACEABILITY

Every Registry Record shall maintain traceability to:

- Source Identifier
- Organization
- Guideline Version
- Publication Information
- Lifecycle Events
- Approval History

This ensures complete governance transparency.

---

# 12. ARCHITECTURAL PRINCIPLES

The Knowledge Source Registry follows:

- Governance-first design
- One source, one identity
- Permanent identifiers
- Standardized metadata
- Traceability
- Auditability
- Technology independence

---

# 13. RELATED DOCUMENTS

## Upstream

- KNOWLEDGE_BASE.md
- KNOWLEDGE_INGESTION_WORKFLOW.md

## Downstream

- KNOWLEDGE_SOURCE_APPROVAL_POLICY.md
- EVALUATION_FRAMEWORK.md
- TECH_STACK.md

---

# 14. AMENDMENT TRACEABILITY

## Version 1.0

Initial Release.

Locked Decisions Incorporated

LD-0115 — Registry Purpose

LD-0116 — One Source, One Registry Record

LD-0117 — Permanent Source Identifier

LD-0118 — Mandatory Registry Metadata

LD-0119 — Source Classification

LD-0120 — Source Authority

LD-0121 — Source Lifecycle