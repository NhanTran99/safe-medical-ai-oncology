# PP-0188 — Molecular Subtypes of Gastric Cancer
## Primary Evidence Package

**EP ID:** EP-PP-0188  
**PP ID:** PP-0188  
**Version:** 1.0.0  
**Status:** GOLD — LOCKED / READY FOR INTEGRATION  
**Last Updated:** 2026-08-09

---

# 1. Clinical Question

> What major molecular-subtyping frameworks have been developed for gastric cancer, what are their defining biological and clinical characteristics, how do TCGA and ACRG compare, and what do these classifications mean clinically?

---

# 2. Educational Intent

This Evidence Package supports a patient-facing knowledge object that explains:

1. why gastric cancer has multiple molecular phenotypes;
2. the TCGA four-subtype framework;
3. the ACRG four-subtype framework;
4. the biological and clinical meaning of each framework;
5. the overlap and non-equivalence between the two;
6. the distinction between molecular subtype, individual biomarker, histology, and stage;
7. the difference between research-level molecular classification and routine clinical testing;
8. the limits of using retrospective subtype associations to infer treatment decisions.

---

# 3. Scope

## Included

- TCGA molecular subtypes: EBV, MSI, GS, CIN.
- ACRG molecular subtypes: MSI, MSS/EMT, MSS/TP53+, MSS/TP53−.
- Biological characteristics.
- Selected clinical phenotype.
- Prognostic associations.
- Recurrence associations.
- TCGA retrospective chemotherapy-response evidence.
- Cross-framework comparison.
- Non-equivalence.
- Relationship to Lauren classification and individual biomarkers.
- Clinical implementation limitations.

## Excluded

- detailed laboratory methodology;
- individual biomarker testing;
- genomic report interpretation;
- variant interpretation;
- treatment algorithms;
- individualized prognosis;
- universal clinical subtype testing;
- hereditary/germline classification;
- longitudinal molecular monitoring.

---

# 4. Primary Evidence Sources

## S0 — Current Clinical Guideline Anchor

**NCCN Clinical Practice Guidelines in Oncology: Gastric Cancer, Version 2.2026.**

Role:

- current clinical framework;
- clinical biomarker/testing context;
- prevention of overstatement of research molecular classifications as universal routine testing.

The NCCN source is treated as the current clinical anchor; the TCGA and ACRG papers provide the detailed molecular-classification evidence.

---

## S1 — TCGA Clinical Validation

**Sohn BH, Hwang JE, Jang HJ, et al. Clinical significance of four molecular subtypes of gastric cancer identified by The Cancer Genome Atlas project. Clin Cancer Res. 2017;23:4441–4449. doi:10.1158/1078-0432.CCR-16-2211.**

Role:

- validates the four TCGA molecular subtypes using gene-expression prediction;
- demonstrates reproducibility in two independent patient cohorts;
- provides survival associations;
- provides recurrence-free survival associations;
- evaluates retrospective adjuvant chemotherapy benefit;
- describes subtype-specific biological characteristics.

Source file: **Clinical significance of four molecular subtypes of gastric cancer identified by The Cancer Genome Atlas project.pdf**

---

## S2 — ACRG Molecular Classification

**Cristescu R, Lee J, Nebozhyn M, et al. Molecular analysis of gastric cancer identifies subtypes associated with distinct clinical outcomes. Nat Med. 2015. doi:10.1038/nm.3850.**

Role:

- establishes ACRG molecular classification;
- defines MSI, MSS/EMT, MSS/TP53+, MSS/TP53−;
- provides molecular characterization;
- validates classification in independent cohorts;
- evaluates prognosis;
- evaluates recurrence patterns;
- directly compares ACRG with TCGA and other molecular classifications.

Source file: **Molecular analysis of gastric cancer identifies subtypes associated with distinct clinical outcomes.pdf**

---

## S3 — TCGA Foundational Molecular Characterization

**Cancer Genome Atlas Research Network. Comprehensive molecular characterization of gastric adenocarcinoma. Nature. 2014;513:202–209.**

Role:

- foundational TCGA gastric-cancer molecular characterization;
- basis for the EBV, MSI, GS and CIN genomic subtype framework.

---

# 5. Evidence Hierarchy

| Level | Evidence | Role |
|---|---|---|
| 1 | NCCN v2.2026 | Current clinical/guideline anchor |
| 2 | TCGA 2014 | Foundational molecular characterization |
| 2 | ACRG 2015 | Foundational independent molecular classification |
| 2 | Sohn 2017 | TCGA clinical validation |
| 3 | Cohort-level subtype associations within S1/S2 | Prognosis/recurrence/translational interpretation |

