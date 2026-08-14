# RESPONSE_GENERATION_ARCHITECTURE

---

# DOCUMENT METADATA

Document ID:
DOC-ARC-008

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
PROMPTING_STRATEGY.md
EVIDENCE_PACKAGE_SPECIFICATION.md
SAFETY_FRAMEWORK.md
CLINICAL_NAVIGATION_ENGINE.md

Required By:
OUTPUT_VALIDATION_FRAMEWORK.md
DELIVERY_POLICY.md
EVALUATION_FRAMEWORK.md
TECH_STACK.md

Last Updated:
2026-08-03

---

# 1. PURPOSE

This document defines the Response Generation Architecture of the Safe Medical AI System.

Response Generation transforms governed clinical evidence into patient-centered educational communication while preserving evidence fidelity, safety, explainability, and architectural separation of concerns.

---

# 2. DESIGN PHILOSOPHY

Response Generation follows the principles of:

- Evidence-guided communication
- Communication before generation
- Governance before language
- Patient-centered education
- Explainability
- Deterministic behavior
- Technology independence

---

# 3. ROLE

Response Generation is responsible for:

- transforming Evidence Packages into educational responses
- adapting communication to patient understanding
- preserving evidence fidelity
- maintaining citation traceability
- integrating governed safety advice

Response Generation is not responsible for:

- clinical reasoning
- evidence retrieval
- governance decisions
- medical knowledge creation

---

# 4. RESPONSE GENERATION PHILOSOPHY

Response Generation performs evidence-guided communication.

Clinical reasoning is completed upstream through Navigation, Governance, and Retrieval.

The language model communicates governed evidence rather than generating independent medical knowledge.

---

# 5. INPUT CONTRACT

Response Generation receives exactly two standardized inputs:

- Navigation Context
- Evidence Package

Direct access to:

- Knowledge Base
- Retrieval Layer
- Knowledge Registry

is prohibited.

---

# 6. CLINICAL REASONING BOUNDARY

Response Generation shall not create new clinical recommendations.

If sufficient evidence is unavailable, the response shall follow governance policies rather than speculate or infer unsupported recommendations.

---

# 7. COMMUNICATION DESIGN

Response Generation optimizes:

- patient education
- readability
- empathy
- health literacy
- communication clarity

The system is designed for patient education rather than clinical decision support.

---

# 8. RESPONSE COMPOSITION

Responses follow a standardized logical structure.

Illustrative components include:

- Educational Answer
- Evidence Explanation
- Important Notes
- Safety Advice
- References

Presentation details remain implementation-specific.

---

# 9. EVIDENCE FIDELITY

Generated responses shall preserve:

- recommendation intent
- supporting evidence
- clinical meaning
- evidence hierarchy

Evidence shall not be exaggerated, weakened, or reinterpreted.

---

# 10. SAFETY INTEGRATION

Safety Advice originates from the Safety Framework.

Response Generation integrates governed safety guidance without independently generating safety rules.

---

# 11. CITATION PRESERVATION

Every clinical statement shall remain traceable through:

Generated Response

↓

Evidence Package

↓

Clinical Knowledge Object

↓

Knowledge Passport

↓

Knowledge Source

Citation traceability shall remain preserved throughout the pipeline.

---

# 12. RESPONSE DETERMINISM

Equivalent:

- Navigation Context
- Evidence Package
- Prompt Specification Version

shall produce equivalent response content.

Determinism supports evaluation, auditing, and reproducibility.

---

# 13. RESPONSE BOUNDARY

Response Generation terminates after producing the Generated Response.

Subsequent validation, quality assurance, and delivery are performed by downstream architectural components.

---

# 14. ARCHITECTURAL PRINCIPLES

The Response Generation Architecture follows:

- Governance-first communication
- Evidence fidelity
- Patient-centered education
- Explainability
- Determinism
- Separation of concerns
- Technology independence

---

# 15. RELATED DOCUMENTS

## Upstream

- PROMPTING_STRATEGY.md
- EVIDENCE_PACKAGE_SPECIFICATION.md
- SAFETY_FRAMEWORK.md
- CLINICAL_NAVIGATION_ENGINE.md

## Downstream

- OUTPUT_VALIDATION_FRAMEWORK.md
- DELIVERY_POLICY.md
- EVALUATION_FRAMEWORK.md
- TECH_STACK.md

---

# 16. AMENDMENT TRACEABILITY

## Version 1.0

Initial Release.

Locked Decisions Incorporated

LD-0179 — Response Generation Philosophy

LD-0180 — Single Input Contract

LD-0181 — No Independent Clinical Reasoning

LD-0182 — Communication-first Design

LD-0183 — Layered Response Composition

LD-0184 — Evidence Fidelity

LD-0185 — Safety Integration

LD-0186 — Citation Preservation

LD-0187 — Response Determinism

LD-0188 — Response Boundary