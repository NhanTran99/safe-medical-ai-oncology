# EVIDENCE_PACKAGE_SPECIFICATION

---

# DOCUMENT METADATA

Document ID:
DOC-RAG-002

Version:
1.0

Status:
LOCKED

Authority:
ARCHITECTURE

Owner:
Project Coordinator

Strategist:
ChatGPT

Implementation:
Claude

Depends On:
RETRIEVAL_POLICY.md
KNOWLEDGE_OBJECT_SPECIFICATION.md
PROMPTING_STRATEGY.md

Required By:
OUTPUT_CONTRACT.md
EVALUATION_FRAMEWORK.md
TECH_STACK.md

Last Updated:
2026-08-03

---

# 1. PURPOSE

This document defines the standardized Evidence Package used by the Safe Medical AI System.

The Evidence Package serves as the governed interface between the Retrieval Layer and the Prompting Strategy, ensuring deterministic, explainable, and traceable evidence transfer.

---

# 2. DESIGN PHILOSOPHY

The Evidence Package follows the principles of:

- Governance before communication
- Separation of evidence and prompting
- Immutable evidence transfer
- Complete provenance
- Deterministic construction
- Technology independence

---

# 3. ROLE

The Evidence Package is responsible for transferring governed clinical evidence from the Retrieval Layer to the Prompt Builder.

Responsibilities include:

- evidence transport
- provenance preservation
- retrieval traceability
- structural consistency
- governance integrity

The Evidence Package does not contain prompt instructions or generated responses.

---

# 4. EVIDENCE PACKAGE PHILOSOPHY

The Evidence Package is the standardized retrieval output.

It represents evidence selected through governed retrieval rather than semantic search results or language model prompts.

---

# 5. EVIDENCE PACKAGE COMPOSITION

Every Evidence Package consists of two logical components:

## Evidence Content

The governed clinical evidence.

## Evidence Metadata

Governance metadata supporting traceability, reproducibility, and auditing.

Clinical evidence and governance metadata shall remain logically separated.

---

# 6. EVIDENCE CONTENT

Evidence Content contains only retrieved Clinical Knowledge Objects.

Evidence Content shall not include:

- Prompt instructions
- Prompt templates
- Language model directives
- Generated responses

---

# 7. EVIDENCE METADATA

Every Evidence Package shall maintain standardized metadata.

Minimum metadata include:

- Evidence Package Identifier
- Retrieval Identifier
- Navigation Context Identifier
- Retrieval Policy Version
- Knowledge Base Version
- Generation Timestamp

Additional metadata may be introduced through governed amendments.

---

# 8. SOURCE PROVENANCE

Every retrieved Clinical Knowledge Object shall maintain complete provenance.

Minimum provenance includes:

- Knowledge Object Identifier
- Knowledge Passport Identifier
- Source Identifier
- Guideline Version

Complete provenance supports explainability and governance auditing.

---

# 9. EVIDENCE ORDERING

Evidence ordering shall be preserved exactly as produced by the Retrieval Layer.

Downstream components shall not reorder evidence.

---

# 10. EVIDENCE INTEGRITY

Prompt Builder may format Evidence Packages for downstream consumption.

Prompt Builder shall not modify:

- clinical recommendations
- supporting evidence
- provenance
- governance metadata

Evidence integrity shall remain preserved throughout the pipeline.

---

# 11. PACKAGE IMMUTABILITY

Evidence Packages are immutable after retrieval completion.

Modified retrieval results shall generate a new Evidence Package rather than modifying an existing one.

---

# 12. OUTPUT CONTRACT

Every Evidence Package shall satisfy a standardized Output Contract before downstream processing.

Minimum validation includes:

- governance completeness
- provenance completeness
- retrieval completeness
- structural validity

Evidence Packages failing validation shall not proceed to Prompt Builder.

---

# 13. PROMPT INTERFACE

Prompt Builder shall receive exactly one standardized input:

Evidence Package

Prompt Builder shall not directly access:

- Knowledge Base
- Knowledge Source Registry
- Clinical Knowledge Objects

This preserves architectural separation of concerns.

---

# 14. ARCHITECTURAL PRINCIPLES

The Evidence Package follows:

- Governance-first design
- Deterministic transfer
- Immutable evidence
- Explainability
- Traceability
- Separation of concerns
- Technology independence

---

# 15. RELATED DOCUMENTS

## Upstream

- RETRIEVAL_POLICY.md
- KNOWLEDGE_OBJECT_SPECIFICATION.md

## Downstream

- PROMPTING_STRATEGY.md
- OUTPUT_CONTRACT.md
- EVALUATION_FRAMEWORK.md
- TECH_STACK.md

---

# 16. AMENDMENT TRACEABILITY

## Version 1.0

Initial Release.

Locked Decisions Incorporated

LD-0169 — Evidence Package Philosophy

LD-0170 — Evidence Package Composition

LD-0171 — Evidence Content Unit

LD-0172 — Evidence Metadata

LD-0173 — Source Provenance

LD-0174 — Evidence Ordering

LD-0175 — Evidence Integrity

LD-0176 — Package Immutability

LD-0177 — Evidence Package Output Contract

LD-0178 — Prompt Interface