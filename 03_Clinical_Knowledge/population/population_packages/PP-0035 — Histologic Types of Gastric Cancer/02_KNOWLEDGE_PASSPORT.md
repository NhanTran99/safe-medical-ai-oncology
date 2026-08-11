# 02_KNOWLEDGE_PASSPORT.md

# Knowledge Passport

---

# Identity

| Field | Value |
|-------|-------|
| Knowledge Passport ID | KP-PP-0035 |
| Population Package ID | PP-0035 |
| Clinical Knowledge Object | CKO-PP-0035 |
| Title | Histologic Types of Gastric Cancer |
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
| Educational Category | Cancer Pathology & Histology |
| Educational Level | Introductory |
| Clinical Complexity | Basic |
| Intended Audience | General public, patients diagnosed with gastric cancer, caregivers |
| Reading Level | Plain Language |
| Knowledge Granularity | Atomic (Single Educational Question) |
| Knowledge Scope | Foundational Histologic Classification |

---

# Patient Journey Classification

| Stage | Applicable |
|---------|------------|
| Before Diagnosis |  |
| During Diagnosis | ✓ |
| Treatment Decision | ✓ |
| Active Treatment |  |
| Follow-up |  |
| Survivorship |  |
| Palliative Care |  |

**Reason:**

Histologic type is identified after pathological examination of biopsy tissue and represents one of the first pathological characteristics patients encounter following diagnosis. This Population Package provides the foundation for understanding subsequent pathology classifications and biomarker reports.

---

# Intended Runtime Usage

## Primary Runtime Role

- Foundational educational response

---

## Secondary Runtime Role

- Pathology education
- Histology literacy
- Diagnostic terminology explanation
- Prerequisite knowledge retrieval

---

## Typical Trigger Questions

- What is a histologic type?
- What type of stomach cancer do I have?
- What does adenocarcinoma mean?
- What is diffuse-type gastric cancer?
- What is intestinal-type gastric cancer?
- What does signet ring cell carcinoma mean?
- Does my histologic type determine my treatment?

---

## Retrieval Priority

**High**

**Reason:**

Histologic type is one of the earliest pathological findings communicated to patients after diagnosis and serves as the prerequisite for understanding Lauren classification, WHO classification, tumor grade and molecular classification.

---

# Knowledge Graph

## Prerequisite Population Packages

PP-0001 → PP-0034

---

## Related Population Packages

| PP | Relationship |
|----|--------------|
| PP-0033 | Introduces pathology reports |
| PP-0034 | Explains pathology report structure |
| PP-0036 | Explains Lauren Classification |
| WHO Classification | Expands formal histologic classification |
| Tumor Grade | Explains tumor differentiation |
| Biomarker Testing | Introduces molecular characterization |

---

## Recommended Next Population Package

**PP-0036**

**Lauren Classification**

---

# Clinical Scope

## Included

- Definition of histology
- Definition of histologic type
- Microscopic appearance of tumors
- Adenocarcinoma
- Intestinal type
- Diffuse type
- Signet ring cell carcinoma (introductory)
- Relationship to pathology reports
- Role within overall diagnosis

---

## Explicitly Excluded

- Lauren classification details
- WHO classification
- Histologic grading
- Tumor differentiation
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
   - Gastric Cancer Genetics (supporting concepts)

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

- NCI substantially revises educational content regarding gastric cancer histology.
- ACS updates patient education on histologic classification.
- NCCN or ESMO revises terminology related to histologic classification.
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

This Knowledge Passport is the official governance metadata for **PP-0035** and is fully compliant with the locked **Gold Population Package Specification v1.0**.