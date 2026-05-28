# Portfolio Polish Architecture

## Phase Structure
Phase 6 is a presentation and documentation phase. It should mainly touch:
- landing page composition and copywriting
- README information architecture
- lightweight portfolio-supporting documentation
- current/archive spec snapshots

It should avoid structural backend work unless a documentation or naming issue requires a minimal text correction.

## Landing Page Component Structure
- `LandingPage`
  - Hero section
  - Problem section
  - Solution loop section
  - AI capability breakdown grid
  - Demo flow section
  - Roadmap preview section
  - final CTA section

The page should reuse existing project design primitives when possible:
- `PageHeader` if appropriate for supporting pages, but the hero should likely become landing-specific rather than a generic page header
- existing button, card, and section styling patterns from the app shell

## README Information Architecture
README should be reorganized into product-first reading order:
1. what the product is
2. who it serves
3. what user problem it solves
4. what the end-to-end MVP flow is
5. how the AI capability is decomposed
6. how the system is structured
7. how recommendation logic works
8. what is mocked versus real
9. how to run, test, demo, and deploy it

This order is better for interviewers than a code-first or endpoint-first README.

## Portfolio Case Study Structure
The portfolio case study text should follow this narrative:
- product framing
- user problem
- AI capability decomposition
- technical implementation
- explainability and recommendation logic
- UX polish and demo readiness
- mock-to-real architecture

This structure can live inside README now and remain reusable later for resume bullets, portfolio site copy, or case-study slides.

## Deployment Notes Structure
Deployment notes should stay advisory, not operationally binding:
- frontend hosting suggestions
- backend hosting suggestions
- production database suggestions
- production storage suggestions
- note that the current MVP uses local preview and mock providers

The goal is to show launch readiness and architecture maturity, not to introduce real deployments in this phase.

## Mock-To-Real Service Abstraction
The architecture should continue to describe StyleSnap through replaceable seams:
- `ai_vision_service.py`
  - mock image analysis now
  - future multimodal model adapter later
- `weather_service.py`
  - mock provider now
  - real weather and reverse geocoding adapters later
- local preview image handling in frontend
  - MVP placeholder now
  - object storage later
- scoring and reasoning services
  - deterministic rule layer now
  - optional LLM or learned ranking later

This abstraction is a portfolio asset and should be documented explicitly.

## Backend Contract Boundary
Phase 6 should not change backend contracts because:
- the end-to-end loop is already working
- the frontend and README can now be polished against stable APIs
- reopening schemas would create regression risk unrelated to portfolio outcomes
- the real value of this phase is clarity, not feature growth

## Naming Boundary
Global copy updates are allowed where they improve product framing:
- emphasize `Weather Skill as outfit context`
- emphasize `AI outfit assistant`
- avoid framing the app as a weather tool
- keep score-dimension naming consistent with the documented scoring formula
