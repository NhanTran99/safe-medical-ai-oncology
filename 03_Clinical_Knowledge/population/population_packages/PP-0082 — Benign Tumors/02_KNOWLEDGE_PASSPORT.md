# 02_KNOWLEDGE_PASSPORT.md

# Knowledge Passport

---

# Identity

| Field | Value |
|-------|-------|
| Knowledge Passport ID | KP-PP-0082 |
| Population Package ID | PP-0082 |
| Clinical Knowledge Object | CKO-PP-0082 |
| Title | Benign Tumors |
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
| Knowledge Scope | Benign Tumors |

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
| Palliative Care | |

**Reason:**

Patients frequently misunderstand the word **tumor**, assuming it always means cancer. This Population Package introduces the concept of benign tumors and provides the foundation for understanding malignant tumors and subsequent discussions about cancer diagnosis.

---

# Intended Runtime Usage

## Primary Runtime Role

- Foundational educational response

---

## Secondary Runtime Role

- Tumor terminology education
- Health literacy support
- Patient counseling
- Cancer education
- Knowledge graph integration

---

## Typical Trigger Questions

- What is a benign tumor?
- Is a benign tumor cancer?
- Can a benign tumor spread?
- Can a benign tumor cause symptoms?
- Does every tumor need treatment?
- How do doctors know a tumor is benign?

---

## Retrieval Priority

**Very High**

**Reason:**

Misunderstanding the distinction between benign and malignant tumors is one of the most common causes of unnecessary anxiety after imaging or pathology results. This package serves as the foundational educational node for tumor biology terminology.

---

# Knowledge Graph

## Prerequisite Population Packages

PP-0001 → PP-0081

---

## Related Population Packages

| PP | Relationship |
|----|--------------|
| PP-0079 | What Does "Mass" Mean? |
| PP-0083 | Malignant Tumors |
| PP-0084 | Benign vs Malignant Tumors |
| Biopsy | Related |
| Pathology Report | Related |

---

## Recommended Next Population Package

**PP-0083**

**Malignant Tumors**

---

# Clinical Scope

## Included

- Definition of benign tumors
- General biological behavior
- Possible symptoms
- Clinical evaluation
- Appropriate patient understanding

---

## Explicitly Excluded

- Malignant tumors
- Comparative pathology
- Biopsy interpretation
- Treatment planning
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

This Knowledge Passport is the official governance metadata for **PP-0082** and is fully compliant with the locked **Gold Population Package Specification v1.0**.