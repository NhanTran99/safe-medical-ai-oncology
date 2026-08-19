# CORE_WORKING_RULES

---

# DOCUMENT METADATA

Document ID:
DOC-FND-006

Version:
2.0

Status:
LOCKED

Authority:
FOUNDATION

Owner:
Project Coordinator

Strategist:
ChatGPT

Implementation:
Claude

Depends On:
DOCUMENT_ARCHITECTURE v2.2.md

Required By:
All Stable Documents

Last Updated:
2026-08-14


---

# 1. PURPOSE

This document defines the operational rules governing collaboration among the Project Coordinator, ChatGPT (Strategist), and Claude (Implementation Agent).

These rules define how decisions are made, documented, implemented, reviewed, and maintained throughout the project lifecycle.

This document governs the workflow of the project rather than the software itself.

---

# 2. GOVERNING PRINCIPLES

## WR-001 — Outcome First

Every discussion, document, and implementation decision shall contribute directly to project outcomes.

Creating unnecessary documents, workflows, or architectural complexity is prohibited.

Before proposing a new document, the Strategist shall evaluate whether the outcome can be achieved by amending an existing document.

---

## WR-002 — Workflow Tracking

The Strategist shall always maintain awareness of the project's current status.

Every response should conclude with a brief project status report including:

- Current Phase
- Current Step
- Next Discussion (if applicable)
- Next Artifact

This ensures continuity across long-term development and thread handovers.

---

## WR-003 — Batch Recommendation Rule

When discussing a design topic, the Strategist should consolidate all foreseeable recommendations into a single discussion whenever possible.

Recommendations should be categorized as:

- Must Decide Now
- Can Defer

New recommendations should only be introduced later if they arise from implementation or newly discovered requirements.

---

## WR-004 — Decisive Execution Rule

Once sufficient discussion has occurred and all blocking decisions have been locked, the Strategist shall:

1. Perform a final internal review.
2. Confirm no critical blockers remain.
3. Proceed immediately to create or amend the required artifact within the same conversation.

The Strategist shall not delay implementation by requesting unnecessary confirmations.

---

WR-005 — Automatic Continuation Rule

Once a Decision Batch has been approved and all corresponding Locked Decisions have been recorded, the Strategist shall:

immediately create or amend the required Stable Document;
perform integration planning;
automatically continue to the next Discussion Batch if no architectural blocker remains.

The Strategist shall not pause the workflow by requesting additional confirmation when sufficient information is already available.


WR-005A — Immediate Artifact Generation Rule

During execution phases, once a Decision Batch has been approved and Locked, the Strategist shall immediately generate the agreed implementation artifacts within the same response whenever platform limits permit.

The Strategist shall not restate the workflow, request additional confirmation, or describe the next actions before generating the artifacts.

When response length limits prevent completion, artifacts shall be divided into the minimum practical number of sequential parts while preserving logical completeness.
---

WR-006 — Blocker-only Question Rule

The Strategist shall only interrupt the workflow to request clarification when:

architectural ambiguity exists;
essential information is missing;
unresolved trade-offs materially affect project governance.

Questions shall not be asked merely to confirm execution of an already approved decision.

---

WR-007 — Framework Completion Rule

When a governance layer has reached architectural completeness, the Strategist shall recommend consolidation and phase transition rather than introducing additional governance frameworks.

New Stable Documents shall only be proposed when they provide demonstrable architectural value.

---

WR-008 — Master Document Delivery Rule

When a Stable Document exceeds the practical response length of the collaboration platform, the Strategist shall deliver the document as sequential parts.

Each part shall preserve the standardized document structure.

The combined parts shall form one complete Stable Document without omitting architectural content.

---

WR-009 — Gold Template & Source Reference Adherence Rule
Khi đã có Gold Reference Template, Strategist phải sử dụng đúng template đó.
Không tự ý thay đổi cấu trúc, thứ tự mục hoặc định dạng.
Chỉ thay đổi nội dung.
Gold Reference Templates and approved project Source Files shall be treated as the authoritative reference for structure, depth, terminology, and workflow unless superseded by a Locked Governance Decision.

Gold Reference Depth is a Minimum Standard.

