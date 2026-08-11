# 02_KNOWLEDGE_PASSPORT.md

# Knowledge Passport

---

# Identity

| Field | Value |
|-------|-------|
| Knowledge Passport ID | KP-PP-0070 |
| Population Package ID | PP-0070 |
| Clinical Knowledge Object | CKO-PP-0070 |
| Title | MRI (Magnetic Resonance Imaging) |
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
| Educational Category | Cancer Imaging |
| Educational Level | Introductory |
| Clinical Complexity | Intermediate (Conceptual) |
| Intended Audience | General public, patients diagnosed with gastric cancer, caregivers |
| Reading Level | Plain Language |
| Knowledge Granularity | Atomic (Single Educational Question) |
| Knowledge Scope | MRI (Magnetic Resonance Imaging) |

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

MRI is one of the most commonly discussed imaging examinations in oncology. Many patients ask why MRI is recommended, whether it is better than CT, and whether MRI uses radiation. This Population Package provides a foundational explanation while avoiding technical imaging details.

---

# Intended Runtime Usage

## Primary Runtime Role

- Foundational educational response

---

## Secondary Runtime Role

- Imaging education
- Diagnostic terminology explanation
- Treatment monitoring education
- Patient counseling
- Knowledge graph integration

---

## Typical Trigger Questions

- What is an MRI?
- Why do I need an MRI?
- Does MRI use radiation?
- Why did my doctor order MRI instead of CT?
- Will my MRI need contrast?
- What does MRI show?

---

## Retrieval Priority

**Very High**

**Reason:**

MRI is a major imaging modality used throughout oncology. Patients frequently seek understandable explanations about why MRI is recommended and how it differs conceptually from other imaging studies.

---

# Knowledge Graph

## Prerequisite Population Packages

PP-0001 → PP-0069

---

## Related Population Packages

| PP | Relationship |
|----|--------------|
| PP-0068 | Follow-up Imaging |
| PP-0069 | CT Scan |
| PP-0071 | PET/CT |
| MRI Contrast Agent | Supporting concept |
| MRI Safety | Future package |

---

## Recommended Next Population Package

**PP-0071**

**PET/CT**

---

# Clinical Scope

## Included

- Definition of MRI
- Basic imaging principle
- Purpose in cancer care
- Monitoring during treatment
- Basic introduction to MRI contrast agents
- Integration into comprehensive clinical assessment

---

## Explicitly Excluded

- MRI physics
- MRI pulse sequences
- MRI safety
- MRI contraindications
- MRI preparation
- MRI interpretation
- Comparison with CT or PET/CT
- Treatment planning

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

This Knowledge Passport is the official governance metadata for **PP-0070** and is fully compliant with the locked **Gold Population Package Specification v1.0**.