# 02_KNOWLEDGE_PASSPORT.md

# Knowledge Passport

## Identity

| Field | Value |
|---|---|
| KP ID | KP-PP-0189 |
| PP ID | PP-0189 |
| Title | Genomic Test Results / How to Read a Molecular Report |
| Version | 1.0.0 |
| Status | GOLD — READY FOR INTEGRATION |
| Clinical Domain | Diagnosis / Precision Oncology / Molecular Testing |
| Audience | Patients, caregivers, and general oncology learners |
| Language | English source artifact; patient-facing plain-language style |

---

# Knowledge Classification

## Knowledge Type

Patient-facing clinical education / molecular testing literacy.

## Atomic Clinical Question

> **How can I read and understand a genomic or molecular test report in gastric cancer?**

## Primary Function

This PP is a **report-literacy node** between molecular testing and downstream biomarker/treatment application.

It teaches the reader how to orient to:

- the test;
- the specimen;
- the assay scope;
- the molecular finding;
- the laboratory interpretation;
- possible clinical relevance;
- limitations;
- clinical context.

It does not own individualized interpretation or treatment selection.

---

# Patient Journey Classification

| Dimension | Classification |
|---|---|
| Primary journey stage | Diagnosis / Molecular characterization |
| Secondary journey stage | Treatment planning / Precision oncology |
| Decision point | Understanding a completed or available molecular test report |
| Typical trigger | Patient receives or is asked to discuss a genomic/molecular report |
| Downstream need | Biomarker-specific interpretation and treatment application |

---

# Intended Runtime Usage

## Primary Runtime Use

Retrieve when a user asks:

- “How do I read my molecular report?”
- “What does this genomic test result mean?”
- “What does detected/not detected mean?”
- “What is a VUS?”
- “What does actionable mean on a cancer report?”
- “Why does my report say no actionable alteration?”
- “Why did my tissue and blood tests differ?”
- “What does NGS report?”
- “Why does the report mention HER2/MSI/PD-L1/TMB/FGFR2/CLDN18.2?”

## Secondary Runtime Use

Retrieve when a user needs orientation before entering a dedicated biomarker or treatment package.

## Do Not Use as a Substitute For

- individualized variant interpretation;
- individualized genetic counselling;
- individualized treatment selection;
- detailed biomarker testing interpretation;
- interpretation of an actual laboratory report without clinical context.

---

# Retrieval / Runtime Relevance

## High-Priority Retrieval Terms

- molecular report
- genomic report
- genomic test result
- molecular test result
- NGS report
- sequencing report
- molecular profiling
- actionable alteration
- no actionable alteration
- detected
- not detected
- negative molecular test
- VUS
- variant of uncertain significance
- pathogenic variant
- specimen
- tumor tissue
- liquid biopsy
- ctDNA
- tumor cellularity
- sample adequacy
- molecular pathology report
- biomarker report

## Gastric-Cancer Biomarker Retrieval Terms

- HER2 report
- MSI
- MMR
- PD-L1
- CLDN18.2
- TMB
- FGFR2
- genomic alteration
- gene amplification
- deletion
- fusion
- mutation

## Clinical Context Retrieval Terms

- precision oncology
- treatment relevance
- targeted therapy biomarker
- immunotherapy biomarker
- germline question
- tumor-only sequencing
- genetic counselling
- molecular tumor board

---

# Knowledge Graph

## Prerequisites

### PP-0097 — Biomarker Testing

Provides the foundational concept that biomarker testing evaluates biological characteristics that may contribute to cancer care and is individualized rather than universal.

### PP-0107 — Clinical Genomics

Provides the broader genomic context required to understand molecular findings.

### PP-0110 — Somatic Genetic Testing

Provides the concept of tumor/somatic genomic testing that generates molecular findings.

### PP-0111 — Liquid Biopsy

Provides the broad liquid-biopsy context for blood-based molecular testing.

### PP-0187 — NGS Biomarker Testing

Provides the testing approach that can generate multi-gene/multi-event molecular information.

### PP-0188 — Molecular Subtypes of Gastric Cancer

Provides broader molecular classification context.

### PP-0181–PP-0186

Provide dedicated interpretation of specific gastric-cancer biomarkers that may appear in a molecular testing record.

---

## Related

- PP-0108 — Variant Classification
- PP-0109 — Variant-specific interpretation packages
- PP-0178 — Histopathologic Classification
- PP-0179 — Lauren Classification
- PP-0180 — Gastric Cancer Molecular Classification
- ctDNA / liquid-biopsy packages
- Hereditary gastric cancer
- Genetic testing
- Genetic counselling
- Molecular pathology
- Precision oncology

---

## Next / Downstream

### PP-0190 — Biomarker Testing for Targeted Therapy

Owns the transition from molecular findings to targeted-therapy biomarker application.

### PP-0191 — Biomarker Testing for Immunotherapy

Owns the transition from molecular/immune findings to immunotherapy biomarker application.

### Treatment Population Packages

Own treatment decisions and treatment-specific clinical application.

---

# Clinical Scope

## Core Ownership

PP-0189 owns the **interpretive literacy layer of a molecular report**.

It explains:

1. what the report is;
2. what test generated it;
3. what specimen was tested;
4. what the assay could assess;
5. what types of findings may be listed;
6. what common result terms mean at a high level;
7. how clinical relevance is described;
8. why limitations matter;
9. why molecular results need clinical context;
10. what questions the patient should ask the care team.

