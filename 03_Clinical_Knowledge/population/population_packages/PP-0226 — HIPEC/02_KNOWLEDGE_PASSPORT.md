# 02_KNOWLEDGE_PASSPORT.md

# Knowledge Passport

## Identity

| Field | Value |
|---|---|
| Knowledge Passport ID | KP-PP-0226 |
| Population Package ID | PP-0226 |
| Title | HIPEC |
| Version | 1.0.0 |
| Status | Approved — GOLD |
| Clinical Domain | Treatment / Peritoneal Disease / Local-Regional Therapy |
| Population Wave | Wave 1 |
| Knowledge Product Type | Patient-facing clinical education node |

---

# Knowledge Classification

## Primary Knowledge Type

**Treatment-modality-specific clinical knowledge**

PP-0226 is a dedicated package about hyperthermic intraperitoneal chemotherapy as a local-regional treatment modality in gastric cancer with peritoneal disease.

It is not a general metastatic-gastric-cancer package and is not a general surgery package.

## Secondary Knowledge Types

- Patient education
- Treatment selection context
- Evidence interpretation
- Risk/benefit communication
- Clinical pathway knowledge
- Knowledge Graph treatment node

---

# Clinical Domain

## Primary Domain

**Treatment**

## Subdomains

- Peritoneal disease
- Local-regional therapy
- Cytoreductive treatment
- Intraperitoneal chemotherapy
- Surgical oncology interface
- Evidence-based treatment selection

---

# Patient Journey Classification

**Diagnosis / Staging → Systemic Treatment → Response Assessment → Specialized Treatment Selection → Local-Regional Treatment → Recovery → Surveillance**

PP-0226 occupies a specialized decision point after:

- documentation/characterization of peritoneal disease;
- systemic treatment;
- restaging;
- multidisciplinary reassessment.

It is therefore a downstream treatment-modality node rather than a first-line diagnostic node.

---

# Intended Runtime Usage

## Primary Uses

1. Explain what HIPEC is.
2. Explain why HIPEC may be discussed in selected gastric-cancer patients with peritoneal disease.
3. Explain the relationship between HIPEC and cytoreductive surgery.
4. Explain why selection is necessary.
5. Explain PCI and complete-cytoreduction concepts at a patient-facing level.
6. Explain current guideline positioning.
7. Explain the major evidence and its limitations.
8. Explain treatment burden and uncertainty.
9. Correct common misconceptions.
10. Support informed discussion with a multidisciplinary clinical team.

## Runtime Safety

The package must not be used to:

- declare an individual patient eligible for HIPEC;
- recommend HIPEC to an individual;
- interpret a patient's PCI without full clinical context;
- substitute for multidisciplinary tumor-board review;
- substitute for the original guideline or clinical-trial evidence;
- generate individualized survival estimates;
- provide technical surgical instructions.

---

# Retrieval / Runtime Relevance

## High-Priority Retrieval Concepts

- HIPEC
- hyperthermic intraperitoneal chemotherapy
- intraperitoneal chemotherapy
- cytoreductive surgery
- peritoneal metastasis
- peritoneal carcinoma
- gastric cancer
- gastric adenocarcinoma
- PCI
- complete cytoreduction
- GASTRIPEC-I
- CYTO-CHIP
- PERISCOPE II
- PIPAC
- multidisciplinary tumor board
- selected HIPEC
- peritoneal-only disease

## Retrieval Synonyms

- hyperthermic intraperitoneal chemotherapy
- hyperthermic intraperitoneal perfusion
- IC/HIPEC
- intraperitoneal chemotherapy
- CRS + HIPEC
- cytoreduction + HIPEC

---

# Clinical Scope

## Core

HIPEC as a treatment modality; conceptual rationale; relationship with cytoreductive surgery; selected treatment pathway; PCI and complete-cytoreduction context; evidence; risks; uncertainties; patient-facing decision support.

## Supporting

Systemic therapy before reassessment, restaging, disease-control context, extraperitoneal disease, fitness, quality of life, clinical-trial context, PIPAC distinction.

## Excluded

