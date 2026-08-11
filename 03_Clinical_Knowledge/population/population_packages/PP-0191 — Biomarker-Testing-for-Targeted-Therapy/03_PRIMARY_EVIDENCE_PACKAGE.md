# 03_PRIMARY_EVIDENCE_PACKAGE.md

# Primary Evidence Package

## Identity

| Field | Value |
|---|---|
| Evidence Package ID | EP-PP-0191 |
| Population Package ID | PP-0191 |
| Title | Biomarker Testing for Targeted Therapy |
| Clinical Domain | Precision Oncology / Biomarker Testing |
| Version | 1.0.0 |
| Status | Approved — GOLD |

---

# 1. Clinical Question

## Primary Educational Question

> **Which biomarker testing should be considered to identify potential targeted-treatment opportunities in gastric adenocarcinoma?**

## Clinical-Educational Intent

Provide a source-grounded framework for understanding **testing strategy** before targeted treatment is considered.

The package is intentionally positioned between individual biomarker-testing packages and the downstream biomarker-directed treatment-selection package.

The conceptual sequence is:

**Clinical question**

→ **Relevant biomarker information**

→ **Testing strategy**

→ **Result**

→ **Molecular report**

→ **Biomarker-directed treatment application**

→ **Treatment**

The package does not prescribe an individual testing plan or treatment.

---

# 2. Scope

## Included

- Purpose of biomarker testing for targeted-treatment readiness.
- Predictive biomarker concept at a high level.
- Clinical-question-driven testing strategy.
- Targeted biomarker testing versus broader molecular profiling.
- HER2 testing as a representative targeted-treatment biomarker domain.
- CLDN18.2 testing as a representative targeted-treatment biomarker domain.
- Selected NTRK, BRAF V600E, RET and FGFR2 examples at the strategy level.
- NGS as a broader molecular-testing approach.
- IHC/ISH/targeted PCR versus NGS at a conceptual level.
- Specimen availability and adequacy.
- Tissue versus blood-based genomic testing.
- Selected ctDNA/liquid-biopsy context.
- Testing timing in relation to the clinical question.
- Negative, inadequate, failed and non-actionable testing concepts.
- Additional testing when a previous test does not answer the current question.
- Multidisciplinary/molecular review concept.
- Patient-facing testing questions.
- Common misconceptions.
- Knowledge-graph boundaries.

## Excluded

- Detailed HER2 IHC/ISH methodology and scoring.
- Detailed MSI/MMR testing.
- Detailed PD-L1 testing.
- Detailed CLDN18.2 methodology/scoring.
- Detailed TMB testing.
- Detailed FGFR2 testing.
- NGS laboratory methodology.
- Sequencing chemistry.
- Library preparation.
- Bioinformatics.
- Variant calling.
- Detailed variant interpretation or classification.
- Molecular-report literacy.
- Detailed ctDNA biology or longitudinal monitoring.
- MRD.
- Companion-diagnostic regulatory methodology.
- Treatment selection.
- Drug or regimen selection.
- Treatment sequencing.
- Dosing.
- Toxicity management.
- Response/resistance management.
- Individualized testing recommendations.
- Individualized treatment recommendations.

---

# 3. Primary Sources

| Priority | Source | Role in PP-0191 |
|---|---|---|
| 1 | `1. Gastric Cancer_v.2.2026_NCCN-3-109.pdf` — NCCN Gastric Cancer v2.2026 | Primary disease-specific source for biomarker-testing context, HER2, CLDN18.2, NGS, targeted biomarkers, and ctDNA/liquid-biopsy testing |
| 2 | `4. ESMO-ASCO Recommendations for a Global Curriculum in Medical Oncology Edition 2023.pdf` | Cross-cutting genomic-testing framework: assay categories, analytes, panels, molecular events, specimen/pre-analytic variables, clinical context |
| 3 | `17. Treatment of Stomach Cancer - NCI.pdf` | Patient-facing linkage between biomarker testing and targeted therapy |
| 4 | `5. Stomach Cancer_ACS.pdf` | Patient-facing biomarker-treatment examples including HER2, CLDN18.2, NTRK, BRAF and RET |
| 5 | `7. Immunotherapy for Stomach Cancer_ACS.pdf` | Supporting biomarker-treatment context |
| 6 | `15. Cancer Genetics Risk Assessment and Counseling (PDQ®) - NCI.pdf` | Supporting genetic-testing and possible germline-implication context |

