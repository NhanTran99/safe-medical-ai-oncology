# 01_CKO.md

# Clinical Knowledge Object

## Identity

| Field | Value |
|---|---|
| CKO ID | CKO-PP-0191 |
| PP ID | PP-0191 |
| Title | Biomarker Testing for Targeted Therapy |
| Clinical Domain | Precision Oncology / Biomarker Testing / Treatment Planning |
| Population Wave | Gastric Cancer Knowledge Population |
| Version | 1.0.0 |
| Status | Approved — GOLD |
| Audience | Patients, caregivers, and general clinical-education users |
| Reading Level | Patient-facing / clinically informed |
| Last Updated | 2026-08-09 |

---

# 1. Educational Question

> **Which biomarker testing should be considered to identify potential targeted-treatment opportunities in gastric adenocarcinoma?**

This Population Package occupies the **testing-strategy layer** of the gastric-cancer precision-oncology knowledge graph.

It explains why biomarker testing matters before targeted treatment can be considered, what broad types of testing may be relevant, how the clinical question influences the testing strategy, and why tissue availability, assay scope, and broader molecular profiling matter.

It deliberately stops before individualized treatment selection.

The core pathway is:

**Clinical question**

↓

**Potential targeted-treatment opportunities**

↓

**Relevant biomarker information**

↓

**Appropriate testing strategy**

↓

**Test result**

↓

**Molecular report**

↓

**PP-0190 — Biomarker-Directed Treatment Selection**

↓

**Downstream treatment Population Packages**

---

# 2. Educational Objectives

After reading this Population Package, the reader should be able to:

1. Explain why biomarker testing can be important when targeted therapy is being considered in gastric adenocarcinoma.
2. Distinguish a **testing strategy** from an individual biomarker test, a molecular report, and a treatment-selection decision.
3. Recognize that different biomarkers may require different testing approaches.
4. Understand why biomarker-specific testing and broader NGS-based molecular profiling are complementary rather than universally interchangeable approaches.
5. Understand why the clinical question, disease setting, available specimen, and assay scope matter when choosing a testing approach.
6. Recognize HER2 and CLDN18.2 as important examples of biomarker domains linked to targeted-treatment pathways.
7. Recognize that broader molecular testing may identify selected less-common molecular alterations relevant to treatment opportunities.
8. Understand at a high level why NTRK, BRAF V600E, RET, and other molecular alterations may appear in broader targeted-treatment testing discussions without turning those findings into automatic treatment recommendations.
9. Understand that a blood-based genomic test may sometimes be considered when tissue is limited or traditional biopsy is not feasible, while not assuming that blood and tissue testing are universally interchangeable.
10. Understand the difference between a negative result, an inadequate/failed test, and a result that identifies no currently actionable alteration.
11. Understand that a negative result applies to the scope and limitations of the test performed.
12. Recognize that more testing is not automatically better if it does not answer a clinically relevant question.
13. Know what questions to ask the care team about biomarker testing before targeted treatment is considered.

---

# 3. Scope

## Included

This package covers:

- the purpose of biomarker testing for targeted-treatment readiness;
- the concept of a predictive biomarker at a high level;
- the relationship between biomarker testing and targeted therapy;
- clinical-question-driven testing strategy;
- the distinction between targeted biomarker testing and broader molecular profiling;
- HER2 as a targeted-treatment-relevant biomarker domain;
- CLDN18.2 as a targeted-treatment-relevant biomarker domain;
- selected broader molecular targets such as NTRK, BRAF V600E, and RET at the testing-strategy level;
- FGFR2 as an example of a biomarker that may be encountered in precision-oncology testing;
- the role of NGS as a broader molecular-testing approach;
- the role of specimen availability and tissue adequacy;
- high-level tissue-versus-blood genomic-testing context;
- selected liquid-biopsy/ctDNA context where it directly affects testing strategy;
- timing of testing in relation to the clinical question;
- the concept of testing completeness and assay scope;
- negative, non-actionable, inadequate, and failed testing results;
- the possibility that additional testing may sometimes be considered when an earlier test does not answer the current clinical question;
- the relationship between testing strategy and molecular-report literacy;
- the relationship between testing strategy and biomarker-directed treatment selection;
- patient-facing questions and common misconceptions.

