# Knowledge Passport

---

# Identity

| Field | Value |
|-------|-------|
| Knowledge Passport ID | KP-PP-0029 |
| Population Package ID | PP-0029 |
| Clinical Knowledge Object | CKO-PP-0029 |
| Title | Interstitial Lung Disease (ILD) Associated with ADC Therapy |
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
| Educational Category | Treatment Safety |
| Educational Level | Introductory |
| Clinical Complexity | Intermediate |
| Intended Audience | Newly diagnosed patients, caregivers, general public |
| Reading Level | Plain Language |
| Knowledge Granularity | Atomic (Single Educational Question) |
| Knowledge Scope | Serious Treatment Toxicity |

---

# Patient Journey Classification

| Stage | Applicable |
|---------|------------|
| Before Diagnosis | ✗ |
| During Diagnosis | ✗ |
| Treatment Decision | ✓ |
| Active Treatment | ✓ |
| Follow-up | ✓ |
| Survivorship | ✓ |
| Palliative Care | ✓ |

**Reason**

Patients receiving certain antibody-drug conjugates should understand ILD because early recognition and prompt reporting of respiratory symptoms are essential for treatment safety.

---

# Intended Runtime Usage

## Primary Runtime Role

- Foundational educational response regarding ADC-associated interstitial lung disease (ILD).

## Secondary Runtime Role

- Safety education before and during ADC therapy.
- Prerequisite knowledge retrieval before ILD diagnosis and management Population Packages.

## Typical Trigger Questions

- What is ILD?
- Can ADCs cause lung problems?
- Why am I being monitored for breathing symptoms?
- What symptoms should I report immediately?
- Does every ADC cause ILD?
- Should I stop treatment if I develop a cough?
- Is ILD dangerous?

## Retrieval Priority

Very High

**Reason**

ILD is an uncommon but potentially serious toxicity that requires rapid recognition and immediate communication with the healthcare team.

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
- PP-0017 PD-L1 Testing for Gastric Adenocarcinoma
- PP-0018 MSI-H / dMMR Testing for Gastric Adenocarcinoma
- PP-0019 CLDN18.2 Testing for Gastric Adenocarcinoma
- PP-0020 HER2-targeted Therapy for Gastric Adenocarcinoma
- PP-0021 Trastuzumab for Gastric Adenocarcinoma
- PP-0022 Trastuzumab Deruxtecan (T-DXd) for Gastric Adenocarcinoma
- PP-0023 Antibody-Drug Conjugates (ADC)
- PP-0024 ADC Mechanism of Action
- PP-0025 Payload Mechanism
- PP-0026 Linker Technology
- PP-0027 Bystander Effect
- PP-0028 ADC Toxicities

---

## Related Population Packages

| PP | Relationship |
|----|--------------|
| PP-0028 | Introduces overall ADC safety principles |
| PP-0022 | T-DXd is an ADC for which ILD monitoring is clinically important |
| PP-0023 | Introduces the ADC platform |
| Future PP | Diagnosis of ADC-associated ILD |
| Future PP | Management of ADC-associated ILD |
| Future PP | Corticosteroid Therapy |
| Future PP | Dose Modification |
| Future PP | Drug Rechallenge After ILD |
| Future PP | Drug-specific ILD Profiles |

---

## Recommended Next Population Package

**PP-0030**

Cardiotoxicity Associated with Targeted Therapy

---

# Clinical Scope

## Included

- Definition of ILD
- Relationship between ILD and some ADC therapies
- General warning symptoms
- Importance of early recognition
- Importance of prompt reporting
- General patient safety principles
- Communication with the healthcare team

---

## Explicitly Excluded

- CTCAE grading
- HRCT interpretation
- Bronchoscopy
- Lung pathology
- ILD pathophysiology
- Incidence statistics
- Risk prediction models
- Corticosteroid treatment
- Drug rechallenge
- Drug-specific comparisons
- Clinical trial interpretation

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
| 1.0.0 | 2026-08-04 | Initial Knowledge Passport for Interstitial Lung Disease (ILD) Associated with ADC Therapy |

---

# Future Update Trigger

This Knowledge Passport should be reviewed if:

- NCCN substantially revises recommendations regarding ADC-associated ILD.
- New safety warnings or monitoring recommendations are issued.
- JNCCN publishes major updates regarding ILD management.
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

This Knowledge Passport is the official governance metadata for **PP-0029 — Interstitial Lung Disease (ILD) Associated with ADC Therapy** and conforms to the **Gold Population Package Specification v1.0**.