---

# 4. Supporting / Related Project Sources

The package architecture also uses the following project Source Files as contextual references:

- `2. Gastric cancer_NCCN CLINICAL PRACTICE GUIDELINES IN ONCOLOGY.pdf`
- `9. Drugs Approved for Stomach (Gastric) Cancer - NCI.pdf`
- `6. Chemotherapy for Stomach Cancer_ACS.pdf`
- `PP Registry.xlsx`
- `CORE_WORKING_RULES v1.7.md`
- `FREEZE GOLD POPULATION PACKAGE SPECIFICATION v1.1.md`
- `PP Discussion depth and format example.md`
- Approved Gold artifact references, especially the completed PP-0189 package and the approved PP discussion example.

The clinical evidence hierarchy remains led by NCCN and ESMO-ASCO, with NCI/ACS used primarily for patient-facing context.

---

# 5. Evidence Hierarchy

## Level I — Disease-Specific Guideline

### NCCN Gastric Cancer v2.2026

NCCN is the highest-priority disease-specific evidence source for PP-0191.

The guideline's biomarker-testing framework supports several central points:

1. Biomarker assessment is part of gastric-cancer treatment planning.
2. HER2 testing is recommended in the appropriate advanced/metastatic context.
3. CLDN18.2 testing is recommended when advanced/metastatic disease is documented or suspected.
4. IHC, ISH, or targeted PCR are preferred approaches for specified biomarkers initially.
5. Validated NGS may be considered later in the clinical course in selected patients with sufficient tumor tissue.
6. NGS can assess several mutations and other molecular events simultaneously.
7. The targeted biomarker landscape can include multiple molecular event classes.
8. Blood-based ctDNA testing is recognized as a form of liquid biopsy.
9. Blood-based genomic testing may be considered in selected patients when tissue is limited or traditional biopsy is not feasible.

The testing-strategy implication is:

> **There is no single universal biomarker test for gastric cancer. Testing approach depends on the biomarker question and clinical context.**

---

## Level I — ESMO-ASCO Global Curriculum 2023

The ESMO-ASCO curriculum provides the broader genomic-testing framework required to interpret the testing strategy.

It recognizes that molecular assays may be directed toward:

- DNA;
- RNA;
- protein;
- a specific analyte;
- a panel;
- broader genomic approaches.

It also recognizes multiple classes of genomic alterations, including:

- sequence variants;
- insertions/deletions;
- copy-number changes;
- fusions;
- transcript-level changes;
- protein-level findings.

For PP-0191, the most important point is that **assay scope varies**.

A test designed for one biomarker cannot automatically be assumed to answer a different biomarker question.

---

# 6. Evidence Matrix

