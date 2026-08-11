# 02_KNOWLEDGE_PASSPORT.md

# Knowledge Passport

---

# Identity

| Field | Value |
|-------|-------|
| Knowledge Passport ID | KP-PP-0064 |
| Population Package ID | PP-0064 |
| Clinical Knowledge Object | CKO-PP-0064 |
| Title | Partial Response (PR) |
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
| Educational Category | Treatment Response Assessment – Partial Response |
| Educational Level | Introductory |
| Clinical Complexity | Intermediate (Conceptual) |
| Intended Audience | General public, patients diagnosed with gastric cancer, caregivers |
| Reading Level | Plain Language |
| Knowledge Granularity | Atomic (Single Educational Question) |
| Knowledge Scope | Partial Response (PR) |

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

Patients frequently encounter the term **Partial Response (PR)** after imaging assessments or during oncology consultations. This Population Package explains its meaning in plain language while preventing the common misconception that Partial Response means cancer has almost disappeared or no further treatment is needed.

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

- What does Partial Response mean?
- Is Partial Response good news?
- Does Partial Response mean my cancer is almost gone?
- Can treatment continue after Partial Response?
- What happens after Partial Response?
- Is Partial Response the same as Complete Response?

---

## Retrieval Priority

**Very High**

**Reason:**

Partial Response is one of the four major RECIST response categories and is frequently misunderstood by patients. Clear explanation helps patients understand that treatment is effective while recognizing that detectable cancer remains.

---

# Knowledge Graph

## Prerequisite Population Packages

PP-0001 → PP-0063

---

## Related Population Packages

| PP | Relationship |
|----|--------------|
| PP-0058 | Introduces RECIST |
| PP-0059 | Introduces RECIST 1.1 |
| PP-0063 | Complete Response (CR) |
| PP-0065 | Stable Disease (SD) |
| Treatment Response | Clinical application |
| Progressive Disease (PD) | Future comparison |

---

## Recommended Next Population Package

**PP-0065**

**Stable Disease (SD)**

---

# Clinical Scope

## Included

- Definition of Partial Response
- Partial Response as a standardized RECIST response category
- Meaning of significant tumor shrinkage under standardized assessment
- Difference between Partial Response and Complete Response
- Importance of continued treatment and follow-up
- Integration with comprehensive clinical assessment
- Explanation that Partial Response does not indicate complete disappearance of cancer

---

## Explicitly Excluded

- RECIST 1.1 technical criteria for Partial Response
- Percentage reduction required for PR
- Target lesion measurement
- Non-target lesion assessment
- Lymph node criteria
- Complete Response (CR) technical comparison
- Stable Disease (SD)
- Progressive Disease (PD)
- RECIST response algorithms
- Post-PR treatment strategies
- Cancer recurrence
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
- ACS updates patient education concerning treatment response during therapy.
- NCCN or ESMO revises recommendations involving RECIST response categories.
- The RECIST Working Group publishes major revisions affecting the definition of Partial Response.
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

This Knowledge Passport is the official governance metadata for **PP-0064** and is fully compliant with the locked **Gold Population Package Specification v1.0**.