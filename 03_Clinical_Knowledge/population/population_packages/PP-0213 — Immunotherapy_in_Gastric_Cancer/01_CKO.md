# 01_CKO.md

# Clinical Knowledge Object

## Metadata

| Field | Value |
|---|---|
| CKO ID | CKO-PP-0213 |
| PP ID | PP-0213 |
| Title | Immunotherapy in Gastric Cancer |
| Clinical Domain | Treatment / Systemic Therapy / Immuno-Oncology |
| Population Wave | Population Package execution wave |
| Version | 1.0.0 |
| Status | GOLD — READY FOR INTEGRATION |
| Audience | Patients, caregivers, general oncology learners, and clinicians requiring a patient-facing knowledge layer |
| Reading Level | Patient-facing plain language with medical terminology explained at first use |
| Last Updated | 2026-08-09 |
| Evidence Basis | Project Source Files; source-first production |
| Decision Status | APPROVED / LOCKED |

---

# Educational Objectives

After reading this Population Package, the reader should be able to:

1. Explain what cancer immunotherapy means and how it differs conceptually from chemotherapy and classical targeted therapy.
2. Explain, at a high level, why immune checkpoints can prevent immune cells from attacking cancer and how checkpoint inhibitors can interfere with that process.
3. Understand that immune checkpoint inhibition is the dominant established immunotherapy paradigm represented in the supplied gastric-cancer clinical sources.
4. Understand why immunotherapy is not a single treatment and why different drugs, combinations, treatment settings, and biomarkers can lead to different clinical uses.
5. Understand the broad role of PD-L1 and MSI-H/dMMR status in immunotherapy treatment selection without turning this package into a biomarker-testing manual.
6. Recognize that immunotherapy can be used in selected perioperative and advanced/metastatic gastric-cancer settings.
7. Understand the evidence logic behind representative gastric-cancer immunotherapy trials, including CheckMate-649, KEYNOTE-859, RATIONALE-305, KEYNOTE-811, and MATTERHORN.
8. Understand that immunotherapy can produce durable benefit in some patients but is not universally effective.
9. Recognize that immune-related adverse events are a distinctive safety issue and that new symptoms during immunotherapy should be reported to the treating team.
10. Understand why response assessment can sometimes be more complex with immunotherapy, including delayed response and pseudoprogression.
11. Understand which detailed topics are deliberately delegated to adjacent Population Packages.

---

# Scope

## Included

This Population Package owns the **clinical immunotherapy framework for gastric/EGJ adenocarcinoma**.

The package covers:

- the meaning of immunotherapy in cancer;
- the immune-system and immune-checkpoint concept at clinically useful depth;
- PD-1/PD-L1 and CTLA-4 as conceptual immune-checkpoint mechanisms;
- immune checkpoint inhibitors as the dominant established immunotherapy paradigm in the supplied gastric-cancer evidence;
- the difference between immunotherapy, chemotherapy, and classical targeted therapy;
- immunotherapy alone versus combination treatment at conceptual level;
- treatment-setting dependence;
- perioperative/neoadjuvant immunotherapy;
- advanced/metastatic immunotherapy;
- HER2-positive immunotherapy combinations as an example of multimodality treatment;
- HER2-negative immunotherapy combinations;
- MSI-H/dMMR as a major immunotherapy-relevant tumor context;
- PD-L1 as a major but not universal treatment-selection context;
- TMB-H as a limited contextual example where supported;
- representative landmark clinical evidence;
- benefits, limitations, resistance concept, and evidence uncertainty;
- durable responses;
- unconventional response patterns;
- immune-related adverse-event awareness;
- patient-facing questions and misconceptions;
- the clinical boundary between this umbrella package and downstream immunotherapy-specific packages.

## Not Included

The following are intentionally outside the substantive ownership of PP-0213:

- detailed immune checkpoint inhibitor pharmacology;
- drug-specific dosing and administration;
- detailed agent-by-agent prescribing instructions;
- detailed PD-L1 laboratory methodology;
- CPS/TAP scoring methodology;
- MSI/MMR laboratory methodology;
- TMB laboratory methodology;
- individualized biomarker-report interpretation;
- individualized treatment recommendations;
- detailed treatment sequencing;
- detailed treatment-duration decisions;
- detailed immune-related adverse-event grading and management algorithms;
- detailed RECIST/iRECIST methodology;
- detailed imaging methodology;
- detailed HER2-targeted therapy;
- detailed CLDN18.2-targeted therapy;
- detailed anti-angiogenic therapy;
- experimental cellular immunotherapy, cancer vaccines, or other investigational immunotherapy unless separately assigned;
- individualized prognosis.

---

# Clinical Knowledge Blocks

## Block 1 — What Is Immunotherapy?

Immunotherapy is treatment that helps the person's immune system recognize and attack cancer more effectively.

The American Cancer Society describes immunotherapy for stomach cancer as medicines that help a person's own immune system find and destroy cancer cells more effectively. The supplied NCI stomach-cancer treatment source likewise identifies immunotherapy as one of the treatment categories used for stomach cancer and notes that biomarker testing may help predict response to some immunotherapy drugs.

The important concept is that immunotherapy does not simply mean “turning the immune system on.” The immune system already has powerful mechanisms for controlling when immune cells should attack. Cancer can exploit some of those regulatory mechanisms to reduce immune attack.

The clinical immunotherapy paradigm covered by this package is therefore primarily about **changing immune regulation so that an existing anti-tumor immune response can work more effectively**.

---

## Block 2 — Why Does the Immune System Need Checkpoints?

The immune system needs safeguards because uncontrolled immune activation could damage normal tissues.

Immune checkpoint proteins act as regulatory signals. The American Cancer Society explains that checkpoint proteins on immune cells can function like switches that help regulate whether an immune response proceeds.

PD-1 is a checkpoint protein on T cells. When PD-1 interacts with PD-L1, the interaction can reduce T-cell attack. Some cancer cells can exploit this pathway by expressing PD-L1 and thereby helping themselves avoid immune attack.

Checkpoint inhibitors interfere with this inhibitory signaling.

The simplified concept is:

**Cancer cell / tumor environment**

↓ inhibitory checkpoint signaling

**T-cell activity is reduced**

Checkpoint inhibitor

↓

**inhibitory signal is blocked or weakened**

↓

**anti-tumor immune activity can become more effective**

This is a conceptual explanation, not a complete description of tumor immunology.

---

## Block 3 — Immunotherapy Is Not One Treatment

“Immunotherapy” is a treatment category rather than one drug.

The project sources identify multiple immune checkpoint inhibitors used in gastric-cancer contexts, including:

- durvalumab;
- nivolumab;
- pembrolizumab;
- tislelizumab;
- dostarlimab.

The exact role of an agent depends on the disease setting, biomarker context, treatment line, combination partner, and evidence supporting that particular use.

Therefore it is unsafe to reason:

> “Immunotherapy works, so any immunotherapy drug should work for this patient.”

The correct reasoning is:

> **Which immunotherapy strategy has evidence in this specific gastric-cancer setting and patient population?**

Detailed agent-specific ownership belongs to PP-0214 and related treatment-specific packages.

---

## Block 4 — Immunotherapy Versus Chemotherapy

Chemotherapy uses anticancer drugs that generally kill cancer cells or stop them from dividing.

Immunotherapy works through the patient's immune system.

These mechanisms are different, but the treatments can be used together.

This is clinically important because many modern gastric-cancer immunotherapy regimens combine a checkpoint inhibitor with chemotherapy.

The combination is not redundant:

- chemotherapy can directly affect tumor cells;
- immunotherapy can modify immune regulation;
- the combination may improve treatment outcomes in selected populations.

The NCI and ACS sources both support the concept that immunotherapy may be used with other treatments, including chemotherapy.

---

## Block 5 — Immunotherapy Versus Classical Targeted Therapy

Classical targeted therapy generally acts against a defined molecular target or pathway associated with the cancer.

Examples in gastric cancer include:

- HER2-directed therapy;
- CLDN18.2-directed therapy;
- VEGFR-directed anti-angiogenic therapy.

Immunotherapy targets immune-regulatory mechanisms rather than simply attacking a tumor-specific molecular pathway in the same way.