## Supporting Ownership

PP-0189 may introduce, without owning detailed methodology:

- tissue versus liquid genomic testing;
- tumor cellularity;
- sample quality;
- assay limitations;
- discordant results;
- possible germline implications;
- molecular tumor board review;
- clinical-trial relevance.

## Explicit Exclusions

PP-0189 does not own:

- NGS laboratory methodology;
- sequencing chemistry;
- bioinformatics;
- variant calling;
- detailed variant interpretation;
- variant-classification systems;
- detailed biomarker-specific testing/scoring;
- detailed ctDNA biology;
- germline testing algorithms;
- hereditary-risk management;
- treatment selection;
- individualized prognosis;
- individualized report interpretation.

---

# Authoritative Source Set

## Primary Project Source Materials

### 1. Gastric Cancer v2.2026 — NCCN Clinical Practice Guidelines in Oncology

Primary gastric-cancer guideline source for:

- biomarker testing context;
- preferred initial testing approaches;
- NGS biomarker testing;
- molecular events detectable by NGS;
- ctDNA/liquid-biopsy context;
- selected targetable alterations.

The guideline states that IHC/ISH/targeted gene PCR is preferred initially for biomarkers, while validated NGS may be considered later in selected patients with sufficient tumor tissue. It also describes NGS as capable of assessing multiple mutations and other molecular events, including amplification, deletions, TMB, and MSI.

### 2. ESMO-ASCO Recommendations for a Global Curriculum in Medical Oncology — Edition 2023

Primary genomic-testing framework for:

- DNA/RNA/protein-directed assays;
- analyte, panel, and genome-wide testing concepts;
- genomic alteration categories;
- pre-analytic variables;
- post-analytic variables;
- clinical context for variant interpretation;
- potential germline findings from tumor testing;
- molecular/genomic testing indications.

### 3. NCI Cancer Genetics Risk Assessment and Counseling PDQ

Primary source for:

- multigene testing;
- possible genetic-test outcomes;
- VUS;
- incidental germline findings from somatic mutation profiling;
- genetic counselling and follow-up concepts.

### 4. NCI Treatment of Stomach Cancer

Supporting patient-facing source for:

- biomarker tests in relation to targeted therapy and immunotherapy;
- treatment decisions being made with the cancer care team and considering multiple factors.

### 5. American Cancer Society — Stomach Cancer

Supporting patient-facing source for:

- biomarker-associated treatment contexts;
- examples of HER2, CLDN18.2, PD-L1 and MSI-H/dMMR relevance;
- the broader role of testing within gastric-cancer management.

### 6. American Cancer Society — Immunotherapy for Stomach Cancer

Supporting source for biomarker-linked treatment context and examples of molecularly selected therapies.

---

# Evidence Classification

## Established / Guideline-Supported

- Molecular/genomic testing can evaluate defined biological characteristics of cancer.
- Assays differ in scope and can be directed toward DNA, RNA, protein, specific analytes, panels, or broader genomic assays.
- Molecular testing can detect multiple classes of genomic alterations.
- Specimen characteristics and pre-analytic variables can influence molecular test results.
- NGS can assess multiple molecular events simultaneously.
- In gastric cancer, NGS is a relevant clinical testing approach in selected contexts, while IHC/ISH/targeted PCR remain preferred initial approaches for specific biomarkers in NCCN guidance.
- Blood-based ctDNA is a form of liquid biopsy and may be considered in selected gastric-cancer situations.
- Molecular findings require interpretation in the proper clinical context.
- Possible germline findings from somatic profiling may require additional work-up and genetic counselling.
- Biomarker testing can contribute to treatment planning in selected targeted-therapy and immunotherapy contexts.

## Context-Dependent

- Whether a specific molecular finding is clinically actionable.
- Whether a broader NGS panel is useful for an individual patient.
- Whether additional testing is needed after an indeterminate, inadequate, or potentially germline-relevant result.
- Whether tissue or blood-based testing is preferable in a particular clinical setting.

## Not Owned by This PP

- detailed treatment algorithms;
- detailed biomarker thresholds;
- variant-classification methodology;
- individualized genomic interpretation.

---

# Governance Metadata

| Field | Value |
|---|---|
| Governance Standard | CORE_WORKING_RULES v1.6 |
| Gold Specification | FREEZE GOLD POPULATION PACKAGE SPECIFICATION v1.0 |
| Discussion Reference | PP Discussion depth and format example.md |
| Decision Status | APPROVED / LOCKED |
| Artifact Status | GOLD |
| Boundary | Required in final production response and maintained in artifact scope/exclusion sections |
| Evidence Basis | Project Source Files; no silent substitution with external evidence |

---

# Version Control

| Version | Date | Change |
|---|---|---|
| 1.0.0 | 2026-08-09 | Initial Gold production after approved/locked PP-0189 Decision Batch. |

---

# Change History

## 1.0.0

Initial release.

Scope locked around **molecular-report literacy** rather than:

- NGS methodology;
- variant interpretation;
- individual biomarker testing;
- treatment selection.

The package explicitly preserves the ownership boundaries with PP-0187, PP-0181–PP-0186, PP-0190, and PP-0191.

---

# Final Status

**GOLD — READY FOR INTEGRATION**