## Explicitly Excluded

This package does not own:

- detailed HER2 testing methodology or scoring;
- detailed MSI/MMR testing;
- detailed PD-L1 testing;
- detailed CLDN18.2 testing/scoring;
- detailed TMB testing;
- detailed FGFR2 testing;
- NGS laboratory methodology;
- sequencing chemistry;
- library preparation;
- bioinformatics;
- variant calling;
- detailed variant interpretation/classification;
- molecular-report literacy as a separate educational package;
- detailed ctDNA biology or longitudinal monitoring;
- companion-diagnostic regulatory methodology;
- treatment selection;
- drug selection;
- regimen selection;
- treatment sequencing;
- dosing;
- toxicity management;
- response assessment;
- resistance management;
- individualized testing recommendations;
- individualized treatment recommendations.

---


## Delegated-to PP

- PP-0181 — HER2 Testing
- PP-0182 — MSI/MMR Testing
- PP-0183 — PD-L1 Testing
- PP-0184 — CLDN18.2 Testing
- PP-0185 — TMB
- PP-0186 — FGFR2 Testing
- PP-0187 — NGS Biomarker Testing
- PP-0189 — Genomic Test Results / How to Read a Molecular Report
- PP-0190 — Biomarker-Directed Treatment Selection
- PP-0208 — Targeted Therapy in Gastric Cancer
- PP-0209 — HER2-targeted Therapy
- PP-0210 — CLDN18.2-targeted Therapy
- PP-0211 — Anti-angiogenic Therapy
- Relevant liquid-biopsy/ctDNA, companion-diagnostics, hereditary/genetic-testing, and downstream therapy packages

---

# 4. Clinical Knowledge Blocks

## Block 1 — What Is Biomarker Testing for Targeted Therapy?

Biomarker testing is testing performed to identify a biological characteristic of a cancer that may be relevant to a particular clinical decision.

In the context of targeted therapy, the purpose is not simply to collect as much molecular information as possible. The purpose is to determine whether the tumor has a characteristic that can meaningfully inform consideration of a targeted-treatment pathway.

The National Cancer Institute explains that biomarker tests may help predict response to certain targeted therapy drugs. This establishes the clinical bridge between testing and treatment planning without making the test itself a treatment decision.

A useful patient-facing sequence is:

> **What treatment opportunities might be relevant? → What biomarker information identifies those opportunities? → Which test can provide that information?**

The exact treatment decision remains downstream and depends on the full clinical situation.

---

## Block 2 — What Is a Predictive Biomarker?

A **predictive biomarker** is a biological characteristic that provides information about the likelihood that a patient may benefit from a particular treatment or treatment class.

This is different from a **prognostic biomarker**, which describes information about disease behavior or outcome independently of a specific treatment.

For this package, the important point is practical:

> **A targeted-treatment biomarker is useful because its result can help determine whether a particular treatment pathway should be considered.**

The presence of a biomarker does not, by itself, mean that a patient should receive a specific drug.

That distinction belongs to the boundary between PP-0191 and PP-0190.

---

## Block 3 — Why Is Testing Needed Before Targeted Treatment?

Targeted therapies are designed around particular biological features.

Examples in gastric-cancer care include treatment pathways associated with biomarkers such as HER2 or CLDN18.2. Other targeted-treatment opportunities may be associated with less-common genomic alterations.

Therefore, if the relevant biomarker has not been assessed, a treatment opportunity may not be recognized.

NCCN v2.2026 places biomarker assessment within the gastric-cancer clinical work-up and identifies HER2 and CLDN18.2 testing in appropriate advanced/metastatic settings. It also states that NGS should be considered and describes broader molecular testing for multiple events.

The key educational message is:

> **Testing makes certain treatment opportunities detectable; testing does not itself prescribe the treatment.**

---

## Block 4 — Testing Strategy Is Different From a Single Test

There is no single universal "biomarker test" for gastric cancer.

A testing strategy may include:

- a specific biomarker assay;
- several biomarker-specific assays;
- a broader molecular panel;
- or selected blood-based genomic testing when appropriate.

