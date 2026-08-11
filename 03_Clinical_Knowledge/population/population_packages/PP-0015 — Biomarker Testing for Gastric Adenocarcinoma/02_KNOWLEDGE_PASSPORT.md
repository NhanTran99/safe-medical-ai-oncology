# Knowledge Passport

---

# Identity

| Field | Value |
|-------|-------|
| Knowledge Passport ID | KP-PP-0015 |
| Population Package ID | PP-0015 |
| Clinical Knowledge Object | CKO-PP-0015 |
| Title | Biomarker Testing for Gastric Adenocarcinoma |
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
| Knowledge Scope | Foundational Diagnostic & Treatment Selection Concept |

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

Biomarker testing is a foundational step in precision oncology and supports treatment selection throughout the management of gastric adenocarcinoma.

---

# Intended Runtime Usage

## Primary Runtime Role

- Foundational educational response regarding biomarker testing.

## Secondary Runtime Role

- Prerequisite knowledge retrieval before biomarker-specific testing and precision oncology Population Packages.

## Typical Trigger Questions

- What is a biomarker?
- What is biomarker testing?
- Why do I need biomarker testing?
- When is biomarker testing performed?
- Which biomarkers are commonly tested?
- How do biomarker results affect treatment?
- Does everyone have the same biomarker results?
- Can biomarker testing be repeated?

## Retrieval Priority

High

**Reason**

Biomarker testing serves as the gateway to personalized treatment decisions and links pathology with targeted therapy and immunotherapy.

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
- PP-0014 Immunotherapy for Gastric Adenocarcinoma

---

## Related Population Packages

| PP | Relationship |
|----|--------------|
| PP-0007 | Biomarker testing is commonly performed using pathology specimens |
| PP-0013 | Biomarker testing identifies patients who may benefit from targeted therapy |
| PP-0014 | Biomarker testing identifies patients who may benefit from immunotherapy |
| Future PP | HER2 Testing |
| Future PP | PD-L1 Testing |
| Future PP | MSI-H / dMMR Testing |
| Future PP | CLDN18.2 Testing |
| Future PP | Molecular Pathology |
| Future PP | Companion Diagnostics |
| Future PP | Precision Medicine |

---

## Recommended Next Population Package

**PP-0016**

HER2 Testing for Gastric Adenocarcinoma

---

# Clinical Scope

## Included

- Definition of biomarkers
- Definition of biomarker testing
- Purpose of biomarker testing
- Timing of testing
- General specimen sources
- Major biomarkers (overview only)
- Relationship between biomarkers and treatment selection
- General interpretation of positive and negative results
- Common misconceptions
- General patient expectations

---

## Explicitly Excluded

- HER2 testing methodology
- PD-L1 CPS scoring
- MSI-H testing methodology
- dMMR testing methodology
- CLDN18.2 testing methodology
- FISH / ISH
- PCR
- Next-generation sequencing
- Liquid biopsy
- Companion diagnostics
- Drug-specific treatment indications
- Detailed biomarker interpretation

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
| 1.0.0 | 2026-08-04 | Initial Knowledge Passport for Biomarker Testing for Gastric Adenocarcinoma |

---

# Future Update Trigger

This Knowledge Passport should be reviewed if:

- NCCN substantially revises biomarker testing recommendations.
- JNCCN publishes major updates affecting biomarker-guided treatment.
- New clinically validated biomarkers become standard of care.
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

This Knowledge Passport is the official governance metadata for **PP-0015 — Biomarker Testing for Gastric Adenocarcinoma** and conforms to the **Gold Population Package Specification v1.0**.