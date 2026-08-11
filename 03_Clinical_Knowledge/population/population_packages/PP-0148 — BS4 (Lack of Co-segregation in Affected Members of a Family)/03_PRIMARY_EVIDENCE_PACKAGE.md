# Primary Evidence Package

---

# Identity

| Field | Value |
|-------|-------|
| Evidence Package ID | EP-PP-0148 |
| Population Package ID | PP-0148 |
| Title | BS4 (Lack of Co-segregation in Affected Members of a Family) |
| Clinical Domain | Understanding Cancer |
| Version | 1.0.0 |
| Status | Approved |

---

# Clinical Question

**Primary Educational Question**

> **What is BS4 (Lack of Co-segregation in Affected Members of a Family)?**

---

# Educational Intent

Provide patients and caregivers with an accurate, evidence-based explanation of **BS4** as a Strong Benign Evidence criterion within the ACMG/AMP variant interpretation framework.

The original ACMG/AMP framework defines BS4 as:

> Lack of segregation in affected members of a family.

The central principle is:

> If a variant truly causes a familial disorder, it is generally expected to occur in affected family members according to the relevant inheritance model. When appropriately characterized affected relatives have the disease but do not carry the variant, this lack of segregation can provide evidence against the variant being disease-causing.

However, non-segregation must be interpreted carefully.

