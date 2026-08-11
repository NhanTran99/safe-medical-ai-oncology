# Primary Evidence Package

## Identity

| Field | Value |
|---|---|
| Evidence Package ID | EP-PP-0176 |
| PP ID | PP-0176 |
| Title | Endoscopic Diagnosis of Gastric Cancer |
| Version | 1.0.0 |
| Clinical Domain | Diagnosis |
| Status | Approved / Gold |

# Clinical Question

> **How is endoscopy used to identify, localize and characterize suspicious gastric neoplasia, and what are the limits of visual diagnosis before tissue-based confirmation?**

# Educational Intent

Explain diagnostic endoscopy as a specialized gastric-cancer diagnostic step while preserving the distinction between:

- screening;
- diagnostic endoscopy;
- surveillance;
- visual/anatomic assessment;
- tissue diagnosis;
- staging;
- treatment.

The package should help patients understand what an endoscopist is looking for, why findings are documented, why suspicious areas are sampled, and why a visual examination or initial biopsy may not answer every clinical question.

# Scope

## Included

- Diagnostic endoscopy.
- Gastric-cancer-specific lesion recognition.
- Conceptual morphology.
- Location, size and extent.
- EGJ relationship.
- Systematic examination and documentation.
- Suspicious versus confirmed diagnosis.
- Biopsy transition.
- Diagnostic limitations.
- Diffuse/microscopic disease.
- Endoscopy-pathology discordance.
- Selected EUS interface.
- Selected EMR/ESD interface.
- Downstream planning interface.

## Excluded

- General endoscopy preparation.
- Sedation/anesthesia.
- Post-procedure care.
- Complications.
- Detailed biopsy strategy.
- Histopathology.
- Lauren classification.
- Molecular/biomarker testing.
- Detailed EUS/imaging.
- Full staging.
- EMR/ESD technique.
- Therapeutic endoscopy.
- HDGC surveillance protocols.
- Individualized clinical decisions.

# Primary Evidence Sources

1. NCCN Gastric Cancer v2.2026, GAST-A.
2. NCI Hereditary Diffuse Gastric Cancer PDQ.
3. NCI Genetics of Gastric Cancer PDQ.
4. Vietnam Ministry of Health gastric-cancer diagnosis/treatment guideline.
5. ACS stomach-cancer materials supplied in the project.

# Supporting Sources

1. NCI gastric-cancer screening/diagnostic materials supplied in the project.
2. PP Registry.xlsx.
3. CORE_WORKING_RULES v1.6.
4. FREEZE GOLD POPULATION PACKAGE SPECIFICATION v1.0.
5. Approved PP Discussion depth and format example.
6. Approved Gold Population Package examples.

# Evidence Hierarchy

## Level 1 — Current Clinical Guideline

NCCN Gastric Cancer v2.2026 is the strongest direct source for the role of diagnostic endoscopy, location documentation, biopsy interface, EUS staging and selected EMR/ESD use.

## Level 2 — NCI PDQ

NCI HDGC and gastric-cancer genetics sources provide important evidence on limitations of endoscopic visibility, diffuse/microscopic disease and the relationship between endoscopic findings and biopsy.

## Level 3 — National Clinical Guidance

The Vietnam guideline supports the broader diagnostic architecture and the role of endoscopy/biopsy in definitive diagnosis.

## Level 4 — Patient-Facing Sources

ACS provides patient-oriented context for diagnostic endoscopy and the broader gastric-cancer diagnostic pathway.

## Level 5 — Governance / Registry

Project governance and Registry materials determine PP identity, boundaries, artifact structure and workflow.

# Evidence Matrix

