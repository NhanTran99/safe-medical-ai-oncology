# 02_KNOWLEDGE_PASSPORT.md

# Knowledge Passport

---

# Identity

| Field | Value |
|-------|-------|
| Knowledge Passport ID | KP-PP-0091 |
| Population Package ID | PP-0091 |
| Clinical Knowledge Object | CKO-PP-0091 |
| Title | Understanding Stage I–IV |
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
| Knowledge Scope | Understanding Stage I–IV |

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

Patients commonly ask what Stage I, II, III or IV means immediately after diagnosis. This Population Package provides a safe, general explanation before introducing cancer-specific staging systems or prognosis.

---

# Intended Runtime Usage

## Primary Runtime Role

- Foundational cancer stage education

---

## Secondary Runtime Role

- Cancer diagnosis education
- Patient counseling
- Health literacy support
- Shared decision-making support
- Knowledge graph integration

---

## Typical Trigger Questions

- What does Stage III mean?
- What is Stage IV cancer?
- What is the difference between Stage I and Stage II?
- Is Stage IV always the worst?
- Is stage the same for every cancer?
- Does stage determine treatment?

---

## Retrieval Priority

**Very High**

**Reason:**

Stage I–IV is one of the most frequently encountered concepts in oncology. Patients often receive a stage designation before understanding TNM details, making this package a high-priority educational resource.

---

# Knowledge Graph

## Prerequisite Population Packages

PP-0001 → PP-0090

---

## Related Population Packages

| PP | Relationship |
|----|--------------|
| PP-0090 | TNM Staging |
| PP-0092 | Clinical Stage vs Pathological Stage |
| Tumor Grade | Related |
| Prognosis | Related |
| Treatment Planning | Related |

---

## Recommended Next Population Package

**PP-0092**

**Clinical Stage vs Pathological Stage**

---

# Clinical Scope

## Included

- Stage I–IV overview
- General meaning of stage groups
- Relationship with TNM
- Clinical role
- Appropriate interpretation

---

## Explicitly Excluded

- Stage IA/IB
- Clinical stage
- Pathological stage
- Disease-specific staging systems
- Prognosis
- Treatment algorithms

These topics are intentionally delegated to independent Population Packages.

---

# Authoritative Sources

## Primary Sources

1. AJCC Cancer Staging Manual
2. UICC TNM Classification of Malignant Tumours
3. National Cancer Institute (NCI PDQ)
4. American Cancer Society (ACS)

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

This Knowledge Passport is the official governance metadata for **PP-0091** and is fully compliant with the locked **Gold Population Package Specification v1.0**.