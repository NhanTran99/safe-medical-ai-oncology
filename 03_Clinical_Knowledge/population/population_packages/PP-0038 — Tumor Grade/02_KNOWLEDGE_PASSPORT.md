# 02_KNOWLEDGE_PASSPORT.md

# Knowledge Passport

---

# Identity

| Field | Value |
|-------|-------|
| Knowledge Passport ID | KP-PP-0038 |
| Population Package ID | PP-0038 |
| Clinical Knowledge Object | CKO-PP-0038 |
| Title | Tumor Grade |
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
| Educational Category | Cancer Pathology & Tumor Assessment |
| Educational Level | Introductory |
| Clinical Complexity | Basic |
| Intended Audience | General public, patients diagnosed with gastric cancer, caregivers |
| Reading Level | Plain Language |
| Knowledge Granularity | Atomic (Single Educational Question) |
| Knowledge Scope | Foundational Tumor Grade Education |

---

# Patient Journey Classification

| Stage | Applicable |
|---------|------------|
| Before Diagnosis |  |
| During Diagnosis | ✓ |
| Treatment Decision | ✓ |
| Active Treatment | ✓ |
| Follow-up |  |
| Survivorship |  |
| Palliative Care |  |

**Reason:**

Tumor grade is commonly reported after pathological examination and frequently appears in pathology reports before treatment planning. This Population Package provides patients with a clear understanding of what tumor grade means without encouraging self-interpretation of prognosis or treatment.

---

# Intended Runtime Usage

## Primary Runtime Role

- Foundational educational response

---

## Secondary Runtime Role

- Pathology terminology explanation
- Histology education
- Patient reassurance
- Prerequisite knowledge retrieval

---

## Typical Trigger Questions

- What does tumor grade mean?
- What is a well differentiated tumor?
- What does poorly differentiated mean?
- Is tumor grade the same as cancer stage?
- Why is tumor grade listed in my pathology report?
- Does tumor grade affect treatment?
- How is tumor grade determined?

---

## Retrieval Priority

**High**

**Reason:**

Tumor grade is one of the most frequently encountered pathological terms in gastric cancer pathology reports and serves as a prerequisite for understanding histologic differentiation and prognostic pathology concepts.

---

# Knowledge Graph

## Prerequisite Population Packages

PP-0001 → PP-0037

---

## Related Population Packages

| PP | Relationship |
|----|--------------|
| PP-0035 | Introduces histologic types of gastric cancer |
| PP-0036 | Explains Lauren Classification |
| PP-0037 | Explains WHO Classification |
| PP-0039 | Explains Histologic Differentiation |
| Understanding Your Pathology Report | Explains pathology report structure |
| Prognostic Factors | Future clinical context |

---

## Recommended Next Population Package

**PP-0039**

**Histologic Differentiation**

---

# Clinical Scope

## Included

- Definition of tumor grade
- Purpose of tumor grading
- Well differentiated
- Moderately differentiated
- Poorly differentiated
- Relationship to pathology reports
- Difference between tumor grade and cancer stage
- Role within overall pathological assessment

---

## Explicitly Excluded

- Histologic grading criteria
- Histologic differentiation mechanisms
- WHO grading methodology
- Lauren Classification
- WHO Classification
- TNM staging
- Molecular classification
- MSI subtype
- EBV-associated gastric cancer
- Prognostic interpretation
- Treatment implications

These topics are intentionally delegated to independent Population Packages.

---

# Authoritative Sources

## Primary Sources

1. National Cancer Institute (NCI PDQ)
   - Gastric Cancer Treatment

2. American Cancer Society (ACS)
   - Stomach Cancer
   - Pathology and diagnosis

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

- NCI substantially revises educational content regarding tumor grading.
- ACS updates patient education on pathology terminology.
- NCCN or ESMO revises terminology related to tumor grading.
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

This Knowledge Passport is the official governance metadata for **PP-0038** and is fully compliant with the locked **Gold Population Package Specification v1.0**.