Detailed operative technique, exact HIPEC parameters, detailed drug dosing, PCI scoring, detailed imaging/response methodology, detailed toxicity management, individualized treatment decisions.

---

# Knowledge Units

## KU-01 — Definition

HIPEC is heated chemotherapy circulated within the peritoneal cavity, generally after cytoreductive surgery.

## KU-02 — Treatment Architecture

HIPEC is generally considered as part of a cytoreductive strategy rather than as a replacement for systemic treatment.

## KU-03 — Selection

Selection incorporates disease control, PCI, extraperitoneal disease, predicted complete cytoreduction, fitness, and multidisciplinary review.

## KU-04 — PCI

PCI describes peritoneal disease burden/distribution and is used as part of selection.

## KU-05 — Complete Cytoreduction

The current NCCN pathway links the selected HIPEC option to predicted complete cytoreduction.

## KU-06 — Evidence

Evidence includes observational, phase II, randomized phase III, and ongoing trial data.

## KU-07 — Evidence Uncertainty

The evidence is not uniformly positive for OS.

## KU-08 — Safety

HIPEC is a major treatment strategy with substantial potential morbidity.

## KU-09 — PIPAC

PIPAC is a distinct intraperitoneal approach and remains investigational in the supplied NCCN framework.

## KU-10 — Prophylactic HIPEC

Prophylactic IC/HIPEC/PIPAC in non-metastatic disease remains investigational.

## KU-11 — Patient Decision

The decision should incorporate benefit, uncertainty, treatment burden, quality of life, alternatives, and patient goals.

---

# Evidence Classification

## Established / Guideline-Supported

- Definition of HIPEC.
- Use with cytoreductive surgery.
- Selected use in appropriate peritoneal disease.
- Multidisciplinary discussion.
- PCI and complete-cytoreduction considerations.
- Current NCCN selected-use framework.
- PIPAC investigational status.
- Prophylactic HIPEC investigational status.

## Context-Dependent

- Patient suitability.
- Feasibility of complete cytoreduction.
- Meaning of PCI in the whole clinical context.
- Expected morbidity.
- Clinical-trial availability.
- Local expertise.
- Quality-of-life implications.

## Emerging / Investigational

- Broader indications.
- Higher-PCI use outside trials.
- Prophylactic use.
- PIPAC.
- Long-term comparative effectiveness under contemporary systemic therapy.

## Not Established / Excluded

- Universal HIPEC benefit.
- Guaranteed cure.
- PCI as a standalone eligibility rule.
- Routine prophylactic HIPEC.
- PIPAC as routine standard treatment.

---

# Authoritative Sources

## Primary

### 1. NCCN Gastric Cancer Version 2.2026

Role:

- direct disease-specific guideline;
- HIPEC definition;
- selection pathway;
- PCI threshold;
- complete-cytoreduction criterion;
- multidisciplinary requirement;
- CYTO-CHIP;
- GASTRIPEC-I;
- PERISCOPE II;
- PIPAC status.

The supplied NCCN source states that HIPEC is continuous circulation of heated sterile chemotherapy-containing solution after cytoreductive surgery and that selected patients with PCI ≤10 who are candidates for complete cytoreduction may have IC/HIPEC as an option.

## Supporting

### 2. NCCN Gastric Cancer Version 2.2025

Role:

- corroborating HIPEC definition;
- supporting evidence history;
- Badgwell phase II;
- Yang randomized phase III;
- GASTRIPEC-I;
- current selective-use interpretation.

### 3. PP-0225 Decision Batch / Gold package

Role:

- upstream peritoneal-only disease pathway;
- selection sequence;
- interface between systemic therapy, restaging, PCI and local-regional treatment.

### 4. PP-0224 Decision/Gold package

Role:

- peritoneal carcinomatosis disease-state boundary.

### 5. PP Discussion depth and format example

Role:

- Decision Batch structure;
- Gold reasoning depth;
- boundary reasoning;
- Knowledge Graph treatment;
- evidence maturity framework.

### 6. FREEZE GOLD POPULATION PACKAGE SPECIFICATION v1.1

Role:

- four-artifact structure;
- Gold depth;
- CKO/KP/EP/QA requirements.

