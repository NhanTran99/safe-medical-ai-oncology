# 02_KNOWLEDGE_PASSPORT — PP-0222 Management of Recurrent Gastric Cancer

## Identity

| Field | Value |
|---|---|
| KP ID | KP-PP-0222 |
| PP ID | PP-0222 |
| Title | Management of Recurrent Gastric Cancer |
| Version | 1.0.0 |
| Status | GOLD — READY FOR INTEGRATION |
| Last Updated | 2026-08-09 |

## Knowledge Classification

| Field | Classification |
|---|---|
| Clinical Domain | Gastric Cancer / Recurrence / Management |
| Domain Code | GC-REC-MGMT |
| Educational Level | Patient-facing clinical education with clinician-compatible precision |
| Clinical Complexity | High |
| Patient Journey Stage | After recurrence detection; treatment planning and ongoing management |
| Primary Question | How is recurrent gastric cancer managed after recurrence has been established? |
| Package Type | Atomic management-framework Population Package |
| Treatment Ownership | Strategic management framework; detailed modality ownership delegated |

## Intended Runtime Usage

This package is intended to provide a stable knowledge layer between recurrence detection and modality-specific management.

### Primary runtime uses

1. Explain the clinical transition from recurrence detection to management.
2. Organize recurrent disease into management-relevant patterns.
3. Explain treatment intent.
4. Explain the role of resectability and medical fitness.
5. Explain why previous treatment and biomarkers matter.
6. Explain the strategic roles of surgery, systemic therapy, selected chemoradiation, clinical trials and supportive/palliative care.
7. Support patient-facing questions about why treatment choices differ.
8. Provide routing to specialized downstream Population Packages.

### Retrieval intent

High-value retrieval concepts include:

- recurrent gastric cancer management;
- recurrence treatment;
- locoregional recurrence management;
- isolated recurrence surgery;
- unresectable recurrence;
- metastatic recurrence;
- systemic therapy after recurrence;
- prior treatment;
- performance status;
- biomarker-guided management;
- treatment intent;
- palliative care;
- supportive care;
- clinical trials.

## Retrieval / Runtime Relevance

### High-priority retrieval statements

- Recurrence management is distinct from recurrence detection.
- Isolated resectable locoregional recurrence may be considered for surgery in selected medically fit patients.
- Unresectable/recurrent/metastatic disease may enter systemic/palliative management.
- Prior therapy and performance status influence subsequent treatment.
- Biomarkers may influence treatment selection.
- Treatment goals and patient preferences matter.
- Supportive and palliative care can be integrated with disease-directed therapy.

### Do-not-infer rules

The runtime system must not infer:

- resectability for an individual patient;
- a specific drug or regimen;
- an individual treatment line;
- an individual prognosis;
- that recurrence necessarily means metastatic disease;
- that best supportive care means abandonment of active care;
- that a biomarker result alone determines treatment.

## Clinical Scope

### Core

Management of established recurrent gastric cancer as an overall clinical decision framework: treatment intent; recurrence-pattern-informed management; assessment of resectability and medical fitness; selected local treatment/surgery; unresectable recurrence; metastatic recurrence as a management branch; systemic therapy at strategic level; selected chemoradiation; biomarker-informed management; prior-treatment context; performance status and comorbidity; clinical trials; treatment reassessment/change; patient goals; shared decision-making; quality of life; multidisciplinary decision-making; and integration of palliative/supportive care.

### Supporting

Definitions and interfaces from recurrence detection, response assessment, imaging, pathology/biomarker testing, treatment history, nutrition/functional status, and patient-facing explanations needed to understand the management framework.

### Explicitly Excluded

Detailed systemic regimens/dosing; detailed targeted or immunotherapy algorithms; detailed biomarker testing/NGS or variant interpretation; detailed surgery/lymphadenectomy technique; radiation planning; RECIST/iRECIST; detailed imaging methodology; detailed metastatic/peritoneal disease packages; HIPEC/PIPAC; detailed palliative or best-supportive-care protocols; detailed toxicity algorithms; detailed MDT workflow; individualized treatment or prognostic recommendations.

### Delegated

PP-0208 Palliative Systemic Therapy; PP-0209 Targeted Therapy in Gastric Cancer; PP-0210 HER2-targeted Therapy; PP-0211 CLDN18.2-targeted Therapy; PP-0212 Anti-angiogenic Therapy; PP-0213 Immunotherapy in Gastric Cancer; PP-0214 Immune Checkpoint Inhibitors; PP-0215 MSI-H/dMMR Gastric Cancer and Immunotherapy; PP-0216 PD-L1-guided Immunotherapy; PP-0217 Response Assessment; PP-0218 RECIST-based Assessment; PP-0219 Post-treatment Imaging; PP-0223 Metastatic Gastric Cancer; PP-0224 Peritoneal Carcinomatosis; PP-0225 Peritoneal Carcinoma as Only Disease; PP-0226 HIPEC; PP-0227 Palliative Care; PP-0228 Best Supportive Care; PP-0231 Treatment-related Toxicity and Supportive Care; PP-0232 Multidisciplinary Management; and relevant dedicated surgery, pathology, biomarker and radiation packages.

