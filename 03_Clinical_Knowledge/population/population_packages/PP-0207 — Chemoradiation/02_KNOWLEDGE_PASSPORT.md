# PP-0207 — Chemoradiation

# Knowledge Passport

## 1. Identity

**KP ID:** KP-PP-0207  
**PP ID:** PP-0207  
**Title:** Chemoradiation  
**Version:** 1.0.0  
**Artifact Status:** GOLD — READY FOR INTEGRATION  
**CKO Link:** CKO-PP-0207  
**Evidence Package Link:** EP-PP-0207  
**QA Report Link:** QA-PP-0207

---

# 2. Knowledge Classification

## Clinical Domain

**Gastric Cancer Treatment**

## Domain Code

**GC-TX**

## Population Package Type

**Patient-facing treatment education / combined-modality therapy**

## Clinical Question Type

**Treatment modality and treatment-context explanation**

## Clinical Complexity

**High**

The topic requires integration of systemic therapy, radiation therapy, surgery, pathology, lymph-node dissection, treatment sequence, evidence interpretation and treatment intent.

## Patient Journey Stage

Primary stage:

**Treatment selection → Multimodality treatment → Post-treatment / reassessment interface**

Secondary stages:

- preoperative treatment context;
- postoperative treatment context;
- unresectable local/regional disease;
- palliative/local symptom control.

---

# 3. Educational Intent

The package is intended to help a patient understand:

- what chemoradiation is;
- why chemotherapy and radiation may be combined;
- why it is not a universal treatment;
- how previous therapy and surgery influence its role;
- what major evidence supports or limits its use;
- why INT-0116, CRITICS and TOPGEAR cannot be interpreted as the same clinical question;
- what side effects and nutritional issues may occur;
- why multidisciplinary decision-making is required.

The package is not intended to prescribe a patient's treatment.

---

# 4. Patient-Facing Runtime Purpose

This package should be retrieved when a patient asks questions such as:

- “What is chemoradiation?”
- “Why am I getting chemotherapy and radiation together?”
- “Do I need radiation after stomach surgery?”
- “Why does my positive margin affect treatment?”
- “Why does D2 surgery matter?”
- “Why didn't my doctor add radiation after chemotherapy and surgery?”
- “Can chemoradiation be used if my tumor cannot be removed?”
- “What did the major chemoradiation trials show?”
- “What side effects should I understand before chemoradiation?”

---

# 5. Retrieval / Runtime Relevance

## High-Relevance Queries

- chemoradiation gastric cancer
- chemotherapy radiation stomach cancer
- postoperative chemoradiation
- adjuvant chemoradiation gastric cancer
- R1 gastric cancer chemoradiation
- R2 gastric cancer chemoradiation
- D1 D2 chemoradiation gastric cancer
- INT-0116 gastric cancer
- SWOG-9008 gastric cancer
- CRITICS chemoradiation gastric cancer
- TOPGEAR chemoradiation gastric cancer
- preoperative chemoradiation gastric cancer
- unresectable gastric cancer chemoradiation
- radiation with chemotherapy stomach cancer
- side effects chemoradiation stomach cancer
- radiation after gastrectomy

## Secondary Queries

- positive surgical margin stomach cancer
- postoperative radiation gastric cancer
- locally unresectable gastric cancer
- palliative radiation stomach cancer
- radiation planning stomach cancer
- nutrition during chemoradiation
- multidisciplinary gastric cancer treatment

---

# 6. Retrieval Safety Rules

When retrieving this PP:

1. Do not interpret “chemoradiation” as automatically meaning metastatic disease.
2. Do not state that all gastric-cancer patients require radiation.
3. Do not state that every patient after surgery needs chemoradiation.
4. Do not imply that TOPGEAR established preoperative chemoradiation as standard treatment for resectable disease.
5. Do not imply that CRITICS demonstrated benefit from postoperative chemoradiation after preoperative chemotherapy.
6. Do not convert historical INT-0116 evidence into a universal current treatment rule.
7. Do not provide individualized chemotherapy or radiation prescriptions.
8. Do not provide radiation-dose or contouring instructions.
9. Do not replace the treating team's multidisciplinary decision.

---

# 7. Knowledge Graph

## Prerequisite

- PP-0027 — Staging Work-up
- PP-0028 — Treatment Overview
- PP-0196 — Gastrectomy Principles
- PP-0199 — Lymphadenectomy
- PP-0200 — D1 Lymphadenectomy
- PP-0201 — D2 Lymphadenectomy
- PP-0203 — Perioperative Chemotherapy
- PP-0205 — Adjuvant Therapy
- PP-0206 — Neoadjuvant Therapy

## Related

