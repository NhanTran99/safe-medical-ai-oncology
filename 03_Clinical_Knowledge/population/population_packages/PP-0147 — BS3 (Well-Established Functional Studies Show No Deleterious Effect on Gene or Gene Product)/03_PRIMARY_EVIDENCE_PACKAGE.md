# Primary Evidence Package

---

# Identity

| Field | Value |
|-------|-------|
| Evidence Package ID | EP-PP-0147 |
| Population Package ID | PP-0147 |
| Title | BS3 (Well-Established Functional Studies Show No Deleterious Effect on Gene or Gene Product) |
| Clinical Domain | Understanding Cancer |
| Version | 1.0.0 |
| Status | Approved |

---

# Clinical Question

**Primary Educational Question**

> **What is BS3 (Well-Established Functional Studies Show No Deleterious Effect on Gene or Gene Product)?**

---

# Educational Intent

Provide patients and caregivers with an accurate, evidence-based explanation of **BS3** as a **Strong Benign Evidence** criterion within the ACMG/AMP variant interpretation framework.

The original ACMG/AMP framework defines BS3 around well-established in vitro or in vivo functional studies showing no damaging effect on protein function or splicing.

The central principle is:

> A well-established and disease-relevant functional study showing that a variant does not cause a damaging functional effect can provide evidence supporting a benign interpretation.

However, the presence of a "normal" laboratory result does **not automatically qualify as BS3**.

ClinGen SVI recommendations establish a structured approach for evaluating functional evidence, including:

1. defining the disease mechanism;
2. evaluating the applicability of the assay class;
3. evaluating the validity of the specific assay;
4. applying the evidence to the individual variant.

Therefore, this Population Package presents BS3 as a **context-dependent functional-evidence criterion**, not as a simple "normal laboratory result = benign" rule.

---

# Scope

## Included

- Definition of BS3
- Functional studies
- No-damaging-effect results
- Meaning of "well-established"
- Assay validity
- Appropriate controls
- Reproducibility
- Disease relevance
- BS3 versus PS3
- Disease-specific interpretation
- Gastric-cancer/hereditary gastric-cancer context
- Patient-facing interpretation
- Common misconceptions

---

## Excluded

- Detailed functional assay protocols
- Laboratory validation procedures
- Statistical calibration
- OddsPath calculations
- ClinGen SVI technical implementation algorithm
- Gene-specific VCEP BS3 specifications
- BS3_Moderate / BS3_Supporting implementation
- Detailed PS3 implementation
- RNA-splicing-specific implementation
- Bayesian framework
- ACMG benign evidence-combination rules
- Laboratory workflow
- Treatment recommendations

These topics require dedicated Population Packages.

---

# Primary Evidence Sources

| Priority | Source | Purpose |
|-----------|--------|---------|
| 1 | American College of Medical Genetics and Genomics (ACMG) | Original ACMG/AMP framework and BS3 definition |
| 2 | Association for Molecular Pathology (AMP) | Joint variant interpretation framework |
| 3 | ClinGen Sequence Variant Interpretation (SVI) Working Group | Functional evidence evaluation framework |
| 4 | ClinGen Variant Curation Expert Panels (VCEPs) | Disease- and gene-specific functional evidence implementation |
| 5 | College of American Pathologists (CAP) | Molecular pathology context |
| 6 | National Cancer Institute (NCI) | Cancer genetics education |
| 7 | NCCN | Hereditary cancer and clinical genetics context |
| 8 | American Society of Clinical Oncology (ASCO) | Cancer genetics / precision oncology context |
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
| BS3 is a Strong Benign Evidence criterion concerning well-established functional studies showing no damaging effect. | ACMG + AMP |
| Functional studies can provide evidence about the biological consequences of a variant. | ACMG + AMP + ClinGen SVI |
| Functional evidence should be evaluated according to disease mechanism and assay applicability. | ClinGen SVI |
| Specific assay validity must be evaluated before functional evidence is assigned. | ClinGen SVI |
| Variant-level interpretation is required before applying functional evidence. | ClinGen SVI |
| Appropriate controls and assay validation contribute to confidence in functional evidence. | ClinGen SVI |
| Disease-specific VCEPs may modify the strength or applicability of BS3. | ClinGen VCEPs |
| Some diseases may have no sufficiently established assay for BS3. | ClinGen VCEPs |

