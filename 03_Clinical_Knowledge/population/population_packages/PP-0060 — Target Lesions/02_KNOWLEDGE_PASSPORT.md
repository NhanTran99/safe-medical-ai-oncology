# 02_KNOWLEDGE_PASSPORT.md

# Knowledge Passport

---

# Identity

| Field | Value |
|-------|-------|
| Knowledge Passport ID | KP-PP-0060 |
| Population Package ID | PP-0060 |
| Clinical Knowledge Object | CKO-PP-0060 |
| Title | Target Lesions |
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
| Educational Category | Treatment Response Assessment – Target Lesions |
| Educational Level | Introductory |
| Clinical Complexity | Intermediate (Conceptual) |
| Intended Audience | General public, patients diagnosed with gastric cancer, caregivers |
| Reading Level | Plain Language |
| Knowledge Granularity | Atomic (Single Educational Question) |
| Knowledge Scope | Target Lesions |

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

Patients may see the term **target lesions** in imaging reports, RECIST assessments or clinical trial documents. This Population Package introduces the concept as selected lesions used for standardized follow-up while avoiding technical measurement rules.

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

- What are target lesions?
- Why did my doctor choose only some tumors?
- Why aren't all tumors measured?
- Are tumors that are not target lesions still important?
- Who decides which lesions become target lesions?
- Does a target lesion mean it is the most dangerous tumor?

---

## Retrieval Priority

**Very High**

**Reason:**

Target lesions are a core concept within RECIST 1.1 and are frequently mentioned during imaging follow-up. Understanding this concept is essential before learning measurable disease, non-target lesions and RECIST response categories.

---

# Knowledge Graph

## Prerequisite Population Packages

PP-0001 → PP-0059

---

## Related Population Packages

| PP | Relationship |
|----|--------------|
| PP-0058 | Introduces RECIST |
| PP-0059 | Introduces RECIST 1.1 |
| PP-0061 | Measurable Disease |
| PP-0062 | Non-target Lesions |
| Treatment Response | Clinical application |
| CT Scan | Common imaging modality |
| MRI | Common imaging modality |

---

## Recommended Next Population Package

**PP-0061**

**Measurable Disease**

---

# Clinical Scope

## Included

- Definition of target lesions
- Purpose of selecting target lesions
- Standardized longitudinal follow-up
- Professional selection process
- Continued importance of non-selected lesions
- Explanation that patients should not self-identify target lesions

---

## Explicitly Excluded

- Measurable disease
- Non-target lesions
- Maximum number of target lesions
- Target lesion size criteria
- Lymph node measurement criteria
- Sum of target lesion diameters
- Complete Response (CR)
- Partial Response (PR)
- Stable Disease (SD)
- Progressive Disease (PD)
- RECIST calculations
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

- NCI substantially revises educational content regarding response assessment.
- ACS updates patient education concerning treatment monitoring.
- NCCN or ESMO revises recommendations involving RECIST target lesion selection.
- The RECIST Working Group publishes major revisions affecting target lesion concepts.
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

This Knowledge Passport is the official governance metadata for **PP-0060** and is fully compliant with the locked **Gold Population Package Specification v1.0**.