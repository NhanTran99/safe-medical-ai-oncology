# 02_KNOWLEDGE_PASSPORT.md

# Knowledge Passport

## Identity

- **KP ID:** KP-PP-0205
- **PP ID:** PP-0205
- **Title:** Adjuvant Therapy
- **Version:** v1.0.0
- **Status:** GOLD / LOCKED
- **Artifact Class:** Knowledge Passport

# Knowledge Classification

## Knowledge Type

Strategy-level clinical education package.

## Atomic Clinical Question

> What is adjuvant therapy after definitive gastric-cancer surgery, why is it used, how is postoperative treatment selected from pathology and previous treatment, and how does it differ from perioperative, neoadjuvant, chemoradiation, and palliative treatment?

## Primary Function

To provide a reusable, patient-centered, evidence-traceable representation of postoperative/adjuvant treatment strategy without absorbing the ownership of individual chemotherapy regimens, surgery, chemoradiation, biomarker testing, targeted therapy, immunotherapy, recurrence treatment, or surveillance.

## Clinical Granularity

**Strategy level.**

The package is broader than:

- a single chemotherapy regimen;
- a single radiation regimen;
- a single postoperative trial.

It is narrower than:

- the entire gastric-cancer treatment pathway;
- perioperative chemotherapy as a global strategy;
- systemic therapy for advanced disease.

# Patient Journey Classification

## Primary Journey Stage

**Definitive surgery → postoperative risk assessment → adjuvant treatment decision → postoperative treatment → treatment completion → transition to surveillance**

## Secondary Journey Stages

- postoperative recovery;
- pathology review;
- multidisciplinary decision-making;
- nutritional/functional recovery;
- shared decision-making;
- toxicity and treatment-tolerance assessment.

# Intended Runtime Usage

## Primary Runtime Use

Retrieve when the user asks:

- What is adjuvant therapy?
- Why do I need treatment after surgery?
- Do I need chemotherapy after gastrectomy?
- What determines postoperative treatment?
- What does my pathology mean for adjuvant treatment?
- Why does D2 lymphadenectomy matter for postoperative therapy?
- Why might I receive chemotherapy after D2 surgery?
- What evidence supports adjuvant chemotherapy?
- What did the CLASSIC trial show?
- What did the S-1/ACTS-GC trial show?
- Why might chemoradiation be used after surgery?
- Why does previous chemotherapy before surgery matter?
- Is adjuvant therapy the same as FLOT?
- Is adjuvant treatment the same as palliative chemotherapy?

## Secondary Runtime Use

Use as a bridge to:

- PP-0203 Perioperative Chemotherapy;
- PP-0204 FLOT;
- PP-0201 D2 Lymphadenectomy;
- PP-0206 Chemoradiation;
- downstream surveillance and recurrence packages.

# Classification

## Clinical Domain

Gastric Cancer — Treatment.

## Domain Subtype

Postoperative / adjuvant treatment strategy.

## Clinical Complexity

Moderate-to-high.

The package is patient-facing but contains trial-level evidence and treatment-pathway distinctions that require careful context.

## Educational Level

Patient / caregiver with clinician-verifiable detail.

## Treatment Intent

Primarily curative-intent postoperative management after definitive local treatment.

## Evidence Role

- current guideline interpretation;
- randomized trial evidence;
- patient-facing treatment explanation;
- boundary and retrieval control.

# Runtime Metadata

## Retrieval Tags

- adjuvant therapy gastric cancer
- postoperative therapy gastric cancer
- postoperative chemotherapy
- adjuvant chemotherapy
- D2 gastrectomy adjuvant chemotherapy
- CLASSIC trial
- ACTS-GC
- S-1 adjuvant gastric cancer
- postoperative chemoradiation
- INT-0116
- SWOG-9008
- ARTIST
- ARTIST II
- CRITICS
- R0 resection
- R1 resection
- R2 resection
- postoperative treatment
- after gastrectomy
- treatment after surgery
- recurrence risk reduction

## Query Expansion

“adjuvant” ↔ postoperative treatment

“after surgery” ↔ postoperative treatment

“chemo after surgery” ↔ adjuvant chemotherapy

“D2 + chemo” ↔ postoperative chemotherapy after D2 gastrectomy

“radiation after surgery” ↔ postoperative chemoradiation

“FLOT after surgery” ↔ postoperative component of perioperative FLOT

## Retrieval Exclusions

Do not retrieve PP-0205 as the sole source for:

- individualized chemotherapy dosing;
- exact FLOT administration;
- radiation planning;
- biomarker-testing methodology;
- advanced/metastatic systemic therapy;
- emergency toxicity management;
- detailed surgery.

# Clinical Boundary Model

## Core