The appropriate strategy depends on the clinical question.

For example:

**Question:** Could HER2-directed treatment be relevant?

→ HER2 assessment is directly relevant.

**Question:** Could CLDN18.2-directed treatment be relevant?

→ CLDN18.2 assessment is directly relevant.

**Question:** Could an uncommon genomic alteration create another targeted-treatment opportunity?

→ Broader molecular profiling may be useful in selected circumstances.

The strategy should therefore be **question-driven**, not technology-driven.

---

## Block 5 — HER2 as a Targeted-Treatment-Relevant Biomarker

HER2, also known as ERBB2, is an important example of a biomarker that can identify a targeted-treatment pathway in gastric adenocarcinoma.

NCCN v2.2026 recommends assessment of HER2 overexpression using IHC with ISH/FISH or another appropriate ISH method when trastuzumab therapy is being considered in patients with inoperable locally advanced, recurrent, or metastatic gastric adenocarcinoma.

NCCN also notes that NGS can assess numerous mutations and other molecular events, including amplification, but it retains biomarker-specific approaches as the preferred initial strategy for specified biomarkers.

For PP-0191, the important point is:

> **HER2 testing is an example of a targeted biomarker test that may need to be available before a HER2-directed treatment pathway can be considered.**

Detailed HER2 IHC/ISH methodology and interpretation remain owned by PP-0181.

---

## Block 6 — CLDN18.2 as a Targeted-Treatment-Relevant Biomarker

CLDN18.2 is another important biomarker domain in gastric-cancer targeted treatment.

NCCN v2.2026 identifies CLDN18.2 testing when advanced/metastatic disease is documented or suspected and provides a defined biomarker-testing framework for patients for whom CLDN18.2-directed treatment may be considered.

The American Cancer Society similarly explains that patients with advanced stomach cancer may have their cancer cells tested for high levels of CLDN18.2 when determining whether they might benefit from a CLDN18.2-directed therapy.

For PP-0191:

> **CLDN18.2 belongs in the testing-strategy layer because its status may determine whether a targeted-treatment pathway can be considered.**

Detailed IHC methodology, scoring, thresholds, and interpretation remain delegated to PP-0184.

---

## Block 7 — Selected Less-Common Molecular Targets

Broad molecular testing can identify molecular alterations beyond the most commonly discussed gastric-cancer biomarkers.

The project Source Materials include examples such as:

- NTRK gene changes/fusions;
- BRAF V600E;
- RET gene fusions.

The American Cancer Society describes targeted treatment options associated with NTRK, BRAF, and RET alterations in selected advanced cancers.

NCCN also lists targeted-treatment options associated with NTRK gene fusions, BRAF V600E-mutated tumors, and RET gene fusions in appropriate clinical contexts.

For PP-0191, these examples demonstrate why a broader molecular-testing strategy may sometimes be clinically useful.

They do **not** establish that every patient should receive testing for every rare alteration, nor do they establish an automatic treatment recommendation.

---

## Block 8 — Why Broader Molecular Profiling Can Matter

A narrow biomarker test answers a narrow question.

A broader molecular panel can assess multiple molecular events simultaneously.

NCCN v2.2026 states that validated NGS may be considered later in the clinical course for patients with sufficient tumor tissue and that NGS can assess several mutations and other molecular events simultaneously.

ESMO-ASCO describes molecular assays that may be directed toward a specific analyte, a panel, or broader genomic approaches.

This creates a useful distinction:

### Targeted testing

> "I need to know whether this specific biomarker is present."

### Broader molecular profiling

> "I need to evaluate multiple molecular possibilities that may affect future clinical options."

Neither approach is universally superior.

The appropriate choice depends on the clinical question, disease context, available specimen, assay characteristics, and what clinical decisions may reasonably follow from the result.

---

## Block 9 — NGS Is Not Automatically Required for Everyone

A major misconception is:

> "If targeted therapy is being considered, every patient must have NGS."

The project Source Materials do not support this universal statement.

NCCN v2.2026 specifically distinguishes biomarker-specific approaches such as IHC, ISH, and targeted PCR from broader validated NGS.

