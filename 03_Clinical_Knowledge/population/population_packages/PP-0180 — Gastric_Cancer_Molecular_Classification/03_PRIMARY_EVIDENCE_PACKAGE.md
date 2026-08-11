# 03_PRIMARY_EVIDENCE_PACKAGE — PP-0180 Gastric Cancer Molecular Classification

## Identity

- **PP ID:** PP-0180
- **Title:** Gastric Cancer Molecular Classification
- **Evidence Package ID:** EP-PP-0180
- **Version:** 1.0.0
- **Status:** GOLD — READY FOR INTEGRATION
- **Last Updated:** 2026-08-09

## Clinical Question

**What is molecular classification of gastric cancer, why is it needed, what broad molecular framework is used, and how should molecular classification be interpreted alongside histology, biomarkers and molecular testing?**

## Educational Intent

PP-0180 provides the dedicated molecular-classification layer of the gastric cancer knowledge graph.

The intended hierarchy is:

**Histopathology**
→ **Lauren Classification**
→ **Molecular Classification**
→ **Individual Biomarker / Molecular Testing**
→ **Molecular Subtypes**
→ **Genomic Report Interpretation**
→ **Clinical/Treatment Relevance**

The package explains the framework without duplicating detailed subtype biology or individual testing methodologies.

## Scope

### Included

- Definition and rationale.
- Molecular heterogeneity.
- Genetic aberrations.
- Genome instability.
- MSI.
- Chromosomal instability.
- EBV-positive molecular category.
- TCGA framework.
- EBV / MSI / GS / CIN high-level groups.
- Molecular alterations.
- Classification versus biomarkers.
- Classification versus NGS.
- Assay scope.
- Specimen limitations.
- Somatic versus germline.
- Precision-oncology context.
- Clinical interpretation limits.

### Excluded

- Detailed Lauren/WHO classification.
- Detailed molecular subtype biology.
- Individual biomarker testing methods.
- NGS laboratory workflow.
- Variant interpretation.
- Genomic report interpretation.
- Germline testing/counseling.
- Individualized prognosis.
- Individualized treatment.
- ctDNA/MRD/resistance monitoring.

## Primary Evidence Sources

### 1. NCCN Gastric Cancer Version 2.2026

NCCN states that pathologic review and biomarker testing play important roles in the diagnosis, classification and molecular characterization of gastric cancer. It describes accumulation of genetic aberrations during gastric carcinogenesis, including changes involving growth factors/receptors, tumor suppressor genes, the cell cycle, and DNA repair/damage response. It further identifies genome instability, including chromosomal instability and MSI, as an important part of gastric tumor biology. fileciteturn31file13

The same NCCN guideline recommends universal MSI/MMR testing and universal PD-L1 testing in the supplied v2.2026 diagnostic pathway, with HER2 and CLDN18.2 testing in relevant advanced/metastatic settings and NGS considered. fileciteturn30file9

NCCN also cites the Cancer Genome Atlas Research Network's comprehensive molecular characterization of gastric adenocarcinoma as a foundational reference. fileciteturn31file15

### 2. ESMO-ASCO Recommendations for a Global Curriculum in Medical Oncology, 2023

ESMO-ASCO provides the molecular-pathology framework needed to explain:

- different genomic alteration types;
- appropriate molecular-test selection;
- assay scope and limitations;
- panel versus exome versus genome-wide sequencing;
- DNA/RNA/protein requirements;
- germline-testing considerations;
- interpretation of molecular pathology reports;
- molecular tumor-board context.

The curriculum explicitly identifies point mutations, rearrangements and copy-number alterations and emphasizes matching the test to the clinical question. fileciteturn30file7

### 3. NCI Genetics of Gastric Cancer PDQ

NCI provides the separate hereditary/germline framework and distinguishes inherited gastric-cancer susceptibility from tumor molecular characterization. fileciteturn29file5

## Supporting Sources

- ACS Stomach Cancer materials.
- NCI Gastric Cancer Treatment PDQ.
- NCI EBV/HDGC materials where relevant.
- PP Registry.
- CORE_WORKING_RULES v1.6.
- FREEZE GOLD POPULATION PACKAGE SPECIFICATION v1.0.
- Approved Discussion depth/format reference.
- Completed Gold package references.

## Evidence Hierarchy