---

# 6. Evidence Matrix

| Clinical Claim | Evidence | Strength / Interpretation |
|---|---|---|
| Gastric cancer is molecularly heterogeneous | S1, S2, S3 | Strong; foundational |
| TCGA defines EBV, MSI, GS, CIN | S1, S3 | Strong |
| ACRG defines MSI, MSS/EMT, MSS/TP53+, MSS/TP53− | S2 | Strong |
| TCGA and ACRG are not interchangeable | S2 | Strong; direct comparative analysis |
| TCGA EBV has favorable prognosis in validation cohorts | S1 | Strong cohort-level association |
| TCGA GS has least favorable prognosis in validation cohorts | S1 | Strong cohort-level association |
| TCGA MSI and CIN show intermediate prognosis in S1 | S1 | Cohort-level association |
| ACRG MSI has best prognosis | S2 | Replicated cohort-level association |
| ACRG MSS/EMT has worst prognosis | S2 | Replicated cohort-level association |
| ACRG MSS/EMT has highest recurrence | S2 | Strong within supplied cohorts |
| ACRG MSI has lowest recurrence | S2 | Strong within supplied cohorts |
| MSS/EMT is associated with diffuse histology and signet-ring disease | S2 | Strong association |
| ACRG MSI is associated with intestinal histology and earlier stage | S2 | Strong association |
| EBV-positive tumors are enriched in ACRG MSS/TP53+ | S2 | Association; not equivalence |
| TCGA GS is enriched in ACRG MSS/EMT | S2 | Association; not equivalence |
| TCGA CIN is enriched in ACRG MSS/TP53− | S2 | Association; not equivalence |
| TCGA CIN benefit from adjuvant chemotherapy was observed retrospectively | S1 | Exploratory/retrospective; not routine predictive evidence |
| TCGA GS did not show significant adjuvant chemotherapy benefit in S1 | S1 | Exploratory/retrospective |
| Molecular subtype alone should not determine treatment | S0 + limitations of S1/S2 | Governance/clinical interpretation |
| Molecular subtype does not replace Lauren classification | S2 + PP boundary | Architecture-supported |
| Molecular subtype does not replace TNM stage | S0 + PP boundary | Clinical architecture |
| TCGA/ACRG are not universal interchangeable routine clinical tests | S0, S1, S2 | Current implementation interpretation |

---

# 7. Detailed Evidence Notes

## 7.1 TCGA classification

Sohn et al. describe the TCGA framework as:

- EBV;
- MSI;
- GS;
- CIN.

The TCGA molecular characterization integrated multiple genomic/proteomic data types. The Sohn validation study subsequently generated gene-expression signatures and a decision-tree prediction model using TCGA-derived subtype signatures. [S1]

The decision sequence used in the validation model was:

**EBV → MSI → GS → CIN**

according to Bayesian probability thresholds.

The exact algorithm is evidence context only and is not part of the patient-facing clinical scope.

---

## 7.2 TCGA EBV biology

Sohn et al. describe EBV tumors as showing:

- extreme promoter/DNA hypermethylation;
- frequent PIK3CA mutation;
- cytokine/immune activation;
- distinctive metabolic changes.

EBV was associated with the best prognosis in both validation cohorts. [S1]

This supports a clinically meaningful association, but not an individualized prognostic rule.

---

## 7.3 TCGA MSI biology

MSI was associated with:

- high mutation rate;
- hypermethylation;
- distinct molecular phenotype.

MSI is also a clinically actionable biomarker domain, but detailed MSI/MMR testing is owned by PP-0182.

---

## 7.4 TCGA GS biology

The TCGA GS subtype was characterized by:

- low mutation rate;
- low copy-number alteration;
- frequent CDH1 and RHOA alterations.

It had the poorest overall clinical outcome among the TCGA groups in the validation cohorts. [S1]

The ACRG comparison is particularly important: TCGA GS and ACRG MSS/EMT overlap but differ in molecular and histologic details. [S2]

---

## 7.5 TCGA CIN biology

CIN was characterized by:

- marked aneuploidy;
- high copy-number alteration;
- focal amplification of receptor tyrosine kinases.

CIN showed intermediate prognosis overall in the Sohn validation work, although the exact outcome pattern was less homogeneous across validation cohorts than EBV or GS. [S1]

---

# 8. TCGA Prognostic Evidence

The Sohn study used two independent validation cohorts:

- MD Anderson Cancer Center: n=267;
- Samsung Medical Center: n=432.

The overall pattern was:

**EBV best → MSI/CIN intermediate → GS worst.**

