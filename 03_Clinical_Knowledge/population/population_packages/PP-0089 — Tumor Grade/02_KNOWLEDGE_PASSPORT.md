# 02_KNOWLEDGE_PASSPORT.md

# Knowledge Passport

---

# Identity

| Field | Value |
|-------|-------|
| Knowledge Passport ID | KP-PP-0089 |
| Population Package ID | PP-0089 |
| Clinical Knowledge Object | CKO-PP-0089 |
| Title | Tumor Grade |
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
| Educational Category | Pathology |
| Educational Level | Introductory |
| Clinical Complexity | Basic |
| Intended Audience | General public, patients diagnosed with gastric cancer, caregivers |
| Reading Level | Plain Language |
| Knowledge Granularity | Atomic (Single Educational Question) |
| Knowledge Scope | Tumor Grade |

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
| Palliative Care | |

**Reason:**

Tumor grade is commonly discussed after pathology results become available. This Population Package introduces the concept before patients learn about TNM staging, prognosis, and disease-specific grading systems.

---

# Intended Runtime Usage

## Primary Runtime Role

- Foundational pathology education

---

## Secondary Runtime Role

- Cancer diagnosis education
- Pathology literacy
- Patient counseling
- Health literacy support
- Knowledge graph integration

---

## Typical Trigger Questions

- What is tumor grade?
- What does grade mean?
- Is grade the same as stage?
- What does well differentiated mean?
- What does poorly differentiated mean?
- Why is tumor grade important?

---

## Retrieval Priority

**Very High**

**Reason:**

Tumor grade is one of the most commonly misunderstood pathology terms. Patients frequently confuse grade with stage, making this package a high-priority educational node within the pathology knowledge graph.

---

# Knowledge Graph

## Prerequisite Population Packages

PP-0001 → PP-0088

---

## Related Population Packages

| PP | Relationship |
|----|--------------|
| PP-0088 | Understanding the Final Diagnosis Section |
| PP-0090 | TNM Staging |
| Differentiation | Related |
| Prognosis | Related |
| Treatment Planning | Related |

---

## Recommended Next Population Package

**PP-0090**

**TNM Staging**

---

# Clinical Scope

## Included

- Definition of tumor grade
- Cellular differentiation
- Clinical significance
- Difference from stage
- Patient interpretation

---

## Explicitly Excluded

- Disease-specific grading systems
- TNM staging
- Prognosis
- Treatment algorithms
- Biomarker interpretation

These topics are intentionally delegated to independent Population Packages.

---

# Authoritative Sources

## Primary Sources

1. National Cancer Institute (NCI Dictionary of Cancer Terms)
2. National Cancer Institute (NCI PDQ)
3. American Cancer Society (ACS)

---

## Supporting Sources

- College of American Pathologists (CAP)
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

- National Cancer Institute
- American Cancer Society

### Supporting

- CAP
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

This Knowledge Passport is the official governance metadata for **PP-0089** and is fully compliant with the locked **Gold Population Package Specification v1.0**.