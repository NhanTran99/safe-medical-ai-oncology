# PROJECT_ROADMAP

---

# DOCUMENT METADATA

Document ID:
DOC-FND-003

Version:
1.1

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
DOCUMENT_ARCHITECTURE.md
CORE_WORKING_RULES.md
PROJECT_FOUNDATION.md
MISSION_AND_SCOPE.md

Required By:
PROJECT_STATUS.md
All Architecture Documents

Last Updated:
2026-08-02

---

# 1. PURPOSE

This document defines the governed development roadmap of the project.

Unlike a traditional software roadmap, this roadmap is organized around governance milestones.

Each phase is completed only after its deliverables, documentation, and approval criteria have been satisfied.

---

# 2. ROADMAP PHILOSOPHY

The project follows a Governed Milestone model.

A phase is considered complete only when:

- planned deliverables are completed;
- corresponding Stable Documents are approved and locked;
- completion criteria are satisfied;
- downstream phases are unblocked.

Progress is measured by governance completion rather than coding progress.

The roadmap may be refined through minor amendments when governed architectural decisions significantly improve project organization while preserving the overall project direction.

---

# 3. PROJECT ROADMAP

## Phase 0 — Foundation

### Objective

Establish the project's identity, governance, documentation system, and working methodology.

### Deliverables

- DOCUMENT_ARCHITECTURE.md
- CORE_WORKING_RULES.md
- PROJECT_FOUNDATION.md
- MISSION_AND_SCOPE.md
- PROJECT_ROADMAP.md
- PROJECT_STATUS.md
- NOVELTY.md

### Completion Criteria

- Foundation Stable Documents approved.
- Documentation governance finalized.
- Project identity finalized.

---

## Phase 1 — System Architecture

### Objective

Design the complete architecture of the Safe Medical AI System.

### Expected Deliverables

- SYSTEM_ARCHITECTURE.md
- CLINICAL_NAVIGATION_ENGINE.md
- MEDICAL_GOVERNANCE.md
- SAFETY_FRAMEWORK.md
- RAG_ARCHITECTURE.md
- KNOWLEDGE_BASE.md
- PROMPTING_STRATEGY.md

### Completion Criteria

- Overall architecture approved.
- Component interactions defined.
- Safety architecture established.
- Knowledge architecture completed.
- Prompting strategy finalized.
- Architecture governance approved.

---

## Phase 2 — Clinical Knowledge Curation

### Objective

Build, govern, curate, and maintain the clinical knowledge assets that power the approved system architecture.

### Deliverable Structure

#### Clinical Knowledge Assets

Examples include:

- Clinical Knowledge Objects
- Knowledge Passports
- Knowledge Source Registry
- Clinical Knowledge Domains
- Curated Guideline Assets

#### Operational Specifications

- KNOWLEDGE_INGESTION_WORKFLOW.md
- KNOWLEDGE_UPDATE_POLICY.md

#### Knowledge Repository Assets

Operational assets generated during implementation, including:

- Knowledge Registry
- Approved Knowledge Objects
- Curated Evidence Assets

### Completion Criteria

- Initial Clinical Knowledge Assets curated.
- Knowledge ingestion workflow approved.
- Knowledge governance workflow operational.
- Initial knowledge repository established.

---

## Phase 3 — Evaluation Framework

### Objective

Define how the system will be evaluated scientifically and technically.

### Expected Deliverables

- EVALUATION_FRAMEWORK.md
- CLINICAL_VALIDATION.md
- TECHNICAL_VALIDATION.md

### Completion Criteria

- Evaluation protocol approved.
- Clinical assessment strategy finalized.
- Technical evaluation metrics defined.

---

## Phase 4 — Development Specification

### Objective

Prepare implementation-ready technical specifications.

### Expected Deliverables

- TECH_STACK.md
- REPOSITORY_STRUCTURE.md

### Completion Criteria

- Development specifications approved.
- Repository architecture finalized.
- Claude implementation ready.

---

## Phase 5 — Implementation

### Objective

Implement the approved architecture.

### Expected Activities

- Frontend development.
- Backend development.
- RAG implementation.
- AI workflow implementation.
- Testing.

### Completion Criteria

- MVP completed.
- Internal review completed.

---

## Phase 6 — Validation

### Objective

Validate the implemented system.

### Expected Activities

- Clinical expert review.
- Technical validation.
- Safety validation.
- User testing.

### Completion Criteria

- Validation targets achieved.
- Improvement actions documented.

---

## Phase 7 — Portfolio Packaging

### Objective

Prepare showcase materials.

### Expected Deliverables

- GitHub repository.
- Technical documentation.
- System architecture figures.
- Demonstration video.
- Evaluation summary.

### Completion Criteria

- Portfolio package completed.
- Public presentation ready.

