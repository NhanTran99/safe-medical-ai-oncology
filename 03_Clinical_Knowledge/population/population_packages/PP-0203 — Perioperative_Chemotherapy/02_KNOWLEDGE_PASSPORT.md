# 02_KNOWLEDGE_PASSPORT.md

# Knowledge Passport

## Identity

| Field | Value |
|---|---|
| KP ID | KP-PP-0203 |
| PP ID | PP-0203 |
| Title | Perioperative Chemotherapy |
| Version | 1.0.0 |
| Status | GOLD — READY FOR INTEGRATION |
| Clinical Domain | Treatment / Systemic Therapy / Curative-Intent Multimodality Treatment |
| Audience | Patients, caregivers, and general oncology learners |
| Language | English source artifact; patient-facing plain-language style |

---

# Knowledge Classification

## Knowledge Type

Patient-facing clinical education / gastric-cancer treatment-strategy literacy.

## Atomic Clinical Question

> **What is perioperative chemotherapy in gastric cancer, why is chemotherapy given before and after surgery, who may be considered for this strategy, and how should the sequence be understood?**

## Primary Function

This PP is a **treatment-strategy node** between general treatment/surgical knowledge and downstream systemic-treatment packages.

It teaches:

- what perioperative chemotherapy means;
- why systemic therapy is integrated around surgery;
- how the preoperative and postoperative components fit together;
- why surgery remains central;
- what evidence supports the strategy;
- why FLOT is an important contemporary regimen example;
- how pathology and recovery influence postoperative management;
- how perioperative therapy differs from adjacent treatment concepts.

It does not own detailed regimen prescribing, detailed surgical technique, or individualized treatment selection.

---

# Patient Journey Classification

| Dimension | Classification |
|---|---|
| Primary journey stage | Treatment planning / Curative-intent multimodality treatment |
| Secondary journey stage | Perioperative systemic therapy |
| Decision point | Understanding why chemotherapy is given before and after surgery |
| Typical trigger | Patient with localized/resectable gastric cancer is discussing treatment around planned surgery |
| Downstream need | Regimen-specific, adjuvant, neoadjuvant, radiation, targeted-therapy, or immunotherapy packages |

---

# Intended Runtime Usage

## Primary Runtime Use

Retrieve when a user asks:

- “What is perioperative chemotherapy?”
- “Why do I need chemotherapy before stomach-cancer surgery?”
- “Why do I need chemotherapy after surgery if I already had it before?”
- “What does perioperative mean?”
- “Is FLOT the same as perioperative chemotherapy?”
- “What is the difference between perioperative and adjuvant chemotherapy?”
- “What is the difference between perioperative and neoadjuvant treatment?”
- “Why is chemotherapy given around surgery?”
- “What happens after chemotherapy before surgery?”
- “What happens after surgery?”
- “Can chemotherapy affect whether I can have surgery?”
- “Why might my postoperative treatment change after pathology?”

## Secondary Runtime Use

Retrieve when a patient needs a conceptual treatment-sequence explanation before entering a regimen-specific or modality-specific package.

## Do Not Use as a Substitute For

- individualized treatment selection;
- FLOT prescribing;
- chemotherapy dosing;
- chemotherapy administration;
- detailed adjuvant therapy;
- detailed neoadjuvant therapy;
- detailed chemoradiation;
- metastatic/palliative systemic therapy;
- detailed biomarker interpretation;
- individualized pathology interpretation;
- individualized surgical planning.

---

# Retrieval / Runtime Relevance

## High-Priority Retrieval Terms

- perioperative chemotherapy
- perioperative systemic therapy
- chemotherapy before surgery
- chemotherapy after surgery
- preoperative chemotherapy
- postoperative chemotherapy
- chemotherapy around surgery
- curative intent
- resectable gastric cancer
- localized gastric cancer
- gastric cancer surgery
- perioperative treatment
- treatment sequence
- treatment sequencing
- preoperative treatment
- postoperative treatment
- FLOT
- FLOT4
- MAGIC trial
- surgery alone
- pathology after surgery
- margin status
- lymph-node status
- lymphadenectomy
- treatment completion
- chemotherapy toxicity

## Terminology Distinction Terms

- perioperative
- adjuvant
- neoadjuvant
- chemoradiation
- systemic therapy
- palliative therapy
- curative intent
- resectable
- unresectable
- metastatic

## Patient Context Terms

- why chemotherapy before surgery
- why chemotherapy after surgery
- can I have surgery after chemotherapy
- what happens before surgery
- what happens after surgery
- pathology changes treatment
- chemotherapy side effects
- unable to complete chemotherapy

---

# Clinical Scope

## Core Ownership

PP-0203 owns the **perioperative treatment-strategy layer**.

It explains:

