# 02_KNOWLEDGE_PASSPORT.md

# Knowledge Passport

---

# Identity

| Field | Value |
|-------|-------|
| Knowledge Passport ID | KP-PP-0043 |
| Population Package ID | PP-0043 |
| Clinical Knowledge Object | CKO-PP-0043 |
| Title | T Category (Primary Tumor) |
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
| Educational Category | TNM Staging – Primary Tumor |
| Educational Level | Introductory |
| Clinical Complexity | Basic |
| Intended Audience | General public, patients diagnosed with gastric cancer, caregivers |
| Reading Level | Plain Language |
| Knowledge Granularity | Atomic (Single Educational Question) |
| Knowledge Scope | T Category (Primary Tumor) |

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

The T category is one of the first staging terms patients encounter after learning about the TNM staging system. This Population Package provides a conceptual understanding of the T category before introducing the detailed AJCC T classifications.

---

# Intended Runtime Usage

## Primary Runtime Role

- Foundational educational response

---

## Secondary Runtime Role

- TNM staging education
- Medical terminology explanation
- Patient reassurance
- Pathology education
- Prerequisite knowledge retrieval

---

## Typical Trigger Questions

- What does the T in TNM mean?
- What is the T category?
- Does T describe tumor size?
- Why is the T category important?
- Does a higher T category always mean a worse prognosis?
- Is T the same as cancer stage?
- How do doctors determine the T category?

---

## Retrieval Priority

**Very High**

**Reason:**

The T category is one of the three core components of the TNM staging system and forms the basis for understanding subsequent Population Packages on individual T classifications and stage grouping.

---

# Knowledge Graph

## Prerequisite Population Packages

PP-0001 → PP-0042

---

## Related Population Packages

| PP | Relationship |
|----|--------------|
| PP-0041 | Introduces stage as a prognostic factor |
| PP-0042 | Introduces the TNM staging system |
| PP-0044 | Explains the N Category |
| PP-0045 | Explains the M Category |
| Anatomy of the Stomach Wall | Explains anatomical layers relevant to T category |
| AJCC Stage Groups | Combines T, N and M into overall stage |

---

## Recommended Next Population Package

**PP-0044**

**N Category (Regional Lymph Nodes)**

---

# Clinical Scope

## Included

- Definition of the T category
- Meaning of Primary Tumor
- Purpose of the T category
- Depth of tumor invasion
- Relationship between T category and disease extent
- Relationship to TNM staging
- Role in treatment planning
- Role in prognostic assessment
- Importance of combining T with N and M

---

## Explicitly Excluded

- Tis
- T1
- T2
- T3
- T4a
- T4b
- Detailed stomach wall anatomy
- AJCC Stage Groups
- Clinical stage
- Pathological stage
- Restaging
- Stage-specific survival statistics
- Treatment recommendations by T category

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

- NCI substantially revises guidance regarding gastric cancer T classification.
- ACS updates patient education concerning TNM staging.
- NCCN or ESMO revises terminology related to primary tumor staging.
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

This Knowledge Passport is the official governance metadata for **PP-0043** and is fully compliant with the locked **Gold Population Package Specification v1.0**.