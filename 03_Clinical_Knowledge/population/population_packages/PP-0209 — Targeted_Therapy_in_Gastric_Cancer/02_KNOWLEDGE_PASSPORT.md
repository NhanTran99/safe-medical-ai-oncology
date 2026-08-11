# 02_KNOWLEDGE_PASSPORT.md

# Knowledge Passport

---

# Identity

| Field | Value |
|---|---|
| KP ID | KP-PP-0209 |
| PP ID | PP-0209 |
| Title | Targeted Therapy in Gastric Cancer |
| Version | 1.0.0 |
| Status | APPROVED / LOCKED — GOLD |
| Production Status | GOLD — READY FOR INTEGRATION |
| Last Updated | 2026-08-09 |
| Governance Standard | CORE_WORKING_RULES v1.7 |
| Artifact Standard | FREEZE GOLD POPULATION PACKAGE SPECIFICATION v1.1 |

---

# 1. Classification

| Field | Value |
|---|---|
| Clinical Domain | Gastric Cancer — Treatment / Precision Oncology |
| Domain Code | GC-TX / PRECISION-ONCOLOGY |
| Educational Level | Patient-facing clinical education |
| Clinical Complexity | High |
| Patient Journey Stage | Treatment planning / advanced disease / biomarker-directed treatment |
| Knowledge Type | Treatment modality / precision-treatment framework |
| Treatment Intent | Context-dependent; not inherently curative or palliative |
| Atomic Question | What is targeted therapy for gastric cancer, how is it different from chemotherapy and immunotherapy, when can it be used, and why do biomarker results matter? |
| Core Population | Patients with gastric cancer for whom targeted-treatment concepts or biomarker-directed treatment are clinically relevant |
| Core Targets | HER2; CLDN18.2; VEGFR-2; selected NTRK, BRAF V600E and RET alterations |
| Core Modality | Targeted systemic therapy |
| Main Setting | Unresectable, recurrent, or metastatic disease; selected treatment contexts as supported by source materials |
| Output Type | Patient-facing, source-grounded, reusable knowledge product |

# 2. Clinical-Educational Role

PP-0209 is the **foundational targeted-therapy modality node**.

It sits between:

**biomarker testing**

and

**target-specific treatment**.

The central runtime relationship is:

**Biomarker information**

→ **target/actionability**

→ **targeted-treatment consideration**

→ **benefit/burden assessment**

PP-0209 therefore answers the modality-level question.

It does not replace:

- biomarker-testing packages;
- treatment-selection packages;
- target-specific therapy packages;
- toxicity packages;
- resistance packages.

This distinction is essential for retrieval accuracy and for preventing duplicate content.

# 3. Retrieval Intent

Retrieve PP-0209 when the user asks:

- What is targeted therapy?
- What does targeted therapy mean in gastric cancer?
- How is targeted therapy different from chemotherapy?
- How is targeted therapy different from immunotherapy?
- Why do I need biomarker testing before targeted therapy?
- What targets can be treated in gastric cancer?
- What are HER2, CLDN18.2 and VEGFR-2 in relation to targeted treatment?
- Can targeted therapy be combined with chemotherapy?
- Can targeted therapy be used alone?
- Why can targeted therapy stop working?
- Does a positive biomarker guarantee response?
- Why might biomarker testing be repeated?
- What are the general benefits and limitations of targeted therapy?

# 4. Do Not Retrieve PP-0209 as the Primary Source When the User Asks

Do not use PP-0209 as the primary package for:

- detailed HER2 testing;
- detailed HER2 treatment;
- trastuzumab-specific management;
- trastuzumab deruxtecan-specific management;
- detailed CLDN18.2 testing;
- zolbetuximab-specific management;
- detailed anti-angiogenic treatment;
- ramucirumab-specific management;
- NGS methodology;
- variant interpretation;
- molecular-report interpretation;
- individualized regimen selection;
- dose and schedule questions;
- drug-specific toxicity management;
- detailed resistance management.

Route to the relevant downstream package.

# 5. Core Retrieval Concepts

## Concept 1 — Targeted Therapy

A systemic treatment designed around a specific biological target or feature.

## Concept 2 — Biomarker

