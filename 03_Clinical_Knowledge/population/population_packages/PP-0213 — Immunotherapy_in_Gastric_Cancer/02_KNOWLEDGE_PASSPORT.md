# 02_KNOWLEDGE_PASSPORT.md

# Knowledge Passport

## Identity

| Field | Value |
|---|---|
| KP ID | KP-PP-0213 |
| PP ID | PP-0213 |
| Title | Immunotherapy in Gastric Cancer |
| Version | 1.0.0 |
| Status | GOLD — READY FOR INTEGRATION |
| Clinical Domain | Treatment / Systemic Therapy / Immuno-Oncology |
| Audience | Patients, caregivers, general oncology learners, oncology clinicians |
| Language | English source artifact; patient-facing plain-language style |
| Decision Status | APPROVED / LOCKED |

---

# Knowledge Classification

## Knowledge Type

Patient-facing clinical education / gastric-cancer immunotherapy framework.

## Atomic Clinical Question

> **What is immunotherapy in gastric cancer, how does it work at a clinically understandable level, when can it be used, how do biomarkers and treatment setting affect its role, and what benefits and safety issues should patients understand?**

## Primary Function

PP-0213 is the **clinical umbrella node for immunotherapy** in the gastric-cancer knowledge graph.

It bridges foundational immunotherapy concepts and the specialized downstream packages for:

- immune checkpoint inhibitors;
- MSI-H/dMMR and immunotherapy;
- PD-L1-guided immunotherapy.

It is deliberately broader than a drug-specific package and narrower than a general tumor-immunology package.

## Secondary Function

It provides a reusable patient-facing explanation for questions such as:

- “What is immunotherapy?”
- “How does immunotherapy work?”
- “Why is my doctor combining immunotherapy with chemotherapy?”
- “Why does PD-L1 matter?”
- “Why does MSI-H matter?”
- “Can immunotherapy be given before surgery?”
- “Why can immunotherapy cause unusual side effects?”
- “Why can a scan look worse during immunotherapy?”

## Non-Function

PP-0213 is not:

- an individualized treatment selector;
- a prescribing guide;
- a checkpoint-inhibitor pharmacology manual;
- a biomarker-testing manual;
- an immune-related toxicity-management protocol;
- a response-assessment manual.

---

# Patient Journey Classification

| Dimension | Classification |
|---|---|
| Primary journey stage | Treatment selection / Systemic therapy |
| Secondary journey stage | Treatment delivery / Response monitoring / Safety |
| Major disease settings | Perioperative/neoadjuvant; unresectable locally advanced; recurrent; metastatic |
| Decision point | Understanding whether and why immunotherapy may be part of a gastric-cancer treatment plan |
| Typical trigger | New diagnosis requiring systemic-treatment education; biomarker results; treatment discussion; new symptoms during immunotherapy |
| Downstream need | Drug-specific checkpoint package, biomarker-specific treatment package, toxicity and response packages |

---

# Intended Runtime Usage

## Primary Retrieval Triggers

Retrieve PP-0213 when the user asks:

- “What is immunotherapy for stomach cancer?”
- “How does immunotherapy work?”
- “Is immunotherapy different from chemotherapy?”
- “Can immunotherapy be combined with chemotherapy?”
- “Why would gastric cancer need immunotherapy?”
- “Can immunotherapy be used before surgery?”
- “Can immunotherapy be used for metastatic gastric cancer?”
- “Why does PD-L1 matter?”
- “Does everyone need PD-L1 positive disease?”
- “What does MSI-H mean for immunotherapy?”
- “What are the main benefits of immunotherapy?”
- “What are the special side effects of immunotherapy?”
- “Can immunotherapy cause pseudoprogression?”

## Secondary Retrieval Triggers

Retrieve when the user needs a conceptual bridge before a more specific package:

**General immunotherapy**

→ **checkpoint inhibitors**

or

**biomarker**

→ **immunotherapy application**

or

**immunotherapy**

→ **toxicity / response assessment**

## Do Not Use as a Substitute For

