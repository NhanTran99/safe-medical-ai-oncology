# 02_KNOWLEDGE_PASSPORT.md

# Knowledge Passport

---

# Identity

| Field | Value |
|-------|-------|
| Knowledge Passport ID | KP-PP-0086 |
| Population Package ID | PP-0086 |
| Clinical Knowledge Object | CKO-PP-0086 |
| Title | Pathology Report |
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
| Educational Level | Introductory |
| Clinical Complexity | Basic |
| Intended Audience | General public, patients diagnosed with gastric cancer, caregivers |
| Reading Level | Plain Language |
| Knowledge Granularity | Atomic (Single Educational Question) |
| Knowledge Scope | Pathology Report |

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

The pathology report is one of the most important documents patients receive during cancer diagnosis. This Population Package explains its purpose before introducing report interpretation, grading, staging, biomarkers, and molecular pathology.

---

# Intended Runtime Usage

## Primary Runtime Role

- Foundational educational response

---

## Secondary Runtime Role

- Cancer diagnosis education
- Pathology education
- Patient counseling
- Health literacy support
- Knowledge graph integration

---

## Typical Trigger Questions

- What is a pathology report?
- Why is my pathology report important?
- Who writes a pathology report?
- Does my pathology report confirm cancer?
- Should I read my pathology report?
- Why is my pathology report difficult to understand?

---

## Retrieval Priority

**Very High**

**Reason:**

The pathology report is a cornerstone of cancer diagnosis. This package establishes the conceptual foundation required before patients learn how to interpret pathology findings and understand biomarker or molecular testing.

---

# Knowledge Graph

## Prerequisite Population Packages

PP-0001 → PP-0085

---

## Related Population Packages

| PP | Relationship |
|----|--------------|
| PP-0085 | Biopsy |
| PP-0087 | How to Read a Pathology Report |
| Biomarker Testing | Related |
| Molecular Testing | Related |
| Tumor Grade | Related |

---

## Recommended Next Population Package

**PP-0087**

**How to Read a Pathology Report**

---

# Clinical Scope

## Included

- Definition
- Purpose
- Author
- Diagnostic role
- Clinical interpretation

---

## Explicitly Excluded

- Report interpretation
- Tumor grading
- Tumor staging
- Biomarker testing
- Molecular pathology
- CAP synoptic reporting

These topics are intentionally delegated to independent Population Packages.

---

# Authoritative Sources

## Primary Sources

1. National Cancer Institute (NCI Dictionary of Cancer Terms)
2. National Cancer Institute (NCI PDQ)
3. American Cancer Society (ACS)

---

## Supporting Sources

- NCCN Clinical Practice Guidelines
- College of American Pathologists (CAP)
- JNCCN Gastric Cancer Guideline Discussion
- ESMO Clinical Practice Guidelines

---

# Evidence Classification

## Evidence Model

Authoritative Educational Synthesis

---

## Evidence Hierarchy

### Level I

- National Cancer Institute (NCI)
- American Cancer Society (ACS)

### Supporting

- NCCN
- CAP
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

This Knowledge Passport is the official governance metadata for **PP-0086** and is fully compliant with the locked **Gold Population Package Specification v1.0**.