1. **Level 1 — Current gastric-cancer guideline:** NCCN Gastric Cancer v2.2026.
2. **Level 2 — Molecular oncology curriculum:** ESMO-ASCO 2023.
3. **Level 2 — NCI disease/genetics sources:** gastric cancer and hereditary context.
4. **Level 3 — Project Registry/governance:** package ownership and boundaries.
5. **Level 4 — General background:** used only when consistent with and necessary to explain source-supported concepts.

## Evidence Matrix

| Clinical Claim | Supporting Source | Evidence Class | Ownership |
|---|---|---|---|
|Molecular classification is part of gastric-cancer diagnosis/classification and molecular characterization.|NCCN Gastric Cancer v2.2026|Established / guideline-supported|Core|
|Gastric carcinogenesis involves accumulation of genetic aberrations affecting growth factors/receptors, tumor suppressors, cell cycle and DNA repair.|NCCN Gastric Cancer v2.2026|Established / guideline-supported|Core|
|Genome instability includes chromosomal instability and MSI.|NCCN Gastric Cancer v2.2026|Established / guideline-supported|Core|
|TCGA provided comprehensive molecular characterization of gastric adenocarcinoma.|NCCN cites Cancer Genome Atlas Research Network|Established research framework|Core|
|The broad TCGA framework includes EBV-positive, MSI, genomically stable and chromosomal instability groups.|TCGA framework as used in project architecture; detailed subtype ownership delegated to PP-0188|Established research framework|Core|
|NCCN recommends universal MSI/MMR testing in newly diagnosed gastric cancer.|NCCN Gastric Cancer v2.2026|Established / guideline-supported|Supporting|
|NCCN recommends PD-L1 testing universally in newly diagnosed patients in the supplied v2.2026 guideline.|NCCN Gastric Cancer v2.2026|Established / guideline-supported|Supporting|
|NCCN recommends HER2 testing when advanced/metastatic disease is documented or suspected.|NCCN Gastric Cancer v2.2026|Established / guideline-supported|Supporting|
|NCCN recommends CLDN18.2 testing in relevant advanced/metastatic settings.|NCCN Gastric Cancer v2.2026|Established / guideline-supported|Supporting|
|NCCN states that CLDN18.2 positivity can be independent of established molecular subtypes such as dMMR and HER2 status.|NCCN Gastric Cancer v2.2025 discussion source|Established / guideline-supported|Supporting|
|ESMO-ASCO distinguishes point mutations, rearrangements and copy-number alterations and emphasizes matching tests to patient needs.|ESMO-ASCO 2023|Established|Core|
|ESMO-ASCO emphasizes assay scope and limitations, including single-analyte, targeted multi-analyte and genome-wide approaches.|ESMO-ASCO 2023|Established|Core|
|ESMO-ASCO distinguishes panel, exome and genome-wide sequencing within NGS.|ESMO-ASCO 2023|Established|Supporting|
|ESMO-ASCO emphasizes determining whether an assay requires DNA, RNA or protein and how this affects tissue requirements.|ESMO-ASCO 2023|Established|Supporting|
|ESMO-ASCO recognizes the role of multidisciplinary interpretation and molecular tumor boards.|ESMO-ASCO 2023|Established|Supporting|
|NCI separately defines hereditary gastric-cancer susceptibility and germline genetic testing.|NCI Genetics of Gastric Cancer PDQ|Established|Supporting|
|Molecular classification should not be treated as a standalone treatment or individual prognostic algorithm.|Project Registry / locked boundary|Governance / safety boundary|Core|

## Evidence Notes

### Evidence Note 1 — Molecular characterization is a distinct diagnostic layer

NCCN explicitly places molecular characterization alongside pathologic review and biomarker testing. This supports PP-0180 as a distinct package rather than a repetition of histopathology. fileciteturn31file13

### Evidence Note 2 — Genome instability is central to the framework

NCCN identifies chromosomal instability and MSI as forms of genome instability in gastric cancer. This supports their inclusion as core molecular concepts. fileciteturn31file13

### Evidence Note 3 — TCGA is foundational but not synonymous with routine clinical testing

NCCN cites the TCGA comprehensive molecular characterization study. The project architecture uses the TCGA four-group framework as an educational foundation but deliberately delegates detailed subtype biology to PP-0188. fileciteturn31file15

### Evidence Note 4 — Individual biomarker testing is downstream

The v2.2026 NCCN diagnostic pathway separates MSI/MMR, PD-L1, HER2, CLDN18.2 and NGS as specific testing decisions. This supports a parent-child architecture in which PP-0180 explains the framework and PP-0181–PP-0187 own the specific tests. fileciteturn30file9