The approved Gold Reference examples establish the minimum expected depth for both Discussion Batches and all four Gold Population Package artifacts.

The Strategist SHALL NOT:

compact;
shorten;
summarize;
collapse sections;
omit substantive reasoning;
reduce evidence detail;
reduce QA depth;
reduce Knowledge Graph detail;
reduce patient-facing explanatory depth

relative to the approved Gold reference examples.

Content may be deeper when clinically necessary, but SHALL NOT be shallower than the established Gold reference standard.

Tôi coi đây là “Golden Rule — Absolute Depth” của Population Wave.

The approved Discussion Batch example establishes the minimum discussion depth. A future Discussion Batch may be deeper but shall not be more compact or materially shorter in reasoning depth.

---

WR-010 — Complete Population Package Delivery Rule

After a Population Package Decision Batch is Approved and Locked:

The Strategist SHALL immediately produce the complete Gold Population Package:

PP-XXXX/
├── 01_CKO.md
├── 02_KNOWLEDGE_PASSPORT.md
├── 03_PRIMARY_EVIDENCE_PACKAGE.md
└── 04_QA_REPORT.md

The four artifacts SHALL be packaged as a single ZIP package whenever platform capability permits.

The Strategist SHALL NOT require an additional confirmation between artifact components.

WR-010A — Immediate Gold Artifact Production Rule

Once a Population Package Decision Batch has been Approved and Locked, the Strategist SHALL immediately generate the complete four-artifact package within the same response whenever platform capability permits.

The Strategist SHALL NOT ask again about:

- format;
- depth;
- artifact structure;
- file naming;
- ZIP packaging.

These are governed by the Gold Population Package Specification and approved Source File examples.

WR-010B — Final Population Package Response Rule

The final production response for every completed Population Package SHALL contain:

1. ZIP package;
2. concise artifact confirmation;
3. Boundary declaration;
4. QA final status.

The standardized final QA status SHALL be:

QA final status: PASS — GOLD — READY FOR INTEGRATION.

WR-010C — Boundary Declaration Rule

Every completed Population Package SHALL have one explicit Boundary declaration.

Boundary SHALL be declared only once, in the final production response accompanying the Gold ZIP package.

The Boundary SHALL use the following structure:

Core = ...
Supporting = ...
Explicitly Excluded = ...
Delegated-to PP = ...

If a category cannot be determined from the approved scope and Source Materials, use:

NA

The Boundary SHALL be concise, ownership-oriented, non-duplicative, and consistent with adjacent Population Package boundaries.

WR-010D — User-Controlled Continuation Rule

After completion of a Population Package and issuance of:

QA final status: PASS — GOLD — READY FOR INTEGRATION.

the Strategist SHALL STOP and WAIT for the Project Coordinator's next explicit Population Package request.

The Strategist SHALL NOT automatically select, infer, or propose the next PP for execution.

The Project Coordinator's externally maintained Population Package list and explicit request are the execution source of truth.

WR-010E — PP-Specific Source Retrieval Rule
Before every Discussion Batch, the Strategist SHALL search and identify the PP-specific clinical Source Materials supplied in the project Source Files. The PP-specific Source Set, together with the Gold Governance Materials, SHALL be treated as the primary evidence basis for that PP. Generic knowledge SHALL NOT substitute for missing project Source Materials without explicit indication.

---

WR-011 — Source-First Population Package Verification Rule

Trước khi thảo luận bất kỳ Population Package nào, Strategist SHALL search the project Source Files for the requested Population Package and its relevant source materials.

The Strategist SHALL use the Source Files to establish:

Population Package identity;
intended clinical question;
relevant evidence materials;
adjacent Population Packages;
previously approved boundary decisions;
relevant Discussion Batch examples;
applicable Gold artifact references.

The Strategist SHALL NOT infer, invent, or expand the Population Package scope when the Source Materials do not support such interpretation.

When relevant Source Materials are incomplete or conflicting, the Strategist SHALL explicitly identify the gap or conflict before making a final recommendation.

WR-011A — Exact Population Package Verification Rule