| Clinical Claim | Supporting Source | Evidence Role | PP-0191 Boundary |
|---|---|---|---|
| Biomarker tests may help predict response to selected targeted therapies. | NCI Treatment of Stomach Cancer | Direct patient-facing clinical evidence | Treatment selection remains downstream |
| HER2 testing is relevant when targeted therapy is being considered in the appropriate advanced/metastatic setting. | NCCN v2.2026 | Direct disease-specific guideline evidence | Detailed HER2 testing = PP-0181 |
| CLDN18.2 testing is relevant in appropriate advanced/metastatic disease. | NCCN v2.2026 | Direct disease-specific guideline evidence | Detailed CLDN18.2 testing = PP-0184 |
| IHC/ISH/targeted PCR are preferred initial approaches for specified biomarkers. | NCCN v2.2026 | Direct guideline evidence | Prevents universal-NGS claim |
| Validated NGS may be considered later in selected patients with sufficient tumor tissue. | NCCN v2.2026 | Direct guideline evidence | NGS methodology = PP-0187 |
| NGS can assess multiple molecular events simultaneously. | NCCN v2.2026 | Direct guideline evidence | Conceptual only |
| Testing can target a specific analyte, panel or broader genomic approach. | ESMO-ASCO 2023 | Professional curriculum evidence | No technical workflow |
| Specimen characteristics can influence molecular testing. | ESMO-ASCO 2023 | Professional curriculum evidence | Patient-facing specimen concept only |
| Tumor cellularity and nucleic-acid quality/quantity may influence testing. | ESMO-ASCO 2023 | Professional curriculum evidence | No numerical thresholds |
| Blood-based ctDNA is a liquid-biopsy approach. | NCCN v2.2026 | Direct guideline evidence | Detailed ctDNA = delegated |
| Blood-based genomic testing may be considered in selected circumstances with limited tissue or inability to undergo traditional biopsy. | NCCN v2.2026 | Direct guideline evidence | Not universal tissue replacement |
| HER2/CLDN18.2 and other molecular features may be linked to targeted-treatment contexts. | ACS Stomach Cancer + NCCN | Supporting disease-specific evidence | Detailed therapy = downstream |
| NTRK, BRAF V600E and RET alterations can be associated with targeted-treatment opportunities in selected advanced cancers. | ACS Stomach Cancer + NCCN | Supporting/direct disease-specific evidence | Examples only; no universal screening claim |
| A negative result must be interpreted according to test scope and limitations. | NCCN + ESMO-ASCO framework | Evidence-supported conceptual synthesis | No universal sensitivity threshold |
| Inadequate/failed testing is distinct from a negative result. | ESMO-ASCO testing framework | Evidence-supported educational distinction | No repeat-testing algorithm |
| A tumor finding does not automatically establish an inherited finding. | ESMO-ASCO + NCI Genetics PDQ | Genetic-testing evidence | Germline package owns follow-up |
| Biomarker testing is not itself a treatment order. | NCI + NCCN treatment framework | Patient-facing clinical principle | PP-0190 owns downstream application |

---

# 7. Evidence Discussion

## 7.1 Biomarker Testing as a Clinical Bridge

NCI explicitly describes biomarker testing as potentially useful for predicting response to certain targeted therapy drugs.

This supports the fundamental educational premise of PP-0191:

> **Targeted treatment may depend on biological information that must be measured before the treatment pathway can be considered.**

The package therefore does not present testing as an isolated laboratory activity.

Instead, it places testing within a clinical pathway:

**Potential treatment opportunity**

→ **Need for relevant biomarker information**

→ **Appropriate test**

→ **Result**

→ **Clinical interpretation**

→ **Treatment consideration**

This is a testing-strategy concept rather than a treatment algorithm.

---

## 7.2 HER2 Testing

NCCN v2.2026 recommends HER2 assessment using IHC with ISH/FISH or another appropriate ISH method for patients with inoperable locally advanced, recurrent, or metastatic gastric adenocarcinoma for whom trastuzumab therapy is being considered.

The same NCCN framework also notes that NGS can assess numerous mutations and molecular events, including amplification.

This creates an important educational distinction:

> **A biomarker can be clinically important without requiring a broad NGS panel as the initial testing method.**

PP-0191 therefore explains the strategy.

PP-0181 owns the detailed test.

PP-0190 owns the biomarker-directed treatment application.

---

## 7.3 CLDN18.2 Testing

NCCN v2.2026 identifies CLDN18.2 testing when advanced/metastatic disease is documented or suspected.

ACS patient-facing material also explains that cancer cells may be tested for high levels of CLDN18.2 when determining whether a patient may benefit from a CLDN18.2-directed therapy.

The evidence supports CLDN18.2 as a clear example of the chain:

**Targeted-treatment possibility**

→ **Biomarker requirement**

→ **Biomarker testing**

→ **Result**

PP-0191 should not duplicate the CLDN18.2 assay/scoring package.

---

## 7.4 Broader Molecular Alterations

ACS identifies selected targeted-treatment examples involving:

- NTRK;
- BRAF V600E;
- RET.

NCCN similarly lists targeted-treatment options associated with selected molecular alterations.

This supports the use of these biomarkers as **examples demonstrating the value of broader molecular testing**.

The package does not make the stronger claim that every patient should undergo universal testing for every rare alteration.

The correct educational statement is:

> **Broader molecular testing may identify selected molecular alterations that could create additional treatment opportunities.**

