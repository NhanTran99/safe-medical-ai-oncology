# 03_PRIMARY_EVIDENCE_PACKAGE --- PP-0179 Lauren Classification

## Identity

-   **PP ID:** PP-0179
-   **Title:** Lauren Classification
-   **Evidence Package ID:** EP-PP-0179
-   **Version:** 1.0.0
-   **Status:** GOLD --- READY FOR INTEGRATION
-   **Last Updated:** 2026-08-09

## Clinical Question

**What is Lauren Classification, what do the intestinal, diffuse and
mixed categories mean, how is the classification established from
pathology, and how should it be interpreted alongside grade, stage,
molecular classification and biomarker information?**

## Educational Intent

This package provides the dedicated Lauren Classification layer of the
gastric cancer knowledge graph.

Its central architecture is:

**tissue acquisition → histopathology → Lauren Classification →
molecular/biomarker characterization → clinical integration**

The package intentionally does not replace broad histopathologic
characterization, WHO classification, staging, molecular classification
or biomarker testing.

## Scope

### Included

-   Definition and purpose of Lauren Classification.
-   Intestinal type.
-   Diffuse type.
-   Mixed type.
-   Morphologic concepts relevant to these categories.
-   Signet-ring/poorly cohesive context.
-   Tumor heterogeneity.
-   Specimen limitations.
-   Biopsy versus larger specimen implications.
-   Relationship with histopathology.
-   Relationship with grade and differentiation.
-   Relationship with TNM staging.
-   Relationship with WHO classification.
-   Relationship with molecular classification.
-   Selected biomarker context.
-   High-level clinical relevance.
-   Prognostic and treatment interpretation limits.

### Excluded

-   Detailed endoscopic diagnosis.
-   Biopsy technique.
-   Full histopathologic taxonomy.
-   Detailed WHO classification.
-   Grade/differentiation methodology.
-   Complete TNM staging.
-   Biomarker testing/scoring.
-   Molecular classification methodology.
-   NGS.
-   Genomic interpretation.
-   EBV laboratory testing.
-   Hereditary genetics.
-   Individualized prognosis.
-   Treatment algorithms.

## Primary Evidence Sources

### 1. NCCN Gastric Cancer Version 2.2026

The supplied NCCN guideline identifies gastric adenocarcinoma as the
dominant gastric cancer histology and describes classification by
anatomic location and histologic type, including diffuse and intestinal
types. It describes diffuse tumors as poorly differentiated/discohesive
with signet-ring or non-signet-ring morphology and intestinal tumors as
generally mass-forming with tubular/glandular architecture.
fileciteturn28file6

NCCN also states that pathologic review and biomarker testing contribute
to diagnosis, classification and molecular characterization, and that
intestinal/diffuse subclassification may have therapeutic implications.
fileciteturn28file9

The same guideline reports higher HER2 positivity in intestinal than
diffuse gastric adenocarcinoma, supporting a limited biomarker-context
discussion while preserving dedicated ownership of HER2 testing.
fileciteturn28file15

### 2. NCI Gastric Cancer / Stomach Cancer PDQ

NCI supports the intestinal/diffuse framework and the existence of mixed
intestinal/diffuse features. The source describes intestinal tumors as
tending toward tubular/glandular architecture and diffuse tumors as
lacking gland formation and infiltrating the gastric wall.

### 3. NCI Hereditary Diffuse Gastric Cancer PDQ

This source provides disease-specific context for diffuse gastric cancer
and signet-ring morphology, including the possibility that superficial
biopsies may miss isolated signet-ring cells. It is used only to support
the morphology/context layer, not hereditary-genetic decision making.
fileciteturn28file17

## Supporting Sources

-   ACS Stomach Cancer source materials.
-   ESMO--ASCO Global Curriculum 2023.
-   PP Registry.
-   CORE_WORKING_RULES v1.6.
-   FREEZE GOLD POPULATION PACKAGE SPECIFICATION v1.0.
-   Approved Discussion Batch and Gold artifact examples.

## Evidence Hierarchy

