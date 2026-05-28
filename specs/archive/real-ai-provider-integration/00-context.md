# Real AI Provider Integration Context

## Why Phase 7 Exists
StyleSnap already has a stable end-to-end MVP loop:
- wardrobe digitization
- Weather Skill as outfit context
- rule-based candidate generation
- rule-based scoring
- explainable recommendation results

Phase 7 upgrades the AI layer from purely mock behavior to a provider-based architecture without rewriting that loop.

## Product Principle
The large model must not replace the recommendation engine.

StyleSnap should remain:
- wardrobe-grounded
- weather-aware
- explainable
- testable
- fallback-safe

The AI stylist layer enhances explanation, tone, and optional rerank of the already-selected top looks. It must not invent clothing that is not present in the wardrobe candidates.

## Why Not Let The LLM Control Everything
- It could recommend clothing the user does not own.
- It would weaken score explainability.
- It would make regression testing much less stable.
- Provider outages would break the core user flow.
- The AI product story is stronger when capability is decomposed into deterministic ranking plus optional AI enhancement.

## Phase 7 Scope
- configurable stylist provider
- DeepSeek V4 Flash integration for explanation enhancement and optional rerank
- vision provider abstraction with mock default and real placeholder
- provider fallback behavior
- additive API metadata about which stylist provider ran

## Phase 7 Boundaries
- no rewrite of scoring rules
- no rewrite of Weather Skill
- no rewrite of wardrobe persistence
- no forced frontend changes
- no real vision integration requirement in this phase
