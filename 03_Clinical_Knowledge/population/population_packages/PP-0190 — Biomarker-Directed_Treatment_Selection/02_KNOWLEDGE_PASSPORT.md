# 02_KNOWLEDGE_PASSPORT.md

# Knowledge Passport

## Identity

| Field | Value |
|---|---|
| KP ID | KP-PP-0190 |
| PP ID | PP-0190 |
| Title | Biomarker-Directed Treatment Selection |
| Version | 1.0.0 |
| Status | GOLD — READY FOR INTEGRATION |
| Clinical Domain | Treatment / Precision Oncology / Biomarker-Directed Therapy |
| Audience | Patients, caregivers, and general oncology learners |
| Language | English source artifact; patient-facing plain-language style |

---

# Knowledge Classification

## Knowledge Type

Patient-facing clinical education / biomarker-directed treatment-selection literacy.

## Atomic Clinical Question

> **How do biomarker results help determine which targeted treatment options may be considered for gastric adenocarcinoma?**

## Primary Function

This PP is the **clinical-application bridge node** between:

**biomarker testing/result interpretation**

and

**targeted-treatment application**.

It explains how a validated biomarker result may identify a clinically relevant targeted-treatment option while preserving the distinction between:

- biomarker detection;
- clinical relevance;
- actionability;
- treatment applicability;
- actual treatment decision.

It does not own detailed biomarker testing or detailed targeted-drug treatment management.

---

# Patient Journey Classification

| Dimension | Classification |
|---|---|
| Primary journey stage | Treatment planning / Precision oncology |
| Secondary journey stage | Advanced/recurrent/metastatic treatment selection where biomarker-directed options are most prominent |
| Decision point | Interpretable biomarker result is available and treatment options are being considered |
| Typical trigger | Patient receives a biomarker result and wants to understand whether it changes treatment options |
| Upstream need | Validated biomarker testing and molecular-report interpretation |
| Downstream need | Targeted-therapy or therapy-specific treatment package |
| Parallel branch | Biomarker-directed immunotherapy selection through PP-0191 |

---

# Intended Runtime Usage

## Primary Runtime Use

Retrieve when a user asks:

- “Does this biomarker result affect my treatment?”
- “What does HER2-positive mean for treatment?”
- “What does CLDN18.2-positive mean for treatment?”
- “Does an NTRK fusion mean there is a targeted drug?”
- “What treatment is linked to BRAF V600E?”
- “What does a RET fusion mean for treatment?”
- “How does my molecular result affect treatment?”
- “What does actionable mean in cancer?”
- “Does positive biomarker mean I need the drug?”
- “Why does treatment depend on the treatment line?”
- “Can targeted therapy be combined with chemotherapy?”
- “Why does my negative biomarker result matter?”
- “Why do several biomarkers need to be considered together?”

## Secondary Runtime Use

Retrieve when a user has understood a molecular report and needs a conceptual bridge to treatment application before entering a dedicated targeted-therapy package.

## Do Not Use as a Substitute For

- detailed biomarker testing;
- detailed biomarker scoring;
- molecular-report literacy;
- variant interpretation/classification;
- detailed NGS methodology;
- individualized treatment selection;
- drug dosing;
- treatment toxicity management;
- individualized prognosis;
- immunotherapy treatment-selection detail;
- individualized interpretation of a patient's biomarker result.

---

# Retrieval / Runtime Relevance

## High-Priority Retrieval Terms

- biomarker-directed treatment
- biomarker-guided treatment
- biomarker treatment selection
- targeted treatment selection
- actionable biomarker
- actionable alteration
- precision treatment
- precision oncology
- treatment eligibility
- treatment relevance
- treatment line
- first-line targeted therapy
- second-line targeted therapy
- later-line targeted therapy
- biomarker positive
- biomarker negative
- targeted therapy decision

## Gastric-Cancer Biomarker Retrieval Terms

- HER2-positive
- HER2-directed therapy
- trastuzumab
- trastuzumab deruxtecan
- CLDN18.2-positive
- zolbetuximab
- NTRK fusion
- TRK inhibitor
- BRAF V600E
- dabrafenib trametinib
- RET fusion
- selpercatinib
- FGFR2
- molecular alteration

## Parallel Immunotherapy Retrieval Terms

- PD-L1
- MSI-H
- dMMR
- TMB-H
- immunotherapy biomarker
- biomarker-directed immunotherapy

## Clinical Context Retrieval Terms

- advanced gastric cancer
- metastatic gastric cancer
- recurrent gastric cancer
- unresectable gastric cancer
- treatment line
- prior treatment
- performance status
- combination treatment
- molecular tumor board
- multidisciplinary treatment decision
- clinical trial

---

# Knowledge Graph

## Prerequisites