Information used to identify or characterize a biological feature that may influence treatment selection.

## Concept 3 — Actionability

The clinical relevance of a finding to an available treatment, clinical trial, or other management option.

## Concept 4 — Precision Oncology

An approach that incorporates biological characteristics of a cancer into clinical decision-making.

## Concept 5 — Target Classes

Targets may involve:

- protein expression;
- receptor signaling;
- angiogenic pathways;
- gene fusions;
- specific mutations;
- amplification/overexpression states.

## Concept 6 — Treatment Context

Targeted therapy must be interpreted with:

- disease setting;
- treatment line;
- previous therapy;
- performance status;
- toxicity;
- patient goals.

# 6. Target-to-Therapy Map

| Target / Alteration | Representative therapy | Educational purpose | Detailed owner |
|---|---|---|---|
| HER2 | Trastuzumab | Classic biomarker-directed treatment paradigm | PP-0210 |
| HER2 | Trastuzumab deruxtecan | Later-line targeted-treatment paradigm | PP-0210 |
| CLDN18.2 | Zolbetuximab | Protein-targeted treatment paradigm | PP-0211 |
| VEGFR-2 | Ramucirumab | Pathway/receptor-directed paradigm | PP-0212 |
| NTRK fusion | Entrectinib / larotrectinib / repotrectinib | Rare actionable genomic alteration | Future/specific PP |
| BRAF V600E | Dabrafenib + trametinib | Mutation-directed treatment paradigm | Future/specific PP |
| RET fusion | Selpercatinib | Fusion-directed treatment paradigm | Future/specific PP |
| VEGFR/multikinase pathways | Regorafenib | Selected later-line targeted-treatment example | Downstream therapy-specific ownership |

This map is for retrieval and conceptual routing, not prescribing.

# 7. Patient-Facing Retrieval Sequence

When explaining targeted therapy, retrieve in this order:

1. **What is targeted therapy?**
2. **Why is a target important?**
3. **How is the target identified?**
4. **How is targeted therapy different from chemotherapy?**
5. **How is it different from immunotherapy?**
6. **Which major targets are relevant in gastric cancer?**
7. **Can targeted therapy be combined with other treatments?**
8. **What benefits might occur?**
9. **Why might the treatment not work?**
10. **Can resistance develop?**
11. **Can the tumor biology change?**
12. **What are the major treatment burdens?**
13. **Which detailed package should be consulted next?**

# 8. Knowledge Graph

## Upstream

- PP-0009 — Treatment Options for Gastric Adenocarcinoma.
- PP-0190 — Biomarker-Directed Treatment Selection.
- PP-0191 — Biomarker Testing for Targeted Therapy.
- Individual biomarker-testing packages.
- Molecular profiling / NGS packages.

## Current Node

**PP-0209 — Targeted Therapy in Gastric Cancer**

## Downstream

- PP-0210 — HER2-targeted Therapy.
- PP-0211 — CLDN18.2-targeted Therapy.
- PP-0212 — Anti-angiogenic Therapy.
- Future NTRK/BRAF/RET or other target-specific packages.

## Parallel Nodes

- PP-0208 — Palliative Systemic Therapy.
- PP-0213 — Immunotherapy in Gastric Cancer.
- PP-0214 — Immune Checkpoint Inhibitors.
- PP-0215 — MSI-H/dMMR Gastric Cancer and Immunotherapy.
- PP-0216 — PD-L1-guided Immunotherapy.

# 9. Boundary Routing Matrix

| User Question | Primary PP |
|---|---|
| What is targeted therapy? | PP-0209 |
| Why does targeted therapy need biomarkers? | PP-0209 + PP-0191 |
| How do I test HER2? | HER2 testing PP |
| What does HER2-positive mean? | HER2 testing / PP-0190 |
| How is trastuzumab used? | PP-0210 |
| How is trastuzumab deruxtecan used? | PP-0210 |
| What is CLDN18.2? | CLDN18.2 testing PP |
| How is zolbetuximab used? | PP-0211 |
| What is ramucirumab? | PP-0212 |
| How do I choose among targeted drugs? | PP-0208 + PP-0190 + target-specific PP |
| What is NGS? | NGS testing PP |
| What does a molecular report mean? | Molecular-report PP |
| What are immunotherapy biomarkers? | PP-0192 / PP-0213–PP-0216 |
| What are targeted-therapy side effects? | Relevant therapy/toxicity PP |

