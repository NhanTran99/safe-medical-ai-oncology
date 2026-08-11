# Knowledge Passport

---

## Identity

| Field | Value |
|-------|-------|
| Knowledge Passport ID | KP-PP-0155 |
| Population Package ID | PP-0155 |
| Clinical Knowledge Object | CKO-PP-0155 |
| Title | Family history as a risk factor and Risk-information Tool |
| Clinical Domain | Risk & Prevention |
| Clinical Domain Code | RP |
| Population Batch | Risk & Prevention |
| Population Wave | Wave 1 |
| Version | 1.0.0 |
| Status | Approved |

---

# Knowledge Classification

| Field | Value |
|-------|-------|
| Knowledge Type | Risk and Preventive Medical Knowledge |
| Educational Category | Gastric-Cancer Risk Assessment |
| Educational Level | Introductory |
| Clinical Complexity | Basic to Intermediate |
| Intended Audience | General public, patients with gastric cancer, patients with a family history of gastric cancer, caregivers |
| Reading Level | Plain Language |
| Knowledge Granularity | Atomic (Single Educational Question) |
| Knowledge Scope | Family history as a risk factor and risk-information tool |

---

# Patient Journey Classification

| Stage | Applicable |
|---------|------------|
| Before Diagnosis | ✓ |
| During Diagnosis | ✓ |
| Treatment Decision | |
| Active Treatment | |
| Follow-up | |
| Survivorship | |
| Palliative Care | |

**Reason:**

Family history is primarily used to understand risk before or around clinical evaluation and to determine whether a person may benefit from more detailed hereditary-risk assessment. It is not itself a treatment or surveillance package.

---

# Intended Runtime Usage

## Primary Runtime Role

- Explain why family history matters in gastric-cancer risk assessment.

## Secondary Runtime Role

- Risk-information support.
- Patient education.
- Family-history documentation support.
- Hereditary-risk awareness.
- Shared decision-making support.
- Knowledge graph integration.

## Typical Trigger Questions

- Does stomach cancer run in families?
- Does having a parent with stomach cancer increase my risk?
- Which relatives count as family history?
- Does my father's side of the family matter?
- Why does the age when my relative got cancer matter?
- Does several relatives with stomach cancer mean I have a genetic syndrome?
- Why does my doctor ask about other cancers in my family?
- How accurate does my family history need to be?
- What should I do if several relatives have had gastric cancer?

---

# Retrieval Priority

**High**

**Reason:**

Family history is a common, clinically meaningful gastric-cancer risk factor and an important entry point into hereditary-risk assessment. The package also serves as a clean bridge between general gastric-cancer risk-factor education and the specialized hereditary-gastric-cancer packages.

---

# Knowledge Graph

## Prerequisite Population Packages

- PP-0011 — Risk Factors
- PP-0015 — Hereditary Gastric Cancer

## Related Population Packages

| PP | Relationship |
|----|--------------|
| PP-0012 | Helicobacter pylori |
| PP-0152 | HDGC Genetic Testing Criteria |
| PP-0153 | HDGC-like Families |
| PP-0154 | Hereditary Gastric Cancer Risk Assessment |
| PP-0156 | Genetic Counseling for Hereditary Gastric Cancer |
| PP-0157 | Cascade Testing in Hereditary Gastric Cancer |
| PP-0170 | Gastric Cancer Screening in High-Risk Individuals |

## Recommended Next Population Package

**PP-0156 — Genetic Counseling for Hereditary Gastric Cancer**

---

# Clinical Scope

## Included

- Family history as a gastric-cancer risk factor.
- Family-history structure and clinically relevant features.
- Degree of biological relatedness.
- Number of affected relatives.
- Generational pattern.
- Maternal and paternal lineage.
- Age at diagnosis.
- Cancer site and histology.
- Other relevant cancers and gastrointestinal polyps.
- Family-history accuracy and verification.
- Familial risk versus hereditary syndrome.
- Family history as a risk-information tool.
- High-level transition to further risk assessment.

## Explicitly Excluded

- Formal hereditary-risk assessment algorithms.
- Exact HDGC testing criteria.
- CDH1/CTNNA1-specific interpretation.
- Genetic testing methodology.
- Genetic counseling.
- Cascade testing.
- HDGC-like management.
- Risk-reducing surgery.
- Endoscopic surveillance.
- Screening schedules.
- H. pylori testing or eradication.
- Individualized numerical risk calculation.
- Treatment recommendations.

---

# Authoritative Sources

## Primary Sources

1. National Cancer Institute — *Causes of Stomach Cancer*
2. National Cancer Institute — *Genetics of Gastric Cancer (PDQ®)*
3. National Cancer Institute — *Cancer Genetics Risk Assessment and Counseling (PDQ®)*
4. American Cancer Society — *Stomach Cancer*

## Supporting Sources

- National Comprehensive Cancer Network — Gastric Cancer Guidelines / genetic-risk principles where relevant and available in the project source set.
- International hereditary gastric-cancer guidance as represented in the NCI gastric-genetics and HDGC PDQ materials.

---

# Evidence Classification

## Evidence Model

**Authoritative Educational Synthesis**

## Evidence Hierarchy

### Level I

- NCI PDQ / NCI patient-facing gastric-cancer risk information.
- American Cancer Society patient-facing gastric-cancer risk information.

### Supporting

- NCCN.
- International hereditary gastric-cancer guidance represented in NCI PDQ materials.

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
|-------|-------|
| Current Version | 1.0.0 |
| Major Version | 1 |
| Minor Version | 0 |
| Patch Version | 0 |

---

# Change History

| Version | Date | Description |
|----------|------|-------------|
| 1.0.0 | 2026-08-08 | Initial Gold Release following approved and locked PP-0155 scope |

---

# Final Status

**APPROVED**

This Knowledge Passport is the official governance metadata for:

> **PP-0155 — Family history as a risk factor and Risk-information Tool**

The package is intentionally positioned as the **family-history risk-information layer**, with formal hereditary-risk assessment, syndrome-specific testing, counseling, surveillance, and management delegated to dedicated Population Packages.
