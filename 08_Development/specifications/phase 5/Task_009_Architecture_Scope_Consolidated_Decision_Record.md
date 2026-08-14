# Task #009 — Architecture / Scope Consolidated Decision Record

**Phase:** Phase 5
**Task:** #009 — Safety Enforcement Boundary
**Gate:** Architecture / Scope B1–B4
**Status:** APPROVED — LOCKED

## 1. Scope

Task #009 establishes the governed Safety Enforcement / Authorization boundary before normal medical retrieval.

It is responsible for scope/authorization assessment, risk classification, emergency routing, prohibited/restricted capability handling, deterministic Safety Action selection, fail-closed behavior, escalation/termination semantics, traceability, and policy-version recording.

It does **not** perform retrieval, evidence assembly, runtime integration, generation, validation, clinical reasoning, or final clinical approval.

## 2. B1 — Safety Enforcement Boundary

**LOCKED**

Authorization and safety routing precede Retrieval. The boundary returns a governed Safety Decision and does not perform downstream work.

## 3. B2 — Authorization / Risk / Safety Action Contract

**LOCKED**

Risk vocabulary:

- `LOW`
- `MODERATE`
- `HIGH`
- `EMERGENCY`

Complete Safety Action vocabulary:

- `ALLOW`
- `ALLOW_WITH_WARNING`
- `ASK_CLARIFICATION`
- `REDIRECT`
- `ESCALATE`
- `REJECT`

Locked principles: default deny for unresolved safety state; emergency precedence; prohibited capabilities cannot be allowed; individualized high-risk clinical requests require controlled restriction; decisions are deterministic and policy-versioned; downstream layers cannot override restrictive Safety Decisions.

## 4. B3 — Failure / Escalation / Termination Semantics

**LOCKED**

- `REJECT` → no Retrieval, Generation, or automatic delivery.
- `ESCALATE` → no automatic clinical answer or completion claim.
- `ASK_CLARIFICATION` → current execution terminates; new information requires fresh evaluation.
- `REDIRECT` → new route requires fresh Safety Enforcement evaluation.
- `EMERGENCY` → normal pipeline terminates.
- Safety-engine failure → fail closed; never default to `ALLOW`.
- Escalation failure → never fall back to `ALLOW`.
- Restrictive actions cannot automatically recover to `ALLOW`.
- Validation success cannot override a restrictive Safety Decision.

## 5. B4 — Implementation Surface + Tests + E2E Acceptance

**LOCKED**

Implementation surface:

```text
08_Development/implementation/src/safe_medical_ai/safety/
├── __init__.py
├── models.py
├── enforcement.py
└── README.md
```

Tests:

```text
08_Development/implementation/tests/
├── test_safety_models.py
└── test_safety_enforcement.py
```

Acceptance covers typed models, authorization/risk, emergency/prohibited handling, six-action semantics, failure/fail-closed behavior, escalation, traceability, cross-boundary behavior, E2E scenarios, full regression, static architecture checks, and scope/diff verification.

## 6. Locked Cross-Boundary Invariants

```text
ALLOW
    → normal Phase 5 pipeline may proceed

ALLOW_WITH_WARNING
    → normal pipeline may proceed with warning preserved

ASK_CLARIFICATION
    → terminate current execution

REDIRECT
    → terminate unsafe route; fresh evaluation required

ESCALATE
    → terminate automated normal delivery

REJECT / EMERGENCY
    → terminate normal pipeline
```

No downstream layer may transform a restrictive Safety Decision into `ALLOW`.

## 7. Scope Closure Guard

Task #009 is intended to close the remaining runtime Clinical/Safety Enforcement gap identified by the Phase 5 Closure Review.

A future task must not be created merely for enhancement or optimization. A new task is justified only by a genuine architecture-level gap preventing acceptance of the locked Phase 5 objective.

## 8. Gate Disposition

**Task #009 Architecture / Scope Gate: PASS — CLOSED.**

B1–B4 are consolidated and locked.

**Next authorized artifact:** Task #009 Implementation Specification.
