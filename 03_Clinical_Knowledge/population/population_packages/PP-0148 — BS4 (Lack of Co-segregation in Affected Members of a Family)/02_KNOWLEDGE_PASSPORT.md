# Knowledge Passport

---

# Identity

| Field | Value |
|-------|-------|
| Knowledge Passport ID | KP-PP-0148 |
| Population Package ID | PP-0148 |
| Clinical Knowledge Object | CKO-PP-0148 |
| Title | BS4 (Lack of Co-segregation in Affected Members of a Family) |
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
| Intended Audience | General public, patients diagnosed with gastric cancer, caregivers |
| Reading Level | Plain Language |
| Knowledge Granularity | Atomic (Single Educational Question) |
| Knowledge Scope | BS4 (Lack of Co-segregation in Affected Members of a Family) |

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

Patients with gastric cancer may undergo genetic testing when hereditary cancer predisposition is being evaluated. Family-based genetic evidence may contribute to interpretation of a variant identified during this process.

---

# Intended Runtime Usage

## Primary Runtime Role

- Foundational education on BS4

## Secondary Runtime Role

- ACMG evidence-code education
- Strong Benign Evidence education
- Family-based genetic evidence education
- Hereditary gastric-cancer genetics education
- Variant interpretation education
- Patient counseling
- Knowledge graph integration

---

## Typical Trigger Questions

- What is BS4?
- What does co-segregation mean?
- What does lack of segregation mean?
- Why does an affected relative without a variant matter?
- Why can gastric cancer in a relative be a phenocopy?
- Does one affected relative without the variant prove that the variant is benign?
- Why are family genetics rules different between hereditary cancer syndromes?

---

# Retrieval Priority

**Very High**

**Reason:**

BS4 is a foundational Strong Benign Evidence criterion for family-based variant interpretation and is particularly important in hereditary cancer, where phenocopies and alternative molecular causes can make apparent non-segregation difficult to interpret.

---

# Knowledge Graph

## Prerequisite Population Packages

PP-0001 → PP-0147

---

## Related Population Packages

| PP | Relationship |
|----|--------------|
| PP-0147 | BS3 |
| PP-0146 | BS2 |
| PP-0145 | BS1 |
| PP-0144 | BS Evidence Codes |
| PP-0133 | PP3 |
| PP-0116 | ACMG Evidence Codes |
| PP-0115 | ACMG Variant Classification Framework |
| PP-0108 | Variant Classification |

---

## Future Population Packages

- BA1
- PP1
- Detailed Co-segregation Analysis
- Quantitative Segregation Evidence
- Bayesian Segregation Framework
- Disease-Specific ClinGen Segregation Specifications
- Family History Interpretation
- Penetrance Modelling

---

# Clinical Scope

## Included

- BS4 definition
- Co-segregation
- Lack of co-segregation
- Affected family members
- Genotype-positive/genotype-negative distinction
- Inheritance pattern
- Phenotype definition
- Penetrance
- Age
- Phenocopies
- Alternative genetic causes
- Disease-specific interpretation
- Hereditary gastric-cancer context

---

## Explicitly Excluded

- Quantitative segregation statistics
- Bayesian likelihood ratios
- BayesScore
- Detailed PP1 implementation
- Minimum informative relatives
- Minimum meioses
- Pedigree statistical modelling
- Detailed penetrance calculations
- Disease-specific VCEP formulas
- Family-based molecular diagnostic workflow
- ACMG evidence-combination rules
- Treatment recommendations

These topics are intentionally delegated to independent Population Packages.

---

# Authoritative Sources

## Primary Sources

1. ACMG
2. AMP
3. ClinGen SVI
4. ClinGen Variant Curation Expert Panels
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

**ACMG/AMP**

BS4 is defined as:

> Lack of segregation in affected members of a family.

The framework also highlights important limitations, including phenocopies and the possibility that more than one pathogenic variant may occur within a family.

---

# Current Governance

Current ClinGen implementation emphasizes that BS4 should be applied only when family members are appropriately informative and the phenotype, genotype, inheritance model, and disease characteristics support the interpretation.

Disease-specific ClinGen Expert Panels may:

- define affected phenotypes;
- specify age requirements;
- modify evidence strength;
- establish family/informative-member requirements;
- restrict BS4;
- or determine that BS4 is not applicable.

---

# Gastric Cancer Context

Within the Safe Medical AI System for Oncology Patient Education, BS4 is relevant to interpretation of variants associated with **gastric cancer and hereditary gastric-cancer predisposition**.

The system must preserve the following boundaries:

- gastric cancer alone does not establish a hereditary syndrome phenotype;
- apparent non-segregation may represent a phenocopy;
- alternative pathogenic variants may explain disease in a family member;
- penetrance and age can affect informativeness;
- disease/gene-specific ClinGen specifications take precedence.

A particularly important governance example is **CDH1**, for which the current ClinGen Expert Panel specification states that BS4 is **not applicable**.

---

# Governance Metadata

| Field | Value |
|-------|-------|
| Clinical Governance | Enabled |
| Evidence Traceability | Complete |
| Scope Boundary | Defined |
| Knowledge Graph | Complete |
| Gastric-Cancer Context | Preserved |
| Disease-Specific Governance | Required |
| Runtime Ready | Yes |
| Repository Ready | Yes |
| Current-Use Status | Current Evidence Criterion |
| Universal Application Allowed | No |

---

# Runtime Safety Rule

The Safe Medical AI System must distinguish:

**Affected relative without the variant**

from:

**Reliable evidence of non-segregation**

and from:

**Final benign classification**

These concepts must not be treated as interchangeable.

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

This Knowledge Passport is the official governance metadata for **PP-0148** and is fully compliant with the locked **Gold Population Package Specification v1.0**.