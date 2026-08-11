# 02_KNOWLEDGE_PASSPORT — PP-0180 Gastric Cancer Molecular Classification

## Identity

- **KP ID:** KP-PP-0180
- **PP ID:** PP-0180
- **Title:** Gastric Cancer Molecular Classification
- **Version:** 1.0.0
- **Status:** GOLD — READY FOR INTEGRATION
- **Last Updated:** 2026-08-09

## Knowledge Classification

- **Clinical Domain:** Diagnosis / Pathology / Molecular Oncology
- **Primary Knowledge Type:** Patient-facing clinical education
- **Secondary Knowledge Types:** Molecular classification, molecular pathology, precision-oncology context
- **Clinical Complexity:** Intermediate-to-advanced
- **Educational Level:** Foundational-to-intermediate
- **Atomic Clinical Question:** What is molecular classification of gastric cancer, why is it needed, what broad molecular framework is used, and how does it relate to biomarkers and molecular testing?
- **Primary Runtime Intent:** Explain the molecular layer of gastric cancer characterization without duplicating individual biomarker or molecular-subtype packages.
- **Primary Clinical Dependency:** Tumor tissue/pathologic characterization with appropriate molecular or biomarker information.
- **Primary Downstream Dependencies:** Individual biomarker testing, detailed molecular subtypes, genomic-report interpretation and treatment-relevant molecular packages.

## Patient Journey Classification

- **Journey Stage:** Diagnosis → Pathology characterization → Molecular characterization → Precision-oncology context
- **Primary Patient Question:** “What does molecular classification tell us about my stomach cancer?”
- **Secondary Patient Questions:**
  - “Is molecular classification the same as genetic testing?”
  - “What are EBV, MSI, GS and CIN?”
  - “Is my HER2 or PD-L1 result my molecular subtype?”
  - “Does NGS tell me my molecular classification?”
  - “Does molecular classification determine treatment?”

## Intended Runtime Usage

This package is intended to:

1. Explain molecular classification as a higher-level framework.
2. Explain molecular heterogeneity.
3. Introduce the TCGA four-group framework.
4. Explain the difference between molecular classification and biomarker testing.
5. Explain the difference between molecular classification and NGS.
6. Introduce assay and specimen limitations.
7. Explain somatic versus germline distinctions.
8. Provide a controlled bridge to precision oncology.
9. Prevent overinterpretation of molecular results.
10. Preserve detailed ownership of PP-0188 and PP-0181–PP-0187.

## Retrieval / Runtime Relevance

### High-Priority Retrieval Concepts

- gastric cancer molecular classification
- gastric cancer molecular subtypes
- TCGA gastric cancer
- EBV-positive gastric cancer molecular subtype
- MSI gastric cancer molecular subtype
- genomically stable gastric cancer
- chromosomal instability gastric cancer
- gastric cancer molecular heterogeneity
- molecular classification vs biomarker testing
- gastric cancer NGS
- somatic vs germline gastric cancer
- molecular pathology gastric cancer

### Query Expansion Terms

- TCGA four molecular subtypes gastric adenocarcinoma
- EBV MSI GS CIN gastric cancer
- molecular characterization gastric adenocarcinoma
- genome instability gastric cancer
- chromosomal instability gastric cancer
- MSI MMR molecular classification
- HER2 biomarker vs molecular subtype
- PD-L1 molecular biomarker gastric cancer
- CLDN18.2 molecular subtype gastric cancer
- NGS molecular characterization gastric cancer

## Knowledge Graph

### Prerequisites

- PP-0175 — Gastric Cancer Diagnostic Work-up
- PP-0178 — Histopathologic Classification
- PP-0179 — Lauren Classification

### Related

- PP-0168 — EBV-associated Gastric Cancer + EBV Testing
- PP-0037 — WHO Classification
- Molecular pathology
- Precision oncology
- Biomarker testing

### Downstream