The ACMG/AMP framework specifically notes that phenocopies can mimic lack of segregation, particularly for common phenotypes such as cancer, and that families can contain more than one pathogenic variant. ClinGen similarly emphasizes that BS4 concerns affected, phenotype-positive individuals who are genotype-negative for the variant of interest. ([clinicalgenome.org](https://www.clinicalgenome.org/site/assets/files/2071/clingen_cmp_acmg_specifications_v1-1.pdf))

Within the Safe Medical AI System, this knowledge is relevant to **gastric cancer and hereditary gastric-cancer predisposition**, while preserving disease-specific interpretation.

---

# Scope

## Included

- Definition of BS4
- Co-segregation and non-segregation
- Affected family members
- Genotype-positive and genotype-negative relatives
- Inheritance pattern
- Phenotype definition
- Penetrance and age
- Phenocopies
- Alternative pathogenic variants
- Disease-specific interpretation
- Gastric-cancer/hereditary gastric-cancer context
- Common misconceptions
- Patient-facing interpretation

---

## Excluded

- Detailed segregation statistics
- Bayesian likelihood ratios
- Quantitative co-segregation calculators
- BayesScore calculations
- PP1 detailed implementation
- Disease-specific ClinGen VCEP thresholds
- Minimum number of meioses or relatives
- Pedigree statistical modelling
- Detailed penetrance calculations
- Family-based molecular diagnostic workflow
- ACMG evidence-combination rules
- Treatment recommendations

These topics require dedicated Population Packages.

---

# Primary Evidence Sources

| Priority | Source | Purpose |
|-----------|--------|---------|
| 1 | American College of Medical Genetics and Genomics (ACMG) | Original ACMG/AMP framework and BS4 definition |
| 2 | Association for Molecular Pathology (AMP) | Joint variant interpretation framework |
| 3 | ClinGen Sequence Variant Interpretation (SVI) | Segregation evidence implementation principles |
| 4 | ClinGen Variant Curation Expert Panels (VCEPs) | Disease- and gene-specific BS4 implementation |
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
| BS4 is a Strong Benign Evidence criterion concerning lack of segregation in affected family members. | ACMG + AMP |
| BS4 concerns affected, phenotype-positive family members who do not carry the variant of interest. | ClinGen SVI |
| Phenocopies can mimic lack of segregation. | ACMG/AMP + ClinGen |
| Cancer is specifically highlighted as a phenotype where phenocopies can complicate BS4. | ACMG/AMP + ClinGen |
| Multiple pathogenic variants in one family can confound apparent non-segregation. | ACMG/AMP + ClinGen |
| Affected status must be appropriately characterized. | ClinGen VCEPs |
| Age and penetrance can affect whether family members are informative. | ClinGen VCEPs |
| Disease-specific VCEPs may modify strength or applicability of BS4. | ClinGen VCEPs |
| BS4 may be unavailable for some genes/diseases. | ClinGen VCEPs |

---

# Historical ACMG/AMP Definition

The original ACMG/AMP framework defines BS4 as:

> **Lack of segregation in affected members of a family.**

The framework also gives an important caveat:

- phenocopies, particularly for common phenotypes such as cancer, can mimic lack of segregation;
- families may have more than one pathogenic variant contributing to an autosomal dominant disorder.

Therefore, apparent non-segregation should not automatically be interpreted as benign evidence.

---

# What Is Co-Segregation?

Co-segregation describes whether a genetic variant tends to occur together with a disease phenotype within a family.

Conceptually:

**Variant present**

+

**Disease present**

across informative family members

→ the variant may be co-segregating with disease.

This type of evidence can support pathogenicity.

The opposite pattern is relevant to BS4:

**Disease present**

+

**Variant absent**

in an appropriately characterized affected family member

→ lack of segregation may support a benign interpretation.

---

# What Does "Affected" Mean?

For BS4, an affected family member should have the phenotype that is relevant to the specific disorder being evaluated.

This is particularly important in hereditary cancer.

For example:

> Family member has gastric cancer

does not automatically mean:

> Family member has the hereditary gastric-cancer syndrome under evaluation.

The cancer may instead represent:

- sporadic gastric cancer;
- a phenocopy;
- a different hereditary syndrome;
- another genetic cause;
- or an unrelated condition.

Therefore, phenotype definition is an essential part of interpreting non-segregation.

---

# What Does "Non-Segregation" Mean?

ClinGen guidance distinguishes BS4 from other family-based evidence.

For BS4, the relevant situation is:

> **Phenotype positive + genotype negative**

That is:

- the family member is appropriately affected;
- the family member does not carry the variant of interest.

By contrast:

> **Genotype positive + phenotype negative**

is a different situation and may be relevant to BS2 when appropriate for the particular disease.

This distinction is important because the two patterns answer different clinical questions. ([clinicalgenome.org](https://www.clinicalgenome.org/site/assets/files/3677/clingen_variant-curation_sopv1.pdf))

---

# Why Inheritance Pattern Matters

A variant is expected to track with disease according to the relevant inheritance model.

Therefore, interpretation of non-segregation requires consideration of:

- dominant inheritance;
- recessive inheritance;
- X-linked inheritance;
- other relevant inheritance mechanisms.

A family member who does not carry the variant may or may not be informative depending on the disease model.

---

# Why Penetrance Matters

If a disorder has incomplete or reduced penetrance, disease expression may not occur in every person who carries a pathogenic variant.

Similarly, age-dependent penetrance means that some relatives may not yet be old enough to determine whether they are truly unaffected.

Therefore, family evidence must be interpreted in relation to:

- penetrance;
- age of onset;
- expected phenotype;
- inheritance pattern.

ClinGen VCEP specifications demonstrate that these considerations can directly modify BS4 implementation. For example, some disease-specific specifications require affected individuals to meet defined phenotype criteria and may require additional family evidence before assigning stronger BS4 evidence. ([cspec.clinicalgenome.org](https://cspec.clinicalgenome.org/cspec/ui/svi/doc/GN078))

---

# Why Phenocopies Matter

A **phenocopy** is a condition that resembles the phenotype associated with a genetic disorder but is caused by something other than the variant being evaluated.

Phenocopies are particularly important in cancer genetics.

For example:

**Relative has gastric cancer**

↓

**Relative does not carry the variant**

does not necessarily mean:

**The variant does not cause hereditary gastric cancer.**

The relative may have developed a separate, sporadic cancer.

The original ACMG/AMP framework specifically highlights cancer as a phenotype in which phenocopies can mimic lack of segregation. ([clinicalgenome.org](https://www.clinicalgenome.org/site/assets/files/2071/clingen_cmp_acmg_specifications_v1-1.pdf))

---

# Why Multiple Pathogenic Variants Matter

A family may occasionally contain more than one pathogenic variant.

If one affected relative has a different disease-causing variant, absence of the variant being evaluated may not represent true evidence against that variant.

Therefore:

> **Alternative molecular explanations should be considered before interpreting apparent non-segregation as BS4.**

This is explicitly recognized in ACMG/AMP and ClinGen implementation guidance.

---

# BS4 Versus PP1

| Evidence | Direction |
|---|---|
| **PP1** | Variant co-segregates with disease → supports pathogenicity |
| **BS4** | Variant fails to segregate with disease in affected members → supports benign interpretation |

They are conceptually opposite directions of family-based evidence.

However, neither should be reduced to simply counting relatives without considering whether those relatives are informative.

---

# Why One Affected Relative Does Not Automatically Prove Benignity

A single genotype-negative affected relative can be informative, but the strength of that observation depends on:

- phenotype certainty;
- genotype certainty;
- inheritance model;
- penetrance;
- age;
- possibility of phenocopy;
- possibility of another pathogenic variant;
- disease-specific criteria.

Current ClinGen VCEP specifications demonstrate that implementations vary substantially.

Some specifications may allow BS4 at different strengths depending on the number of informative relatives or families, while others may determine that BS4 is not applicable at all. ([cspec.clinicalgenome.org](https://cspec.clinicalgenome.org/cspec/ui/svi/doc/GN078))

---

# Gastric Cancer Context

BS4 is particularly important to handle carefully in hereditary gastric-cancer interpretation.

For example, **CDH1** is a major hereditary gastric-cancer predisposition gene.

The current ClinGen CDH1 Expert Panel specification explicitly lists **BS4 as not applicable for CDH1**, while retaining the warning about phenocopies and multiple pathogenic variants. ([clinicalgenome.org](https://clinicalgenome.org/site/assets/files/7580/clingen_cdh1_acmg_specifications_v3_1.pdf))

This is an important governance example:

> **The existence of the generic ACMG BS4 criterion does not mean BS4 can automatically be used for every gastric-cancer gene.**

Therefore, in this Safe Medical AI System:

- disease/gene-specific ClinGen specifications take precedence;
- gastric cancer in a family must not automatically be treated as syndrome-specific disease;
- apparent non-segregation must be evaluated for phenocopies;
- alternative genetic causes must be considered.

---

# Clinical Claims Summary

The evidence supports the following educational messages:

- BS4 is Strong Benign Evidence in the general ACMG/AMP framework.
- BS4 concerns lack of segregation in appropriately characterized affected family members.
- The relevant pattern is generally phenotype-positive and genotype-negative for the variant of interest.
- Affected status must correspond to the disease being evaluated.
- Age, penetrance, inheritance pattern, and phenotype definition matter.
- Phenocopies are an important caveat, especially in cancer.
- Multiple pathogenic variants can confound apparent non-segregation.
- Disease-specific ClinGen specifications may modify or exclude BS4.
- In gastric-cancer genetics, the generic BS4 rule must not be applied without checking the relevant gene/disease-specific framework.
- For CDH1 specifically, the current ClinGen Expert Panel specification states that BS4 is not applicable.

---

# Evidence Consistency Review

The general ACMG/AMP principle and current ClinGen implementation are consistent:

**Disease + variant should normally track together if the variant is truly responsible for the familial disorder.**

Failure of that expected relationship can provide benign evidence.

However, ClinGen implementation makes clear that the observation must be interpreted in the context of:

- phenotype validity;
- genotype validity;
- inheritance;
- penetrance;
- phenocopies;
- alternative pathogenic variants;
- disease-specific specifications.

The gastric-cancer context makes these safeguards particularly important.

---

# Evidence Gaps

This Population Package intentionally does not provide:

- quantitative segregation calculations;
- likelihood ratios;
- Bayesian scoring;
- minimum family-member thresholds;
- disease-specific VCEP formulas;
- PP1 implementation;
- penetrance modelling;
- detailed pedigree algorithms.

These subjects require independent Population Packages.

---

# Future Update Trigger

Review this package when:

- ACMG/AMP updates benign evidence criteria.
- ClinGen SVI revises segregation guidance.
- ClinGen VCEPs publish or revise BS4 specifications.
- Gastric-cancer predisposition gene specifications change.
- ClinGen updates CDH1 or other hereditary gastric-cancer gene specifications.
- Clinical governance requests revision.

---

# Evidence Package Decision

**APPROVED**

Evidence traceability is complete.

The package preserves the essential distinction:

> **BS4 is not simply "an affected relative does not carry the variant."**

It requires appropriately characterized affected family members, reliable genotype information, and interpretation within the relevant disease model.

For gastric-cancer genetics, disease/gene-specific ClinGen guidance must take precedence over the generic ACMG/AMP rule.

Repository Status: **Ready**.