There can be overlap in terminology because checkpoint inhibitors are themselves directed against specific molecules such as PD-1, PD-L1, or CTLA-4. The clinically important distinction is the **therapeutic mechanism and treatment logic**.

This package introduces the distinction; detailed targeted therapies are owned by PP-0210, PP-0211, PP-0212, and related packages.

---

## Block 6 — Why Biomarkers Matter

Immunotherapy is not automatically appropriate for every patient with gastric cancer.

The supplied NCCN pathway demonstrates that treatment selection may incorporate:

- HER2 status;
- PD-L1 expression;
- MSI-H/dMMR status;
- treatment setting;
- disease extent;
- other clinical factors.

NCI also states that biomarker testing may help predict response to certain immunotherapy drugs.

A key point is:

> **There is no single universal immunotherapy biomarker rule.**

PD-L1 is important for several immunotherapy pathways, but MSI-H/dMMR disease can have immunotherapy indications independent of PD-L1 status in the current NCCN framework.

Detailed testing and scoring are delegated to dedicated biomarker packages.

---

## Block 7 — PD-L1: Important but Not Universal

PD-L1 can be reported using different scoring approaches. In the current NCCN gastric-cancer material, both Combined Positive Score (CPS) and Tumor Area Positivity (TAP) appear in treatment contexts.

For example, current NCCN first-line advanced-disease pathways include:

- nivolumab + chemotherapy for HER2-negative disease with PD-L1 CPS ≥1, with category 1 designation at CPS ≥5;
- pembrolizumab + chemotherapy in similar PD-L1 contexts;
- tislelizumab + chemotherapy in the corresponding PD-L1 context;
- pembrolizumab + trastuzumab + chemotherapy for HER2-positive disease with PD-L1 CPS ≥1.

However, the current NCCN pathway separately identifies MSI-H/dMMR tumors as an immunotherapy-relevant group **independent of PD-L1 status**.

Therefore:

> **PD-L1 is clinically important, but it is not a universal gatekeeper for all immunotherapy strategies.**

PP-0216 owns detailed PD-L1-guided treatment.

---

## Block 8 — MSI-H/dMMR: A Distinct Immunotherapy-Relevant Context

Microsatellite instability-high (MSI-H) and mismatch-repair deficient (dMMR) tumors represent an important biologic subgroup.

The current NCCN pathway includes multiple immunotherapy strategies for MSI-H/dMMR tumors independent of PD-L1 status.

The supplied NCCN discussion reports particularly strong survival signals in MSI-H subgroups from CheckMate-649. In patients with MSI-H tumors, nivolumab-containing strategies showed substantial benefit compared with chemotherapy in the reported analyses.

This supports an important educational principle:

> **The biological context of the tumor can materially change the expected relevance of immunotherapy.**

PP-0215 owns the detailed MSI-H/dMMR and immunotherapy package.

---

## Block 9 — Perioperative / Neoadjuvant Immunotherapy

Immunotherapy is no longer limited to metastatic disease.

Current NCCN v2.2026 includes:

- FLOT + durvalumab as a preferred perioperative option for selected patients;
- PD-L1 CPS ≥1 or TAP ≥1% as a category 1 context;
- clinical node-negative disease as an additional specified context;
- category 2B use in selected PD-L1-negative/TAP-negative and diffuse-type contexts;
- selected neoadjuvant/perioperative immunotherapy strategies for MSI-H/dMMR tumors.

This represents an important evolution of the treatment landscape.

However, perioperative immunotherapy must not be presented as universally beneficial.

The NCCN discussion of MATTERHORN reports:

- 948 untreated patients with resectable gastric or EGJ adenocarcinoma;
- durvalumab + FLOT versus placebo + FLOT;
- 24-month event-free survival of 67.4% versus 58.5%;
- HR for event or death 0.71;
- the PD-L1 TAP ≥1% subgroup had HR 0.70;
- the TAP <1% subgroup had HR 0.77 with a wide confidence interval;
- importantly, diffuse-type tumors did not show an EFS advantage, with HR 0.93.

Therefore the correct patient-facing message is:

> **Perioperative immunotherapy can be beneficial in selected settings, but the benefit is not uniform across all patient or tumor subgroups.**

---

## Block 10 — Advanced / Metastatic Disease

