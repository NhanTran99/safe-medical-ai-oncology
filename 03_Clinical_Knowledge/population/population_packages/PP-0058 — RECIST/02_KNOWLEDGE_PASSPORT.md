# 02_KNOWLEDGE_PASSPORT.md

# Knowledge Passport

---

# Identity

| Field | Value |
|-------|-------|
| Knowledge Passport ID | KP-PP-0058 |
| Population Package ID | PP-0058 |
| Clinical Knowledge Object | CKO-PP-0058 |
| Title | RECIST (Response Evaluation Criteria in Solid Tumors) |
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
| Educational Category | Treatment Response Assessment – RECIST |
| Educational Level | Introductory |
| Clinical Complexity | Intermediate (Conceptual) |
| Intended Audience | General public, patients diagnosed with gastric cancer, caregivers |
| Reading Level | Plain Language |
| Knowledge Granularity | Atomic (Single Educational Question) |
| Knowledge Scope | RECIST |

---

# Patient Journey Classification

| Stage | Applicable |
|---------|------------|
| Before Diagnosis | |
| During Diagnosis | |
| Treatment Decision | ✓ |
| Active Treatment | ✓ |
| Follow-up | ✓ |
| Survivorship | ✓ |
| Palliative Care | ✓ |

**Reason:**

Patients frequently encounter the term **RECIST** in oncology consultations, clinical trial discussions and imaging reports. This Population Package introduces the concept of RECIST as a standardized assessment system before explaining its technical criteria in later Population Packages.

---

# Intended Runtime Usage

## Primary Runtime Role

- Foundational educational response

---

## Secondary Runtime Role

- Medical terminology explanation
- Treatment response education
- Imaging assessment education
- Clinical trial terminology support
- Prerequisite knowledge retrieval

---

## Typical Trigger Questions

- What is RECIST?
- What does RECIST stand for?
- Why is RECIST used?
- Is RECIST a cancer stage?
- Does RECIST determine my treatment?
- Why do doctors mention RECIST after my CT scan?

---

## Retrieval Priority

**Very High**

**Reason:**

RECIST is one of the most widely used standardized response assessment systems for solid tumors and is commonly referenced in oncology practice and research. This Population Package establishes the conceptual foundation before introducing RECIST 1.1, target lesions and response categories.

---

# Knowledge Graph

## Prerequisite Population Packages

PP-0001 → PP-0057

---

## Related Population Packages

| PP | Relationship |
|----|--------------|
| PP-0057 | Tumor Burden |
| PP-0059 | RECIST 1.1 |
| CT Scan | Imaging modality commonly used for RECIST assessment |
| MRI | Imaging modality commonly used for RECIST assessment |
| Treatment Response | Clinical application |

---

## Recommended Next Population Package

**PP-0059**

**RECIST 1.1**

---

# Clinical Scope

## Included

- Definition of RECIST
- Meaning of the acronym
- RECIST as a standardized assessment system
- Purpose of evaluating tumor changes over time
- General role of imaging studies
- Difference between RECIST and cancer stage
- Explanation that RECIST is not a treatment

---

## Explicitly Excluded

- RECIST 1.1 technical criteria
- Target lesions
- Non-target lesions
- Measurable disease
- Complete Response (CR)
- Partial Response (PR)
- Stable Disease (SD)
- Progressive Disease (PD)
- Sum of target lesion diameters
- PET response criteria
- iRECIST
- Treatment decisions
- Prognostic statistics

These topics are intentionally delegated to independent Population Packages.

---

# Authoritative Sources

## Primary Sources

1. National Cancer Institute (NCI PDQ)
   - Gastric Cancer Treatment

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

- NCI substantially revises educational content regarding response assessment in solid tumors.
- ACS updates patient education concerning treatment response monitoring.
- NCCN or ESMO revises recommendations regarding RECIST use.
- International RECIST Working Group publishes major conceptual revisions affecting patient education.
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

This Knowledge Passport is the official governance metadata for **PP-0058** and is fully compliant with the locked **Gold Population Package Specification v1.0**.