# Recommendation Engine Decision Log

## Decision 1: Use Rule-Based Recommendation In Phase 4
- Decision:
  - Build the first recommendation engine with deterministic rules and weighted scoring.
- Why:
  - The MVP needs explainable, testable behavior more than model sophistication.
- Alternatives Rejected:
  - End-to-end LLM recommendation
  - Black-box ranking with no deterministic breakdown
- Future Extension:
  - Add learned ranking later once user behavior and evaluation data exist.

## Decision 2: Generate Candidates Before Ranking
- Decision:
  - Produce bounded outfit candidates first, then score and sort them.
- Why:
  - It separates combination logic from ranking logic and keeps scoring independently testable.
- Alternatives Rejected:
  - Greedy single-pass item selection
  - Mixing candidate generation and scoring in one opaque loop
- Future Extension:
  - Add pruning heuristics or reranking stages without changing the API.

## Decision 3: Depend On Weather Skill Context Instead Of Raw Weather Only
- Decision:
  - Consume `WeatherSkillResponse` and use `outfit_context` as the primary weather constraint input.
- Why:
  - Weather Skill already translates raw weather into outfit-aware rules such as layering, rain protection, and UV protection.
- Alternatives Rejected:
  - Re-implementing weather heuristics inside the recommendation router
  - Treating weather as a direct frontend concern
- Future Extension:
  - Expand `outfit_context` fields as recommendation complexity grows.

## Decision 4: Use Template-Based Explanations
- Decision:
  - Keep reasoning deterministic and template-based in Phase 4.
- Why:
  - Explanation quality must remain inspectable and stable while the recommendation rules are still evolving.
- Alternatives Rejected:
  - Real LLM explanation generation
  - Returning scores without human-readable reasoning
- Future Extension:
  - Replace or augment templates with `llm_service.py` once prompt and privacy boundaries are defined.

## Decision 5: Keep Phase 4 Frontend Minimal
- Decision:
  - Add only enough frontend integration to trigger and preview recommendation results.
- Why:
  - Phase 4's main value is the decision engine, not final presentation polish.
- Alternatives Rejected:
  - Building the full portfolio-ready results experience in the same phase
- Future Extension:
  - Phase 5 will focus on richer result cards, interaction, and screenshot quality.
