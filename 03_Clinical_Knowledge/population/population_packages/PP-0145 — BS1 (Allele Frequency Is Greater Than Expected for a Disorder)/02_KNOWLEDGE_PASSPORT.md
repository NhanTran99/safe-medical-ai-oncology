
# Knowledge Passport

---

# Identity

| Field | Value |
|-------|-------|
| Knowledge Passport ID | KP-PP-0145 |
| Population Package ID | PP-0145 |
| Clinical Knowledge Object | CKO-PP-0145 |
| Title | BS1 (Allele Frequency Is Greater Than Expected for a Disorder) |
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
| Educational Category | Clinical Genomics |
| Educational Level | Introductory |
| Clinical Complexity | Advanced Introductory |
| Intended Audience | General public, patients diagnosed with cancer, caregivers |
| Reading Level | Plain Language |
| Knowledge Granularity | Atomic (Single Educational Question) |
| Knowledge Scope | BS1 (Allele Frequency Is Greater Than Expected for a Disorder) |

---

# Patient Journey Classification

| Stage | Applicable |
|---------|------------|
| Before Diagnosis | |
| During Diagnosis | ✓ |
| Treatment Decision | ✓ |
| Active Treatment | ✓ |
| Follow-up | ✓ |
| Survivorship | ✓ |
| Palliative Care | ✓ |

**Reason:**

Patients undergoing genetic testing may encounter population-frequency information in variant reports. This Population Package explains how an unexpectedly high population frequency can provide strong benign evidence and why that interpretation must be specific to the disorder being evaluated.

---

# Intended Runtime Usage

## Primary Runtime Role

- Foundational education on BS1

## Secondary Runtime Role

- Population frequency education
- ACMG evidence-code education
- Benign evidence education
- Variant interpretation education
- Genetic testing counseling
- Knowledge graph integration

---

## Typical Trigger Questions

- What is BS1?
- What does allele frequency mean?
- Why can a common variant be considered benign evidence?
- Why does the disease matter when interpreting frequency?
- Is there one BS1 cutoff for every disease?
- Is BS1 the same as BA1?

---

# Retrieval Priority

**Very High**

**Reason:**

BS1 is the foundational population-frequency criterion within the Strong Benign Evidence family and establishes the conceptual basis needed before introducing disease-specific thresholds, population databases and BA1.

---

# Knowledge Graph

## Prerequisite Population Packages

PP-0001 → PP-0144

---

## Related Population Packages

| PP | Relationship |
|----|--------------|
| PP-0144 | BS Evidence Codes |
| PP-0136 | BP Evidence Codes |
| PP-0116 | ACMG Evidence Codes |
| PP-0115 | ACMG Variant Classification Framework |
| PP-0108 | Variant Classification |

---

## Future Population Packages

- BS2
- BS3
- BS4
- BA1
- Population Frequency / gnomAD
- PopMax / GrpMax / FAF
- Founder Effect
- Disease-specific BS1 Thresholds
- ACMG Benign Evidence Combination Rules

---

# Clinical Scope

## Included

- BS1 definition
- Allele frequency
- Greater-than-expected frequency
- Disease-specific interpretation
- Population context
- Relationship to benign evidence
- BS1 versus BA1

---

## Explicitly Excluded

- Numerical thresholds for individual genes/disorders
- gnomAD technical methodology
- PopMax / GrpMax / FAF implementation
- Whiffin/Ware calculator methodology
- Founder-effect calculations
- Detailed ancestry/population-stratification methodology
- BA1 implementation
- Bayesian framework
- ACMG benign evidence-combination rules
- Gene-specific ClinGen VCEP specifications
- Laboratory workflow
- Treatment recommendations

These topics are intentionally delegated to independent Population Packages.

---

# Authoritative Sources

## Primary Sources

1. ACMG
2. AMP
3. ClinGen SVI
4. ClinGen Expert Panels / VCEPs
5. CAP
6. NCI
7. NCCN
8. ASCO

## Supporting Patient-Education Sources

- ACS
- ESMO

---

# Evidence Classification

## Evidence Model

Authoritative Educational Synthesis

---

# Historical Framework

**ACMG/AMP 2015**

BS1 was defined as:

> **Allele frequency is greater than expected for disorder.**

The original framework explains that a control-population frequency greater than expected for a rare Mendelian disorder provides strong support for a benign interpretation. :contentReference[oaicite:3]{index=3}

---

# Current Governance

ClinGen implementation emphasizes that BS1 is **disease-specific**.

Current VCEP specifications demonstrate that thresholds can be calculated or selected using disease prevalence, penetrance, allelic heterogeneity, genetic heterogeneity and population data, with different disorders receiving different thresholds. :contentReference[oaicite:4]{index=4}

Therefore:

> **BS1 is a disease-specific principle, not a universal frequency cutoff.**

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
| Current-Use Status | Current Evidence Criterion |
| Disease-Specific Implementation Required | Yes |

---

# Runtime Safety Rule

The Safe Medical AI System must **not** infer:

> "Frequency above X% = BS1 for every disorder."

Instead, it should communicate:

> **BS1 depends on whether the observed allele frequency is greater than expected for the specific disorder.**

When a disease-specific ClinGen specification exists, the applicable specification should take precedence over a generic numerical assumption.

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
| 1.0.0 | 2026-08-08 | Initial Gold Release Knowledge Passport |

---

# Final Status

**APPROVED**

This Knowledge Passport is the official governance metadata for **PP-0145** and is fully compliant with the locked **Gold Population Package Specification v1.0**.