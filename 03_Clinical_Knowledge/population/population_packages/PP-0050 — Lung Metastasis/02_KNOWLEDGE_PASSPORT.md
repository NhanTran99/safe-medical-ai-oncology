# 02_KNOWLEDGE_PASSPORT.md

# Knowledge Passport

---

# Identity

| Field | Value |
|-------|-------|
| Knowledge Passport ID | KP-PP-0050 |
| Population Package ID | PP-0050 |
| Clinical Knowledge Object | CKO-PP-0050 |
| Title | Lung Metastasis |
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
| Educational Category | Metastatic Disease – Lung Metastasis |
| Educational Level | Introductory |
| Clinical Complexity | Basic |
| Intended Audience | General public, patients diagnosed with gastric cancer, caregivers |
| Reading Level | Plain Language |
| Knowledge Granularity | Atomic (Single Educational Question) |
| Knowledge Scope | Lung Metastasis |

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

Lung metastasis is an important form of distant metastatic disease that patients frequently encounter during staging investigations and imaging reports. This Population Package provides foundational knowledge before introducing imaging interpretation, bronchoscopy, biopsy or treatment strategies.

---

# Intended Runtime Usage

## Primary Runtime Role

- Foundational educational response

---

## Secondary Runtime Role

- Metastatic disease education
- Organ-specific metastasis education
- Medical terminology explanation
- Patient reassurance
- Prerequisite knowledge retrieval

---

## Typical Trigger Questions

- What is lung metastasis?
- Has my stomach cancer spread to my lungs?
- Is lung metastasis the same as lung cancer?
- Can stomach cancer spread to the lungs?
- Does everyone with stomach cancer develop lung metastasis?
- How do doctors know whether cancer has spread to the lungs?

---

## Retrieval Priority

**Very High**

**Reason:**

Lung metastasis is one of the recognized distant metastatic sites in gastric cancer and serves as prerequisite knowledge for future Population Packages covering thoracic imaging, bronchoscopy, lung biopsy and treatment of pulmonary metastatic disease.

---

# Knowledge Graph

## Prerequisite Population Packages

PP-0001 → PP-0049

---

## Related Population Packages

| PP | Relationship |
|----|--------------|
| PP-0045 | Introduces the M Category |
| PP-0046 | Defines metastasis |
| PP-0047 | Explains pathways of gastric cancer spread |
| PP-0049 | Liver metastasis |
| PP-0051 | Bone metastasis |
| Understanding Your Pathology Report | Clinical interpretation |

---

## Recommended Next Population Package

**PP-0051**

**Bone Metastasis**

---

# Clinical Scope

## Included

- Definition of the lungs
- Definition of lung metastasis
- Relationship between gastric cancer and the lungs
- Difference between primary lung cancer and lung metastasis
- Relationship between lung metastasis and metastatic gastric cancer
- Importance of appropriate medical evaluation

---

## Explicitly Excluded

- Primary lung cancer
- Small cell lung cancer
- Non-small cell lung cancer
- M1 classification
- CT chest
- PET-CT
- Bronchoscopy
- Lung biopsy
- Pulmonary metastasectomy
- Radiation therapy
- Systemic therapy
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

- NCI substantially revises educational content regarding lung metastasis.
- ACS updates patient education concerning metastatic gastric cancer involving the lungs.
- NCCN or ESMO revises recommendations affecting pulmonary metastatic disease.
- AJCC introduces major conceptual changes affecting metastatic staging.
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

This Knowledge Passport is the official governance metadata for **PP-0050** and is fully compliant with the locked **Gold Population Package Specification v1.0**.