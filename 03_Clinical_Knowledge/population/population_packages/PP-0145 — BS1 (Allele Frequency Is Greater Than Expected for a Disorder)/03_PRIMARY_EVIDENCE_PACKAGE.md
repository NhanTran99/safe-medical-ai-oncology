# Primary Evidence Package

---

# Identity

| Field | Value |
|-------|-------|
| Evidence Package ID | EP-PP-0145 |
| Population Package ID | PP-0145 |
| Title | BS1 (Allele Frequency Is Greater Than Expected for a Disorder) |
| Clinical Domain | Understanding Cancer |
| Version | 1.0.0 |
| Status | Approved |

---

# Clinical Question

**Primary Educational Question**

> **What is BS1 (Allele Frequency Is Greater Than Expected for a Disorder)?**

---

# Educational Intent

Provide patients and caregivers with an accurate, evidence-based explanation of **BS1** as a **Strong Benign Evidence** criterion within the ACMG/AMP variant interpretation framework.

The core principle is that if a genetic variant occurs in a population at a frequency that is **greater than would be expected for a particular disorder**, that population frequency can provide strong evidence that the variant is unlikely to be responsible for that disorder.

The original ACMG/AMP framework defines BS1 as:

> **Allele frequency is greater than expected for disorder.** :contentReference[oaicite:0]{index=0}

Current ClinGen implementation demonstrates that BS1 is **disease-specific**. Expert Panels may establish different thresholds according to the disorder's prevalence, penetrance, allelic heterogeneity, genetic heterogeneity and available population data. :contentReference[oaicite:1]{index=1}

Therefore, this Population Package intentionally does **not** define a universal numerical BS1 cutoff.

---

# Scope

## Included

- Definition of BS1
- Meaning of allele frequency
- Meaning of "greater than expected for a disorder"
- Why population frequency can provide benign evidence
- Disease-specific interpretation
- General factors affecting expected frequency
- Relationship between BS1 and other benign evidence categories
- Patient-facing interpretation
- Common misconceptions

---

## Excluded

- Numerical thresholds for individual genes or disorders
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

These topics require dedicated Population Packages.

---

# Primary Evidence Sources

| Priority | Source | Purpose |
|-----------|--------|---------|
| 1 | American College of Medical Genetics and Genomics (ACMG) | Original ACMG/AMP framework and BS1 definition |
| 2 | Association for Molecular Pathology (AMP) | Joint variant interpretation framework |
| 3 | ClinGen Sequence Variant Interpretation (SVI) Working Group | Current implementation principles |
| 4 | ClinGen Variant Curation Expert Panels (VCEPs) | Disease/gene-specific BS1 specifications |
| 5 | College of American Pathologists (CAP) | Molecular pathology context |
| 6 | National Cancer Institute (NCI) | Patient-facing genomic education |
| 7 | NCCN Clinical Practice Guidelines | Clinical genomic context |
| 8 | American Society of Clinical Oncology (ASCO) | Precision oncology context |
| 9 | American Cancer Society (ACS) | Patient education |
| 10 | ESMO | International oncology context |

---

# Evidence Hierarchy

## Level I — Variant Interpretation Framework

- ACMG
- AMP
- ClinGen SVI

## Level I — Disease-Specific Implementation

- ClinGen VCEPs

## Supporting Clinical / Educational Sources

- CAP
- NCI
- NCCN
- ASCO
- ACS
- ESMO

---

# Evidence Matrix

| Clinical Claim | Supporting Source |
|----------------|-------------------|
| BS1 is a Strong Benign Evidence criterion. | ACMG + AMP |
| BS1 concerns an allele frequency greater than expected for the disorder. | ACMG + AMP |
| An unexpectedly high population frequency can support a benign interpretation. | ACMG + AMP |
| BS1 should be interpreted in relation to the specific disorder. | ClinGen SVI + VCEP specifications |
| BS1 thresholds can be disease- or gene-specific. | ClinGen VCEPs |
| Disease prevalence and penetrance can influence BS1 threshold development. | ClinGen VCEPs |
| Allelic and genetic heterogeneity can influence expected disease allele frequency. | ClinGen VCEPs |
| Large population datasets such as gnomAD may be used in BS1 implementation. | ClinGen SVI/VCEPs |
| A single universal frequency cutoff should not be assumed for every disorder. | ClinGen VCEP specifications |

---

# Historical ACMG/AMP Definition

The original ACMG/AMP framework defines **BS1** as:

> **Allele frequency is greater than expected for disorder.** :contentReference[oaicite:2]{index=2}

The underlying logic is that a variant responsible for a rare disorder should not ordinarily be present in the general population at a frequency that is incompatible with the expected disease frequency.

Therefore, an allele frequency that is too high for the disease model can provide **Strong evidence of benign impact**.

---

# Current ClinGen Interpretation

ClinGen implementation demonstrates that the phrase **"greater than expected"** cannot be reduced to one universal number.

