# Recommendation Engine Tasks

## Task 1: Recommendation Schemas
- Add request and response schemas for outfit recommendation
- Model weather source unions and nested outfit payloads
- Preserve stable API envelope conventions

## Task 2: Outfit Candidate Generation
- Add bounded candidate builder from wardrobe categories
- Require top + pants
- Add optional shoes, outerwear, and accessory roles when useful

## Task 3: Scoring Functions
- Add pure scoring functions for weather, style, color, occasion, and preference
- Add weighted total score calculation

## Task 4: Explanation and Warning Builder
- Add deterministic reasoning templates
- Add weather- and wardrobe-gap warnings

## Task 5: Recommendation Service
- Resolve weather context from weather source
- Load wardrobe items
- Generate, score, rank, and trim candidates
- Return meta information

## Task 6: Recommendation Router API
- Add `POST /api/outfits/recommend`
- Register outfits router in `main.py`

## Task 7: Backend Tests
- Add recommendation API and scoring tests first
- Keep health, wardrobe, and weather regression in the full test run

## Task 8: Minimal Frontend API Integration
- Add `recommendOutfits(payload)` service
- Extend recommendation page with input controls and minimal result preview
- Keep visual scope intentionally small

## Task 9: README and Repo Map Update
- Document recommendation engine contract, scoring formula, and Weather Skill usage
- Record Phase 4 decisions

## Task 10: Review and Archive
- Run verification
- Update `specs/current/`
- Archive `recommendation-engine`
- Update lessons learned
