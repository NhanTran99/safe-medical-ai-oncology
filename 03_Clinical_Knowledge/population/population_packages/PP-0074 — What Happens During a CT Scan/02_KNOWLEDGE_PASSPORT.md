# 02_KNOWLEDGE_PASSPORT.md

# Knowledge Passport

---

# Identity

| Field | Value |
|-------|-------|
| Knowledge Passport ID | KP-PP-0074 |
| Population Package ID | PP-0074 |
| Clinical Knowledge Object | CKO-PP-0074 |
| Title | What Happens During a CT Scan? |
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
| Educational Category | Imaging Procedure |
| Educational Level | Introductory |
| Clinical Complexity | Basic |
| Intended Audience | General public, patients diagnosed with gastric cancer, caregivers |
| Reading Level | Plain Language |
| Knowledge Granularity | Atomic (Single Educational Question) |
| Knowledge Scope | What Happens During a CT Scan? |

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

Many patients experience anxiety before entering the CT scanner because they do not know what will happen during the examination. This Population Package explains the patient experience step by step in simple language without introducing technical radiology concepts.

---

# Intended Runtime Usage

## Primary Runtime Role

- Foundational educational response

---

## Secondary Runtime Role

- Imaging procedure education
- Patient counseling
- Anxiety reduction
- Examination expectation setting
- Knowledge graph integration

---

## Typical Trigger Questions

- What happens during a CT scan?
- Will the CT scan hurt?
- Will I have to hold my breath?
- Why do I have to stay still?
- What happens after the pictures are taken?
- What will I experience during the scan?

---

## Retrieval Priority

**Very High**

**Reason:**

Understanding the examination process is one of the most common patient concerns immediately before CT imaging and helps reduce anxiety while improving cooperation during image acquisition.

---

# Knowledge Graph

## Prerequisite Population Packages

PP-0001 → PP-0073

---

## Related Population Packages

| PP | Relationship |
|----|--------------|
| PP-0069 | CT Scan |
| PP-0072 | Contrast Agent |
| PP-0073 | Preparing for a CT Scan |
| PP-0075 | After a CT Scan |
| Understanding Your CT Report | Future package |

---

## Recommended Next Population Package

**PP-0075**

**After a CT Scan**

---

# Clinical Scope

## Included

- Patient experience during CT
- Positioning
- Breath-holding
- Remaining still
- Communication with imaging staff
- Temporary sensations from contrast

---

## Explicitly Excluded

- CT preparation
- Contrast safety
- Radiation exposure
- CT interpretation
- CT results
- Post-procedure care

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

This Knowledge Passport is the official governance metadata for **PP-0074** and is fully compliant with the locked **Gold Population Package Specification v1.0**.