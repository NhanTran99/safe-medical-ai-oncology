# 02_KNOWLEDGE_PASSPORT.md

# Knowledge Passport

---

# Identity

| Field | Value |
|-------|-------|
| Knowledge Passport ID | KP-PP-0033 |
| Population Package ID | PP-0033 |
| Clinical Knowledge Object | CKO-PP-0033 |
| Title | Understanding Your Pathology Report |
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
| Educational Category | Cancer Diagnosis & Pathology |
| Educational Level | Introductory |
| Clinical Complexity | Basic |
| Intended Audience | General public, patients undergoing biopsy, caregivers |
| Reading Level | Plain Language |
| Knowledge Granularity | Atomic (Single Educational Question) |
| Knowledge Scope | Foundational Diagnostic Interpretation |

---

# Patient Journey Classification

| Stage | Applicable |
|---------|------------|
| Before Diagnosis | ✓ |
| During Diagnosis | ✓ |
| Treatment Decision |  |
| Active Treatment |  |
| Follow-up |  |
| Survivorship |  |
| Palliative Care |  |

**Reason:**

The pathology report represents the transition from tissue sampling to definitive diagnosis. Understanding its purpose enables patients to participate more effectively in discussions about diagnosis and future management.

---

# Intended Runtime Usage

## Primary Runtime Role

- Foundational educational response

---

## Secondary Runtime Role

- Pathology education
- Patient reassurance
- Prerequisite knowledge retrieval

---

## Typical Trigger Questions

- What is a pathology report?
- What does my pathology report mean?
- Who writes a pathology report?
- Why is my pathology report important?
- Can I understand my pathology report by myself?
- Does my pathology report confirm cancer?
- Why do I need to discuss my pathology report with my doctor?

---

## Retrieval Priority

**High**

**Reason:**

The pathology report is the central document linking biopsy findings to definitive diagnosis and forms the prerequisite for subsequent Population Packages involving histology, biomarkers and treatment planning.

---

# Knowledge Graph

## Prerequisite Population Packages

PP-0001 → PP-0032

---

## Related Population Packages

| PP | Relationship |
|----|--------------|
| PP-0032 | Explains why biopsy is performed |
| PP-0034 | Explains how to read a pathology report |
| Histopathology | Introduces microscopic tissue examination |
| Gastric Cancer Diagnosis | Explains complete diagnostic workflow |
| Biomarker Testing | Explains additional pathology-based testing |
| HER2 Testing | Expands targeted biomarker assessment |

---

## Recommended Next Population Package

**PP-0034**

**How to Read Your Pathology Report**

---

# Clinical Scope

## Included

- Definition of pathology report
- Role of the pathologist
- Relationship between biopsy and pathology
- Types of findings reported
- Importance of pathology for diagnosis
- Integration of pathology with other clinical information
- Importance of physician explanation
- General patient expectations

---

## Explicitly Excluded

- Interpretation of individual pathology report sections
- Histologic subtype
- Tumor grade
- Lauren classification
- WHO classification
- TNM staging
- Biomarker interpretation
- HER2
- MSI
- PD-L1
- Molecular pathology
- Treatment recommendations

These topics are intentionally delegated to independent Population Packages.

---

# Authoritative Sources

## Primary Sources

1. National Cancer Institute (NCI PDQ)
   - Gastric Cancer Treatment
   - Screening for Stomach Cancer

2. American Cancer Society (ACS)
   - Stomach Cancer
   - Diagnostic evaluation

---

## Supporting Sources

- NCCN Clinical Practice Guidelines
- JNCCN Gastric Cancer Guideline Discussion
- ESMO Clinical Practice Guidelines

---

# Evidence Classification

## Evidence Model

Authoritative Educational Synthesis

---

## Evidence Hierarchy

### Level 1

- National Cancer Institute (NCI PDQ)

### Level 1

- American Cancer Society (ACS)

### Supporting

- NCCN
- JNCCN
- ESMO

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
| 1.0.0 | 2026-08-04 | Initial Gold Release Knowledge Passport |

---

# Future Update Trigger

This Knowledge Passport should be reviewed if:

- NCI substantially revises educational content regarding pathology reports.
- ACS updates patient education on pathology interpretation.
- NCCN or ESMO revises recommendations affecting pathological diagnosis.
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

This Knowledge Passport is the official governance metadata for **PP-0033** and is fully compliant with the locked **Gold Population Package Specification v1.0**.