1. what perioperative chemotherapy is;
2. why systemic treatment is integrated around surgery;
3. the preoperative component;
4. reassessment before surgery;
5. the surgical interface;
6. the postoperative component;
7. the evidence supporting the strategy;
8. the contemporary role of FLOT as a regimen example;
9. treatment-completion concepts;
10. high-level toxicity;
11. terminology distinctions;
12. patient-facing questions and misconceptions.

## Supporting Ownership

PP-0203 may introduce:

- MAGIC and FLOT4 numerical outcomes;
- margin-free resection;
- pathological response;
- D1/D2 as postoperative-management context;
- biomarkers as treatment-selection context;
- selected perioperative immunotherapy evolution;
- multidisciplinary planning;
- clinical-trial relevance;
- nutritional and functional status.

These topics are not owned in detail.

## Explicit Exclusions

PP-0203 does not own:

- detailed FLOT regimen;
- FLOT dosing;
- FLOT cycle schedule;
- detailed adjuvant therapy;
- detailed neoadjuvant therapy;
- chemoradiation;
- palliative systemic therapy;
- metastatic treatment;
- targeted therapy;
- immunotherapy treatment algorithms;
- detailed biomarker testing;
- individualized treatment selection;
- detailed gastrectomy;
- detailed lymphadenectomy;
- detailed pathology;
- detailed toxicity management;
- dose modification;
- administration logistics.

---

# Authoritative Source Set

## 1. Gastric Cancer v2.2026 — NCCN Clinical Practice Guidelines in Oncology

Primary disease-specific guideline source.

Role in PP-0203:

- localized/resectable gastric-cancer treatment framework;
- perioperative systemic therapy;
- FLOT as preferred category-1 regimen in the relevant setting;
- postoperative treatment context;
- interaction between treatment, surgery, pathology, margins, and lymph-node dissection;
- selected biomarker-defined systemic-treatment contexts;
- distinction between chemotherapy, chemoradiation, and other systemic strategies.

Source status:

**Highest-priority disease-specific guideline within the supplied Source Materials.**

---

## 2. NCI — Gastric Cancer Treatment (PDQ)

Primary evidence source for the randomized evidence discussion.

Role:

- AIO-FLOT4;
- MAGIC;
- survival outcomes;
- margin-free resection;
- toxicity comparison;
- perioperative treatment evidence;
- surgical and postoperative treatment context.

Key evidence:

### AIO-FLOT4

716 patients with stage IB–III resectable gastric or gastroesophageal adenocarcinoma.

FLOT versus ECF/ECX.

Reported:

- median OS 50 versus 35 months;
- HR 0.77;
- margin-free resection 85% versus 78%.

### MAGIC

Stage II or higher gastric/lower-third esophageal adenocarcinoma.

Perioperative ECF versus surgery alone.

Reported:

- PFS HR 0.66;
- OS HR 0.75;
- 5-year OS 36.3% versus 23%.

---

## 3. American Cancer Society — Chemotherapy for Stomach Cancer

Patient-facing supporting source.

Role:

- chemotherapy as systemic treatment;
- timing of chemotherapy around surgery;
- patient-facing explanation of perioperative versus adjuvant concepts;
- broad treatment-side-effect awareness.

---

## 4. ESMO-ASCO Recommendations for a Global Curriculum in Medical Oncology — Edition 2023

Professional curriculum source.

The gastric-cancer section emphasizes:

- treatment guided by tumor stage, functional status, and biomarkers;
- multidisciplinary treatment;
- indications for surgery, perioperative, and adjuvant treatment;
- treatment sequencing;
- management of treatment-associated side effects.

Role:

**Professional framework supporting multidisciplinary sequencing and treatment-selection concepts.**

---

## 5. Other supplied gastric-cancer source materials

Supporting sources include:

- NCI Treatment of Stomach Cancer;
- ACS Stomach Cancer;
- ACS Immunotherapy for Stomach Cancer;
- NCCN Gastric Cancer v2.2026;
- ESMO-ASCO 2023.

Only claims relevant to PP-0203 are used.

---

# Evidence Classification

## Established / Guideline-Supported

- Perioperative systemic therapy is a recognized treatment framework for appropriately selected localized/resectable gastric cancer.
- FLOT has a preferred contemporary role in the relevant NCCN framework.
- Perioperative chemotherapy includes systemic treatment around surgery.
- Surgery remains central to curative-intent treatment for appropriate resectable disease.
- Postoperative management is influenced by pathology, margins, nodal findings, extent of lymphadenectomy, previous treatment, and recovery.
- Treatment sequencing is a multidisciplinary decision.
- Biomarkers can influence systemic-treatment selection in selected settings.

## Established / Randomized Evidence

- MAGIC supports perioperative chemotherapy versus surgery alone.
- FLOT4 supports FLOT versus ECF/ECX within perioperative treatment.
- FLOT4 reports improved median OS and margin-free resection with FLOT.

## Context-Dependent