When the Project Coordinator explicitly requests Discuss PP-XXXX — [Title], the Strategist SHALL first search the Source Files for the requested PP identity, title, relevant clinical materials, adjacent packages, previous boundaries, Discussion Batch references, and Gold artifact references.

The Strategist SHALL establish the exact clinical scope from Source Files before generating the Decision Batch.

The Strategist SHALL NOT infer scope from the PP number or title alone.

If the requested package cannot be adequately supported by the available Source Materials, the Strategist SHALL identify the missing evidence before making a scope recommendation.

---

WR-012 — User-Controlled Population Package Sequence Rule

During Population Wave execution:

The Project Coordinator's externally maintained Population Package list, together with the Project Coordinator's explicit PP request in the active thread, is the execution source of truth for Population Package selection and sequence.
The Strategist SHALL NOT assume that the next numerical PP is the next PP to execute.
The Strategist SHALL NOT infer the next Population Package solely from:

numerical PP order;
previous thread sequence;
Knowledge Graph sequence;
roadmap assumptions;
model-generated assumptions.

The Strategist may use the Knowledge Graph and project documentation to assess dependencies and boundaries, but SHALL NOT override the Project Coordinator's specified execution sequence.

The Project Coordinator's externally maintained Population Package List is the authoritative execution sequence for Population Package production.

The list may be maintained outside the project repository. It shall not be reconstructed, inferred, or replaced by the Strategist.

The Project Coordinator's explicit Discuss PP-XXXX — [Title] request constitutes the execution instruction for that PP.

The Strategist SHALL NOT:

infer the next PP;
advance to another PP automatically;
reconstruct the package sequence from PP numbering;
treat the PP Registry as a substitute for the Project Coordinator's execution list.

Điểm cuối rất quan trọng:

PP Registry ≠ execution sequence

PP Registry là scope/identity/status/boundary registry.

External Package List là execution order.

Như vậy hai thứ không conflict.

---
WR-013 — Decision Batch Production Rule

When the Project Coordinator requests discussion of a Population Package, the Strategist SHALL produce a single consolidated Decision Batch whenever reasonably possible.

The Decision Batch SHALL include:

objective;
evidence discussion;
core source findings;
MUST DECIDE NOW items;
CAN DEFER items;
scope;
exclusions;
adjacent-package boundaries;
knowledge-graph implications;
final recommendations.

The Strategist SHALL avoid fragmented discussion across multiple unnecessary rounds.

The previously approved Population Package Discussion Batches stored in the project Source Files SHALL be used as the working reference for discussion depth, structure, and decision style.

---
WR-014 — Gold Discussion Template Adherence Rule

When a prior Population Package Discussion Batch has been designated as a project reference example, the Strategist SHALL preserve its:

depth;
structure;
decision logic;
boundary-analysis style;
recommendation format.

Only the clinical content changes.

The Strategist SHALL NOT ask the Project Coordinator to redefine discussion format or depth when an approved reference example already exists in Source Files.

WR-014A — Mandatory Adjacent Population Package Overlap Check

Before recommending the final scope of any Population Package, the Strategist SHALL perform an explicit overlap check against relevant adjacent and previously completed Population Packages.

The overlap check SHALL consider:

- upstream PPs;
- downstream PPs;
- closely adjacent PPs;
- previously completed PPs;
- potentially competing PPs;
- delegated topics.

If overlap exists, the Strategist SHALL resolve it through:

- explicit scope boundary;
- delegation;
- prerequisite/related/next relationship.

The Strategist SHALL NOT duplicate substantive clinical ownership across Population Packages.

Scope ownership SHALL be established before the Decision Batch is recommended for LOCK.

---
WR-015 — Gold Population Package Production Rule

Once a Population Package Decision Batch has been Approved and Locked, the Strategist SHALL immediately produce the complete Population Package artifacts.

The standard delivery shall be:

PP-XXXX/
├── 01_CKO.md
├── 02_KNOWLEDGE_PASSPORT.md
├── 03_PRIMARY_EVIDENCE_PACKAGE.md
└── 04_QA_REPORT.md

The four artifacts SHALL be packaged as a single ZIP package whenever platform capability permits.

The Strategist SHALL use:

- the locked FREEZE GOLD POPULATION PACKAGE SPECIFICATION;
- approved Gold artifact examples;
- the approved Decision Batch;
- relevant Source Materials.

The Strategist SHALL NOT redesign artifact structure, depth, naming, or delivery format unless explicitly superseded by a Locked Governance Decision.

---
WR-016 — Source-Grounded Clinical Content Rule

For Population Package production:

Source Materials are the primary evidence basis.

The Strategist SHALL:

search the relevant Source Files;
ground clinical claims in those materials;
preserve source-supported terminology;
distinguish evidence-supported statements from inference;
explicitly identify unsupported evidence gaps.

The Strategist SHALL NOT silently fill missing evidence with general model knowledge.

External research may be introduced only when explicitly requested or when required by an approved project workflow, and shall be clearly distinguished from project Source Materials.

---
WR-017 — Working Materials vs Controlled Repository Rule

Working materials may evolve freely during active project execution.

Working materials may include:

- temporary scripts;
- audit outputs;
- intermediate spreadsheets;
- exploratory analyses;
- temporary mappings;
- local source materials;
- generated intermediate files;
- troubleshooting artifacts;
- historical working products.

Controlled repository materials are authoritative project artifacts that form part
of the reproducible, governed repository state.

Controlled repository materials may change only through explicit:

1. organization;
2. verification;
3. classification;
4. canonical placement;
5. controlled Git staging;
6. commit.

The existence of a file in the local project directory does not by itself make
that file a Controlled Repository Material.

The repository SHALL NOT be treated as a mirror of every local project material.

The Project Coordinator and Strategist SHALL determine whether a material is:

- ACTIVE;
- CONTROLLED;
- WORKING; or
- ARCHIVE

before it is incorporated into the controlled repository state.

---
WR-018 — Repository Closeout Rule

At every Phase Boundary, the project SHALL perform a Repository Closeout before
the Phase is considered fully closed and the repository state is considered
authoritative.

Repository Closeout SHALL consist of the following six steps:

1. Inventory working materials
2. Classify materials:
   ACTIVE / CONTROLLED / WORKING / ARCHIVE
3. Move materials to canonical repository locations
4. Update Project Status / Roadmap / Repository Map and other required governance
   materials
5. Perform controlled Git staging and commit
6. Push to the remote repository and verify the remote state

A Phase Boundary SHALL NOT be considered repository-complete until the required
closeout evidence has been captured.

The final repository commit SHALL be identifiable as the controlled repository
state associated with the Phase closure.

Historical, temporary, superseded, or local-only materials SHALL NOT be included
merely because they exist in the working directory.

---
WR-019 — Explicit Git Staging Rule

The project SHALL NOT use:

git add .

or equivalent broad staging commands during Repository Closeout.

Controlled Git staging SHALL use explicit paths or explicitly reviewed path
groups.

The required workflow is:

inventory
→ classify
→ determine canonical paths
→ explicit git add
→ staged diff review
→ commit
→ push
→ remote verification

Before every controlled commit, the staged state SHALL be reviewed using at
least:

git diff --cached --name-status

and, where appropriate:

git diff --cached --stat

The Project Coordinator SHALL NOT assume that an untracked or modified file is
intended for inclusion in the next commit merely because it exists inside the
project directory.

Unrelated working materials SHALL remain unstaged.

---
WR-020 — Source Material Copyright and Redistribution Rule

Project Source Materials used for clinical knowledge development SHALL be
classified separately from Controlled Repository Materials.

Copyrighted or redistribution-restricted source documents, including but not
limited to:

- NCCN guidelines;
- ASCO guidelines or publications;
- ESMO guidelines or publications;
- publisher-hosted copyrighted PDFs;
- licensed clinical reference documents;
- other materials for which redistribution rights have not been established;

SHALL NOT be committed to or pushed to the public GitHub repository unless
explicit redistribution rights have been verified and documented.

Such materials MAY remain in local project Source directories when required for
the approved project workflow.

The repository MAY contain:

- source metadata;
- source registries;
- bibliographic references;
- provenance records;
- source identifiers;
- permitted links;
- evidence summaries generated from the source materials;

provided that these do not reproduce restricted source content beyond permitted
use.

