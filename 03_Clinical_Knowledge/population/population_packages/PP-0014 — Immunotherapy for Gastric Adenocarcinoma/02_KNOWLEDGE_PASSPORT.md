# Knowledge Passport

---

# Identity

| Field | Value |
|-------|-------|
| Knowledge Passport ID | KP-PP-0014 |
| Population Package ID | PP-0014 |
| Clinical Knowledge Object | CKO-PP-0014 |
| Title | Immunotherapy for Gastric Adenocarcinoma |
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

Immunotherapy is a precision oncology treatment used during treatment planning and active management for selected patients with gastric adenocarcinoma, particularly when appropriate biomarkers are present.

---

# Intended Runtime Usage

## Primary Runtime Role

- Foundational educational response regarding immunotherapy.

## Secondary Runtime Role

- Prerequisite knowledge retrieval before biomarker-specific and immunotherapy-specific Population Packages.

## Typical Trigger Questions

- What is immunotherapy?
- How does immunotherapy work?
- How is immunotherapy different from chemotherapy?
- Why do I need PD-L1 or MSI testing?
- Who can receive immunotherapy?
- Can immunotherapy be combined with chemotherapy?
- What are the benefits of immunotherapy?
- What side effects can immunotherapy cause?

## Retrieval Priority

High

**Reason**

Immunotherapy is a major systemic treatment modality in modern gastric cancer management and provides prerequisite knowledge for biomarker-guided precision oncology.

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
- PP-0012 Radiotherapy for Gastric Adenocarcinoma
- PP-0013 Targeted Therapy for Gastric Adenocarcinoma

---

## Related Population Packages

| PP | Relationship |
|----|--------------|
| Future PP | Biomarker Testing |
| Future PP | PD-L1 Testing |
| Future PP | MSI-H / dMMR Testing |
| Future PP | Immune Checkpoint Inhibitors |
| Future PP | Combination Immunotherapy |
| Future PP | Immune-related Adverse Events |
| Future PP | Precision Medicine |

---

## Recommended Next Population Package

**PP-0015**

Biomarker Testing for Gastric Adenocarcinoma

---

# Clinical Scope

## Included

- Definition of immunotherapy
- Role of the immune system in cancer treatment
- Difference from chemotherapy and targeted therapy
- General biomarker concepts
- Clinical situations where immunotherapy may be used
- Expected benefits
- General limitations
- Immune-related side effects (overview)
- General patient expectations

---

## Explicitly Excluded

- Individual immune checkpoint inhibitors
- PD-L1 CPS methodology
- MSI-H testing methodology
- dMMR testing
- TMB testing
- Drug dosing
- Treatment sequencing
- Combination protocols
- Immune-related adverse event management
- Corticosteroid treatment
- Resistance mechanisms

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
| 1.0.0 | 2026-08-04 | Initial Knowledge Passport for Immunotherapy for Gastric Adenocarcinoma |

---

# Future Update Trigger

This Knowledge Passport should be reviewed if:

- NCCN substantially revises immunotherapy recommendations.
- JNCCN publishes major updates affecting immunotherapy.
- New immune checkpoint inhibitors or biomarker indications become standard of care.
- NCI or ACS substantially updates patient education.
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

This Knowledge Passport is the official governance metadata for **PP-0014 — Immunotherapy for Gastric Adenocarcinoma** and conforms to the **Gold Population Package Specification v1.0**.