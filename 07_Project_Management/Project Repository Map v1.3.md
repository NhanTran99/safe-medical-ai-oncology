# PROJECT REPOSITORY MAP — END OF PHASE 4

Version:
1.3

Repository State:
Phase 4 CLOSED

Last Updated:
2026-08-12

---

# PROJECT REPOSITORY MAP — END OF PHASE 3

```text
project/
│
├── 01_Foundation/
│
├── 02_Architecture/
│
├── 03_Clinical_Knowledge/
│
├── 04_Knowledge_Governance/
│
├── 05_Operations/
│
├── 06_Governance/
│
├── 07_Project_Management/
│
├── 08_Development/
│
├── 09_Evaluation/
│
├── sources/
│
├── working/
│
├── archive/
│
└── README.md
```

Annotation

01–07
Governed organizational / architectural documentation

08
Implementation / development

09
Evaluation and verification evidence

sources
Evidence source layer

working
Non-authoritative execution workspace

archive
Historical / superseded materials

---

# 01_Foundation/

**Vai trò:** những tài liệu nền tảng định nghĩa project là gì, phạm vi gì, nguyên tắc nào và documentation được tổ chức/govern thế nào.

```text
01_Foundation/
├── PROJECT_FOUNDATION.md
├── MISSION_AND_SCOPE.md
├── CORE_WORKING_RULES.md
├── NOVELTY.md
└── DOCUMENT_ARCHITECTURE.md
```

| Document                   | Mục đích                                                                                               |
| -------------------------- | ------------------------------------------------------------------------------------------------------ |
| `PROJECT_FOUNDATION.md`    | Nền tảng của toàn project: purpose, vision, scope, architecture/governance direction.                  |
| `MISSION_AND_SCOPE.md`     | Định nghĩa mission, mục tiêu và boundary của system.                                                   |
| `CORE_WORKING_RULES.md`    | Các nguyên tắc làm việc cốt lõi áp dụng xuyên project.                                                 |
| `NOVELTY.md`               | Ghi nhận novelty/contribution của project.                                                             |
| `DOCUMENT_ARCHITECTURE.md` | Quy định hệ thống documentation: document classes, authority, hierarchy, lifecycle, naming/versioning. |

**Thread mới cần đọc trước:** `PROJECT_FOUNDATION` + `MISSION_AND_SCOPE` + `CORE_WORKING_RULES` + `DOCUMENT_ARCHITECTURE`.

---

# 02_Architecture/

**Vai trò:** mô tả **system architecture**, không phải code implementation.

```text
02_Architecture/
│
├── system/
│   ├── SYSTEM_ARCHITECTURE.md
│   ├── CLINICAL_NAVIGATION_ENGINE.md
│   ├── MEDICAL_GOVERNANCE.md
│   └── SAFETY_FRAMEWORK.md
│
├── knowledge/
│   ├── RAG_ARCHITECTURE.md
│   ├── KNOWLEDGE_BASE.md
│   └── PROMPTING_STRATEGY.md
│
└── runtime/
    ├── EVIDENCE_PACKAGE_SPECIFICATION.md
    ├── RESPONSE_GENERATION_ARCHITECTURE.md
    ├── OUTPUT_VALIDATION_FRAMEWORK.md
    └── DELIVERY_POLICY.md
```

## `system/`

| Document                        | Mục đích                                                       |
| ------------------------------- | -------------------------------------------------------------- |
| `SYSTEM_ARCHITECTURE.md`        | Kiến trúc tổng thể của Safe Medical AI System.                 |
| `CLINICAL_NAVIGATION_ENGINE.md` | Cách system điều hướng clinical knowledge trước khi retrieval. |
| `MEDICAL_GOVERNANCE.md`         | Medical governance ở system level.                             |
| `SAFETY_FRAMEWORK.md`           | Safety architecture và safety boundaries.                      |

## `knowledge/`

| Document                | Mục đích                                                                       |
| ----------------------- | ------------------------------------------------------------------------------ |
| `RAG_ARCHITECTURE.md`   | Kiến trúc Retrieval-Augmented Generation.                                      |
| `KNOWLEDGE_BASE.md`     | Logical architecture của knowledge base và các knowledge layers.               |
| `PROMPTING_STRATEGY.md` | Prompt Builder, Prompt Contract, prompt layers và model-independent prompting. |

## `runtime/`

