# 02_KNOWLEDGE_PASSPORT.md

# Knowledge Passport

---

# Identity

| Field | Value |
|-------|-------|
| Knowledge Passport ID | KP-PP-0044 |
| Population Package ID | PP-0044 |
| Clinical Knowledge Object | CKO-PP-0044 |
| Title | N Category (Regional Lymph Nodes) |
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
| Educational Category | TNM Staging – Regional Lymph Nodes |
| Educational Level | Introductory |
| Clinical Complexity | Basic |
| Intended Audience | General public, patients diagnosed with gastric cancer, caregivers |
| Reading Level | Plain Language |
| Knowledge Granularity | Atomic (Single Educational Question) |
| Knowledge Scope | N Category (Regional Lymph Nodes) |

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

The N category is one of the three fundamental components of the TNM staging system. Patients commonly encounter this terminology after diagnosis, making it essential to establish a clear conceptual understanding before introducing detailed N classifications or lymph node mapping.

---

# Intended Runtime Usage

## Primary Runtime Role

- Foundational educational response

---

## Secondary Runtime Role

- TNM staging education
- Medical terminology explanation
- Lymph node education
- Patient reassurance
- Prerequisite knowledge retrieval

---

## Typical Trigger Questions

- What does the N in TNM mean?
- What is the N category?
- What are regional lymph nodes?
- Why are lymph nodes important in stomach cancer?
- Does a higher N category always mean a worse prognosis?
- Is the N category the same as metastasis?
- How do doctors determine the N category?

---

## Retrieval Priority

**Very High**

**Reason:**

The N category is a core component of TNM staging and serves as the prerequisite for understanding detailed lymph node classifications, lymph node surgery and AJCC stage grouping.

---

# Knowledge Graph

## Prerequisite Population Packages

PP-0001 → PP-0043

---

## Related Population Packages

| PP | Relationship |
|----|--------------|
| PP-0041 | Introduces stage as a prognostic factor |
| PP-0042 | Introduces the TNM staging system |
| PP-0043 | Explains the T Category |
| PP-0045 | Explains the M Category |
| What Are Lymph Nodes? | Explains lymphatic system basics |
| AJCC Stage Groups | Integrates T, N and M into overall stage |

---

## Recommended Next Population Package

**PP-0045**

**M Category (Distant Metastasis)**

---

# Clinical Scope

## Included

- Definition of the N category
- Meaning of regional lymph nodes
- Basic explanation of lymph nodes
- Purpose of the N category
- Relationship between N category and regional lymph node involvement
- Relationship to TNM staging
- Role in treatment planning
- Role in prognostic assessment
- Importance of combining N with T and M

---

## Explicitly Excluded

- N0
- N1
- N2
- N3
- Number of positive lymph nodes
- Regional lymph node stations
- Sentinel lymph node
- D1 lymphadenectomy
- D2 lymphadenectomy
- AJCC Stage Groups
- Stage-specific survival statistics
- Treatment recommendations according to N category

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

- NCI substantially revises guidance regarding regional lymph node staging.
- ACS updates patient education concerning lymph node involvement.
- NCCN or ESMO revises terminology related to N classification.
- AJCC introduces major conceptual changes affecting lymph node staging.
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

This Knowledge Passport is the official governance metadata for **PP-0044** and is fully compliant with the locked **Gold Population Package Specification v1.0**.