Advanced or metastatic gastric cancer is a major established setting for immunotherapy.

Current NCCN v2.2026 lists several first-line immunotherapy-containing approaches.

### HER2-positive disease

Selected patients with PD-L1 CPS ≥1 may receive:

**fluoropyrimidine + platinum + trastuzumab + pembrolizumab**

This illustrates that immunotherapy may be combined with another targeted treatment.

### HER2-negative disease

Current preferred pathways include:

- fluoropyrimidine + oxaliplatin + nivolumab for PD-L1 CPS ≥1;
- fluoropyrimidine + oxaliplatin + pembrolizumab for PD-L1 CPS ≥1;
- fluoropyrimidine + oxaliplatin + tislelizumab for PD-L1 CPS ≥1;

with stronger category 1 positioning at higher PD-L1 thresholds as specified by NCCN.

These are guideline-level treatment pathways, not individualized prescriptions.

---

## Block 11 — CheckMate-649

CheckMate-649 is a landmark first-line trial supporting nivolumab + chemotherapy in advanced gastric/GEJ/esophageal adenocarcinoma.

The supplied NCCN evidence reports that in the PD-L1 CPS ≥5 population:

- median OS was 14.4 months versus 11.1 months;
- HR was 0.70;
- median PFS was 8.3 versus 6.1 months;
- HR was 0.70.

At longer follow-up, the benefit remained evident.

The reported 3-year analysis also showed:

- objective response rate 60% versus 45%;
- complete response rate 13% versus 7%.

In the PD-L1 CPS ≥1 population:

- median OS was 13.8 versus 11.3 months;
- HR 0.75;
- median PFS 7.5 versus 6.9 months;
- HR 0.77.

The educational importance of CheckMate-649 is not simply that “nivolumab works.” It demonstrates:

1. a randomized phase III evidence base;
2. benefit from adding immunotherapy to chemotherapy;
3. the importance of defining the population in which the treatment was studied;
4. the relevance of PD-L1 context;
5. the fact that effect size is population-level evidence rather than a guarantee for an individual.

---

## Block 12 — KEYNOTE-859

KEYNOTE-859 provides major phase III evidence for pembrolizumab + chemotherapy in advanced HER2-negative gastric/GEJ adenocarcinoma.

The supplied NCCN evidence reports:

### PD-L1 CPS ≥10

- median OS 15.7 versus 11.8 months;
- HR 0.65;
- median PFS 8.1 versus 5.6 months;
- HR 0.62;
- objective response 61% versus 43%.

### PD-L1 CPS ≥1

- median OS 13.0 versus 11.4 months;
- HR 0.74;
- median PFS 6.9 versus 5.6 months;
- HR 0.72;
- objective response 52% versus 43%.

The key lesson is that the benefit of an immunotherapy combination should always be interpreted in relation to the studied population and biomarker-defined context.

---

## Block 13 — RATIONALE-305

RATIONALE-305 is a phase III trial supporting tislelizumab + chemotherapy.

The supplied NCCN evidence reports:

- 501 patients received tislelizumab + chemotherapy;
- 496 received placebo + chemotherapy;
- median OS 15.0 versus 12.9 months;
- HR 0.80;
- median PFS 6.9 versus 6.2 months;
- HR 0.78.

In the PD-L1 TAP ≥5% subgroup:

- median OS 17.2 versus 12.6 months;
- HR 0.74;
- median PFS 7.2 versus 5.9 months;
- HR 0.67.

The trial also provides a useful example of why different PD-L1 scoring frameworks must be understood in context: the NCCN discussion notes high concordance between TAP and CPS in the reported analysis.

---

## Block 14 — KEYNOTE-811

KEYNOTE-811 is important because it demonstrates an immunotherapy strategy combined with HER2-targeted therapy.

The current NCCN pathway includes:

**fluoropyrimidine + platinum + trastuzumab + pembrolizumab**

for selected HER2-positive advanced disease with PD-L1 CPS ≥1.

The educational point is:

> Immunotherapy can be integrated into a multimodality systemic regimen rather than used as an isolated treatment.

Detailed HER2 biology, testing, trastuzumab treatment, and HER2-specific safety remain outside this package.

---