## Knowledge Units

### KU-01 — Recurrence-to-management transition

**Concept:** Management begins after recurrence has been clinically established.

**Runtime interpretation:** Route detection questions to PP-0221; route treatment-strategy questions here.

### KU-02 — Recurrence pattern

**Concept:** Localized/locoregional, unresectable, metastatic and peritoneal patterns can require different strategies.

**Safety:** Never collapse all recurrence into one treatment pathway.

### KU-03 — Treatment intent

**Concept:** Management may aim at local control, disease control, symptom relief, quality-of-life preservation or selected curative intent.

### KU-04 — Resectability

**Concept:** Selected isolated locoregional recurrence may be considered for surgery when resectable and the patient is medically fit.

### KU-05 — Medical fitness

**Concept:** Performance status, comorbidity, organ function, nutrition and previous toxicity affect treatment suitability.

### KU-06 — Previous treatment

**Concept:** Previous surgery, systemic therapy and radiation influence subsequent options.

### KU-07 — Systemic therapy

**Concept:** Systemic treatment is a major branch for unresectable or metastatic recurrence, but detailed regimens belong to PP-0208 and therapy-specific packages.

### KU-08 — Biomarker-informed management

**Concept:** HER2, CLDN18.2, PD-L1 and MSI/MMR status may affect treatment pathways when relevant.

### KU-09 — Selected chemoradiation

**Concept:** Selected locally unresectable recurrence may be considered for chemoradiation when appropriate.

### KU-10 — Clinical trials

**Concept:** Trials may provide appropriate options for selected patients.

### KU-11 — Reassessment loop

**Concept:** Management changes according to response, progression, toxicity, health status and patient goals.

### KU-12 — Palliative/supportive care

**Concept:** Palliative and supportive care are active management components and may be delivered alongside anticancer treatment.

### KU-13 — Shared decision-making

**Concept:** Expected benefit, burden, uncertainty, alternatives and patient preferences should be considered.

### KU-14 — MDT interface

**Concept:** Complex recurrence management benefits from multidisciplinary review.

## Evidence Classification

### Established / guideline-supported

- Recurrence management is a distinct pathway from surveillance and recurrence detection.
- NCCN provides a dedicated recurrence pathway.
- Selected isolated locoregional recurrence may be considered for surgery when resectable and medically fit.
- Unresectable/recurrent/metastatic disease may require palliative management.
- Systemic therapy is a major treatment component where local therapy is not indicated.
- Subsequent systemic therapy depends on prior therapy and performance status.
- Biomarker testing can influence advanced/recurrent treatment selection.
- Selected locally unresectable disease may be considered for chemoradiation.
- Best supportive care is a recognized management option.
- Multidisciplinary review is an important decision principle.

### Context-dependent

- Re-resection.
- Chemoradiation.
- Systemic therapy.
- Biomarker-directed treatment.
- Clinical trial enrollment.
- Peritoneal-directed management.
- Intensity of treatment.
- Treatment continuation or change.
- Primary supportive-care strategy.

### Emerging / update-sensitive

- New biomarker-directed therapies.
- Novel combinations.
- Molecular reassessment strategies.
- ctDNA-guided treatment adaptation.
- Experimental local therapies.

These must not be converted into universal standards without supporting project evidence.

## Authoritative Sources

| Source | Use | Authority |
|---|---|---|
| NCCN Gastric Cancer v2.2026 | GAST-7/GAST-8/GAST-9; GAST-A/B/E/F/G/J; 2026 project copy | Primary guideline source |
| NCCN Gastric Cancer v2.2025 JNCCN | GAST-8/GAST-9/GAST-F; recurrent/unresectable/metastatic pathway and systemic therapy principles | Supporting guideline source |
| NCI Treatment of Stomach Cancer | Treatment overview; treatment planning considers stage, health, preferences, goals, options and side effects | Patient-facing supporting source |
| NCI Gastric Cancer Treatment PDQ | Treatment evidence and clinical context for gastric cancer | Supporting evidence source |
| CORE_WORKING_RULES v1.7 | WR-009, WR-010A-C, WR-011/011A, WR-012-014 | Governance authority |
| FREEZE GOLD POPULATION PACKAGE SPECIFICATION v1.1 | Four-artifact structure, Gold depth, evidence traceability, QA and Knowledge Graph | Structural authority |
| PP Discussion depth and format example | PP-0112 discussion used as format/depth reference | Discussion reference |
| PP Registry.xlsx | PP-0222 identity and adjacent package boundaries | Scope/registry source |

## Governance Metadata

