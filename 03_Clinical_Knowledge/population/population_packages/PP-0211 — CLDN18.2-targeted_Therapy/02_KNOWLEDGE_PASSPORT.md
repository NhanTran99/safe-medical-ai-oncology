# 02_KNOWLEDGE_PASSPORT.md

> Knowledge Passport — PP-0211 — CLDN18.2-targeted Therapy

## Identity

|Field|Value|
|---|---|
|KP ID|KP-PP-0211|
|PP ID|PP-0211|
|Title|CLDN18.2-targeted Therapy|
|Version|1.0.0|
|Status|Approved — GOLD|

## Classification

|Field|Value|
|---|---|
|Clinical Domain|Treatment / Precision Oncology / Biomarker-Directed Therapy|
|Domain Code|TREATMENT.PRECISION.CLND18.2|
|Educational Level|Patient-facing clinical education|
|Clinical Complexity|Moderate–high|
|Patient Journey Stage|Treatment Selection → Treatment Initiation → Treatment Monitoring → Reassessment|
|Knowledge Type|Biomarker-directed treatment modality|
|Primary Treatment Node|Zolbetuximab-containing therapy|
|Prerequisite Knowledge|CLDN18.2 testing; biomarker-directed treatment selection; advanced gastric cancer systemic therapy context|

## Runtime Metadata

|Field|Value|
|---|---|
|Intended Runtime Usage|Retrieval for patient questions about CLDN18.2-targeted treatment and biomarker-directed therapy|
|Primary Retrieval Tags|CLDN18.2; zolbetuximab; Vyloy; targeted therapy; HER2-negative; CLDN18.2-positive; gastric cancer; EGJ adenocarcinoma; SPOTLIGHT; GLOW|
|Secondary Tags|biomarker-directed therapy; first-line therapy; unresectable; metastatic; mFOLFOX6; CAPOX; treatment benefit; nausea; vomiting; adverse effects|
|Negative/Boundary Tags|CLDN18.2 testing methodology; IHC scoring; zolbetuximab dosing; FLOT; neoadjuvant; adjuvant; immunotherapy; resistance mechanism|

## Clinical Knowledge Map

### Entry Question

> “My gastric cancer is CLDN18.2-positive. What does that mean for targeted treatment?”

### Retrieval Logic

- Retrieve the upstream CLDN18.2 testing package when the user asks what the test means or how positivity is established.
- Retrieve PP-0211 when the user asks what treatment CLDN18.2 positivity can lead to.
- Retrieve the Zolbetuximab package when the question is drug-specific.
- Retrieve chemotherapy packages when the question is regimen-specific.
- Retrieve toxicity/supportive-care packages when the question concerns management of adverse effects.
- Retrieve immunotherapy packages when the question concerns PD-L1, MSI-H/dMMR, immune checkpoint inhibitors, or immune-related toxicity.
- Do not infer individualized treatment eligibility from PP-0211 alone.

## Clinical Knowledge Units

|ID|Knowledge Unit|Definition|Primary Source|
|---|---|---|---|
|K01|CLDN18.2 target concept|CLDN18.2 is a treatment-relevant molecular target in gastric/EGJ adenocarcinoma.|S1; S4|
|K02|Biomarker prerequisite|CLDN18.2 assessment is relevant when zolbetuximab is being considered in the specified advanced disease setting.|S1|
|K03|Treatment population|HER2-negative, CLDN18.2-positive, unresectable locally advanced/recurrent/metastatic disease.|S1; S2|
|K04|Targeted agent|Zolbetuximab is a monoclonal antibody targeting CLDN18.2.|S1; S4; S5|
|K05|Combination paradigm|Established first-line treatment combines zolbetuximab with fluoropyrimidine/platinum-based chemotherapy.|S1; S2|
|K06|SPOTLIGHT|Zolbetuximab + mFOLFOX6 improved PFS and OS versus placebo + mFOLFOX6.|S1|
|K07|GLOW|Zolbetuximab + CAPOX improved PFS and OS versus placebo + CAPOX.|S1|
|K08|Patient interpretation|Trial benefit is population-level and not an individualized guarantee.|S1; S3; S6|
|K09|Safety|Nausea/vomiting are prominent; hematologic, hepatic and electrolyte adverse effects may occur.|S1; S4|
|K10|Boundary|Testing, scoring, drug management and detailed toxicity are separate ownerships.|S1; governance Source Files|

## Evidence Maturity Classification

### Established / Guideline-supported