- Exact regimen choice.
- Whether a patient is fit enough for perioperative chemotherapy.
- Whether postoperative treatment can be completed.
- How pathology changes the postoperative plan.
- Whether selected biomarker-defined perioperative systemic approaches are relevant.
- Whether chemoradiation is appropriate in a particular postoperative context.

## Not Owned by This PP

- detailed FLOT prescribing;
- detailed adjuvant therapy;
- detailed neoadjuvant therapy;
- detailed chemoradiation;
- palliative systemic therapy;
- targeted therapy;
- immunotherapy;
- biomarker testing;
- individualized treatment recommendations.

---

# Evidence Boundaries

## Evidence Boundary 1 — Strategy versus Regimen

**PP-0203**

> perioperative strategy.

**PP-0204**

> FLOT regimen.

---

## Evidence Boundary 2 — Perioperative versus Adjuvant

**PP-0203**

> systemic treatment before and after surgery.

**PP-0205**

> postoperative/adjuvant treatment.

---

## Evidence Boundary 3 — Perioperative versus Neoadjuvant

**PP-0203**

> preoperative treatment as one component of a broader perioperative sequence.

**PP-0206**

> neoadjuvant treatment.

---

## Evidence Boundary 4 — Perioperative Chemotherapy versus Chemoradiation

**PP-0203**

> chemotherapy around surgery.

**PP-0207**

> chemotherapy + radiation.

---

## Evidence Boundary 5 — Curative versus Palliative

**PP-0203**

> curative-intent localized/resectable disease.

**PP-0208**

> palliative systemic therapy.

---

# Knowledge Graph

## Prerequisites

- PP-0007 — Early vs Advanced Gastric Cancer.
- PP-0008 — Stages of Gastric Cancer.
- PP-0027 — Staging Work-up.
- PP-0028 — Treatment Overview.
- PP-0196 — Gastrectomy Principles.
- PP-0199 — Lymphadenectomy.

## Related

- PP-0197 — Subtotal Gastrectomy.
- PP-0198 — Total Gastrectomy.
- PP-0200 — D1 Lymphadenectomy.
- PP-0201 — D2 Lymphadenectomy.
- PP-0202 — Sentinel Lymph Node.
- PP-0207 — Chemoradiation.
- Biomarker testing packages.
- Multidisciplinary treatment planning.

## Next / Downstream

- PP-0204 — FLOT.
- PP-0205 — Adjuvant Therapy.
- PP-0206 — Neoadjuvant Therapy.
- PP-0207 — Chemoradiation.
- PP-0208 — Palliative Systemic Therapy.
- PP-0209–PP-0212 — Targeted therapy packages.
- PP-0213–PP-0216 — Immunotherapy packages.

---

# Runtime Decision Logic

When a user asks:

> “What is perioperative chemotherapy?”

Retrieve PP-0203.

When the user asks:

> “What is FLOT?”

Retrieve PP-0204.

When the user asks:

> “What chemotherapy is given after surgery?”

Use PP-0205 when the question is specifically about adjuvant therapy.

When the user asks:

> “What is treatment before surgery?”

Use PP-0206 when the question is specifically about neoadjuvant treatment.

When the user asks:

> “Should I receive FLOT?”

PP-0203 alone is insufficient for individualized decision-making.

The response must direct the user toward the cancer care team and relevant treatment-selection context.

---

# Safety / Uncertainty Rules

1. Never equate perioperative chemotherapy with a guarantee of cure.
2. Never state that every localized gastric-cancer patient requires perioperative chemotherapy.
3. Never state that every patient can tolerate FLOT.
4. Never interpret inability to complete all cycles as automatic treatment failure.
5. Never imply that preoperative response automatically determines whether surgery will occur.
6. Never infer an individualized regimen from stage alone.
7. Never convert biomarker status into an automatic treatment order.
8. Never treat postoperative treatment as mechanically predetermined before surgery.
9. Never provide dosing or administration from this PP.
10. Never replace individualized multidisciplinary clinical judgment.

---

# Governance Metadata

| Field | Value |
|---|---|
| Governance Standard | CORE_WORKING_RULES v1.7 |
| Gold Specification | FREEZE GOLD POPULATION PACKAGE SPECIFICATION v1.1 / applicable locked Gold production standard |
| Discussion Reference | PP Discussion depth and format example.md |
| Decision Status | APPROVED / LOCKED |
| Artifact Status | GOLD |
| Boundary | Core / Supporting / Explicitly Excluded / Delegated-to PP |
| Evidence Basis | Project Source Files |
| External Evidence | None introduced for production |
| Source-First | PASS |

---

# Version Control

| Version | Date | Change |
|---|---|---|
| 1.0.0 | 2026-08-09 | Initial Gold production after approved/locked PP-0203 Decision Batch. |

---

# Final Status

**GOLD — READY FOR INTEGRATION**