---

## 7.5 NGS as a Testing Strategy

NCCN states that IHC/ISH/targeted PCR is preferred to assess biomarkers initially, while validated NGS may be considered later in selected patients with sufficient tumor tissue.

This directly prevents two opposite errors:

### Error A

"Every biomarker should be tested by NGS."

Not supported.

### Error B

"NGS has no role because biomarker-specific tests exist."

Also not supported.

The correct framework is:

> **Biomarker-specific assays and broader NGS are complementary tools whose value depends on the clinical question.**

---

## 7.6 Assay Scope

ESMO-ASCO's framework emphasizes that molecular assays can be directed toward different analytes and levels of breadth.

Therefore:

> **A negative result is meaningful only in relation to what the test was designed and validated to assess.**

This is why a narrow test cannot automatically be interpreted as a comprehensive molecular exclusion.

The patient-facing consequence is important:

> "Not detected" does not mean "nothing molecularly relevant exists."

---

## 7.7 Specimen Adequacy

Molecular testing depends on the quality and quantity of the available biological material.

ESMO-ASCO identifies pre-analytic factors such as:

- tumor cellularity;
- nucleic-acid quantity;
- nucleic-acid quality;
- specimen collection;
- preparation;
- transport;
- storage.

This supports the inclusion of specimen adequacy as part of the testing strategy.

A technically unsuccessful test should not be presented as equivalent to a true negative result.

---

## 7.8 Tissue and Blood-Based Testing

NCCN recognizes ctDNA in blood as a form of liquid biopsy.

It also allows selected consideration of validated blood-based genomic testing when tissue is limited or traditional biopsy is not feasible in advanced/metastatic disease.

This supports a high-level testing-strategy message:

> **When tissue cannot adequately answer the clinical question, blood-based genomic testing may sometimes provide useful molecular information.**

The evidence does not support a universal statement that blood testing is equivalent to tissue testing in every circumstance.

Detailed ctDNA biology and monitoring remain delegated.

---

## 7.9 Testing Timing

NCCN places different biomarkers into different clinical contexts.

For example:

- MSI/MMR testing is described as universal at diagnosis;
- PD-L1 testing is described as universal at diagnosis;
- HER2 testing is tied to advanced/metastatic disease being documented or suspected;
- CLDN18.2 testing is similarly tied to advanced/metastatic disease;
- NGS should be considered.

This illustrates an important principle:

> **Testing timing is biomarker- and context-dependent.**

PP-0191 should therefore not impose a universal "test everything at the same time" rule.

---

## 7.10 Testing Completeness

A test can be technically successful but still not answer the clinical question.

For example:

- a test may assess HER2 but not a broader set of genomic alterations;
- an assay may detect protein expression but not a specific gene alteration;
- a targeted assay may not evaluate a newly relevant biomarker.

Therefore:

> **Testing completeness is relative to the clinical question.**

This is one of the most important conceptual contributions of PP-0191.

---

## 7.11 Negative Results

A negative result means that the assessed finding was not detected.

It does not establish that:

- all molecular abnormalities are absent;
- all targeted-treatment opportunities are absent;
- all future testing would also be negative.

The negative result must be interpreted with respect to:

- assay scope;
- specimen;
- quality;
- biomarker definition;
- clinical setting.

---

## 7.12 No Actionable Alteration

The project evidence supports distinguishing:

**molecular alteration detected**

from

**clinically actionable alteration**

and from

**treatment eligibility**.

These are not synonymous.

A molecular alteration may be biologically real but not provide an actionable treatment option in the relevant clinical setting.

This is why PP-0191 stops at testing strategy and PP-0190 owns the downstream clinical application.

---

## 7.13 Additional Testing

The evidence supports a contextual rather than universal approach.

Additional testing may be relevant when:

- the prior test did not assess the relevant biomarker;
- the prior specimen was inadequate;
- the assay scope was too narrow for the new clinical question;
- tissue becomes unavailable;
- broader molecular information may be useful.

The package deliberately avoids recommending routine repeat testing intervals.

---

# 8. Evidence-Supported Clinical Testing Model

## Level 1 — Define the Clinical Question