- PP-0033 — Radiotherapy
- PP-0204 — FLOT
- PP-0217 — Response Assessment
- PP-0218 — RECIST
- PP-0219 — Post-treatment Imaging
- PP-0231 — Treatment-related Toxicity and Supportive Care
- PP-0232 — Multidisciplinary Management of Gastric Cancer

## Next / Downstream

- response assessment;
- post-treatment imaging;
- surgical reassessment where relevant;
- supportive care;
- surveillance and recurrence pathways;
- advanced/palliative treatment pathways when cure is not feasible.

---

# 8. Clinical Scope

## Core

- Definition of chemoradiation.
- Rationale for combined chemotherapy and radiation.
- Treatment-context dependence.
- Selected postoperative use.
- R1/R2 implications.
- Selected high-risk R0 implications.
- Relationship to D1/D2 extent.
- INT-0116/SWOG-9008.
- CRITICS.
- TOPGEAR.
- RTOG 9904 context.
- Selected unresectable local/regional disease.
- Selected palliative/local symptom control.
- Conceptual radiation planning.
- Patient-facing toxicity and nutrition.
- Multidisciplinary decision-making.

## Supporting

- broad radiotherapy principles;
- systemic therapy context;
- pathology and margin terminology;
- surgical context;
- EGJ overlap;
- response/reassessment interface;
- historical evidence.

## Explicitly Excluded

- detailed chemotherapy regimen instruction;
- FLOT instruction;
- detailed radiotherapy prescriptions;
- radiation contouring and physics;
- surgery technique;
- D1/D2 technique;
- formal RECIST;
- detailed imaging methodology;
- detailed toxicity algorithms;
- detailed nutritional protocols;
- individualized treatment decisions;
- recurrent/metastatic treatment algorithms.

## Delegated-to PP

- PP-0033 Radiotherapy
- PP-0203 Perioperative Chemotherapy
- PP-0204 FLOT
- PP-0205 Adjuvant Therapy
- PP-0206 Neoadjuvant Therapy
- PP-0196–0201 surgical/lymphadenectomy PPs
- PP-0217 Response Assessment
- PP-0218 RECIST
- PP-0219 Post-treatment Imaging
- PP-0231 Treatment-related Toxicity and Supportive Care
- PP-0232 Multidisciplinary Management
- downstream advanced/recurrent/palliative packages

---

# 9. Evidence Classification

## Established / Guideline-Supported

- Chemoradiation is a combined-modality approach.
- Selected postoperative chemoradiation is supported by current NCCN guidance.
- R1/R2 resection can support postoperative chemoradiation in appropriate patients.
- Less-than-D2 surgery is an important factor in selected postoperative chemoradiation pathways.
- Chemoradiation is an option in selected unresectable local/regional disease.
- Radiation has selected palliative/local symptom-control roles.
- Radiation requires multidisciplinary planning.

## Landmark Randomized Evidence

### SWOG-9008 / INT-0116

Supports postoperative combined-modality therapy in the studied context.

### CRITICS

Does not support routine postoperative chemoradiation after preoperative chemotherapy and surgery.

### TOPGEAR

Does not support routine preoperative chemoradiation for resectable gastric/EGJ adenocarcinoma.

## Historical / Supporting

- RTOG 9904.
- CALGB-80101.
- Earlier randomized RT/chemoradiation studies summarized by NCCN and NCI.

---

# 10. Evidence Interpretation Rules

### Rule 1

A positive trial in one treatment sequence cannot automatically be transferred to another sequence.

### Rule 2

Pathologic complete response is not equivalent to overall survival benefit.

### Rule 3

Current guideline recommendations must be interpreted together with prior systemic therapy and surgery.

### Rule 4

R1/R2 recommendations should be distinguished from randomized-trial-supported routine pathways when the guideline itself notes limited prospective evidence.

### Rule 5

The existence of a chemoradiation option does not mean that it is mandatory.

### Rule 6

Patient-facing language should distinguish:

- standard/guideline-supported;
- selected/context-dependent;
- historical;
- investigational/not recommended routinely.

---

# 11. Primary Authoritative Sources

1. **NCCN Guidelines — Gastric Cancer, Version 2.2026**  
   Direct disease-specific guideline source for postoperative management, chemoradiation principles, TOPGEAR, CRITICS, D1/D2-related treatment pathways and multidisciplinary radiation planning.

2. **NCI PDQ — Gastric Cancer Treatment**  
   Independent evidence synthesis covering SWOG-9008/INT-0116, CRITICS, RTOG 9904 and treatment options.

---

# 12. Supporting Sources

3. **American Cancer Society — Stomach Cancer**  
   Patient-facing explanation of radiation use, chemoradiation, unresectable disease, palliative use, radiation delivery and side effects.

