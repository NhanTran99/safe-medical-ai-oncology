# Knowledge Passport

---

# Identity

| Field | Value |
|-------|-------|
| Knowledge Passport ID | KP-PP-0017 |
| Population Package ID | PP-0017 |
| Clinical Knowledge Object | CKO-PP-0017 |
| Title | PD-L1 Testing for Gastric Adenocarcinoma |
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
| Knowledge Scope | Biomarker-specific Testing Concept |

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

PD-L1 testing is a core biomarker assessment supporting immunotherapy selection and precision oncology for appropriate patients with gastric adenocarcinoma.

---

# Intended Runtime Usage

## Primary Runtime Role

- Foundational educational response regarding PD-L1 testing.

## Secondary Runtime Role

- Prerequisite knowledge retrieval before immunotherapy-specific and PD-L1-specific Population Packages.

## Typical Trigger Questions

- What is PD-L1?
- What is PD-L1 testing?
- Why do I need PD-L1 testing?
- When is PD-L1 testing performed?
- What does PD-L1-positive mean?
- What does PD-L1-negative mean?
- Does PD-L1 determine whether I can receive immunotherapy?
- How do PD-L1 results affect treatment?

## Retrieval Priority

High

**Reason**

PD-L1 testing is one of the principal biomarker tests used in modern gastric cancer treatment planning and is closely linked to immunotherapy decisions.

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
- PP-0015 Biomarker Testing for Gastric Adenocarcinoma
- PP-0016 HER2 Testing for Gastric Adenocarcinoma

---

## Related Population Packages

| PP | Relationship |
|----|--------------|
| PP-0015 | PD-L1 testing is a specific biomarker test within the overall biomarker testing framework |
| PP-0014 | PD-L1 testing supports immunotherapy treatment selection |
| PP-0007 | PD-L1 testing is performed using pathology specimens |
| Future PP | PD-L1 Biology |
| Future PP | PD-L1 CPS Scoring |
| Future PP | PD-L1 IHC Testing |
| Future PP | Immune Checkpoint Inhibitors |
| Future PP | Companion Diagnostics |
| Future PP | Precision Oncology |

---

## Recommended Next Population Package

**PP-0018**

MSI-H / dMMR Testing for Gastric Adenocarcinoma

---

# Clinical Scope

## Included

- Definition of PD-L1
- Definition of PD-L1 testing
- Clinical purpose of PD-L1 testing
- Timing of testing
- General specimen sources
- General meaning of PD-L1-positive and PD-L1-negative
- Relationship between PD-L1 status and immunotherapy
- General limitations of PD-L1 testing
- General patient expectations

---

## Explicitly Excluded

- PD-L1 biology
- PD-1/PD-L1 signaling pathway
- CPS methodology
- TPS methodology
- IHC laboratory methodology
- Companion diagnostics
- Individual immune checkpoint inhibitors
- Drug dosing
- Treatment sequencing
- Immune-related adverse event management

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

# Evidence Hierarchy

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
| 1.0.0 | 2026-08-04 | Initial Knowledge Passport for PD-L1 Testing for Gastric Adenocarcinoma |

---

# Future Update Trigger

This Knowledge Passport should be reviewed if:

- NCCN substantially revises PD-L1 testing recommendations.
- JNCCN publishes major updates regarding biomarker-guided immunotherapy.
- PD-L1 testing standards or companion diagnostics change.
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

This Knowledge Passport is the official governance metadata for **PP-0017 — PD-L1 Testing for Gastric Adenocarcinoma** and conforms to the **Gold Population Package Specification v1.0**.