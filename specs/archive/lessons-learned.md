# Lessons Learned

## Phase 2: Wardrobe Core
- A dedicated feature spec kept the wardrobe scope from bleeding into weather and recommendation logic.
- Keeping mock AI behind `ai_vision_service.py` made the analyze contract usable without external dependencies.
- Centralizing frontend wardrobe requests in `clothesApi.ts` prevented fetch logic from leaking into page components.
- Seed data belongs in backend bootstrap, not frontend mocks, because later recommendation logic needs one consistent data source.
- SQLite test isolation required explicit environment-driven database reconfiguration; otherwise model metadata and state leaked between tests.

## Phase 3: Weather Skill
- Treating weather as an internal skill produced a cleaner product surface than building a visible city-search weather tool.
- Converting raw weather into `outfit_context` early prevents the later recommendation engine from duplicating environmental rules.
- Geolocation-first with city fallback keeps the demo closer to a real recommendation flow while still staying fully mockable.
- A small provider seam and a mock coordinate resolver were enough to preserve replaceability without introducing real weather or geocoding dependencies.
- Frontend dependency trees in this workspace can become partially corrupted; reinstalling dependencies was the fastest reliable recovery path when standard library files went missing.

## Phase 4: Recommendation Engine
- Candidate generation and scoring needed separate files; combining them too early would have made the rules harder to test and explain.
- Weather Skill `outfit_context` kept recommendation rules simpler because the recommendation engine could consume constraints instead of raw meteorology.
- A bounded candidate search was enough for the MVP wardrobe size and prevented unnecessary combinatorial growth.
- Minimal frontend integration was the right scope for this phase; the decision engine can now evolve independently from the polished result UI that comes next.

## Phase 5: Frontend Recommendation Flow
- The recommendation page became easier to reason about once state orchestration stayed in the page and presentation moved into smaller components.
- Weather worked better as a compact contextual entry section than as an always-visible detailed dashboard.
- Splitting score, reasoning, and warnings into separate cards improved screenshot quality without any backend change.
- Explicit insufficient-wardrobe and no-result states made the recommendation experience feel more product-grade than generic API error text.
