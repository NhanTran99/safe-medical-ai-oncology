DOCUMENT METADATA

Document ID

DOC-CK-008

Version

1.0

Status

LOCKED

Authority

Clinical Knowledge Governance

Owner

Project Coordinator

Strategist

ChatGPT

Implementation

Claude

Depends On

KNOWLEDGE_PASSPORT.md
CLINICAL_KNOWLEDGE_POPULATION_STRATEGY.md
CLINICAL_KNOWLEDGE_OBJECT_TEMPLATE.md
KNOWLEDGE_SOURCE_REGISTRY.md

Required By

All Knowledge Passports
Clinical Knowledge Objects
Evidence Packages
Governance Review

Last Updated

2026-08-03

1. PURPOSE

This document defines the standardized operational process for creating, completing, validating, and maintaining Knowledge Passports within the Safe Medical AI System.

Knowledge Passports function as the governance identity and lifecycle record for every Clinical Knowledge Object.

2. DESIGN PHILOSOPHY

Knowledge Passport population follows:

Governance before Publication
One Passport per Knowledge Object
Metadata-driven Governance
Complete Traceability
Amendment-first Evolution
Continuous Governance Synchronization

Knowledge Passports describe governed knowledge assets rather than clinical content.

3. ROLE

This document governs:

Passport creation;
Passport completion;
governance validation;
lifecycle synchronization.

It does not define:

patient education content;
evidence interpretation;
clinical recommendations;
retrieval behavior.
4. PASSPORT OWNERSHIP

Every Clinical Knowledge Object shall possess exactly one Knowledge Passport.

A Knowledge Passport shall never govern multiple Clinical Knowledge Objects.

Likewise, a Clinical Knowledge Object shall never possess multiple active Knowledge Passports.

This one-to-one relationship establishes an immutable governance identity throughout the object's lifecycle.

5. PASSPORT CONTENT SCOPE

Knowledge Passports shall contain governance metadata only.

Typical governed information includes:

object identity;
ownership;
clinical domain;
version;
lifecycle status;
provenance;
approval history;
reviewer information;
linked Evidence Packages;
dependencies;
amendment history.

Clinical narrative, patient education text, and medical recommendations shall remain within the Clinical Knowledge Object.

6. POPULATION TIMING

Knowledge Passport creation begins simultaneously with Clinical Knowledge Object creation.

The Passport is progressively completed during:

Evidence curation

↓

Knowledge construction

↓

Clinical review

↓

Governance review

↓

Approval

↓

Activation

Governance metadata evolves together with the associated Clinical Knowledge Object.

7. VALIDATION GATE

A Clinical Knowledge Object shall not enter the Active or Retrieval-ready state unless its Knowledge Passport satisfies all mandatory governance requirements.

Validation shall confirm:

complete metadata;
evidence linkage;
provenance;
approval status;
lifecycle consistency;
governance compliance.

Incomplete Passports automatically prevent downstream activation.

8. LIFECYCLE SYNCHRONIZATION

Knowledge Passports remain synchronized with their corresponding Clinical Knowledge Objects throughout the entire lifecycle.

Lifecycle synchronization includes:

creation;
review;
approval;
activation;
amendment;
version evolution;
archival.

Any governance amendment affecting a Clinical Knowledge Object shall be reflected in the corresponding Knowledge Passport.

9. GOVERNANCE PRINCIPLES

Every Knowledge Passport shall maintain:

one-to-one ownership;
complete provenance;
explicit evidence references;
lifecycle traceability;
governance transparency;
version integrity.

Knowledge Passports serve as the authoritative governance record for each Clinical Knowledge Object.

10. QUALITY REQUIREMENTS

Before approval, every Knowledge Passport shall satisfy:

ownership verification;
metadata completeness;
evidence linkage;
provenance verification;
lifecycle consistency;
governance approval;
traceability validation.

Only validated Passports may accompany Active Clinical Knowledge Objects.

11. RELATED DOCUMENTS
Upstream
KNOWLEDGE_PASSPORT.md
CLINICAL_KNOWLEDGE_POPULATION_STRATEGY.md
CLINICAL_KNOWLEDGE_OBJECT_TEMPLATE.md
KNOWLEDGE_SOURCE_REGISTRY.md
Downstream
Clinical Knowledge Objects
Evidence Packages
Clinical Validation Records
Retrieval-ready Knowledge Repository
12. AMENDMENT TRACEABILITY
Version 1.0

Initial Phase 3 release.

Integrated Locked Decisions:

LD-0391 — Passport Ownership
LD-0392 — Passport Content Scope
LD-0393 — Population Timing
LD-0394 — Validation Gate
LD-0395 — Lifecycle Synchronization

This document establishes the operational governance guide for all Knowledge Passports and standardizes their creation, validation, and maintenance throughout the knowledge population lifecycle.