Adjuvant therapy as a postoperative strategy.

## Supporting

Postoperative chemoradiation and related trial evidence.

## Explicitly Excluded

Regimen-specific prescribing, technical surgery, radiation planning, biomarker methodology, advanced-disease treatment, surveillance.

## Delegated-to PP

PP-0203, PP-0204, PP-0206, PP-0207, PP-0196–0202, biomarker/targeted/immunotherapy PPs, response/surveillance PPs.

# Evidence Hierarchy

## Tier 1 — Current disease-specific guideline

### NCCN Gastric Cancer

Use for:

- current postoperative treatment framework;
- pathologic-stage and nodal-status decision context;
- margin status;
- extent of lymphadenectomy;
- previous treatment;
- current preferred postoperative strategies.

## Tier 2 — Randomized evidence synthesized by NCI

Use for:

- CLASSIC;
- ACTS-GC/S-1;
- INT-0116/SWOG-9008;
- CRITICS;
- perioperative treatment context.

## Tier 3 — Vietnamese clinical guideline

Use for:

- regional clinical framework;
- postoperative chemotherapy context;
- adjuvant chemoradiation regimen examples;
- D1/D2 surgical context;
- postoperative nutritional considerations.

## Tier 4 — ESMO-ASCO curriculum

Use for:

- multidisciplinary treatment sequencing;
- stage, functional status, and biomarker-guided strategy;
- treatment across the gastric-cancer continuum.

## Tier 5 — ACS/NCI patient-facing material

Use for:

- patient-friendly definition of adjuvant therapy;
- distinction between perioperative and adjuvant chemotherapy;
- general treatment explanation.

# Evidence Confidence Map

| Knowledge Element | Confidence | Reason |
|---|---|---|
| Definition of adjuvant therapy | Very high | NCI patient-facing treatment source |
| Postoperative treatment depends on pathology and previous treatment | Very high | NCCN |
| Postoperative chemotherapy after primary D2 dissection | Very high | NCCN |
| CLASSIC DFS benefit | Very high | NCI randomized evidence |
| CLASSIC OS result | Very high | NCI randomized evidence |
| S-1/ACTS-GC OS benefit | Very high | NCI randomized evidence |
| INT-0116 survival benefit | Very high | NCI randomized evidence |
| CRITICS lack of OS benefit for postoperative chemoradiation after preoperative chemotherapy | Very high | NCI randomized evidence |
| ARTIST/ARTIST II interpretation | High | NCCN evidence synthesis |
| D2 vs less-than-D2 postoperative strategy | Very high | NCCN |
| Postoperative readiness concepts | High | guideline/curriculum/supportive evidence |
| Exact individual regimen choice | Not determinable | patient-specific |
| Exact dose modification | Not supported as universal | regimen-specific |
| Individual recurrence prediction | Not supported | trial populations are not individual forecasts |

# Evidence-to-Runtime Translation

## Rule A — Strategy question

If the user asks:

> “Do I need treatment after surgery?”

Use PP-0205 first.

Then identify whether the patient previously received systemic treatment and whether the question requires regimen-specific or chemoradiation-specific routing.

## Rule B — Regimen question

If the user asks:

> “What is FLOT?”

Use PP-0204.

## Rule C — Perioperative sequence question

If the user asks:

> “Why is chemotherapy given before and after surgery?”

Use PP-0203, with PP-0205 for the postoperative/adjuvant distinction.

## Rule D — D2 question

If the user asks:

> “What is D2 lymphadenectomy?”

Use PP-0201.

If the user asks:

> “Why does D2 affect postoperative treatment?”

Use PP-0205.

## Rule E — Chemoradiation question

If the user asks:

> “Why am I getting radiation with chemotherapy after surgery?”

Use PP-0206 for detailed content, with PP-0205 providing the strategy-level context.

## Rule F — Recurrence question

If recurrence is documented, do not treat the situation as routine adjuvant therapy.

Route to recurrence/advanced-disease packages.

# Knowledge Objects

## KO-01 — Adjuvant Therapy Definition

**Type:** Clinical concept.

**Definition:** Treatment delivered after definitive local treatment to reduce recurrence risk.

**Source:** NCI.

## KO-02 — Postoperative Decision Inputs

**Type:** Decision context.

**Inputs:**

- pathologic stage;
- nodal status;
- margin status;
- lymphadenectomy extent;
- previous treatment.

**Source:** NCCN.

## KO-03 — D2 / Postoperative Chemotherapy Relationship

**Type:** Treatment-strategy relationship.

**Source:** NCCN + CLASSIC.

## KO-04 — CLASSIC Evidence Node

**Type:** Randomized evidence.

