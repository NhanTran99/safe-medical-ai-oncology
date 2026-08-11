# 02_KNOWLEDGE_PASSPORT.md

# Knowledge Passport

---

# Identity

| Field | Value |
|-------|-------|
| Knowledge Passport ID | KP-PP-0056 |
| Population Package ID | PP-0056 |
| Clinical Knowledge Object | CKO-PP-0056 |
| Title | Oligometastatic Disease |
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
| Educational Category | Metastatic Disease – Oligometastatic Disease |
| Educational Level | Introductory |
| Clinical Complexity | Intermediate (Conceptual) |
| Intended Audience | General public, patients diagnosed with gastric cancer, caregivers |
| Reading Level | Plain Language |
| Knowledge Granularity | Atomic (Single Educational Question) |
| Knowledge Scope | Oligometastatic Disease |

---

# Patient Journey Classification

| Stage | Applicable |
|---------|------------|
| Before Diagnosis | |
| During Diagnosis | |
| Treatment Decision | ✓ |
| Active Treatment | ✓ |
| Follow-up | ✓ |
| Survivorship | |
| Palliative Care | ✓ |

**Reason:**

Patients may encounter the term **oligometastatic disease** during multidisciplinary discussions, specialist consultations or when reviewing treatment options. This Population Package introduces the concept without discussing specific eligibility criteria or treatment approaches.

---

# Intended Runtime Usage

## Primary Runtime Role

- Foundational educational response

---

## Secondary Runtime Role

- Metastatic disease education
- Medical terminology explanation
- Cancer staging support
- Patient reassurance
- Prerequisite knowledge retrieval

---

## Typical Trigger Questions

- What is oligometastatic disease?
- What does oligometastatic mean?
- Is oligometastatic disease a cancer stage?
- Does having only a few metastases mean I have oligometastatic disease?
- Who decides whether my cancer is oligometastatic?
- Why do different doctors describe oligometastatic disease differently?

---

## Retrieval Priority

**Very High**

**Reason:**

Oligometastatic disease is an increasingly recognized clinical concept in oncology but is frequently misunderstood by patients. This Population Package provides prerequisite knowledge before introducing tumor burden, local ablative therapies, RECIST or treatment strategies.

---

# Knowledge Graph

## Prerequisite Population Packages

PP-0001 → PP-0055

---

## Related Population Packages

| PP | Relationship |
|----|--------------|
| PP-0045 | Introduces the M Category |
| PP-0046 | Defines metastasis |
| PP-0055 | Multiple Organ Metastases |
| PP-0057 | Tumor Burden |
| PP-0058 | RECIST |
| Understanding Your Pathology Report | Clinical interpretation |

---

## Recommended Next Population Package

**PP-0057**

**Tumor Burden**

---

# Clinical Scope

## Included

- Definition of oligometastatic disease
- Explanation of limited metastatic spread
- Oligometastatic disease as a clinical concept
- Recognition that no universal definition exists
- Importance of comprehensive medical evaluation
- Explanation that imaging findings alone are insufficient

---

## Explicitly Excluded

- Numerical definitions (e.g., ≤3 or ≤5 metastases)
- ESTRO/EORTC consensus
- SABR/SBRT
- Metastasectomy
- Local ablative therapy
- Tumor burden
- RECIST
- Treatment
- Prognostic statistics

These topics are intentionally delegated to independent Population Packages.

---

# Authoritative Sources

## Primary Sources

1. National Cancer Institute (NCI PDQ)
   - Gastric Cancer Treatment

2. American Cancer Society (ACS)
   - Stomach Cancer

---

## Supporting Sources

- NCCN Clinical Practice Guidelines
- JNCCN Gastric Cancer Guideline Discussion
- ESMO Clinical Practice Guidelines
- International consensus documents (terminology only)

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

- NCI substantially revises educational content regarding metastatic gastric cancer.
- ACS updates patient education concerning metastatic disease.
- NCCN or ESMO revises recommendations regarding oligometastatic disease.
- International consensus statements substantially revise the conceptual definition of oligometastatic disease.
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

This Knowledge Passport is the official governance metadata for **PP-0056** and is fully compliant with the locked **Gold Population Package Specification v1.0**.