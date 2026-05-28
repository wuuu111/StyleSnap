# Recommendation Engine Requirements

## Feature Goal
Generate 2-3 explainable outfit recommendations from the user's wardrobe plus Weather Skill context.

## User Stories
- As a user, I can request today's outfit recommendations.
- As a user, I can choose an occasion and target style, and optionally describe my preference.
- As a user, I can rely on either city-based or location-based weather context without manually re-entering raw weather details.
- As a user, I receive 2-3 scored outfits with understandable reasoning and warnings.
- As a developer, I can test the scoring and recommendation logic without any real LLM or vision model.

## Functional Requirements
1. The backend must expose `POST /api/outfits/recommend`.
2. The request body must include:
   - `occasion`
   - `target_style`
   - `preference_text`
   - `weather_source`
3. `weather_source` must support:
   - `{"type": "city", "city": "..."}`
   - `{"type": "location", "lat": ..., "lon": ...}`
4. The recommendation service must read current wardrobe data from persisted `ClothingItem` rows.
5. The recommendation service must resolve weather only through the Weather Skill service and consume `outfit_context`.
6. The recommendation service must generate outfit candidates from wardrobe category combinations.
7. The service must score every candidate using:
   - `weather_fit_score`
   - `style_match_score`
   - `color_harmony_score`
   - `occasion_fit_score`
   - `user_preference_score`
   - `total_outfit_score`
8. `total_outfit_score` must use:
   - `0.30 * WeatherFit`
   - `0.25 * StyleMatch`
   - `0.20 * ColorHarmony`
   - `0.15 * OccasionFit`
   - `0.10 * UserPreference`
9. The API must return:
   - `weather_context`
   - `recommended_outfits`
   - `meta`
10. The API must return 2-3 outfits when enough viable candidates exist.
11. Every returned outfit must include:
   - `id`
   - `items`
   - `total_score`
   - `score_breakdown`
   - `reasoning`
   - `warnings`
12. Reasoning must include:
   - `summary`
   - `weather_reasoning`
   - `style_reasoning`
   - `color_reasoning`
   - `occasion_reasoning`
   - `preference_reasoning`
13. Warnings must be template-based and deterministic.
14. The API must not depend on a real LLM or real AI vision service.

## Candidate Generation Rules
- `top` and `pants` are mandatory for a full outfit.
- `shoes` should be added when available.
- `outerwear` should be added or preferred when `outerwear_needed` or `layering_needed` is true.
- Rainy context should prefer `rain_suitable=true` shoes and outerwear.
- Warm context should avoid thick outerwear when possible.
- Cool or cold context should prefer medium or thick outerwear when available.
- Candidate search must be bounded:
  - top: max 8
  - pants: max 8
  - shoes: max 5
  - outerwear: max 5
  - total candidates: max 50
- Return at most top 3 outfits after scoring.

## Response Contract
- `weather_context`: full `WeatherSkillResponse`
- `recommended_outfits`: list of explainable outfit recommendations
- `meta`:
  - `candidate_count`
  - `returned_count`
  - `scoring_version`

## Edge Cases
- Empty wardrobe returns stable error with message that recommendation cannot run without wardrobe items.
- Missing `top` returns stable error.
- Missing `pants` returns stable error.
- Missing `shoes` may still return partial outfits without shoes if tops and pants exist.
- Missing `outerwear` in cold or layering-heavy weather should still allow output but add warnings.
- Rainy weather without suitable shoes or outerwear should still allow output but add warnings.
- Empty `preference_text` returns neutral user-preference score of 70.
- `target_style` without direct wardrobe matches should still return best-effort recommendations with lower style score.
- `occasion` without direct wardrobe matches should still return best-effort recommendations with lower occasion score.
- Weather Skill fallback city or fallback location context must still be accepted.

## Non-Goals
- Virtual try-on
- Ecommerce recommendation
- Deep learning ranking
- Multi-user auth and permissions
- Real LLM explanation generation
- Real multimodal clothing understanding
