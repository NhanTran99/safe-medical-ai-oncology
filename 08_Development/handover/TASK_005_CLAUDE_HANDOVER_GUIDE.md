# Hướng dẫn handover Task #005 cho Claude

## Cách tôi khuyến nghị

Không nên gửi cho Claude một đoạn chat dài chứa toàn bộ lịch sử thảo luận.

Hãy handover theo mô hình:

**1 authoritative task specification + 1 concise handoff instruction + required source files**

### Bước 1 — Đưa cho Claude 3 artifact mới nhất

- `TASK_005_IMPLEMENTATION_SPECIFICATION_v1.0.md`
- `TASK_005_CLAUDE_IMPLEMENTATION_HANDOFF.md`
- `PHASE_5_IMPLEMENTATION_READINESS_DECISION_RECORD_v6.0.md`
- `Phase_5_Governance_Consolidated_Decision_Record_v6.0.md`

### Bước 2 — Đưa các locked source documents cần thiết

Tối thiểu:

- `TECH_STACK.md`
- `OUTPUT_CONTRACT.md`
- `EVIDENCE_PACKAGE_SPECIFICATION.md` v1.1
- `RETRIEVAL_POLICY.md`
- `RAG_ARCHITECTURE.md` v1.1
- `RESPONSE_GENERATION_ARCHITECTURE.md` v1.1
- `OUTPUT_VALIDATION_FRAMEWORK.md`

Không cần đưa toàn bộ 239 PP corpus.

### Bước 3 — Yêu cầu Claude inspect repository trước khi code

Câu lệnh nên bắt đầu bằng:

> Read the attached Task #005 Implementation Specification and Handoff first.
> Then inspect the current `08_Development/implementation/` code and tests on
> branch `phase5/task002-scaffolding`.
>
> Do not implement anything until you have confirmed that the existing
> Task #002–#004 retrieval contracts are understood.
>
> Then implement exactly the approved Task #005 scope and return an exported
> patch plus the required test/scope report.
>
> Do not commit or push.

### Bước 4 — Không cho Claude tự “improve architecture”

Đặc biệt nhắc:

> If you identify a design issue that is outside the locked Task #005
> specification, do not silently solve it. Report it as a blocker/decision
> request.

### Bước 5 — Claude phải trả patch, không phải chỉ code snippet

Output cần:

- patch/export;
- exact changed files;
- tests;
- diff-check;
- scope confirmation;
- blockers.

Sau đó **không apply ngay**.

---

# Sau khi Claude trả patch

Workflow tiếp tục:

```text
Claude patch
    ↓
ChatGPT review
    ↓
PASS / REQUEST CHANGES
    ↓
nếu PASS:
VS Code apply
    ↓
pytest + diff-check
    ↓
explicit staging
    ↓
staged diff review
    ↓
commit
    ↓
push
    ↓
remote verification
```

### Rất quan trọng

**Không yêu cầu Claude commit/push trong bước implementation này.**

Task #005 specification hiện chỉ authorize:

> **implementation + tests + patch export**

Commit/push là **controlled closeout operation** sau khi ChatGPT review patch.

---

# Copy/paste message ngắn để gửi Claude

You can paste this after attaching the artifacts:

> **Task #005 Implementation — Execute Approved Specification**
>
> Read `TASK_005_IMPLEMENTATION_SPECIFICATION_v1.0.md` and
> `TASK_005_CLAUDE_IMPLEMENTATION_HANDOFF.md` first.
>
> Then inspect the current implementation and tests under
> `08_Development/implementation/` on branch
> `phase5/task002-scaffolding`.
>
> Implement exactly the approved Task #005 scope:
>
> **RetrievalResponse → Runtime Evidence Package**
>
> Preserve all locked B1–B4 decisions. Do not redesign architecture or
> silently resolve ambiguities outside the specification.
>
> Run the full test suite and `git diff --check`.
>
> Do not commit or push.
>
> Return:
> 1. implementation summary;
> 2. exact changed files;
> 3. tests added/changed and full test result;
> 4. diff-check result;
> 5. scope/prohibited-functionality confirmation;
> 6. exported patch;
> 7. blockers/decision requests, if any.
>
> If an issue requires a governance or architectural decision not already
> locked in the specification, stop and report it instead of inventing a
> solution.
