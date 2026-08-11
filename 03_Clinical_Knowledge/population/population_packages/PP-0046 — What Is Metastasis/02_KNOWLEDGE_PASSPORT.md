# 02_KNOWLEDGE_PASSPORT.md

# Knowledge Passport

---

# Identity

| Field | Value |
|-------|-------|
| Knowledge Passport ID | KP-PP-0046 |
| Population Package ID | PP-0046 |
| Clinical Knowledge Object | CKO-PP-0046 |
| Title | What Is Metastasis? |
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
| Educational Category | Cancer Biology – Metastasis |
| Educational Level | Introductory |
| Clinical Complexity | Basic |
| Intended Audience | General public, patients diagnosed with gastric cancer, caregivers |
| Reading Level | Plain Language |
| Knowledge Granularity | Atomic (Single Educational Question) |
| Knowledge Scope | Definition of Metastasis |

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

The concept of metastasis is fundamental to understanding cancer staging, prognosis and treatment discussions. Patients frequently encounter the word "metastasis" shortly after diagnosis or staging investigations. This Population Package establishes the conceptual foundation before introducing M classifications or organ-specific metastatic disease.

---

# Intended Runtime Usage

## Primary Runtime Role

- Foundational educational response

---

## Secondary Runtime Role

- Cancer terminology explanation
- Metastatic disease education
- TNM prerequisite retrieval
- Patient reassurance
- Educational concept clarification

---

## Typical Trigger Questions

- What is metastasis?
- What does metastatic cancer mean?
- Has my cancer spread?
- Is metastasis the same as Stage IV cancer?
- Is metastasis the same as the M category?
- Does metastasis mean a new cancer?
- What is the difference between a primary tumor and metastatic cancer?

---

## Retrieval Priority

**Very High**

**Reason:**

Metastasis is one of the most frequently encountered concepts in oncology and serves as prerequisite knowledge for understanding M Category, Stage IV disease, metastatic sites and treatment planning.

---

# Knowledge Graph

## Prerequisite Population Packages

PP-0001 → PP-0045

---

## Related Population Packages

| PP | Relationship |
|----|--------------|
| PP-0042 | Introduces the TNM staging system |
| PP-0045 | Explains the M Category |
| PP-0047 | Explains how gastric cancer spreads |
| Understanding Your Pathology Report | Explains diagnostic terminology |
| AJCC Stage Groups | Integrates metastatic status into overall staging |

---

## Recommended Next Population Package

**PP-0047**

**How Does Gastric Cancer Spread?**

---

# Clinical Scope

## Included

- Definition of metastasis
- Definition of primary tumor
- Difference between primary and metastatic tumors
- Difference between metastasis and the M category
- General explanation of cancer spread
- Relationship between metastasis and cancer staging
- Importance of medical evaluation before diagnosing metastasis

---

## Explicitly Excluded

- M0
- M1
- Peritoneal metastasis
- Liver metastasis
- Lung metastasis
- Bone metastasis
- Brain metastasis
- Mechanisms of metastasis
- Routes of tumor spread
- Imaging investigations
- AJCC Stage Groups
- Stage-specific prognosis
- Treatment recommendations for metastatic disease

These topics are intentionally delegated to independent Population Packages.

---

# Authoritative Sources

## Primary Sources

1. National Cancer Institute (NCI PDQ)
   - Gastric Cancer Treatment
   - NCI Dictionary of Cancer Terms (Metastasis)

2. American Cancer Society (ACS)
   - Understanding Metastatic Cancer
   - Stomach Cancer

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

- National Cancer Institute (NCI PDQ)

### Level I

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
| 1.0.0 | 2026-08-05 | Initial Gold Release Knowledge Passport |

---

# Future Update Trigger

This Knowledge Passport should be reviewed if:

- NCI substantially revises the educational definition of metastasis.
- ACS updates patient education regarding metastatic cancer.
- NCCN or ESMO revises terminology related to metastatic disease.
- AJCC introduces major conceptual changes affecting metastatic classification.
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

This Knowledge Passport is the official governance metadata for **PP-0046** and is fully compliant with the locked **Gold Population Package Specification v1.0**.