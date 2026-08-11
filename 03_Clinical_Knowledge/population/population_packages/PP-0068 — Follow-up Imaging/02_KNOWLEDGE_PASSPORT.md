# 02_KNOWLEDGE_PASSPORT.md

# Knowledge Passport

---

# Identity

| Field | Value |
|-------|-------|
| Knowledge Passport ID | KP-PP-0068 |
| Population Package ID | PP-0068 |
| Clinical Knowledge Object | CKO-PP-0068 |
| Title | Follow-up Imaging |
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
| Educational Category | Treatment Monitoring |
| Educational Level | Introductory |
| Clinical Complexity | Intermediate (Conceptual) |
| Intended Audience | General public, patients diagnosed with gastric cancer, caregivers |
| Reading Level | Plain Language |
| Knowledge Granularity | Atomic (Single Educational Question) |
| Knowledge Scope | Follow-up Imaging |

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

Patients frequently wonder why they need repeated scans even when they feel well or have already undergone previous imaging. This Population Package explains the purpose of serial imaging in treatment monitoring using patient-friendly language while avoiding technical imaging details.

---

# Intended Runtime Usage

## Primary Runtime Role

- Foundational educational response

---

## Secondary Runtime Role

- Treatment monitoring education
- Imaging education
- Response assessment support
- Patient counseling
- Knowledge graph integration

---

## Typical Trigger Questions

- Why do I need repeated scans?
- Why can't one scan tell everything?
- How do doctors compare scans?
- How often will I need imaging?
- Why do I keep having CT scans?
- How is cancer monitored during treatment?

---

## Retrieval Priority

**Very High**

**Reason:**

Follow-up imaging is a fundamental concept linking imaging studies with treatment response assessment. Patients commonly ask about repeated imaging, making this a high-frequency educational topic.

---

# Knowledge Graph

## Prerequisite Population Packages

PP-0001 → PP-0067

---

## Related Population Packages

| PP | Relationship |
|----|--------------|
| PP-0058 | RECIST |
| PP-0059 | RECIST 1.1 |
| PP-0067 | Response Assessment Algorithm |
| PP-0069 | CT Scan |
| PP-0070 | MRI |
| PP-0071 | PET/CT |

---

## Recommended Next Population Package

**PP-0069**

**CT Scan**

---

# Clinical Scope

## Included

- Definition of follow-up imaging
- Purpose of repeated imaging
- Longitudinal comparison of imaging
- Monitoring treatment response
- Individualized imaging schedules
- Integration with overall clinical assessment

---

## Explicitly Excluded

- CT technique
- MRI technique
- PET/CT technique
- Imaging protocols
- RECIST measurements
- Treatment decisions
- Radiation safety
- Prognosis

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
- RECIST 1.1 Working Group publication

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
- RECIST 1.1 Working Group publication

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

This Knowledge Passport is the official governance metadata for **PP-0068** and is fully compliant with the locked **Gold Population Package Specification v1.0**.