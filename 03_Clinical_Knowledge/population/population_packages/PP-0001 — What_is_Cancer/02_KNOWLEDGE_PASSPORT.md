# 02_KNOWLEDGE_PASSPORT.md

# Knowledge Passport

---

# Identity

| Field | Value |
|-------|-------|
| Knowledge Passport ID | KP-PP-0001 |
| Population Package ID | PP-0001 |
| Clinical Knowledge Object | CKO-PP-0001 |
| Title | What is Cancer? |
| Clinical Domain | Understanding Cancer |
| Clinical Domain Code | UC |
| Population Batch | Understanding Cancer |
| Population Wave | Wave 1 |
| Version | 1.0.0 |
| Status | Approved |

---

# Knowledge Classification

| Field | Value |
|-------|-------|
| Knowledge Type | Foundational Medical Knowledge |
| Educational Category | Core Oncology Patient Education |
| Educational Level | Introductory |
| Clinical Complexity | Basic |
| Intended Audience | Newly diagnosed patients, caregivers, general public |
| Reading Level | Plain Language |
| Knowledge Granularity | Atomic (Single Educational Question) |
| Knowledge Scope | Foundational Concept |

---

# Patient Journey Classification

| Stage | Applicable |
|---------|------------|
| Before Diagnosis | ✓ |
| During Diagnosis | ✓ |
| Treatment Decision | ✓ |
| Active Treatment | ✓ |
| Follow-up | ✓ |
| Survivorship | ✓ |
| Palliative Care | ✓ |

Reason:

Cancer is a universal concept that supports every subsequent stage of the patient journey.

---

# Intended Runtime Usage

Primary Runtime Role

- Foundational educational response

Secondary Runtime Role

- Prerequisite knowledge retrieval

Typical Trigger Questions

- What is cancer?
- What does cancer mean?
- How does cancer happen?
- What is a malignant tumor?
- Is every tumor cancer?
- Is cancer inherited?
- Can cancer spread?
- Is cancer always fatal?

Retrieval Priority

High

Reason:

This Population Package serves as the entry point for the entire oncology knowledge graph.

---

# Knowledge Graph

## Prerequisite Population Packages

None

---

## Related Population Packages

| PP | Relationship |
|----|--------------|
| PP-0002 | Defines gastric cancer specifically |
| PP-0003 | Explains gastric adenocarcinoma |
| PP-0004 | Expands benign vs malignant tumors |
| PP-0005 | Explains carcinogenesis in greater depth |
| PP-0006 | Explains cancer metastasis |

---

## Recommended Next Population Package

PP-0002

What is Gastric Cancer?

---

# Clinical Scope

## Included

- Definition of cancer
- Basic cancer biology
- Difference between normal and cancer cells
- Benign vs malignant tumors
- Basic metastasis
- Basic hereditary cancer concept
- General prognosis concepts

---

## Explicitly Excluded

- Gastric cancer
- Cancer diagnosis
- Cancer staging
- Biomarkers
- Screening
- Prevention
- Surgery
- Chemotherapy
- Radiotherapy
- Targeted therapy
- Immunotherapy
- Palliative care

These topics are intentionally delegated to independent Population Packages.

---

# Authoritative Sources

## Primary Sources

1. National Cancer Institute (NCI)

2. American Cancer Society (ACS)

---

## Supporting Sources

- NCCN Guidelines for Patients (conceptual terminology only)

---

# Evidence Classification

Evidence Model

Authoritative Educational Synthesis

Evidence Hierarchy

Level 1

- National Cancer Institute

- American Cancer Society

Supporting

- NCCN Patient Guidelines

No lower-level evidence was required.

---

# Governance Metadata

| Field | Value |
|-------|-------|
| Clinical Governance | Enabled |
| Evidence Traceability | Complete |
| Scope Boundary | Defined |
| Knowledge Graph | Complete |
| Runtime Ready | Yes |
| Repository Ready | Yes |

---

# Version Control

| Item | Value |
|------|-------|
| Current Version | 1.0.0 |
| Major Version | 1 |
| Minor Version | 0 |
| Patch Version | 0 |

---

# Change History

| Version | Date | Description |
|----------|------|-------------|
| 1.0.0 | 2026-08-04 | Initial Gold Reference Knowledge Passport |

---

# Future Update Trigger

This Knowledge Passport should be reviewed if:

- NCI revises foundational cancer education.
- ACS substantially updates patient education content.
- Runtime retrieval strategy changes.
- Population Graph architecture changes.
- Governance specification changes.

---

# Quality Status

| Check | Result |
|-------|--------|
| Identity Complete | PASS |
| Classification Complete | PASS |
| Scope Clearly Defined | PASS |
| Knowledge Graph Complete | PASS |
| Runtime Metadata Complete | PASS |
| Governance Metadata Complete | PASS |
| Versioning Complete | PASS |

---

# Final Status

**APPROVED**

This Knowledge Passport is the official governance metadata for **PP-0001** and serves as the reference implementation for all future Population Packages.