---

# 4. PHASE TRANSITION RULES

A phase may begin only if:

- the previous phase has been completed;
- blocking decisions have been locked;
- required Stable Documents have been approved.

Skipping governance phases is discouraged unless explicitly approved by the Project Coordinator.

Architecture phases should be considered complete only after all required architectural Stable Documents have been approved, locked, and integrated into the governed documentation system.

Knowledge curation phases shall prioritize governed clinical knowledge quality over implementation speed.


# 5. CHANGE MANAGEMENT

The roadmap is intended to remain stable.

Minor additions and organizational refinements should be incorporated through amendments.

Minor roadmap refinements are permitted when governed architectural decisions improve project organization while preserving the project's overall direction.

Major restructuring requires a Major Version update.

---

# 6. SUCCESS INDICATORS

The roadmap aims to ensure that the project progresses through:

- well-defined governance;
- reproducible documentation;
- architecture-first development;
- governed clinical knowledge curation;
- safe implementation;
- research-grade outcomes.

---

# 7. RELATED DOCUMENTS

## Upstream

- DOCUMENT_ARCHITECTURE.md
- CORE_WORKING_RULES.md
- PROJECT_FOUNDATION.md
- MISSION_AND_SCOPE.md

---

## Downstream

- PROJECT_STATUS.md
- All Architecture Documents
- Clinical Knowledge Curation Documents
- Evaluation Documents
- Development Documents

---

# 8. AMENDMENT HISTORY

## Version 1.1

Minor Foundation Release.

### Summary

Refined the governed project roadmap following completion of the System Architecture phase.

### Amendments

#### Roadmap Structure

- Moved KNOWLEDGE_BASE.md from Phase 2 to Phase 1.
- Moved PROMPTING_STRATEGY.md from Phase 2 to Phase 1.
- Removed GUIDELINE_POLICY.md as an independent Stable Document.
- Renamed Phase 2 from **Knowledge Architecture** to **Clinical Knowledge Curation**.

#### Phase Objectives

Updated the objective of Phase 2 to emphasize:

- clinical knowledge curation;
- knowledge governance;
- knowledge lifecycle management;
- operational knowledge workflows.

#### Phase Deliverables

Introduced a deliverable structure consisting of:

- Clinical Knowledge Assets;
- Operational Specifications;
- Knowledge Repository Assets.

#### Completion Criteria

Updated Phase 1 completion criteria to include:

- Knowledge Architecture completed;
- Prompting Strategy finalized;
- Architecture governance approved.

Updated Phase 2 completion criteria to include:

- Initial Clinical Knowledge Assets curated;
- Knowledge ingestion workflow approved;
- Knowledge governance workflow operational;
- Initial knowledge repository established.

#### Roadmap Governance

Added roadmap refinement guidance permitting minor organizational amendments while preserving overall project direction.

---

## Version 1.0

Initial release.

Established:

- Governed Milestone roadmap.
- Phase structure.
- Deliverables for each phase.
- Completion criteria.
- Phase transition rules.
- Change management strategy.

Locked Decisions incorporated:

- Governed Milestone Philosophy.
- Outcome First.
- Documentation-driven Development.
-````

---

## Strategist Review (sau khi hoàn thành v1.1)

Tôi đã rà soát lại toàn bộ Foundation sau bản **v1.1**.

Đánh giá của tôi:

- **Foundation**: ổn định.
- **Roadmap**: phản ánh đúng trạng thái thực tế của dự án.
- **Phase 1**: đã được "đóng vòng" (closed loop), không còn phụ thuộc ngược.
- **Phase 2**: giờ có nhiệm vụ rõ ràng, chuyển từ **thiết kế** sang **vận hành tri thức**.

Tôi **không còn đề xuất amendment nào nữa** cho Foundation ở thời điểm này.

Theo nguyên tắc **Foundation Stability**, từ đây trở đi chỉ nên sửa Foundation khi có thay đổi kiến trúc thực sự lớn (Major Version) hoặc có một Minor Amendment thật sự cần thiết trong tương lai.

---

## Project Continuation Block

### Current Phase

**Phase 2 — Clinical Knowledge Curation (Ready to Start)**

### Current Step

**Foundation v1.1 Released**

### Completed Artifacts

- ✅ Foundation: 7 Stable Documents (v1.1 aligned)
- ✅ Architecture: 7 Stable Documents (LOCKED)

### Locked Decision Range

**LD-0010 → LD-0087**

### Next Discussion Batch

**Batch #16 — Clinical Knowledge Ingestion Workflow**

### Next Artifact

**`KNOWLEDGE_INGESTION_WORKFLOW.md` v1.0 (LOCK)** – tài liệu đầu tiên của **Phase 2 — Clinical Knowledge Curation**.