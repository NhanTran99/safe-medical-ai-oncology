# 02_KNOWLEDGE_PASSPORT.md

# Knowledge Passport

---

# Identity

| Field | Value |
|-------|-------|
| Knowledge Passport ID | KP-PP-0093 |
| Population Package ID | PP-0093 |
| Clinical Knowledge Object | CKO-PP-0093 |
| Title | Restaging |
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
| Educational Category | Cancer Staging |
| Educational Level | Introductory |
| Clinical Complexity | Basic |
| Intended Audience | General public, patients diagnosed with gastric cancer, caregivers |
| Reading Level | Plain Language |
| Knowledge Granularity | Atomic (Single Educational Question) |
| Knowledge Scope | Restaging |

---

# Patient Journey Classification

| Stage | Applicable |
|---------|------------|
| Before Diagnosis | |
| During Diagnosis | |
| Treatment Decision | ✓ |
| Active Treatment | ✓ |
| Follow-up | ✓ |
| Survivorship | ✓ |
| Palliative Care | ✓ |

**Reason:**

Restaging is primarily encountered after diagnosis when clinicians need updated information about disease status during treatment, after treatment, or when progression or recurrence is suspected.

---

# Intended Runtime Usage

## Primary Runtime Role

- Foundational education on cancer reassessment

---

## Secondary Runtime Role

- Treatment monitoring education
- Patient counseling
- Health literacy support
- Shared decision-making support
- Knowledge graph integration

---

## Typical Trigger Questions

- What is restaging?
- Why do I need another stage?
- Why am I having more scans?
- Does restaging mean my cancer changed?
- Is restaging the same as my original stage?
- Why is my doctor repeating tests?

---

## Retrieval Priority

**High**

**Reason:**

Patients commonly encounter restaging during ongoing cancer care and often misunderstand it as a correction of the original stage rather than a reassessment using updated clinical information.

---

# Knowledge Graph

## Prerequisite Population Packages

PP-0001 → PP-0092

---

## Related Population Packages

| PP | Relationship |
|----|--------------|
| PP-0090 | TNM Staging |
| PP-0091 | Understanding Stage I–IV |
| PP-0092 | Clinical Stage vs Pathological Stage |
| PP-0094 | RECIST |
| Follow-up Imaging | Related |

---

## Recommended Next Population Package

**PP-0094**

**RECIST (Response Evaluation Criteria)**

---

# Clinical Scope

## Included

- Definition
- Purpose
- Timing
- Investigations
- Clinical role
- Patient interpretation

---

## Explicitly Excluded

- RECIST
- ypStage
- Recurrence staging
- Surveillance protocols
- Disease-specific algorithms
- Treatment recommendations

These topics are intentionally delegated to independent Population Packages.

---

# Authoritative Sources

## Primary Sources

1. NCCN Clinical Practice Guidelines
2. National Cancer Institute (NCI PDQ)
3. American Cancer Society (ACS)

---

## Supporting Sources

- AJCC Cancer Staging Manual
- JNCCN
- ESMO Clinical Practice Guidelines

---

# Evidence Classification

## Evidence Model

Authoritative Educational Synthesis

---

## Evidence Hierarchy

### Level I

- NCCN
- National Cancer Institute
- American Cancer Society

### Supporting

- AJCC
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

This Knowledge Passport is the official governance metadata for **PP-0093** and is fully compliant with the locked **Gold Population Package Specification v1.0**.