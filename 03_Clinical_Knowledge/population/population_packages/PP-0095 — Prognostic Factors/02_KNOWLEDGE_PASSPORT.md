# 02_KNOWLEDGE_PASSPORT.md

# Knowledge Passport

---

# Identity

| Field | Value |
|-------|-------|
| Knowledge Passport ID | KP-PP-0095 |
| Population Package ID | PP-0095 |
| Clinical Knowledge Object | CKO-PP-0095 |
| Title | Prognostic Factors |
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
| Educational Category | Prognosis |
| Educational Level | Introductory |
| Clinical Complexity | Basic |
| Intended Audience | General public, patients diagnosed with cancer, caregivers |
| Reading Level | Plain Language |
| Knowledge Granularity | Atomic (Single Educational Question) |
| Knowledge Scope | Prognostic Factors |

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

Patients frequently ask what influences prognosis after learning their diagnosis and stage. This Population Package provides a foundational explanation before introducing predictive factors, prognostic biomarkers, and risk models.

---

# Intended Runtime Usage

## Primary Runtime Role

- Foundational prognosis education

---

## Secondary Runtime Role

- Health literacy support
- Patient counseling
- Shared decision-making support
- Cancer education
- Knowledge graph integration

---

## Typical Trigger Questions

- What are prognostic factors?
- What affects cancer prognosis?
- Does tumor grade affect prognosis?
- Does stage determine prognosis?
- Can one test predict my future?
- What information do doctors use to estimate prognosis?

---

## Retrieval Priority

**High**

**Reason:**

Prognostic factors are among the most common concepts discussed after staging and pathology results become available. Understanding them provides the conceptual basis for later Population Packages on predictive factors, biomarkers, and personalized prognosis.

---

# Knowledge Graph

## Prerequisite Population Packages

PP-0001 → PP-0094

---

## Related Population Packages

| PP | Relationship |
|----|--------------|
| PP-0094 | Prognostic Stage |
| PP-0089 | Tumor Grade |
| PP-0090 | TNM Staging |
| PP-0096 | Predictive Factors |
| Biomarker Testing | Related |

---

## Recommended Next Population Package

**PP-0096**

**Predictive Factors**

---

# Clinical Scope

## Included

- Definition
- Clinical purpose
- Common prognostic factors
- Interpretation
- Clinical role

---

## Explicitly Excluded

- Predictive factors
- Prognostic biomarkers
- Risk scores
- Nomograms
- AI prediction models
- Treatment recommendations

These topics are intentionally delegated to independent Population Packages.

---

# Authoritative Sources

## Primary Sources

1. National Cancer Institute (NCI PDQ)
2. NCCN Clinical Practice Guidelines
3. American Cancer Society (ACS)

---

## Supporting Sources

- AJCC Cancer Staging Manual
- ESMO Clinical Practice Guidelines
- JNCCN

---

# Evidence Classification

## Evidence Model

Authoritative Educational Synthesis

---

## Evidence Hierarchy

### Level I

- NCI
- NCCN
- ACS

### Supporting

- AJCC
- ESMO
- JNCCN

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

# Final Status

**APPROVED**

This Knowledge Passport is the official governance metadata for **PP-0095** and is fully compliant with the locked **Gold Population Package Specification v1.0**.