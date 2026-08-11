# 02_KNOWLEDGE_PASSPORT.md

# Knowledge Passport

---

# Identity

| Field | Value |
|-------|-------|
| Knowledge Passport ID | KP-PP-0090 |
| Population Package ID | PP-0090 |
| Clinical Knowledge Object | CKO-PP-0090 |
| Title | TNM Staging |
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
| Knowledge Scope | TNM Staging |

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

TNM staging is a fundamental concept introduced soon after diagnosis and remains relevant throughout treatment, follow-up, and discussions about prognosis. This package establishes the core staging framework before introducing Stage I–IV and disease-specific staging systems.

---

# Intended Runtime Usage

## Primary Runtime Role

- Foundational cancer staging education

---

## Secondary Runtime Role

- Cancer diagnosis education
- Health literacy support
- Patient counseling
- Shared decision-making support
- Knowledge graph integration

---

## Typical Trigger Questions

- What is TNM staging?
- What does T mean?
- What does N mean?
- What does M mean?
- What is the difference between grade and stage?
- Why is TNM staging important?

---

## Retrieval Priority

**Very High**

**Reason:**

TNM staging is one of the core concepts in oncology and provides the foundation for understanding disease extent, treatment planning, prognosis discussions, and future education about Stage I–IV.

---

# Knowledge Graph

## Prerequisite Population Packages

PP-0001 → PP-0089

---

## Related Population Packages

| PP | Relationship |
|----|--------------|
| PP-0089 | Tumor Grade |
| PP-0091 | Understanding Stage I–IV |
| Clinical Stage | Related |
| Pathological Stage | Related |
| Prognosis | Related |

---

## Recommended Next Population Package

**PP-0091**

**Understanding Stage I–IV**

---

# Clinical Scope

## Included

- Definition of TNM staging
- T, N and M concepts
- Overall stage concept
- Difference between grade and stage
- Clinical purpose

---

## Explicitly Excluded

- Stage I–IV
- Detailed TNM categories
- Clinical vs pathological staging
- Disease-specific staging systems
- Prognosis
- Treatment algorithms

These topics are intentionally delegated to independent Population Packages.

---

# Authoritative Sources

## Primary Sources

1. AJCC Cancer Staging Manual
2. UICC TNM Classification of Malignant Tumours
3. National Cancer Institute (NCI Dictionary of Cancer Terms)
4. National Cancer Institute (NCI PDQ)
5. American Cancer Society (ACS)

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

### Level I

- AJCC
- UICC
- National Cancer Institute
- American Cancer Society

### Supporting

- NCCN
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

This Knowledge Passport is the official governance metadata for **PP-0090** and is fully compliant with the locked **Gold Population Package Specification v1.0**.