1.  **Level 1 --- Current gastric-cancer guideline:** NCCN Gastric
    Cancer v2.2026.
2.  **Level 2 --- Disease-specific authoritative sources:** NCI gastric
    cancer and HDGC PDQ materials.
3.  **Level 2 --- Oncology curriculum:** ESMO--ASCO 2023.
4.  **Level 3 --- Project Registry and governance:** architecture,
    ownership and boundaries.
5.  **Level 4 --- General background knowledge:** not used to expand
    claims beyond the supplied evidence base.

## Evidence Matrix

  --------------------------------------------------------------------------
  Clinical Claim       Supporting        Evidence Level    Ownership
                       Evidence                            
  -------------------- ----------------- ----------------- -----------------
  Gastric              NCCN Gastric      Direct guideline  Core
  adenocarcinomas are  Cancer v2.2026                      
  typically classified                                     
  by anatomic location                                     
  and histologic type,                                     
  including diffuse                                        
  and intestinal                                           
  types.                                                   

  Diffuse gastric      NCCN Gastric      Direct guideline  Core
  adenocarcinoma is    Cancer v2.2026                      
  characterized by                                         
  poorly                                                   
  differentiated and                                       
  discohesive cells                                        
  with signet-ring or                                      
  non-signet-ring                                          
  morphology and                                           
  diffuse gastric-wall                                     
  infiltration.                                            

  Intestinal gastric   NCCN Gastric      Direct guideline  Core
  adenocarcinoma tends Cancer v2.2026                      
  to form a mass with                                      
  tubular or glandular                                     
  architecture and                                         
  variable                                                 
  differentiation.                                         

  Gastric              NCI gastric       Direct disease    Core
  adenocarcinomas can  cancer PDQ        source            
  show mixed                                               
  intestinal and                                           
  diffuse features.                                        

  Lauren               Project           Governance /      Core
  Classification is a  Registry + source conceptual        
  histologic           architecture                        
  classification                                           
  framework rather                                         
  than a staging                                           
  system.                                                  

  Lauren type should   Project Registry  Locked boundary   Core
  not be used                                              
  independently to                                         
  determine prognosis                                      
  or treatment.                                            

  Histologic subtype   NCCN Gastric      Direct guideline  Core
  and molecular        Cancer v2.2026                      
  characteristics both                                     
  contribute to                                            
  gastric cancer                                           
  characterization.                                        

  Intestinal/diffuse   NCCN Gastric      Direct guideline  Supporting
  subclassification    Cancer v2.2026                      
  may have                                                 
  implications for                                         
  therapy because                                          
  biomarker                                                
  distributions differ                                     
  by subtype.                                              

  HER2 positivity is   NCCN Gastric      Direct guideline  Supporting
  reported more        Cancer v2.2026                      
  frequently in                                            
  intestinal than                                          
  diffuse gastric                                          
  adenocarcinoma.                                          

  Signet-ring          NCCN + NCI HDGC   Direct disease    Supporting
  morphology is        PDQ               sources           
  relevant to diffuse                                      
  gastric cancer and                                       
  hereditary diffuse                                       
  gastric cancer.                                          

  A very superficial   NCI HDGC PDQ      Direct disease    Supporting
  biopsy may miss                        source            
  isolated signet-ring                                     
  cells in diffuse                                         
  disease.                                                 

  A larger specimen    NCCN pathology    Direct guideline  Supporting
  may provide more     framework         / synthesis       
  information about                                        
  tumor morphology                                         
  than a limited                                           
  biopsy.                                                  

  Lauren               NCCN + Registry   Conceptual        Core
  classification,                        synthesis         
  tumor grade and                                          
  histologic                                               
  differentiation                                          
  answer different                                         
  pathology questions.                                     

  Lauren               Project Registry  Architecture      Core
  classification and                     source            
  WHO classification                                       
  are distinct                                             
  histologic                                               
  frameworks.                                              

  Lauren               NCCN + Registry   Guideline +       Core
  classification and                     architecture      
  molecular                                                
  classification are                                       
  complementary layers                                     
  of characterization.                                     
  --------------------------------------------------------------------------

## Evidence Notes

