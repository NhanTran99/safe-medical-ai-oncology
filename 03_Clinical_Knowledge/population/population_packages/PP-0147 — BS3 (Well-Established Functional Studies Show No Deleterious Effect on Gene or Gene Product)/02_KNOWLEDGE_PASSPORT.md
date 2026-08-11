# Knowledge Passport

---

# Identity

| Field | Value |
|-------|-------|
| Knowledge Passport ID | KP-PP-0147 |
| Population Package ID | PP-0147 |
| Clinical Knowledge Object | CKO-PP-0147 |
| Title | BS3 (Well-Established Functional Studies Show No Deleterious Effect on Gene or Gene Product) |
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
| Knowledge Scope | BS3 (Well-Established Functional Studies Show No Deleterious Effect on Gene or Gene Product) |

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

Patients with gastric cancer may undergo genetic testing when hereditary cancer predisposition is being evaluated. Functional evidence may contribute to interpretation of a genetic variant identified during this process.

---

# Intended Runtime Usage

## Primary Runtime Role

- Foundational education on BS3

## Secondary Runtime Role

- ACMG evidence-code education
- Strong Benign Evidence education
- Functional evidence education
- Hereditary cancer genetics education
- Gastric-cancer genetic testing education
- Variant interpretation education
- Patient counseling
- Knowledge graph integration

---

## Typical Trigger Questions

- What is BS3?
- What is a functional study?
- What does a normal functional result mean?
- Why does a functional study need to be well established?
- Why do controls matter?
- What is the difference between BS3 and PS3?
- Can a normal laboratory result prove that a variant is benign?

---

# Retrieval Priority

**Very High**

**Reason:**

BS3 is the foundational Strong Benign Evidence criterion for functional evidence and establishes the conceptual basis for understanding how functional studies can support benign variant interpretation.

---

# Knowledge Graph

## Prerequisite Population Packages

PP-0001 → PP-0146

---

## Related Population Packages

| PP | Relationship |
|----|--------------|
| PP-0146 | BS2 |
| PP-0145 | BS1 |
| PP-0144 | BS Evidence Codes |
| PP-0133 | PP3 |
| PP-0116 | ACMG Evidence Codes |
| PP-0115 | ACMG Variant Classification Framework |
| PP-0108 | Variant Classification |

---

## Future Population Packages

- BS4
- BA1
- PS3
- Functional Assay Validation
- ClinGen Functional Evidence Framework
- RNA Splicing Evidence
- Disease-Specific BS3 Specifications
- ACMG Benign Evidence Combination Rules

---

# Clinical Scope

## Included

- BS3 definition
- Functional studies
- Non-damaging functional results
- Assay validity
- Controls
- Reproducibility
- Disease relevance
- BS3 versus PS3
- Hereditary gastric-cancer context
- Patient implications

---

## Explicitly Excluded

- Detailed functional assay protocols
- Laboratory validation procedures
- Statistical calibration
- OddsPath calculations
- ClinGen SVI technical algorithm
- Gene-specific VCEP BS3 specifications
- BS3_Moderate / BS3_Supporting implementation
- Detailed PS3 implementation
- RNA-splicing-specific implementation
- Bayesian framework
- ACMG benign evidence-combination rules
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

**ACMG/AMP**

BS3 is the Strong Benign Evidence criterion for:

> Well-established in vitro or in vivo functional studies showing no damaging effect on protein function or splicing.

The criterion establishes the conceptual basis for using appropriately validated functional evidence to support a benign interpretation.

---

# Current Governance

ClinGen SVI recommendations emphasize that functional evidence should be evaluated systematically rather than treating every functional experiment as equivalent.

Relevant considerations include:

- disease mechanism;
- assay class applicability;
- assay validity;
- variant-level evidence;
- appropriate controls;
- reproducibility.

Disease-specific ClinGen VCEP specifications may further modify the strength or applicability of BS3.

---

# Gastric Cancer Context

Within the Safe Medical AI System for Oncology Patient Education, BS3 is relevant when functional evidence contributes to interpretation of variants associated with **gastric cancer or hereditary gastric-cancer predisposition**.

The system must preserve the following boundaries:

- functional evidence must be relevant to the specific gene;
- the assay must relate to the disease mechanism;
- a normal assay result is not automatically BS3;
- evidence from one gastric-cancer gene or syndrome must not automatically be generalized to another;
- BS3 evidence does not automatically constitute a final benign classification.

---

# Governance Metadata

| Field | Value |
|-------|-------|
| Clinical Governance | Enabled |
| Evidence Traceability | Complete |
| Scope Boundary | Defined |
| Knowledge Graph | Complete |
| Gastric-Cancer Context | Preserved |
| Runtime Ready | Yes |
| Repository Ready | Yes |
| Current-Use Status | Current Evidence Criterion |
| Disease-Specific Implementation Required | Yes |

---

# Runtime Safety Rule

The Safe Medical AI System must distinguish:

**Normal functional assay result**

from:

**Well-established, disease-relevant functional evidence supporting no damaging effect**

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

This Knowledge Passport is the official governance metadata for **PP-0147** and is fully compliant with the locked **Gold Population Package Specification v1.0**.