# 02_KNOWLEDGE_PASSPORT.md

# Knowledge Passport

---

# Identity

| Field | Value |
|-------|-------|
| Knowledge Passport ID | KP-PP-0071 |
| Population Package ID | PP-0071 |
| Clinical Knowledge Object | CKO-PP-0071 |
| Title | PET/CT (Positron Emission Tomography / Computed Tomography) |
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
| Knowledge Scope | PET/CT (Positron Emission Tomography / Computed Tomography) |

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

Patients frequently hear about PET/CT but are often uncertain how it differs from CT or MRI and whether everyone with cancer needs this examination. This Population Package provides a foundational explanation while avoiding technical nuclear medicine concepts.

---

# Intended Runtime Usage

## Primary Runtime Role

- Foundational educational response

---

## Secondary Runtime Role

- Imaging education
- Nuclear medicine terminology explanation
- Treatment monitoring education
- Patient counseling
- Knowledge graph integration

---

## Typical Trigger Questions

- What is a PET/CT scan?
- Why do I need PET/CT?
- What does PET/CT show?
- Why can't CT alone answer this question?
- Does PET/CT use radioactive material?
- Does every cancer patient need PET/CT?

---

## Retrieval Priority

**Very High**

**Reason:**

PET/CT is a commonly misunderstood imaging modality in oncology. Patients frequently request a simple explanation of its purpose and when it is used.

---

# Knowledge Graph

## Prerequisite Population Packages

PP-0001 → PP-0070

---

## Related Population Packages

| PP | Relationship |
|----|--------------|
| PP-0068 | Follow-up Imaging |
| PP-0069 | CT Scan |
| PP-0070 | MRI |
| PP-0072 | Contrast Agent |
| Radiotracer | Future package |
| PET/CT Safety | Future package |

---

## Recommended Next Population Package

**PP-0072**

**Contrast Agent**

---

# Clinical Scope

## Included

- Definition of PET/CT
- PET and CT concepts
- Role during cancer care
- Basic introduction to radiotracers
- Integration into comprehensive clinical assessment

---

## Explicitly Excluded

- PET physics
- FDG metabolism
- SUV
- PET preparation
- Blood glucose management
- PET interpretation
- Imaging comparison
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
- Society of Nuclear Medicine and Molecular Imaging (SNMMI)
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
- SNMMI
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

This Knowledge Passport is the official governance metadata for **PP-0071** and is fully compliant with the locked **Gold Population Package Specification v1.0**.