# 10. Evidence Classification

## Established / Guideline-Supported

- Targeted therapy is a recognized gastric-cancer treatment modality.
- HER2-directed treatment is incorporated into selected advanced HER2-positive treatment pathways.
- CLDN18.2-directed therapy is incorporated into selected first-line advanced HER2-negative, CLDN18.2-positive treatment pathways.
- Ramucirumab has an established role in selected subsequent-line treatment.
- Selected NTRK, BRAF V600E and RET alterations can lead to targeted-treatment options.
- Targeted therapy can be combined with chemotherapy.
- Selected molecularly defined cancers may receive targeted therapy alone.

## Context-Dependent

- Exact drug selection.
- Treatment line.
- Combination versus monotherapy.
- Retesting.
- Treatment continuation.
- Treatment after progression.
- Use of rare alteration-directed therapies.

## Emerging / Evolving

- Additional actionable alterations.
- New target-directed combinations.
- Resistance-directed strategies.
- Broader molecular selection strategies.

The package must preserve these evidence distinctions during retrieval.

# 11. Clinical Safety Guardrails

When retrieving PP-0209:

- Never state that a biomarker guarantees response.
- Never state that targeted therapy has no toxicity.
- Never convert a target into an automatic prescription.
- Never omit treatment-line context.
- Never omit previous therapy when discussing later-line targeted treatment.
- Never imply that every target is a mutation.
- Never imply that targeted therapy always replaces chemotherapy.
- Never imply that targeted therapy and immunotherapy are the same.
- Never provide drug dosing from this package.
- Never use PP-0209 as individualized treatment advice.

# 12. Patient-Language Glossary

| Technical term | Patient-facing explanation |
|---|---|
| Targeted therapy | Treatment designed to act on a specific biological feature of cancer |
| Biomarker | A measurable feature that can provide information about the cancer or treatment |
| Actionable alteration | A finding that may have a clinically relevant treatment or trial implication |
| HER2 | A protein/receptor-related cancer characteristic that can guide HER2-directed treatment |
| CLDN18.2 | A protein that can serve as a treatment target in selected gastric cancers |
| VEGFR-2 | A receptor involved in signaling related to blood-vessel formation |
| Gene fusion | Two gene segments becoming abnormally joined, sometimes creating an actionable target |
| Mutation | A change in DNA sequence |
| Resistance | When cancer becomes less sensitive or no longer responds to a treatment |
| Tumor heterogeneity | Differences between cancer cells within the same cancer or between disease sites |

# 13. Knowledge Graph Integrity Rules

### Rule 1

PP-0209 owns the **modality concept**, not the entire targeted-drug catalog.

### Rule 2

PP-0191 owns the **testing strategy**.

### Rule 3

PP-0190 owns the **biomarker-to-treatment-selection bridge**.

### Rule 4

PP-0210, PP-0211 and PP-0212 own detailed therapy-specific content.

### Rule 5

PP-0208 owns broader palliative systemic-treatment sequencing.

### Rule 6

Targeted therapy may overlap with immunotherapy in a combination regimen, but the conceptual treatment modalities remain distinct.

### Rule 7

The package should route rather than duplicate downstream details.

# 14. Maintenance Triggers

Review PP-0209 when:

- NCCN changes targeted-treatment pathways.
- New targeted agents receive a gastric-cancer indication.
- A major biomarker becomes clinically actionable.
- A new target-specific PP is created.
- A downstream package changes ownership.
- New safety information changes the modality-level explanation.
- Governance changes the PP boundary.

During updates, preserve the atomic question unless a new locked governance decision changes it.

# 15. Final Runtime Summary

PP-0209 should be retrieved as the **foundational explanation of targeted therapy in gastric cancer**.

Its defining chain is:

**Target**

→ **Biomarker**

→ **Actionability**

→ **Treatment consideration**

→ **Benefit / burden**

→ **Reassessment**

The package should always route detailed therapy questions to the appropriate downstream Population Package.

---

# 16. Revision History

