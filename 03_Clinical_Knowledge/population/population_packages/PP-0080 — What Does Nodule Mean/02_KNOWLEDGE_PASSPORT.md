# 02_KNOWLEDGE_PASSPORT.md

# Knowledge Passport

---

# Identity

| Field | Value |
|-------|-------|
| Knowledge Passport ID | KP-PP-0080 |
| Population Package ID | PP-0080 |
| Clinical Knowledge Object | CKO-PP-0080 |
| Title | What Does "Nodule" Mean? |
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
| Educational Level | Introductory |
| Clinical Complexity | Basic |
| Intended Audience | General public, patients diagnosed with gastric cancer, caregivers |
| Reading Level | Plain Language |
| Knowledge Granularity | Atomic (Single Educational Question) |
| Knowledge Scope | What Does "Nodule" Mean? |

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

The word **nodule** is frequently encountered in CT reports and is commonly misunderstood. Patients often assume that every nodule represents cancer or, conversely, that every small nodule is harmless. This Population Package addresses both misconceptions while providing foundational health literacy.

---

# Intended Runtime Usage

## Primary Runtime Role

- Foundational educational response

---

## Secondary Runtime Role

- Radiology terminology education
- Imaging report education
- Health literacy support
- Patient counseling
- Knowledge graph integration

---

## Typical Trigger Questions

- What does nodule mean?
- Does a nodule mean cancer?
- My CT report says nodule. Should I worry?
- Is every nodule dangerous?
- Can a nodule be benign?
- What happens after a nodule is found?

---

## Retrieval Priority

**Very High**

**Reason:**

"Nodule" is one of the most frequently searched imaging terms by patients. This package completes the foundational terminology sequence (lesion → mass → nodule) and prepares users for future packages comparing these related concepts.

---

# Knowledge Graph

## Prerequisite Population Packages

PP-0001 → PP-0079

---

## Related Population Packages

| PP | Relationship |
|----|--------------|
| PP-0077 | Common Terms in a CT Report |
| PP-0078 | What Does "Lesion" Mean? |
| PP-0079 | What Does "Mass" Mean? |
| PP-0081 | Difference Between Lesion, Mass and Nodule |
| Biopsy | Related |

---

## Recommended Next Population Package

**PP-0081**

**Difference Between Lesion, Mass and Nodule**

---

# Clinical Scope

## Included

- Definition of nodule
- Descriptive imaging terminology
- Possible causes
- Clinical interpretation
- Appropriate patient understanding

---

## Explicitly Excluded

- Lesion vs mass vs nodule comparison
- Organ-specific nodules
- Imaging characterization
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

This Knowledge Passport is the official governance metadata for **PP-0080** and is fully compliant with the locked **Gold Population Package Specification v1.0**.