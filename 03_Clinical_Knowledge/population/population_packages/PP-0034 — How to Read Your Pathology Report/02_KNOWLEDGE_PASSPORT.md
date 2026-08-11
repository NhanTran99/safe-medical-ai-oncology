# 02_KNOWLEDGE_PASSPORT.md

# Knowledge Passport

---

# Identity

| Field | Value |
|-------|-------|
| Knowledge Passport ID | KP-PP-0034 |
| Population Package ID | PP-0034 |
| Clinical Knowledge Object | CKO-PP-0034 |
| Title | How to Read Your Pathology Report |
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
| Educational Category | Cancer Diagnosis & Pathology Literacy |
| Educational Level | Introductory |
| Clinical Complexity | Basic |
| Intended Audience | General public, patients receiving pathology reports, caregivers |
| Reading Level | Plain Language |
| Knowledge Granularity | Atomic (Single Educational Question) |
| Knowledge Scope | Foundational Pathology Report Literacy |

---

# Patient Journey Classification

| Stage | Applicable |
|---------|------------|
| Before Diagnosis | ✓ |
| During Diagnosis | ✓ |
| Treatment Decision | ✓ |
| Active Treatment |  |
| Follow-up |  |
| Survivorship |  |
| Palliative Care |  |

**Reason:**

Patients often receive access to their pathology reports before meeting with their physician. This Population Package helps patients understand the overall structure and purpose of the report while encouraging discussion with the healthcare team rather than self-interpretation.

---

# Intended Runtime Usage

## Primary Runtime Role

- Foundational educational response

---

## Secondary Runtime Role

- Pathology literacy education
- Patient reassurance
- Clinical communication support
- Prerequisite knowledge retrieval

---

## Typical Trigger Questions

- How do I read my pathology report?
- Which part of the pathology report is most important?
- What does "Final Diagnosis" mean?
- Why is my pathology report so difficult to understand?
- Should I interpret my pathology report myself?
- What questions should I ask my doctor about my pathology report?
- Why is my pathology report being updated?

---

## Retrieval Priority

**High**

**Reason:**

Understanding how to navigate a pathology report is a common patient concern immediately after biopsy results become available and serves as the bridge between receiving results and discussing diagnosis with the healthcare team.

---

# Knowledge Graph

## Prerequisite Population Packages

PP-0001 → PP-0033

---

## Related Population Packages

| PP | Relationship |
|----|--------------|
| PP-0033 | Introduces pathology reports |
| PP-0035 | Explains histologic types of gastric cancer |
| Tumor Grade | Explains grading terminology |
| Biomarker Testing | Introduces pathology-based biomarker testing |
| Gastric Cancer Diagnosis | Explains complete diagnostic pathway |
| Treatment Planning | Uses pathology findings for treatment decisions |

---

## Recommended Next Population Package

**PP-0035**

**Histologic Types of Gastric Cancer**

---

# Clinical Scope

## Included

- Purpose of pathology reports
- General report structure
- Common report sections
- Final Diagnosis
- Additional comments
- Supplementary pathology testing
- Communication with the treating physician
- Patient questions

---

## Explicitly Excluded

- Histologic subtype interpretation
- Tumor grade interpretation
- Lauren classification
- WHO classification
- TNM staging
- HER2 interpretation
- MSI interpretation
- PD-L1 interpretation
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
- ACS updates patient education regarding pathology literacy.
- NCCN or ESMO revises recommendations affecting pathology reporting.
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

This Knowledge Passport is the official governance metadata for **PP-0034** and is fully compliant with the locked **Gold Population Package Specification v1.0**.