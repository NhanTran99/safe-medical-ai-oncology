# 02_KNOWLEDGE_PASSPORT.md

# Knowledge Passport

---

# Identity

| Field | Value |
|-------|-------|
| Knowledge Passport ID | KP-PP-0094 |
| Population Package ID | PP-0094 |
| Clinical Knowledge Object | CKO-PP-0094 |
| Title | Prognostic Stage |
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
| Educational Category | Cancer Staging |
| Educational Level | Introductory |
| Clinical Complexity | Basic |
| Intended Audience | General public, patients diagnosed with gastric cancer, caregivers |
| Reading Level | Plain Language |
| Knowledge Granularity | Atomic (Single Educational Question) |
| Knowledge Scope | Prognostic Stage |

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

Some patients encounter the term **prognostic stage** during discussions about pathology, biomarkers, or treatment planning. This package introduces the concept without requiring disease-specific staging knowledge.

---

# Intended Runtime Usage

## Primary Runtime Role

- Foundational education on prognostic staging

---

## Secondary Runtime Role

- Cancer staging education
- Health literacy support
- Patient counseling
- Shared decision-making support
- Knowledge graph integration

---

## Typical Trigger Questions

- What is prognostic stage?
- Is prognostic stage different from TNM stage?
- Why does my doctor mention prognostic stage?
- Does every cancer have a prognostic stage?
- Is prognostic stage based only on tumor spread?
- What factors are included in prognostic stage?

---

## Retrieval Priority

**High**

**Reason:**

Prognostic staging represents an important evolution of cancer staging in selected malignancies. Patients benefit from understanding the concept before learning disease-specific applications.

---

# Knowledge Graph

## Prerequisite Population Packages

PP-0001 → PP-0093

---

## Related Population Packages

| PP | Relationship |
|----|--------------|
| PP-0089 | Tumor Grade |
| PP-0090 | TNM Staging |
| PP-0091 | Understanding Stage I–IV |
| PP-0095 | Prognostic Factors |
| Biomarker Testing | Related |

---

## Recommended Next Population Package

**PP-0095**

**Prognostic Factors**

---

# Clinical Scope

## Included

- Definition
- Purpose
- Relationship with TNM
- Additional prognostic information
- Clinical role
- Patient interpretation

---

## Explicitly Excluded

- Disease-specific prognostic staging
- Biomarker algorithms
- Prognostic models
- Survival prediction
- Treatment recommendations

These topics are intentionally delegated to independent Population Packages.

---

# Authoritative Sources

## Primary Sources

1. AJCC Cancer Staging Manual
2. National Cancer Institute (NCI PDQ)
3. American Cancer Society (ACS)

---

## Supporting Sources

- NCCN Clinical Practice Guidelines
- JNCCN
- ESMO Clinical Practice Guidelines

---

# Evidence Classification

## Evidence Model

Authoritative Educational Synthesis

---

## Evidence Hierarchy

### Level I

- AJCC
- National Cancer Institute
- American Cancer Society

### Supporting

- NCCN
- JNCCN
- ESMO

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
| 1.0.0 | 2026-08-06 | Initial Gold Release Knowledge Passport |

---

# Final Status

**APPROVED**

This Knowledge Passport is the official governance metadata for **PP-0094** and is fully compliant with the locked **Gold Population Package Specification v1.0**.