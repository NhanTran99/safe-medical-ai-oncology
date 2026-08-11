# 02_KNOWLEDGE_PASSPORT.md

# Knowledge Passport

---

# Identity

| Field | Value |
|-------|-------|
| Knowledge Passport ID | KP-PP-0065 |
| Population Package ID | PP-0065 |
| Clinical Knowledge Object | CKO-PP-0065 |
| Title | Stable Disease (SD) |
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
| Educational Category | Treatment Response Assessment – Stable Disease |
| Educational Level | Introductory |
| Clinical Complexity | Intermediate (Conceptual) |
| Intended Audience | General public, patients diagnosed with gastric cancer, caregivers |
| Reading Level | Plain Language |
| Knowledge Granularity | Atomic (Single Educational Question) |
| Knowledge Scope | Stable Disease (SD) |

---

# Patient Journey Classification

| Stage | Applicable |
|---------|------------|
| Before Diagnosis | |
| During Diagnosis | |
| Treatment Decision | |
| Active Treatment | ✓ |
| Follow-up | ✓ |
| Survivorship | ✓ |
| Palliative Care | ✓ |

**Reason:**

Patients frequently misunderstand **Stable Disease (SD)** as meaning treatment has failed. This Population Package explains that SD is a standardized treatment response category and that maintaining disease stability may itself represent a meaningful treatment outcome.

---

# Intended Runtime Usage

## Primary Runtime Role

- Foundational educational response

---

## Secondary Runtime Role

- Medical terminology explanation
- RECIST education
- Treatment response education
- Imaging result interpretation support
- Prerequisite knowledge retrieval

---

## Typical Trigger Questions

- What does Stable Disease mean?
- Is Stable Disease bad?
- Does Stable Disease mean treatment is not working?
- Can cancer stay stable for a long time?
- What happens after Stable Disease?
- Is Stable Disease better than Progressive Disease?

---

## Retrieval Priority

**Very High**

**Reason:**

Stable Disease is commonly misunderstood by patients. Accurate explanation helps prevent unnecessary anxiety while clarifying that disease stabilization may represent a successful treatment outcome depending on the clinical context.

---

# Knowledge Graph

## Prerequisite Population Packages

PP-0001 → PP-0064

---

## Related Population Packages

| PP | Relationship |
|----|--------------|
| PP-0058 | Introduces RECIST |
| PP-0059 | Introduces RECIST 1.1 |
| PP-0063 | Complete Response (CR) |
| PP-0064 | Partial Response (PR) |
| PP-0066 | Progressive Disease (PD) |
| Treatment Response | Clinical application |

---

## Recommended Next Population Package

**PP-0066**

**Progressive Disease (PD)**

---

# Clinical Scope

## Included

- Definition of Stable Disease
- Stable Disease as a standardized RECIST response category
- Meaning of disease stability under standardized assessment
- Explanation that Stable Disease is not equivalent to treatment failure
- Importance of continued monitoring and treatment planning
- Integration with comprehensive clinical assessment

---

## Explicitly Excluded

- RECIST technical criteria for Stable Disease
- Percentage thresholds
- Target lesion measurement
- Non-target lesion assessment
- Lymph node criteria
- Progressive Disease
- RECIST response algorithms
- Post-SD treatment
- Prognostic statistics
- Cancer recurrence

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
- ACS updates patient education concerning disease stabilization during treatment.
- NCCN or ESMO revises recommendations involving RECIST response categories.
- The RECIST Working Group publishes major revisions affecting the definition of Stable Disease.
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

This Knowledge Passport is the official governance metadata for **PP-0065** and is fully compliant with the locked **Gold Population Package Specification v1.0**.