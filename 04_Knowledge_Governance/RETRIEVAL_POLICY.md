# RETRIEVAL_POLICY

---

# DOCUMENT METADATA

Document ID:
DOC-RAG-001

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
RAG_ARCHITECTURE.md
KNOWLEDGE_BASE.md
CLINICAL_NAVIGATION_ENGINE.md
KNOWLEDGE_RELATIONSHIP_MODEL.md

Required By:
PROMPTING_STRATEGY.md
EVALUATION_FRAMEWORK.md
TECH_STACK.md

Last Updated:
2026-08-03

---

# 1. PURPOSE

This document defines the Retrieval Policy governing evidence retrieval within the Safe Medical AI System.

The Retrieval Policy standardizes how governed knowledge is selected, filtered, expanded, ranked, and packaged before response generation while remaining independent of implementation technology.

---

# 2. DESIGN PHILOSOPHY

The Retrieval Policy follows the principles of:

- Navigation before retrieval
- Governance before relevance
- Clinical context before semantic similarity
- Minimum sufficient evidence
- Explainable retrieval
- Deterministic execution
- Technology independence

---

# 3. ROLE

The Retrieval Layer is responsible for:

- selecting eligible knowledge
- applying governance filters
- retrieving Clinical Knowledge Objects
- relationship expansion
- evidence ranking
- Evidence Package construction

The Retrieval Layer does not generate natural language responses.

---

# 4. RETRIEVAL PHILOSOPHY

Retrieval performs governed evidence retrieval rather than generic semantic search.

The objective is to retrieve the most appropriate evidence rather than the largest quantity of information.

---

# 5. NAVIGATION-FIRST RETRIEVAL

Every retrieval begins with a Navigation Context.

Standard flow:

Patient Question

↓

Navigation Context

↓

Clinical Knowledge Domain

↓

Knowledge Retrieval

Searching the entire Knowledge Base without Navigation Context is prohibited.

---

# 6. GOVERNANCE FILTER

Only knowledge satisfying all governance requirements shall be eligible.

Minimum requirements include:

- Approved
- Published
- Active

Knowledge failing governance validation shall be excluded before retrieval.

---

# 7. DOMAIN-FIRST RETRIEVAL

Retrieval operates only within Clinical Knowledge Domains selected by the Navigation Engine.

Cross-domain retrieval is performed only through governed relationship expansion.

---

# 8. RELATIONSHIP EXPANSION

Relationship expansion occurs after retrieval of Primary Clinical Knowledge Objects.

Standard flow:

Primary Knowledge Objects

↓

Knowledge Relationship Model

↓

Supporting Knowledge Objects

↓

Evidence Package

Relationship expansion shall remain governed and explainable.

---

# 9. EVIDENCE RANKING

Evidence shall be ranked according to the following priority:

1. Governance Eligibility
2. Clinical Relevance
3. Navigation Match
4. Authority Tier
5. Evidence Level
6. Recency

Embedding similarity shall not be the primary ranking criterion.

---

# 10. MINIMUM SUFFICIENT RETRIEVAL

The Retrieval Layer shall retrieve only the minimum evidence necessary to answer the current clinical question.

Retrieving complete guidelines by default is prohibited.

---

# 11. RETRIEVAL TRACEABILITY

Every retrieval generates a Retrieval Record.

Minimum metadata include:

- Retrieval Identifier
- Navigation Context Identifier
- Retrieved Knowledge Object Identifiers
- Source Identifiers
- Retrieval Timestamp

Additional metadata may be introduced through governed amendments.

---

# 12. RETRIEVAL DETERMINISM

Retrieval shall be deterministic.

Identical:

- Navigation Context
- Knowledge Base Version
- Retrieval Policy Version

shall produce identical Retrieval Results.

---

# 13. RETRIEVAL OUTPUT CONTRACT

The Retrieval Layer outputs:

- Evidence Package
- Retrieval Metadata

Natural language generation belongs exclusively to the Prompting Strategy and downstream language model.

---

# 14. ARCHITECTURAL PRINCIPLES

The Retrieval Policy follows:

- Governance-first retrieval
- Navigation-driven retrieval
- Domain-centered retrieval
- Explainability
- Determinism
- Traceability
- Technology independence

---

# 15. RELATED DOCUMENTS

## Upstream

- CLINICAL_NAVIGATION_ENGINE.md
- RAG_ARCHITECTURE.md
- KNOWLEDGE_BASE.md
- KNOWLEDGE_RELATIONSHIP_MODEL.md

## Downstream

- PROMPTING_STRATEGY.md
- EVALUATION_FRAMEWORK.md
- TECH_STACK.md

---

# 16. AMENDMENT TRACEABILITY

## Version 1.0

Initial Release.

Locked Decisions Incorporated

LD-0159 — Retrieval Philosophy

LD-0160 — Navigation-first Retrieval

LD-0161 — Governance Filter First

LD-0162 — Domain-first Retrieval

LD-0163 — Relationship Expansion

LD-0164 — Evidence Ranking

LD-0165 — Minimum Sufficient Retrieval

LD-0166 — Retrieval Traceability

LD-0167 — Retrieval Determinism

LD-0168 — Retrieval Output Contract