For specified biomarkers, IHC/ISH/targeted PCR remains the preferred initial approach. NGS may be considered later in selected circumstances when sufficient tumor tissue is available.

Therefore:

> **NGS is a broader testing option within the overall strategy; it is not a universal replacement for every biomarker-specific test.**

---

## Block 10 — Tissue Availability Matters

Testing strategy depends partly on the specimen available.

Gastric-cancer molecular testing may use tumor tissue obtained from a biopsy or another appropriate specimen. The amount and quality of tumor material can influence whether testing can be successfully performed.

ESMO-ASCO identifies pre-analytic factors such as:

- tumor cellularity;
- quantity and quality of nucleic acids;
- specimen collection and preparation;
- transport;
- storage;
- analyte type.

The patient-facing implication is simple:

> **The best test is only useful if the available specimen can provide a reliable answer.**

A report that says a specimen was inadequate is different from a report that says a biomarker was not detected.

---

## Block 11 — Why One Test May Not Answer Every Question

Different tests examine different biological features.

For example:

- IHC can evaluate protein expression;
- ISH can evaluate gene amplification;
- targeted PCR can evaluate selected molecular changes;
- NGS can evaluate multiple molecular events.

Therefore, a previous test does not automatically answer every later biomarker question.

If the treatment question changes, the care team may need to determine whether the previous testing already provides the necessary information.

This is not the same as recommending routine repeat testing.

The principle is:

> **Testing should be sufficient for the current clinical question, but not assumed to be universally complete simply because one molecular test was already performed.**

---

## Block 12 — Tissue Versus Blood-Based Genomic Testing

NCCN recognizes blood-based circulating tumor DNA as a form of liquid biopsy.

In selected gastric-cancer circumstances, validated blood-based genomic testing may be considered when tissue is limited or when a patient with advanced/metastatic disease is not able to undergo a traditional biopsy.

This creates an important testing-strategy option.

However:

> **Blood-based genomic testing does not universally replace tissue-based testing.**

Tissue and blood can provide different types of information and may have different limitations.

Detailed ctDNA biology and longitudinal monitoring remain outside PP-0191.

---

## Block 13 — What Does a Negative Test Mean?

A negative result means that the assessed finding was not detected by the test within its defined scope.

It does **not** necessarily mean:

- no molecular alteration exists anywhere in the tumor;
- no future targeted-treatment opportunity could ever exist;
- every possible biomarker was tested;
- the cancer contains no genomic abnormalities.

The meaning of "negative" depends on:

- what was tested;
- which specimen was tested;
- which assay was used;
- what the assay was capable of detecting;
- whether the specimen was adequate.

Therefore:

> **Negative means "not detected by this test within its scope," not "nothing molecularly relevant exists."**

---

## Block 14 — Negative Versus Inadequate/Failed Testing

These are different outcomes.

### Negative

The test produced an interpretable result and the assessed biomarker was not detected.

### Inadequate / failed / insufficient

The test could not reliably answer the intended question.

The distinction matters because an inadequate test may leave the clinical question unresolved.

The package does not prescribe whether or how testing should be repeated. That decision depends on the clinical setting and the care team.

---

## Block 15 — What If No Actionable Alteration Is Found?

A broader molecular test may identify:

- an alteration with established clinical relevance;
- a potentially relevant alteration;
- a finding whose significance is uncertain;
- or no currently actionable alteration.

"No actionable alteration" does not mean:

> "The tumor contains no molecular changes."

It means that the test did not identify a finding that currently provides a clinically actionable pathway within the relevant interpretation framework.

This distinction is important for patient understanding and prevents overinterpretation of either positive or negative testing.

---

## Block 16 — Why More Testing Is Not Always Better

Broader testing can generate more information.

But more information is useful only when it can be interpreted appropriately and potentially connected to a meaningful clinical question.

A very broad test may produce:

- findings that are not clinically actionable;
- uncertain findings;
- findings outside the immediate treatment question;
- information requiring specialized interpretation.

Therefore:

> **The goal of testing is not to maximize the number of findings. The goal is to obtain clinically useful information with an appropriate testing strategy.**

This is a central principle of PP-0191.

---

