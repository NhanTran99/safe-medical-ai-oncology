# Knowledge Passport

---

# Identity

| Field | Value |
|-------|-------|
| Knowledge Passport ID | KP-PP-0028 |
| Population Package ID | PP-0028 |
| Clinical Knowledge Object | CKO-PP-0028 |
| Title | ADC Toxicities for Gastric Adenocarcinoma |
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
| Clinical Complexity | Intermediate |
| Intended Audience | Newly diagnosed patients, caregivers, general public |
| Reading Level | Plain Language |
| Knowledge Granularity | Atomic (Single Educational Question) |
| Knowledge Scope | Treatment Safety |

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

Understanding the general safety profile of antibody-drug conjugates (ADCs) prepares patients to recognize symptoms early, participate in routine monitoring and communicate effectively with their healthcare team throughout treatment.

---

# Intended Runtime Usage

## Primary Runtime Role

- Foundational educational response regarding the general toxicities associated with ADC therapy.

## Secondary Runtime Role

- Prerequisite knowledge retrieval before Population Packages covering specific ADC toxicities such as ILD, cardiotoxicity, ocular toxicity and peripheral neuropathy.

## Typical Trigger Questions

- Can ADCs cause side effects?
- Are ADCs safer than chemotherapy?
- What side effects can ADC therapy cause?
- Why do I need monitoring during ADC treatment?
- When should I contact my healthcare team?
- Should I stop treatment if I develop side effects?
- Why is early reporting important?

## Retrieval Priority

High

**Reason**

Safety education is essential before starting ADC therapy and supports informed participation throughout treatment.

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
- PP-0023 Antibody-Drug Conjugates (ADC) for Gastric Adenocarcinoma
- PP-0024 ADC Mechanism of Action
- PP-0025 Payload Mechanism
- PP-0026 Linker Technology
- PP-0027 Bystander Effect

---

## Related Population Packages

| PP | Relationship |
|----|--------------|
| PP-0023 | Introduces the ADC platform |
| PP-0024 | Explains how ADCs work |
| PP-0025 | Explains the therapeutic payload responsible for treatment effects |
| PP-0026 | Explains the structural linker component |
| PP-0027 | Explains the bystander effect |
| PP-0022 | Example of an approved ADC used in gastric adenocarcinoma |
| Future PP | Interstitial Lung Disease (ILD) |
| Future PP | Cardiotoxicity |
| Future PP | Ocular Toxicity |
| Future PP | Peripheral Neuropathy |
| Future PP | Dose Modification |
| Future PP | Supportive Care During ADC Therapy |

---

## Recommended Next Population Package

**PP-0029**

Interstitial Lung Disease (ILD) Associated with ADC Therapy

---

# Clinical Scope

## Included

- General concept of ADC toxicities
- Why targeted therapy can still cause side effects
- Common categories of adverse effects
- Importance of routine monitoring
- Early symptom recognition
- Patient communication
- General safety principles

---

## Explicitly Excluded

- Drug-specific toxicity profiles
- Interstitial lung disease (ILD)
- Cardiotoxicity
- Ocular toxicity
- Peripheral neuropathy
- Hepatotoxicity
- CTCAE grading
- Dose modification algorithms
- Supportive medications
- Clinical trial safety interpretation

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
| 1.0.0 | 2026-08-04 | Initial Knowledge Passport for ADC Toxicities for Gastric Adenocarcinoma |

---

# Future Update Trigger

This Knowledge Passport should be reviewed if:

- NCCN substantially revises recommendations regarding ADC safety.
- Major new safety warnings are added for ADC therapies.
- JNCCN publishes significant updates on ADC toxicity.
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

This Knowledge Passport is the official governance metadata for **PP-0028 — ADC Toxicities for Gastric Adenocarcinoma** and conforms to the **Gold Population Package Specification v1.0**.