Disease-specific Expert Panel specifications establish different BS1 thresholds for different disorders.

Examples include:

- One ClinGen specification uses a BS1 interval of **0.015%–0.15%**, based on disease-specific calculations. :contentReference[oaicite:3]{index=3}
- Another specification uses a BS1 threshold of **0.2%**, with disease-specific assumptions and population data requirements. :contentReference[oaicite:4]{index=4}
- Other Expert Panels use substantially different thresholds depending on disease characteristics and population datasets. :contentReference[oaicite:5]{index=5}

These examples demonstrate the governing principle:

> **BS1 is disease-specific, not a universal frequency cutoff.**

Disease-specific specifications may consider:

- disease prevalence;
- penetrance;
- allelic heterogeneity;
- genetic heterogeneity;
- population structure;
- population dataset quality;
- ancestry representation;
- quality-control requirements.

---

# Why Population Frequency Matters

If a disease is very rare, a variant that is responsible for that disease generally cannot be extremely common in the general population unless the disease model permits that frequency.

Therefore, an unexpectedly high population frequency can provide evidence against pathogenicity.

The reasoning is:

**Observed population frequency**

↓

**Compare with expected frequency for the disorder**

↓

**If substantially higher than expected**

↓

**Strong evidence that the variant may not be disease-causing**

This is the conceptual basis of BS1.

---

# Why There Is No Universal BS1 Cutoff

The expected frequency of disease-causing variants depends on the disorder.

Relevant factors may include:

- how common the disease is;
- penetrance;
- how many different variants can cause the disease;
- how many different genes can cause the disease;
- inheritance model;
- population structure.

ClinGen VCEP specifications demonstrate this directly: disease-specific BS1 thresholds range widely and may be calculated using different disease and population assumptions. :contentReference[oaicite:6]{index=6}

Consequently:

> **A frequency that is too high for one disorder may not be too high for another.**

---

# Population Data Context

Population frequency should be derived from an appropriate population dataset.

Current ClinGen implementations commonly use large population resources such as **gnomAD**, with disease-specific specifications determining which frequency measure and population groups should be considered. :contentReference[oaicite:7]{index=7}

This means that the following concepts may matter during technical implementation:

- population ancestry;
- maximum population frequency;
- filtering allele frequency;
- population sample size;
- quality-control filtering;
- founder populations.

These technical details are intentionally outside the scope of this patient-facing Population Package.

---

# BS1 Versus Other Benign Evidence

| Evidence Category | General Meaning |
|-------------------|-----------------|
| **BP** | Supporting Benign Evidence |
| **BS** | Strong Benign Evidence |
| **BA** | Stand-Alone Benign Evidence |

BS1 belongs to the **BS / Strong Benign Evidence** category.

It should therefore not be treated as interchangeable with BP evidence or BA1.

The specific rules governing how these evidence categories combine are intentionally deferred to separate Population Packages.

---

# Clinical Claims Summary

The evidence supports the following educational messages:

- BS1 is Strong Benign Evidence.
- BS1 considers whether a variant is more common than expected for a particular disorder.
- An unexpectedly high population frequency can provide strong evidence against pathogenicity.
- "Greater than expected" depends on the disorder.
- There is no universal BS1 frequency threshold applicable to every disease.
- Disease prevalence, penetrance and genetic/allelic heterogeneity can affect threshold determination.
- Population data must be interpreted in appropriate clinical and population context.
- BS1 is evidence within a structured variant interpretation framework, not simply a numerical shortcut.

---

# Evidence Consistency Review

The original ACMG/AMP definition and current ClinGen implementation are consistent in their central principle:

> **A variant that is too common for a particular disorder is less likely to be the cause of that disorder.**

The major refinement is implementation.

The original framework gives the conceptual criterion, while ClinGen VCEPs may operationalize BS1 using disease-specific thresholds and population-data requirements. :contentReference[oaicite:8]{index=8}

This package therefore intentionally avoids presenting any one numerical threshold as universal.

---

# Evidence Gaps

This Population Package intentionally does **not** provide:

- gene-specific BS1 thresholds;
- Whiffin/Ware calculations;
- gnomAD technical implementation;
- PopMax / GrpMax / FAF;
- detailed ancestry methodology;
- founder-effect analysis;
- BA1 thresholds;
- Bayesian calculations;
- ACMG benign evidence-combination rules;
- laboratory implementation.

These subjects require independent Population Packages.

---

# Future Update Trigger

Review this package when:

- ACMG/AMP updates benign variant interpretation guidance.
- ClinGen SVI updates population-frequency recommendations.
- ClinGen VCEPs publish or revise disease-specific BS1 specifications.
- Population databases undergo major methodological changes.
- Clinical governance requests revision.

---

# Evidence Package Decision

**APPROVED**

Evidence traceability is complete.

The package preserves the essential distinction:

> **BS1 = allele frequency greater than expected for the specific disorder**

rather than:

> **BS1 = allele frequency above one universal percentage.**

Repository Status: **Ready**.