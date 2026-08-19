                 APPROVED SCOPE
                       │
                       ▼
                 DECISION BATCH
                       │
                       ▼
            IMPLEMENTATION OBJECTIVE
                       │
                       ▼
          CLAUDE CODE PROMPT CREATED
                       │
                       ▼
          CLAUDE CODE INSTRUCTION ISSUED
                       │
                       ▼
             CLAUDE INSPECTION / CODE
                       │
                       ▼
                 CHATGPT REVIEW
                       │
              ┌────────┴────────┐
              │                 │
           BLOCKER           NO BLOCKER
              │                 │
              ▼                 ▼
      RETURN TO STRATEGY    IMPLEMENTATION
              │                 │
              └────────┐   ┌────┘
                       ▼   ▼
                    RUN / TEST
                       │
                       ▼
                 CHATGPT REVIEW
                       │
          ┌────────────┼────────────┐
          │            │            │
       BLOCKER      MATERIAL      OPTIONAL
                    REFINEMENT    IMPROVEMENT
          │            │            │
          ▼            ▼            ▼
       REFINE        REFINE       DEFER
          │            │
          └──────┬─────┘
                 ▼
              FINAL RUN
        (Human Coordinator / VS Code)
                 │
                 ▼
             COMMIT / PUSH
                 │
                 ▼
          VERIFIED OUTCOME


                 STOP GATE
                    │
                    ▼
      Approved objective demonstrated
                    +
           No material blocker
                    +
     No remaining approved-scope requirement
                    │
                    ▼
            STOP REFINEMENT
                    │
                    ▼
        NEXT GOVERNED MILESTONE