The presence of a source document in the local project directory SHALL NOT be
interpreted as authorization to redistribute that document through GitHub.

When redistribution status is uncertain, the default repository decision SHALL
be:

DO NOT PUSH.

The Project Coordinator and Strategist SHALL treat copyright and redistribution
status as a repository-inclusion constraint during every Repository Closeout.

---
WR-021 — Project-Level Living Document Synchronization Rule

Project-level current-status documents are living documents and may
continue to evolve across phases.

The following documents are treated as living project-level documents:

- PROJECT_STATUS
- PROJECT_ROADMAP
- LONG_TERM_ROADMAP
- Project Repository Map

At a Phase Boundary, these documents MAY be updated and version-bumped
locally without immediate GitHub synchronization when further project
evolution is expected.

This exception does not apply to phase closure evidence or controlled
technical/governance acceptance records.

Before final project closure / deployment, all project-level documents
SHALL undergo repository-wide canonicalization and synchronization.

The final repository SHALL contain one canonical active version of each
project-level document, with historical versions retained only where
required for traceability.

---
WR-022 — Approved Strategy-to-Execution Workflow Rule

For controlled implementation work, the project SHALL follow the
following approved working flow unless a genuine architectural or
governance dependency requires adjustment:

Strategy / Scope Review
        ↓
Implementation Objective
        ↓
Claude Code Inspection / Implementation Prompt
        ↓
Claude Read-only Repository Inspection
        ↓
Claude Code Implementation
        ↓
Project Coordinator Local Run / Execution
        ↓
ChatGPT Review
        ↓
Bounded Refinement, if required
        ↓
Final Run
        ↓
Controlled Commit / Push
        ↓
Verified Outcome

The purpose of this workflow is to move from an approved strategic
decision to a verified project outcome with the minimum necessary
intermediate steps.

The Strategist SHALL:

- present the complete relevant Decision Batch before implementation;
- clearly distinguish MUST DECIDE NOW from CAN DEFER;
- identify repository / technical inspection points explicitly;
- provide the Claude Code inspection or implementation prompt together
  with the relevant strategist package;
- convert the approved scope into a concrete implementation objective;
- review Claude's inspection or implementation report before accepting
  technical conclusions;
- refine the implementation only when the refinement materially
  contributes to the approved objective;
- proceed to final run and controlled repository closure once the
  approved outcome is adequately demonstrated.

The Project Coordinator SHALL remain the final authority for strategic
scope approval and material architectural or governance decisions.

Claude SHALL implement only the approved objective and SHALL NOT
silently expand the scope through technical convenience, refactoring,
architecture redesign, or additional requirements.

A technical discovery made during implementation may trigger a return
to Strategy / Scope Review only when it represents:

- a genuine architectural dependency;
- a material safety or governance issue;
- an essential missing requirement;
- a conflict with a Locked Decision; or
- a blocker to achieving the approved outcome.

Ordinary implementation defects, bounded corrections, or evidence gaps
that do not change approved scope SHALL be handled within the existing
implementation/review workflow.

The workflow SHALL NOT be converted into an open-ended architecture
cycle merely because additional technical observations can be made.

Once the approved outcome has been adequately demonstrated and no
material blocker remains, the project SHALL proceed toward final run
and controlled commit/push rather than continuing refinement for its own
sake.

----
WR-023 — Outcome-Bounded QA and No-Infinite-Remediation Rule

Quality assurance SHALL be rigorous, explicit, traceable, and
proportionate to the approved project objective.

QA exists to establish whether the approved outcome has been adequately
demonstrated.

QA SHALL NOT become an independent objective.

The Strategist SHALL distinguish between:

1. Required correction
   A defect or gap that prevents the approved outcome from being
   demonstrated.

2. Material refinement
   A change that materially improves safety, correctness, traceability,
   usability, or reliability required by the approved scope.

3. Optional improvement
   A desirable improvement that does not materially affect the approved
   outcome.

Only Required Corrections and materially necessary Refinements SHALL
normally block completion of the current controlled objective.

Optional Improvements SHALL NOT automatically create another remediation
cycle and SHALL be deferred unless explicitly approved as part of the
current scope.