| Clinical Claim | Supporting Evidence |
|---|---|
| Diagnostic endoscopy is an important component of gastric-cancer diagnosis. | NCCN Gastric Cancer v2.2026, GAST-A |
| Diagnostic endoscopy aims to determine the presence and location of neoplastic disease. | NCCN GAST-A |
| Suspicious gastric lesions should undergo tissue sampling. | NCCN GAST-A |
| Tumor location in the cardia, fundus, body, antrum and pylorus, and relationship to the EGJ for proximal tumors, should be recorded. | NCCN GAST-A |
| Ulcerated lesions require particular attention to obtaining adequate tissue. | NCCN GAST-A |
| EMR/ESD can provide a larger specimen for selected small lesions and may improve assessment of differentiation, LVI and depth of infiltration. | NCCN GAST-A |
| EUS contributes to initial clinical staging by assessing depth of invasion and regional nodes. | NCCN GAST-A |
| Diffuse gastric cancer/linitis plastica can infiltrate the stomach wall and may be difficult to diagnose with superficial biopsy. | NCI HDGC PDQ |
| Microscopic signet-ring-cell foci may be difficult to identify endoscopically in hereditary diffuse gastric cancer. | NCI HDGC PDQ |
| Intestinal metaplasia is not always visible endoscopically and may be identified through biopsy. | NCI Genetics of Gastric Cancer PDQ |
| A suspicious endoscopic appearance is not equivalent to a final tissue diagnosis. | NCCN GAST-A + supplied diagnostic guideline materials |
| Endoscopy does not by itself provide complete gastric-cancer staging. | NCCN GAST-A + gastric-cancer staging/work-up materials |

# Evidence Notes

## 1. Diagnostic endoscopy has two central diagnostic tasks

NCCN states that diagnostic and surveillance endoscopies are performed to determine the presence and location of neoplastic disease and to biopsy suspicious lesions. It therefore treats these as the two components of an adequate diagnostic endoscopic examination. fileciteturn21file16

For PP-0176, this becomes the central architecture:

**detect → localize → characterize → document → enable tissue evaluation.**

## 2. Location is not a trivial documentation detail

NCCN specifically identifies the cardia, fundus, body, antrum and pylorus and requires the relationship to the EGJ for proximal tumors to be recorded. The guideline explains that this supports treatment planning and follow-up examinations. fileciteturn21file16

PP-0176 therefore owns the endoscopic localization concept, while downstream packages own the clinical interpretation of location for treatment.

## 3. Suspicious appearance is not the same as tissue diagnosis

NCCN connects visual identification of suspicious lesions with biopsy rather than treating endoscopic appearance as definitive pathology. fileciteturn21file16

This distinction is essential for patient education and for maintaining the PP-0177/PP-0178 boundary.

## 4. Ulcerated lesions are an important sampling interface

NCCN specifically notes the need for adequate biopsy material, particularly in ulcerated lesions. fileciteturn21file16

PP-0176 therefore recognizes ulceration as an important endoscopic finding but delegates biopsy optimization to PP-0177.

## 5. Diffuse gastric cancer illustrates the limits of visual diagnosis

NCI describes diffuse gastric cancer/linitis plastica as diffuse infiltration of the stomach wall and notes that superficial biopsy may be negative for cancer cells. fileciteturn22file15

This directly supports the inclusion of diffuse/infiltrative disease as a diagnostic limitation in PP-0176.

## 6. Microscopic disease may not be visible

NCI's HDGC PDQ describes microscopic signet-ring-cell foci that can be difficult to identify endoscopically. fileciteturn22file6

This supports the patient-facing message that a visually normal or nonspecific mucosa does not have identical exclusionary meaning in every clinical context.

## 7. Intestinal metaplasia demonstrates the endoscopy–biopsy complement

NCI notes that intestinal metaplasia is not always visible during endoscopy and may be identified by random gastric biopsies. fileciteturn19file15

This is included only as a supporting illustration; PP-0166 owns the clinical topic of intestinal metaplasia.

## 8. EMR/ESD may provide additional diagnostic information

NCCN notes that EMR or ESD can be performed for selected small lesions to obtain a larger specimen and provide more information on differentiation, LVI and depth of infiltration. fileciteturn21file16

The procedures themselves are delegated to PP-0192–0194.