The MD Anderson cohort showed:

- RFS P=0.006;
- OS P=0.004.

The Samsung cohort reproduced the broad pattern:

- RFS P=0.04;
- OS P=0.03.

[S1]

The evidence supports:

> TCGA molecular subtype captures clinically relevant heterogeneity.

It does not support:

> molecular subtype alone as an individualized prognostic calculator.

---

# 9. TCGA Treatment-Response Evidence

In the subset analysis of stage II/III/IV disease without distant metastasis:

### CIN

- HR for recurrence with adjuvant chemotherapy: 0.39
- 95% CI: 0.16–0.94
- P=0.03

### GS

- HR: 0.83
- 95% CI: 0.36–1.89
- P=0.65

### MSI

- HR: 0.55
- 95% CI: 0.22–1.3
- P=0.18

### EBV

Benefit could not be assessed because all patients received chemotherapy.

[S1]

The paper explicitly states that the retrospective study design limited the predictive nature of this association.

### Evidence classification

**Exploratory / hypothesis-generating**

Not sufficient to establish:

> TCGA subtype-guided chemotherapy as routine clinical practice.

---

# 10. ACRG Classification Evidence

ACRG analyzed 300 primary gastric tumors and identified:

- MSI: n=68;
- MSS/EMT: n=46;
- MSS/TP53+: n=79;
- MSS/TP53−: n=107.

[S2]

The classification used expression signatures to identify MSI and EMT groups and then used a TP53-activity signature to separate the remaining MSS tumors.

---

# 11. ACRG MSI Evidence

ACRG MSI:

- hypermutated;
- MLH1 expression loss;
- increased methylation;
- predominantly intestinal;
- often antral;
- frequently earlier stage.

More than 60% of ACRG MSI tumors were intestinal, and more than half were stage I/II. [S2]

### Prognosis

Best among ACRG subtypes.

### Recurrence

Pooled ACRG + SMC-2:

**26/117 = 22.2%**

[S2]

---

# 12. ACRG MSS/EMT Evidence

MSS/EMT:

- MSS;
- EMT signature;
- diffuse Lauren phenotype;
- signet-ring-cell enrichment;
- CDH1 expression loss;
- younger age;
- advanced stage.

More than 80% were diffuse-type, and most were stage III/IV. [S2]

### Prognosis

Worst among ACRG groups.

### Recurrence

Pooled ACRG + SMC-2:

**64/101 = 63.4%**

### Peritoneal recurrence

**41/64 = 64.1%** of documented recurrences in the pooled data were associated with peritoneal seeding.

[S2]

These findings are important clinical associations but are not an individualized recurrence prediction model.

---

# 13. ACRG MSS/TP53+ Evidence

MSS/TP53+ represents relatively preserved TP53 activity.

The two-gene TP53 activity signature used:

- MDM2;
- CDKN1A/p21.

The signature was significantly associated with TP53 mutation status. [S2]

EBV-positive tumors were enriched in this subgroup:

**12/18 EBV-positive tumors**

were in MSS/TP53+. [S2]

This supports association, not identity.

---

# 14. ACRG MSS/TP53− Evidence

MSS/TP53− represents reduced/inactive TP53-related activity.

It was associated with:

- TP53 mutation;
- broad CNV damage;
- intermediate prognosis.

Pooled recurrence:

**85/195 = 43.6%**

[S2]

---

# 15. ACRG Survival Validation

The ACRG study reproduced subtype-associated survival patterns in:

- ACRG cohort, n=300;
- SMC-2, n=277;
- Singapore, n=200;
- TCGA gastric cohort, n=205 with survival data.

Merged cohorts showed highly significant survival trends. [S2]

The broad survival ordering was:

**MSS/EMT < MSS/TP53− < MSS/TP53+ < MSI**

for prognosis from worse to better.

---

# 16. ACRG Recurrence Validation

Pooled ACRG + SMC-2 recurrence rates:

| ACRG subtype | Recurrence |
|---|---:|
| MSS/TP53− | 43.6% |
| MSS/TP53+ | 37.2% |
| MSI | 22.2% |
| MSS/EMT | 63.4% |

[S2]

Peritoneal recurrence was especially frequent among MSS/EMT recurrences:

| Subtype | Peritoneal seeding among documented recurrences |
|---|---:|
| MSS/TP53− | 23.5% |
| MSS/TP53+ | 24.6% |
| MSI | 15.4% |
| MSS/EMT | 64.1% |

[S2]

These values describe the supplied cohorts and should not be presented as universal patient-specific risks.

---

# 17. Direct TCGA–ACRG Comparison

