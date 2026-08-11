# Knowledge Passport

---

# Identity

| Field | Value |
|-------|-------|
| Knowledge Passport ID | KP-PP-0143 |
| Population Package ID | PP-0143 |
| Clinical Knowledge Object | CKO-PP-0143 |
| Title | BP7 (Synonymous Variant with No Impact on Splicing or Gene Function) |
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
| Knowledge Scope | BP7 (Synonymous Variant with No Impact on Splicing or Gene Function) |

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

Patients undergoing genetic testing may encounter synonymous or "silent" variants in genomic reports. This Population Package explains why such variants are not automatically harmless and how evidence concerning RNA splicing can contribute to a benign interpretation.

---

# Intended Runtime Usage

## Primary Runtime Role

- Foundational education on BP7

---

## Secondary Runtime Role

- ACMG evidence-code education
- Synonymous variant education
- RNA splicing education
- Computational evidence education
- Variant interpretation education
- Benign evidence education
- Patient counseling
- Knowledge graph integration

---

## Typical Trigger Questions

- What is BP7?
- What is a synonymous or silent variant?
- Can a silent variant cause a problem?
- Why does splicing matter for synonymous variants?
- Why does the location of a synonymous variant matter?
- How does BP7 support a benign interpretation?

---

# Retrieval Priority

**Very High**

**Reason:**

BP7 introduces the clinically important distinction between **protein sequence neutrality** and **overall gene-function neutrality**. It provides the foundational patient-facing explanation needed before introducing detailed splice prediction, RNA evidence, and splicing assays.

---

# Knowledge Graph

## Prerequisite Population Packages

PP-0001 → PP-0142

---

## Related Population Packages

| PP | Relationship |
|----|--------------|
| PP-0140 | BP4 |
| PP-0136 | BP Evidence Codes |
| PP-0133 | PP3 |
| PP-0116 | ACMG Evidence Codes |
| PP-0115 | ACMG Variant Classification Framework |
| PP-0108 | Variant Classification |

---

## Future Population Packages

- Splice prediction
- SpliceAI
- RNA evidence
- Functional splicing assays
- Deep intronic variants
- BP7_Strong(RNA)
- ACMG/ClinGen Splicing Framework

---

# Clinical Scope

## Included

- BP7 definition
- Synonymous/silent variants
- RNA splicing
- Splicing-related benign evidence
- Variant location
- Current ClinGen SVI refinement
- Patient implications

---

## Explicitly Excluded

- SpliceAI methodology
- MaxEntScan
- Individual prediction algorithms
- RNA sequencing
- RT-PCR
- Minigene assays
- Detailed splice-position calculations
- Gene-specific BP7 specifications
- BP7_Strong(RNA) implementation
- Bayesian framework
- ACMG evidence combination rules
- Treatment recommendations

These topics are intentionally delegated to independent Population Packages.

---

# Authoritative Sources

## Primary Sources

1. ACMG
2. AMP
3. ClinGen SVI
4. ClinGen SVI Splicing Subgroup
5. CAP
6. NCI
7. NCCN
8. ASCO

---

## Supporting Sources

- ACS
- ESMO

---

# Evidence Classification

## Evidence Model

Authoritative Educational Synthesis

---

## Historical Framework

**ACMG/AMP 2015**

BP7 was originally defined around synonymous variants for which splicing prediction algorithms predicted no impact on splice consensus/new splice sites and the nucleotide was not highly conserved. :contentReference[oaicite:0]{index=0}

---

## Current Governance

**ClinGen SVI Splicing Subgroup**

Current recommendations refine BP7 by:

- applying BP7 after BP4 is met;
- excluding synonymous variants at the first nucleotide or last three nucleotides of an exon;
- treating evolutionary conservation as non-informative for BP7;
- providing a separate framework for RNA evidence through BP7_Strong(RNA). :contentReference[oaicite:1]{index=1}

Disease/gene-specific ClinGen specifications may further modify these rules. :contentReference[oaicite:2]{index=2}

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
| Current-Use Status | Applicable with context-specific guidance |

---

# Runtime Safety Rule

The Safe Medical AI System must distinguish:

**Synonymous variant**

from:

**No biological effect**

A synonymous variant may still affect RNA splicing.

The system must therefore avoid generating:

> "Silent variants are harmless."

Instead, it should communicate that appropriate splicing evidence is needed before treating a synonymous variant as supporting benign evidence.

The system must also avoid presenting any single gene/disease-specific splice-position threshold as a universal rule.

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

This Knowledge Passport is the official governance metadata for **PP-0143** and is fully compliant with the locked **Gold Population Package Specification v1.0**.