| Document                              | Mục đích                                                                       |
| ------------------------------------- | ------------------------------------------------------------------------------ |
| `EVIDENCE_PACKAGE_SPECIFICATION.md`   | Cấu trúc/interface của Evidence Package giữa evidence/retrieval và generation. |
| `RESPONSE_GENERATION_ARCHITECTURE.md` | Kiến trúc tạo response từ retrieved evidence/knowledge.                        |
| `OUTPUT_VALIDATION_FRAMEWORK.md`      | Validation trước khi output được release.                                      |
| `DELIVERY_POLICY.md`                  | Quy định về delivery/output ở system level.                                    |

**Thread Phase 4 cần đọc:** `SYSTEM_ARCHITECTURE`, `RAG_ARCHITECTURE`, `EVIDENCE_PACKAGE_SPECIFICATION`, `RESPONSE_GENERATION_ARCHITECTURE`.

---

# 03_Clinical_Knowledge/

Đây là **trung tâm của Phase 3**.

Nó chứa cả:

1. architecture/specification của clinical knowledge;
2. population strategy/framework;
3. actual Population Packages.

```text
03_Clinical_Knowledge/
│
├── architecture/
│   ├── KNOWLEDGE_INGESTION_WORKFLOW.md
│   ├── KNOWLEDGE_OBJECT_SPECIFICATION.md
│   ├── KNOWLEDGE_PASSPORT.md
│   ├── CLINICAL_KNOWLEDGE_DOMAINS.md
│   ├── KNOWLEDGE_RELATIONSHIP_MODEL.md
│   ├── CLINICAL_KNOWLEDGE_REPOSITORY_STRUCTURE.md
│   └── CLINICAL_KNOWLEDGE_OBJECT_TEMPLATE.md
│
└── population/
    ├── strategy/
    ├── framework/
    ├── registry/
    └── population_packages/
```

## `architecture/`

| Document                                     | Mục đích                                                       |
| -------------------------------------------- | -------------------------------------------------------------- |
| `KNOWLEDGE_INGESTION_WORKFLOW.md`            | Workflow đưa knowledge/evidence vào governed knowledge system. |
| `KNOWLEDGE_OBJECT_SPECIFICATION.md`          | Định nghĩa CKO: identity, granularity, structure, lifecycle.   |
| `KNOWLEDGE_PASSPORT.md`                      | Specification của Knowledge Passport.                          |
| `CLINICAL_KNOWLEDGE_DOMAINS.md`              | Taxonomy/domain structure của clinical knowledge.              |
| `KNOWLEDGE_RELATIONSHIP_MODEL.md`            | Các relationship được phép giữa CKOs/knowledge assets.         |
| `CLINICAL_KNOWLEDGE_REPOSITORY_STRUCTURE.md` | Repository hierarchy: Domain → Topic → Batch → PP → CKO/KP/EP. |
| `CLINICAL_KNOWLEDGE_OBJECT_TEMPLATE.md`      | Template chuẩn để tạo từng CKO.                                |

**Lưu ý:** `CLINICAL_KNOWLEDGE_OBJECT_TEMPLATE` để **thẳng trong `architecture/`**, không tạo `templates/` riêng.

---

## `population/strategy/`

| Document                                     | Mục đích                                                                        |
| -------------------------------------------- | ------------------------------------------------------------------------------- |
| `CLINICAL_KNOWLEDGE_POPULATION_STRATEGY.md`  | Strategy tổng thể để chuyển evidence thành retrieval-ready clinical knowledge.  |
| `KNOWLEDGE_POPULATION_PRIORITY_FRAMEWORK.md` | Quy định ưu tiên topic, Population Waves, batch selection và re-prioritization. |

---

## `population/framework/`

| Document                                      | Mục đích                                                                           |
| --------------------------------------------- | ---------------------------------------------------------------------------------- |
| `EVIDENCE_PACKAGE_POPULATION_GUIDE.md`        | Hướng dẫn xây dựng Primary Evidence Package trong PP workflow.                     |
| `KNOWLEDGE_PASSPORT_POPULATION_GUIDE.md`      | Hướng dẫn hoàn thiện Knowledge Passport trong population workflow.                 |
| `KNOWLEDGE_POPULATION_EXECUTION_FRAMEWORK.md` | Execution workflow từ approved evidence → CKO → KP → EP → validation → repository. |
| `KNOWLEDGE_ASSET_WORKFLOW_SOP.md`             | SOP thực thi workflow tạo knowledge assets.                                        |
| `POPULATION_PACKAGE_GOLD_SPECIFICATION.md`    | Gold specification của Population Package và 4-artifact production standard.       |
| `KNOWLEDGE_POPULATION_QUALITY_FRAMEWORK.md`   | QA layers, checklist, quality gates và traceability cho Population Package.        |
| `PP_DISCUSSION_FORMAT_EXAMPLE.md`             | Reference về format/depth của PP Discussion trước production.                      |

