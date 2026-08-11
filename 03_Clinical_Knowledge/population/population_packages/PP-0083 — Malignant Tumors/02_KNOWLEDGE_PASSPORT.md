# 02_KNOWLEDGE_PASSPORT.md

# Knowledge Passport

---

# Identity

| Field | Value |
|-------|-------|
| Knowledge Passport ID | KP-PP-0083 |
| Population Package ID | PP-0083 |
| Clinical Knowledge Object | CKO-PP-0083 |
| Title | Malignant Tumors |
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
| Educational Category | Tumor Biology |
| Educational Level | Introductory |
| Clinical Complexity | Basic |
| Intended Audience | General public, patients diagnosed with gastric cancer, caregivers |
| Reading Level | Plain Language |
| Knowledge Granularity | Atomic (Single Educational Question) |
| Knowledge Scope | Malignant Tumors |

---

# Patient Journey Classification

| Stage | Applicable |
|---------|------------|
| Before Diagnosis | ✓ |
| During Diagnosis | ✓ |
| Treatment Decision | ✓ |
| Active Treatment | ✓ |
| Follow-up | ✓ |
| Survivorship | ✓ |
| Palliative Care | ✓ |

**Reason:**

Patients often associate the word **malignant** with hopelessness or immediate death. This Population Package provides a balanced, evidence-based explanation that malignant tumors are cancers while emphasizing that treatment options and outcomes vary considerably among individuals.

---

# Intended Runtime Usage

## Primary Runtime Role

- Foundational educational response

---

## Secondary Runtime Role

- Cancer terminology education
- Health literacy support
- Patient counseling
- Oncology education
- Knowledge graph integration

---

## Typical Trigger Questions

- What is a malignant tumor?
- Is a malignant tumor cancer?
- Does every malignant tumor spread?
- Can malignant tumors be treated?
- What does malignant mean?
- Is malignant always fatal?

---

## Retrieval Priority

**Very High**

**Reason:**

Understanding the meaning of "malignant" is essential for virtually every patient diagnosed with cancer. This package establishes the foundation for later Population Packages covering metastasis, staging, pathology, and treatment.

---

# Knowledge Graph

## Prerequisite Population Packages

PP-0001 → PP-0082

---

## Related Population Packages

| PP | Relationship |
|----|--------------|
| PP-0082 | Benign Tumors |
| PP-0084 | Benign vs Malignant Tumors |
| Metastasis | Related |
| Cancer Diagnosis | Related |
| Pathology Report | Related |

---

## Recommended Next Population Package

**PP-0084**

**Benign vs Malignant Tumors**

---

# Clinical Scope

## Included

- Definition of malignant tumors
- General biological behavior
- High-level explanation of invasion and spread
- Treatment concept
- Appropriate patient understanding

---

## Explicitly Excluded

- Benign tumors
- Comparative pathology
- TNM staging
- Tumor grading
- Treatment strategies
- Prognosis

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

This Knowledge Passport is the official governance metadata for **PP-0083** and is fully compliant with the locked **Gold Population Package Specification v1.0**.