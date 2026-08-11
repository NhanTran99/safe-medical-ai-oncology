# 02_KNOWLEDGE_PASSPORT.md

# Knowledge Passport

---

# Identity

| Field | Value |
|-------|-------|
| Knowledge Passport ID | KP-PP-0042 |
| Population Package ID | PP-0042 |
| Clinical Knowledge Object | CKO-PP-0042 |
| Title | TNM Staging System |
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
| Knowledge Scope | Foundational TNM Staging System |

---

# Patient Journey Classification

| Stage | Applicable |
|---------|------------|
| Before Diagnosis |  |
| During Diagnosis | ✓ |
| Treatment Decision | ✓ |
| Active Treatment | ✓ |
| Follow-up | ✓ |
| Survivorship | ✓ |
| Palliative Care | ✓ |

**Reason:**

The TNM staging system is introduced soon after diagnosis and is referenced throughout cancer care. This Population Package provides the conceptual foundation needed before learning the individual T, N and M categories or AJCC stage groups.

---

# Intended Runtime Usage

## Primary Runtime Role

- Foundational educational response

---

## Secondary Runtime Role

- Cancer staging education
- Medical terminology explanation
- Patient reassurance
- Prognosis education
- Prerequisite knowledge retrieval

---

## Typical Trigger Questions

- What is the TNM staging system?
- What does T mean?
- What does N mean?
- What does M mean?
- Why do doctors use TNM?
- Does TNM determine treatment?
- Is TNM the same as cancer stage?

---

## Retrieval Priority

**Very High**

**Reason:**

TNM is the universal language used to describe cancer extent and is the foundation for understanding staging, prognosis and treatment planning. It serves as the prerequisite for all subsequent Population Packages on T, N, M and AJCC stage groups.

---

# Knowledge Graph

## Prerequisite Population Packages

PP-0001 → PP-0041

---

## Related Population Packages

| PP | Relationship |
|----|--------------|
| PP-0040 | Introduces prognostic factors |
| PP-0041 | Explains stage as a prognostic factor |
| PP-0043 | Explains T (Primary Tumor) |
| PP-0044 | Explains N (Regional Lymph Nodes) |
| PP-0045 | Explains M (Distant Metastasis) |
| AJCC Stage Groups | Combines TNM categories into overall stages |

---

## Recommended Next Population Package

**PP-0043**

**T Category (Primary Tumor)**

---

# Clinical Scope

## Included

- Definition of TNM staging system
- Purpose of TNM staging
- General meaning of T
- General meaning of N
- General meaning of M
- Role of TNM in determining cancer stage
- Role in treatment planning
- Role in prognostic assessment
- Standardized international communication

---

## Explicitly Excluded

- T1–T4 categories
- N0–N3 categories
- M0–M1 categories
- AJCC Stage Groups
- Clinical stage
- Pathological stage
- Restaging
- Stage-specific survival statistics
- Stage-specific treatment recommendations
- AJCC edition differences

These topics are intentionally delegated to independent Population Packages.

---

# Authoritative Sources

## Primary Sources

1. National Cancer Institute (NCI PDQ)
   - Gastric Cancer Treatment

2. American Cancer Society (ACS)
   - Stomach Cancer
   - Cancer staging

---

## Supporting Sources

- NCCN Clinical Practice Guidelines
- JNCCN Gastric Cancer Guideline Discussion
- ESMO Clinical Practice Guidelines

---

# Evidence Classification

## Evidence Model

Authoritative Educational Synthesis

---

## Evidence Hierarchy

### Level 1

- National Cancer Institute (NCI PDQ)

### Level 1

- American Cancer Society (ACS)

### Supporting

- NCCN
- JNCCN
- ESMO

No lower-level evidence was required.

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
| 1.0.0 | 2026-08-04 | Initial Gold Release Knowledge Passport |

---

# Future Update Trigger

This Knowledge Passport should be reviewed if:

- NCI substantially revises guidance regarding TNM staging.
- ACS updates patient education concerning cancer staging.
- NCCN or ESMO revises staging terminology or recommendations.
- AJCC introduces major conceptual changes affecting patient education.
- Population Graph architecture changes.
- Governance specification changes.

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

This Knowledge Passport is the official governance metadata for **PP-0042** and is fully compliant with the locked **Gold Population Package Specification v1.0**.