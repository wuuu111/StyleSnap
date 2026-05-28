# Real AI Provider Integration Architecture

## Recommendation Flow
- wardrobe items
- Weather Skill `outfit_context`
- occasion / target style / preference
- rule-based candidate generation
- rule-based scoring
- top 2-3 outfits
- baseline template reasoning
- stylist provider enhancement
- stable response payload

The stylist provider runs after rule selection, never before.

## Provider Package
- `backend/app/services/providers/__init__.py`
- `stylist_provider.py`
- `mock_stylist_provider.py`
- `deepseek_stylist_provider.py`
- `vision_provider.py`
- `mock_vision_provider.py`
- `vision_provider_placeholder.py`
- optional provider selection helper if needed

## Stylist Provider Contract
`StylistProvider` returns a stable dict with:
- `provider`
- `model`
- `recommended_order`
- `looks`
- `fallback_used`

Each look entry contains:
- `id`
- `stylist_summary`
- `weather_reasoning`
- `style_reasoning`
- `color_reasoning`
- `occasion_reasoning`
- `preference_reasoning`
- `improvement_suggestion`

## Vision Provider Contract
`VisionProvider` returns clothing analysis aligned to the existing clothing analyze schema.

## Merge Strategy
- build template reasoning first
- call stylist provider
- merge enhanced fields into baseline reasoning field by field
- map `stylist_summary` into response `reasoning.summary`
- keep baseline values for any missing AI field
- attach provider metadata to `ai_metadata`

## Fallback Strategy
- if stylist provider config is missing, use mock stylist
- if DeepSeek request fails, times out, or returns invalid JSON, use mock stylist output and mark fallback
- if vision provider config is incomplete, use mock vision by default

## Contract Boundary
- keep `recommended_outfits` response shape intact
- only add optional `ai_metadata`
- no frontend dependency on new metadata in this phase