### 7. CORE_WORKING_RULES v1.7

Role:

- Source-First;
- Gold depth;
- immediate production;
- boundary;
- QA;
- user-controlled sequence.

---

# Governance Metadata

| Field | Value |
|---|---|
| Governance status | Locked |
| Source-first | Required |
| Decision Batch | Approved + Locked |
| Gold production | Required |
| Four artifacts | Required |
| ZIP | Required |
| Boundary | Required once in final response |
| QA final status | PASS — GOLD — READY FOR INTEGRATION |
| User-controlled sequence | Yes |
| Version | 1.0.0 |

---

# Knowledge Graph

## Prerequisite

- PP-0223 Metastatic Gastric Cancer
- PP-0224 Peritoneal Carcinomatosis
- PP-0225 Peritoneal Carcinoma as Only Disease
- PP-0217 Response Assessment
- PP-0219 Post-treatment Imaging
- Relevant surgery knowledge

## Related

- PP-0218 RECIST-based Assessment
- PP-0227 Palliative Care
- PP-0228 Best Supportive Care
- PP-0231 Treatment-related Toxicity and Supportive Care
- PP-0232 Multidisciplinary Management
- systemic-treatment packages
- surgery-specific packages
- clinical-trial package

## Downstream

- post-treatment recovery;
- surveillance;
- recurrence detection;
- long-term follow-up.

## Delegated

Detailed surgery, PCI scoring, imaging, RECIST, systemic regimens, toxicity management, palliative care, supportive care, surveillance and recurrence remain outside PP-0226.

---

# Boundary Map

| Topic | PP-0226 Ownership |
|---|---|
| Peritoneal carcinomatosis definition | Delegated to PP-0224 |
| Peritoneal-only disease pathway | Delegated to PP-0225 |
| HIPEC definition | Core |
| HIPEC rationale | Core |
| HIPEC + cytoreduction relationship | Core |
| PCI concept | Core/supporting |
| PCI scoring method | Excluded |
| Complete cytoreduction concept | Core |
| Cytoreductive surgery technique | Delegated |
| Systemic treatment before HIPEC | Supporting/context |
| Detailed systemic regimens | Delegated |
| Response assessment | Delegated |
| RECIST | Delegated |
| Imaging methodology | Delegated |
| CYTO-CHIP evidence | Core |
| Badgwell phase II evidence | Core |
| Yang randomized evidence | Core |
| GASTRIPEC-I | Core |
| PERISCOPE II | Core |
| PIPAC distinction | Supporting |
| Prophylactic HIPEC | Core boundary/evidence context |
| Postoperative toxicity management | Delegated |
| Palliative care | Delegated |
| Surveillance | Delegated |
| Recurrence detection | Delegated |
| MDT rationale | Core |
| MDT operating workflow | Delegated |

---

# Safety / Runtime Rules

1. Never interpret PCI alone as eligibility.
2. Never promise survival benefit.
3. Never describe HIPEC as a universal standard for all peritoneal metastases.
4. Never describe HIPEC as replacing systemic therapy.
5. Never treat a study-specific morbidity rate as an individual risk estimate.
6. Never treat PIPAC as equivalent to HIPEC.
7. Never turn the package into a surgical manual.
8. Preserve uncertainty when randomized evidence is mixed.
9. Distinguish observational association from randomized evidence.
10. Distinguish OS from PFS and other disease-control endpoints.
11. Avoid individualized treatment advice.
12. Direct patient-specific decisions to the treating multidisciplinary team.

---

# Version Control

| Version | Date | Change |
|---|---|---|
| 1.0.0 | 2026-08-09 | Initial Gold version after approved PP-0226 Decision Batch |

---

# Change History

- Initial PP-0226 scope approved and locked.
- Gold package generated without reopening decisions.
- Source-first clinical evidence anchored to supplied NCCN v2.2026/v2.2025 material.
- Boundary ownership aligned with PP-0224 and PP-0225.
- Evidence maturity explicitly preserved.

---

# Final Status

**Approved — GOLD**

**QA final status: PASS — GOLD — READY FOR INTEGRATION.**
