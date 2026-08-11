# 02_KNOWLEDGE_PASSPORT.md

# Knowledge Passport

---

# Identity

| Field | Value |
|-------|-------|
| Knowledge Passport ID | KP-PP-0073 |
| Population Package ID | PP-0073 |
| Clinical Knowledge Object | CKO-PP-0073 |
| Title | Preparing for a CT Scan |
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
| Educational Category | Imaging Preparation |
| Educational Level | Introductory |
| Clinical Complexity | Basic |
| Intended Audience | General public, patients diagnosed with gastric cancer, caregivers |
| Reading Level | Plain Language |
| Knowledge Granularity | Atomic (Single Educational Question) |
| Knowledge Scope | Preparing for a CT Scan |

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

Patients frequently ask how they should prepare before arriving for a CT examination. This Population Package provides universal preparation principles while avoiding procedure-specific protocols that vary between institutions.

---

# Intended Runtime Usage

## Primary Runtime Role

- Foundational educational response

---

## Secondary Runtime Role

- Imaging preparation education
- Patient counseling
- Examination readiness
- Knowledge graph integration

---

## Typical Trigger Questions

- How should I prepare for a CT scan?
- Do I need to fast before CT?
- Can I take my medicines before CT?
- What should I tell the radiology department?
- Do all CT scans require the same preparation?
- What happens before a CT scan?

---

## Retrieval Priority

**Very High**

**Reason:**

Preparation questions are among the most common concerns before outpatient imaging examinations and directly influence patient readiness and examination quality.

---

# Knowledge Graph

## Prerequisite Population Packages

PP-0001 → PP-0072

---

## Related Population Packages

| PP | Relationship |
|----|--------------|
| PP-0069 | CT Scan |
| PP-0072 | Contrast Agent |
| PP-0074 | What Happens During a CT Scan |
| Contrast Allergy | Future package |
| Contrast and Kidney Function | Future package |

---

## Recommended Next Population Package

**PP-0074**

**What Happens During a CT Scan?**

---

# Clinical Scope

## Included

- General preparation principles
- Individualized preparation
- Fasting guidance
- Health information to report
- Medication guidance

---

## Explicitly Excluded

- CT procedure
- Contrast safety
- Contrast allergy
- Kidney assessment
- Radiation safety
- CT interpretation
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

This Knowledge Passport is the official governance metadata for **PP-0073** and is fully compliant with the locked **Gold Population Package Specification v1.0**.