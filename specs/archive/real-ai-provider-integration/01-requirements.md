# Real AI Provider Integration Requirements

## Feature Goal
Introduce a configurable AI provider architecture that keeps the existing rule-based recommendation flow stable while allowing a real stylist model to enhance explanations and optionally rerank top looks.

## Functional Requirements
1. The backend must support `STYLIST_PROVIDER` and `VISION_PROVIDER` environment-based provider selection.
2. Default provider mode for both stylist and vision must remain `mock`.
3. Missing API keys or incomplete provider configuration must not break startup.
4. DeepSeek stylist integration must only enhance already-selected candidate looks.
5. The AI stylist layer must not invent new wardrobe items or recommend purchases.
6. Recommendation candidate generation and scoring must remain rule-based.
7. Recommendation API must keep its existing `recommended_outfits` contract.
8. Recommendation API may add optional `ai_metadata`.
9. `ai_metadata` must include:
   - `stylist_provider`
   - `stylist_model`
   - `fallback_used`
10. DeepSeek reorder should apply only when the returned `recommended_order` is complete and valid.
11. Invalid or partial AI reorder must fall back to original rule-based ordering.
12. `/api/outfits/recommend` must still succeed when the stylist provider fails.
13. `/api/clothes/analyze` must move behind a vision provider abstraction.
14. Mock vision must remain the default implementation.
15. When `VISION_PROVIDER != mock` but config is incomplete, analyze must fall back to mock vision.
16. A placeholder real vision provider may exist but must not be treated as fully supported behavior in this phase.

## Required Environment Variables
- `STYLIST_PROVIDER=mock`
- `VISION_PROVIDER=mock`
- `DEEPSEEK_API_KEY=`
- `DEEPSEEK_BASE_URL=https://api.deepseek.com`
- `DEEPSEEK_MODEL=deepseek-v4-flash`
- `DEEPSEEK_TIMEOUT_SECONDS=30`
- `VISION_PROVIDER_NAME=mock`
- `VISION_API_KEY=`
- `VISION_BASE_URL=`
- `VISION_MODEL=`

## Security Requirements
1. Real API keys must only come from environment variables.
2. Real API keys must never be committed to the repository.
3. API keys must not be logged.
4. Full image base64 payloads must not be logged.
5. DeepSeek stylist requests must send only necessary structured clothing metadata and context, not raw images.
6. Provider failure must fall back to stable recommendation behavior instead of failing the core API.

## Non-Goals
- No real vision rollout requirement
- No direct LLM replacement of scoring
- No direct LLM generation of nonexistent clothing
- No frontend AI-specific rendering work requirement
- No large SDK dependency adoption