- CLDN18.2 is an actionable/treatment-relevant biomarker in the specified gastric/EGJ disease context.
- Zolbetuximab is an approved CLDN18.2-targeted drug listed in the supplied NCI drug source.
- NCCN v2.2026 identifies fluoropyrimidine + oxaliplatin + zolbetuximab as a category 1 preferred first-line option for HER2-negative, CLDN18.2-positive, unresectable locally advanced, recurrent, or metastatic gastric cancer.
- NCI PDQ identifies zolbetuximab plus CAPOX or mFOLFOX6 for CLDN18.2-positive tumors in the relevant first-line palliative systemic-treatment context.
- SPOTLIGHT and GLOW provide randomized phase III evidence for PFS and OS benefit.

### Context-dependent / Patient-specific

- Whether a particular patient is a candidate for zolbetuximab.
- Which chemotherapy backbone is appropriate for an individual.
- How biomarker results interact with other disease features and biomarkers.
- How treatment is monitored and when it should be changed.
- What treatment should follow progression.

### Not Established by This Package

- A universal CLDN18.2-targeted regimen for early or resectable disease.
- A universal perioperative, neoadjuvant, or adjuvant CLDN18.2-targeted algorithm.
- A universal later-line CLDN18.2-targeted sequence.
- Individualized survival prediction from SPOTLIGHT or GLOW.
- Detailed resistance-guided treatment selection.

## Boundary Map

|Ownership|PP-0211 Position|
|---|---|
|Upstream|CLDN18.2 Testing; Biomarker Testing for Targeted Therapy|
|Parallel|HER2-targeted Therapy; other biomarker-specific treatment packages|
|Downstream|Zolbetuximab; SPOTLIGHT; GLOW; toxicity/supportive care; resistance|
|Excluded|Detailed laboratory methods, drug dosing, chemotherapy management, individualized treatment|

## Safety / Communication Rules

- Never state that CLDN18.2 positivity guarantees benefit.
- Never imply that targeted therapy means chemotherapy is unnecessary.
- Never turn population-level trial medians into individual prognosis.
- Never infer treatment eligibility from biomarker positivity without disease-context assessment.
- Never reproduce detailed dosing or toxicity-management algorithms in this package.
- Direct individualized treatment decisions to the cancer care team.

## Knowledge Graph

### Prerequisite

- CLDN18.2 Testing for Gastric Adenocarcinoma
- Biomarker Testing for Targeted Therapy
- Targeted Therapy in Gastric Cancer

### Related

- CLDN18.2 Biology
- CLDN18.2 IHC Testing
- CLDN18.2 Scoring
- HER2-targeted Therapy
- Chemotherapy
- Immunotherapy

### Next / Downstream

- Zolbetuximab
- SPOTLIGHT
- GLOW
- Treatment Toxicity / Supportive Care
- CLDN18.2 Resistance, if separately defined


## Primary Governance Sources

- CORE_WORKING_RULES v1.7 — Source-First, Gold depth, immediate post-lock artifact production, boundary declaration.
- FREEZE GOLD POPULATION PACKAGE SPECIFICATION v1.1 — four-artifact structure, Gold depth, evidence traceability, QA layers, Knowledge Graph.
- PP Discussion depth and format example — approved Discussion Batch depth and boundary style.
- PP Registry.xlsx — PP identity and neighboring package architecture.

## Revision History

| Version | Date | Change |
|---|---|---|
| 1.0.0 | 2026-08-09 | Initial GOLD Knowledge Passport following locked PP-0211 Decision Batch. |
## Extended Runtime Classification

### Query Class A — Definition

Examples:

- “What is CLDN18.2-targeted therapy?”
- “What does CLDN18.2 mean?”

Primary retrieval:
- PP-0211 CKO.

Secondary retrieval:
- CLDN18.2 Biology;
- CLDN18.2 Testing.

### Query Class B — Treatment Eligibility Concept

Examples:

- “If CLDN18.2 is positive, can I receive treatment?”
- “Who gets zolbetuximab?”

Primary retrieval:
- PP-0211.

Required contextual retrieval:
- CLDN18.2 Testing;
- HER2 Testing;
- advanced gastric-cancer systemic-treatment context.

Runtime safeguard:
- Do not convert a general answer into an individual prescription.

### Query Class C — Drug-Specific

Examples:

- “How is zolbetuximab given?”
- “What dose of zolbetuximab do I need?”
- “How do you manage zolbetuximab nausea?”

Primary retrieval:
- Zolbetuximab-specific package, when available.

PP-0211 should provide only the high-level treatment concept and safety awareness.

### Query Class D — Trial-Specific

Examples:

- “What was the SPOTLIGHT trial?”
- “What did GLOW show?”

Primary retrieval:
- dedicated trial node if available.

PP-0211 provides the clinical interpretation bridge.

### Query Class E — Testing

Examples:

- “How is CLDN18.2 tested?”
- “What percentage of cells makes the test positive?”

Primary retrieval:
- CLDN18.2 Testing / IHC / Scoring packages.

