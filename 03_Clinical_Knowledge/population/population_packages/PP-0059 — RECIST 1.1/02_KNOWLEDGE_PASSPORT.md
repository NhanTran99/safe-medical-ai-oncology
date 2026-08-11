# 02_KNOWLEDGE_PASSPORT.md

# Knowledge Passport

---

# Identity

| Field | Value |
|-------|-------|
| Knowledge Passport ID | KP-PP-0059 |
| Population Package ID | PP-0059 |
| Clinical Knowledge Object | CKO-PP-0059 |
| Title | RECIST 1.1 |
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
| Educational Category | Treatment Response Assessment – RECIST 1.1 |
| Educational Level | Introductory |
| Clinical Complexity | Intermediate (Conceptual) |
| Intended Audience | General public, patients diagnosed with gastric cancer, caregivers |
| Reading Level | Plain Language |
| Knowledge Granularity | Atomic (Single Educational Question) |
| Knowledge Scope | RECIST 1.1 |

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

Patients may encounter **RECIST 1.1** in imaging reports, oncology consultations or clinical trial documents. This Population Package introduces RECIST 1.1 as the current widely used version of RECIST while intentionally avoiding technical measurement rules.

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

- What is RECIST 1.1?
- Why do doctors use RECIST 1.1?
- Is RECIST 1.1 different from RECIST?
- Do I need to understand RECIST 1.1 measurements?
- Does RECIST 1.1 determine my treatment?
- Why is RECIST 1.1 mentioned in my scan report?

---

## Retrieval Priority

**Very High**

**Reason:**

RECIST 1.1 is the current internationally adopted version of RECIST and serves as the conceptual gateway before patients learn about target lesions, measurable disease and response categories.

---

# Knowledge Graph

## Prerequisite Population Packages

PP-0001 → PP-0058

---

## Related Population Packages

| PP | Relationship |
|----|--------------|
| PP-0058 | Introduces RECIST |
| PP-0057 | Tumor Burden |
| PP-0060 | Target Lesions |
| Treatment Response | Clinical application |
| CT Scan | Imaging commonly used for RECIST 1.1 |
| MRI | Imaging commonly used for RECIST 1.1 |

---

## Recommended Next Population Package

**PP-0060**

**Target Lesions**

---

# Clinical Scope

## Included

- Definition of RECIST 1.1
- Relationship between RECIST and RECIST 1.1
- Purpose of RECIST 1.1
- Standardization of treatment response assessment
- Explanation that RECIST 1.1 is one component of clinical evaluation
- Recognition that technical rules are intended for healthcare professionals

---

## Explicitly Excluded

- Target lesions
- Non-target lesions
- Measurable disease
- Number of target lesions
- Lymph node measurement criteria
- Complete Response (CR)
- Partial Response (PR)
- Stable Disease (SD)
- Progressive Disease (PD)
- Sum of target lesion diameters
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
- RECIST 1.1 Working Group publication

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

### Background Terminology

- RECIST 1.1 Working Group publication

Technical implementation details are intentionally excluded.

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

- NCI substantially revises educational content regarding treatment response assessment.
- ACS updates patient education concerning treatment monitoring.
- NCCN or ESMO revises recommendations involving RECIST 1.1.
- The RECIST Working Group publishes a major conceptual revision replacing or substantially modifying RECIST 1.1.
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

This Knowledge Passport is the official governance metadata for **PP-0059** and is fully compliant with the locked **Gold Population Package Specification v1.0**.