### Foundational Biomarker Testing

Provides the basic concept of biomarkers and why biomarker testing can contribute to personalized treatment selection.

### PP-0181 — HER2 Testing

Provides HER2 testing and result interpretation before HER2-directed treatment is considered.

### PP-0182 — MSI/MMR Testing

Provides MSI-H/dMMR result context for the separate immunotherapy-selection branch.

### PP-0183 — PD-L1 Testing

Provides PD-L1 result context for the separate immunotherapy-selection branch.

### PP-0184 — CLDN18.2 Testing

Provides CLDN18.2 testing and positivity context.

### PP-0185 — TMB

Provides TMB result context.

### PP-0186 — FGFR2 Testing

Provides FGFR2 result context.

### PP-0187 — NGS Biomarker Testing

Provides broader molecular-profiling context.

### PP-0189 — Genomic Test Results / How to Read a Molecular Report

Provides the report-literacy layer that precedes clinical application.

---

## Related

- PP-0191 — Biomarker Testing for Immunotherapy
- PP-0208 — Targeted Therapy in Gastric Cancer
- PP-0209 — HER2-targeted Therapy
- PP-0210 — CLDN18.2-targeted Therapy
- PP-0211 — Anti-angiogenic Therapy
- Companion Diagnostics
- Molecular Pathology
- Precision Oncology
- Molecular Tumor Board
- Clinical Trials
- ctDNA / Liquid Biopsy
- Molecular Classification

---

## Next / Downstream

### PP-0208 — Targeted Therapy in Gastric Cancer

Owns the broad targeted-therapy treatment domain.

### PP-0209 — HER2-targeted Therapy

Owns detailed HER2-targeted treatment.

### PP-0210 — CLDN18.2-targeted Therapy

Owns detailed CLDN18.2-targeted treatment.

### PP-0211 — Anti-angiogenic Therapy

Owns anti-angiogenic treatment.

### Additional Therapy-Specific Packages

Own detailed treatment-specific clinical application as assigned by the Project Coordinator's PP Package List.

---

# Clinical Scope

## Core Ownership

PP-0190 owns the **decision bridge from biomarker result to targeted-treatment relevance**.

It explains:

1. what biomarker-directed treatment selection means;
2. why detection does not automatically equal actionability;
3. why actionability is context-dependent;
4. how disease setting affects treatment relevance;
5. how treatment line affects treatment relevance;
6. how prior therapy affects subsequent options;
7. how multiple biomarkers may need to be integrated;
8. how positive results can open targeted-treatment pathways;
9. how negative results can close or reduce support for a specific pathway;
10. how representative actionable biomarkers connect to targeted treatment;
11. how HER2 status can direct HER2-targeted treatment consideration;
12. how CLDN18.2 status can direct zolbetuximab-containing treatment consideration;
13. how NTRK, BRAF V600E, and RET findings can support selected targeted-treatment consideration;
14. why PD-L1/MSI-H/dMMR/TMB belong primarily to the immunotherapy branch;
15. why targeted treatment can be combined with chemotherapy or other systemic treatment;
16. why the molecular report is not itself a treatment order;
17. what patients should ask the care team.

## Supporting Ownership

PP-0190 may introduce, without owning detailed methodology:

- companion-diagnostic concept;
- molecular tumor board / multidisciplinary interpretation;
- clinical-trial relevance;
- ctDNA-derived actionable findings at a conceptual level;
- treatment availability and feasibility as contextual considerations;
- the concept of tumor-agnostic or rare molecularly matched treatment in selected circumstances;
- the distinction between guideline-preferred and selected-circumstance options.

## Explicit Exclusions

PP-0190 does not own:

- detailed HER2 testing;
- detailed CLDN18.2 testing;
- detailed PD-L1 testing;
- detailed MSI/MMR testing;
- detailed TMB testing;
- detailed FGFR2 testing;
- NGS laboratory methodology;
- variant calling;
- variant classification;
- molecular-report literacy;
- detailed ctDNA biology;
- general treatment-by-stage algorithms;
- chemotherapy selection independent of biomarkers;
- surgery;
- radiotherapy;
- detailed immunotherapy selection;
- drug dosing;
- drug administration;
- detailed toxicity management;
- treatment response assessment;
- treatment resistance management;
- individualized treatment eligibility;
- individualized treatment recommendation.

---

# Authoritative Source Set

## 1. Gastric Cancer v2.2026 — NCCN Clinical Practice Guidelines in Oncology

Primary disease-specific source.

Supports:

- universal MSI/MMR testing;
- universal PD-L1 testing;
- HER2 testing in advanced/metastatic disease when documented/suspected;
- CLDN18.2 testing in advanced/metastatic disease when documented/suspected;
- consideration of NGS;
- HER2-directed treatment;
- CLDN18.2-directed treatment;
- selected NTRK, BRAF V600E, and RET-directed treatment;
- treatment-line dependence;
- performance-status dependence in later-line treatment;
- distinction between targeted and immunotherapy pathways;
- molecular findings and treatment-relevant alterations.

