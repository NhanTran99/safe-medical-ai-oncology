# Primary Evidence Package

---

# Identity

| Field | Value |
|-------|-------|
| Evidence Package ID | EP-PP-0146 |
| Population Package ID | PP-0146 |
| Title | BS2 (Observed in Healthy Adults Without the Disease) |
| Clinical Domain | Understanding Cancer |
| Version | 1.0.0 |
| Status | Approved |

---

# Clinical Question

**Primary Educational Question**

> **What is BS2 (Observed in Healthy Adults Without the Disease)?**

---

# Educational Intent

Provide patients and caregivers with an accurate, evidence-based explanation of **BS2** as a **Strong Benign Evidence** criterion within the ACMG/AMP variant interpretation framework.

The original ACMG/AMP framework defines BS2 around observation of a variant in a healthy adult in the relevant genotype state for a recessive, dominant, or X-linked disorder when **full penetrance is expected at an early age**. 

The underlying principle is:

> If a variant were expected to cause an early-onset, highly penetrant disorder, finding that variant in an appropriately evaluated healthy adult would be unexpected.

However, a healthy adult observation is **not automatically benign evidence**. Its significance depends on the disease model, age, penetrance, inheritance pattern, genotype, and adequacy of phenotyping.

Current ClinGen disease-specific specifications may restrict, modify, strengthen, weaken, or exclude BS2 depending on the disorder's characteristics. Therefore, this package presents BS2 as a **context-dependent criterion**, rather than a universal rule.

Within the Safe Medical AI System, this knowledge is relevant to interpretation of genetic findings in **gastric-cancer and hereditary gastric-cancer contexts**, while preserving the disease-specific nature of the underlying ACMG/ClinGen framework.

---

# Scope

## Included

- Definition of BS2
- Healthy adult observation
- Relationship between genotype and expected phenotype
- Age and disease onset
- Penetrance
- Inheritance pattern
- Adequacy of phenotyping
- Disease-specific interpretation
- Strong Benign Evidence
- Relevance to hereditary gastric-cancer interpretation
- Common misconceptions

---

## Excluded

- Disease-specific BS2 thresholds
- Detailed penetrance calculations
- Age-dependent penetrance modelling
- Detailed genotype-counting methodology
- gnomAD technical methodology
- Homozygote/hemizygote counting methodology
- BS2_Strong / BS2_Supporting implementation
- Detailed ClinGen VCEP specifications
- Bayesian framework
- ACMG benign evidence-combination rules
- BA1
- Laboratory workflow
- Treatment recommendations

These topics require dedicated Population Packages.

---

# Primary Evidence Sources

| Priority | Source | Purpose |
|-----------|--------|---------|
| 1 | American College of Medical Genetics and Genomics (ACMG) | Original ACMG/AMP framework and BS2 definition |
| 2 | Association for Molecular Pathology (AMP) | Joint variant interpretation framework |
| 3 | ClinGen Sequence Variant Interpretation (SVI) | Current interpretation and implementation principles |
| 4 | ClinGen Variant Curation Expert Panels (VCEPs) | Disease- and gene-specific implementation |
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
| BS2 is a Strong Benign Evidence criterion. | ACMG + AMP |
| BS2 concerns observation of a variant in a healthy adult in an appropriate genotype state. | ACMG + AMP |
| The original criterion assumes full penetrance at an early age. | ACMG + AMP |
| Age and expected disease onset affect interpretation of a healthy adult observation. | ACMG/AMP + ClinGen VCEP implementation |
| Reduced penetrance can weaken or prevent interpretation using BS2. | ClinGen VCEP specifications |
| Disease-specific specifications may modify BS2 implementation. | ClinGen VCEPs |
| Adequate phenotyping can be important when determining whether an individual is truly unaffected. | ClinGen disease-specific implementation |
| BS2 should not be interpreted as an automatic benign classification. | ACMG + AMP + ClinGen |

---

# Historical ACMG/AMP Definition

The original ACMG/AMP framework defines BS2 using observation of the variant in a healthy adult with the appropriate genotype for:

- a dominant disorder;
- a recessive disorder; or
- an X-linked disorder,

when **full penetrance is expected at an early age**. 

The underlying logic is that if a variant truly caused an early-onset, fully penetrant disorder, an appropriately evaluated adult carrying that variant would be expected to show the disorder.

Finding the variant in an unaffected adult therefore provides evidence against pathogenicity.

---

# Why Age Matters

A healthy adult observation is most informative when the disorder should already have manifested by that person's age.

For example:

**Early-onset disorder**

→ disease expected by adulthood

→ genuinely unaffected adult

→ observation may provide strong benign evidence.

By contrast:

**Late-onset disorder**

→ disease may not yet have appeared

→ healthy adult

→ observation may provide little or no equivalent evidence.

Therefore, the word **"adult"** cannot be interpreted independently of the disease's natural history.

---

# Why Penetrance Matters

Penetrance describes the proportion of people carrying a disease-causing variant who develop the associated condition.

When a disorder has very high or full penetrance, an unaffected person carrying the relevant disease-causing genotype is unexpected.

