DOCUMENT METADATA

Document ID

DOC-ARC-005

Version

1.1

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

Required By

KNOWLEDGE_BASE.md
EVALUATION_FRAMEWORK.md
TECH_STACK.md

Last Updated

2026-08-12

1. PURPOSE

This document defines the Retrieval-Augmented Generation (RAG) Architecture responsible for retrieving, organizing, synthesizing, and delivering evidence to downstream language models.

The RAG subsystem serves as the knowledge intelligence component of the Safe Medical AI System and operates strictly within the governance and safety constraints established by upstream architecture.

2. DESIGN PHILOSOPHY

The RAG Architecture follows six principles:

Retrieval before generation
Evidence before explanation
Governance before retrieval
Transparency over completeness
Preserve evidence provenance
Modular retrieval pipeline
3. ROLE WITHIN THE SYSTEM

The RAG subsystem is responsible for:

retrieving evidence;
ranking evidence;
assembling evidence;
preserving citations.

The RAG subsystem does not:

determine clinical workflows;
authorize responses;
perform safety assessment.
4. HIGH-LEVEL WORKFLOW
Navigation Context
        │
        ▼
Knowledge Domain Selection
        │
        ▼
Hierarchical Retrieval
        │
        ▼
Retrieval Context
        │
        ▼
Evidence Assembly
        │
        ▼
Evidence Package
        │
        ▼
LLM Response Generation
5. HIERARCHICAL RETRIEVAL

Retrieval follows a hierarchical process:

Navigation Context
Knowledge Domain
Evidence Source
Document
Chunk
Citation

This hierarchy minimizes irrelevant retrieval and improves explainability.

6. KNOWLEDGE HIERARCHY

Evidence sources follow the approved priority hierarchy.

Illustrative hierarchy:

Clinical Guidelines
Consensus Statements
High-quality Systematic Reviews
Major Clinical Trials
Educational Resources

Detailed source policies are delegated to the Knowledge Base.

7. RETRIEVAL CONTEXT

The RAG subsystem generates a Retrieval Context describing the evidence selected for downstream synthesis.

Illustrative information includes:

Knowledge Domain
Retrieved Documents
Evidence Level
Citation List
Evidence Summary
Retrieval Confidence
8. MULTI-SOURCE EVIDENCE FUSION

Multiple evidence sources remain distinguishable.

When sources disagree, the disagreement shall be preserved and communicated rather than automatically reconciled.

9. CHUNK-LEVEL CITATION

Evidence citations shall remain associated with individual retrieved chunks whenever technically feasible.

This supports transparency, auditing, and explainability.

10. RETRIEVAL BEFORE GENERATION

Language model generation depends on successful retrieval unless upstream governance explicitly permits a restricted educational fallback.

11. RETRIEVAL LOGGING

Every retrieval process generates a structured Retrieval Record.

Illustrative fields include:

Knowledge Domain
Retrieved Sources
Evidence Rank
Retrieval Confidence
Selected Chunks
Selection Rationale

These records support auditing, evaluation, and research reproducibility.

12. RUNTIME EVIDENCE PACKAGE

The Runtime Evidence Package is the standardized output of the RAG subsystem.

It is an internal runtime artifact assembled from governed Clinical Knowledge
Objects selected through the approved retrieval process.

The Runtime Evidence Package may contain:

- Evidence Summary
- Evidence Hierarchy
- Supporting Citations
- Contradictory Evidence
- Evidence Confidence
- Retrieval Confidence
- Evidence Gap

The Runtime Evidence Package is distinct from the Primary Evidence Package
(Artifact 03) contained within a Gold Population Package.

The Primary Evidence Package is a governed static knowledge artifact.

The Runtime Evidence Package is a dynamic retrieval output.

The two shall not be conflated.

13. EVIDENCE CONFLICT

Conflicting recommendations shall be explicitly represented.

The system shall explain that multiple authoritative recommendations exist without automatically selecting a preferred guideline.

14. EVIDENCE FRESHNESS

Evidence metadata shall preserve:

Guideline Version
Publication Year
Evidence Currency

Freshness information supports transparency and future evaluation.

15. LOGICAL EVIDENCE GRAPH

The architecture adopts a logical Evidence Graph linking:

User Question
        │
        ▼
Knowledge Domain
        │
        ▼
Guideline
        │
        ▼
Recommendation
        │
        ▼
Supporting Evidence
        │
        ▼
Citation

This graph represents logical relationships and does not prescribe implementation technology.

16. RELATED DOCUMENTS
Upstream
SYSTEM_ARCHITECTURE.md
CLINICAL_NAVIGATION_ENGINE.md
MEDICAL_GOVERNANCE.md
SAFETY_FRAMEWORK.md
Downstream
KNOWLEDGE_BASE.md
EVALUATION_FRAMEWORK.md
TECH_STACK.md
17. AMENDMENT TRACEABILITY
Version 1.0

Initial Release.

Locked Decisions Incorporated

LD-0038 — RAG Responsibility
LD-0039 — Hierarchical Retrieval
LD-0040 — Knowledge Hierarchy
LD-0041 — Retrieval Context
LD-0042 — Multi-source Evidence Fusion
LD-0043 — Chunk-level Citation Policy
LD-0044 — Retrieval Before Generation
LD-0045 — Retrieval Logging
LD-0046 — Evidence Package
LD-0047 — Evidence Conflict Policy
LD-0048 — Evidence Freshness Policy
LD-0049 — Confidence Separation
LD-0050 — Logical Evidence Graph