Do not use PP-0211 as the source of detailed scoring.

### Query Class F — Chemotherapy

Examples:

- “What is CAPOX?”
- “What is mFOLFOX6?”
- “How is FLOT given?”

Primary retrieval:
- chemotherapy-specific package.

PP-0211 only establishes the trial backbone relationship.

### Query Class G — Toxicity

Examples:

- “What should I do about severe vomiting?”
- “How is neutropenia managed?”

Primary retrieval:
- toxicity/supportive-care package and treating team.

PP-0211 provides awareness, not management.

## Retrieval Guardrails

### Guardrail 1 — Biomarker determinism

Never generate:

> CLDN18.2-positive = automatically eligible.

Generate:

> CLDN18.2 positivity can identify a treatment-relevant population; eligibility depends on the full clinical context.

### Guardrail 2 — Stage extrapolation

Never generalize the first-line advanced-disease evidence to early/resectable disease.

### Guardrail 3 — Regimen extrapolation

Never infer FLOT + zolbetuximab from the existence of FLOT and CLDN18.2 positivity.

### Guardrail 4 — Drug extrapolation

Do not list investigational CLDN18.2 drugs as established alternatives unless authoritative project Source Materials support them.

### Guardrail 5 — Prognostic overreach

Never turn SPOTLIGHT or GLOW median OS into an individual prognosis.

### Guardrail 6 — Toxicity overreach

Never turn the CKO safety list into a dose-modification or emergency-treatment protocol.

## Clinical Entity Map

| Entity | Relationship to PP-0211 | Runtime Role |
|---|---|---|
| CLDN18.2 | Target/biomarker | Core |
| Zolbetuximab | Targeted agent | Core / downstream drug node |
| HER2-negative | Treatment-context qualifier | Core |
| Gastric adenocarcinoma | Disease | Core |
| EGJ adenocarcinoma | Trial/treatment context | Core at supported level |
| mFOLFOX6 | SPOTLIGHT backbone | Supporting |
| CAPOX | GLOW backbone | Supporting |
| SPOTLIGHT | Pivotal trial | Supporting / downstream |
| GLOW | Pivotal trial | Supporting / downstream |
| CLDN18.2 IHC | Testing method | Delegated |
| CLDN18.2 scoring | Interpretation | Delegated |
| FLOT | Separate regimen | Excluded/delegated |
| PD-L1 | Other biomarker | Related, not core |
| MSI-H/dMMR | Other biomarker | Related, not core |
| HER2-targeted therapy | Parallel treatment node | Related |
| Resistance | Future/adjacent | Deferred |

## Patient-Journey Placement

### Before PP-0211

- diagnosis;
- staging;
- biomarker testing;
- CLDN18.2 testing;
- HER2 testing;
- systemic-treatment assessment.

### PP-0211

- understanding the targeted-treatment implication of CLDN18.2 status;
- understanding zolbetuximab-containing therapy;
- understanding evidence and treatment burden.

### After PP-0211

- drug-specific education;
- chemotherapy education;
- toxicity management;
- response assessment;
- progression/reassessment;
- subsequent treatment.

## Knowledge Graph Semantics

### `requires`

PP-0211 `requires` clinically interpretable CLDN18.2 status.

### `informs`

CLDN18.2 status `informs` treatment consideration.

### `targets`

Zolbetuximab `targets` CLDN18.2.

### `combines_with`

Zolbetuximab `combines_with` fluoropyrimidine/platinum chemotherapy in the evidence-supported first-line paradigm.

### `supported_by`

PP-0211 `supported_by` SPOTLIGHT and GLOW evidence.

### `delegates_to`

PP-0211 `delegates_to` drug-specific management, testing methodology, toxicity management and detailed resistance.

## Governance Interpretation

This Knowledge Passport is intentionally not a prescribing object.

Its role is to support:

- retrieval;
- contextual understanding;
- patient education;
- evidence linkage;
- boundary-aware navigation.

It should not be used as:

- a stand-alone treatment order;
- a dose calculator;
- an adverse-event management protocol;
- a laboratory scoring tool;
- an individualized prognosis model.

## Maintenance Rules

Review PP-0211 when:

1. NCCN changes the CLDN18.2 pathway.
2. Regulatory status of zolbetuximab changes.
3. A new phase III trial materially changes efficacy interpretation.
4. A new standard CLDN18.2-targeted therapy becomes established.
5. A dedicated resistance package is added.
6. CLDN18.2 testing criteria materially change.
7. New safety information changes the patient-facing risk description.

Do not update the package merely because a new experimental drug appears in the literature unless the project Source Materials and governance scope support incorporation.

## Extended Knowledge Unit Set