---

# Historical ACMG/AMP Definition

BS3 is the benign counterpart of the functional evidence criterion PS3.

Conceptually:

**PS3**

→ well-established functional evidence supports a damaging effect.

**BS3**

→ well-established functional evidence shows no damaging effect.

The original ACMG/AMP framework therefore places BS3 within the Strong Benign Evidence category.

---

# Why Functional Studies Matter

A genetic variant changes DNA sequence, but the clinical interpretation may depend on whether that change actually alters biological function.

Functional studies can investigate consequences at different biological levels, including:

- gene function;
- RNA processing;
- protein function;
- cellular function;
- relevant biological pathways.

A functional result can therefore provide information that is not available from the DNA sequence alone.

However, the usefulness of a functional study depends on whether the measured function is relevant to the disease mechanism.

---

# What Does "No Damaging Effect" Mean?

For BS3, the functional result should support the conclusion that the variant does **not** disrupt a relevant biological function in a way expected to cause disease.

The interpretation should therefore not be reduced to:

> "The experiment looked normal."

Instead, the relevant question is:

> **Does the experiment reliably measure a biological function that is relevant to the disease mechanism, and does the result support normal function?**

---

# Why "Well-Established" Matters

Functional studies vary considerably in quality and clinical relevance.

A well-established assay should have sufficient evidence supporting:

- technical reliability;
- reproducibility;
- appropriate controls;
- biological relevance;
- ability to distinguish relevant normal and abnormal states.

ClinGen SVI developed a structured framework specifically because functional assays had historically been applied inconsistently across variant-interpretation settings.

---

# Functional Evidence Evaluation Framework

At the conceptual level, ClinGen SVI recommends evaluating functional evidence through four major steps:

### Step 1 — Define the Disease Mechanism

Determine what biological mechanism is known to cause the disorder.

### Step 2 — Evaluate Assay Applicability

Determine whether the type of assay being used can meaningfully evaluate that disease mechanism.

### Step 3 — Evaluate Specific Assay Validity

Determine whether the particular assay has sufficient validity, controls, reproducibility, and other evidence to support clinical interpretation.

### Step 4 — Apply Evidence to the Individual Variant

Determine whether the specific variant's result supports the relevant evidence code and strength.

These steps prevent a technically successful experiment from being automatically interpreted as clinically meaningful functional evidence.

---

# Why Controls Matter

Controls help establish what normal and abnormal assay results look like.

Appropriate controls can help researchers determine:

- the expected normal range;
- the abnormal range;
- assay variability;
- whether the assay can distinguish known benign and pathogenic variants.

Without appropriate controls, it may be difficult to determine how confidently a result should influence variant interpretation.

---

# Why Reproducibility Matters

A result that can be reproduced reliably is generally more convincing than an isolated result obtained under uncertain experimental conditions.

Reproducibility can increase confidence that:

- the assay measures a real biological effect;
- the result is not simply technical variation;
- the interpretation is stable across appropriate experimental settings.

---

# Why Disease Relevance Matters

A gene or protein may perform multiple biological functions.

An assay can show that one function is normal without proving that all disease-relevant functions are normal.

Therefore:

> **A good assay is not necessarily a relevant assay.**

For BS3, the measured biological function should have a meaningful relationship to the disease mechanism being evaluated.

---

# BS3 Versus PS3

| Evidence | General Meaning |
|---|---|
| **PS3** | Well-established functional evidence supports a damaging effect |
| **BS3** | Well-established functional evidence supports no damaging effect |

Both criteria concern functional evidence.

The difference is the direction of the evidence.

The quality requirements for interpreting functional evidence remain important for both criteria.

---

