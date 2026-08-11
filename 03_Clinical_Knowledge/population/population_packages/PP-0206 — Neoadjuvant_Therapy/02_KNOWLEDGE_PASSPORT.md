# 02_KNOWLEDGE_PASSPORT.md

# Knowledge Passport

## Identity

| Field | Value |
|---|---|
| KP ID | KP-PP-0206 |
| PP ID | PP-0206 |
| Title | Neoadjuvant Therapy |
| Version | 1.0.0 |
| Status | GOLD — READY FOR INTEGRATION |
| Clinical Domain | Treatment / Multimodality Gastric Cancer Therapy |
| Audience | Patients, caregivers, and general oncology learners |
| Language | English source artifact; patient-facing plain-language style |

---

# Knowledge Classification

## Knowledge Type

Patient-facing clinical education / treatment-sequencing strategy.

## Atomic Clinical Question

> **What is neoadjuvant therapy in gastric cancer, why may treatment be given before definitive surgery, how does it fit within the overall treatment sequence, and how are response, resectability, tumor biology, and patient fitness integrated into this strategy?**

## Primary Function

PP-0206 is the **preoperative-treatment strategy node** in the gastric-cancer knowledge graph.

It teaches:

- what treatment before surgery means;
- why it may be selected;
- how it differs from perioperative and adjuvant therapy;
- how preoperative treatment connects to restaging and surgery;
- why selected MSI-H/dMMR tumors may have a neoadjuvant immunotherapy pathway;
- how patients should understand response and uncertainty.

It does not own the individual treatment regimen.

---

# Patient Journey Classification

| Dimension | Classification |
|---|---|
| Primary journey stage | Treatment planning / Preoperative treatment |
| Secondary journey stage | Treatment response / Surgical preparation |
| Decision point | Selection and interpretation of treatment before definitive surgery |
| Typical trigger | Patient with potentially resectable gastric cancer is being considered for treatment before surgery |
| Upstream need | Accurate staging, pathology, biomarker context, resectability assessment |
| Downstream need | Response assessment, surgical evaluation, postoperative strategy |

---

# Intended Runtime Usage

## Primary Runtime Use

Retrieve when a user asks:

- “What is neoadjuvant therapy?”
- “Why do I need treatment before surgery?”
- “Why am I getting chemotherapy before my stomach surgery?”
- “Does neoadjuvant treatment mean my cancer cannot be removed?”
- “What is the difference between neoadjuvant and adjuvant treatment?”
- “What is the difference between neoadjuvant and perioperative treatment?”
- “What happens after treatment before surgery?”
- “Why do I need another scan before surgery?”
- “What does pathologic response mean after preoperative treatment?”
- “Can immunotherapy be given before surgery?”
- “Why does MSI-H/dMMR matter before surgery?”
- “If the tumor disappears, do I still need surgery?”
- “What if the tumor does not shrink?”

## Secondary Runtime Use

Retrieve when a user needs orientation before:

- perioperative chemotherapy;
- FLOT;
- immunotherapy;
- response assessment;
- surgery;
- postoperative/adjuvant therapy.

## Do Not Use as a Substitute For

- individualized treatment prescription;
- chemotherapy regimen selection;
- FLOT regimen interpretation;
- detailed immunotherapy selection;
- biomarker testing interpretation;
- detailed imaging interpretation;
- formal response criteria;
- surgical planning;
- metastatic/recurrent treatment.

---

# Retrieval / Runtime Relevance

## High-Priority Retrieval Terms

- neoadjuvant therapy
- neoadjuvant treatment
- preoperative therapy
- preoperative treatment
- treatment before surgery
- chemotherapy before surgery
- immunotherapy before surgery
- gastric cancer before surgery
- treatment sequencing
- resectable gastric cancer
- resectability
- perioperative treatment
- perioperative chemotherapy
- preoperative chemotherapy
- surgery after chemotherapy

## Evidence Retrieval Terms

- MAGIC
- FLOT4
- perioperative chemotherapy
- ECF
- ECF/ECX
- FLOT
- stage IB
- stage II
- stage III
- resectable
- margin-free resection

## Biomarker / Immunotherapy Retrieval Terms

- MSI-H
- dMMR
- neoadjuvant immunotherapy
- perioperative immunotherapy
- NEONIPIGA
- nivolumab
- ipilimumab
- pembrolizumab
- pathologic complete response
- pathologic response

## Response Retrieval Terms

- response assessment
- restaging
- CT
- PET/CT
- EGD
- biopsy
- persistent local disease
- new metastatic disease
- complete response
- tumor regression

---

# Runtime Decision Logic

## Rule 1 — Timing

If the user asks about treatment **before surgery**, retrieve PP-0206.

## Rule 2 — Perioperative

If the user asks about the complete chemotherapy strategy **before and after surgery**, retrieve PP-0203.

## Rule 3 — FLOT

If the user asks “What is FLOT?”, retrieve PP-0204.

## Rule 4 — Postoperative

If the user asks about treatment **after definitive surgery to reduce recurrence risk**, retrieve PP-0205.