### Gold PP standard

Mỗi PP production-ready gồm **4 artifacts**:

```text
PP-XXXX/
├── 01_CKO.md
├── 02_KNOWLEDGE_PASSPORT.md
├── 03_PRIMARY_EVIDENCE_PACKAGE.md
└── 04_QA_REPORT.md
```

Đây là **knowledge product**, không phải execution log.

---

## `population/registry/`

Đây là **control/registry layer của Population**, không phải clinical knowledge content.

Hiện các Excel chính:

```text
Master_Population_Map.xlsx
Population_Registry.xlsx
01_Master_Registry.xlsx
02_Topic_Mapping.xlsx
03_PP_Mapping.xlsx
04_Coverage_Dashboard.xlsx
```

### Vai trò

* population master map;
* PP registry;
* topic mapping;
* PP mapping;
* coverage;
* audit/control của Phase 3.

---

## `population/population_packages/`

**Actual Phase 3 production output.**

```text
population_packages/
├── PP-0001/
├── PP-0002/
├── ...
└── PP-0239/
```

Mỗi folder PP chứa 4 Gold artifacts như trên.

**Đây là một trong những phần quan trọng nhất cần preserve khi chuyển thread/phase.**

---

# 04_Knowledge_Governance/

**Vai trò:** governance của knowledge assets/sources/lifecycle, khác với clinical knowledge architecture.

```text
04_Knowledge_Governance/
├── KNOWLEDGE_SOURCE_REGISTRY.md
├── KNOWLEDGE_SOURCE_APPROVAL_POLICY.md
├── KNOWLEDGE_UPDATE_POLICY.md
├── RETRIEVAL_POLICY.md
└── KNOWLEDGE_ASSET_REGISTRY_SPECIFICATION.md
```

| Document                                    | Mục đích                                                          |
| ------------------------------------------- | ----------------------------------------------------------------- |
| `KNOWLEDGE_SOURCE_REGISTRY.md`              | Specification/structure của source registry.                      |
| `KNOWLEDGE_SOURCE_APPROVAL_POLICY.md`       | Quy định source nào được approve trước ingestion.                 |
| `KNOWLEDGE_UPDATE_POLICY.md`                | Versioning, update, amendment, deprecation của knowledge/source.  |
| `RETRIEVAL_POLICY.md`                       | Governance/policy cho retrieval behavior và retrieval boundaries. |
| `KNOWLEDGE_ASSET_REGISTRY_SPECIFICATION.md` | Specification của registry quản lý governed knowledge assets.     |

### Phân biệt quan trọng

```text
04_Knowledge_Governance/
    = rules/specifications

sources/source_registry/
    = actual source metadata/records
```

---

# 05_Operations/

**Vai trò:** vận hành system sau khi architecture và knowledge đã tồn tại.

```text
05_Operations/
│
├── evaluation/
│   └── SYSTEM_EVALUATION_FRAMEWORK.md
│
├── monitoring/
│   ├── MONITORING_FRAMEWORK.md
│   └── OBSERVABILITY_FRAMEWORK.md
│
├── incident/
│   └── INCIDENT_MANAGEMENT_POLICY.md
│
├── release/
│   └── RELEASE_POLICY.md
│
└── quality/
    ├── CONTINUOUS_IMPROVEMENT_FRAMEWORK.md
    └── QUALITY_MANAGEMENT_FRAMEWORK.md
```

| Document                              | Mục đích                             |
| ------------------------------------- | ------------------------------------ |
| `SYSTEM_EVALUATION_FRAMEWORK.md`      | Framework đánh giá system.           |
| `MONITORING_FRAMEWORK.md`             | Monitoring sau deployment/operation. |
| `OBSERVABILITY_FRAMEWORK.md`          | Observability của system.            |
| `INCIDENT_MANAGEMENT_POLICY.md`       | Xử lý incident.                      |
| `RELEASE_POLICY.md`                   | Controlled release/change process.   |
| `CONTINUOUS_IMPROVEMENT_FRAMEWORK.md` | Continuous improvement cycle.        |
| `QUALITY_MANAGEMENT_FRAMEWORK.md`     | Operational quality management.      |

