# KNOWLEDGE ASSET WORKFLOW SOP

---

# DOCUMENT METADATA

Document ID:
DOC-KM-002

Document Name:
KNOWLEDGE_ASSET_WORKFLOW_SOP.md

Version:
1.0

Status:
LOCKED

Authority:
FOUNDATION

Owner:
Project Coordinator

Strategist:
ChatGPT

Implementation:
Claude

Depends On:

- DOCUMENT_ARCHITECTURE.md
- CORE_WORKING_RULES.md
- KNOWLEDGE_ASSET_REGISTRY_SPECIFICATION.md

Required By:

- Population Map
- Population Registry
- Population Package Production

Last Updated:
2026-08-04

---

# 1. PURPOSE

This document defines the official Standard Operating Procedure (SOP) governing how Knowledge Assets are collected, registered, reviewed, classified, mapped and transformed into Population Packages.

The workflow ensures:

- complete evidence traceability;
- consistent knowledge curation;
- efficient reuse of evidence;
- scalable Population Package production;
- long-term maintainability.

This SOP governs the operational workflow rather than the governance architecture.

---

# 2. SCOPE

This SOP applies to every Knowledge Asset entering the project.

Examples include:

External

- Clinical Guidelines
- Consensus Statements
- PDQ Documents
- Regulatory Documents
- Clinical Trials
- Systematic Reviews
- Meta-analyses
- Narrative Reviews

Internal

- Clinical Knowledge Objects
- Knowledge Passports
- Evidence Packages
- QA Reports
- Population Registry
- Population Map

---

# 3. ROLES

## Project Coordinator

Responsible for:

- approving new Knowledge Assets when necessary;
- approving Decision Batches;
- approving Locked Decisions.

---

## Strategist (ChatGPT)

Responsible for:

- reviewing Knowledge Assets;
- proposing mappings;
- identifying evidence gaps;
- preparing Decision Batches;
- ensuring evidence consistency.

---

## Implementation Agent (Claude)

Responsible for:

- producing approved Population Package artifacts;
- maintaining registry consistency;
- implementing approved specifications.

---

# 4. KNOWLEDGE SUPPLY CHAIN

Every Knowledge Asset follows the workflow below.

```
Knowledge Collection

↓

Knowledge Registration

↓

Metadata Extraction

↓

Topic Tagging

↓

Evidence Classification

↓

Population Package Mapping

↓

Coverage Review

↓

Decision Batch

↓

Project Coordinator LOCK

↓

Population Package Production

↓

Population Registry Update

↓

Repository Integration
```

No step shall be skipped.

---

# 5. OPERATIONAL STEPS

## STEP 1 — Knowledge Collection

Objective

Collect authoritative Knowledge Assets.

Typical sources include:

- NCCN
- NCI
- ACS
- ESMO
- JNCCN
- Regulatory Agencies

Output

Knowledge Asset ready for registration.

---

## STEP 2 — Knowledge Registration

Register the asset in the Knowledge Asset Registry.

Assign:

- Asset ID
- Title
- Asset Type
- Source
- Organization
- Publication Year

Output

Registered Knowledge Asset.

---

## STEP 3 — Metadata Extraction

Complete registry metadata.

Examples

- Version
- Clinical Domain
- Evidence Level
- Keywords
- Major Topics

Output

Metadata-complete asset.

---

## STEP 4 — Topic Tagging

Assign standardized topic tags.

Examples

- Diagnosis
- Biomarker
- HER2
- ADC
- Toxicity
- Nutrition

Multiple tags are encouraged.

Output

Indexed Knowledge Asset.

---

## STEP 5 — Evidence Classification

Classify evidence according to the project Evidence Hierarchy.

Examples

Level 1

- NCCN
- ESMO

Level 2

- NCI PDQ
- ACS

Level 3

- High-quality Systematic Reviews

Level 4

- Narrative Reviews

Output

Evidence-classified asset.

---

## STEP 6 — Population Package Mapping

Determine which Population Packages are supported.

Relationship:

One Knowledge Asset

↓

Many Population Packages

Many Knowledge Assets

↓

One Population Package

Output

Updated PP Mapping.

---

## STEP 7 — Coverage Review

Review whether sufficient evidence exists.

Questions

- Are Level 1 sources available?
- Is patient education available?
- Is evidence sufficient?
- Is another document required?

Possible outcomes

- Ready
- Additional evidence required

---

## STEP 8 — Decision Batch Preparation

Prepare a Discussion Batch following the Gold Workflow.

Include:

- Objective
- Must Decide Now
- Can Defer
- Trade-off
- Recommendation
- Decision Proposal

Output

Decision Batch ready.

---

## STEP 9 — Population Package Production

After Project Coordinator LOCK:

Immediately produce:

Part 1

- Clinical Knowledge Object
- Knowledge Passport

Part 2

- Primary Evidence Package
- QA Report
- Population Registry Update

No additional confirmation is required unless an architectural blocker exists.

---

## STEP 10 — Repository Integration

Update:

- Population Registry
- Repository
- Version History

Mark the Population Package as completed.

---

# 6. QUALITY CONTROL

Every Knowledge Asset shall satisfy:

✓ Metadata complete

✓ Evidence classified

✓ Topic tagged

✓ Population Package mapped

✓ Registry updated

Only then may it enter production.

---

# 7. TRACEABILITY

Every Population Package shall be traceable to:

Knowledge Asset

↓

Evidence Package

↓

Clinical Knowledge Object

↓

Population Registry

↓

Repository

No Population Package shall exist without upstream Knowledge Assets.

---

# 8. EXCEPTION HANDLING

Workflow interruption is permitted only when:

- authoritative evidence is unavailable;
- architectural ambiguity exists;
- governance conflict exists;
- Project Coordinator requests redesign.

Otherwise the workflow shall continue automatically.

---

# 9. RELATED DOCUMENTS

Upstream

- DOCUMENT_ARCHITECTURE.md
- CORE_WORKING_RULES.md
- KNOWLEDGE_ASSET_REGISTRY_SPECIFICATION.md

Downstream

- Population Map
- Population Registry
- Population Packages

---

# 10. EFFECTIVE STATUS

Status:

LOCKED

This SOP becomes the official operational workflow governing Knowledge Asset processing and Population Package production throughout the project.