# 02_KNOWLEDGE_PASSPORT.md

# Knowledge Passport

## Identity

| Field | Value |
|---|---|
| KP ID | KP-PP-0192 |
| PP ID | PP-0192 |
| Title | Biomarker Testing for Immunotherapy |
| Version | 1.0.0 |
| Status | GOLD — READY FOR INTEGRATION |
| Clinical Domain | Treatment / Precision Oncology / Immunotherapy / Biomarker Testing |
| Audience | Patients, caregivers, and general oncology learners |
| Language | English source artifact; patient-facing plain-language style |
| Last Updated | 2026-08-09 |

---

# Knowledge Classification

## Knowledge Type

Patient-facing clinical education / immunotherapy biomarker-testing strategy.

## Atomic Clinical Question

> **Which biomarker testing is relevant when immunotherapy is being considered for gastric adenocarcinoma?**

## Primary Function

This PP is the **testing-strategy node between general biomarker/immunotherapy foundations and biomarker-specific interpretation or treatment application**.

It explains:

- why immunotherapy biomarker testing is needed;
- which biomarker domains are central;
- how PD-L1 and MSI/MMR relate;
- where TMB and NGS fit;
- why selected contextual biomarkers may appear in the same treatment-planning landscape;
- why specimen, timing, and adequacy matter;
- how testing connects to downstream treatment decisions.

It does not own detailed testing methodology or treatment selection.

---

# Patient Journey Classification

| Dimension | Classification |
|---|---|
| Primary journey stage | Treatment planning / Precision oncology |
| Secondary journey stage | Diagnosis / Molecular characterization |
| Decision point | Determining which biomarker information is relevant before immunotherapy-related treatment planning |
| Typical trigger | Gastric adenocarcinoma patient is being evaluated for an immunotherapy-containing treatment strategy |
| Upstream need | General immunotherapy and biomarker-testing foundations |
| Downstream need | Biomarker-specific interpretation and immunotherapy application |

---

# Intended Runtime Usage

## Primary Runtime Use

Retrieve when a user asks:

- “Which tests do I need before immunotherapy?”
- “Why do I need PD-L1 testing?”
- “Why do I need MSI or MMR testing?”
- “Are PD-L1 and MSI the same thing?”
- “If MSI is tested, do I still need PD-L1?”
- “What is TMB testing for immunotherapy?”
- “Does everyone need NGS before immunotherapy?”
- “Why are several biomarkers being tested?”
- “What does a positive immunotherapy biomarker mean?”
- “What does a negative biomarker result mean?”
- “What if there is not enough tissue for testing?”
- “Can blood testing replace tissue testing?”
- “What other biomarkers matter when immunotherapy is being considered?”

## Secondary Runtime Use

Retrieve when a user needs orientation before entering:

- PD-L1-specific testing/interpretation;
- MSI/MMR-specific testing/interpretation;
- TMB interpretation;
- NGS testing;
- MSI-H/dMMR immunotherapy application;
- PD-L1-guided immunotherapy.

## Do Not Use as a Substitute For

- individualized treatment selection;
- detailed PD-L1 scoring;
- detailed MSI/MMR interpretation;
- detailed TMB interpretation;
- detailed NGS methodology;
- detailed molecular-report interpretation;
- individualized prognosis;
- interpretation of an individual laboratory report;
- immunotherapy drug selection or dosing.

---

# Retrieval / Runtime Relevance

## High-Priority Retrieval Terms

- immunotherapy biomarker testing
- biomarker testing for immunotherapy
- gastric cancer immunotherapy testing
- immunotherapy biomarkers
- predictive biomarker
- treatment-selection biomarker
- biomarker before immunotherapy
- which tests before immunotherapy
- PD-L1 testing
- MSI testing
- MMR testing
- MSI-H
- dMMR
- PD-L1 and MSI
- PD-L1 versus MSI
- TMB
- TMB-H
- NGS
- molecular profiling
- companion diagnostic
- tumor tissue
- FFPE
- inadequate specimen
- negative biomarker
- biomarker result

## Gastric-Cancer Biomarker Retrieval Terms

- HER2
- CLDN18.2
- EBV
- PD-L1 CPS
- TAP
- MSI-H/dMMR
- TMB-high
- gastric adenocarcinoma
- EGJ adenocarcinoma
- precision oncology

## Clinical Context Retrieval Terms