| Version | Date | Change |
|---|---|---|
| 1.0.0 | 2026-08-09 | Initial Gold production after PP-0209 Decision Batch approval and lock. |

---

# 17. Final Passport Status

**GOLD — READY FOR INTEGRATION**


# 18. Expanded Runtime Retrieval Map

## Query Class A — Definition

**User:** “What is targeted therapy?”

Retrieve:

- definition;
- target concept;
- biomarker relationship;
- comparison with chemotherapy and immunotherapy.

Do not immediately retrieve a drug-specific package.

## Query Class B — Biomarker Relationship

**User:** “Why do I need biomarker testing before targeted therapy?”

Retrieve:

- PP-0209 target-biomarker relationship;
- PP-0191 testing strategy;
- relevant biomarker-testing PP.

## Query Class C — Target Identification

**User:** “What targets are important in gastric cancer?”

Retrieve:

- HER2;
- CLDN18.2;
- VEGFR-2;
- NTRK;
- BRAF V600E;
- RET.

Present these as examples, not as a universal mandatory panel.

## Query Class D — Treatment Selection

**User:** “Which targeted therapy should I receive?”

PP-0209 alone is insufficient.

Route to:

- PP-0190;
- PP-0208;
- target-specific package;
- individual clinical assessment.

Do not provide an individualized answer from PP-0209.

## Query Class E — Drug-Specific

**User:** “How does trastuzumab work?”

Route to PP-0210.

**User:** “How does zolbetuximab work?”

Route to PP-0211.

**User:** “How does ramucirumab work?”

Route to PP-0212.

---

# 19. Expanded Target Retrieval Table

| Search term | Retrieval behavior |
|---|---|
| targeted therapy | PP-0209 |
| precision therapy | PP-0209 |
| molecularly targeted therapy | PP-0209 |
| biomarker-directed treatment | PP-0190 + PP-0209 |
| HER2 treatment | PP-0210 |
| trastuzumab | PP-0210 |
| trastuzumab deruxtecan | PP-0210 |
| CLDN18.2 treatment | PP-0211 |
| zolbetuximab | PP-0211 |
| VEGFR-2 | PP-0212 |
| ramucirumab | PP-0212 |
| NTRK treatment | future/specific targeted PP if available |
| BRAF V600E treatment | future/specific targeted PP if available |
| RET treatment | future/specific targeted PP if available |
| biomarker test | PP-0191 / specific biomarker PP |
| NGS | NGS testing PP |
| molecular report | molecular-report PP |
| systemic therapy | PP-0208 |
| palliative systemic therapy | PP-0208 |
| immunotherapy | PP-0213 onward |

---

# 20. Retrieval Guardrail Matrix

| User intent | Primary package | Secondary routing |
|---|---|---|
| Definition of targeted therapy | PP-0209 | — |
| Why biomarker testing matters | PP-0209 | PP-0191 |
| Which biomarker to test | PP-0191 | Specific biomarker PP |
| What a biomarker result means for treatment | PP-0190 | PP-0209 |
| HER2 targeted therapy | PP-0210 | HER2 testing PP |
| CLDN18.2 targeted therapy | PP-0211 | CLDN18.2 testing PP |
| Anti-angiogenic therapy | PP-0212 | — |
| Overall palliative systemic strategy | PP-0208 | PP-0209 |
| Immunotherapy | PP-0213 onward | — |
| Molecular report interpretation | Molecular-report PP | NGS / biomarker PP |
| Drug-specific toxicity | Therapy/toxicity PP | — |
| Target-specific resistance | Therapy/resistance PP | — |

---

# 21. Knowledge Passport Maintenance Rule

When a new target-specific PP is created:

1. Add it to the downstream routing table.
2. Keep PP-0209 at modality level.
3. Remove only duplicate drug-specific detail if necessary.
4. Preserve the modality-level example.
5. Update the boundary and Knowledge Graph.
6. Update the QA report.

Do not redesign PP-0209 merely because a new drug appears.


# 22. Expanded Retrieval Tags

## Primary Tags

- targeted therapy
- targeted treatment
- precision oncology
- gastric cancer targeted therapy
- biomarker-directed therapy
- molecularly targeted treatment
- actionable target
- targetable alteration

