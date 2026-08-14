# Phase 5 Governance — Package D Decision Record
Status: LOCKED — approved by Project Coordinator
Purpose: Consolidated record of Package D decisions.

## D1 — Post-Gold PP Amendment Lifecycle
A substantive post-Gold change must use a governed amendment:
issue → amendment registration → impact assessment → correction → re-QA → Layer 3 re-verification → integration re-verification → controlled commit → closure.

Every amendment assesses PP/Asset, affected artifacts, clinical/evidence impact, registry impact, integration impact, retrieval impact, and required re-validation.

Every canonical-artifact amendment requires Layer 3 rerun. Retrieval impact is reassessed when relevant. PP-0195 is a historical precedent, not a special-case rule.

## D2 — Classification, severity and propagation
Four amendment classes:
- A Administrative
- B Metadata / Structural
- C Knowledge / Evidence
- D Safety / Governance Critical

Severity is separate:
LOW / MODERATE / HIGH / CRITICAL.

Downstream dimensions:
PP/Asset → Registry → Integration → Retrieval → Runtime/Validation.

Required action is proportional to impact. Safety-critical changes may temporarily make the affected knowledge NOT READY/restricted until review and re-validation.

Closed amendment evidence records amendment ID, PP/Asset ID, class, severity, reason, affected artifacts, before/after state/version, QA evidence, integration evidence, retrieval disposition, commit and closure status.

Historical states remain reconstructable.

## D3 — KAR ↔ Population Integration Manifest authority
- KAR is authoritative for Knowledge Asset identity, metadata, evidence classification, lifecycle, provenance, ownership/governance.
- Population Integration Manifest is authoritative for PP integration unit, canonical repository mapping, integration verification state and repository/integration evidence.
- Stable identifiers link the two; metadata is not duplicated wholesale.
- Cross-domain conflicts are surfaced for governance review; neither registry is silently overwritten.
- Retrieval Ready is derived from KAR + PIM + verification evidence + RR assessment; it belongs to neither registry as a lifecycle state.
- PP amendments trigger KAR/PIM impact assessment only where relevant.
- Exact field-level schema is intentionally deferred to implementation context.

## Approval
Package D is approved and locked.
