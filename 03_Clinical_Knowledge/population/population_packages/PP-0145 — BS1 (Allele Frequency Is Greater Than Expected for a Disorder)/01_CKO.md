# Clinical Knowledge Object (CKO)

---

## Metadata

| Field | Value |
|-------|-------|
| CKO ID | CKO-PP-0145 |
| Population Package ID | PP-0145 |
| Title | BS1 (Allele Frequency Is Greater Than Expected for a Disorder) |
| Clinical Domain | Understanding Cancer |
| Population Wave | Wave 1 |
| Version | 1.0.0 |
| Audience | General public, patients diagnosed with cancer, caregivers |
| Reading Level | Plain language |
| Last Updated | 2026-08-08 |

---

# Educational Objectives

After reading this Population Package, the reader should be able to:

- Understand what BS1 is.
- Understand what allele frequency means.
- Understand why a variant that is more common than expected for a particular disorder may provide strong benign evidence.
- Understand why BS1 depends on the specific disorder rather than one universal frequency cutoff.
- Understand why population frequency must be interpreted in clinical and population context.
- Understand that BS1 is strong evidence but is not itself a universal shortcut to variant classification.

---

# Scope

## Included

- Definition of BS1
- Meaning of allele frequency
- Meaning of "greater than expected for a disorder"
- Why high population frequency can support a benign interpretation
- Disease-specific context
- General factors influencing expected frequency
- Relationship between BS1 and other benign evidence categories
- Common misconceptions
- Key messages

---

## Not Included

This Population Package does **not** explain:

- Numerical BS1 thresholds for individual genes or disorders
- gnomAD technical methodology
- PopMax / GrpMax / FAF implementation
- Whiffin/Ware calculator methodology
- Founder-effect calculations
- Detailed ancestry/population-stratification methodology
- BA1 implementation
- Bayesian framework
- ACMG benign evidence-combination rules
- Gene-specific ClinGen VCEP specifications
- Laboratory workflow
- Treatment recommendations

These topics are covered in separate Population Packages.

---

# Knowledge Block 1 — What Is BS1?

## Patient Explanation

**BS1** is an ACMG/AMP **Strong Benign Evidence** criterion.

It can be considered when a genetic variant occurs in a population at a frequency that is **higher than would be expected for the particular disorder** being evaluated.

If a variant is much too common to reasonably explain a rare disorder, that population frequency can provide strong evidence that the variant is unlikely to be disease-causing.

---

## Clinical Importance

BS1 uses information about how common a variant is in a population to help assess whether the variant could realistically be responsible for a particular disorder.

---

## Key Concepts

- BS1
- Allele frequency
- Population frequency
- Strong Benign Evidence
- Disorder-specific interpretation

---

# Knowledge Block 2 — What Is Allele Frequency?

## Patient Explanation

**Allele frequency** describes how often a particular genetic version, or allele, is observed in a population.

For example, if a particular allele is observed in a small number of people, its population frequency is low. If it is observed in many people, its frequency is higher.

Genetics professionals can compare this frequency with how common a particular disorder is expected to be.

---

## Clinical Importance

Population frequency can provide important evidence about whether a genetic variant is plausible as a disease-causing variant.

---

# Knowledge Block 3 — What Does "Greater Than Expected for a Disorder" Mean?

## Patient Explanation

A variant may be considered **more common than expected** when its population frequency is too high to be compatible with the expected frequency and genetic characteristics of the disorder.

For example, if a disorder is very rare and usually caused by rare genetic variants, finding a particular variant in a substantial proportion of the general population may make it unlikely that the variant is responsible for that disorder.

The important point is that:

> **The expected frequency depends on the disorder.**

There is no single frequency that automatically defines BS1 for every disease.

---

## Clinical Importance

BS1 is therefore a **disease-specific concept**, not simply a fixed percentage.

ClinGen Expert Panel specifications demonstrate that actual BS1 thresholds can differ substantially between disorders depending on the underlying disease model and available population data. :contentReference[oaicite:0]{index=0}

---

# Knowledge Block 4 — Why Can a High Frequency Support a Benign Interpretation?

## Patient Explanation

If a genetic variant were responsible for a rare disorder, the variant generally could not be extremely common in the general population unless the disease model allowed that frequency.