- individualized immunotherapy selection;
- interpretation of a patient's exact PD-L1 CPS/TAP result;
- interpretation of a patient's MSI/MMR test;
- checkpoint inhibitor dosing;
- immune-related toxicity management;
- RECIST/iRECIST interpretation;
- treatment sequencing;
- individualized prognosis.

---

# Retrieval / Runtime Relevance

## High-Priority Terms

- immunotherapy
- stomach cancer immunotherapy
- gastric cancer immunotherapy
- gastric adenocarcinoma immunotherapy
- immune checkpoint inhibitor
- checkpoint inhibitor
- PD-1
- PD-L1
- CTLA-4
- immune response
- immune system
- cancer immune evasion
- immunotherapy and chemotherapy
- immunotherapy and targeted therapy
- combination immunotherapy
- durable response
- immunotherapy resistance
- pseudoprogression
- hyperprogression
- immune-related adverse event
- immune toxicity

## Biomarker Terms

- PD-L1
- CPS
- TAP
- MSI-H
- dMMR
- MSI
- MMR
- TMB-H
- HER2

## Treatment-Setting Terms

- perioperative immunotherapy
- neoadjuvant immunotherapy
- resectable gastric cancer
- advanced gastric cancer
- metastatic gastric cancer
- recurrent gastric cancer
- first-line immunotherapy
- systemic therapy

## Trial Terms

- CheckMate-649
- KEYNOTE-859
- KEYNOTE-811
- RATIONALE-305
- MATTERHORN

---

# Knowledge Units

## KU-01 — Definition

Immunotherapy helps the immune system attack cancer more effectively.

## KU-02 — Immune Checkpoint Concept

Checkpoint proteins regulate immune activation. Tumors can exploit checkpoint signaling to reduce immune attack.

## KU-03 — PD-1 / PD-L1

Blocking PD-1/PD-L1 signaling can restore or enhance anti-tumor immune activity.

## KU-04 — Immunotherapy Is a Category

Different agents and regimens have different evidence and clinical uses.

## KU-05 — Biomarker Context

PD-L1 and MSI-H/dMMR are major examples of tumor characteristics that can influence immunotherapy use.

## KU-06 — Treatment Setting

Immunotherapy can be relevant in selected perioperative and advanced/metastatic settings.

## KU-07 — Combination Treatment

Immunotherapy may be combined with chemotherapy or selected targeted therapies.

## KU-08 — Evidence

Representative phase III evidence includes CheckMate-649, KEYNOTE-859, RATIONALE-305, KEYNOTE-811, and MATTERHORN.

## KU-09 — Benefit and Limitation

Some patients have durable benefit; not all respond, and resistance can occur.

## KU-10 — Safety

Immune-related adverse events can affect multiple organs and may be serious.

## KU-11 — Response Patterns

Delayed response, pseudoprogression, mixed response, and hyperprogression are recognized immunotherapy concepts.

## KU-12 — Boundary

Detailed drug, biomarker-testing, toxicity, response, and individualized-treatment ownership is delegated.

---

# Evidence Classification

## Established / Guideline-Supported

- Immunotherapy is an established treatment category for selected gastric-cancer patients.
- Immune checkpoint inhibition is the dominant established immunotherapy paradigm represented in the project sources.
- Nivolumab, pembrolizumab, tislelizumab, durvalumab, and dostarlimab appear in the supplied gastric-cancer immunotherapy materials.
- Current NCCN v2.2026 includes immunotherapy-containing pathways in selected perioperative and advanced/metastatic settings.
- PD-L1 status is used in several treatment pathways.
- MSI-H/dMMR can support immunotherapy strategies independent of PD-L1 status in selected contexts.
- CheckMate-649, KEYNOTE-859, and RATIONALE-305 support immunotherapy + chemotherapy approaches in defined advanced populations.
- KEYNOTE-811 supports a selected HER2-positive immunotherapy + trastuzumab + chemotherapy approach.
- MATTERHORN supports a selected perioperative durvalumab + FLOT approach while showing important subgroup limitations.
- Immune-related adverse events are a distinctive safety issue.
- Unconventional response patterns are recognized with immunotherapy.

