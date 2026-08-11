# 02_KNOWLEDGE_PASSPORT.md

# Knowledge Passport

---

# Identity

| Field | Value |
|-------|-------|
| Knowledge Passport ID | KP-PP-0037 |
| Population Package ID | PP-0037 |
| Clinical Knowledge Object | CKO-PP-0037 |
| Title | WHO Classification of Gastric Cancer |
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
| Educational Category | Cancer Pathology & Histologic Classification |
| Educational Level | Introductory |
| Clinical Complexity | Basic |
| Intended Audience | General public, patients diagnosed with gastric cancer, caregivers |
| Reading Level | Plain Language |
| Knowledge Granularity | Atomic (Single Educational Question) |
| Knowledge Scope | Foundational WHO Histologic Classification |

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

The WHO Classification is frequently included in pathology reports and provides internationally standardized terminology for describing gastric cancer histology. This Population Package enables patients to understand the purpose of this classification before learning more advanced pathological concepts.

---

# Intended Runtime Usage

## Primary Runtime Role

- Foundational educational response

---

## Secondary Runtime Role

- Histology education
- Pathology terminology explanation
- Patient reassurance
- Prerequisite knowledge retrieval

---

## Typical Trigger Questions

- What is the WHO Classification?
- Why is the WHO Classification listed in my pathology report?
- What does tubular adenocarcinoma mean?
- What is poorly cohesive carcinoma?
- Is the WHO Classification the same as the Lauren Classification?
- Does the WHO Classification determine my treatment?
- Why do doctors use the WHO Classification?

---

## Retrieval Priority

**High**

**Reason:**

WHO Classification is one of the principal international systems used in gastric cancer pathology and serves as a prerequisite for understanding tumor grade, histologic differentiation and individual histologic subtypes.

---

# Knowledge Graph

## Prerequisite Population Packages

PP-0001 → PP-0036

---

## Related Population Packages

| PP | Relationship |
|----|--------------|
| PP-0035 | Introduces histologic types of gastric cancer |
| PP-0036 | Explains Lauren Classification |
| PP-0038 | Explains Tumor Grade |
| Histologic Differentiation | Explains differentiation terminology |
| Molecular Classification | Introduces molecular subtypes |
| Biomarker Testing | Introduces molecular pathology |

---

## Recommended Next Population Package

**PP-0038**

**Tumor Grade**

---

# Clinical Scope

## Included

- Definition of WHO Classification
- Purpose of WHO Classification
- International standardization
- Common WHO histologic subtypes
- Relationship to pathology reports
- Difference from Lauren Classification
- Difference from cancer staging
- Role within overall pathological assessment

---

## Explicitly Excluded

- Histologic diagnostic criteria
- Microscopic features of each subtype
- Lauren Classification details
- Tumor grade
- Histologic differentiation
- Molecular classification
- MSI subtype
- EBV-associated gastric cancer
- HER2
- PD-L1
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

- NCI substantially revises educational content regarding WHO histologic classification.
- ACS updates patient education regarding gastric cancer pathology.
- NCCN or ESMO revises terminology related to WHO Classification.
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

This Knowledge Passport is the official governance metadata for **PP-0037** and is fully compliant with the locked **Gold Population Package Specification v1.0**.