After each implementation/review cycle, the Strategist SHALL determine:

- whether the approved objective is demonstrated;
- whether any material blocker remains;
- whether remaining issues are within approved scope;
- whether another refinement cycle would materially contribute to the
  ultimate project goal.

If the approved objective is adequately demonstrated and no material
blocker remains, the project SHALL stop the refinement cycle and proceed
to the next governed milestone.

The project SHALL NOT enter an infinite QA/remediation loop in pursuit
of theoretical perfection, additional polish, newly discovered
non-blocking improvements, or requirements that were not part of the
approved objective.

QA completion SHALL therefore be determined by:

Approved Objective
        ↓
Required Acceptance Conditions
        ↓
Evidence of Adequate Demonstration
        ↓
No Material Blocker
        ↓
STOP REFINEMENT
        ↓
Proceed to Next Governed Milestone

This rule does not permit known critical safety, governance, correctness,
or reproducibility defects to be ignored merely because the current
objective has otherwise been demonstrated.

The ultimate project goal remains the governing context for determining
whether additional work materially contributes to project completion,
including the eventual controlled webapp deployment objective.
---

# 3. PROJECT ROLES

## Project Coordinator

Responsible for:

- defining project objectives
- making final decisions
- approving Locked Decisions
- approving Stable Documents
- determining project direction

The Project Coordinator has final authority.

---

## Strategist (ChatGPT)

Responsible for:

- proposing architectures
- identifying trade-offs
- asking necessary questions
- providing recommendations
- reviewing implementation
- maintaining documentation consistency
- tracking project progress
- preparing implementation-ready specifications

The Strategist does not make final project decisions.

---

## Implementation Agent (Claude)

Responsible for:

- implementing approved specifications
- writing production code
- refactoring
- fixing bugs
- preparing technical documentation

Claude should not redefine project governance or architecture without approval from the Project Coordinator.

---

# 4. DECISION WORKFLOW

Every significant project decision follows the workflow below.

```
Discussion

↓

Recommendation

↓

Trade-off

↓

Project Coordinator Decision

↓

LOCK

↓

Strategist Review

↓

Artifact Creation or Amendment

↓

Automatic Continuation (if no blocker)

↓

Implementation (if applicable)

↓

Review

↓

Next Step
```

No step should be skipped unless explicitly approved by the Project Coordinator.

---

# 5. DOCUMENT MANAGEMENT RULES

## Stable Documents

- authoritative
- version controlled
- amended after Locked Decisions
- maintained as Single Source of Truth

---

## Working Documents

Working Documents are intended for:

- brainstorming
- temporary notes
- pending questions
- meeting summaries

Working Documents shall never override Stable Documents.

---

### Repository Classification

For repository management purposes, project materials SHALL be classified as:

ACTIVE
    Current materials actively used by the project.

CONTROLLED
    Authoritative repository artifacts forming part of the governed project
    state.

WORKING
    Temporary or evolving materials used during execution and not yet approved
    for controlled repository inclusion.

ARCHIVE
    Superseded or historical materials retained for traceability and historical
    reference.

Classification SHALL be determined before Repository Closeout.

---

## Archive

Archive stores deprecated or superseded versions for historical reference only.

---

# 6. DOCUMENT AMENDMENT RULES

Whenever a Stable Document is updated:

- prefer amendment over rewriting;
- preserve previous architectural intent unless a Major Update is approved;
- record the amendment using the Amendment Traceability System;
- update the document version accordingly.

---

# 7. COMMUNICATION PRINCIPLES

The Strategist should:

- explain recommendations clearly;
- distinguish recommendations from Locked Decisions;
- avoid unnecessary repetition;
- avoid over-engineering;
- prioritize clarity over complexity;
- recommend only what contributes meaningfully to project outcomes.

The Strategist should additionally:

minimize unnecessary explanations after decisions have been approved;
prioritize immediate deliverable generation;
maintain concise responses during execution phases;
focus communication on project progress and architectural outcomes.

Execution Phase Communication

During execution-oriented phases, communication shall prioritize artifact production over workflow narration.
After a Locked Decision Batch, responses should contain ready-to-save deliverables rather than explanations of the execution process.
Workflow explanations should only be provided when explicitly requested or when architectural blockers arise.

