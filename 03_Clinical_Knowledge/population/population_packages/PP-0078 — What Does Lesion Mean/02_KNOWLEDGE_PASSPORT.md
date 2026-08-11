# 02_KNOWLEDGE_PASSPORT.md

# Knowledge Passport

---

# Identity

| Field | Value |
|-------|-------|
| Knowledge Passport ID | KP-PP-0078 |
| Population Package ID | PP-0078 |
| Clinical Knowledge Object | CKO-PP-0078 |
| Title | What Does "Lesion" Mean? |
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
| Knowledge Scope | What Does "Lesion" Mean? |

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

The term **lesion** is one of the most common and most misunderstood words encountered in CT reports. This Population Package explains its general meaning while preventing patients from equating the word with a cancer diagnosis.

---

# Intended Runtime Usage

## Primary Runtime Role

- Foundational educational response

---

## Secondary Runtime Role

- Radiology terminology education
- Health literacy support
- Imaging report interpretation support
- Patient counseling
- Knowledge graph integration

---

## Typical Trigger Questions

- What does lesion mean?
- Does lesion mean cancer?
- My CT report says lesion. Should I worry?
- Is a lesion always dangerous?
- What happens after a lesion is found?
- Can a lesion be benign?

---

## Retrieval Priority

**Very High**

**Reason:**

"Lesion" is among the most frequently searched and misunderstood radiology terms. Early clarification substantially reduces unnecessary anxiety and supports accurate patient understanding before introducing more specialized terminology.

---

# Knowledge Graph

## Prerequisite Population Packages

PP-0001 → PP-0077

---

## Related Population Packages

| PP | Relationship |
|----|--------------|
| PP-0077 | Common Terms in a CT Report |
| PP-0079 | What Does "Mass" Mean? |
| Target Lesion | Future package |
| Cancer Diagnosis | Related |
| Biopsy | Related |

---

## Recommended Next Population Package

**PP-0079**

**What Does "Mass" Mean?**

---

# Clinical Scope

## Included

- Definition of lesion
- Lesion as descriptive terminology
- Benign and malignant possibilities
- Clinical context
- Appropriate patient interpretation

---

## Explicitly Excluded

- Mass
- Nodule
- RECIST lesions
- Target lesions
- Biopsy
- Treatment decisions

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

This Knowledge Passport is the official governance metadata for **PP-0078** and is fully compliant with the locked **Gold Population Package Specification v1.0**.