**Population:** 1,035 patients; stage IIA–IIIB; curative D2 gastrectomy.

**Intervention:** capecitabine + oxaliplatin.

**Comparator:** follow-up alone.

**Key outcomes:** DFS and OS.

## KO-05 — ACTS-GC Evidence Node

**Type:** Randomized evidence.

**Population:** 1,059 patients; stage II/III; D2 gastrectomy.

**Intervention:** one year S-1.

**Comparator:** surgery alone.

**Key outcome:** OS.

## KO-06 — INT-0116 Evidence Node

**Type:** Randomized evidence.

**Population:** completely resected stage IB–IV M0 gastric/GEJ adenocarcinoma.

**Intervention:** postoperative chemotherapy + radiation.

**Comparator:** surgery alone.

**Key outcome:** OS and relapse-free survival.

## KO-07 — CRITICS Evidence Node

**Type:** Randomized evidence.

**Context:** preoperative chemotherapy + surgery followed by postoperative chemotherapy versus chemoradiotherapy.

**Key finding:** no survival advantage for postoperative chemoradiotherapy.

## KO-08 — FLOT Interface

**Type:** Boundary object.

**Relationship:** postoperative FLOT may be the postoperative component of perioperative FLOT.

**Owner of detailed regimen:** PP-0204.

# Maintenance Triggers

Review this package when:

- gastric-cancer guideline postoperative recommendations change;
- new randomized adjuvant chemotherapy evidence changes the standard;
- interpretation of D2 versus less-than-D2 surgery changes;
- new perioperative strategies alter postoperative continuation;
- major immunotherapy or biomarker-defined postoperative strategies become guideline-defining;
- a new postoperative modality changes the treatment architecture.

# Maintenance Rules

1. Do not silently convert adjuvant therapy into a regimen package.
2. Do not silently absorb chemoradiation.
3. Do not silently absorb surveillance.
4. Do not replace randomized trial results with generalized claims.
5. Preserve population qualifiers for trial outcomes.
6. Preserve the distinction between evidence and individualized recommendation.
7. Update boundary declarations when neighboring PPs change.
8. Any structural change requires a new governance decision.

# Gold Depth Requirement

This Passport intentionally contains:

- identity;
- classification;
- runtime metadata;
- evidence hierarchy;
- confidence mapping;
- knowledge objects;
- boundary logic;
- retrieval safety;
- maintenance logic.

The depth is part of the Gold standard and must not be compressed in future revisions.

# Final Runtime Statement

**PP-0205 is the authoritative strategy-level knowledge node for adjuvant/postoperative treatment after definitive gastric-cancer surgery within the current Population Package architecture.**


# Extended Runtime and Governance Layer

# Clinical Decision Ontology

## Concept Type

**Postoperative treatment strategy**

## Parent Concept

**Gastric-cancer treatment**

## Child Concepts

- postoperative chemotherapy;
- postoperative chemoradiation;
- postoperative continuation of perioperative systemic therapy.

## Excluded Child Ownership

- FLOT regimen;
- CAPOX regimen;
- FOLFOX regimen;
- S-1 regimen;
- radiation planning;
- immunotherapy regimen;
- targeted therapy regimen.

# Runtime Intent Matrix

| User Intent | Primary PP | Secondary PP |
|---|---|---|
| What is adjuvant therapy? | PP-0205 | NCI patient-facing source |
| Why treatment after surgery? | PP-0205 | PP-0203 |
| Do I need chemo after gastrectomy? | PP-0205 | PP-0201 / relevant regimen PP |
| Why D2 affects treatment? | PP-0205 | PP-0201 |
| What is FLOT? | PP-0204 | PP-0205 |
| What is CAPOX? | regimen-specific PP | PP-0205 |
| Why radiation after surgery? | PP-0206 | PP-0205 |
| What did CLASSIC show? | PP-0205 | evidence package |
| What did ACTS-GC show? | PP-0205 | evidence package |
| What did CRITICS show? | PP-0205 | PP-0206 |
| What happens after recurrence? | PP-0207 / recurrence PP | PP-0205 only for boundary |
| When does surveillance begin? | surveillance PP | PP-0205 only as transition |

# Semantic Guardrails

## Guardrail 1

“Adjuvant” means postoperative treatment in the relevant clinical context.

## Guardrail 2

“Perioperative” means treatment spanning the preoperative and postoperative phases around surgery.

## Guardrail 3

“Neoadjuvant” means treatment before definitive surgery.

## Guardrail 4

“Palliative” means treatment for advanced/recurrent disease with disease-control/symptom goals rather than routine recurrence-risk reduction after definitive surgery.

## Guardrail 5

“FLOT” is a regimen name, not a synonym for adjuvant therapy.

# Evidence Retrieval Logic