## Block 15 — MSI-H/dMMR Evidence and CheckMate-649

The supplied NCCN discussion reports strong MSI-H subgroup findings.

Among all randomized patients with MSI-H tumors:

- median OS was 38.7 versus 12.3 months;
- HR 0.34.

For nivolumab + ipilimumab compared with chemotherapy in MSI-H tumors:

- median OS was not reached versus 10 months;
- HR 0.28;
- objective response was 70% versus 57%.

The NCCN discussion also notes that there was no survival benefit for nivolumab + ipilimumab in the microsatellite-stable cohort in that analysis.

These results should be interpreted as subgroup evidence, not as a promise that every MSI-H/dMMR patient will have a durable response.

---

## Block 16 — TMB-H: Context, Not a Universal Gastric-Cancer Rule

Tumor mutational burden-high (TMB-H) can be relevant to tumor-agnostic immunotherapy concepts.

However, the supplied NCCN evidence notes an important limitation: no gastroesophageal cancers were included in the relevant KEYNOTE-158 TMB analysis used for that evidence.

Therefore PP-0213 should not present TMB-H as having the same gastric-cancer-specific evidence maturity as:

- PD-L1 in defined gastric-cancer treatment pathways;
- MSI-H/dMMR in gastric-cancer immunotherapy pathways.

The correct framing is:

> TMB-H is a recognized immunotherapy-related biomarker context, but the direct gastric/GEJ evidence in the supplied materials is more limited.

Detailed TMB ownership remains with the dedicated biomarker package.

---

## Block 17 — Durable Responses

One important feature of immunotherapy is the possibility of a durable response in some patients.

ESMO-ASCO identifies durable responses as a key immunotherapy concept.

However:

- durable benefit is not universal;
- not every patient responds;
- resistance can develop;
- response duration cannot be predicted from the general package for an individual patient.

The correct patient-facing message is:

> **Some patients can experience long-lasting benefit from immunotherapy, but this is not guaranteed.**

---

## Block 18 — Unconventional Response Patterns

Immunotherapy can produce response patterns that differ from conventional cytotoxic treatment.

ESMO-ASCO identifies:

- late responses;
- regression after apparent progression;
- pseudoprogression;
- mixed response;
- hyperprogression.

This does not mean that every apparent progression is pseudoprogression.

The clinical principle is:

> **Imaging changes during immunotherapy sometimes require careful clinical interpretation rather than an automatic assumption that treatment has failed.**

Formal response criteria and imaging interpretation belong to PP-0217, PP-0218, and PP-0219.

---

## Block 19 — Immune-Related Adverse Events

Checkpoint inhibition can produce a distinctive toxicity pattern because immune activation can affect normal tissues.

The supplied ACS source identifies common side effects such as:

- fatigue;
- fever;
- cough;
- nausea;
- itching;
- rash;
- appetite loss;
- muscle or joint pain;
- constipation or diarrhea.

It also describes more serious immune-mediated reactions that can affect:

- lungs;
- intestines;
- liver;
- hormone-producing glands;
- kidneys;
- skin;
- other organs.

ESMO-ASCO similarly emphasizes immune-related adverse events affecting skin, endocrine, gastrointestinal, pulmonary, and hepatic systems and stresses the need to distinguish immune toxicity from non-immune toxicity and disease progression.

### Patient-facing safety principle

A new or worsening symptom during immunotherapy should be reported to the cancer-care team rather than assumed to be an ordinary side effect.

This package does not provide treatment-hold, corticosteroid, or organ-specific management algorithms.

---

## Block 20 — Immunotherapy and Treatment Combination

Immunotherapy may be combined with:

- chemotherapy;
- targeted therapy;
- other immunotherapy agents;
- selected perioperative treatment programs.

The combination may be rational because different treatment components act through different biological mechanisms.

But combinations can also increase complexity and toxicity.

ESMO-ASCO specifically highlights both the potential benefits and unique side effects of combining immunotherapy with conventional therapeutics such as chemotherapy, targeted therapy, and radiation therapy.

Therefore:

> **Combination therapy should be understood as evidence-dependent, not automatically better than single-agent treatment.**

---

## Block 21 — Treatment Setting Changes the Meaning of Immunotherapy

