# 02_KNOWLEDGE_PASSPORT.md

# Knowledge Passport

---

# Identity

| Field | Value |
|-------|-------|
| Knowledge Passport ID | KP-PP-0062 |
| Population Package ID | PP-0062 |
| Clinical Knowledge Object | CKO-PP-0062 |
| Title | Non-target Lesions |
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
| Educational Category | Treatment Response Assessment – Non-target Lesions |
| Educational Level | Introductory |
| Clinical Complexity | Intermediate (Conceptual) |
| Intended Audience | General public, patients diagnosed with gastric cancer, caregivers |
| Reading Level | Plain Language |
| Knowledge Granularity | Atomic (Single Educational Question) |
| Knowledge Scope | Non-target Lesions |

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

Patients may encounter the term **non-target lesions** in RECIST assessments, radiology reports or oncology consultations. This Population Package explains the concept in plain language before introducing the technical RECIST response rules for these lesions.

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

- What are non-target lesions?
- Why wasn't one of my tumors selected as a target lesion?
- Are non-target lesions still monitored?
- Does a non-target lesion mean it is less important?
- Why aren't all tumors measured?
- How do doctors evaluate non-target lesions?

---

## Retrieval Priority

**Very High**

**Reason:**

Non-target lesions are a fundamental concept in RECIST 1.1 and complete the patient's understanding of how standardized response assessment considers the entire burden of disease rather than only measured lesions.

---

# Knowledge Graph

## Prerequisite Population Packages

PP-0001 → PP-0061

---

## Related Population Packages

| PP | Relationship |
|----|--------------|
| PP-0058 | Introduces RECIST |
| PP-0059 | Introduces RECIST 1.1 |
| PP-0060 | Target Lesions |
| PP-0061 | Measurable Disease |
| PP-0063 | Complete Response (CR) |
| Treatment Response | Clinical application |
| CT Scan | Common imaging modality |
| MRI | Common imaging modality |

---

## Recommended Next Population Package

**PP-0063**

**Complete Response (CR)**

---

# Clinical Scope

## Included

- Definition of non-target lesions
- Difference between target and non-target lesions
- Continued monitoring during treatment
- Clinical importance of non-target lesions
- Integration into comprehensive disease assessment
- Explanation that classification does not reflect severity

---

## Explicitly Excluded

- RECIST 1.1 technical criteria for non-target lesions
- Complete Response (CR)
- Progressive Disease (PD)
- Unequivocal progression
- Measurable disease
- Target lesions
- RECIST calculations
- Imaging protocols
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

# Evidence Hierarchy

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

Technical response criteria remain intentionally outside the scope of this foundational package.

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
- NCCN or ESMO revises recommendations involving non-target lesion assessment.
- The RECIST Working Group publishes major revisions affecting non-target lesion concepts.
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

This Knowledge Passport is the official governance metadata for **PP-0062** and is fully compliant with the locked **Gold Population Package Specification v1.0**.