# Why a Normal Result Is Not Automatically BS3

Consider the following progression:

**Laboratory experiment**

↓

**Normal-looking result**

↓

**Is the assay valid?**

↓

**Is the assay relevant to the disease mechanism?**

↓

**Are controls appropriate?**

↓

**Is the result reproducible and interpretable?**

↓

**Does the result apply meaningfully to this variant?**

Only after appropriate evaluation can functional evidence be assigned the relevant evidence strength.

Therefore:

> **Normal result ≠ automatically BS3.**

---

# Disease-Specific Implementation

ClinGen VCEP specifications demonstrate that BS3 is not implemented identically across all genes and diseases.

Depending on the available evidence, a VCEP may:

- retain BS3 at Strong;
- assign a lower strength;
- specify particular approved assays;
- restrict BS3 to particular functional readouts;
- or determine that BS3 is not applicable.

Some disease-specific specifications also explicitly state that currently available assays are insufficient to establish BS3.

Therefore:

> **The availability of a functional assay does not itself establish that BS3 can be applied.**

---

# Gastric Cancer Context

Within the Safe Medical AI System for Oncology Patient Education, BS3 is relevant when functional evidence contributes to interpretation of variants associated with:

- gastric cancer;
- hereditary gastric-cancer predisposition;
- genes relevant to inherited cancer risk.

The system must preserve the following boundaries:

- the assay must be relevant to the specific gene;
- the assay must be relevant to the disease mechanism;
- a normal assay result is not automatically BS3;
- evidence from one hereditary gastric-cancer gene or syndrome must not automatically be generalized to another;
- disease-specific ClinGen guidance should take precedence when available.

---

# Clinical Claims Summary

The evidence supports the following educational messages:

- BS3 is Strong Benign Evidence.
- BS3 concerns well-established functional studies showing no relevant damaging effect.
- Functional studies can provide biological evidence about the consequences of a genetic variant.
- Not every functional assay is sufficiently reliable or relevant for BS3.
- Disease mechanism, assay applicability, assay validity, controls, and reproducibility matter.
- A normal laboratory result is not automatically BS3.
- PS3 and BS3 represent opposite directions of functional evidence.
- Disease-specific ClinGen specifications may modify the strength or applicability of BS3.
- In gastric-cancer interpretation, functional evidence must be relevant to the specific gene and disease mechanism.

---

# Evidence Consistency Review

The ACMG/AMP framework establishes BS3 as Strong Benign Evidence based on well-established functional studies showing no damaging effect.

ClinGen SVI subsequently provided a structured framework because differences in functional-evidence evaluation contributed to disagreement between variant-classification laboratories.

The current evidence therefore supports a patient-facing interpretation that distinguishes:

**functional experiment**

from

**validated and disease-relevant functional evidence**

and from

**final benign classification**.

---

# Evidence Gaps

This Population Package intentionally does **not** provide:

- detailed assay protocols;
- specific assay-control numbers;
- statistical calibration;
- OddsPath calculations;
- gene-specific assay thresholds;
- disease-specific VCEP rules;
- BS3_Moderate / BS3_Supporting implementation;
- PS3 implementation;
- detailed RNA-splicing implementation;
- Bayesian interpretation;
- ACMG evidence-combination rules.

These subjects require independent Population Packages.

---

# Future Update Trigger

Review this package when:

- ACMG/AMP updates functional evidence criteria.
- ClinGen SVI revises PS3/BS3 recommendations.
- ClinGen VCEPs publish or revise disease-specific BS3 specifications.
- New validated functional assays become clinically accepted for relevant gastric-cancer genes.
- Major hereditary gastric-cancer variant-interpretation standards change.
- Clinical governance requests revision.

---

# Evidence Package Decision

**APPROVED**

Evidence traceability is complete.

The package preserves the essential distinction:

> **BS3 is not "a normal laboratory result."**

Rather, BS3 requires functional evidence that is sufficiently well established, valid, and relevant to the disease mechanism to support a non-damaging interpretation.

Repository Status: **Ready**.