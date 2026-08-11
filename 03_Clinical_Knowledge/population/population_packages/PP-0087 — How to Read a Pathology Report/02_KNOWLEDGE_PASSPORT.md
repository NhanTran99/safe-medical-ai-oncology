# 02_KNOWLEDGE_PASSPORT.md

# Knowledge Passport

---

# Identity

| Field | Value |
|-------|-------|
| Knowledge Passport ID | KP-PP-0087 |
| Population Package ID | PP-0087 |
| Clinical Knowledge Object | CKO-PP-0087 |
| Title | How to Read a Pathology Report |
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
| Educational Category | Cancer Diagnosis |
| Educational Level | Introductory Navigation Guide |
| Clinical Complexity | Basic |
| Intended Audience | General public, patients diagnosed with gastric cancer, caregivers |
| Reading Level | Plain Language |
| Knowledge Granularity | Atomic (Single Educational Question) |
| Knowledge Scope | How to Read a Pathology Report |

---

# Patient Journey Classification

| Stage | Applicable |
|---------|------------|
| Before Diagnosis | |
| During Diagnosis | ✓ |
| Treatment Decision | ✓ |
| Active Treatment | ✓ |
| Follow-up | ✓ |
| Survivorship | |
| Palliative Care | |

**Reason:**

Patients frequently receive copies of pathology reports through patient portals before speaking with their doctors. This package teaches patients how to approach these reports safely without attempting self-diagnosis.

---

# Intended Runtime Usage

## Primary Runtime Role

- Foundational pathology report navigation

---

## Secondary Runtime Role

- Cancer diagnosis education
- Health literacy support
- Patient counseling
- Shared decision-making support
- Knowledge graph integration

---

## Typical Trigger Questions

- How do I read my pathology report?
- Which part of the pathology report is most important?
- What should I look at first?
- Why is my pathology report difficult to understand?
- Should I interpret my pathology report myself?
- How should I prepare questions for my doctor?

---

## Retrieval Priority

**Very High**

**Reason:**

This package acts as the educational bridge between understanding **what a pathology report is** and learning about the individual components that will be explained in subsequent Population Packages.

---

# Knowledge Graph

## Prerequisite Population Packages

PP-0001 → PP-0086

---

## Related Population Packages

| PP | Relationship |
|----|--------------|
| PP-0086 | Pathology Report |
| PP-0088 | Understanding the Final Diagnosis Section |
| Tumor Grade | Related |
| Biomarker Testing | Related |
| Molecular Testing | Related |

---

## Recommended Next Population Package

**PP-0088**

**Understanding the Final Diagnosis Section**

---

# Clinical Scope

## Included

- Overall report structure
- Major report sections
- Reading strategy
- Appropriate patient expectations

---

## Explicitly Excluded

- Diagnostic interpretation
- Tumor grading
- Tumor staging
- Biomarker interpretation
- Molecular pathology
- Prognostic interpretation

These topics are intentionally delegated to independent Population Packages.

---

# Authoritative Sources

## Primary Sources

1. National Cancer Institute (NCI PDQ)
2. American Cancer Society (ACS)

---

## Supporting Sources

- College of American Pathologists (CAP)
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

- National Cancer Institute
- American Cancer Society

### Supporting

- CAP
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

This Knowledge Passport is the official governance metadata for **PP-0087** and is fully compliant with the locked **Gold Population Package Specification v1.0**.