---

# 06_Governance/

**Vai trò:** governance ở organizational/executive/regulatory level.

```text
06_Governance/
│
├── executive/
│   ├── GOVERNANCE_DASHBOARD.md
│   ├── GOVERNANCE_METRICS_FRAMEWORK.md
│   └── EXECUTIVE_REPORTING.md
│
├── organizational/
│   ├── AUDIT_FRAMEWORK.md
│   ├── GOVERNANCE_MATURITY_MODEL.md
│   ├── ORGANIZATIONAL_GOVERNANCE.md
│   ├── RISK_MANAGEMENT_FRAMEWORK.md
│   └── DOCUMENTATION_GOVERNANCE_FRAMEWORK.md
│
└── regulatory/
    └── REGULATORY_READINESS_FRAMEWORK.md
```

## `executive/`

| Document                          | Mục đích                                    |
| --------------------------------- | ------------------------------------------- |
| `GOVERNANCE_DASHBOARD.md`         | Executive-level governance state/dashboard. |
| `GOVERNANCE_METRICS_FRAMEWORK.md` | Metrics dùng để đo governance.              |
| `EXECUTIVE_REPORTING.md`          | Executive reporting structure.              |

## `organizational/`

| Document                                | Mục đích                                    |
| --------------------------------------- | ------------------------------------------- |
| `AUDIT_FRAMEWORK.md`                    | Audit framework.                            |
| `GOVERNANCE_MATURITY_MODEL.md`          | Maturity model của governance.              |
| `ORGANIZATIONAL_GOVERNANCE.md`          | Organizational governance.                  |
| `RISK_MANAGEMENT_FRAMEWORK.md`          | Risk identification/management.             |
| `DOCUMENTATION_GOVERNANCE_FRAMEWORK.md` | Governance toàn bộ documentation lifecycle. |

## `regulatory/`

| Document                            | Mục đích                        |
| ----------------------------------- | ------------------------------- |
| `REGULATORY_READINESS_FRAMEWORK.md` | Regulatory-readiness framework. |

---

# 07_Project_Management/

Chỉ chứa **project planning/status**, không chứa architecture/specification.

```text
07_Project_Management/
├── PROJECT_ROADMAP.md
├── PROJECT_STATUS.md
├── LONG_TERM_ROADMAP.md
├── Closing note_Phase 2.txt
├── Closing note_Phase 3.txt
└── Closing note_Phase 4.txt
```

| Document               | Mục đích                              |
| ---------------------- | ------------------------------------- |
| `PROJECT_ROADMAP.md`   | Roadmap phát triển theo phases.       |
| `PROJECT_STATUS.md`    | Current authoritative project status. |
| `LONG_TERM_ROADMAP.md` | Direction sau các phase hiện tại.     |

### Phase 3 → Phase 4 handover

Đây là nơi thread mới nên kiểm tra đầu tiên để biết:

> **Project đang ở đâu và phase tiếp theo là gì?**

Phase Closing Notes

Closing note_Phase 2.txt
Historical Phase 2 closure record.

Closing note_Phase 3.txt
Historical Phase 3 closure record.

Closing note_Phase 4.txt
Current Phase 4 closure record documenting completion of Repository &
Integration Verification.

---

# 08_Development/

Hiện tại **chưa có implementation materials thực tế cần populate**.

```text
08_Development/
├── specifications/
└── implementation/
```

Trước đây có đề xuất:

```text
TECH_STACK.md
REPOSITORY_STRUCTURE.md
```

nhưng **hai file này không tồn tại trong inventory thực tế** → **không tạo**.

Khi Phase 4+ bắt đầu implementation, đây sẽ là nơi dành cho:

* technical specifications;
* code architecture;
* implementation components.

---

# 09_Evaluation/

Đây là nơi tôi muốn đặc biệt nhấn mạnh khi bạn bước từ **Phase 3 → Phase 4**.