## Block 17 — What Is the Difference Between Testing and Treatment Selection?

PP-0191 ends at:

> **"Do we have the appropriate biomarker information?"**

PP-0190 begins at:

> **"Given the biomarker information, how does it affect targeted-treatment selection?"**

For example:

**HER2 testing**

→ establishes HER2 status

**Molecular report**

→ documents the result

**PP-0190**

→ explains how the result may direct consideration of targeted therapy

**Downstream treatment PP**

→ explains the treatment itself

This separation prevents PP-0191 from becoming a duplicate treatment-selection package.

---

## Block 18 — Relationship With Molecular Report Literacy

PP-0189 owns:

> **How to understand a molecular/genomic report.**

PP-0191 owns:

> **What testing strategy should be considered to make targeted-treatment opportunities detectable.**

The sequence is:

**Testing strategy**

↓

**Testing**

↓

**Result / molecular report**

↓

**Report literacy**

↓

**Biomarker-directed treatment application**

The two packages are therefore complementary.

---

## Block 19 — When Might Additional Testing Be Considered?

Additional testing may sometimes be considered when:

- the original test did not assess the biomarker relevant to the current treatment question;
- the previous specimen was inadequate;
- the previous assay had a narrower scope;
- broader molecular profiling becomes relevant to the clinical question;
- tissue is unavailable or insufficient and a validated blood-based approach may be appropriate in selected circumstances.

The package deliberately avoids creating a universal repeat-testing schedule.

The correct principle is:

> **Additional testing is a clinical question, not an automatic step after every prior test.**

---

## Block 20 — Molecular Tumor Board / Multidisciplinary Review

Complex molecular testing may produce findings that require integration of:

- pathology;
- oncology;
- molecular testing;
- biomarker interpretation;
- treatment options;
- clinical context.

A multidisciplinary or molecular-tumor-board approach may therefore be relevant in selected situations.

PP-0191 may introduce this concept as a supporting principle.

It does not prescribe when a molecular tumor board must be convened.

---

## Block 21 — Germline Implications Are Separate

Tumor testing may sometimes identify findings that raise a question about inherited cancer risk.

ESMO-ASCO and NCI Genetics PDQ support the possibility that somatic/tumor profiling can reveal findings that warrant confirmatory germline evaluation and genetic counselling.

However:

> **A molecular finding in a tumor does not automatically mean that the same finding is inherited.**

PP-0191 should alert readers to this distinction but does not own hereditary cancer assessment or germline testing.

---

## Block 22 — Patient-Facing Testing Questions

Patients may reasonably ask:

1. What biomarker tests are relevant to my current treatment situation?
2. Has HER2 been tested?
3. Has CLDN18.2 been tested if it is relevant to my disease setting?
4. Has broader molecular testing been considered?
5. What genes or biomarkers were included in the test?
6. What specimen was tested?
7. Was the specimen adequate?
8. Was the test negative, inconclusive, or technically unsuccessful?
9. Does the test cover the biomarker needed for the treatment being considered?
10. If the test was negative, what exactly was ruled out?
11. Would a broader or different test answer an unanswered clinical question?
12. Would blood-based genomic testing be useful if tissue is limited?
13. Does the result require review by a molecular pathology or multidisciplinary team?
14. Does any result raise a separate question about inherited cancer risk?
15. How does the result connect to the next treatment discussion?

---

# 5. Common Misconceptions

## Myth 1 — "Everyone who may receive targeted therapy needs every biomarker test."

**Fact:** Testing should be connected to the clinical question and the treatment opportunities that need to be evaluated.

---

## Myth 2 — "NGS replaces all other biomarker tests."

**Fact:** NCCN distinguishes biomarker-specific approaches such as IHC/ISH/targeted PCR from broader validated NGS.

---

## Myth 3 — "The largest molecular panel is always the best test."

**Fact:** Broader testing can identify more molecular events, but its usefulness depends on clinical context, specimen availability, assay scope, and whether the findings can meaningfully inform care.

---

## Myth 4 — "A negative biomarker test means there is no molecular target."

**Fact:** A negative result applies to the biomarker and assay scope that were actually assessed.

---

## Myth 5 — "A failed test is the same as a negative test."

