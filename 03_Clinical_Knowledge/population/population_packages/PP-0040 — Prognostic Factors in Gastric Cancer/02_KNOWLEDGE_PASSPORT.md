# 02_KNOWLEDGE_PASSPORT.md

# Knowledge Passport

---

# Identity

| Field | Value |
|-------|-------|
| Knowledge Passport ID | KP-PP-0040 |
| Population Package ID | PP-0040 |
| Clinical Knowledge Object | CKO-PP-0040 |
| Title | Prognostic Factors in Gastric Cancer |
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
| Educational Category | Prognosis & Clinical Assessment |
| Educational Level | Introductory |
| Clinical Complexity | Basic |
| Intended Audience | General public, patients diagnosed with gastric cancer, caregivers |
| Reading Level | Plain Language |
| Knowledge Granularity | Atomic (Single Educational Question) |
| Knowledge Scope | Foundational Prognostic Concepts |

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

Questions about prognosis commonly arise throughout the entire cancer journey. This Population Package provides a foundational understanding of prognostic factors while emphasizing that prognosis is based on multiple factors and should always be interpreted within the complete clinical context.

---

# Intended Runtime Usage

## Primary Runtime Role

- Foundational educational response

---

## Secondary Runtime Role

- Prognosis education
- Patient reassurance
- Clinical terminology explanation
- Shared decision-making support
- Prerequisite knowledge retrieval

---

## Typical Trigger Questions

- What is a prognostic factor?
- What affects the prognosis of gastric cancer?
- Can one test predict my future?
- Does my pathology report determine my prognosis?
- Can prognosis change over time?
- Why do doctors consider so many different factors?
- Is prognosis the same as survival?

---

## Retrieval Priority

**Very High**

**Reason:**

Understanding prognosis is one of the most common concerns among patients after diagnosis. This Population Package establishes the conceptual foundation before introducing staging, survival statistics, prognostic models and biomarker-specific prognosis.

---

# Knowledge Graph

## Prerequisite Population Packages

PP-0001 → PP-0039

---

## Related Population Packages

| PP | Relationship |
|----|--------------|
| Cancer Staging | Major prognostic factor |
| PP-0038 | Introduces Tumor Grade |
| PP-0039 | Introduces Histologic Differentiation |
| Biomarker Testing | Biomarkers may contribute to prognosis |
| Understanding Your Pathology Report | Explains pathological findings |
| Survival Statistics | Explains outcome statistics |

---

## Recommended Next Population Package

**PP-0041**

**Cancer Staging as a Prognostic Factor**

---

# Clinical Scope

## Included

- Definition of prognostic factors
- Purpose of prognostic assessment
- Major prognostic factor categories
- Cancer stage
- Pathological findings
- Biomarker results (introductory)
- Treatment response
- General health and performance status
- Prognosis as an estimate
- Dynamic nature of prognosis

---

## Explicitly Excluded

- Survival statistics
- Five-year survival rates
- Kaplan–Meier curves
- Hazard ratios
- Nomograms
- Prognostic prediction models
- AJCC Prognostic Stage
- AI prediction models
- Individual biomarker prognosis
- Personalized survival prediction

These topics are intentionally delegated to independent Population Packages.

---

# Authoritative Sources

## Primary Sources

1. National Cancer Institute (NCI PDQ)
   - Gastric Cancer Treatment

2. American Cancer Society (ACS)
   - Stomach Cancer
   - Prognosis and treatment planning

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

- NCI substantially revises guidance regarding prognostic assessment in gastric cancer.
- ACS updates patient education concerning prognosis.
- NCCN or ESMO revises prognostic terminology or risk assessment recommendations.
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

This Knowledge Passport is the official governance metadata for **PP-0040** and is fully compliant with the locked **Gold Population Package Specification v1.0**.