## 9. EUS is a staging extension, not the core visual-diagnosis package

NCCN describes EUS as important for initial clinical staging and for assessing depth of tumor invasion and abnormal lymph nodes. fileciteturn21file16

PP-0176 therefore includes EUS only as a transition point.

# Clinical Claims Summary

1. Diagnostic endoscopy is a core component of gastric-cancer diagnosis.
2. The endoscopic examination seeks to determine whether suspicious neoplastic disease is present and where it is located.
3. Suspicious lesions require appropriate tissue evaluation.
4. Endoscopy provides visual/anatomic information rather than definitive histologic classification.
5. Gastric cancer can appear in different morphologic patterns.
6. Diffuse/infiltrative and microscopic disease can be difficult to detect.
7. Location, size, extent and EGJ relationship are clinically important documentation elements.
8. Endoscopy and pathology are complementary rather than interchangeable.
9. A negative or nondiagnostic first biopsy may not always resolve strong endoscopic suspicion.
10. EUS and selected EMR/ESD can provide additional information in appropriate clinical contexts.
11. Endoscopy contributes to later staging and treatment planning but does not determine treatment independently.
12. There is no universal endoscopic algorithm that applies identically to every patient.

# Evidence Consistency Review

The supplied sources are consistent on the major architecture:

**clinical suspicion → diagnostic endoscopy → identify/localize suspicious lesion → biopsy/tissue evaluation → pathology → further staging/characterization.**

NCCN provides the most direct guideline-level description of the endoscopic diagnostic component. NCI materials add important limitations involving diffuse and microscopic disease. The Vietnam guideline supports the broader diagnostic role of endoscopy and biopsy.

The sources do not justify a universal technical enhanced-imaging protocol, universal repeat-endoscopy interval, or a single appearance-based rule for diagnosing cancer. Those claims are therefore excluded.

# Evidence Gaps

The supplied project sources do not establish:

- one universal enhanced-endoscopy protocol;
- one universal repeat-endoscopy interval after nondiagnostic biopsy;
- one universal lesion-size threshold for all endoscopic interventions;
- a visual appearance that independently confirms histologic cancer;
- one universal sequence for every patient;
- universal performance characteristics for every endoscopic technique.

# Out-of-Scope Topics / Delegation

| Topic | Delegated Ownership |
|---|---|
| Overall diagnostic work-up | PP-0175 |
| Screening endoscopy | PP-0171 |
| Hereditary diffuse gastric cancer surveillance | PP-0159 |
| Biopsy strategy | PP-0177 |
| Histopathologic classification | PP-0178 |
| Lauren classification | PP-0179 |
| Molecular classification | PP-0180 |
| Biomarker testing | PP-0181+ |
| EUS methodology/staging | Dedicated EUS/staging package |
| CT/PET/CT | Dedicated imaging packages |
| EMR/ESD | PP-0192–0194 |
| Therapeutic endoscopy | Treatment packages |

# Future Update Triggers

Review PP-0176 when:

- NCCN materially changes diagnostic endoscopy recommendations;
- new evidence changes recognition of subtle gastric neoplasia;
- enhanced endoscopic imaging becomes guideline-standardized;
- new evidence changes the approach to diffuse/infiltrative gastric cancer detection;
- biopsy/endoscopy discordance management is materially revised;
- endoscopic resection indications materially change;
- new diagnostic technologies materially change the endoscopic work-up.

# Source Traceability

Major clinical claims are traceable to the supplied NCCN GAST-A guideline section, NCI PDQ sources and the supplied national/patient-facing gastric-cancer diagnostic materials.

No unsupported universal technical protocol or individualized recommendation has been introduced.

# Boundary Verification

**Boundary: {boundary}**

# Evidence Package Decision

**PASS — evidence traceability complete; endoscopic diagnostic ownership preserved; biopsy, pathology, staging and treatment boundaries protected.**

# Final Evidence Status

**PASS — Evidence traceability complete.**
