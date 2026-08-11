# 02_KNOWLEDGE_PASSPORT.md

# Knowledge Passport

---

# Identity

| Field | Value |
|-------|-------|
| Knowledge Passport ID | KP-PP-0055 |
| Population Package ID | PP-0055 |
| Clinical Knowledge Object | CKO-PP-0055 |
| Title | Multiple Organ Metastases |
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
| Educational Category | Metastatic Disease – Multiple Organ Metastases |
| Educational Level | Introductory |
| Clinical Complexity | Basic |
| Intended Audience | General public, patients diagnosed with gastric cancer, caregivers |
| Reading Level | Plain Language |
| Knowledge Granularity | Atomic (Single Educational Question) |
| Knowledge Scope | Multiple Organ Metastases |

---

# Patient Journey Classification

| Stage | Applicable |
|---------|------------|
| Before Diagnosis | |
| During Diagnosis | ✓ |
| Treatment Decision | ✓ |
| Active Treatment | ✓ |
| Follow-up | ✓ |
| Survivorship | ✓ |
| Palliative Care | ✓ |

**Reason:**

Patients frequently become concerned when imaging reports describe metastases in more than one organ. This Population Package explains the concept of **multiple organ metastases**, emphasizing that the number of organs involved is only one part of a comprehensive clinical assessment and should not be interpreted in isolation.

---

# Intended Runtime Usage

## Primary Runtime Role

- Foundational educational response

---

## Secondary Runtime Role

- Metastatic disease education
- Cancer staging education
- Patient reassurance
- Medical terminology explanation
- Prerequisite knowledge retrieval

---

## Typical Trigger Questions

- What does multiple organ metastases mean?
- Has my stomach cancer spread to several organs?
- Is cancer in two organs worse than cancer in one organ?
- Do all patients with metastatic stomach cancer have multiple organ metastases?
- Does the number of organs determine my prognosis?
- Why do doctors evaluate more than just the number of metastatic sites?

---

## Retrieval Priority

**Very High**

**Reason:**

Multiple organ metastases is a common concept encountered in radiology reports and oncology consultations. This Population Package serves as prerequisite knowledge for future Population Packages discussing oligometastatic disease, tumor burden, RECIST and treatment assessment.

---

# Knowledge Graph

## Prerequisite Population Packages

PP-0001 → PP-0054

---

## Related Population Packages

| PP | Relationship |
|----|--------------|
| PP-0045 | Introduces the M Category |
| PP-0046 | Defines metastasis |
| PP-0047 | Explains pathways of gastric cancer spread |
| PP-0048 | Peritoneal metastasis |
| PP-0049 | Liver metastasis |
| PP-0050 | Lung metastasis |
| PP-0051 | Bone metastasis |
| PP-0052 | Brain metastasis |
| PP-0054 | Distant lymph node metastasis |
| PP-0056 | Oligometastatic Disease |

---

## Recommended Next Population Package

**PP-0056**

**Oligometastatic Disease**

---

# Clinical Scope

## Included

- Definition of multiple organ metastases
- Explanation that metastatic disease may involve more than one distant organ
- Individual variation in metastatic patterns
- Relationship between multiple organ metastases and metastatic gastric cancer
- Importance of comprehensive clinical evaluation
- Explanation that the number of organs involved is only one aspect of assessment

---

## Explicitly Excluded

- Oligometastatic disease
- Tumor burden
- Number of metastatic lesions
- RECIST
- TNM staging details
- Treatment
- Palliative care
- Prognostic statistics

These topics are intentionally delegated to independent Population Packages.

---

# Authoritative Sources

## Primary Sources

1. National Cancer Institute (NCI PDQ)
   - Gastric Cancer Treatment
   - Gastric Cancer (Health Professional)

2. American Cancer Society (ACS)
   - Stomach Cancer

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

### Level I

- National Cancer Institute (NCI PDQ)

### Level I

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
| 1.0.0 | 2026-08-05 | Initial Gold Release Knowledge Passport |

---

# Future Update Trigger

This Knowledge Passport should be reviewed if:

- NCI substantially revises educational content regarding metastatic gastric cancer.
- ACS updates patient education concerning advanced or metastatic disease.
- NCCN or ESMO revises recommendations affecting assessment of metastatic disease extent.
- International oncology terminology regarding metastatic disease burden changes.
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

This Knowledge Passport is the official governance metadata for **PP-0055** and is fully compliant with the locked **Gold Population Package Specification v1.0**.