- treatment planning
- immunotherapy selection
- biomarker-guided therapy
- companion diagnostic
- multidisciplinary care
- molecular pathology
- clinical trial
- tissue adequacy
- repeat testing
- discordant biomarker results

---

# Knowledge Graph

## Prerequisites

### PP-0014 — Immunotherapy for Gastric Adenocarcinoma

Foundational immunotherapy concept, treatment context, benefits, limitations, and general biomarker-guided selection.

### PP-0015 — Biomarker Testing for Gastric Adenocarcinoma

Foundational purpose and timing of biomarker testing and the role of biomarkers in personalized treatment.

### PP-0182 — MSI/MMR Testing

Detailed testing and interpretation of MSI/MMR.

### PP-0183 — PD-L1 Testing

Detailed PD-L1 testing, specimen, scoring, and interpretation.

### PP-0185 — Tumor Mutational Burden (TMB)

Detailed TMB definition, threshold, clinical relevance, and limitations.

### PP-0187 — NGS Biomarker Testing

Detailed NGS testing framework and molecular-profiling concepts.

---

## Related

- PP-0181 — HER2 Testing
- PP-0184 — CLDN18.2 Testing
- PP-0186 — FGFR2 Testing
- PP-0188 — Gastric Cancer Molecular Classification
- PP-0189 — Genomic Test Results / How to Read a Molecular Report
- PP-0168 — EBV-associated Gastric Cancer + EBV Testing
- Companion Diagnostics
- Molecular Pathology
- Liquid Biopsy / ctDNA
- Hereditary Gastric Cancer
- Genetic Testing

---

## Next / Downstream

### PP-0214 — MSI-H/dMMR Gastric Cancer and Immunotherapy

Clinical application of MSI-H/dMMR status to immunotherapy.

### PP-0215 — PD-L1-guided Immunotherapy

Clinical application of PD-L1 findings to immunotherapy.

### PP-0213 — Immune Checkpoint Inhibitors

Treatment-class and drug-level application.

### PP-0212 — Immunotherapy in Gastric Cancer

Broader immunotherapy treatment package.

---

# Clinical Scope

## Core Ownership

PP-0192 owns the **immunotherapy biomarker-testing strategy layer**.

It covers:

1. purpose of biomarker testing before immunotherapy;
2. predictive-biomarker concept;
3. PD-L1 as a core immunotherapy-relevant testing domain;
4. MSI/MMR as a core immunotherapy-relevant testing domain;
5. complementary relationship between PD-L1 and MSI/MMR;
6. TMB as a selected broader molecular-testing consideration;
7. NGS as a broader molecular-testing platform;
8. EBV as emerging/non-routine contextual information;
9. HER2 and CLDN18.2 as interacting treatment-relevant biomarkers;
10. timing and availability of testing;
11. specimen and adequacy concepts;
12. negative versus inadequate results;
13. conceptual tissue-versus-blood testing context;
14. companion-diagnostic concept;
15. transition from testing to downstream interpretation and treatment application.

## Supporting Ownership

PP-0192 may introduce, without owning detailed methodology:

- high-level PD-L1 scoring concepts such as CPS/TAP;
- high-level MSI versus MMR distinction;
- high-level TMB;
- high-level NGS;
- high-level companion-diagnostic concept;
- tissue-versus-blood molecular testing;
- multi-biomarker treatment-planning context;
- clinical-trial context;
- EBV as an emerging biomarker;
- HER2/CLDN18.2 as other treatment-relevant biomarkers.

## Explicit Exclusions

PP-0192 does not own:

- detailed PD-L1 biology;
- detailed PD-L1 IHC methodology;
- detailed CPS/TAP scoring;
- detailed MSI/MMR biology;
- detailed MSI/MMR laboratory methodology;
- detailed TMB methodology or threshold interpretation;
- NGS sequencing/bioinformatics;
- variant interpretation/classification;
- detailed EBV testing;
- HER2 testing;
- CLDN18.2 testing;
- molecular-report literacy;
- germline testing algorithms;
- immunotherapy drug mechanisms;
- drug-specific treatment;
- dosing;
- toxicity management;
- response/resistance algorithms;
- individualized treatment;
- individualized prognosis.

---

# Authoritative Source Set

## Primary Project Source Materials

### 1. Gastric Cancer v2.2026 — NCCN Clinical Practice Guidelines in Oncology

Primary disease-specific source for:

