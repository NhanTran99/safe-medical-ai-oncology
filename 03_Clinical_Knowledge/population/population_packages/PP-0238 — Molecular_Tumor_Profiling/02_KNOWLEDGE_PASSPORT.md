# Knowledge Passport

---

# Identity

| Field | Value |
|-------|-------|
| Knowledge Passport ID | KP-PP-0238 |
| Population Package ID | PP-0238 |
| Clinical Knowledge Object | CKO-PP-0238 |
| Title | Molecular Tumor Profiling |
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
| Educational Category | Precision Oncology / Clinical Genomics |
| Educational Level | Introductory |
| Clinical Complexity | Intermediate |
| Intended Audience | General public, patients diagnosed with cancer, caregivers |
| Reading Level | Plain Language |
| Knowledge Granularity | Atomic (Single Educational Question) |
| Knowledge Scope | Molecular Tumor Profiling |

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
| Palliative Care | |

**Reason:**

Molecular tumor profiling is primarily encountered after a cancer diagnosis when clinicians are characterizing the tumor and considering whether molecular information may contribute to prognosis, treatment selection, or other management decisions. Its relevance can extend into later treatment and follow-up contexts when molecular characteristics are reassessed.

---

# Intended Runtime Usage

## Primary Runtime Role

- Foundational education on molecular tumor profiling

---

## Secondary Runtime Role

- Precision oncology education
- Clinical genomics education
- Molecular diagnostics education
- Patient counseling
- Shared decision-making support
- Interpretation of the concept of a molecular profile
- Knowledge graph integration

---

## Typical Trigger Questions

- What is molecular tumor profiling?
- Is molecular profiling the same as genetic testing?
- Is molecular profiling the same as NGS?
- What information is included in a tumor molecular profile?
- Can my gastric cancer have more than one molecular characteristic?
- Are HER2, MSI, or PD-L1 part of molecular profiling?
- Why is pathology still needed if molecular testing is done?
- What does an actionable mutation mean?
- Can a tumor's molecular profile change over time?
- Can blood testing provide molecular information about my tumor?

---

# Retrieval Priority

**Very High**

**Reason:**

Molecular tumor profiling is a central bridge between foundational biomarker testing/somatic genetic testing and downstream precision-oncology concepts. It provides the conceptual layer needed to understand why multiple molecular findings may be integrated into a tumor profile without conflating the profile with any single testing technology.

---

# Knowledge Graph

## Prerequisite Population Packages

- PP-0233 — Clinical Genomics
- PP-0235 — Somatic Genetic Testing
- Foundational biomarker and molecular-testing concepts

---

## Related Population Packages

| PP | Relationship |
|----|--------------|
| PP-0097 | Biomarker Testing |
| PP-0099 | Molecular Testing |
| PP-0101 | Next-Generation Sequencing (NGS) |
| PP-0102 | Gene Panel Testing |
| PP-0104 | Whole Exome Sequencing (WES) |
| PP-0105 | RNA Sequencing |
| PP-0107 | Variant Interpretation |
| PP-0236 | Liquid Biopsy |
| PP-0237 | Circulating Tumor DNA (ctDNA) |

---

## Recommended Next Population Package

PP-0239 — Genomic Biomarkers in Gastric Cancer

---

# Clinical Scope

## Included

- Definition of molecular tumor profiling
- Integrated molecular characterization
- Relationship to somatic genetic testing
- Genomic alterations
- Mutations
- Copy-number alterations/amplifications
- Gene fusions
- MSI/MMR and selected biomarker information as examples
- HER2, PD-L1, and CLDN18.2 as illustrative examples
- Targeted versus broader profiling
- NGS as one profiling approach
- Integration with pathology and clinical context
- Tumor heterogeneity
- Molecular evolution
- Conceptual actionability
- Tissue versus blood/ctDNA relationship
- Profile limitations
- Patient-facing interpretation

---

## Explicitly Excluded

- Detailed NGS methodology
- WGS/WES/RNA-sequencing methodology
- Bioinformatics and variant calling
- Variant interpretation/classification
- ACMG/AMP/ClinGen frameworks
- Germline testing workflow
- Genetic counseling
- Detailed biomarker-specific testing
- Detailed ctDNA biology/monitoring
- Molecular subtype algorithms
- Treatment algorithms
- Individual treatment recommendations

These topics are intentionally delegated to independent Population Packages.

---

# Authoritative Sources

## Primary Sources

1. **NCCN Clinical Practice Guidelines in Oncology — Gastric Cancer, Version 2.2026**
   - Principles of Pathologic Review and Biomarker Testing (GAST-B)
   - NGS biomarker testing
   - HER2, MSI/MMR, PD-L1, and related molecular/biomarker characterization
   - Current gastric-cancer clinical context

2. **ESMO/ASCO Recommendations for a Global Curriculum in Medical Oncology, Edition 2023**
   - Molecular oncology
   - Molecular biology/pathology
   - Genetic and genomic testing
   - Integration of pathology, molecular pathology, and other diagnostic materials

3. **NCCN Clinical Practice Guidelines in Oncology — Gastric Cancer, Version 2.2025 / JNCCN 2025**
   - Supporting gastric-cancer molecular/biomarker framework

4. **American Cancer Society — Stomach Cancer**
   - Patient-facing gastric-cancer education
   - Pathology, diagnosis, treatment, and integrated cancer-care context

5. **NCI — Genetics of Gastric Cancer (PDQ)**
   - Supporting distinction between tumor molecular findings and inherited/germline cancer genetics

---

## Supporting Sources

- NCI PDQ resources
- ACS patient education
- Project-approved molecular/genomic testing materials
- Dedicated PP-0106/PP-0107/PP-0110/PP-0111/PP-0112 materials for boundary alignment

---

# Evidence Classification

## Evidence Model

**Authoritative Educational Synthesis**

The package synthesizes high-authority gastric-cancer guidelines and oncology curriculum material into a patient-facing conceptual model.

---

## Evidence Hierarchy

### Level I

- NCCN
- ESMO
- ASCO

### Level II

- NCI PDQ
- ACS

### Supporting

- Project-approved dedicated molecular/genomic Population Packages

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
| Architecture Status | Locked |
| Production Status | Gold Release |

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
| 1.0.0 | 2026-08-08 | Initial Gold Release after approved PP-0238 scope lock |

---

# Final Status

**APPROVED**

This Knowledge Passport is the official governance metadata for **PP-0238 — Molecular Tumor Profiling** and is compliant with the locked Gold Population Package workflow and specification.
