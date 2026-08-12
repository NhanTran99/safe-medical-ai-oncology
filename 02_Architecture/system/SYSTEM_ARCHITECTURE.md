SYSTEM_ARCHITECTURE.md v1.0 (LOCK)
DOCUMENT METADATA

Document ID

DOC-ARC-001

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
PROJECT_ROADMAP.md
NOVELTY.md

Required By

CLINICAL_NAVIGATION_ENGINE.md
MEDICAL_GOVERNANCE.md
SAFETY_FRAMEWORK.md
RAG_ARCHITECTURE.md
KNOWLEDGE_BASE.md
TECH_STACK.md

Last Updated

2026-08-01

1. PURPOSE

This document defines the overall logical architecture of the Safe Medical AI System for Oncology Patient Education.

It establishes the major architectural components, their responsibilities, interactions, and execution flow.

Implementation details are intentionally delegated to downstream architecture documents.

2. ARCHITECTURAL PHILOSOPHY

The system adopts a Layered + Pipeline Hybrid Architecture.

The layered view separates responsibilities into modular components.

The pipeline view represents the execution sequence of a user conversation.

This architecture prioritizes:

Patient Safety
Explainability
Maintainability
Research Reproducibility
Separation of Concerns
3. SYSTEM EXECUTION FLOW
User

↓

Presentation Layer

↓

Conversation Orchestrator

↓

Conversation Understanding Layer

↓

Clinical Safety Layer

↓

Clinical Navigation Engine

↓

Knowledge Retrieval Layer

↓

Evidence Processing Layer

↓

LLM Response Generation

↓

Response Validation

↓

Presentation Layer

↓

User

The pipeline describes the logical execution order.

Internal implementation may optimize or parallelize certain operations without changing the logical architecture.

4. MAJOR ARCHITECTURAL COMPONENTS
4.1 Presentation Layer

Responsibilities

User interface
Session management
Conversation history
Response presentation
User feedback collection
4.2 Conversation Orchestrator

Responsibilities

Coordinate end-to-end workflow
Invoke architectural components
Manage execution sequence
Aggregate intermediate outputs
Handle orchestration logic
4.3 Conversation Understanding Layer

Responsibilities

Intent detection
Clinical entity extraction
Context normalization
Ambiguity detection
Language identification
Structured conversation context generation

Purpose

Provide a standardized representation of the user's request before any clinical processing occurs.

4.4 Clinical Safety Layer

Responsibilities

Scope validation
Unsafe request detection
Safety policy enforcement
Emergency scenario identification
Conversation boundary enforcement

Purpose

Ensure that only safe, in-scope educational requests proceed further into the system.

4.5 Clinical Navigation Engine

Responsibilities

Determine educational pathway
Classify clinical scenario
Select navigation strategy
Route downstream knowledge retrieval

Purpose

Guide the system through structured oncology education pathways before information retrieval.

4.6 Knowledge Retrieval Layer

Responsibilities

Retrieve guideline-based knowledge
Execute Retrieval-Augmented Generation workflow
Identify relevant evidence sources
Retrieve supporting references

Purpose

Provide evidence-grounded information for downstream response generation.

4.7 Evidence Processing Layer

Responsibilities

Rank retrieved evidence
Prepare citations
Support evidence transparency
Prepare future Evidence Strength Dashboard integration

Purpose

Transform retrieved medical evidence into a structured format suitable for explainable AI.

4.8 LLM Response Generation

Responsibilities

Generate patient-friendly educational responses
Integrate retrieved evidence
Produce structured explanations
Maintain readability

Purpose

Transform validated evidence into understandable educational content.

4.9 Response Validation

Responsibilities

Final safety verification
Citation completeness check
Response consistency validation
Output formatting
Delivery approval

Purpose

Perform the final quality assurance step before presenting information to users.

5. ARCHITECTURAL PRINCIPLES

The architecture follows six execution principles.

Safety Before Intelligence

Safety validation precedes knowledge generation.

Navigation Before Retrieval

Clinical context is established before searching for evidence.

Retrieval Before Generation

Evidence is retrieved before the LLM generates responses.

Evidence Before Explanation

Educational explanations should be grounded in retrieved evidence whenever possible.

Validation Before Delivery

Every response undergoes a final validation stage.

Separation of Concerns

Each architectural component has a clearly defined responsibility and minimizes coupling with other components.

6. COMPONENT INTERACTION

Each component communicates only with adjacent logical layers through the Conversation Orchestrator.

Business logic should remain encapsulated within the responsible downstream component.

Cross-layer dependencies should be minimized.

7. DOWNSTREAM ARCHITECTURE DOCUMENTS

This document intentionally omits implementation details.

Detailed specifications are delegated to specialized Stable Documents.

Stable Document	Primary Responsibility
CLINICAL_NAVIGATION_ENGINE.md	Navigation logic and educational pathways
MEDICAL_GOVERNANCE.md	Clinical governance policies
SAFETY_FRAMEWORK.md	Safety rules and risk mitigation
RAG_ARCHITECTURE.md	Retrieval workflow and document selection
KNOWLEDGE_BASE.md	Knowledge organization and guideline hierarchy
TECH_STACK.md	Technical implementation
8. DEFERRED ARCHITECTURAL DECISIONS

The following concepts have been intentionally deferred.

Evidence Strength Dashboard implementation
Conversation Constraint Engine rule engine
Guideline hierarchy
Knowledge Base implementation
Evaluation framework
Technical stack
Database schema
API specification

These decisions will be addressed within their dedicated downstream documents.

9. CONSISTENCY WITH FOUNDATION

This architecture remains consistent with the project's foundational principles.

Specifically:

Patient Safety First
Structured Clinical Navigation
Explainable AI
Evidence-based Medicine
Human-centered Design
Research-grade Documentation
10. AMENDMENT TRACEABILITY
Version 1.0

Initial Release.

Locked Decisions Incorporated

LD-0010 — Layered + Pipeline Hybrid Architecture
LD-0011 — Architecture Abstraction Policy
LD-0012 — Conversation Understanding Layer

No previous architecture version exists.