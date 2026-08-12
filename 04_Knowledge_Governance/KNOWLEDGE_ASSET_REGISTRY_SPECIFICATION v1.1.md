DOCUMENT METADATA
Field	Value
Document ID	DOC-KM-001
Document Name	KNOWLEDGE_ASSET_REGISTRY_SPECIFICATION.md
Version	1.0
Status	LOCKED
Authority	FOUNDATION
Owner	Project Coordinator
Strategist	ChatGPT
Implementation	Claude
Depends On	DOCUMENT_ARCHITECTURE.md, CORE_WORKING_RULES.md
Required By	Population Map, Population Registry, Population Packages
Last Updated	TBD
1. PURPOSE

This document defines the official governance, structure, metadata standard, lifecycle and management rules for all Knowledge Assets used throughout the project.

It establishes the Knowledge Asset Registry (KAR) as the single authoritative inventory of every external and internal knowledge asset supporting the Medical AI System.

The purpose of this specification is to ensure:

complete evidence traceability;
consistent knowledge organization;
efficient reuse of knowledge across Population Packages;
long-term maintainability;
scalable knowledge management.
2. SCOPE

This specification governs every Knowledge Asset that contributes to the project.

Examples include:

External Assets

Clinical Guidelines
Consensus Statements
PDQ Documents
Systematic Reviews
Meta-analyses
Randomized Trials
Regulatory Documents
Patient Education Documents

Internal Assets

Clinical Knowledge Objects
Population Packages
Knowledge Passports
Evidence Packages
QA Reports
Population Registry
Population Map

Future asset types may be added without changing this specification.

3. KNOWLEDGE ASSET DEFINITION

A Knowledge Asset is any governed resource that contributes knowledge to the project.

A Knowledge Asset may be:

external;
internal;
structured;
unstructured.

A Knowledge Asset is not defined by its file format.

Examples:

PDF
Markdown
Excel
CSV
Image
Database export

are merely storage formats.

4. KNOWLEDGE ASSET REGISTRY (KAR)

The Knowledge Asset Registry is the Single Source of Truth for all project knowledge assets.

The Registry records:

identity;
metadata;
ownership;
evidence level;
topic mapping;
Population Package mapping;
lifecycle status.

No Knowledge Asset shall exist outside the Registry.

5. KNOWLEDGE ASSET CLASSIFICATION

Every asset shall belong to one Asset Type.

External Clinical Evidence
Guideline
Consensus
PDQ
Regulatory
Clinical Trial
Systematic Review
Meta-analysis
Narrative Review
Internal Knowledge
Clinical Knowledge Object
Knowledge Passport
Evidence Package
QA Report
Population Registry
Population Map
Supporting Assets
Images
Figures
Tables
Datasets
Terminology
Taxonomy
SOP
Governance Documents

6. METADATA STANDARD

Every Knowledge Asset shall contain the following metadata.

Identity

- Asset ID
- Title
- Version
- Status
- Source

Classification

- Asset Type
- Clinical Domain
- Evidence Level

Usage

- Applicable Population Packages
- Major Topics
- Keywords

Lifecycle

- Imported
- Screened
- Indexed
- Mapped
- Active
- Archived

Repository / Integration Metadata

For repository-bound internal Knowledge Assets, the Registry may additionally
record:

- Repository Path
- Repository Integration Status
- Repository Verification Reference
- Immutable Repository / Commit / Release Identifier

Repository / integration metadata shall not replace the asset's governance
lifecycle status.

Lifecycle status and repository integration status are distinct governance
dimensions.



7. KNOWLEDGE LIFECYCLE

Every Knowledge Asset follows the lifecycle below.

Collected

↓

Registered

↓

Metadata Completed

↓

Topic Indexed

↓

Evidence Classified

↓

Population Package Mapping

↓

Active

↓

Archived

No step shall be skipped.

8. EVIDENCE CLASSIFICATION

Evidence shall follow the hierarchy already adopted by the project.

Typical examples include:

Level 1

NCCN
ESMO
ASCO

Level 2

NCI PDQ
ACS

Level 3

High-quality Systematic Reviews

Level 4

Narrative Reviews

This specification does not redefine the project's Evidence Framework.

9. TOPIC TAGGING

Knowledge Assets shall be indexed using standardized topic tags.

Examples:

Diagnosis
Surgery
Chemotherapy
Biomarkers
HER2
ADC
Toxicity
Nutrition

Multiple tags are encouraged.

10. POPULATION PACKAGE MAPPING

Each Knowledge Asset shall indicate the Population Packages it supports.

Example

MAT-0007

↓

PP-0022

PP-0023

PP-0024

PP-0028

PP-0029

One asset may support many Population Packages.

One Population Package may use many assets.

This defines a many-to-many relationship.

11. REGISTRY GOVERNANCE

The Knowledge Asset Registry is authoritative.

It shall be:

version controlled;
auditable;
continuously maintained.

Deletion is prohibited.

Assets may instead be marked:

Archived
Deprecated
Superseded
12. RELATIONSHIP TO OTHER FOUNDATIONAL DOCUMENTS

The Knowledge Asset Registry precedes the Population Layer.

Knowledge Assets

↓

Knowledge Asset Registry

↓

Population Map

↓

Population Registry

↓

Population Packages

↓

Repository
13. VERSIONING

Semantic Versioning shall be used.

Examples:

1.0.0
1.1.0
1.1.1
2.0.0
14. CHANGE MANAGEMENT

Amendments should:

preserve Asset IDs;
preserve traceability;
avoid duplicate registrations;
record amendment history.
15. EFFECTIVE STATUS

Status:

LOCKED

This specification becomes the official governance standard for Knowledge Asset management throughout the project.