**Fact:** An inadequate or failed test may mean that the clinical question remains unanswered.

---

## Myth 6 — "If a mutation is found, the patient automatically qualifies for a drug."

**Fact:** A molecular finding may be potentially relevant, but treatment selection requires interpretation in the clinical context.

---

## Myth 7 — "Blood and tissue molecular tests are interchangeable."

**Fact:** They may provide different information and have different limitations. Blood-based testing may be useful in selected circumstances but does not universally replace tissue testing.

---

## Myth 8 — "A tumor mutation proves that the patient inherited the mutation."

**Fact:** Tumor findings may sometimes raise a question about inherited risk, but confirmation requires appropriate germline evaluation.

---

## Myth 9 — "Testing is complete once any molecular test has been done."

**Fact:** Different assays answer different questions. A previous test may not include the biomarker relevant to a later treatment question.

---

## Myth 10 — "Biomarker testing tells the doctor exactly which treatment to give."

**Fact:** Biomarker testing provides biological information. Treatment selection is a downstream clinical decision.

---

# 6. Key Messages

1. **Biomarker testing is part of precision treatment planning, not a treatment order.**
2. **The right test depends on the clinical question.**
3. **HER2 and CLDN18.2 are important targeted-treatment-relevant biomarker domains in gastric cancer.**
4. **Broader molecular profiling can identify additional molecular alterations in selected circumstances.**
5. **NGS is not a universal replacement for biomarker-specific testing.**
6. **Specimen availability and quality matter.**
7. **Blood-based genomic testing may be useful in selected situations when tissue is limited, but it does not universally replace tissue testing.**
8. **A negative result applies to the scope and limitations of the test performed.**
9. **An inadequate test is not the same as a negative test.**
10. **No actionable alteration does not mean no molecular alteration exists.**
11. **A molecular finding does not automatically determine treatment.**
12. **Testing strategy, molecular-report literacy, and treatment selection are distinct knowledge layers.**
13. **Complex findings may require multidisciplinary clinical interpretation.**
14. **Tumor findings and inherited genetic findings are not automatically the same.**

---

# 7. Knowledge Graph

## Prerequisite PP

- PP-0015 — Biomarker Testing for Gastric Adenocarcinoma / foundational biomarker-testing concepts where applicable.
- PP-0181 — HER2 Testing.
- PP-0184 — CLDN18.2 Testing.
- PP-0187 — NGS Biomarker Testing.
- PP-0189 — Genomic Test Results / How to Read a Molecular Report, as the immediate interpretive bridge.
- Foundational molecular-testing / precision-oncology concepts.

## Related PP

- PP-0182 — MSI/MMR Testing.
- PP-0183 — PD-L1 Testing.
- PP-0185 — TMB.
- PP-0186 — FGFR2 Testing.
- PP-0188 — Molecular Subtypes of Gastric Cancer.
- PP-0110 — Somatic Genetic Testing.
- PP-0111 — Liquid Biopsy.
- Relevant hereditary/germline-testing packages.
- Companion Diagnostics packages.

## Next / Downstream

- **PP-0190 — Biomarker-Directed Treatment Selection**.
- PP-0208 — Targeted Therapy in Gastric Cancer.
- PP-0209 — HER2-targeted Therapy.
- PP-0210 — CLDN18.2-targeted Therapy.
- PP-0211 — Anti-angiogenic Therapy.
- Other therapy-specific Population Packages supported by the project package list.

---

# 8. Clinical Safety Boundary

This Population Package provides general education about biomarker testing strategy in gastric adenocarcinoma.

It does not determine which test an individual patient should undergo, whether a test is medically necessary, whether a molecular result is actionable for a specific patient, or which treatment should be selected.

A testing decision may require review of:

- disease setting;
- pathology;
- available tissue;
- previous biomarker testing;
- molecular results;
- current treatment history;
- guideline recommendations;
- laboratory capabilities;
- clinical-trial availability;
- the complete clinical situation.

---

# 9. Revision History

| Version | Date | Summary |
|---|---|---|
| 1.0.0 | 2026-08-09 | Initial Gold production from the approved and locked PP-0191 Decision Batch. |