The same word “immunotherapy” can refer to different clinical goals.

### Perioperative / neoadjuvant setting

The goal is integrated management of potentially resectable disease and may include treatment before and after surgery.

### Advanced/metastatic setting

The goals may include disease control, prolongation of survival, symptom control, and maintenance of quality of life.

Therefore:

> **Immunotherapy itself is not inherently “curative” or “palliative.” The treatment setting determines the clinical goal.**

---

## Block 22 — Treatment Selection Is Multidimensional

The appropriate immunotherapy strategy depends on more than one test.

Relevant factors can include:

- disease stage and resectability;
- HER2 status;
- PD-L1 status;
- MSI-H/dMMR status;
- previous therapy;
- performance status;
- comorbidities;
- nutritional condition;
- expected toxicity;
- patient preferences;
- available evidence.

NCI emphasizes that treatment plans are developed with the cancer-care team and consider stage, overall health, preferences, treatment goals, and potential side effects.

This package therefore does not convert one biomarker into an automatic treatment instruction.

---

## Block 23 — Resistance

Immunotherapy resistance can be:

- primary, where the tumor does not respond initially;
- acquired, where a previously responsive tumor later progresses.

ESMO-ASCO identifies primary and acquired resistance as core immunotherapy concepts.

At the patient-facing level:

> A lack of response or later progression does not necessarily mean that immunotherapy was “wrong”; cancer biology can change and resistance can develop.

Detailed mechanisms and resistance-management strategies are delegated to dedicated downstream packages.

---

# Patient Explanation

## “What is immunotherapy for stomach cancer?”

Immunotherapy is a type of cancer treatment that helps your immune system recognize and attack cancer more effectively.

For gastric cancer, the most established form of immunotherapy in the supplied clinical sources is treatment that blocks immune “checkpoint” signals.

These checkpoint signals normally help prevent the immune system from attacking healthy cells. Cancer can sometimes use them to avoid immune attack.

Checkpoint inhibitors interfere with those signals, allowing immune cells to attack cancer more effectively.

---

## “Is immunotherapy the same as chemotherapy?”

No.

Chemotherapy directly affects cancer cells through anticancer drugs.

Immunotherapy works by changing how the immune system responds to cancer.

They can be used together because they work in different ways.

---

## “Does everyone with gastric cancer need immunotherapy?”

No.

Immunotherapy is useful in selected situations.

The decision depends on the type and stage of cancer, treatment setting, biomarkers such as PD-L1 or MSI-H/dMMR in appropriate contexts, previous treatments, overall health, and the evidence supporting a particular regimen.

---

## “Does PD-L1 have to be positive?”

Not for every immunotherapy strategy.

PD-L1 is important for several current gastric-cancer treatment pathways.

However, current NCCN guidance also identifies immunotherapy strategies for MSI-H/dMMR tumors that are independent of PD-L1 status.

---

## “Can immunotherapy be used before surgery?”

Yes, in selected situations.

Current NCCN guidance includes perioperative FLOT plus durvalumab for selected patients and selected neoadjuvant/perioperative immunotherapy approaches for MSI-H/dMMR tumors.

The exact suitability depends on the clinical situation.

---

## “Can immunotherapy be combined with targeted therapy?”

Yes.

For example, pembrolizumab can be combined with trastuzumab and chemotherapy in selected HER2-positive advanced gastric/EGJ adenocarcinoma.

This does not mean that every targeted therapy should be combined with immunotherapy.

---

## “Can immunotherapy cause side effects?”

Yes.

Immune checkpoint inhibitors have a distinctive toxicity pattern.

The immune system can sometimes attack normal organs, including the skin, intestines, liver, lungs, kidneys, or hormone-producing glands.

New symptoms should be reported promptly to the cancer-care team.

---

## “If my scan looks worse, does that always mean immunotherapy failed?”

No.

Some immunotherapy responses can be delayed or can initially look unusual.

Pseudoprogression and mixed response are recognized concepts.

However, apparent progression must still be assessed carefully; worsening disease should never simply be assumed to be pseudoprogression.

---

## “Does immunotherapy always give a long-lasting response?”

No.

Some patients experience durable benefit, but others do not respond or eventually develop resistance.