Examples:

- Is there a known biomarker-linked targeted-treatment pathway relevant to this disease setting?
- Is there a reason to evaluate multiple molecular targets?
- Is existing molecular information sufficient?

↓

## Level 2 — Identify the Biomarker Information Needed

Examples:

- HER2;
- CLDN18.2;
- selected molecular alterations;
- broader genomic profile.

↓

## Level 3 — Select the Appropriate Testing Approach

Possible approaches include:

- biomarker-specific IHC;
- ISH;
- targeted PCR;
- broader NGS.

The approach depends on the biomarker and clinical question.

↓

## Level 4 — Confirm Specimen Adequacy

Ask:

- Is appropriate tissue available?
- Is the specimen adequate?
- Does the test require a specific specimen type?
- Is a blood-based approach relevant in the clinical setting?

↓

## Level 5 — Obtain an Interpretable Result

Distinguish:

- positive/detected;
- negative/not detected;
- uncertain;
- inadequate/failed.

↓

## Level 6 — Interpret the Result

This moves toward PP-0189 and PP-0190.

↓

## Level 7 — Consider Treatment

Treatment selection is downstream.

---

# 9. Testing Strategy Matrix

| Clinical Question | Potential Testing Strategy | PP-0191 Role | Detailed Ownership |
|---|---|---|---|
| Could HER2-directed therapy be relevant? | HER2-specific testing | Explain why testing is relevant | PP-0181 |
| Could CLDN18.2-directed therapy be relevant? | CLDN18.2-specific testing | Explain why testing is relevant | PP-0184 |
| Could several molecular targets be relevant? | Broader molecular profiling may be considered | Explain strategic rationale | PP-0187 |
| Could a selected rare alteration be relevant? | Appropriate molecular testing depending on alteration | Explain testing-strategy concept | Relevant biomarker/NGS PP |
| Is tissue limited? | Consider validated blood-based genomic testing in selected circumstances | Explain context | Liquid-biopsy/ctDNA PP |
| Is the previous test incomplete for the current question? | Consider whether additional testing is needed | Explain the principle | Relevant testing PP |
| What does the result mean? | Review molecular report | Route downstream | PP-0189 |
| What does the result mean for targeted therapy? | Clinical application | Route downstream | PP-0190 |

---

# 10. Evidence Consistency Review

## NCCN versus ESMO-ASCO

No material conflict was identified for the locked scope.

NCCN provides the disease-specific gastric-cancer testing framework.

ESMO-ASCO provides the broader conceptual framework for molecular assays, specimen variables, and clinical interpretation.

The two sources are complementary:

**NCCN = gastric-cancer testing context**

**ESMO-ASCO = molecular-testing framework**

---

## NCCN versus NCI

NCI's patient-facing material states that biomarker tests may help predict response to targeted therapy.

This is consistent with the NCCN framework in which biomarker testing is integrated into gastric-cancer treatment planning.

No material conflict was identified.

---

## NCCN versus ACS

ACS provides patient-facing examples of biomarker-associated treatment contexts.

These examples are used in PP-0191 only to explain why testing may matter.

The package does not import ACS treatment regimens into the testing-strategy layer.

---

# 11. Evidence Gaps

The following limitations are acknowledged and intentionally not filled with unsupported assumptions:

1. There is no single universal testing sequence that applies to every gastric-cancer patient.
2. The exact choice between biomarker-specific testing and broader molecular profiling can depend on clinical context.
3. Assay availability varies by laboratory and jurisdiction.
4. Assay-specific sensitivity, specificity, detection limits, and technical thresholds are not generalized in this package.
5. Blood-based and tissue-based genomic tests are not universally interchangeable.
6. A molecular alteration is not automatically actionable.
7. A negative test cannot be interpreted without knowing the assay scope.
8. The Source Materials do not justify a universal repeat-testing interval.
9. Individual patient testing requires the complete clinical context.
10. Detailed biomarker methodologies are intentionally delegated to dedicated PPs.
11. Detailed variant interpretation and classification are intentionally delegated.
12. Detailed treatment selection is intentionally delegated to PP-0190 and downstream treatment PPs.