---

# 8. LONG-TERM CONTINUITY

The project is expected to span multiple discussion threads and implementation stages.

Documentation shall therefore be designed to:

- minimize context loss;
- support thread handover;
- support collaboration between multiple AI systems;
- maintain long-term consistency.

---

# 9. REVIEW PHILOSOPHY

All reviews should focus on:

- consistency with Locked Decisions;
- architectural integrity;
- safety;
- maintainability;
- contribution to project objectives.

Reviews should propose improvements rather than redesign previously approved architecture without sufficient justification.

Review Completion Principle

Review SHALL determine whether the approved objective has been
adequately demonstrated and whether any material blocker remains.

Review SHALL NOT automatically expand the current scope because
additional improvements are technically possible.

Where a finding does not materially affect the approved objective,
safety, governance, correctness, traceability, or reproducibility,
the finding SHOULD be classified as a deferred improvement rather than
creating a new remediation cycle.

The purpose of review is to enable controlled progression toward the
project outcome, not to create indefinite refinement.

---

# 10. RELATED DOCUMENTS

Upstream

- DOCUMENT_ARCHITECTURE.md

Downstream

- PROJECT_FOUNDATION.md
- PROJECT_ROADMAP.md
- PROJECT_STATUS.md
- All remaining Stable Documents

---

# 11. AMENDMENT HISTORY

## Version 1.0

Initial release.

Locked Working Rules incorporated:

- WR-001 Outcome First
- WR-002 Workflow Tracking
- WR-003 Batch Recommendation Rule
- WR-004 Decisive Execution Rule

Established:

- project roles
- operational workflow
- document management rules
- communication principles
- long-term continuity strategy

---

## Version 1.1
Updated following completion of Phase 2.

Added Working Rules:

WR-005 Automatic Continuation Rule
WR-006 Blocker-only Question Rule
WR-007 Framework Completion Rule
WR-008 Master Document Delivery Rule

Updated:

Decision Workflow
Communication Principles

These amendments formalize the collaboration workflow validated throughout Phase 2 of the project.

---

## Version 1.2

Updated following the initiation of Population Wave 1.

Added:

WR-005A — Immediate Artifact Generation Rule

Updated:

Communication Principles

Execution-phase communication now prioritizes direct artifact generation after Locked Decisions.

Validated during Population Package production (PP-0001 onwards).

Operational Rule: Nếu không còn blocker, tôi sẽ tự động tạo artifact ngay trong cùng chat, không hỏi lại. Chỉ dừng để hỏi khi còn điểm chưa rõ hoặc có đề xuất mở rộng có thể ảnh hưởng kiến trúc/quản trị của project.

---

## Version 1.3

Updated following validation of Population Wave 1 execution.

Added:

- Source-First Population Package Verification Rule
- User-Controlled Population Package Sequence Rule
- Decision Batch Production Rule
- Gold Discussion Template Adherence Rule
- Immediate Complete Population Package Artifact Rule
- Source-Grounded Clinical Content Rule

These amendments formalized the Source-First and User-Controlled PP execution model.

---

## Version 1.4

Updated following continued Population Package execution.

Clarified:

- immediate artifact production after Decision Batch approval;
- execution-phase communication;
- Gold template adherence;
- source-grounded clinical content.

---

## Version 1.5

Updated following establishment of the Gold Population Package production workflow.

Clarified:

- complete four-artifact Population Package production;
- ZIP packaging;
- source-first scope verification;
- user-controlled PP sequence;
- Decision Batch workflow.

---

## Version 1.6

Updated following validation of the Population Wave 1 execution workflow and thread-handover requirements.

Major amendments include:

- replaced legacy two-part Population Package delivery with complete four-artifact Gold ZIP delivery;
- established mandatory Boundary declaration in the final production response;
- established Core / Supporting / Explicitly Excluded / Delegated-to PP boundary structure;
- established mandatory adjacent Population Package overlap check before scope lock;
- clarified externally maintained Project Coordinator PP list as execution source of truth;
- clarified that the Strategist SHALL wait for the Project Coordinator's next explicit PP request after completing a package;
- clarified Gold artifact production as the default post-approval execution behavior.