## Rule 5 — Biomarker Testing

If the user asks how MSI/MMR or another biomarker is tested, route to the relevant biomarker-testing PP.

## Rule 6 — Immunotherapy

If the user asks about a specific immunotherapy drug/regimen, route to the dedicated immunotherapy PP.

## Rule 7 — Response Assessment

If the user asks how response is formally measured, route to the response-assessment PP.

## Rule 8 — Surgery

If the user asks how gastrectomy or lymphadenectomy is performed, route to the surgical PP.

## Rule 9 — Recurrence/Metastatic Disease

If the user asks about treatment after progression or metastatic disease, route downstream.

---

# Semantic Guardrails

## Guardrail 1

Neoadjuvant therapy is defined by **timing before definitive surgery**.

## Guardrail 2

Neoadjuvant therapy is not synonymous with chemotherapy.

## Guardrail 3

Neoadjuvant therapy is not synonymous with FLOT.

## Guardrail 4

Perioperative therapy includes both preoperative and postoperative treatment.

## Guardrail 5

Adjuvant therapy occurs after definitive surgery.

## Guardrail 6

Treatment before surgery does not automatically mean the disease is unresectable.

## Guardrail 7

Not every gastric cancer requires neoadjuvant therapy.

## Guardrail 8

MSI-H/dMMR is a specialized branch of current neoadjuvant/perioperative immunotherapy guidance, not a universal rule.

## Guardrail 9

Pathologic complete response is a response endpoint, not a guarantee of cure.

## Guardrail 10

Radiologic complete response does not automatically eliminate the need for surgical assessment.

---

# Evidence Hierarchy

## Level I — Current Gastric-Cancer Guideline

### NCCN Gastric Cancer v2.2026

Primary source for:

- treatment sequencing;
- perioperative systemic therapy;
- neoadjuvant/perioperative immunotherapy;
- MSI-H/dMMR treatment context;
- response assessment;
- surgical pathway after systemic therapy.

NCCN identifies perioperative systemic therapy as category 1 for resectable T2 or higher disease in medically fit patients and identifies selected neoadjuvant/perioperative immunotherapy for MSI-H/dMMR tumors.

## Level I — NCI PDQ

Primary evidence synthesis source for:

- FLOT4;
- MAGIC;
- treatment sequencing;
- trial-level outcomes.

## Level II — ACS

Patient-facing support for:

- preoperative/neoadjuvant terminology;
- perioperative treatment;
- staging before surgery;
- MSI-H/dMMR treatment pathway.

## Level II — ESMO-ASCO

Professional oncology framework for:

- multidisciplinary treatment sequencing;
- patient treatment planning;
- multimodality care;
- treatment selection across the disease continuum.

---

# Evidence Status

## Established / Guideline-Supported

- Neoadjuvant means treatment before surgery.
- Perioperative systemic therapy is an established treatment strategy in appropriate resectable gastric cancer.
- FLOT is a preferred category 1 perioperative systemic therapy in current NCCN guidance.
- Selected MSI-H/dMMR gastric tumors may receive neoadjuvant/perioperative immunotherapy in certain circumstances.
- Response is assessed after preoperative treatment.
- The role of surgery after complete response to neoadjuvant immunotherapy can be uncertain in selected MSI-H/dMMR settings.

## Randomized Evidence

- MAGIC supports perioperative chemotherapy compared with surgery alone.
- FLOT4 supports FLOT compared with ECF/ECX within a perioperative strategy.

## Context-Dependent

- Whether a patient should receive preoperative therapy.
- Which treatment modality should be used.
- Whether surgery remains appropriate after treatment.
- Whether additional treatment is required after surgery.
- How response should influence subsequent treatment.

## Not Owned

- Individual treatment prescription.
- Individual recurrence prediction.
- Individual survival prediction.
- Detailed toxicity management.

---

# Evidence Object Map

| Evidence Object | Role |
|---|---|
| MAGIC | Historical randomized evidence for perioperative chemotherapy containing preoperative therapy |
| FLOT4 | Modern randomized evidence for perioperative systemic therapy containing preoperative FLOT |
| NEONIPIGA | Phase II evidence for neoadjuvant immunotherapy in MSI-H/dMMR gastric/EGJ adenocarcinoma |
| Pembrolizumab phase II evidence | Neoadjuvant immunotherapy evidence in MSI-H/dMMR solid tumors, mostly colorectal |
| NCCN GAST-3/GAST-F | Current treatment sequencing and systemic therapy positioning |
| NCI PDQ | Trial-level evidence synthesis |
| ACS | Patient-facing explanation of preoperative/perioperative treatment |
| ESMO-ASCO | Multidisciplinary treatment-sequencing framework |

---

# Knowledge Graph

## Prerequisite

### PP-0027 — Staging Work-up

Stage and resectability are foundational.

### PP-0028 — Treatment Overview

Provides the overall treatment map.

### Biomarker Testing PPs

Provide the molecular information needed for selected targeted treatment pathways.

