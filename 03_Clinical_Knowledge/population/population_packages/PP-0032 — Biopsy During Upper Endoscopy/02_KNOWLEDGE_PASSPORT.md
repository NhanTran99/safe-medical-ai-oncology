# 02_KNOWLEDGE_PASSPORT.md

# Knowledge Passport

---

# Identity

| Field | Value |
|-------|-------|
| Knowledge Passport ID | KP-PP-0032 |
| Population Package ID | PP-0032 |
| Clinical Knowledge Object | CKO-PP-0032 |
| Title | Biopsy During Upper Endoscopy |
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
| Educational Category | Cancer Diagnosis & Tissue Diagnosis |
| Educational Level | Introductory |
| Clinical Complexity | Basic |
| Intended Audience | General public, patients undergoing upper endoscopy, caregivers |
| Reading Level | Plain Language |
| Knowledge Granularity | Atomic (Single Educational Question) |
| Knowledge Scope | Foundational Diagnostic Procedure |

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

Biopsy is a fundamental diagnostic procedure that bridges upper endoscopy and definitive pathological diagnosis. Understanding its purpose helps patients interpret the diagnostic process and reduces unnecessary anxiety while awaiting pathology results.

---

# Intended Runtime Usage

## Primary Runtime Role

- Foundational educational response

---

## Secondary Runtime Role

- Diagnostic procedure education
- Patient reassurance
- Prerequisite knowledge retrieval

---

## Typical Trigger Questions

- What is a biopsy?
- Why did my doctor take a biopsy?
- Does having a biopsy mean I have cancer?
- What happens to my biopsy sample?
- Why do biopsy results take several days?
- Can doctors diagnose cancer without a biopsy?
- What information does a biopsy provide?

---

## Retrieval Priority

**High**

**Reason:**

Biopsy is one of the most frequently misunderstood parts of the gastric cancer diagnostic pathway and serves as the prerequisite for pathology, biomarker testing and definitive diagnosis.

---

# Knowledge Graph

## Prerequisite Population Packages

PP-0001 → PP-0031

---

## Related Population Packages

| PP | Relationship |
|----|--------------|
| PP-0031 | Introduces upper endoscopy |
| PP-0033 | Explains pathology reports |
| Gastric Cancer Diagnosis | Explains complete diagnostic workflow |
| HER2 Testing | Explains biomarker evaluation |
| MSI Testing | Explains molecular biomarker testing |
| PD-L1 Testing | Explains immunotherapy biomarker testing |

---

## Recommended Next Population Package

**PP-0033**

**Pathology Report**

---

# Clinical Scope

## Included

- Definition of biopsy
- Purpose of biopsy
- Relationship between endoscopy and biopsy
- Basic explanation of tissue sampling
- Role of biopsy in diagnosing stomach diseases
- Why pathology examination is required
- Waiting for biopsy results
- General patient expectations

---

## Explicitly Excluded

- Biopsy techniques
- Histopathology interpretation
- Histologic classification
- Biomarker testing
- HER2
- MSI
- PD-L1
- Molecular pathology
- Cancer staging
- Treatment planning

These topics are intentionally delegated to independent Population Packages.

---

# Authoritative Sources

## Primary Sources

1. National Cancer Institute (NCI PDQ)
   - Screening for Stomach Cancer
   - Gastric Cancer Treatment

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

- NCI substantially revises educational content regarding biopsy.
- ACS updates patient education regarding tissue diagnosis.
- NCCN or ESMO revises recommendations affecting diagnostic biopsy.
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

This Knowledge Passport is the official governance metadata for **PP-0032** and is fully compliant with the locked **Gold Population Package Specification v1.0**.