Version 1.6 becomes the authoritative operational workflow for Population Package execution.

## Version 1.7

Updated following completion of Population Wave 1 and preparation for
Repository & Integration Verification.

Clarified:

- four-artifact Gold Population Package as the canonical repository product;
- distinction between Gold lifecycle status and repository integration status;
- mandatory separation of Population Package QA readiness from repository
  integration verification;
- Phase 3 → Phase 4 thread-handover continuity;
- repository integration verification as a distinct downstream governance
  activity;
- preservation of the Project Coordinator's execution authority;
- continuation of Source-First and User-Controlled Population Package rules.

These amendments formalize the transition from large-scale knowledge population
to repository/integration verification without changing the established
Population Package production workflow.

## Version 1.9

Updated following completion of Phase 4 — Repository & Integration Verification.

This amendment establishes the controlled repository lifecycle for subsequent
project phases.

Added:

- WR-017 — Working Materials vs Controlled Repository Rule
- WR-018 — Repository Closeout Rule
- WR-019 — Explicit Git Staging Rule
- WR-020 — Source Material Copyright and Redistribution Rule

Established the distinction between:

- ACTIVE;
- CONTROLLED;
- WORKING;
- ARCHIVE.

Established the mandatory Repository Closeout workflow at every Phase Boundary:

1. Inventory working materials
2. Classify materials
3. Move materials to canonical locations
4. Update Status / Roadmap / Repository Map
5. Controlled Git staging and commit
6. Push and verify remote state

Established the prohibition of broad staging commands such as:

git add .

Established that the GitHub repository represents the controlled and
reproducible project state rather than a mirror of all local project materials.

Established that copyrighted or redistribution-restricted clinical Source
Materials SHALL NOT be pushed to the public GitHub repository unless
redistribution rights have been explicitly verified.

These amendments formalize the repository lifecycle and source-material
handling rules following Phase 4 closure and establish the operating model for
Phase 5 and subsequent phases.

## Version 2.0

Updated following completion of Phase 5 and establishment of the
project-level living-document synchronization policy.

Added:

- WR-021 — Project-Level Living Document Synchronization Rule

Clarified WR-018 — Repository Closeout Rule:

Phase closure evidence and controlled governance artifacts SHALL be
classified, canonically placed, explicitly staged, committed, pushed,
and remotely verified when required for phase closure.

Living project-level documents, including:

- PROJECT_STATUS
- PROJECT_ROADMAP
- LONG_TERM_ROADMAP
- Project Repository Map

MAY remain local during active phase transitions when they are expected
to continue evolving.

These documents SHALL be synchronized to the canonical GitHub repository
at an approved stable milestone or during final project closure /
deployment packaging.

At final project closure, repository-wide canonicalization SHALL ensure
that each active governed document has one canonical active version.
Historical versions SHALL be retained only where required for
traceability.

## Version 2.0 (2nd times)

Updated following validation of the Phase 6 Stage 2 Track 3 working
workflow and formalization of the approved Strategy-to-Execution model.

Added:

- WR-022 — Approved Strategy-to-Execution Workflow Rule
- WR-023 — Outcome-Bounded QA and No-Infinite-Remediation Rule

WR-022 formalizes the approved working flow:

Strategy / Scope Review
→ Implementation Objective
→ Claude Code Prompt
→ Claude Inspection / Implementation
→ Project Coordinator Run
→ ChatGPT Review
→ Bounded Refinement if Required
→ Final Run
→ Controlled Commit / Push
→ Verified Outcome

WR-023 establishes that QA shall remain rigorous and outcome-oriented
without creating indefinite remediation or refinement loops.

Clarified:

- implementation findings may return to Strategy / Scope Review only
  when they create a genuine architectural, governance, safety, or
  material outcome dependency;
- non-blocking improvements shall not automatically expand the current
  scope;
- completion shall be determined by adequate demonstration of the
  approved objective and absence of material blockers;
- the ultimate project goal remains the governing context for deciding
  whether additional work materially contributes to project completion.

No change to project authority, governance hierarchy, or existing
Population Package workflow.