4. **ESMO-ASCO Recommendations for a Global Curriculum in Medical Oncology, 2023**  
   Professional curriculum context for multidisciplinary radiotherapy, treatment timing, concurrent chemoradiation and toxicity.

---

# 13. Source Mapping

| Source | Role | PP-0207 use |
|---|---|---|
| NCCN v2.2026 | Primary guideline | Current treatment position and evidence interpretation |
| NCI Gastric Cancer Treatment PDQ | Primary evidence synthesis | INT-0116, CRITICS, RTOG 9904 |
| ACS Stomach Cancer | Patient-facing support | Definition, use, delivery, toxicity, nutrition |
| ESMO-ASCO 2023 | Supporting professional framework | MDT, timing, toxicity, concurrent therapy |

---

# 14. Governance Metadata

**Production rule:** Gold four-artifact package  
**Decision status:** Approved and Locked by Project Coordinator  
**Scope status:** Locked  
**Source-first verification:** Completed before artifact production  
**Adjacent-package overlap check:** Completed at Decision Batch stage  
**Boundary:** Declared in final production response only, per governance  
**Version:** 1.0.0  
**QA gate:** PASS — GOLD — READY FOR INTEGRATION

---

# 15. Runtime Clinical Safety

This package is educational.

It must not be used to generate an individualized treatment recommendation without the patient's clinical record and specialist review.

When a user asks “Should I have chemoradiation?”, the runtime should retrieve this PP to explain the decision factors and then route toward the appropriate treatment-selection and multidisciplinary-care context rather than outputting a personalized prescription.

When a user asks for chemotherapy dose, radiation dose, field design, or detailed toxicity management, the runtime should delegate to the relevant specialist package or advise consultation with the treating team.

---

# 16. Patient Communication Principles

Use plain language.

Explain R0, R1, R2, D1 and D2 when they first appear.

Avoid saying “you need radiation” unless the source context and clinical record support that statement and the question is explicitly about an already documented plan.

Prefer:

> “Radiation may be considered in selected situations.”

When describing current guidance, identify that recommendations depend on the treatment sequence and surgical/pathologic context.

When discussing evidence:

- state the population;
- state what was compared;
- state the key outcome;
- state the limitation or context.

Do not use a single trial result as a universal rule.

---

# 17. Clinical Concept Map

**Chemoradiation**

→ combined systemic + local/regional treatment

→ treatment intent determines context

→ postoperative pathway depends on:

- pathology
- margins
- lymph-node dissection
- previous systemic therapy

→ landmark evidence:

- INT-0116
- CRITICS
- TOPGEAR

→ unresectable local/regional pathway

→ selected palliative/local control

→ toxicity/nutrition

→ multidisciplinary planning

→ response/reassessment downstream.

---

# 18. Boundary Verification

The package does not own broad radiotherapy, broad chemotherapy, FLOT, gastrectomy, D1/D2 surgical technique, formal response criteria or advanced-disease systemic treatment.

The package owns the intersection between chemotherapy and radiation in gastric-cancer treatment and the evidence explaining when that combined strategy is or is not useful.

This is the central ownership principle.

---

# 19. Future Update Triggers

Review PP-0207 when:

1. NCCN changes the gastric-cancer chemoradiation pathway.
2. A major randomized trial changes the evidence for preoperative chemoradiation.
3. CRITICS II reports mature results that materially alter treatment sequencing.
4. New prospective evidence changes the role of postoperative chemoradiation after modern systemic therapy.
5. New evidence changes the role of radiation after D2 surgery.
6. New evidence changes chemoradiation for unresectable disease.
7. Major changes occur in radiation technology that alter the clinical role or toxicity profile.
8. A dedicated PP is created that changes the ownership boundary.

---

# 20. Final Passport Status

**PASS — GOLD — READY FOR INTEGRATION**

# 21. Clinical Decision Dimensions for Retrieval

When a retrieval system uses this PP, it should preserve the following dimensions rather than collapsing the topic into a yes/no radiation question:

1. **Treatment timing** — before surgery, after surgery, or treatment for unresectable disease.
2. **Prior systemic therapy** — whether chemotherapy or other systemic treatment was already given.
3. **Surgical status** — whether a resection occurred and whether disease was completely removed.
4. **Margin status** — R0, R1 or R2.
5. **Lymph-node dissection** — particularly less-than-D2 versus primary D2 dissection.
6. **Disease extent** — resectable, unresectable local/regional, or metastatic.
7. **Treatment intent** — curative, disease-control, or palliative.
8. **Evidence setting** — landmark trial, current guideline, historical evidence, or evolving evidence.
9. **Patient fitness** — whether the patient can tolerate combined treatment.
10. **Toxicity/nutrition** — whether treatment burden changes the risk-benefit discussion.