### Evidence Note 1 --- Intestinal and diffuse are the central Lauren patterns

NCCN directly describes intestinal and diffuse histologic types and
provides their characteristic morphology. This is the strongest clinical
anchor for the core package. fileciteturn28file6

### Evidence Note 2 --- Mixed features are clinically meaningful

NCI source material supports the existence of tumors with mixed
intestinal and diffuse features. This justifies keeping mixed as a
first-class patient-facing knowledge concept rather than treating it as
diagnostic uncertainty.

### Evidence Note 3 --- Histologic subtype is not stage

Lauren classification answers a morphology question. TNM staging answers
an anatomic extent question. The two labels can coexist and should not
be substituted for one another.

### Evidence Note 4 --- Histologic subtype is not grade

NCCN pathology principles treat histologic type and grade as distinct
elements. Lauren classification should therefore not absorb the separate
grade/differentiation packages.

### Evidence Note 5 --- Lauren is not WHO

The Registry maintains separate ownership for Lauren Classification and
WHO Classification. This package introduces the relationship but does
not reproduce the WHO taxonomy.

### Evidence Note 6 --- Lauren is not molecular classification

NCCN treats histologic subtype and molecular characteristics as
complementary dimensions. PP-0180 owns detailed molecular
classification. fileciteturn28file9

### Evidence Note 7 --- Biomarker associations do not replace testing

NCCN reports differences in HER2 positivity across histologic subtypes,
but this does not justify inferring HER2 status from Lauren type.
Dedicated HER2 testing remains necessary in the relevant clinical
setting. fileciteturn28file15

### Evidence Note 8 --- Diffuse/signet-ring morphology and hereditary disease

Diffuse and signet-ring morphology can be important in HDGC contexts,
but morphology alone does not establish a hereditary syndrome. NCI HDGC
PDQ is therefore used only as a supporting morphology/context source.
fileciteturn28file1

### Evidence Note 9 --- Specimen limitations

The available tissue affects the amount of morphology that can be
recognized. NCI HDGC PDQ specifically notes that a very superficial
biopsy may be negative for cancer cells in diffuse disease.
fileciteturn28file17

## Clinical Claims Summary

1.  Lauren Classification is a morphology-based framework for gastric
    adenocarcinoma.
2.  Intestinal, diffuse and mixed are the core categories for this PP.
3.  Intestinal type tends to show tubular/glandular architecture.
4.  Diffuse type is characterized by poorly cohesive/discohesive
    infiltrative cells and may include signet-ring morphology.
5.  Mixed tumors can show both intestinal and diffuse features.
6.  Specimen limitations and heterogeneity can affect classification.
7.  Lauren classification is distinct from histopathology as a whole,
    grade, differentiation and TNM stage.
8.  Lauren and WHO are different classification frameworks.
9.  Lauren and molecular classification are complementary.
10. Lauren subtype can provide context for biomarker distributions but
    cannot replace biomarker testing.
11. Lauren subtype should not independently determine prognosis or
    treatment.

## Evidence Consistency Review

### NCCN ↔ NCI

Consistent on:

-   intestinal/diffuse histologic patterns;
-   characteristic morphology;
-   diffuse/poorly cohesive and signet-ring context;
-   importance of pathological classification.

### NCCN ↔ Registry

Consistent on:

-   Lauren as a histologic classification layer;
-   separation from staging;
-   downstream relationship to molecular/biomarker characterization;
-   prohibition of independent treatment/prognostic use.

### NCI HDGC ↔ NCCN

Consistent on:

-   diffuse and signet-ring morphology;
-   infiltrative diffuse disease;
-   importance of adequate pathological examination.

### No material contradiction identified

No material contradiction in the supplied clinical sources requires a
change to the locked PP-0179 scope.

## Evidence Gaps

The supplied source set does not justify exhaustive treatment of:

-   every WHO histologic subtype;
-   detailed Lauren historical taxonomy beyond the patient-facing
    framework;
-   numerical microscopic thresholds for mixed classification;
-   comprehensive prognostic meta-analysis by Lauren subtype;
-   assay-specific biomarker methodology;
-   molecular classification algorithms;
-   individualized treatment recommendations.

