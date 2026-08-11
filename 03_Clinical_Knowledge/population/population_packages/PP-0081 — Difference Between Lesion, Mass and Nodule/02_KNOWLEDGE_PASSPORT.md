# 02_KNOWLEDGE_PASSPORT.md

# Knowledge Passport

---

# Identity

| Field | Value |
|-------|-------|
| Knowledge Passport ID | KP-PP-0081 |
| Population Package ID | PP-0081 |
| Clinical Knowledge Object | CKO-PP-0081 |
| Title | Difference Between Lesion, Mass and Nodule |
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
| Educational Category | Radiology Terminology |
| Educational Level | Introductory Comparison |
| Clinical Complexity | Basic |
| Intended Audience | General public, patients diagnosed with gastric cancer, caregivers |
| Reading Level | Plain Language |
| Knowledge Granularity | Atomic (Single Educational Question) |
| Knowledge Scope | Difference Between Lesion, Mass and Nodule |

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

Patients frequently encounter all three terms within the same CT report and often believe they represent increasing levels of severity. This Population Package clarifies the conceptual relationship between these descriptive imaging terms and reduces misunderstanding before introducing more advanced radiology concepts.

---

# Intended Runtime Usage

## Primary Runtime Role

- Foundational comparison response

---

## Secondary Runtime Role

- Radiology terminology education
- CT report interpretation support
- Health literacy support
- Patient counseling
- Knowledge graph integration

---

## Typical Trigger Questions

- What is the difference between lesion, mass and nodule?
- Are lesion and mass the same thing?
- Is a nodule different from a mass?
- Which is more serious?
- Does a lesion mean cancer?
- Which word should I worry about most?

---

## Retrieval Priority

**Very High**

**Reason:**

This package integrates the three foundational terminology packages (PP-0078–PP-0080) into a single comparison resource, making it one of the highest-value educational nodes within the radiology terminology knowledge graph.

---

# Knowledge Graph

## Prerequisite Population Packages

PP-0001 → PP-0080

---

## Related Population Packages

| PP | Relationship |
|----|--------------|
| PP-0078 | What Does "Lesion" Mean? |
| PP-0079 | What Does "Mass" Mean? |
| PP-0080 | What Does "Nodule" Mean? |
| PP-0082 | Benign Tumors |
| Biopsy | Related |

---

## Recommended Next Population Package

**PP-0082**

**Benign Tumors**

---

# Clinical Scope

## Included

- Conceptual comparison
- General definitions
- Clinical interpretation
- Similarities and differences
- Appropriate patient understanding

---

## Explicitly Excluded

- Organ-specific definitions
- Imaging criteria
- RECIST terminology
- Biopsy
- Treatment recommendations

These topics are intentionally delegated to independent Population Packages.

---

# Authoritative Sources

## Primary Sources

1. National Cancer Institute (NCI PDQ)
2. American Cancer Society (ACS)

---

## Supporting Sources

- NCCN Clinical Practice Guidelines
- JNCCN Gastric Cancer Guideline Discussion
- ESMO Clinical Practice Guidelines
- American College of Radiology (ACR)
- Radiological Society of North America (RSNA)

---

# Evidence Classification

## Evidence Model

Authoritative Educational Synthesis

---

## Evidence Hierarchy

### Level I

- National Cancer Institute (NCI PDQ)
- American Cancer Society (ACS)

### Supporting

- NCCN
- JNCCN
- ESMO
- ACR
- RSNA

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

This Knowledge Passport is the official governance metadata for **PP-0081** and is fully compliant with the locked **Gold Population Package Specification v1.0**.