The ACRG study directly applied both classification systems to the available datasets.

Broad enrichment relationships were:

- TCGA GS enriched in ACRG MSS/EMT;
- TCGA EBV enriched in ACRG MSS/TP53+;
- TCGA CIN enriched in ACRG MSS/TP53−;
- MSI present in both systems.

However:

- TCGA CIN was distributed across all ACRG subtypes;
- TCGA GS was distributed across all ACRG subtypes;
- GS and MSS/EMT differed in Lauren distribution;
- CDH1 mutation frequency differed markedly;
- RHOA alterations did not map in a one-to-one fashion;
- EBV-positive tumors represented only a subset of MSS/TP53+.

[S2]

Therefore:

> **TCGA and ACRG are biologically overlapping but non-equivalent frameworks.**

---

# 18. Why the Crosswalk Must Not Be Treated as a Translation Table

A dangerous simplification would be:

| TCGA | “Equivalent” ACRG |
|---|---|
| EBV | MSS/TP53+ |
| GS | MSS/EMT |
| CIN | MSS/TP53− |
| MSI | MSI |

This table is acceptable only as a **broad enrichment map**, never as a translation rule.

The evidence explicitly shows non-one-to-one distributions.

Therefore the correct wording is:

> “TCGA subtypes show enrichment within certain ACRG groups, but the frameworks are not interchangeable.”

---

# 19. Molecular Subtype vs Biomarker Evidence

The evidence supports the following hierarchy:

**Molecular classification**

= multi-feature biological grouping.

**Individual biomarker**

= specific measurable molecular feature.

Examples:

- MSI;
- HER2;
- PD-L1;
- CLDN18.2;
- TMB;
- FGFR2 alterations.

A molecular subtype may contain or correlate with individual biomarkers, but the presence of one biomarker does not automatically establish a complete subtype.

---

# 20. Molecular Subtype vs Histology Evidence

ACRG directly demonstrates associations between:

- MSI ↔ intestinal;
- MSS/EMT ↔ diffuse;
- MSS/EMT ↔ signet-ring morphology.

[S2]

This supports a complementary model:

> histology and molecular classification describe related but different dimensions of gastric cancer.

---

# 21. Molecular Subtype vs Stage

ACRG MSS/EMT was strongly associated with stage III/IV, whereas MSI was more often diagnosed at earlier stage. [S2]

This is evidence that molecular biology and disease extent can correlate.

It does not mean:

> subtype determines stage.

---

# 22. Clinical Claims Summary

## Established / strongly supported

- Gastric cancer is molecularly heterogeneous.
- TCGA and ACRG provide major molecular-subtyping frameworks.
- TCGA defines EBV/MSI/GS/CIN.
- ACRG defines MSI/MSS/EMT/MSS/TP53+/MSS/TP53−.
- Both frameworks have been validated in independent cohorts.
- Both demonstrate clinically meaningful subtype–outcome associations.
- ACRG MSS/EMT has particularly poor prognosis and high recurrence in the supplied cohorts.
- ACRG MSI has particularly favorable prognosis and low recurrence in the supplied cohorts.
- TCGA EBV and GS show the most favorable and unfavorable prognosis, respectively, in the Sohn validation cohorts.
- TCGA and ACRG overlap but are not interchangeable.

## Exploratory / retrospective

- TCGA CIN may show greater adjuvant chemotherapy benefit than other TCGA subtypes.
- GS may show relative chemotherapy resistance.

## Not established

- universal TCGA/ACRG routine testing;
- universal subtype-based treatment;
- individualized prognosis based on subtype alone;
- a unified TCGA–ACRG subtype translation table.

---

# 23. Evidence Consistency Review

## Internal consistency

**PASS**

The major findings are consistent across the supplied TCGA and ACRG studies.

## Cross-framework consistency

**PASS WITH QUALIFICATION**

The systems show biologically meaningful overlap but deliberately non-identical classification.

## Prognostic consistency

**PASS**

Both studies support clinically meaningful subtype-associated survival patterns, with different ordering details.

## Treatment-response consistency

**LIMITED**

The TCGA chemotherapy analysis is retrospective and hypothesis-generating.

No equivalent routine treatment-selection evidence is established for ACRG in the supplied materials.

## Current clinical implementation

**QUALIFIED**

Molecular classification is clinically relevant as a biological framework, but the supplied foundational papers do not establish universal routine TCGA/ACRG subtype testing.

---

# 24. Evidence Gaps

