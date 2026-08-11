# Knowledge Passport

---

# Identity

| Field | Value |
|-------|-------|
| Knowledge Passport ID | KP-PP-0027 |
| Population Package ID | PP-0027 |
| Clinical Knowledge Object | CKO-PP-0027 |
| Title | Bystander Effect in Antibody-Drug Conjugates (ADC) for Gastric Adenocarcinoma |
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
| Knowledge Scope | Therapeutic Mechanism Concept |

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

Understanding the bystander effect helps patients appreciate one of the important concepts underlying modern antibody-drug conjugate (ADC) therapy and explains why different ADC medicines may not behave in exactly the same way.

---

# Intended Runtime Usage

## Primary Runtime Role

- Foundational educational response regarding the bystander effect in ADC therapy.

## Secondary Runtime Role

- Prerequisite knowledge retrieval before ADC Toxicities, Drug Release Mechanisms and Resistance Population Packages.

## Typical Trigger Questions

- What is the bystander effect?
- What does the bystander effect mean?
- Why do some ADCs affect nearby cancer cells?
- Does every ADC have a bystander effect?
- Is the bystander effect always beneficial?
- Why is the bystander effect important?
- How does the bystander effect relate to precision oncology?

## Retrieval Priority

High

**Reason**

The bystander effect is an important conceptual property of some ADCs and complements the patient's understanding of ADC platform technology.

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
- PP-0024 ADC Mechanism of Action for Gastric Adenocarcinoma
- PP-0025 Payload Mechanism in Antibody-Drug Conjugates (ADC)
- PP-0026 Linker Technology in Antibody-Drug Conjugates (ADC)

---

## Related Population Packages

| PP | Relationship |
|----|--------------|
| PP-0023 | Introduces the overall ADC platform |
| PP-0024 | Explains the general ADC mechanism |
| PP-0025 | Explains the payload involved in the bystander effect |
| PP-0026 | Explains the linker that contributes to ADC design |
| PP-0022 | T-DXd is an example of an ADC in which the bystander effect is clinically relevant |
| Future PP | ADC Toxicities |
| Future PP | Drug Release Mechanism |
| Future PP | Payload Pharmacology |
| Future PP | Resistance to ADC Therapy |
| Future PP | ADC Platform Comparison |

---

## Recommended Next Population Package

**PP-0028**

ADC Toxicities for Gastric Adenocarcinoma

---

# Clinical Scope

## Included

- Definition of the bystander effect
- Plain-language explanation
- Why the bystander effect may occur
- General clinical significance
- Potential benefits
- General limitations
- Relationship with precision oncology
- General patient expectations

---

## Explicitly Excluded

- Molecular diffusion
- Membrane permeability
- Payload chemistry
- Cleavable versus non-cleavable linker comparison
- Intracellular drug release
- Toxicity mechanisms
- Drug-specific comparisons
- Pharmacokinetics
- Resistance mechanisms
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
| 1.0.0 | 2026-08-04 | Initial Knowledge Passport for Bystander Effect in Antibody-Drug Conjugates (ADC) for Gastric Adenocarcinoma |

---

# Future Update Trigger

This Knowledge Passport should be reviewed if:

- NCCN substantially revises recommendations involving ADC therapies.
- New evidence significantly changes understanding of the bystander effect.
- JNCCN publishes major updates regarding ADC platform design.
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

This Knowledge Passport is the official governance metadata for **PP-0027 — Bystander Effect in Antibody-Drug Conjugates (ADC) for Gastric Adenocarcinoma** and conforms to the **Gold Population Package Specification v1.0**.