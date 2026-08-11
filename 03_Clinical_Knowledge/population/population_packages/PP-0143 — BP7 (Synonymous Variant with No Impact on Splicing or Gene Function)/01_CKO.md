# Clinical Knowledge Object (CKO)

---

## Metadata

| Field | Value |
|-------|-------|
| CKO ID | CKO-PP-0143 |
| Population Package ID | PP-0143 |
| Title | BP7 (Synonymous Variant with No Impact on Splicing or Gene Function) |
| Clinical Domain | Understanding Cancer |
| Population Wave | Wave 1 |
| Version | 1.0.0 |
| Audience | General public, patients diagnosed with cancer, caregivers |
| Reading Level | Plain language |
| Last Updated | 2026-08-08 |

---

# Educational Objectives

After reading this Population Package, the reader should be able to:

- Understand what BP7 is.
- Understand what a synonymous or "silent" variant means.
- Understand why a synonymous variant is not automatically harmless.
- Understand why possible effects on RNA splicing are important.
- Understand how evidence suggesting no meaningful splicing effect can support a benign interpretation.
- Understand that BP7 provides supporting evidence and does not by itself establish that a variant is benign.

---

# Scope

## Included

- Definition of BP7
- Meaning of synonymous/silent variant
- Relationship between synonymous variants and RNA splicing
- Why splicing must be considered
- Role of computational splicing evidence
- Supporting Benign Evidence
- Current ClinGen SVI refinement
- Common misconceptions
- Key messages

---

## Not Included

This Population Package does **not** explain:

- SpliceAI methodology
- MaxEntScan
- Individual splice prediction algorithms
- RNA sequencing methodology
- RT-PCR
- Minigene assays
- Detailed splice-position calculations
- Gene-specific BP7 specifications
- BP7_Strong(RNA) implementation
- Bayesian framework
- ACMG evidence combination rules
- Laboratory workflow
- Treatment recommendations

These topics are covered in separate Population Packages.

---

# Knowledge Block 1 — What Is BP7?

## Patient Explanation

**BP7** is an ACMG/AMP **Supporting Benign Evidence** criterion used when a genetic variant is a **synonymous (silent) variant** and available evidence indicates that it is unlikely to interfere with RNA splicing.

A synonymous variant does not change the amino acid encoded by the usual genetic code, but it can still potentially affect how RNA is processed.

When evidence indicates that the variant is unlikely to affect splicing, BP7 may provide supporting evidence for a benign interpretation.

---

## Clinical Importance

BP7 helps address an important question:

> Could a "silent" genetic change still affect how the gene is processed?

If available evidence suggests that it does not, this can support a benign interpretation.

---

## Key Concepts

- BP7
- Synonymous variant
- Silent variant
- RNA splicing
- Supporting benign evidence

---

# Knowledge Block 2 — What Is a Synonymous or "Silent" Variant?

## Patient Explanation

A **synonymous variant** is a genetic change that does not change the amino acid normally specified by the affected codon.

It is sometimes called a **"silent" variant** because the resulting protein sequence may remain unchanged.

However, "silent" does **not** necessarily mean "no biological effect."

---

## Clinical Importance

Some synonymous variants can affect other steps in gene processing, especially **RNA splicing**.

---

# Knowledge Block 3 — Why Can a Silent Variant Affect Splicing?

## Patient Explanation

Before a gene's information is used to make a protein, the initial RNA copy is processed.

One important step is **splicing**, during which sections of RNA are joined together to produce the mature RNA message.

A synonymous variant can sometimes interfere with signals involved in this process.

If splicing is altered, the final RNA message can be abnormal even though the encoded amino acid at the variant's position has not changed.

---

## Clinical Importance

This is why a synonymous variant cannot automatically be assumed to be harmless simply because it does not change an amino acid.

---

# Knowledge Block 4 — How Does BP7 Support a Benign Interpretation?

## Patient Explanation

BP7 can be considered when evidence indicates that a synonymous variant is unlikely to affect normal RNA splicing.

The original ACMG/AMP framework considered computational predictions of splicing impact and conservation.

Current ClinGen SVI recommendations further emphasize evaluating predicted splicing impact and avoiding BP7 in synonymous variants located very close to exon boundaries, where effects on splicing are more likely.

---

## Clinical Importance

BP7 therefore represents **supporting evidence**, not proof that the variant has no biological effect.

---

# Knowledge Block 5 — Why Does Variant Location Matter?

## Patient Explanation

The location of a synonymous variant can matter.

Some positions near the beginning or end of an exon are especially important for normal RNA splicing.

For this reason, current ClinGen SVI splicing recommendations advise against applying BP7 to synonymous variants located at the **first nucleotide or the last three nucleotides of an exon**.

---

## Clinical Importance

The same type of genetic change can have different implications depending on where it occurs.

---

# Knowledge Block 6 — Does BP7 Mean the Variant Is Definitely Benign?

## Patient Explanation

No.

BP7 provides **Supporting Benign Evidence**.

It does not prove that a variant is benign by itself.

Genetics professionals consider BP7 together with other available evidence before determining the overall classification of a genetic variant.

---

## Clinical Importance

Final variant classification requires integration of multiple evidence categories.

---

# Common Misconception

**Myth**

A synonymous or "silent" variant cannot cause disease because it does not change the protein sequence.

**Fact**

Not necessarily.

Some synonymous variants can affect RNA splicing or other aspects of gene function.

BP7 is used only when appropriate evidence supports the conclusion that the variant is unlikely to have a meaningful effect, particularly on splicing.

---

# Key Messages

- BP7 is a **Supporting Benign Evidence** criterion.
- A synonymous or "silent" variant does not change the usual encoded amino acid.
- "Silent" does **not** automatically mean harmless.
- Synonymous variants can sometimes affect RNA splicing.
- Evidence suggesting no meaningful splicing effect can support a benign interpretation.
- Variant location matters, particularly near exon boundaries.
- BP7 alone does not establish that a variant is benign.

---

# Knowledge Graph

## Prerequisite Population Packages

PP-0001 → PP-0142

---

## Related Population Packages

- PP-0140 BP4
- PP-0136 BP Evidence Codes
- PP-0133 PP3
- PP-0116 ACMG Evidence Codes
- PP-0115 ACMG Variant Classification Framework
- PP-0108 Variant Classification

---

## Future Population Packages

- Splice prediction
- SpliceAI
- RNA evidence
- Functional splicing assays
- Deep intronic variants
- BP7_Strong(RNA)
- ACMG/ClinGen Splicing Framework

---

# Governance Status

**Current ACMG/ClinGen Evidence Criterion — CONTEXT-DEPENDENT APPLICATION**

BP7 remains part of current variant interpretation practice, but its application should follow the applicable ClinGen SVI recommendations and, where available, disease/gene-specific ClinGen Expert Panel specifications.

The Safe Medical AI System must not present the original ACMG/AMP wording as an unrestricted universal rule.

---

# Revision History

| Version | Date | Summary |
|----------|------|---------|
| 1.0.0 | 2026-08-08 | Initial Gold Release |