1. No single universally accepted molecular-subtype framework is established as the sole clinical standard.
2. TCGA and ACRG use different molecular inputs and classification logic.
3. Standardized routine assays for full subtype assignment are not established by these foundational papers.
4. Prospective evidence for subtype-guided treatment selection is limited.
5. Subtype prevalence varies between cohorts.
6. Longitudinal subtype stability/evolution is outside this package.
7. Individualized prognostic performance requires more than cohort-level subtype association.
8. Current guideline-based clinical utility must be anchored to contemporary biomarker-testing recommendations rather than inferred from older molecular-subtyping studies.

---

# 25. Future Update Triggers

Review PP-0188 when any of the following occurs:

- a major NCCN/ESMO/ASCO guideline formally adopts or materially changes molecular-subtype terminology;
- a prospective trial validates subtype-guided treatment selection;
- a standardized clinical assay for TCGA or ACRG assignment gains established clinical utility;
- a consensus molecular classification supersedes or formally integrates TCGA and ACRG;
- new high-quality prospective evidence changes subtype-specific prognostic interpretation;
- clinically relevant molecular subtype definitions are materially revised.

---

# 26. Out-of-Scope / Delegated Topics

| Topic | Delegation |
|---|---|
| EBV-associated gastric cancer and EBV testing | PP-0168 |
| HER2 testing | PP-0181 |
| MSI/MMR testing | PP-0182 |
| PD-L1 testing | PP-0183 |
| CLDN18.2 testing | PP-0184 |
| TMB | PP-0185 |
| FGFR2 testing | PP-0186 |
| NGS biomarker testing | PP-0187 |
| Genomic report interpretation | PP-0189 |
| Biomarker testing for targeted therapy | PP-0190 |
| Biomarker testing for immunotherapy | PP-0191 |
| Histopathologic classification | PP-0178 |
| Lauren classification | PP-0179 |
| Gastric cancer molecular classification concept | PP-0180 |
| Treatment algorithms | Relevant treatment PPs |

---

# 27. Source Traceability

## S0

**NCCN Clinical Practice Guidelines in Oncology: Gastric Cancer, Version 2.2026.**

Used as current clinical/guideline anchor.

## S1

**Sohn BH et al. Clin Cancer Res. 2017;23:4441–4449.**

Relevant source locations:

- pp. 2–4: TCGA molecular framework and prediction methodology.
- pp. 5–6: subtype-specific predictors and prognosis.
- pp. 7–9: chemotherapy association, TRS, discussion and limitations.
- pp. 15–20: subtype signatures, prediction tree, survival, chemotherapy and TRS figures.

## S2

**Cristescu R et al. Nat Med. 2015; doi:10.1038/nm.3850.**

Relevant source locations:

- Figure 1: ACRG classification tree and molecular signatures.
- Figure 2: survival associations and validation.
- Figure 3: molecular alteration landscape and TCGA–ACRG comparison.
- Table 2: recurrence patterns.
- Methods: validation cohorts and survival analyses.
- Comparison section: direct non-equivalence of ACRG and TCGA.

---

# 28. Boundary Verification

**Core = major molecular-subtyping frameworks of gastric cancer; TCGA and ACRG classification systems; subtype definitions; biological characteristics; key clinical/prognostic and recurrence associations; comparison and non-equivalence of TCGA and ACRG; relationship of molecular subtype to histology, stage, and individual biomarkers; research-versus-clinical implementation distinction.**

**Supporting = immune biology, genomic instability, selected gene examples, recurrence-pattern context, exploratory treatment-response evidence, molecular heterogeneity and precision-oncology context.**

**Explicitly Excluded = detailed histopathology/WHO/Lauren classification, individual biomarker assay methodology, NGS technical methodology, variant interpretation, genomic-report interpretation, detailed subtype prediction algorithms, universal TCGA/ACRG testing, individualized prognosis, subtype-specific treatment prescription, routine subtype-guided chemotherapy/immunotherapy, hereditary/germline classification, longitudinal molecular monitoring.**

**Delegated-to PP = PP-0168, PP-0181, PP-0182, PP-0183, PP-0184, PP-0185, PP-0186, PP-0187, PP-0189, PP-0190, PP-0191, and relevant treatment Population Packages.**

---

# 29. Evidence Package Decision

**DECISION: PASS**

The evidence base is sufficient to support a Gold patient-facing PP on major gastric-cancer molecular-subtyping frameworks.

The strongest defensible scope is:

> **TCGA + ACRG molecular subtypes, their biological/clinical characteristics, their overlap and non-equivalence, and their clinical meaning/limitations.**

The package must not transform retrospective subtype associations into routine treatment recommendations.

---

# 30. Final Evidence Status

**Evidence Package Status: PASS — GOLD — READY FOR INTEGRATION.**