### Evidence Note 5 — Biomarker does not equal molecular subtype

NCCN notes that CLDN18.2 positivity can be independent of established molecular subtypes such as dMMR and HER2 status. This provides direct support for teaching patients that a single biomarker is not equivalent to the entire molecular classification. fileciteturn31file0

### Evidence Note 6 — NGS is a technology

ESMO-ASCO explicitly distinguishes sequencing approaches and emphasizes assay scope, alteration types and tissue requirements. NGS therefore belongs as a conceptual technology within PP-0180 but not as the package's laboratory-methodology owner. fileciteturn30file7

### Evidence Note 7 — Somatic and germline are different questions

NCI addresses hereditary gastric-cancer susceptibility separately, while ESMO-ASCO emphasizes recognizing when germline testing and genetic counseling are required. PP-0180 therefore introduces the distinction but delegates hereditary assessment. fileciteturn30file7turn29file5

### Evidence Note 8 — Clinical relevance requires context

NCCN uses molecular biomarkers to inform treatment in defined settings, but these decisions are tied to disease setting and specific validated biomarkers. PP-0180 therefore teaches molecular characterization as clinical context, not as a standalone treatment algorithm. fileciteturn30file10turn31file12

## Evidence-Supported Clinical Use Model

### Use 1 — Molecular characterization

**What molecular features does this gastric cancer have?**

↓

### Use 2 — Classification

**How do these features fit within a broader molecular framework?**

↓

### Use 3 — Biomarker identification

**Is there a specific clinically relevant biomarker or alteration?**

↓

### Use 4 — Clinical integration

**How does the molecular information fit with histology, stage and patient context?**

↓

### Use 5 — Precision oncology

**Does the molecular finding have validated clinical relevance for this patient?**

This is a **conceptual clinical-use ladder**, not a universal treatment algorithm.

## Critical Boundary: PP-0179 vs PP-0180

| PP-0179 — Lauren Classification | PP-0180 — Molecular Classification |
|---|---|
| Morphology-based | Molecular-biology-based |
| Intestinal/diffuse/mixed | EBV/MSI/GS/CIN framework |
| What does the tumor look like? | What molecular features characterize the tumor? |
| Microscopic architecture | Molecular/genomic characteristics |
| Pathology classification | Molecular characterization |

The two layers are complementary.

## Critical Boundary: PP-0180 vs PP-0188

| PP-0180 | PP-0188 |
|---|---|
| What is molecular classification? | What are the molecular subtypes? |
| Why classify molecularly? | What characterizes each subtype? |
| Molecular heterogeneity | Detailed subtype biology |
| TCGA framework | Deep EBV/MSI/GS/CIN profiles |
| High-level four-group introduction | Subtype-specific clinical/molecular evidence |
| Classification vs biomarkers | Detailed subtype–biomarker relationships |

PP-0180 must introduce the framework without consuming PP-0188's detailed ownership.

## Critical Boundary: PP-0180 vs PP-0181–PP-0187

| PP-0180 | PP-0181–PP-0187 |
|---|---|
| Molecular classification framework | Individual molecular/biomarker testing |
| What molecular patterns exist? | How is a specific feature tested? |
| Relationship among molecular layers | Assay-specific methodology |
| High-level NGS concept | NGS testing package |
| Classification limitations | Test-specific limitations |

## Critical Boundary: PP-0180 vs PP-0189

PP-0180 explains **what molecular classification means**.

PP-0189 explains **how to read an actual genomic/molecular test report**.

PP-0180 must not teach variant-level interpretation.

## Evidence Consistency Review

### NCCN ↔ ESMO-ASCO

Consistent on:

- molecular pathology as a major component of modern oncology;
- multiple types of molecular/genomic alterations;
- assay-specific scope;
- need for clinical interpretation;
- molecular testing as a complement to pathology.

### NCCN ↔ NCI

Consistent on:

- molecular/genetic characterization as distinct from hereditary risk assessment;
- importance of specific molecular biomarkers;
- separate hereditary/germline pathway.

### Project Registry ↔ Clinical Sources

Consistent on:

- PP-0180 as molecular-classification owner;
- PP-0188 as detailed molecular-subtype owner;
- PP-0181–PP-0187 as individual testing owners;
- PP-0189 as genomic-report interpretation owner.