| ID | Unit | Patient-facing question | Boundary |
|---|---|---|---|
| K11 | Target biology | “Why can CLDN18.2 be targeted?” | Foundational only |
| K12 | Biomarker meaning | “What does positive mean?” | Treatment context, not scoring |
| K13 | HER2 relationship | “Why does HER2 status matter?” | Context only |
| K14 | Disease setting | “Which stage is this treatment for?” | Advanced/unresectable/recurrent/metastatic |
| K15 | Treatment line | “When is this treatment used?” | First-line evidence |
| K16 | Combination | “Is it chemotherapy or targeted therapy?” | Combination paradigm |
| K17 | SPOTLIGHT | “What did the trial show?” | High-level evidence |
| K18 | GLOW | “What did the second trial show?” | High-level evidence |
| K19 | Benefit | “How much benefit was seen?” | Population-level |
| K20 | Safety | “What side effects matter?” | Awareness only |
| K21 | Reassessment | “What if treatment stops working?” | Conceptual |
| K22 | Patient communication | “What should I ask?” | Practical questions |

## Knowledge Dependencies

### Dependency D01

**CLDN18.2 Testing → PP-0211**

The treatment node depends on a clinically interpretable biomarker result.

### Dependency D02

**HER2 Testing → PP-0211**

The current preferred zolbetuximab pathway is defined under HER2-negative disease.

### Dependency D03

**Advanced disease assessment → PP-0211**

The evidence-supported population is not an all-stage gastric-cancer population.

### Dependency D04

**Systemic-treatment assessment → PP-0211**

The targeted modality exists within a broader treatment plan.

## Retrieval Examples

### Query

> “What is zolbetuximab?”

Retrieve PP-0211 for modality context and the drug-specific node for detailed information.

### Query

> “My CLDN18.2 test says positive. What does that mean?”

Retrieve:

1. CLDN18.2 Testing;
2. PP-0211.

### Query

> “What is the CLDN18.2 positive cutoff?”

Do not answer from PP-0211.

Retrieve CLDN18.2 Scoring/IHC Testing.

### Query

> “Can I use zolbetuximab with FLOT?”

Do not infer.

Retrieve:

- Zolbetuximab;
- FLOT;
- current treatment-setting guidance.

### Query

> “What happened in SPOTLIGHT?”

Retrieve the trial-specific node if available, with PP-0211 as the treatment-context bridge.

### Query

> “What are zolbetuximab side effects?”

Retrieve the drug-specific/toxicity node, with PP-0211 as high-level context.

## Runtime Safety Filters

### Filter F01

If the user asks for a personal treatment decision, PP-0211 can explain the evidence but must not decide for the patient.

### Filter F02

If the user provides a personal biomarker result, the package can explain what the result generally means but cannot independently establish eligibility.

### Filter F03

If the user asks for dosing, route or schedule, route to drug-specific content.

### Filter F04

If the user asks about severe toxicity, route to toxicity/supportive-care content and clinical care.

### Filter F05

If the user asks about later-line treatment, route to the appropriate treatment-sequencing package.

## Knowledge Graph Edge Rules

### Upstream edge

`CLDN18.2 Testing` —provides—> `CLDN18.2 status`

### Treatment edge

`CLDN18.2-positive + appropriate disease context` —supports consideration of—> `CLDN18.2-targeted Therapy`

### Drug edge

`CLDN18.2-targeted Therapy` —includes—> `Zolbetuximab`

### Evidence edge

`Zolbetuximab-containing therapy` —supported by—> `SPOTLIGHT`

`Zolbetuximab-containing therapy` —supported by—> `GLOW`

### Safety edge

`Zolbetuximab-containing therapy` —has—> `Treatment-related adverse effects`

### Delegation edge

`PP-0211` —delegates—> `Testing methodology`

`PP-0211` —delegates—> `Drug-specific management`

`PP-0211` —delegates—> `Resistance`

## Maintenance Priority

### Priority 1 — Immediate review

- NCCN treatment recommendation changes.
- Regulatory indication changes.
- Major new phase III trial.
- Major safety signal.

### Priority 2 — Planned review

- New validated CLDN18.2 testing standards.
- New clinically established CLDN18.2-targeted agents.
- New evidence for other treatment settings.

### Priority 3 — Architecture review

- Addition of dedicated resistance package.
- Addition of dedicated trial packages.
- New downstream toxicity package.
- New combination-therapy package.

## Governance Status

| Governance Item | Status |
|---|---|
| Decision Batch | LOCKED |
| Gold structure | LOCKED |
| Gold depth | LOCKED |
| Source-first requirement | LOCKED |
| Boundary | LOCKED |
| Knowledge Graph | LOCKED for v1.0.0 |
| Version | 1.0.0 |
| Production status | GOLD |
| Integration status | READY |
