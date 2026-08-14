# Phase 5 Governance — Package B Decision Record
Status: LOCKED — approved by Project Coordinator
Purpose: Consolidated record of Package B decisions.

## Definition
Retrieval Ready means the governed knowledge foundation is eligible for controlled retrieval. It does not mean the chatbot is runtime-ready or clinically/safety validated.

## Locked Gate
Retrieval Ready requires all five domains PASS:
1. RR-1 Gold Integrity
2. RR-2 Repository Verification
3. RR-3 Registry Verification
4. RR-4 Traceability
5. RR-5 Required Integration Metadata

No averaging or partial-pass substitution is allowed.

## Evidence
The assessment reuses controlled Phase 3/4 evidence plus an explicit Retrieval Ready gate assessment. It is an evidence index/gate decision, not a duplicate evidence repository.

## Controlled Vocabulary
- PENDING — assessment not yet performed / awaiting verification
- PASS — all mandatory criteria satisfied
- FAIL — a mandatory criterion fails
- NOT READY — evidence is insufficient to establish PASS

## Assessment Model
Each criterion records Status, Evidence Reference, Reviewer/Authority, and Assessment Date.

## Registry Interface
- Knowledge Asset Registry (KAR): asset identity, lifecycle, evidence, provenance, knowledge metadata.
- Population Integration Manifest (PIM): PP identity/integration unit, repository mapping, integration verification and related repository evidence.
- KAR and PIM remain distinct.
- Retrieval Ready is a derived gate result, not a KAR lifecycle state and not a PIM field that replaces the gate.

## Granularity
Assessment is performed at Knowledge Asset / integration-unit level and may aggregate upward. Repository-level PASS does not automatically imply asset-level PASS.

## Boundary
Package B does not decide retrieval algorithm performance, ranking quality, chatbot response quality, hallucination rate, clinical safety, or end-to-end system performance. Those belong to Phase 5 implementation/validation.

## Deferred
- Exact field-level KAR/PIM schema.
- Runtime retrieval schema.