- PP-0181–PP-0187 — Individual biomarker / molecular testing
- PP-0188 — Molecular Subtypes of Gastric Cancer
- PP-0189 — Genomic Test Results / How to Read a Molecular Report
- PP-0190–PP-0191 — Biomarker Testing for Targeted Therapy / Immunotherapy

## Clinical Scope

### Core Knowledge Ownership

PP-0180 owns the molecular-classification layer of gastric cancer:

- definition;
- rationale;
- molecular heterogeneity;
- genome instability;
- TCGA framework;
- four broad molecular groups;
- relationship with histology and Lauren;
- relationship with individual biomarkers;
- relationship with NGS;
- high-level molecular alteration concepts;
- limitations;
- patient-facing interpretation.

### Supporting Knowledge

- DNA/gene/chromosome foundations;
- somatic versus germline distinction;
- assay scope;
- specimen adequacy;
- molecular tumor-board concept;
- tumor evolution;
- selected biomarker relationships.

### Explicit Exclusions

PP-0180 does not own:

- detailed histology;
- detailed Lauren;
- detailed WHO;
- detailed molecular subtype biology;
- individual biomarker testing;
- NGS methodology;
- variant interpretation;
- genomic-report interpretation;
- hereditary testing;
- individualized treatment or prognosis;
- molecular monitoring.

## Authoritative Sources

### Primary Clinical Sources

1. NCCN Gastric Cancer Version 2.2026.
2. NCI gastric-cancer materials supplied in the project.
3. ESMO-ASCO Recommendations for a Global Curriculum in Medical Oncology, 2023, especially molecular pathology and genetic/genomic testing competencies.

### Supporting Sources

- NCI Genetics of Gastric Cancer PDQ.
- ACS stomach-cancer materials where relevant.
- PP Registry.
- CORE_WORKING_RULES v1.6.
- FREEZE GOLD POPULATION PACKAGE SPECIFICATION v1.0.
- Approved Gold artifact and Discussion Batch references.

## Evidence Classification

| Knowledge Area | Evidence Class | Main Support |
|---|---|---|
| Molecular characterization is part of gastric-cancer classification | Established | NCCN |
| Gastric cancer molecular heterogeneity | Established | NCCN / TCGA reference |
| Genome instability | Established | NCCN |
| MSI as molecular feature | Established | NCCN |
| Chromosomal instability | Established | NCCN |
| TCGA four-group framework | Established research framework | TCGA cited by NCCN |
| EBV-positive group | Established molecular framework | TCGA/NCCN context |
| GS group | Established molecular framework | TCGA/NCCN context |
| CIN group | Established molecular framework | TCGA/NCCN context |
| Individual biomarker testing is distinct from classification | Established architecture | NCCN + Registry |
| NGS is a technology rather than classification itself | Established | ESMO-ASCO |
| Assay scope/limitations | Established | ESMO-ASCO |
| Somatic vs germline distinction | Established | ESMO-ASCO / NCI |
| Molecular classification alone determines treatment | Not established | Boundary control |
| Molecular classification alone determines individual prognosis | Not established | Boundary control |

## Governance Metadata

- **Execution Rule:** User-controlled PP sequence.
- **Source Rule:** Source-first.
- **Clinical Content Rule:** Source-grounded; no silent gap filling.
- **Artifact Rule:** Four governed artifacts.
- **Depth Rule:** Absolute full-depth compliance; approved Gold reference depth is the minimum; deeper is permitted.
- **Boundary Rule:** Clean four-part ownership Boundary required in production response.
- **QA Rule:** Four-layer QA.
- **Repository Readiness:** Ready for integration after final QA.

## Version Control

- **Semantic Version:** 1.0.0
- **Change Type:** Initial Gold production from locked Decision Batch.
- **Source Context:** NCCN Gastric Cancer v2.2026; ESMO-ASCO 2023; NCI gastric-cancer/genetics materials; project governance and registry.

## Change History

| Version | Date | Change |
|---|---|---|
| 1.0.0 | 2026-08-09 | Initial Gold Population Package generated after PP-0180 approval/lock. |

## Final Status

**GOLD — READY FOR INTEGRATION**