### PP-0195–PP-0201

Provide the surgical context that follows preoperative treatment.

---

## Related

### PP-0203 — Perioperative Chemotherapy

The closest strategy-level neighbor.

### PP-0204 — FLOT

Regimen-level neighbor.

### PP-0205 — Adjuvant Therapy

Postoperative strategy neighbor.

### PP-0191 — Biomarker Testing for Immunotherapy

Biomarker-selection neighbor.

### Immunotherapy PPs

Treatment-specific neighbors.

### Response Assessment PPs

Post-treatment evaluation neighbors.

---

## Next / Downstream

### Immediate

Response assessment / restaging.

### Then

Definitive surgical evaluation.

### Then

Surgery.

### Then

Adjuvant/postoperative treatment where applicable.

### Alternative branch

Progression or new metastatic disease → advanced/recurrent pathway.

---

# Clinical Boundary Matrix

| Topic | PP-0206 | Neighbor |
|---|---|---|
| Meaning of neoadjuvant therapy | CORE | — |
| Preoperative treatment rationale | CORE | — |
| Perioperative strategy | SUPPORTING | PP-0203 |
| FLOT regimen | EXCLUDED | PP-0204 |
| Adjuvant therapy | EXCLUDED | PP-0205 |
| Gastrectomy technique | EXCLUDED | PP-0196/0197 |
| D1/D2 technique | EXCLUDED | PP-0200/0201 |
| MSI/MMR testing | EXCLUDED | biomarker PP |
| Neoadjuvant immunotherapy concept | CORE-SUPPORTING | immunotherapy PP |
| Immunotherapy drug details | EXCLUDED | immunotherapy PP |
| Response assessment concept | SUPPORTING | response PP |
| RECIST methodology | EXCLUDED | response PP |
| Pathologic response concept | CORE-SUPPORTING | pathology/response PP |
| Recurrent/metastatic treatment | EXCLUDED | downstream PPs |

---

# Patient-Facing Retrieval Templates

## Template A — Definition

> “Neoadjuvant therapy is treatment given before definitive surgery.”

## Template B — Rationale

> “It may be used to treat cancer before surgery and as part of the overall strategy for controlling disease throughout the body.”

## Template C — Reassurance

> “Receiving treatment before surgery does not automatically mean that the cancer cannot be removed.”

## Template D — Response

> “Your doctors may reassess the cancer after treatment to determine whether it remains appropriate to proceed with surgery.”

## Template E — MSI-H/dMMR

> “Some MSI-H/dMMR gastric cancers have a specific pathway in which immunotherapy may be used before or around surgery.”

## Template F — FLOT

> “FLOT is a chemotherapy regimen that can be used in perioperative treatment; it is not another name for neoadjuvant therapy.”

---

# Retrieval Failure Modes

## Failure Mode 1

User asks:

> “Why do I get chemo before surgery?”

System retrieves only chemotherapy drug details.

### Correct behavior

Retrieve PP-0206 first.

Then route to PP-0203 or PP-0204 if the user asks regimen-specific questions.

---

## Failure Mode 2

User asks:

> “What is FLOT?”

System answers with neoadjuvant therapy.

### Correct behavior

Retrieve PP-0204.

---

## Failure Mode 3

User asks:

> “What is adjuvant therapy?”

System retrieves PP-0206.

### Correct behavior

Retrieve PP-0205.

---

## Failure Mode 4

User asks:

> “My MSI is high. Should I get immunotherapy before surgery?”

System should not give a universal yes.

### Correct behavior

Explain that MSI-H/dMMR status can create a neoadjuvant/perioperative immunotherapy pathway in selected patients, then route to biomarker/immunotherapy-specific knowledge and individualized clinical assessment.

---

## Failure Mode 5

User asks:

> “My scan shows complete response. Can I skip surgery?”

### Correct behavior

Explain that imaging response does not automatically establish absence of viable disease and that surgical assessment remains important. In selected MSI-H/dMMR neoadjuvant immunotherapy settings, the role of surgery after complete response may itself be uncertain.

---

## Failure Mode 6

User asks:

> “The tumor did not shrink. Does that mean treatment failed?”

### Correct behavior

Do not make a binary conclusion. Route through response and resectability assessment.

---

# Governance Metadata

| Field | Value |
|---|---|
| Governance Standard | CORE_WORKING_RULES v1.7 |
| Gold Specification | FREEZE GOLD POPULATION PACKAGE SPECIFICATION v1.1 |
| Discussion Reference | PP Discussion depth and format example.md |
| Decision Status | APPROVED / LOCKED |
| Artifact Status | GOLD |
| Source Basis | Project Source Files |
| External Research | Not used |
| Registry Status | PP-0206 confirmed as Neoadjuvant Therapy by Project Coordinator |

---

# Version Control

| Version | Date | Change |
|---|---|---|
| 1.0.0 | 2026-08-09 | Initial Gold production after approved/locked PP-0206 Decision Batch. |

---

# Final Status

**GOLD — READY FOR INTEGRATION**