---

# Clinical Importance

Immunotherapy has become an established component of modern gastric-cancer treatment.

The clinical importance of PP-0213 is therefore not simply to explain a drug class. It provides the conceptual bridge between:

**tumor biology**

→ **immune recognition**

→ **checkpoint regulation**

→ **immunotherapy**

→ **biomarker/context**

→ **treatment setting**

→ **clinical evidence**

→ **benefit and toxicity**

→ **patient interpretation**

This bridge is necessary before a reader enters the more specialized packages:

- immune checkpoint inhibitors;
- MSI-H/dMMR and immunotherapy;
- PD-L1-guided immunotherapy.

---

# Common Misconceptions

## Myth 1 — “Immunotherapy just boosts the whole immune system.”

**Fact:** Checkpoint inhibitors act on specific immune-regulatory pathways. They do not simply activate every part of the immune system.

## Myth 2 — “Every gastric-cancer patient should receive immunotherapy.”

**Fact:** Treatment is context-dependent and depends on disease setting, biomarkers, prior therapy, health, and evidence.

## Myth 3 — “PD-L1 must be positive for immunotherapy.”

**Fact:** PD-L1 is important in several treatment pathways, but MSI-H/dMMR-related immunotherapy strategies can be independent of PD-L1 status.

## Myth 4 — “Immunotherapy is always safer than chemotherapy.”

**Fact:** Its toxicity profile is different, not necessarily safer. Immune-mediated complications can be serious.

## Myth 5 — “If the scan gets worse, immunotherapy definitely failed.”

**Fact:** Some unconventional response patterns exist, but progression must still be clinically evaluated.

## Myth 6 — “Immunotherapy always produces a durable response.”

**Fact:** Some patients have durable benefit; others do not respond or develop resistance.

## Myth 7 — “A biomarker result automatically tells the doctor which immunotherapy to prescribe.”

**Fact:** Biomarkers contribute to treatment selection but must be interpreted together with disease setting, prior treatment, patient factors, and guideline-supported evidence.

## Myth 8 — “Immunotherapy only applies to metastatic disease.”

**Fact:** Current evidence and NCCN guidance also include selected perioperative and neoadjuvant contexts.

---

# Key Messages

1. Immunotherapy helps the immune system attack cancer more effectively.
2. Immune checkpoint inhibition is the dominant established immunotherapy paradigm in the supplied gastric-cancer sources.
3. Immunotherapy is a category, not one drug.
4. Immunotherapy differs from chemotherapy and classical targeted therapy, but it can be combined with both.
5. PD-L1 can guide treatment in several settings, but it is not a universal requirement.
6. MSI-H/dMMR is a particularly important immunotherapy-relevant tumor context.
7. Immunotherapy is now relevant in selected perioperative as well as advanced/metastatic gastric-cancer settings.
8. Landmark trials demonstrate benefit in selected populations, not universal benefit for every patient.
9. Some patients experience durable responses, while others have primary or acquired resistance.
10. Immune-related adverse events are distinctive and can be serious.
11. Unusual response patterns can occur, so apparent progression may require careful assessment.
12. Detailed biomarker testing, checkpoint-inhibitor management, toxicity management, response assessment, and individualized treatment decisions belong to dedicated downstream packages.

---

# Patient Questions

A patient discussing immunotherapy with the cancer-care team may ask:

1. What is the goal of immunotherapy in my treatment plan?
2. Is immunotherapy being used before surgery, after surgery, or for advanced disease?
3. Why is this particular immunotherapy drug being considered?
4. What do my HER2, PD-L1, and MSI/MMR results mean for treatment selection?
5. Is PD-L1 required for the treatment being considered?
6. Is my cancer MSI-H or dMMR?
7. Is immunotherapy being combined with chemotherapy or targeted therapy?
8. What benefits were shown in patients similar to me?
9. What side effects should I report immediately?
10. Could a new symptom be related to immune activation?
11. How will my doctors determine whether treatment is working?
12. If a scan looks worse, how will the team distinguish progression from an unusual immunotherapy response?
13. What happens if the cancer does not respond?
14. What happens if the cancer initially responds and later grows again?
15. Are there clinical trials relevant to my situation?