## Target Tags

- HER2
- ERBB2
- CLDN18.2
- VEGFR-2
- NTRK
- BRAF V600E
- RET

## Treatment Context Tags

- advanced gastric cancer
- unresectable gastric cancer
- recurrent gastric cancer
- metastatic gastric cancer
- first-line targeted therapy
- second-line targeted therapy
- subsequent-line targeted therapy

## Patient-Education Tags

- targeted therapy side effects
- targeted therapy versus chemotherapy
- targeted therapy versus immunotherapy
- biomarker and targeted therapy
- resistance
- tumor evolution
- repeat biomarker testing

---

# 23. Retrieval Priority Rules

### Rule A — Definition first

If the query is broad, retrieve the conceptual definition before naming individual drugs.

### Rule B — Target second

If the query identifies a target, route to the target-specific package after providing the modality-level explanation.

### Rule C — Treatment line third

If a drug is mentioned, preserve treatment-line context.

### Rule D — Testing upstream

If the user asks how the target was measured, route upstream.

### Rule E — Toxicity downstream

If the user asks how to manage a drug-specific adverse effect, route downstream.

### Rule F — Individualized advice requires clinical context

Do not use the package as a substitute for individualized oncology decision-making.

---

# 24. Knowledge Graph Traversal Examples

## Traversal 1

**“What is targeted therapy?”**

→ PP-0209.

## Traversal 2

**“Why is HER2 tested?”**

→ HER2 testing PP → PP-0190 → PP-0209.

## Traversal 3

**“What does HER2-positive mean for treatment?”**

→ HER2 testing PP → PP-0190 → PP-0210.

## Traversal 4

**“What is zolbetuximab?”**

→ PP-0211.

## Traversal 5

**“Why might ramucirumab be used after chemotherapy?”**

→ PP-0212 → PP-0208 for broader treatment-line context.

## Traversal 6

**“Can targeted therapy and immunotherapy be used together?”**

→ PP-0209 for modality relationship → immunotherapy packages for detailed combination context.

---

# 25. Runtime Misconception Controls

When a query contains the word “targeted,” the system should not automatically assume:

- HER2;
- CLDN18.2;
- metastatic disease;
- monotherapy;
- first-line treatment.

The word “targeted” identifies a modality, not a single treatment pathway.

Similarly, the word “biomarker” does not automatically mean:

- HER2;
- NGS;
- PD-L1;
- a positive result;
- a treatment recommendation.

The retrieval system should identify the user's actual question before routing.

---

# 26. Patient-Facing Knowledge Layer

PP-0209 should be understandable without requiring the user to know:

- genomics terminology;
- molecular pathology;
- oncology drug classes.

Therefore:

**technical term**

→ **plain-language explanation**

→ **clinical relevance**

is preferred.

For example:

**HER2**

→ “a protein-related feature that can help guide treatment”

rather than introducing molecular details before explaining why the term matters.

---

# 27. Clinical-Educational Depth Rule

PP-0209 should be deeper than a drug list.

A useful response should explain:

1. what targeted therapy is;
2. why it exists;
3. how the target is identified;
4. how it changes treatment options;
5. why response is not guaranteed;
6. what limitations remain;
7. where to retrieve detailed therapy information.

This is the minimum educational architecture for runtime use.


# 28. Runtime Quality Gate

Before returning a targeted-therapy answer from PP-0209, verify:

1. The answer is about the targeted-therapy modality.
2. The target is identified if a specific target is discussed.
3. The clinical setting is not silently omitted.
4. The treatment line is not silently omitted when relevant.
5. The answer does not imply guaranteed response.
6. The answer does not imply absence of toxicity.
7. The answer does not provide individualized prescribing.
8. The answer routes detailed drug questions to the downstream package.
9. The answer routes detailed testing questions upstream.
10. The answer remains consistent with the current source hierarchy.

---

# 29. Final Knowledge Passport Statement

PP-0209 is the **foundational targeted-therapy knowledge node** for gastric cancer.

Its stable runtime identity is:

> **Targeted therapy as a biomarker-linked treatment modality, explained at patient-facing clinical depth and connected to target-specific downstream packages.**

This identity should remain stable unless superseded by a locked governance decision.