| Field | Value |
|---|---|
| Governance Authority | CORE_WORKING_RULES v1.7 |
| Structural Authority | FREEZE GOLD POPULATION PACKAGE SPECIFICATION v1.1 |
| Discussion Reference | PP Discussion depth and format example |
| Scope/Registry | PP Registry.xlsx |
| Primary Clinical Guideline | NCCN Gastric Cancer v2.2026 project source |
| Supporting Clinical Source | NCI Treatment of Stomach Cancer |
| Evidence Package | 03_PRIMARY_EVIDENCE_PACKAGE.md |
| QA Package | 04_QA_REPORT.md |
| Gold Depth Rule | Absolute minimum relative to approved Gold references |
| Boundary Rule | One clean final-response declaration; artifact scope remains consistent |
| Execution Rule | Approved + Locked → immediate four-artifact production |

## Knowledge Graph

### Prerequisites

PP-0220, PP-0221, PP-0217, PP-0218, PP-0219, relevant pathology/biomarker packages.

### Related

PP-0208, PP-0209–PP-0216, PP-0223–PP-0228, PP-0231, PP-0232.

### Downstream routing

- Detailed systemic therapy → PP-0208.
- Targeted therapy → PP-0209–PP-0212.
- Immunotherapy → PP-0213–PP-0216.
- Response assessment → PP-0217.
- RECIST → PP-0218.
- Post-treatment imaging → PP-0219.
- Metastatic disease → PP-0223.
- Peritoneal disease → PP-0224/0225.
- HIPEC → PP-0226.
- Palliative care → PP-0227.
- Best supportive care → PP-0228.
- Toxicity → PP-0231.
- MDT workflow → PP-0232.

## Boundary Map

### Upstream handoff

**PP-0221 Recurrence Detection**

Owns identification/characterization of recurrence.

**PP-0222**

Owns the management decision framework after recurrence is established.

### Downstream handoff

**PP-0222**

Owns strategic management selection.

**Therapy-specific PPs**

Own detailed treatment modality knowledge.

### Anti-duplication principle

The package may name or contextualize a treatment modality when necessary to explain the management framework, but it must not reproduce the detailed content owned by the downstream package.

## Safety / Runtime Rules

1. Do not convert a general framework into individualized treatment advice.
2. Do not recommend a specific regimen based on a single biomarker.
3. Do not infer resectability from a narrative description.
4. Do not infer treatment intent from recurrence status alone.
5. Do not equate metastatic disease with “no treatment.”
6. Do not equate supportive care with cessation of care.
7. Do not present current regimen lists as permanent standards.
8. Route detailed modality questions to the designated PP.
9. Use the current project guideline source before generic knowledge.
10. If the project source does not support a claim, mark the evidence gap rather than filling it silently.

## Boundary

Core = Management of established recurrent gastric cancer as an overall clinical decision framework: treatment intent; recurrence-pattern-informed management; assessment of resectability and medical fitness; selected local treatment/surgery; unresectable recurrence; metastatic recurrence as a management branch; systemic therapy at strategic level; selected chemoradiation; biomarker-informed management; prior-treatment context; performance status and comorbidity; clinical trials; treatment reassessment/change; patient goals; shared decision-making; quality of life; multidisciplinary decision-making; and integration of palliative/supportive care.

Supporting = Definitions and interfaces from recurrence detection, response assessment, imaging, pathology/biomarker testing, treatment history, nutrition/functional status, and patient-facing explanations needed to understand the management framework.

Explicitly Excluded = Detailed systemic regimens/dosing; detailed targeted or immunotherapy algorithms; detailed biomarker testing/NGS or variant interpretation; detailed surgery/lymphadenectomy technique; radiation planning; RECIST/iRECIST; detailed imaging methodology; detailed metastatic/peritoneal disease packages; HIPEC/PIPAC; detailed palliative or best-supportive-care protocols; detailed toxicity algorithms; detailed MDT workflow; individualized treatment or prognostic recommendations.

Delegated-to PP = PP-0208 Palliative Systemic Therapy; PP-0209 Targeted Therapy in Gastric Cancer; PP-0210 HER2-targeted Therapy; PP-0211 CLDN18.2-targeted Therapy; PP-0212 Anti-angiogenic Therapy; PP-0213 Immunotherapy in Gastric Cancer; PP-0214 Immune Checkpoint Inhibitors; PP-0215 MSI-H/dMMR Gastric Cancer and Immunotherapy; PP-0216 PD-L1-guided Immunotherapy; PP-0217 Response Assessment; PP-0218 RECIST-based Assessment; PP-0219 Post-treatment Imaging; PP-0223 Metastatic Gastric Cancer; PP-0224 Peritoneal Carcinomatosis; PP-0225 Peritoneal Carcinoma as Only Disease; PP-0226 HIPEC; PP-0227 Palliative Care; PP-0228 Best Supportive Care; PP-0231 Treatment-related Toxicity and Supportive Care; PP-0232 Multidisciplinary Management; and relevant dedicated surgery, pathology, biomarker and radiation packages.

## Version Control

| Version | Date | Change |
|---|---|---|
| 1.0.0 | 2026-08-09 | Initial Gold Knowledge Passport after locked Decision Batch |

## Change History

No post-lock changes.

## Final Status

**GOLD — READY FOR INTEGRATION**