These gaps are deliberately preserved.

## Future Update Triggers

Review PP-0179 if:

1.  NCCN changes its terminology or clinical role for intestinal/diffuse
    histologic subtype.
2.  A major WHO update materially changes the relationship between
    Lauren and contemporary histologic taxonomy.
3.  New consensus changes the definition or handling of mixed
    intestinal/diffuse morphology.
4.  Major pathology standards change the interpretation of Lauren
    classification from biopsy versus resection.
5.  New guideline evidence materially changes the relationship between
    Lauren subtype and biomarker testing.
6.  Project architecture changes ownership of WHO, grade, molecular or
    biomarker packages.

## Evidence Package Decision

**PASS --- evidence sufficient for the approved PP-0179 scope.**

The evidence supports a dedicated Lauren Classification package without
expanding into WHO methodology, molecular classification, biomarker
testing or treatment selection.

## Source Traceability

  --------------------------------------------------------------------------
  Source                  Role                    Main Use
  ----------------------- ----------------------- --------------------------
  NCCN Gastric Cancer     Primary guideline       Intestinal/diffuse
  v2.2026                                         histology, pathology
                                                  review, subtype relevance,
                                                  biomarker context

  NCI Gastric Cancer /    Primary disease source  Intestinal/diffuse/mixed
  Stomach Cancer PDQ                              morphology

  NCI HDGC PDQ            Disease-specific        Diffuse/signet-ring
                          supporting source       morphology and specimen
                                                  limitation context

  ACS Stomach Cancer      Supporting patient      Histology/pathology
                          source                  patient context

  ESMO--ASCO 2023         Supporting oncology     Pathology/classification
                          curriculum              framework

  PP Registry             Governance/ownership    Lauren scope and adjacent
                                                  package boundaries

  Gold Specification v1.0 Governance              Artifact structure and QA

  CORE_WORKING_RULES v1.6 Governance              Source-first, production
                                                  and boundary rules
  --------------------------------------------------------------------------

## Boundary Verification

**Boundary: Core = Lauren Classification as a morphology-based framework
for gastric adenocarcinoma, including its purpose and place in
pathology, intestinal, diffuse and mixed categories, the morphologic
concepts underlying these categories, signet-ring/poorly cohesive and
infiltrative morphology as relevant classification context, mixed
features and tumor heterogeneity, specimen-related limitations, and the
relationship of Lauren classification to histopathology, tumor grade,
histologic differentiation, WHO classification, TNM staging, molecular
classification and selected biomarker context; Supporting =
biopsy-versus-resection implications, linitis plastica as a diffuse-type
context, selected source-supported associations between Lauren subtype
and molecular/biomarker features, pathology review in difficult or
discordant cases, historical/conceptual context, and patient-facing
interpretation of Lauren terminology; Explicitly Excluded = detailed
endoscopic diagnosis, biopsy technique, general histopathologic
characterization already owned by PP-0178, exhaustive WHO taxonomy,
detailed WHO diagnostic criteria, tumor-grade methodology,
histologic-differentiation methodology, complete TNM staging, biomarker
testing/scoring, molecular-classification methodology, NGS methodology,
genomic interpretation, EBV testing methodology, hereditary/CDH1
genetics, individualized prognosis, and treatment-selection algorithms;
Delegated-to PP = PP-0178 Histopathologic Classification, PP-0037 WHO
Classification of Gastric Cancer, PP-0038 Tumor Grade, PP-0039
Histologic Differentiation, PP-0180 Gastric Cancer Molecular
Classification, PP-0181--PP-0187 Biomarker/NGS Testing, PP-0189 Genomic
Test Results / How to Read a Molecular Report, PP-0190--PP-0191
Biomarker-guided Treatment, PP-0168 EBV-associated Gastric Cancer + EBV
Testing, hereditary gastric-cancer/HDGC packages, and dedicated staging,
pathology-report, endoscopic and treatment packages.**

## Final Evidence Status

**PASS --- GOLD --- READY FOR INTEGRATION**
