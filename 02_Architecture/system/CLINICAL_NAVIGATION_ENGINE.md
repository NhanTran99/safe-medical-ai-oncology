DOCUMENT METADATA

Document ID

DOC-ARC-002

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
NOVELTY.md

Required By

MEDICAL_GOVERNANCE.md
SAFETY_FRAMEWORK.md
RAG_ARCHITECTURE.md
KNOWLEDGE_BASE.md

Last Updated

2026-08-02

1. PURPOSE

This document defines the architecture and operational workflow of the Clinical Navigation Engine.

The Clinical Navigation Engine is the primary orchestration component responsible for determining the educational pathway before any medical knowledge retrieval or response generation occurs.

It is a core architectural novelty of the project.

2. DESIGN PHILOSOPHY

The Clinical Navigation Engine follows five principles:

Navigation before Retrieval
Rule-based before AI Reasoning
Patient Journey before Topic Classification
Structured Context before Free-text Processing
Education before Recommendation
3. ROLE WITHIN THE SYSTEM

The Clinical Navigation Engine does not generate medical responses.

Instead, it:

identifies the patient's educational context;
determines the current clinical state;
selects the appropriate educational workflow;
prepares a structured Navigation Context for downstream components.
4. HIGH-LEVEL WORKFLOW
User Request
        │
        ▼
Conversation Understanding
        │
        ▼
Clinical Navigation Engine
        │
        ▼
Clinical State Machine
        │
        ▼
Navigation Context
        │
        ▼
Knowledge Retrieval Layer
        │
        ▼
LLM Response Generation

The Navigation Engine acts as the transition between conversation understanding and evidence retrieval.

5. INTERNAL ARCHITECTURE

The engine consists of four logical modules.

5.1 Intent Analyzer

Responsibilities

Detect educational intent
Identify information needs
Determine user objective
5.2 Clinical State Machine

Responsibilities

Determine current clinical state
Manage state transitions
Maintain structured patient journey

The Clinical State Machine serves as the internal decision core of the Navigation Engine.

5.3 Navigation Planner

Responsibilities

Select educational workflow
Route downstream knowledge retrieval
Assign evidence priority
Select response strategy
5.4 Navigation Context Builder

Responsibilities

Generate standardized Navigation Context
Normalize downstream inputs
Prepare structured execution metadata
6. PATIENT JOURNEY MODEL

Navigation is organized around the patient's clinical journey.

Illustrative high-level states include:

Cancer suspicion
Diagnosis
Pathology and staging
Treatment planning
Surgery
Systemic therapy
Radiotherapy
Active treatment
Follow-up
Recurrence
Palliative care
Survivorship

Additional disease-specific states may be introduced by downstream knowledge modules without altering the overall architecture.

7. CLINICAL STATE MACHINE

The Clinical State Machine maintains the patient's educational state rather than the conversational state.

State transitions are triggered by clinically meaningful events or user intent.

Conceptually:

Current Clinical State

+

User Intent

↓

Navigation Decision

↓

Navigation Context

This design enables consistent educational guidance while minimizing unnecessary conversational complexity.

8. NAVIGATION CONTEXT

The Navigation Engine outputs a structured Navigation Context rather than free-text.

A typical Navigation Context includes:

Clinical State
Educational Intent
Clinical Scenario
Safety Level
Knowledge Domain
Evidence Priority
Response Strategy

This structured representation becomes the primary input for downstream retrieval and response generation.

9. CLINICAL CONTEXT MEMORY

The Navigation Engine maintains a structured Clinical Context Memory.

The purpose is to preserve clinically relevant information while avoiding storage of unnecessary conversational content.

Examples include:

Cancer type
Disease stage
Treatment phase
Active therapy
Relevant clinical scenario

General conversational exchanges are intentionally excluded.

10. INTERACTION WITH OTHER COMPONENTS
Component	Interaction
Conversation Understanding	Provides normalized conversation input
Clinical Safety Layer	Performs safety validation before navigation
Knowledge Retrieval Layer	Receives Navigation Context
LLM Response Generation	Uses Navigation Context to generate educational responses
11. ARCHITECTURAL PRINCIPLES

The Clinical Navigation Engine follows the following architectural principles:

Deterministic routing
Explainable workflow
Separation of concerns
Modular extensibility
Guideline-oriented navigation
Human-centered educational design
12. FUTURE EXTENSIBILITY

Future versions may extend the Navigation Engine with:

disease-specific navigation modules;
multilingual navigation policies;
adaptive educational pathways;
personalized educational sequencing.

These extensions shall preserve the architecture defined in Version 1.0.

13. RELATED DOCUMENTS
Upstream
SYSTEM_ARCHITECTURE.md
PROJECT_FOUNDATION.md
MISSION_AND_SCOPE.md
NOVELTY.md
Downstream
MEDICAL_GOVERNANCE.md
SAFETY_FRAMEWORK.md
RAG_ARCHITECTURE.md
KNOWLEDGE_BASE.md
14. AMENDMENT TRACEABILITY
Version 1.0

Initial Release.

Locked Decisions Incorporated

LD-0013 — Navigation Responsibility
LD-0014 — Rule-first Navigation
LD-0015 — Patient Journey Navigation
LD-0016 — Navigation Context Object
LD-0017 — Clinical Context Memory
LD-0018 — Clinical State Machine