### No material contradiction identified

No material contradiction in the supplied sources requires changing the locked PP-0180 scope.

## Evidence Gaps

The supplied project source set does not justify:

- exhaustive molecular-subtype biology;
- a universal clinical algorithm assigning every patient a TCGA subtype;
- detailed molecular subtype prognostic estimates;
- assay-specific laboratory protocols;
- variant-level interpretation;
- germline testing algorithms;
- individualized molecular treatment recommendations;
- longitudinal molecular monitoring algorithms.

These gaps are intentionally preserved as package boundaries.

## Future Update Triggers

Review PP-0180 if:

1. NCCN changes the molecular characterization framework for gastric cancer.
2. A major molecular-classification consensus supersedes or substantially revises the TCGA framework.
3. WHO or another authoritative classification system materially changes the relationship between morphology and molecular classification.
4. Routine clinical practice adopts a validated molecular classification assay or subtype assignment workflow.
5. New evidence materially changes the clinical role of EBV, MSI, GS or CIN classification.
6. Project architecture changes ownership of PP-0188 or the downstream biomarker packages.

## Evidence Package Decision

**PASS — evidence sufficient for the approved PP-0180 scope.**

The supplied evidence supports a dedicated molecular-classification package with a high-level TCGA framework and clear separation from detailed molecular subtypes, individual biomarker testing, NGS methodology and treatment selection.

## Source Traceability

| Source | Role | Main Use |
|---|---|---|
| NCCN Gastric Cancer v2.2026 | Primary guideline | Molecular characterization, genome instability, biomarker testing, NGS, clinical relevance |
| NCCN Gastric Cancer v2.2025 | Supporting guideline discussion | Biomarker relationships and molecular-subtype context |
| ESMO-ASCO 2023 | Molecular oncology curriculum | Alteration types, assay scope, NGS, tissue requirements, interpretation |
| NCI Genetics of Gastric Cancer PDQ | Supporting disease/genetics source | Somatic vs germline boundary |
| NCI Gastric Cancer Treatment PDQ | Supporting disease source | Biomarker-linked treatment context |
| PP Registry | Governance/ownership | PP-0180 and adjacent package boundaries |
| CORE_WORKING_RULES v1.6 | Governance | Source-first and production rules |
| Gold Specification v1.0 | Governance | Artifact structure and QA |
| Discussion depth/format example | Reference | Discussion and artifact depth/style |

## Boundary Verification

**Boundary: Core = gastric cancer molecular classification as a molecular-biology layer of tumor characterization; molecular heterogeneity; rationale for molecular classification; relationship with histopathology and Lauren classification; genome instability; high-level TCGA framework and the four broad groups EBV-positive, MSI, genomically stable (GS), and chromosomal instability (CIN); conceptual genomic alteration types; relationship between molecular classification, biomarker testing, genomic testing and precision oncology; high-level clinical relevance; specimen/assay limitations; molecular heterogeneity and interpretation limits; Supporting = foundational DNA/gene/chromosome concepts, somatic-versus-germline distinction, high-level molecular-group/biomarker relationships, NGS as a conceptual technology, specimen adequacy, molecular tumor-board context, tumor evolution and patient-facing molecular terminology; Explicitly Excluded = detailed Lauren or WHO classification, detailed TCGA subtype biology, exhaustive molecular-subtype profiles, HER2/MSI/MMR/PD-L1/CLDN18.2/TMB/FGFR2 testing methodology, NGS laboratory methodology, variant interpretation, genomic-report interpretation, germline testing and genetic counseling, individualized prognosis, individualized treatment selection, treatment algorithms, ctDNA/MRD/resistance monitoring and recurrence-monitoring algorithms; Delegated-to PP = PP-0168 EBV-associated Gastric Cancer + EBV Testing, PP-0178 Histopathologic Classification, PP-0179 Lauren Classification, PP-0037 WHO Classification, PP-0181–PP-0187 HER2/MSI/MMR/PD-L1/CLDN18.2/TMB/FGFR2/NGS Testing, PP-0188 Molecular Subtypes of Gastric Cancer, PP-0189 Genomic Test Results / How to Read a Molecular Report, PP-0190–PP-0191 Biomarker Testing for Targeted Therapy/Immunotherapy, hereditary/germline packages, and downstream molecular monitoring and treatment packages.**

## Final Evidence Status

**PASS — GOLD — READY FOR INTEGRATION**