These dimensions should remain visible in runtime reasoning.

---

# 22. Runtime Answer Pattern

For a general patient question about chemoradiation, the preferred answer sequence is:

### Step 1 — Define

Explain chemoradiation in plain language.

### Step 2 — Explain why it may be considered

Explain the complementary systemic and local/regional roles.

### Step 3 — Establish context

Ask or use available information about surgery, prior treatment, margins, lymph-node dissection and disease extent.

### Step 4 — Explain the evidence

Use the relevant trial rather than citing all trials indiscriminately.

### Step 5 — State uncertainty

Explain when evidence is context-dependent or evolving.

### Step 6 — Address safety

Mention common treatment burden and the importance of reporting symptoms.

### Step 7 — Route downstream

Delegate regimen, radiation planning, response assessment or toxicity-management questions to the appropriate PP.

---

# 23. Runtime Routing Examples

## Query: “What is chemoradiation?”

Route primarily to PP-0207.

## Query: “What is FLOT?”

Route to PP-0204, with PP-0207 only as comparative context if needed.

## Query: “Why do I need chemotherapy before and after surgery?”

Route primarily to PP-0203.

## Query: “What is adjuvant therapy?”

Route primarily to PP-0205.

## Query: “What is neoadjuvant therapy?”

Route primarily to PP-0206.

## Query: “What is D2 lymphadenectomy?”

Route to PP-0201.

## Query: “How is radiation planned and what dose do I receive?”

Route to PP-0033 / dedicated radiotherapy knowledge; PP-0207 supplies only conceptual context.

## Query: “How do we measure response after chemoradiation?”

Route to PP-0217/0218/0219.

## Query: “How are nausea and diarrhea treated?”

Route to PP-0231.

---

# 24. Knowledge Granularity Rules

The package is deliberately divided into layers.

### Layer A — Definition

What chemoradiation is.

### Layer B — Clinical reasoning

Why the combination may be useful in selected settings.

### Layer C — Evidence

What randomized trials show.

### Layer D — Patient experience

What treatment and side effects may feel like.

### Layer E — Governance/routing

What the package owns and where detailed questions should go.

The runtime should not expose all layers equally in every answer. Retrieval should select the depth needed for the question while preserving the underlying Gold knowledge asset.

---

# 25. High-Risk Misinterpretation Controls

The following phrases should trigger caution:

- “everyone”;
- “always”;
- “never”;
- “standard for all”;
- “stronger treatment”;
- “more effective because it uses two treatments”;
- “radiation is required after surgery”;
- “D2 means no radiation”;
- “chemoradiation is only for advanced cancer”;
- “a complete response means cured.”

The runtime should replace such absolute interpretations with context-dependent language supported by the evidence.

---

# 26. Clinical Intent Taxonomy

## Curative-intent context

Selected postoperative or selected local/regional treatment settings may use chemoradiation with the aim of controlling disease and improving the chance of long-term disease control.

## Disease-control context

Selected unresectable local/regional disease may receive chemoradiation as part of an attempt to control disease and potentially alter resectability.

## Palliative context

Radiation may be used to reduce symptoms such as bleeding or pain.

These intents must not be conflated.

---

# 27. Evidence-to-Patient Translation

### Technical evidence statement

TOPGEAR increased pathologic complete response but did not improve survival.

### Patient-facing translation

A treatment can make the tumor look more completely treated under the microscope without helping patients live longer. That is why doctors consider survival and other meaningful outcomes, not response alone.

### Technical evidence statement

CRITICS did not show a survival benefit for postoperative chemoradiation after preoperative chemotherapy and surgery.

### Patient-facing translation

If someone has already received chemotherapy before surgery, adding radiation afterward is not automatically better.

### Technical evidence statement

INT-0116 demonstrated a survival benefit for postoperative combined-modality therapy versus surgery alone.

### Patient-facing translation

Radiation combined with chemotherapy can be helpful after surgery in selected situations, but the circumstances of the older trial are important when deciding whether the same approach is appropriate today.

---

# 28. Metadata Integrity

No unsupported patient-specific metadata is stored in this passport.

No individualized treatment recommendation is embedded.

No dose, schedule or treatment prescription is embedded.

The passport records the package's knowledge role rather than a patient-specific plan.

---

# 29. Final Runtime Status

**Population Package:** PP-0207  
**Knowledge State:** GOLD  
**Clinical Scope:** Locked  
**Evidence Base:** Source-grounded  
**Boundary State:** Verified  
**Runtime Readiness:** Ready  
**QA Gate:** PASS — GOLD — READY FOR INTEGRATION