These gaps do not block PP-0191 because the locked package is a **testing-strategy educational package**, not an individualized clinical decision algorithm.

---

# 12. Out-of-Scope Topics / Delegation Map

| Topic | Delegated To |
|---|---|
| Foundational biomarker testing | Foundational biomarker-testing package(s) |
| HER2 testing | PP-0181 |
| MSI/MMR testing | PP-0182 |
| PD-L1 testing | PP-0183 |
| CLDN18.2 testing | PP-0184 |
| TMB | PP-0185 |
| FGFR2 testing | PP-0186 |
| NGS biomarker testing | PP-0187 |
| Molecular subtypes | PP-0188 |
| Molecular report literacy | PP-0189 |
| Biomarker-directed targeted-treatment selection | PP-0190 |
| Targeted therapy in gastric cancer | PP-0208 |
| HER2-targeted therapy | PP-0209 |
| CLDN18.2-targeted therapy | PP-0210 |
| Anti-angiogenic therapy | PP-0211 |
| Detailed ctDNA/liquid-biopsy applications | Relevant liquid-biopsy/ctDNA PPs |
| Germline/hereditary cancer | Relevant hereditary/genetic-testing PPs |
| Companion diagnostics | Dedicated companion-diagnostics packages |
| Treatment sequencing | Relevant treatment PPs |

---

# 13. Future Update Triggers

PP-0191 should be reviewed when there are material changes in:

1. NCCN gastric-cancer biomarker-testing recommendations.
2. New or newly established gastric-cancer targeted-treatment biomarkers.
3. Major changes in the clinical use of NGS-based comprehensive molecular profiling.
4. Major changes in the recommended use of HER2 or CLDN18.2 testing.
5. New validated testing approaches that alter the current testing hierarchy.
6. Major changes in the role of blood-based genomic testing.
7. Major changes in companion-diagnostic requirements.
8. New molecular targets that become sufficiently established to affect routine testing strategy.
9. Major changes in adjacent PP ownership.
10. Registry reconciliation affecting PP-0190/PP-0191 identity or scope.

---

# 14. Source Traceability

## Project Source Materials Used

1. `1. Gastric Cancer_v.2.2026_NCCN-3-109.pdf`
2. `2. Gastric cancer_NCCN CLINICAL PRACTICE GUIDELINES IN ONCOLOGY.pdf`
3. `4. ESMO-ASCO Recommendations for a Global Curriculum in Medical Oncology Edition 2023.pdf`
4. `17. Treatment of Stomach Cancer - NCI.pdf`
5. `5. Stomach Cancer_ACS.pdf`
6. `7. Immunotherapy for Stomach Cancer_ACS.pdf`
7. `15. Cancer Genetics Risk Assessment and Counseling (PDQ®) - NCI.pdf`
8. `9. Drugs Approved for Stomach (Gastric) Cancer - NCI.pdf`
9. `6. Chemotherapy for Stomach Cancer_ACS.pdf`
10. `PP Registry.xlsx`
11. `CORE_WORKING_RULES v1.7.md`
12. `FREEZE GOLD POPULATION PACKAGE SPECIFICATION v1.1.md`
13. `PP Discussion depth and format example.md`
14. Approved completed Gold Population Package references.

---

# 15. Source-First Note

Clinical claims in this package are grounded in the project Source Files.

The package does not silently replace missing evidence with unsupported general medical knowledge.

Where a statement represents a conservative educational synthesis of several source-supported concepts, it is framed as a strategy principle rather than an absolute clinical rule.

---

# 16. Evidence Package Decision

## PASS — GOLD EVIDENCE PACKAGE

The Source Materials are sufficient to support the locked educational scope of PP-0191.

The evidence base is strongest for:

- biomarker testing as part of treatment planning;
- HER2 and CLDN18.2 testing;
- biomarker-specific versus broader molecular testing;
- NGS as a selected broader testing approach;
- specimen considerations;
- selected blood-based genomic testing;
- selected targeted-treatment-relevant molecular alterations.

The package intentionally does not make unsupported claims about universal testing, universal NGS use, universal repeat testing, or individualized treatment eligibility.

---

# 17. Final Evidence Status

**PASS — GOLD — READY FOR INTEGRATION**
