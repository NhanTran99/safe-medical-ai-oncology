CLINICAL_KNOWLEDGE_OBJECT_TEMPLATE
DOCUMENT METADATA

Document ID

DOC-CK-007

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

CLINICAL_KNOWLEDGE_POPULATION_STRATEGY.md
KNOWLEDGE_OBJECT_SPECIFICATION.md
KNOWLEDGE_PASSPORT.md
KNOWLEDGE_RELATIONSHIP_MODEL.md
KNOWLEDGE_SOURCE_REGISTRY.md

Required By

All Clinical Knowledge Objects
Knowledge Passports
Evidence Packages
Clinical Validation Records

Last Updated

2026-08-03

1. PURPOSE

This document defines the standardized template governing every Clinical Knowledge Object (CKO) within the Safe Medical AI System.

It establishes the mandatory structure, granularity, lifecycle, and relationship model for all CKOs, ensuring that clinical knowledge is consistent, reusable, traceable, and retrieval-ready.

2. DESIGN PHILOSOPHY

Clinical Knowledge Objects shall follow:

One Concept — One Object
Retrieval-first Design
Patient-centered Organization
Evidence Traceability
Governance before Publication
Reusability
Technology Independence

CKOs represent governed knowledge assets rather than documents.

3. ROLE

The template standardizes:

CKO structure;
mandatory content sections;
object granularity;
relationships;
lifecycle.

Clinical recommendations remain governed by the linked Evidence Package and Knowledge Passport.

4. CKO IDENTITY

Each Clinical Knowledge Object shall represent exactly one clinical concept.

Examples include:

What is chemotherapy?
What is neutropenia?
Managing chemotherapy-induced nausea.
Preparing for a CT scan.
Understanding PD-L1 testing.

Multiple independent concepts shall never be merged into a single CKO.

5. GRANULARITY PRINCIPLE

Each CKO shall be sufficiently focused that it can:

answer one primary patient question;
support one retrieval intent;
remain independently maintainable;
be reused across multiple response scenarios.

If an object becomes too broad, it shall be decomposed into child CKOs.

6. STANDARDIZED CKO TEMPLATE

Every Clinical Knowledge Object shall contain the following mandatory sections.

A. Object Metadata
Object Identifier
Title
Clinical Domain
Clinical Topic
Version
Status
Last Updated
B. Clinical Overview

Defines the clinical concept in standardized language.

C. Patient Education Summary

Provides a concise patient-friendly explanation.

D. Key Messages

Lists the essential take-home points.

E. Clinical Context

Describes when and why the concept is relevant.

F. Patient Guidance

Explains recommended patient actions or considerations.

G. Safety Notes

Highlights safety-critical information requiring emphasis.

H. Related Clinical Concepts

Lists governed links to other CKOs.

I. Knowledge Passport Reference

Links the governing Knowledge Passport.

J. Evidence Package Reference

Links the supporting Evidence Package.

K. Governance Information

Documents approval status, reviewer, and governance metadata.

7. RELATIONSHIP MODEL

Each CKO may establish governed relationships with other CKOs.

Supported relationships include:

Parent
Child
Related Concept
Companion Topic
Prerequisite
Follow-up Topic

Relationship definitions shall follow the existing Knowledge Relationship Model.

8. LIFECYCLE

Every CKO follows the governed lifecycle:

Draft

↓

Evidence Population

↓

Clinical Review

↓

Governance Review

↓

Approved

↓

Active

↓

Amendment

↓

Version Upgrade (if required)

↓

Archived

Superseded CKOs remain archived to preserve organizational traceability.

9. GOVERNANCE PRINCIPLES

Every CKO shall:

maintain evidence provenance;
remain linked to an approved Knowledge Passport;
reference at least one governed Evidence Package;
comply with Knowledge Governance policies;
remain independently reviewable.
10. QUALITY REQUIREMENTS

Before activation, every CKO shall satisfy:

Clinical accuracy
Evidence traceability
Patient readability
Structural completeness
Governance approval
Retrieval readiness
Terminology consistency

Objects failing validation shall remain inactive.

11. RELATED DOCUMENTS
Upstream
CLINICAL_KNOWLEDGE_POPULATION_STRATEGY.md
KNOWLEDGE_OBJECT_SPECIFICATION.md
KNOWLEDGE_PASSPORT.md
KNOWLEDGE_RELATIONSHIP_MODEL.md
Downstream
Knowledge Passports
Evidence Packages
Clinical Validation Records
Retrieval-ready Knowledge Repository
12. AMENDMENT TRACEABILITY
Version 1.0

Initial release for Phase 3.

Integrated Locked Decisions:

LD-0386 — CKO Identity
LD-0387 — CKO Internal Structure
LD-0388 — Granularity Rule
LD-0389 — Relationship Model
LD-0390 — Lifecycle

This document establishes the universal template for all Clinical Knowledge Objects and serves as the foundational specification for large-scale clinical knowledge population.