```text
09_Evaluation/
└── validation/
    └── population_integration/
        ├── Layer3_Aggregate_Verification/
        │   ├── L3_Aggregate_Audit_Depth_Metrics_v3.csv
        │   ├── L3_Aggregate_Audit_Detail_v3.csv
        │   ├── L3_Aggregate_Audit_Exceptions_v3.csv
        │   ├── L3_Aggregate_Audit_Semantic_Evidence_v3.csv
        │   ├── L3_Aggregate_Audit_Summary_v3.txt
        │   └── Layer3_Aggregate_Verification_Record_v0.2.md
        │
        └── [other controlled integration evidence]
        └── POPULATION_PACKAGE_INTEGRATION_MANIFEST.xlsx
```
## Layer3_Aggregate_Verification/

Purpose:
Controlled aggregate verification evidence for the integrated Population
Package repository.

Status:
PASS

Superseded:
Layer3_Aggregate_Verification_Record_v0.1.md

The superseded v0.1 record is preserved under archive/ and is not an
active verification record.

## `population_integration/`

Dùng cho:

> **Layer 4 — Repository / Integration Verification**

Tức là kiểm tra:

```text
PP Gold Package
      ↓
Repository integration
      ↓
Registry linkage
      ↓
Relationship/dependency integrity
      ↓
Navigation/retrieval readiness
      ↓
Integration verification
```

**Không đặt PP Gold artifacts ở đây.**

PP vẫn nằm:

```text
03_Clinical_Knowledge/
└── population/
    └── population_packages/
```

`09_Evaluation/` chỉ lưu **evidence/results/records của verification**.

---

# sources/

Đây là **source material layer**, khác với knowledge product.

```text
sources/
├── core/
├── supporting/
└── source_registry/
```

## `core/`

Guidelines/materials **đã hoặc đang được dùng để tạo Core PP**:

```text
sources/core/
├── NCCN/
├── ESMO/
├── ASCO/
└── ...
```

## `supporting/`

Nguồn hiện **chưa sử dụng**, nhưng dự kiến dùng khi mở rộng project:

```text
sources/supporting/
├── NCCN/
├── ESMO/
├── ASCO/
└── ...
```

## `source_registry/`

Metadata/provenance của sources:

```text
Source ID
Organization
Title
Version/Year
URL
Access date
Evidence role
Used by PP(s)
```

### Public GitHub rule

Các PDF guideline của NCCN/ESMO/ASCO... **không mặc định đưa lên public GitHub**.

```text
sources/core/
sources/supporting/
```

→ local/private + `.gitignore`

Trong public repository chủ yếu giữ:

```text
sources/source_registry/
```

để đảm bảo provenance/traceability.

---

# working/

**Không phải production repository.**

Dùng cho:

* working spreadsheets;
* temporary audit files;
* intermediate calculations;
* drafts;
* files đang chỉnh sửa;
* documents chưa đạt trạng thái authoritative.

Ví dụ hiện tại:

```text
working/
└── Population_Registry_Working_Document.xlsx
```

Không nên coi working file là SSOT.

---

# archive/

Dùng cho **superseded/deprecated historical versions**, không phải nơi chứa file đang active.

Ví dụ:

```text
archive/
└── governance/
    └── CORE_WORKING_RULES_v1.0.md
    └── CORE_WORKING_RULES_v1.1.md
    ...
```

Trong active repository:

```text
CORE_WORKING_RULES.md
```

chỉ giữ **current active version**; version nằm trong document metadata/Git history.

archive/
├── 01_Foundation/
├── 02_Architecture/
├── 03_Clinical_Knowledge/
├── 04_Knowledge_Governance/
├── 07_Project_Management/
├── 09_Evaluation/
│   └── validation/
│       └── population_integration/
│           └── Layer3_Aggregate_Verification/
│               └── Layer3_Aggregate_Verification_Record_v0.1.md
└── phase_handover/

Archive Principle

Archive contains superseded or historical materials that remain necessary
for traceability but are no longer active repository authorities.

Example:

Layer3_Aggregate_Verification_Record_v0.1.md
→ superseded by v0.2
→ retained under archive/
→ not used as the current verification record.

---

# README.md

README ở root sẽ làm nhiệm vụ **public entry point**:

```text
What is the project?
        ↓
Why does it exist?
        ↓
Architecture
        ↓
Clinical Knowledge
        ↓
Population Packages
        ↓
Governance
        ↓
Phase / Roadmap
        ↓
How to navigate repository
```

**README chưa cần hoàn thiện ngay trong Phase 3.**

---

# TỔNG QUAN LOGIC CỦA TOÀN REPOSITORY

Đây là phần tôi nghĩ **quan trọng nhất để đưa cho các thread khác**:

