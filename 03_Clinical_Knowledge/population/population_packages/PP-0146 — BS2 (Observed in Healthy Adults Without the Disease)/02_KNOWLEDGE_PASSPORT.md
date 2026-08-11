# Knowledge Passport

---

# Identity

| Field | Value |
|-------|-------|
| Knowledge Passport ID | KP-PP-0146 |
| Population Package ID | PP-0146 |
| Clinical Knowledge Object | CKO-PP-0146 |
| Title | BS2 (Observed in Healthy Adults Without the Disease) |
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
| Knowledge Scope | BS2 (Observed in Healthy Adults Without the Disease) |

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

Patients with gastric cancer may undergo germline or other genetic testing when hereditary cancer predisposition is being evaluated. This Population Package explains how observation of a variant in an appropriately evaluated healthy adult can contribute to benign variant interpretation and why age, penetrance, inheritance pattern, and disease-specific context matter.

---

# Intended Runtime Usage

## Primary Runtime Role

- Foundational education on BS2

## Secondary Runtime Role

- ACMG evidence-code education
- Strong Benign Evidence education
- Hereditary cancer genetics education
- Gastric-cancer genetic testing education
- Variant interpretation education
- Patient counseling
- Knowledge graph integration

---

## Typical Trigger Questions

- What is BS2?
- Why does finding a variant in a healthy person matter?
- Does a healthy person carrying a variant mean the variant is benign?
- Why does age matter for BS2?
- What is penetrance?
- Why does the inheritance pattern matter?
- How can BS2 be relevant to hereditary gastric cancer?

---

# Retrieval Priority

**Very High**

**Reason:**

BS2 is a foundational Strong Benign Evidence criterion and is particularly important for explaining why an apparently unaffected individual can provide evidence against pathogenicity while avoiding the unsafe assumption that healthy carrier status automatically means benign.

---

# Knowledge Graph

## Prerequisite Population Packages

PP-0001 → PP-0145

---

## Related Population Packages

| PP | Relationship |
|----|--------------|
| PP-0145 | BS1 |
| PP-0144 | BS Evidence Codes |
| PP-0136 | BP Evidence Codes |
| PP-0116 | ACMG Evidence Codes |
| PP-0115 | ACMG Variant Classification Framework |
| PP-0108 | Variant Classification |

---

## Future Population Packages

- BS3
- BS4
- BA1
- Disease Penetrance
- Age-Dependent Penetrance
- Healthy-Control Evidence
- Disease-Specific BS2 Specifications
- ClinGen VCEP Implementation
- ACMG Benign Evidence Combination Rules

---

# Clinical Scope

## Included

- BS2 definition
- Healthy adult observation
- Age
- Penetrance
- Inheritance pattern
- Genotype
- Phenotyping
- Disease-specific interpretation
- Hereditary gastric-cancer context
- Patient implications

---

## Explicitly Excluded

- Disease-specific numerical BS2 thresholds
- Detailed penetrance calculations
- Age-dependent penetrance modelling
- Detailed genotype-counting methodology
- gnomAD technical methodology
- Homozygote/hemizygote counting
- BS2_Strong / BS2_Supporting implementation
- Detailed ClinGen VCEP specifications
- Bayesian framework
- ACMG benign evidence-combination rules
- BA1
- Laboratory workflow
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

**ACMG/AMP 2015**

BS2 was defined around observation of a variant in a healthy adult in the relevant genotype state for a recessive, dominant, or X-linked disorder where **full penetrance is expected at an early age**.

This establishes the central logic that an unaffected adult can provide strong benign evidence when the disease model predicts that a truly pathogenic variant should already have produced disease.

---

# Current Governance

Current ClinGen disease-specific specifications may:

- restrict use of BS2;
- require specific ages;
- require adequate clinical evaluation;
- require a minimum number of unaffected individuals;
- modify the strength assigned to BS2;
- or determine that BS2 is not applicable because of reduced penetrance or other disease characteristics.

Therefore, the generic ACMG/AMP definition must not be treated as an unrestricted universal rule.

---

# Gastric Cancer Context

Within the Safe Medical AI System for Oncology Patient Education, BS2 is relevant when interpreting germline variants in the context of **hereditary gastric-cancer predisposition**.

The system must:

- preserve the disease-specific nature of BS2;
- avoid generalizing one hereditary gastric-cancer syndrome to another;
- account for age of onset and penetrance;
- avoid interpreting "healthy adult" as equivalent to "benign variant."

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

The Safe Medical AI System must distinguish:

**Healthy adult carrying a variant**

from:

**Evidence that the variant is benign**

A healthy adult observation becomes strong evidence only when it is inconsistent with the expected phenotype for the relevant disorder, given the person's age, genotype, inheritance pattern, penetrance, and clinical evaluation.

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

This Knowledge Passport is the official governance metadata for **PP-0146** and is fully compliant with the locked **Gold Population Package Specification v1.0**.