## Context-Dependent

- Which immunotherapy agent is appropriate.
- Whether immunotherapy should be combined with chemotherapy.
- Whether immunotherapy should be combined with HER2-targeted therapy.
- Whether perioperative immunotherapy is appropriate.
- Whether PD-L1 is required for a particular strategy.
- The relative importance of PD-L1 versus MSI-H/dMMR in a given treatment context.
- Duration of benefit.
- Response interpretation in an individual patient.
- Rechallenge or sequencing after progression.

## Evidence-Limited / Requires Caution

- TMB-H as a gastric/GEJ-specific predictor of benefit.
- Extrapolation from tumor-agnostic immunotherapy evidence to gastric cancer.
- Universal prediction of durable benefit.
- Generalization of subgroup trial results to every patient.

---

# Authoritative Sources

## Primary Disease-Specific Guideline

### Gastric Cancer v2.2026 — NCCN Clinical Practice Guidelines in Oncology

Primary source for:

- current gastric-cancer immunotherapy positioning;
- perioperative FLOT + durvalumab;
- neoadjuvant/perioperative immunotherapy for MSI-H/dMMR;
- first-line advanced/metastatic immunotherapy combinations;
- PD-L1 context;
- MSI-H/dMMR context;
- CheckMate-649;
- RATIONALE-305;
- KEYNOTE-859;
- KEYNOTE-811;
- MATTERHORN;
- immune-checkpoint-toxicity governance linkage.

## Primary Patient-Facing Clinical Source

### NCI — Treatment of Stomach Cancer

Supports:

- immunotherapy as a stomach-cancer treatment category;
- biomarker testing in relation to immunotherapy;
- treatment planning as a shared cancer-care-team process;
- patient-facing treatment context.

## Patient-Facing Immunotherapy Source

### American Cancer Society — Immunotherapy for Stomach Cancer

Supports:

- checkpoint concept;
- PD-1/PD-L1 explanation;
- representative immunotherapy agents;
- combination treatment;
- common and serious side effects;
- patient-facing safety messaging.

## Cross-Cutting Professional Source

### ESMO-ASCO Recommendations for a Global Curriculum in Medical Oncology — 2023

Supports:

- immunotherapy mechanism concepts;
- distinction from chemotherapy and targeted therapy;
- durable responses;
- unconventional response patterns;
- pseudoprogression;
- hyperprogression;
- immune-related adverse events;
- combination therapy;
- immunotherapy in curative settings;
- resistance.

## Supporting NCI Source

### Gastric Cancer Treatment (PDQ®)

Supports:

- immunotherapy as part of systemic treatment for advanced/recurrent disease;
- HER2, dMMR/MSI, and PD-L1 testing context;
- immunotherapy + chemotherapy treatment context.

---

# Clinical Scope

## Core Ownership

PP-0213 owns the clinical framework connecting:

**immune system**

→ **checkpoint regulation**

→ **immunotherapy**

→ **biomarker/context**

→ **treatment setting**

→ **evidence**

→ **benefit/limitations**

→ **safety**

→ **patient understanding**

## Supporting Ownership

PP-0213 may introduce:

- PD-L1 CPS/TAP;
- MSI-H/dMMR;
- TMB-H;
- HER2 + immunotherapy;
- FLOT + durvalumab;
- landmark trials;
- immune-related adverse events;
- pseudoprogression;
- resistance.

These are introduced only to the depth needed to answer the umbrella question.

## Explicit Exclusions

PP-0213 does not own:

- detailed checkpoint drug management;
- detailed PD-L1 scoring;
- detailed MSI/MMR testing;
- detailed TMB testing;
- individualized biomarker interpretation;
- detailed toxicity management;
- detailed response criteria;
- individualized treatment;
- detailed treatment sequencing;
- detailed HER2/CLDN18.2/anti-angiogenic treatment.

---

# Runtime Safety Rules

## Rule 1 — No Individualized Prescription

Do not transform:

> “My PD-L1 is CPS 5.”

into:

> “Therefore you should receive drug X.”

