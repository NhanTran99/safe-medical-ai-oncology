# 02_KNOWLEDGE_PASSPORT.md

# Knowledge Passport

---

# Identity

| Field | Value |
|-------|-------|
| Knowledge Passport ID | KP-PP-0057 |
| Population Package ID | PP-0057 |
| Clinical Knowledge Object | CKO-PP-0057 |
| Title | Tumor Burden |
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
| Educational Category | Metastatic Disease – Tumor Burden |
| Educational Level | Introductory |
| Clinical Complexity | Intermediate (Conceptual) |
| Intended Audience | General public, patients diagnosed with gastric cancer, caregivers |
| Reading Level | Plain Language |
| Knowledge Granularity | Atomic (Single Educational Question) |
| Knowledge Scope | Tumor Burden |

---

# Patient Journey Classification

| Stage | Applicable |
|---------|------------|
| Before Diagnosis | |
| During Diagnosis | |
| Treatment Decision | ✓ |
| Active Treatment | ✓ |
| Follow-up | ✓ |
| Survivorship | ✓ |
| Palliative Care | ✓ |

**Reason:**

Patients frequently encounter the term **tumor burden** during oncology consultations, imaging reviews or discussions about disease monitoring. This Population Package establishes the foundational meaning of the term without introducing measurement systems or treatment-response criteria.

---

# Intended Runtime Usage

## Primary Runtime Role

- Foundational educational response

---

## Secondary Runtime Role

- Medical terminology explanation
- Metastatic disease education
- Disease monitoring education
- Patient reassurance
- Prerequisite knowledge retrieval

---

## Typical Trigger Questions

- What does tumor burden mean?
- What is tumor burden?
- Does tumor burden mean cancer stage?
- Is tumor burden measured with a blood test?
- How do doctors determine tumor burden?
- Why doesn't my report give one tumor burden number?

---

## Retrieval Priority

**Very High**

**Reason:**

Tumor burden is a commonly used oncology term that patients often misunderstand. This Population Package provides prerequisite knowledge for later Population Packages covering RECIST, imaging assessment, tumor markers, ctDNA and treatment response monitoring.

---

# Knowledge Graph

## Prerequisite Population Packages

PP-0001 → PP-0056

---

## Related Population Packages

| PP | Relationship |
|----|--------------|
| PP-0045 | Introduces the M Category |
| PP-0055 | Multiple Organ Metastases |
| PP-0056 | Oligometastatic Disease |
| PP-0058 | RECIST |
| Monitoring Metastatic Disease | Future educational expansion |

---

## Recommended Next Population Package

**PP-0058**

**RECIST**

---

# Clinical Scope

## Included

- Definition of tumor burden
- Explanation of the overall amount of cancer present in the body
- General contributors to tumor burden
- Tumor burden as a clinical concept
- Importance of comprehensive clinical evaluation
- Explanation that no universal measurement exists

---

## Explicitly Excluded

- RECIST
- Target lesion measurements
- Sum of lesion diameters
- Volumetric tumor assessment
- PET quantitative parameters
- Metabolic tumor volume
- Total lesion glycolysis
- ctDNA
- Tumor markers
- Treatment response assessment
- Treatment
- Prognostic statistics

These topics are intentionally delegated to independent Population Packages.

---

# Authoritative Sources

## Primary Sources

1. National Cancer Institute (NCI PDQ)
   - Gastric Cancer Treatment
   - Dictionary of Cancer Terms (when applicable)

2. American Cancer Society (ACS)
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

- NCI substantially revises educational content regarding tumor burden.
- ACS updates patient education concerning advanced gastric cancer.
- NCCN or ESMO revises terminology related to disease burden assessment.
- International recommendations substantially change concepts used to describe tumor burden.
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

This Knowledge Passport is the official governance metadata for **PP-0057** and is fully compliant with the locked **Gold Population Package Specification v1.0**.