```text
01_Foundation
        │
        ▼
02_Architecture
        │
        ▼
03_Clinical_Knowledge
        │
        ├── Knowledge Architecture
        │
        └── Population
              │
              ▼
        PP Production
              │
              ▼
        Population Packages
              │
              ▼
04_Knowledge_Governance
              │
              ▼
05_Operations / 06_Governance
              │
              ▼
09_Evaluation
              │
              ▼
Repository / Integration Verification
              │
              ▼
Phase 4
```

---

# 4 LOẠI MATERIALS PHẢI PHÂN BIỆT

Đây là quy tắc rất quan trọng cho các thread sau:

### ① Framework / Specification

```text
01–07
```

→ **How the system is designed/governed.**

---

### ② Source Materials

```text
sources/
```

→ **Evidence used to create knowledge.**

---

### ③ Knowledge Products

```text
03_Clinical_Knowledge/population/population_packages/
```

→ **What the project actually produced.**

---

### ④ Verification / Working Materials

```text
09_Evaluation/
working/
```

→ **Evidence that production/integration was performed correctly.**

---

# PHASE 3 → PHASE 4 HANDOVER

Phase 3 substantive production is complete and formally CLOSED.

Core Gastric Cancer Population Wave:

239 Population Packages
↓
4 canonical Gold artifacts / PP
↓
956 canonical Gold artifacts

Immutable Phase 3 Git Baseline:

a838a9423fc3d14c46f8cd176bafed3b691e65c0

Phase 3 Formal Closure:

LD-P4-001 — LOCKED

Phase 4 Verification Status Vocabulary:

LD-P4-002 — LOCKED

Phase 4 changes the primary objective from:

"Can we produce a governed Population Package?"

to:

"Can all governed Population Packages be deterministically resolved,
registered, integrated, traced, and verified within the Clinical Knowledge
Repository?"

Phase 4 therefore focuses on:

- Registry / Manifest Integration Verification
- Exact Repository Path Resolution
- Four-Artifact Resolution
- Governance Metadata Verification
- Repository / Commit Traceability
- Integration Evidence
- Retrieval-readiness verification

Phase 4 does not reopen Population Package scope or Gold production standards.

---

# PHASE 4 CLOSEOUT

Phase 4 — Repository & Integration Verification is formally CLOSED.

Verified Scope

PP-0001 → PP-0239

239 Population Packages

956 canonical Gold artifacts

Verification Layers

Layer 4A — Registry Integration — PASS
Layer 4B — Repository Resolution — PASS
Layer 4C — Governance Metadata — PASS
Layer 4D — Immutable Integration Evidence — PASS
Layer 3 Aggregate Verification — PASS

Phase 4 Closing Commit

70067d020420eb1792419bb7d7308da524f0031c

Post-integration Archive Correction

d4c2994e390d746c37276b7d29d0ba57ebae0d53

Current Repository State

Phase 3 — CLOSED
Phase 4 — CLOSED
Phase 5 — NEXT

Repository Closeout State

ACTIVE repository materials classified.
Superseded verification record archived.
Phase 4 closing documentation committed.
Repository is ready for controlled transition to Phase 5.

---
## Một nguyên tắc cuối cùng để dùng cho các thread sau

Khi một thread muốn **tạo/cập nhật một artifact**, trước tiên phải xác định nó thuộc:

> **Foundation / Architecture / Clinical Knowledge / Knowledge Governance / Operations / Governance / Project Management / Evaluation / Source / Working**

rồi mới quyết định nơi lưu.

**Không quyết định vị trí dựa trên folder hiện tại của file.**

Đó chính là lý do chúng ta đã phải di chuyển khá nhiều Markdown trong quá trình audit Phase 3. Đây nên được coi là **repository organization rule** cho các phase tiếp theo.

---

Amendment History

## Version 1.3

Updated following formal closure of Phase 4 — Repository & Integration
Verification.

Major updates include:

- Repository map advanced from End of Phase 3 to End of Phase 4.
- Phase 4 verification evidence incorporated into repository structure.
- Layer 3 Aggregate Verification Record v0.2 designated as active.
- Superseded v0.1 record mapped to archive.
- Phase 4 Closing Note incorporated into Project Management structure.
- Working versus controlled repository materials clarified.
- Phase closeout repository procedure documented.
- Current project transition updated to Phase 5 — Implementation.

No change to the fundamental repository architecture.