Instead explain the relevant population-level evidence and recommend discussion with the treating team.

## Rule 2 — No Universal Biomarker Rule

Do not state:

> “PD-L1 positive = immunotherapy.”

The correct interpretation is treatment-specific.

## Rule 3 — MSI-H/dMMR Independence

Do not imply that PD-L1 positivity is always required when discussing MSI-H/dMMR immunotherapy contexts.

## Rule 4 — No False Promise

Do not promise response, cure, or durable benefit.

## Rule 5 — Safety Escalation

When users describe new symptoms during checkpoint therapy, emphasize prompt contact with the treating team rather than attempting to manage the adverse event from this umbrella package.

## Rule 6 — Response Caution

Do not label apparent progression as pseudoprogression without clinical assessment.

## Rule 7 — Source Integrity

Use project Source Materials as the primary evidence basis. Do not silently substitute general knowledge for missing project evidence.

---

# Knowledge Graph

## Prerequisite

- PP-0014 — Foundational Immunotherapy for Gastric Adenocarcinoma
- PP-0208 — Palliative Systemic Therapy
- PP-0209 — Targeted Therapy in Gastric Cancer
- PP-0182 — MSI/MMR Testing
- PP-0183 — PD-L1 Testing
- PP-0191 — Biomarker Testing for Immunotherapy

## Related

- PP-0210 — HER2-targeted Therapy
- PP-0211 — CLDN18.2-targeted Therapy
- PP-0212 — Anti-angiogenic Therapy
- PP-0217 — Response Assessment
- PP-0231 — Treatment-related Toxicity and Supportive Care
- PP-0232 — Multidisciplinary Management

## Next / Downstream

- PP-0214 — Immune Checkpoint Inhibitors
- PP-0215 — MSI-H/dMMR Gastric Cancer and Immunotherapy
- PP-0216 — PD-L1-guided Immunotherapy
- PP-0217 — Response Assessment
- PP-0218 — RECIST-based Assessment
- PP-0219 — Post-treatment Imaging
- PP-0231 — Treatment-related Toxicity and Supportive Care

---

# Boundary Map

| Ownership | PP-0213 | Downstream Specialized PP |
|---|---|---|
| Immunotherapy definition | Core | — |
| Immune checkpoint concept | Core | PP-0214 deepens mechanism |
| Individual checkpoint inhibitors | Conceptual | PP-0214 |
| MSI-H/dMMR relevance | Core context | PP-0215 detailed |
| PD-L1 relevance | Core context | PP-0216 detailed |
| PD-L1 testing | Excluded | PP-0183 |
| Biomarker-directed immunotherapy | Context | PP-0191 / PP-0215 / PP-0216 |
| HER2 + immunotherapy | Supporting | PP-0210 |
| CLDN18.2 + immunotherapy | Context only | Relevant therapy packages |
| Anti-angiogenic therapy | Excluded | PP-0212 |
| Response assessment | Concept only | PP-0217–0219 |
| Immune toxicity | Safety awareness | PP-0231 |
| Detailed sequencing | Excluded | Treatment-sequencing packages |

---

# Governance Metadata

| Field | Value |
|---|---|
| Governance Authority | CORE_WORKING_RULES v1.7 |
| Structural Authority | FREEZE GOLD POPULATION PACKAGE SPECIFICATION v1.1 |
| Discussion Authority | Approved PP Discussion depth and format example |
| Clinical Evidence Authority | Project Source Files, with NCCN v2.2026 as primary disease-specific guideline |
| Execution Authority | Project Coordinator explicit PP request |
| Decision Status | APPROVED / LOCKED |
| Production Standard | GOLD |
| Boundary Rule | One final-response Boundary declaration; artifact scope/exclusion language remains ownership-oriented |
| External Web | Not used as a substitute for project Source Materials |

---

# Version Control

| Version | Date | Change |
|---|---|---|
| 1.0.0 | 2026-08-09 | Initial Gold production after approved/locked PP-0213 Decision Batch. |

---

# Final Status

**GOLD — READY FOR INTEGRATION**