Therefore, when a variant is observed much more frequently than would be expected for the disorder, its frequency provides a reason to question whether it is actually disease-causing.

This is the basic principle behind BS1.

---

## Clinical Importance

The original ACMG/AMP framework identifies an allele frequency greater than expected for the disorder as **Strong evidence of benign impact**. :contentReference[oaicite:1]{index=1}

---

# Knowledge Block 5 — Why Is There No Universal BS1 Cutoff?

## Patient Explanation

Different disorders have different characteristics.

The expected frequency of a disease-causing variant can depend on factors such as:

- how common the disorder is;
- how strongly a variant causes the disorder;
- how many different genes can cause the disorder;
- how many different variants can cause it;
- how strongly the disease is inherited.

For this reason, the same population frequency may provide strong benign evidence for one disorder but not necessarily for another.

---

## Clinical Importance

Current ClinGen disease-specific specifications illustrate this principle. Different Expert Panels may establish different BS1 thresholds based on disease prevalence, penetrance, genetic heterogeneity, allelic heterogeneity and population data. :contentReference[oaicite:2]{index=2}

---

# Knowledge Block 6 — Does "Common" Mean "Benign"?

## Patient Explanation

No.

A variant being relatively common does **not automatically** mean that it is benign.

The relevant question is:

> **Is the variant more common than would be expected for this particular disorder?**

Population frequency must therefore be interpreted together with the disease and its genetic characteristics.

---

## Clinical Importance

A population frequency should not be treated as an isolated numerical answer.

---

# Knowledge Block 7 — Is BS1 the Same as BA1?

## Patient Explanation

No.

Both use population frequency, but they represent different evidence strengths.

- **BS1** = Strong Benign Evidence because the frequency is greater than expected for the specific disorder.
- **BA1** = Stand-Alone Benign Evidence under the applicable framework.

This Population Package focuses only on **BS1**.

---

## Clinical Importance

The distinction prevents the different benign evidence categories from being treated as interchangeable.

---

# Common Misconceptions

**Myth 1**

A variant that is common is automatically benign.

**Fact**

Not necessarily. The frequency must be considered in relation to the specific disorder.

---

**Myth 2**

BS1 always means a variant is above one fixed percentage.

**Fact**

No. BS1 thresholds can be disease- and gene-specific.

---

**Myth 3**

Population frequency alone proves that a variant cannot cause disease.

**Fact**

BS1 provides strong benign evidence within the applicable framework. It should not be reduced to an isolated numerical rule.

---

# Key Messages

- **BS1** is a **Strong Benign Evidence** criterion.
- BS1 considers whether a variant is **more common than expected for a particular disorder**.
- A variant that is too common to be compatible with a rare disorder may be unlikely to cause that disorder.
- There is **no universal BS1 frequency cutoff for every disorder**.
- Disease prevalence, penetrance, genetic heterogeneity, allelic heterogeneity and population context can affect interpretation.
- A variant being common does not automatically mean it is benign.
- BS1 is evidence within a structured variant interpretation framework, not simply a frequency-based shortcut.

---

# Knowledge Graph

## Prerequisite Population Packages

PP-0001 → PP-0144

---

## Related Population Packages

- PP-0144 BS Evidence Codes
- PP-0136 BP Evidence Codes
- PP-0116 ACMG Evidence Codes
- PP-0115 ACMG Variant Classification Framework
- PP-0108 Variant Classification

---

## Future Population Packages

- BS2
- BS3
- BS4
- BA1
- Population Frequency / gnomAD
- PopMax / GrpMax / FAF
- Founder Effect
- Disease-specific BS1 Thresholds
- ACMG Benign Evidence Combination Rules

---

# Governance Status

**Current ACMG/AMP Evidence Criterion — CONTEXT-DEPENDENT APPLICATION**

BS1 remains a Strong Benign Evidence criterion, but its application must follow the applicable ClinGen SVI guidance and, where available, disease- or gene-specific ClinGen Expert Panel specifications.

The Safe Medical AI System must not present a single numerical frequency as a universal BS1 threshold.

---

# Revision History

| Version | Date | Summary |
|----------|------|---------|
| 1.0.0 | 2026-08-08 | Initial Gold Release |