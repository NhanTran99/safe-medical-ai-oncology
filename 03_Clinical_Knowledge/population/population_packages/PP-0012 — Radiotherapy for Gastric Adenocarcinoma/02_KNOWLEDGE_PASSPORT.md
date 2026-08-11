# Knowledge Passport

---

# Identity

| Field | Value |
|-------|-------|
| Knowledge Passport ID | KP-PP-0012 |
| Population Package ID | PP-0012 |
| Clinical Knowledge Object | CKO-PP-0012 |
| Title | Radiotherapy for Gastric Adenocarcinoma |
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
| Educational Category | Core Oncology Patient Education |
| Educational Level | Introductory |
| Clinical Complexity | Basic to Intermediate |
| Intended Audience | Newly diagnosed patients, caregivers, general public |
| Reading Level | Plain Language |
| Knowledge Granularity | Atomic (Single Educational Question) |
| Knowledge Scope | Foundational Treatment Concept |

---

# Patient Journey Classification

| Stage | Applicable |
|---------|------------|
| Before Diagnosis | ✗ |
| During Diagnosis | ✓ |
| Treatment Decision | ✓ |
| Active Treatment | ✓ |
| Follow-up | ✓ |
| Survivorship | ✓ |
| Palliative Care | ✓ |

**Reason**

Radiotherapy is an important treatment modality used in selected patients with gastric adenocarcinoma throughout different stages of the treatment journey, particularly during multidisciplinary treatment planning, active treatment and palliative care.

---

# Intended Runtime Usage

## Primary Runtime Role

- Foundational educational response regarding radiotherapy.

## Secondary Runtime Role

- Prerequisite knowledge retrieval before radiotherapy-specific Population Packages.

## Typical Trigger Questions

- What is radiotherapy?
- Why do I need radiotherapy?
- How does radiotherapy work?
- When is radiotherapy used?
- Will I need radiotherapy after surgery?
- Can radiotherapy be combined with chemotherapy?
- What happens during radiotherapy?
- How is radiotherapy different from chemotherapy?
- What are the common side effects of radiotherapy?

## Retrieval Priority

High

**Reason**

Radiotherapy is a core treatment concept within multidisciplinary gastric cancer care and supports multiple downstream Population Packages.

---

# Knowledge Graph

## Prerequisite Population Packages

- PP-0001 What is Cancer?
- PP-0002 What is Gastric Cancer?
- PP-0003 What is Gastric Adenocarcinoma
- PP-0004 Causes and Risk Factors
- PP-0005 Symptoms
- PP-0006 Diagnosis
- PP-0007 Pathology Report
- PP-0008 Cancer Staging
- PP-0009 Treatment Overview
- PP-0010 Surgery for Gastric Adenocarcinoma
- PP-0011 Chemotherapy for Gastric Adenocarcinoma

---

## Related Population Packages

| PP | Relationship |
|----|--------------|
| PP-0010 | Surgery may be combined with radiotherapy in selected treatment strategies |
| PP-0011 | Chemotherapy may be administered concurrently with radiotherapy |
| Future PP | Chemoradiotherapy |
| Future PP | Radiotherapy Planning |
| Future PP | Radiotherapy Side Effects |
| Future PP | Targeted Therapy |
| Future PP | Immunotherapy |
| Future PP | Palliative Care |

---

## Recommended Next Population Package

**PP-0013**

Targeted Therapy for Gastric Adenocarcinoma

---

# Clinical Scope

## Included

- Definition of radiotherapy
- Purpose of radiotherapy
- General mechanism of action
- Clinical situations where radiotherapy may be used
- Combination with chemotherapy
- General treatment process
- Expected benefits
- Common side effects (overview)
- General patient expectations

---

## Explicitly Excluded

- Radiation dose
- Fractionation
- Treatment planning
- Simulation CT
- IMRT
- VMAT
- Proton therapy
- Target volume definition
- Radiation physics
- Detailed toxicity management
- Concurrent chemoradiotherapy protocols
- Re-irradiation

These topics are intentionally delegated to independent Population Packages.

---

# Authoritative Sources

## Primary Sources

1. NCCN Clinical Practice Guidelines in Oncology: Gastric Cancer
2. JNCCN Gastric Cancer Guideline Discussion

---

## Supporting Sources

- National Cancer Institute (NCI PDQ)
- American Cancer Society (ACS)
- ESMO Clinical Practice Guidelines

---

# Evidence Classification

## Evidence Model

Authoritative Educational Synthesis

---

## Evidence Hierarchy

### Level 1

- NCCN Gastric Cancer Guidelines
- JNCCN Gastric Cancer Guideline Discussion

### Level 1 (Patient Education)

- National Cancer Institute (NCI)
- American Cancer Society (ACS)

### Supporting

- ESMO Clinical Practice Guidelines

No secondary literature was required.

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
| 1.0.0 | 2026-08-04 | Initial Knowledge Passport for Radiotherapy for Gastric Adenocarcinoma |

---

# Future Update Trigger

This Knowledge Passport should be reviewed if:

- NCCN substantially revises radiotherapy recommendations for gastric cancer.
- JNCCN publishes major updates affecting radiotherapy principles.
- NCI or ACS substantially updates patient education regarding radiotherapy.
- ESMO publishes major consensus changes affecting radiotherapy.
- Population Graph architecture changes.
- Governance specification changes.
- Runtime retrieval strategy changes.

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

This Knowledge Passport is the official governance metadata for **PP-0012 — Radiotherapy for Gastric Adenocarcinoma** and conforms to the **Gold Population Package Specification v1.0**.