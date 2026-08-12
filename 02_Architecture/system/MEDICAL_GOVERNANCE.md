DOCUMENT METADATA

Document ID

DOC-ARC-003

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

PROJECT_FOUNDATION.md
MISSION_AND_SCOPE.md
SYSTEM_ARCHITECTURE.md
CLINICAL_NAVIGATION_ENGINE.md
NOVELTY.md

Required By

SAFETY_FRAMEWORK.md
RAG_ARCHITECTURE.md
KNOWLEDGE_BASE.md
EVALUATION_FRAMEWORK.md

Last Updated

2026-08-02

1. PURPOSE

This document defines the Medical Governance Framework of the Safe Medical AI System for Oncology Patient Education.

Medical Governance establishes the clinical policies that determine whether, how, and to what extent the system may generate educational responses. It serves as the highest clinical authority within the architecture and governs downstream medical components without prescribing implementation details.

2. GOVERNANCE PHILOSOPHY

Medical Governance is founded on the principle that clinical safety must precede knowledge generation.

The framework functions as a policy layer that authorizes, restricts, or denies system behaviors before any medical content is retrieved or generated.

3. GOVERNANCE SCOPE

Medical Governance governs:

Clinical behavior
Medical safety
Evidence governance
Educational boundaries
Response authorization
Human escalation

Medical Governance does not govern:

User interface
Technical implementation
Repository structure
Database architecture
API design
Technology stack
4. GOVERNANCE HIERARCHY

The governance hierarchy is defined as:

Mission & Scope
        │
        ▼
Medical Governance
        │
        ▼
Safety Framework
        │
        ▼
Clinical Navigation Engine
        │
        ▼
Knowledge Base
        │
        ▼
RAG Architecture
        │
        ▼
LLM Response Generation

All downstream medical components shall remain consistent with Medical Governance.

5. CORE GOVERNANCE PRINCIPLES

The framework adopts the following principles:

Patient Safety First
Evidence Before Opinion
Education Before Recommendation
Human Oversight Required
Transparency and Explainability
Scope Boundary Enforcement

These principles shall guide every downstream governance policy.

6. MEDICAL DECISION AUTHORITY

Medical Governance determines:

whether a request may be answered;
the permitted educational scope;
the required safety level;
warning requirements;
escalation requirements;
response authorization.

Medical Governance does not determine the medical content itself.

7. MEDICAL RISK CLASSIFICATION

Four medical risk levels are defined:

Level	Description
Level 1	Safe educational information
Level 2	Educational content requiring caution
Level 3	High-risk medical requests requiring significant restrictions
Level 4	Emergency situations requiring immediate escalation

Detailed operational rules are delegated to the Safety Framework.

8. MEDICAL PERMISSION MODEL

Medical Governance regulates AI capabilities through a permission model.

Permission	Status
Explain	Allowed
Educate	Allowed
Summarize	Allowed
Compare evidence	Allowed
Recommend personalized treatment	Restricted
Diagnose	Prohibited
Prescribe medication	Prohibited
Predict individual outcomes	Prohibited

Additional permissions may be introduced without changing the overall architecture.

9. EVIDENCE GOVERNANCE

Medical Governance defines:

approved evidence sources;
evidence prioritization;
minimum evidence requirements;
citation expectations;
conditions under which educational responses remain permissible.

Evidence retrieval mechanisms are delegated to the RAG Architecture.

10. HUMAN ESCALATION POLICY

The system shall escalate users to healthcare professionals whenever governance policies determine that safe educational support is no longer sufficient.

Illustrative scenarios include:

emergency symptoms;
requests for individualized treatment decisions;
medication changes;
interpretation of personal medical findings beyond the project's educational scope.

Detailed escalation criteria are defined within the Safety Framework.

11. CLINICAL PERMISSION PIPELINE

Every user request follows the same governance pipeline:

User Request
        │
        ▼
Scope Check
        │
        ▼
Risk Classification
        │
        ▼
Permission Check
        │
        ▼
Evidence Availability Check
        │
        ▼
Escalation Decision
        │
        ▼
Response Authorization
        │
        ▼
Knowledge Retrieval

No medical knowledge retrieval shall occur before successful response authorization.

12. DEFAULT DENY PRINCIPLE

Medical Governance adopts a Default Deny policy.

Requests remain unauthorized unless explicitly permitted.

When uncertainty exists regarding:

scope;
permissions;
evidence sufficiency; or
safety,

the system shall request clarification, provide only safe educational information, or decline to answer according to governance policies.

13. GOVERNANCE AS A POLICY ENGINE

Medical Governance functions as a centralized Policy Engine.

It defines:

governance policies;
permissions;
decision rules;
evidence rules;
escalation rules.

Execution logic remains the responsibility of downstream architectural components.

14. RELATED DOCUMENTS
Upstream
SYSTEM_ARCHITECTURE.md
CLINICAL_NAVIGATION_ENGINE.md
PROJECT_FOUNDATION.md
MISSION_AND_SCOPE.md
Downstream
SAFETY_FRAMEWORK.md
RAG_ARCHITECTURE.md
KNOWLEDGE_BASE.md
EVALUATION_FRAMEWORK.md
15. AMENDMENT TRACEABILITY
Version 1.0

Initial Release.

Locked Decisions Incorporated

LD-0019 — Medical Governance Scope
LD-0020 — Governance Hierarchy
LD-0021 — Core Medical Governance Principles
LD-0022 — Medical Decision Authority
LD-0023 — Medical Risk Classification
LD-0024 — Evidence Governance
LD-0025 — Human Escalation Policy
LD-0026 — Medical Permission Model
LD-0027 — Clinical Permission Pipeline
LD-0028 — Default Deny Principle
LD-0029 — Governance as Policy Engine