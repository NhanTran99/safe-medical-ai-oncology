# 02_KNOWLEDGE_PASSPORT.md

# Knowledge Passport

---

# Identity

| Field | Value |
|-------|-------|
| Knowledge Passport ID | KP-PP-0041 |
| Population Package ID | PP-0041 |
| Clinical Knowledge Object | CKO-PP-0041 |
| Title | Cancer Staging as a Prognostic Factor |
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
| Educational Category | Prognosis & Cancer Staging |
| Educational Level | Introductory |
| Clinical Complexity | Basic |
| Intended Audience | General public, patients diagnosed with gastric cancer, caregivers |
| Reading Level | Plain Language |
| Knowledge Granularity | Atomic (Single Educational Question) |
| Knowledge Scope | Cancer Stage as a Prognostic Factor |

---

# Patient Journey Classification

| Stage | Applicable |
|---------|------------|
| Before Diagnosis |  |
| During Diagnosis | ✓ |
| Treatment Decision | ✓ |
| Active Treatment | ✓ |
| Follow-up | ✓ |
| Survivorship | ✓ |
| Palliative Care | ✓ |

**Reason:**

Cancer stage is one of the first concepts discussed after diagnosis and remains central throughout treatment, follow-up and survivorship. This Population Package explains why stage is important without introducing the technical details of the TNM staging system.

---

# Intended Runtime Usage

## Primary Runtime Role

- Foundational educational response

---

## Secondary Runtime Role

- Prognosis education
- Cancer staging education
- Clinical terminology explanation
- Patient reassurance
- Prerequisite knowledge retrieval

---

## Typical Trigger Questions

- Why is cancer stage important?
- Does cancer stage affect prognosis?
- Is stage the most important prognostic factor?
- Can people with the same stage have different outcomes?
- Does an early stage always mean cure?
- Can prognosis change even if the stage stays the same?
- Why do doctors care so much about stage?

---

## Retrieval Priority

**Very High**

**Reason:**

Cancer stage is the single most frequently discussed prognostic concept after diagnosis and provides the foundation for understanding prognosis, treatment planning and later Population Packages covering the TNM staging system.

---

# Knowledge Graph

## Prerequisite Population Packages

PP-0001 → PP-0040

---

## Related Population Packages

| PP | Relationship |
|----|--------------|
| PP-0040 | Introduces prognostic factors |
| TNM Staging System | Explains technical staging system |
| PP-0038 | Explains tumor grade |
| PP-0039 | Explains histologic differentiation |
| Biomarker Testing | Additional prognostic information |
| Treatment Planning | Uses staging information |

---

## Recommended Next Population Package

**PP-0042**

**TNM Staging System**

---

# Clinical Scope

## Included

- Definition of cancer stage
- Why stage is important
- Stage as a prognostic factor
- Role of stage in treatment planning
- Relationship between stage and prognosis
- Why patients with the same stage may have different outcomes
- Dynamic nature of prognosis
- Stage as one component of overall assessment

---

## Explicitly Excluded

- TNM staging system
- T category
- N category
- M category
- AJCC Stage Groups
- Clinical stage
- Pathological stage
- Restaging
- Stage-specific survival statistics
- Stage-specific treatment recommendations

These topics are intentionally delegated to independent Population Packages.

---

# Authoritative Sources

## Primary Sources

1. National Cancer Institute (NCI PDQ)
   - Gastric Cancer Treatment

2. American Cancer Society (ACS)
   - Stomach Cancer
   - Understanding staging and prognosis

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

- NCI substantially revises guidance regarding gastric cancer staging.
- ACS updates patient education concerning staging and prognosis.
- NCCN or ESMO revises recommendations related to cancer staging.
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

This Knowledge Passport is the official governance metadata for **PP-0041** and is fully compliant with the locked **Gold Population Package Specification v1.0**.