- universal MSI testing by PCR/NGS or MMR testing by IHC in newly diagnosed gastric cancer;
- PD-L1 IHC testing in newly diagnosed patients who are candidates for PD-1/PD-L1 inhibitors;
- FFPE tissue and specimen adequacy for PD-L1;
- companion-diagnostic framework;
- IHC/ISH/targeted PCR as preferred initial biomarker approaches;
- NGS as a selected broader testing approach;
- TMB assessment through NGS;
- immunotherapy-relevant treatment contexts for MSI-H/dMMR and TMB-H;
- selected treatment combinations in which biomarker information is integrated.

### 2. NCI — Treatment of Stomach Cancer

Supporting patient-facing source for:

- biomarker testing to help predict response to immunotherapy;
- biomarker-informed treatment context;
- integration of treatment decisions with the cancer care team.

### 3. American Cancer Society — Immunotherapy for Stomach Cancer

Supporting patient-facing source for:

- PD-L1-associated immunotherapy context;
- MSI-H/dMMR-associated immunotherapy context;
- broader biomarker-informed treatment examples.

### 4. American Cancer Society — Chemotherapy for Stomach Cancer

Supporting patient-facing source for:

- examples of treatment pathways incorporating PD-L1, MSI-H/dMMR, HER2 and CLDN18.2 information;
- the practical reality that multiple biomarkers may be considered together.

### 5. ESMO-ASCO Recommendations for a Global Curriculum in Medical Oncology — 2023

Supporting professional framework for:

- molecular testing as part of precision oncology;
- clinical interpretation of molecular information;
- assay and diagnostic concepts;
- multidisciplinary clinical decision-making.

### 6. NCI — Genetics of Gastric Cancer / Hereditary Gastric Cancer materials

Supporting context for hereditary implications of selected biomarker findings, especially when MSI/MMR findings may lead to further genetic assessment.

---

# Evidence Classification

## Established / Guideline-Supported

- Biomarker testing can contribute to prediction of response to selected immunotherapy approaches.
- Universal MSI testing by PCR/NGS or MMR testing by IHC is recommended for newly diagnosed gastric cancer in NCCN Version 2.2026.
- Universal PD-L1 IHC testing is recommended for newly diagnosed gastric-cancer patients who are candidates for PD-1/PD-L1 inhibitors.
- PD-L1 testing uses FFPE tumor tissue and a companion-diagnostic framework.
- NGS can provide broader molecular information and can include assessment of TMB and MSI.
- IHC/ISH/targeted gene PCR remain preferred initial approaches for specified biomarkers in NCCN guidance.
- MSI-H/dMMR and TMB-H are recognized immunotherapy-relevant contexts in the NCCN treatment framework.
- Biomarker results are integrated with broader clinical factors rather than functioning as automatic treatment orders.

## Context-Dependent

- Whether broader NGS is useful for an individual patient.
- Whether TMB testing adds clinically useful information.
- Whether additional testing is needed after an inadequate result.
- Whether tissue or blood-based molecular testing is appropriate in a particular setting.
- How multiple biomarkers should be integrated into an individual treatment decision.
- Whether a companion diagnostic is required for a particular treatment context.

## Emerging / Not Routine

- EBV as an immunotherapy-relevant biomarker in gastric cancer.

The current project Registry separately identifies EBV-associated gastric cancer and EBV testing as its own package and does not assign routine immunotherapy biomarker ownership to PP-0192.

---

# Governance Metadata

| Field | Value |
|---|---|
| Governance Standard | CORE_WORKING_RULES v1.7 |
| Gold Specification | FREEZE GOLD POPULATION PACKAGE SPECIFICATION v1.1 |
| Discussion Reference | PP Discussion depth and format example.md |
| Decision Status | APPROVED / LOCKED |
| Artifact Status | GOLD |
| Evidence Basis | Project Source Files; source-first production |
| Boundary Requirement | Final response must contain Core / Supporting / Explicitly Excluded / Delegated-to PP exactly once |

---

# Version Control

| Version | Date | Change |
|---|---|---|
| 1.0.0 | 2026-08-09 | Initial Gold production after approved/locked PP-0192 Decision Batch. |

---

# Change History

## 1.0.0

Initial Gold release.

The package was deliberately separated from:

- dedicated PD-L1 testing;
- dedicated MSI/MMR testing;
- TMB;
- NGS;
- molecular-report literacy;
- targeted-therapy biomarker testing;
- immunotherapy treatment application.

The package therefore functions as the **strategy layer connecting biomarker testing to downstream immunotherapy decision packages**.

---

# Final Status

**GOLD — READY FOR INTEGRATION**