## Query Cluster A — Definition

Retrieve:

- adjuvant;
- postoperative;
- after surgery;
- recurrence risk.

## Query Cluster B — Surgery Interface

Retrieve:

- D2;
- D1;
- lymphadenectomy;
- R0;
- R1;
- R2;
- nodes;
- margins.

## Query Cluster C — Evidence

Retrieve:

- CLASSIC;
- ACTS-GC;
- S-1;
- INT-0116;
- SWOG-9008;
- ARTIST;
- ARTIST II;
- CRITICS.

## Query Cluster D — Previous Treatment

Retrieve:

- perioperative;
- preoperative chemotherapy;
- postoperative continuation;
- FLOT.

# Confidence Handling

## Very High Confidence

Use assertively:

- definition of adjuvant therapy;
- CLASSIC numerical outcomes;
- ACTS-GC numerical outcomes;
- INT-0116 numerical outcomes;
- CRITICS numerical result;
- current NCCN postoperative framework.

## High Confidence

Use with contextual wording:

- nutritional readiness;
- multidisciplinary decision-making;
- treatment adaptation.

## Context-Dependent

Use cautious language:

- exact regimen choice;
- use of chemoradiation;
- postoperative treatment after nonstandard surgery;
- biomarker-directed postoperative approaches.

## Not Supported

Do not answer solely from PP-0205:

- individual prescription;
- dose modification;
- emergency toxicity management;
- individualized survival prediction.

# Patient-Language Translation Table

| Technical Term | Patient-Friendly Translation |
|---|---|
| Adjuvant therapy | Additional treatment after surgery intended to lower recurrence risk |
| Micrometastatic disease | Cancer cells too small to be seen with routine tests |
| Pathologic stage | Stage determined from the tissue removed during surgery |
| Nodal status | Whether cancer was found in lymph nodes |
| Margin | Edge of the removed tissue checked for cancer cells |
| R0 | No residual tumor identified at the surgical margin |
| R1 | Microscopic residual tumor at the margin |
| R2 | Visible/macroscopic residual tumor |
| D2 dissection | More extensive regional lymph-node removal used in gastric-cancer surgery |
| DFS | Time during which cancer does not return or progress, as defined by the study |
| OS | Time from a defined starting point until death from any cause |
| HR | Relative measure comparing the hazard of an event between study groups |

# Common Retrieval Failure Modes

## Failure Mode 1

User says:

> “I need chemo after surgery.”

System immediately retrieves FLOT.

### Correct behavior

Retrieve PP-0205 first.

Then determine:

- whether systemic treatment was already given;
- what surgery occurred;
- what postoperative strategy is being discussed.

## Failure Mode 2

User says:

> “I had D2 surgery.”

System assumes CAPOX.

### Correct behavior

D2 is a treatment-context variable, not a prescription.

## Failure Mode 3

User says:

> “My margin is positive.”

System answers with routine adjuvant chemotherapy.

### Correct behavior

Recognize a residual-disease pathway and route appropriately.

## Failure Mode 4

User says:

> “I had FLOT before surgery.”

System calls postoperative treatment “new adjuvant chemotherapy.”

### Correct behavior

Recognize the postoperative component of perioperative therapy.

## Failure Mode 5

User asks:

> “Should I have radiation?”

System applies INT-0116 universally.

### Correct behavior

Consider:

- previous chemotherapy;
- lymphadenectomy extent;
- current guideline;
- individual risk.

## Failure Mode 6

User asks:

> “CLASSIC says 74% DFS. Is that my chance?”

### Correct behavior

Explain population-level trial evidence and avoid individual prediction.

# Maintenance Matrix

| Trigger | Review Area |
|---|---|
| New NCCN version | Postoperative algorithms |
| New randomized adjuvant trial | Evidence matrix |
| New perioperative regimen | PP-0203/0204 boundary |
| New immunotherapy strategy | Biomarker/immunotherapy boundary |
| New radiation guideline | PP-0206 boundary |
| New surveillance guideline | Downstream transition |
| New surgical standard | D2 evidence interpretation |

# Artifact Interoperability

## CKO

Patient-facing explanation and clinical reasoning.

## KP

Runtime classification and retrieval behavior.

## EP

Evidence traceability and claim support.

## QA

Verification and governance assurance.

These artifacts are complementary and must not be treated as interchangeable summaries.

# Version-Control Rules

A future version must preserve:

- PP identity;
- atomic question;
- four-part Boundary;
- evidence hierarchy;
- Knowledge Graph ownership.

A future update may expand clinical detail without reducing Gold depth.

# Final Passport Status

**PP-0205 Knowledge Passport: GOLD / LOCKED / READY FOR RUNTIME**
