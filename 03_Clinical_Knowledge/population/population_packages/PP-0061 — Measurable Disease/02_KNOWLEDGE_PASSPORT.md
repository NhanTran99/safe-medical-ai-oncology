# 02_KNOWLEDGE_PASSPORT.md

# Knowledge Passport

---

# Identity

| Field | Value |
|-------|-------|
| Knowledge Passport ID | KP-PP-0061 |
| Population Package ID | PP-0061 |
| Clinical Knowledge Object | CKO-PP-0061 |
| Title | Measurable Disease |
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
| Educational Category | Treatment Response Assessment – Measurable Disease |
| Educational Level | Introductory |
| Clinical Complexity | Intermediate (Conceptual) |
| Intended Audience | General public, patients diagnosed with gastric cancer, caregivers |
| Reading Level | Plain Language |
| Knowledge Granularity | Atomic (Single Educational Question) |
| Knowledge Scope | Measurable Disease |

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

Patients may encounter the term **measurable disease** in imaging reports, RECIST assessments or discussions about treatment response. This Population Package explains the concept in plain language before introducing the technical measurement criteria used in RECIST 1.1.

---

# Intended Runtime Usage

## Primary Runtime Role

- Foundational educational response

---

## Secondary Runtime Role

- Medical terminology explanation
- RECIST education
- Treatment response education
- Imaging assessment education
- Prerequisite knowledge retrieval

---

## Typical Trigger Questions

- What does measurable disease mean?
- Why is my cancer called measurable?
- Are all tumors measurable?
- Does non-measurable mean less serious?
- Who decides whether a lesion is measurable?
- Why do doctors describe some lesions as measurable?

---

## Retrieval Priority

**Very High**

**Reason:**

Measurable disease is a core concept within RECIST 1.1 and is essential for understanding subsequent concepts such as non-target lesions, response categories and standardized tumor measurements.

---

# Knowledge Graph

## Prerequisite Population Packages

PP-0001 → PP-0060

---

## Related Population Packages

| PP | Relationship |
|----|--------------|
| PP-0058 | Introduces RECIST |
| PP-0059 | Introduces RECIST 1.1 |
| PP-0060 | Target Lesions |
| PP-0062 | Non-target Lesions |
| Treatment Response | Clinical application |
| CT Scan | Common imaging modality |
| MRI | Common imaging modality |

---

## Recommended Next Population Package

**PP-0062**

**Non-target Lesions**

---

# Clinical Scope

## Included

- Definition of measurable disease
- Purpose of standardized measurement
- Importance for longitudinal assessment
- Explanation that not every lesion is measurable
- Continued clinical importance of non-measurable lesions
- Professional determination of measurability

---

## Explicitly Excluded

- RECIST size thresholds
- Lymph node measurement criteria
- Target lesions
- Non-target lesions
- Complete Response (CR)
- Partial Response (PR)
- Stable Disease (SD)
- Progressive Disease (PD)
- RECIST calculations
- CT protocols
- MRI protocols
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

Technical implementation details remain intentionally outside the scope of this foundational package.

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
- NCCN or ESMO revises recommendations involving measurable disease assessment.
- The RECIST Working Group publishes major revisions affecting measurable disease concepts.
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

This Knowledge Passport is the official governance metadata for **PP-0061** and is fully compliant with the locked **Gold Population Package Specification v1.0**.