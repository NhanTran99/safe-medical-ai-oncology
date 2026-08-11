# 02_KNOWLEDGE_PASSPORT.md

# Knowledge Passport

---

# Identity

| Field | Value |
|-------|-------|
| Knowledge Passport ID | KP-PP-0069 |
| Population Package ID | PP-0069 |
| Clinical Knowledge Object | CKO-PP-0069 |
| Title | CT Scan (Computed Tomography) |
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
| Knowledge Scope | CT Scan (Computed Tomography) |

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

CT is one of the most frequently performed imaging examinations throughout cancer care. Patients commonly ask why CT scans are needed repeatedly and what information CT provides. This Population Package delivers a foundational explanation without introducing technical radiology concepts.

---

# Intended Runtime Usage

## Primary Runtime Role

- Foundational educational response

---

## Secondary Runtime Role

- Imaging education
- Treatment monitoring education
- Diagnostic terminology explanation
- Patient counseling
- Knowledge graph integration

---

## Typical Trigger Questions

- What is a CT scan?
- Why do I need a CT scan?
- Why do doctors repeat CT scans?
- What does a CT scan show?
- Will I need contrast?
- Is CT part of cancer treatment monitoring?

---

## Retrieval Priority

**Very High**

**Reason:**

CT is among the most frequently used imaging modalities in oncology and serves as a cornerstone of diagnosis, staging and treatment monitoring. Patients routinely seek explanations about its purpose during their cancer journey.

---

# Knowledge Graph

## Prerequisite Population Packages

PP-0001 → PP-0068

---

## Related Population Packages

| PP | Relationship |
|----|--------------|
| PP-0068 | Follow-up Imaging |
| PP-0070 | MRI |
| PP-0071 | PET/CT |
| Contrast Agent | Supporting concept |
| RECIST | Response assessment |

---

## Recommended Next Population Package

**PP-0070**

**MRI**

---

# Clinical Scope

## Included

- Definition of CT
- Purpose of CT in cancer care
- Longitudinal monitoring
- Basic introduction to contrast material
- Integration into overall clinical assessment

---

## Explicitly Excluded

- CT physics
- Radiation dose
- Contrast safety
- Scan preparation
- CT interpretation
- Imaging comparison
- RECIST measurements
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

This Knowledge Passport is the official governance metadata for **PP-0069** and is fully compliant with the locked **Gold Population Package Specification v1.0**.