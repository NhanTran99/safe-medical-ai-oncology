# 02_KNOWLEDGE_PASSPORT.md

# Knowledge Passport

---

# Identity

| Field | Value |
|-------|-------|
| Knowledge Passport ID | KP-PP-0039 |
| Population Package ID | PP-0039 |
| Clinical Knowledge Object | CKO-PP-0039 |
| Title | Histologic Differentiation |
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
| Educational Category | Cancer Pathology & Histologic Assessment |
| Educational Level | Introductory |
| Clinical Complexity | Basic |
| Intended Audience | General public, patients diagnosed with gastric cancer, caregivers |
| Reading Level | Plain Language |
| Knowledge Granularity | Atomic (Single Educational Question) |
| Knowledge Scope | Foundational Histologic Differentiation Education |

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

Histologic differentiation is frequently reported in pathology reports and often raises questions from patients because it is closely related to, but distinct from, tumor grade. This Population Package provides foundational education before patients encounter more advanced discussions of prognosis and pathological grading.

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

- What does histologic differentiation mean?
- What is a well differentiated cancer?
- What is a poorly differentiated cancer?
- Is histologic differentiation the same as tumor grade?
- Is differentiation the same as Lauren Classification?
- Why is differentiation written in my pathology report?
- Does differentiation affect treatment?

---

## Retrieval Priority

**High**

**Reason:**

Histologic differentiation is one of the most common microscopic descriptions in gastric cancer pathology reports and provides an important conceptual bridge between tumor grade and later discussions of prognosis.

---

# Knowledge Graph

## Prerequisite Population Packages

PP-0001 → PP-0038

---

## Related Population Packages

| PP | Relationship |
|----|--------------|
| PP-0035 | Introduces histologic types of gastric cancer |
| PP-0036 | Explains Lauren Classification |
| PP-0037 | Explains WHO Classification |
| PP-0038 | Explains Tumor Grade |
| PP-0040 | Introduces prognostic factors in gastric cancer |
| Understanding Your Pathology Report | Explains pathology report structure |

---

## Recommended Next Population Package

**PP-0040**

**Prognostic Factors in Gastric Cancer**

---

# Clinical Scope

## Included

- Definition of histologic differentiation
- Purpose of histologic differentiation
- Well differentiated
- Moderately differentiated
- Poorly differentiated
- Undifferentiated (introductory)
- Relationship to tumor grade
- Relationship to pathology reports
- Difference from histologic type
- Difference from Lauren Classification
- Difference from cancer stage

---

## Explicitly Excluded

- Histologic grading criteria
- WHO grading methodology
- Tumor grade scoring systems
- Lauren Classification details
- WHO Classification details
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

- NCI substantially revises educational content regarding histologic differentiation.
- ACS updates patient education on pathological terminology.
- NCCN or ESMO revises terminology related to histologic differentiation.
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

This Knowledge Passport is the official governance metadata for **PP-0039** and is fully compliant with the locked **Gold Population Package Specification v1.0**.