When penetrance is reduced, however, a person may carry a pathogenic variant and remain unaffected.

Therefore:

> **Healthy carrier ≠ automatically benign variant.**

The usefulness of BS2 depends on whether the disease model makes the healthy observation genuinely unexpected.

---

# Why the Inheritance Pattern Matters

The original ACMG/AMP criterion considers the genotype expected to cause the relevant disorder.

The relevant state may be:

- heterozygous for an appropriate dominant disorder;
- homozygous for an appropriate recessive disorder;
- hemizygous for an appropriate X-linked disorder.

Therefore, simply finding a variant in a healthy person is insufficient.

The genotype must be interpreted according to the disease's inheritance model.

---

# Why Phenotyping Matters

A person should not necessarily be considered unaffected merely because a database does not list a diagnosis.

Depending on the disorder, determining whether an individual is genuinely unaffected may require:

- appropriate clinical history;
- relevant examination;
- age-appropriate screening;
- disease-specific investigations.

The quality of the unaffected status therefore matters when interpreting BS2.

---

# Current ClinGen Governance

ClinGen disease-specific specifications demonstrate that BS2 cannot be applied identically to every disorder.

Depending on the disease, a VCEP may:

- retain BS2;
- restrict the eligible age;
- require specific clinical evaluation;
- require multiple unaffected individuals;
- modify the evidence strength;
- or determine that BS2 is not applicable.

This is particularly important for disorders with:

- reduced penetrance;
- late onset;
- variable expressivity;
- incomplete phenotyping.

Therefore:

> **BS2 is a disease-specific evidence principle, not simply "variant found in a healthy adult."**

---

# Gastric Cancer Context

Within this Safe Medical AI System, BS2 may become relevant when interpreting genetic variants associated with **hereditary gastric-cancer predisposition**.

The system must preserve the following boundary:

> A healthy adult carrying a variant associated with a hereditary gastric-cancer syndrome does not automatically establish that the variant is benign.

The interpretation must consider:

- the specific hereditary gastric-cancer disorder;
- expected age of disease onset;
- penetrance;
- inheritance pattern;
- relevant genotype;
- quality of clinical evaluation.

Evidence from one hereditary gastric-cancer syndrome must not automatically be transferred to another syndrome.

---

# BS2 Versus General "Healthy Carrier" Information

| Observation | Interpretation |
|---|---|
| Variant found in any healthy person | Not automatically BS2 |
| Variant found in appropriately evaluated healthy adult | Potentially relevant |
| Healthy adult with appropriate genotype for the disease | Potentially stronger evidence |
| Healthy adult + early-onset, highly penetrant disorder | BS2 may be applicable |
| Healthy adult + late-onset/reduced-penetrance disorder | BS2 may be weak or inappropriate |
| Disease-specific ClinGen specification available | Follow applicable specification |

---

# Clinical Claims Summary

The evidence supports the following educational messages:

- BS2 is Strong Benign Evidence.
- A healthy adult carrying a variant can provide evidence against pathogenicity when the disease model predicts that a pathogenic variant should already have caused disease.
- Age matters.
- Penetrance matters.
- Inheritance pattern and genotype matter.
- Adequate phenotyping matters.
- Reduced penetrance and late onset can substantially change the interpretation.
- BS2 must be interpreted in the context of the specific disorder.
- In hereditary gastric-cancer interpretation, one syndrome's BS2 rules should not automatically be generalized to another.

---

# Evidence Consistency Review

The original ACMG/AMP framework establishes the central BS2 principle: observation of the relevant genotype in a healthy adult can provide strong benign evidence when full penetrance is expected at an early age. 

Current ClinGen disease-specific implementation reinforces the importance of applying that principle according to the actual disease model rather than treating "healthy adult" as a universal criterion.

The evidence therefore supports a patient-facing explanation that emphasizes:

**healthy status + appropriate genotype + appropriate age + sufficiently penetrant disease model + adequate phenotyping**

rather than treating any one factor in isolation.

---

# Evidence Gaps

This Population Package intentionally does **not** provide:

- numerical BS2 thresholds;
- detailed penetrance calculations;
- age-dependent penetrance models;
- genotype-counting methodology;
- gnomAD implementation;
- BS2_Strong / BS2_Supporting rules;
- disease-specific VCEP specifications;
- Bayesian implementation;
- evidence-combination rules;
- treatment recommendations.

These subjects require independent Population Packages.

---

# Future Update Trigger

Review this package when:

- ACMG/AMP updates benign evidence criteria.
- ClinGen SVI revises BS2 guidance.
- ClinGen VCEPs publish or revise disease-specific BS2 specifications.
- Major hereditary gastric-cancer variant-interpretation standards change.
- Clinical governance requests revision.

---

# Evidence Package Decision

**APPROVED**

Evidence traceability is complete.

The package preserves the essential distinction:

> **BS2 is not "found in a healthy person."**

Rather, it is evidence derived from finding the relevant genotype in an appropriately evaluated healthy adult when the disease model predicts that a pathogenic variant should already have produced disease.

Repository Status: **Ready**.