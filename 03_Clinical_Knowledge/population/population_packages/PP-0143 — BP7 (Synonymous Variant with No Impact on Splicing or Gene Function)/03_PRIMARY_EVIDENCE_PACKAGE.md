# Primary Evidence Package

---

# Identity

| Field | Value |
|-------|-------|
| Evidence Package ID | EP-PP-0143 |
| Population Package ID | PP-0143 |
| Title | BP7 (Synonymous Variant with No Impact on Splicing or Gene Function) |
| Clinical Domain | Understanding Cancer |
| Version | 1.0.0 |
| Status | Approved |

---

# Clinical Question

**Primary Educational Question**

> **What is BP7 (Synonymous Variant with No Impact on Splicing or Gene Function)?**

---

# Educational Intent

Provide patients and caregivers with an accurate, evidence-based explanation of **BP7** as a Supporting Benign Evidence criterion within the ACMG/AMP variant interpretation framework.

A synonymous variant does not change the amino acid encoded by the affected codon, but synonymous changes can still affect RNA processing, particularly **pre-mRNA splicing**. Therefore, the fact that a variant is "silent" does not by itself establish that it has no biological effect.

The original ACMG/AMP framework defined BP7 for synonymous variants when splicing prediction does not indicate an effect on the splice consensus sequence or creation of a new splice site and the affected nucleotide is not highly conserved. 

ClinGen SVI subsequently refined the application of BP7. Current splicing recommendations emphasize that BP7 should be considered together with appropriate computational evidence, should not be applied to synonymous variants at the **first nucleotide or last three nucleotides of an exon**, and should not rely on conservation as an informative requirement. 

This Population Package therefore explains BP7 at a patient-education level while preserving the essential principle:

> **Synonymous does not automatically mean harmless.**

---

# Scope

## Included

- Definition of BP7
- Meaning of synonymous/silent variant
- Relationship between synonymous variants and RNA splicing
- Why splicing matters
- Role of computational splicing evidence
- Importance of variant location
- Supporting Benign Evidence
- Current ClinGen SVI refinement
- Patient-facing interpretation

---

## Excluded

- SpliceAI methodology
- MaxEntScan
- Individual splice prediction algorithms
- RNA sequencing methodology
- RT-PCR
- Minigene assays
- Detailed splice-position calculations
- Gene-specific BP7 specifications
- BP7_Strong(RNA) implementation
- Bayesian framework
- ACMG evidence-combination rules
- Laboratory workflow
- Treatment recommendations

These topics require dedicated Population Packages.

---

# Primary Evidence Sources

| Priority | Source | Purpose |
|-----------|--------|---------|
| 1 | American College of Medical Genetics and Genomics (ACMG) | Original ACMG/AMP framework and BP7 definition |
| 2 | Association for Molecular Pathology (AMP) | Joint variant interpretation framework |
| 3 | ClinGen Sequence Variant Interpretation (SVI) Working Group | Current BP7 implementation guidance |
| 4 | ClinGen SVI Splicing Subgroup | Splicing-specific refinement of BP7 |
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
- ClinGen SVI Splicing Subgroup

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
| BP7 is an ACMG/AMP Supporting Benign Evidence criterion. | ACMG + AMP |
| BP7 concerns synonymous variants for which available evidence indicates no meaningful splicing impact. | ACMG + AMP + ClinGen SVI |
| A synonymous variant does not necessarily have no biological effect. | ACMG/AMP framework + ClinGen SVI splicing guidance |
| Synonymous variants can affect RNA splicing. | ClinGen SVI Splicing Subgroup |
| Variant position near exon boundaries is important when considering splicing. | ClinGen SVI Splicing Subgroup |
| Current ClinGen recommendations refine the original BP7 application. | ClinGen SVI Splicing Subgroup |
| BP7 provides supporting rather than definitive benign evidence. | ACMG + AMP |

---

# Historical ACMG/AMP Definition

The original ACMG/AMP guideline defined BP7 for a synonymous variant where:

- splicing prediction does not indicate an impact on the splice consensus sequence;
- splicing prediction does not indicate creation of a new splice site; and
- the nucleotide is not highly conserved. 

This original definition provides the historical foundation for BP7.

---

# Current ClinGen SVI Refinement

ClinGen SVI Splicing Subgroup recommendations refine the application of BP7.

The current framework emphasizes that:

1. BP7 should be considered in conjunction with appropriate computational evidence.
2. Synonymous variants at the **first nucleotide or last three nucleotides of an exon** should not receive BP7 because these positions can be important for normal splicing.
3. Evolutionary conservation is not considered an informative requirement for BP7.
4. RNA-based evidence can provide a stronger form of evidence through separate BP7 RNA-related implementation rather than being treated as ordinary BP7 computational evidence. 

These refinements are important because the original ACMG/AMP wording does not capture all of the later splicing-specific implementation guidance.

---

# Clinical Claims Summary

The evidence supports the following educational messages:

- BP7 is a Supporting Benign Evidence criterion.
- A synonymous variant does not change the usual encoded amino acid.
- "Silent" does not automatically mean "no biological effect."
- Synonymous variants can sometimes affect RNA splicing.
- Evidence suggesting no meaningful splicing effect may support a benign interpretation.
- The position of a synonymous variant can influence how BP7 is considered.
- Current ClinGen SVI guidance refines the original ACMG/AMP application of BP7.
- BP7 alone does not establish that a variant is benign.

---

# Evidence Consistency Review

The original ACMG/AMP framework and subsequent ClinGen SVI guidance are consistent in their underlying principle but differ in implementation detail.

The original framework established BP7 around synonymous variants with no predicted splice impact and lack of high conservation. 

ClinGen SVI subsequently refined this approach to better account for splicing biology and variant location. The updated recommendations particularly restrict BP7 near exon boundaries and place less reliance on conservation. 

Therefore, this package deliberately presents the **current ClinGen-refined interpretation** rather than treating the original 2015 wording as an unrestricted universal rule.

---

# Evidence Gaps

This Population Package intentionally does **not** provide:

- detailed splice prediction algorithms;
- SpliceAI;
- MaxEntScan;
- RNA sequencing;
- RT-PCR;
- minigene assays;
- detailed splice-position calculations;
- BP7_Strong(RNA) implementation;
- gene-specific specifications;
- Bayesian implementation;
- ACMG evidence-combination rules;
- laboratory workflow;
- treatment recommendations.

These subjects require independent Population Packages.

---

# Future Update Trigger

Review this package when:

- ACMG/AMP updates variant interpretation recommendations.
- ClinGen SVI updates BP7 recommendations.
- ClinGen SVI Splicing Subgroup updates splicing-specific guidance.
- Relevant ClinGen Expert Panels publish gene- or disease-specific BP7 specifications.
- Major clinical genomic standards change.
- Clinical governance requests revision.

---

# Evidence Package Decision

**APPROVED**

Evidence traceability is complete.

The package preserves the central safety distinction:

> **Synonymous does not automatically mean harmless.**

It also preserves the distinction between the **original ACMG/AMP BP7 definition** and the **current ClinGen SVI refinement**.

Repository Status: **Ready**.