---

# Knowledge Graph

## Prerequisite PPs

- PP-0028 — Treatment Overview
- PP-0208 — Palliative Systemic Therapy
- PP-0209 — Targeted Therapy in Gastric Cancer
- PP-0014 — Foundational Immunotherapy for Gastric Adenocarcinoma
- PP-0182 — MSI/MMR Testing
- PP-0183 — PD-L1 Testing
- PP-0191 — Biomarker Testing for Immunotherapy

These packages provide broader treatment, biomarker, and foundational immunotherapy context.

## Related PPs

- PP-0210 — HER2-targeted Therapy
- PP-0211 — CLDN18.2-targeted Therapy
- PP-0212 — Anti-angiogenic Therapy
- PP-0217 — Response Assessment
- PP-0231 — Treatment-related Toxicity and Supportive Care
- PP-0232 — Multidisciplinary Management of Gastric Cancer

## Next / Downstream PPs

- PP-0214 — Immune Checkpoint Inhibitors
- PP-0215 — MSI-H/dMMR Gastric Cancer and Immunotherapy
- PP-0216 — PD-L1-guided Immunotherapy
- PP-0217 — Response Assessment
- PP-0218 — RECIST-based Assessment
- PP-0219 — Post-treatment Imaging
- PP-0231 — Treatment-related Toxicity and Supportive Care

---

# Clinical Safety Boundary

PP-0213 provides **safety literacy**, not individualized toxicity management.

It is appropriate to explain:

- immune-related adverse events exist;
- symptoms may involve multiple organs;
- immune toxicity can differ from chemotherapy toxicity;
- new symptoms should be reported promptly;
- progression and immune toxicity can sometimes resemble other clinical problems.

It is not appropriate for PP-0213 to provide:

- corticosteroid dose;
- treatment-hold thresholds;
- organ-specific immunosuppression protocols;
- rechallenge algorithms;
- individualized treatment modification.

Those belong to dedicated toxicity/supportive-care resources.

---

# Boundary

## Core

Immunotherapy as a gastric/EGJ adenocarcinoma treatment modality; immune/checkpoint mechanism at conceptual clinical depth; immune checkpoint inhibition as the dominant established paradigm; treatment-setting dependence; biomarker relevance at conceptual level; perioperative and advanced/metastatic applications; representative immunotherapy combinations; landmark clinical evidence; benefits, limitations, durable response, resistance concept, unconventional response patterns, immune-related safety awareness, and patient-facing interpretation.

## Supporting

PD-L1 CPS/TAP conceptual context; MSI-H/dMMR relevance; TMB-H as a limited contextual biomarker; HER2 + immunotherapy combinations; FLOT + durvalumab; CheckMate-649, KEYNOTE-859, RATIONALE-305, KEYNOTE-811 and MATTERHORN evidence; patient questions and misconceptions.

## Explicitly Excluded

Detailed checkpoint-inhibitor pharmacology; dosing/administration; detailed biomarker-testing methodology or scoring; individualized biomarker interpretation; detailed immune-related adverse-event management; detailed response-assessment methodology; individualized treatment selection/sequencing; detailed HER2/CLDN18.2/anti-angiogenic treatment; experimental cellular/vaccine immunotherapy; individualized prognosis.

## Delegated-to PP

PP-0209 Targeted Therapy in Gastric Cancer; PP-0210 HER2-targeted Therapy; PP-0211 CLDN18.2-targeted Therapy; PP-0212 Anti-angiogenic Therapy; PP-0214 Immune Checkpoint Inhibitors; PP-0215 MSI-H/dMMR Gastric Cancer and Immunotherapy; PP-0216 PD-L1-guided Immunotherapy; PP-0217 Response Assessment; PP-0218 RECIST-based Assessment; PP-0219 Post-treatment Imaging; PP-0231 Treatment-related Toxicity and Supportive Care; dedicated biomarker-testing, sequencing, resistance, and multidisciplinary-management packages.

---

# Revision History

| Version | Date | Change |
|---|---|---|
| 1.0.0 | 2026-08-09 | Initial Gold production after PP-0213 Decision Batch approval and lock. |

---

# Final Status

**GOLD — READY FOR INTEGRATION**