The current project copy is NCCN Guidelines Version 2.2026, dated 01/21/26.

## 2. NCI Treatment of Stomach Cancer

Supports:

- biomarker testing to help predict response to targeted therapy;
- targeted therapies used in stomach cancer;
- the patient-facing distinction between targeted treatment and broader cancer treatment.

## 3. NCI Gastric Cancer Treatment PDQ — Health Professional Version

Supports:

- treatment options by disease setting;
- biomarker-linked treatment examples;
- HER2-directed therapy;
- CLDN18.2-directed therapy;
- treatment evidence behind selected targeted approaches.

## 4. NCI Drugs Approved for Stomach (Gastric) Cancer

Supports the existence and regulatory treatment context of approved targeted therapies relevant to gastric cancer.

## 5. American Cancer Society — Stomach Cancer

Supports patient-facing explanations of:

- HER2-targeted therapy;
- CLDN18.2-targeted therapy;
- TRK inhibitors;
- RET-targeted therapy;
- BRAF-targeted therapy;
- combination of targeted therapy with chemotherapy.

## 6. American Cancer Society — Immunotherapy for Stomach Cancer

Used primarily to maintain the boundary between targeted-treatment selection and immunotherapy-selection pathways.

## 7. ESMO-ASCO Global Curriculum 2023

Supports the general professional principle that predictive biomarkers should be interpreted and used in forming treatment plans and that molecular information is part of broader clinical decision-making.

---

# Evidence Classification

## Established / Guideline-Supported

- Biomarker results can contribute directly to treatment selection.
- HER2-positive advanced gastric/EGJ adenocarcinoma has a guideline-supported HER2-directed treatment pathway.
- CLDN18.2-positive disease has a guideline-supported zolbetuximab-containing pathway in defined clinical settings.
- Selected NTRK gene fusions can support TRK-directed treatment in appropriate circumstances.
- BRAF V600E mutations can support BRAF/MEK-directed treatment in selected circumstances.
- RET gene fusions can support RET-directed treatment in selected circumstances.
- Treatment selection depends on disease setting and treatment line.
- Later-line treatment is dependent on prior therapy and performance status.
- Targeted therapy may be combined with chemotherapy.
- PD-L1, MSI-H/dMMR and TMB connect to immunotherapy pathways rather than being the primary targeted-therapy ownership of PP-0190.
- A biomarker result informs but does not independently determine the treatment decision.

## Context-Dependent

- Whether a particular actionable finding has a currently applicable treatment option.
- Whether the biomarker result applies to the current treatment line.
- Whether a combination regimen is appropriate.
- Whether a rare molecular alteration should direct treatment in a specific patient.
- Whether additional testing or confirmation is needed.
- Whether a treatment is available, feasible, or clinically appropriate for a particular patient.

## Not Owned by This PP

- detailed assay interpretation;
- biomarker-specific scoring;
- detailed drug selection algorithms;
- detailed regimen dosing;
- toxicity management;
- individualized treatment recommendation.

---

# Evidence-to-Use Translation

| Evidence concept | Runtime meaning |
|---|---|
| Biomarker result | Identify a biological feature relevant to treatment |
| Actionable alteration | Potentially meaningful treatment opportunity in a defined context |
| Treatment setting | Determines whether the option applies |
| Treatment line | Determines when the option may be used |
| Prior therapy | Can alter subsequent treatment options |
| Multiple biomarkers | May require integrated interpretation |
| Negative biomarker | May remove support for a specific targeted option |
| Targeted treatment | Acts on a defined molecular/biological feature |
| Treatment decision | Integrates biomarker plus complete clinical context |

---

# Governance Metadata

| Field | Value |
|---|---|
| Governance Standard | CORE_WORKING_RULES v1.7 |
| Gold Specification | FREEZE GOLD POPULATION PACKAGE SPECIFICATION v1.1 |
| Discussion Reference | PP Discussion depth and format example.md |
| Decision Status | APPROVED / LOCKED |
| Artifact Status | GOLD |
| Evidence Basis | Project Source Files; no silent substitution with unsupported external evidence |
| Boundary Requirement | Core / Supporting / Explicitly Excluded / Delegated-to PP |
| Package Rule | Four Markdown artifacts in one ZIP |

---

# Version Control

| Version | Date | Change |
|---|---|---|
| 1.0.0 | 2026-08-09 | Initial Gold production after PP-0190 Decision Batch approval and lock. |

---

# Final Status

**GOLD — READY FOR INTEGRATION**
