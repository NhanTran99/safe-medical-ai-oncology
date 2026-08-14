# Safety Enforcement — Task #009

Bounded upstream Safety Enforcement / Authorization boundary.

Locked invariants:
- Safety precedes normal Retrieval.
- `EMERGENCY` is a risk class, not an action.
- Emergency maps to `ESCALATE`.
- Unresolved authorization defaults to `REJECT`.
- Restrictive actions never fall back to `ALLOW`.
- The module does not perform Retrieval, RTEP assembly, Integration,
  Generation, Validation, LLM calls, network access, or clinical reasoning.

Public entry point: `evaluate_safety`.
