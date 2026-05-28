# StyleSnap

## Project Overview
StyleSnap is an AI-powered personal outfit assistant that helps users build a digital wardrobe from uploaded clothing images and generate daily outfit recommendations based on personal wardrobe items, target style, occasion, color harmony, weather conditions, and user preferences.

StyleSnap 是一款基于个人衣橱的 AI 每日穿搭助手。用户可以上传衣物图片构建数字衣橱，系统结合衣物属性、目标风格、今日场景、色彩搭配、天气情况和个人偏好，生成可解释的个性化穿搭推荐。

The MVP focuses on a complete AI product loop: wardrobe digitization, clothing metadata extraction, rule-based recommendation scoring, explainable outfit generation, and a portfolio-ready user experience.

项目重点展示从用户痛点、AI 能力拆解、推荐逻辑设计到可运行 Demo 的完整 AI 产品闭环。

## Tech Stack
- Frontend: React, Vite, TypeScript, TailwindCSS, React Router
- Backend: FastAPI, SQLAlchemy 2, Pydantic, SQLite
- Testing: pytest for backend, `npm run build` plus manual acceptance for frontend

## Wardrobe Core Features
- Clothes CRUD API for create, list, get, update, and delete
- Mock AI analyze API based on image URL keywords
- Filterable wardrobe list by category, color, and season
- Add and edit flows with manually editable metadata
- Demo seed wardrobe inserted once for local demos

## Image Upload UX
StyleSnap supports a realistic clothing upload flow. On mobile, users can add clothing by taking a photo or choosing from their album. On desktop, users can upload or drag-and-drop an image.

In the MVP, uploaded images are previewed locally and passed to the mock vision service for metadata generation. The frontend keeps the existing clothes API contract by sending a mock `image_url` identifier for analysis and a local preview placeholder for saved session preview behavior. Future versions can replace this with Supabase Storage or S3.

## Weather Skill
StyleSnap uses weather as a contextual signal for outfit recommendation. The Weather Skill can read location-based or city-based weather data and convert it into outfit-aware context, such as layering needs, rain protection, UV protection, material suggestions, and shoe constraints.

In the MVP, weather data and location resolution are mocked. The interfaces are designed to be replaceable with real weather and geocoding APIs in later versions.

天气不是 StyleSnap 的主功能，而是穿搭推荐的环境上下文能力。Weather Skill 会将温度、降雨概率、风速、湿度和紫外线等信息转化为穿搭推荐可用的约束和提示，例如是否需要外套、是否需要防雨鞋、是否建议防晒、是否避免麂皮材质等。

## Recommendation Engine
- Reads persisted wardrobe items instead of frontend mock data
- Resolves weather only through the Weather Skill contract
- Builds bounded outfit candidates from `top + pants` plus optional shoes, outerwear, and hat
- Scores every candidate with explainable weighted rules
- Returns 2-3 top-ranked outfits with score breakdown, reasoning, warnings, and meta information

### Scoring Formula
```txt
OutfitScore =
0.30 * WeatherFit
+ 0.25 * StyleMatch
+ 0.20 * ColorHarmony
+ 0.15 * OccasionFit
+ 0.10 * UserPreference
```

### Why Rule-Based Recommendation
- Phase 4 prioritizes deterministic, testable recommendation behavior.
- Explainable scoring is easier to validate than a black-box ranking model.
- The architecture keeps scoring and reasoning replaceable for future LLM or learning-to-rank upgrades.

### Future Upgrade Path
- Replace template reasoning with `llm_service.py`
- Add learned reranking after collecting evaluation data
- Expand outfit constraints and style relationships without changing the API contract

## Phase 5 Frontend Experience
- Recommendation page now supports a full polished flow from weather context to result display
- Weather Skill is presented as outfit context, not a standalone weather app
- Add Item now uses upload-first UX instead of URL-first entry
- Outfit results are shown as focused Look cards with previous / next navigation instead of one long stacked list
- Users can regenerate recommendations with the current inputs

## Outfit Carousel UX
Recommendation results are displayed as focused Look cards. Instead of stacking all generated outfits vertically, StyleSnap shows one Look at a time with simple previous / next navigation, making the result easier to compare on both mobile and desktop.

## Clothes API Example

### Create Clothing Item
```json
POST /api/clothes
{
  "name": "White T-shirt",
  "image_url": "https://example.com/white-shirt.jpg",
  "category": "top",
  "color": "white",
  "style_tags": ["Clean Fit", "casual"],
  "season_tags": ["summer"],
  "thickness": "thin",
  "min_temperature": 20,
  "max_temperature": 32,
  "rain_suitable": false,
  "occasion_tags": ["上课", "休闲"],
  "notes": "Everyday base layer."
}
```

### Mock Analyze Example
```json
POST /api/clothes/analyze
{
  "image_url": "https://example.com/white-tshirt.jpg"
}
```

## Weather API Example

### Location-Based Weather Skill
```json
GET /api/weather/current?lat=25.033&lon=121.565
{
  "source": "location",
  "location": {
    "lat": 25.033,
    "lon": 121.565,
    "resolved_city": "Taipei"
  },
  "weather": {
    "city": "Taipei",
    "temperature": 27,
    "feels_like": 29,
    "min_temp": 24,
    "max_temp": 30,
    "weather_condition": "rainy",
    "rain_probability": 70,
    "wind_speed": 4.2,
    "humidity": 78,
    "uv_index": 5
  },
  "outfit_context": {
    "temperature_level": "warm",
    "rain_risk": "high",
    "wind_risk": "medium",
    "uv_risk": "medium",
    "layering_needed": false,
    "outerwear_needed": false,
    "rain_protection_needed": true,
    "uv_protection_needed": false,
    "recommended_materials": ["cotton", "linen", "breathable fabric", "quick-dry fabric"],
    "avoid_materials": ["suede", "heavy wool"],
    "shoe_constraints": ["avoid suede shoes", "prefer water-resistant shoes"],
    "styling_hints": ["choose breathable layers", "avoid long heavy outerwear"]
  }
}
```

## Recommendation API Example
```json
POST /api/outfits/recommend
{
  "occasion": "上课",
  "target_style": "Clean Fit",
  "preference_text": "不想太正式，想显高",
  "weather_source": {
    "type": "city",
    "city": "Taipei"
  }
}
```

## Demo Flow
1. Open `/recommendation`
2. Click `Use my location`, or enter a city manually if location is unavailable
3. Choose `occasion`
4. Choose `target_style`
5. Add optional `preference_text`
6. Click `Generate Outfits`
7. Review one focused Look card at a time, then switch between Looks with previous / next navigation
8. Use regenerate to request another recommendation set

## Result Card Design
- `Look 1 / 2 / 3` hierarchy
- clear total score badge
- compact item grid with clothing images when available
- simple progress-bar breakdown for five scoring dimensions
- summary reasoning first, detailed reasoning behind a collapsible section
- dedicated warning area with safe empty state

## Manual Acceptance
- Add Item mobile flow shows `拍照添加` and `从相册选择`
- Add Item desktop flow shows upload and drag-and-drop affordances
- Local image preview appears before save
- Invalid file type or files over 5MB show upload validation feedback
- Mock AI analyze works from local file selection
- Recommendation page loads
- Weather context can be acquired by location or city fallback
- Inputs render and submit cleanly
- 2-3 recommendations render as one-look-at-a-time cards when results exist
- Insufficient wardrobe state links users to wardrobe
- Regenerate action re-requests recommendations
- Wardrobe and landing flows still work

## Demo Seed Data
- The backend inserts 8 demo wardrobe items on startup when the clothes table is empty.
- Seed insertion is guarded so it does not duplicate on later startups.
- Seed data is disabled in backend tests to keep test isolation clean.

## Local Development

### Backend Run Command
```bash
cd backend
uv venv .venv --python 3.13
uv pip install --python .venv/bin/python --index-url https://pypi.tuna.tsinghua.edu.cn/simple -r requirements.txt
.venv/bin/python -m uvicorn app.main:app --reload
```

### Frontend Run Command
```bash
cd frontend
npm install
npm run dev
```

## Phase 5 Test Command
```bash
cd frontend
npm run build

cd ../backend
.venv/bin/python -m pytest
```

## Current Phase Status
- Phase 0: completed
- Phase 1: project skeleton completed
- Phase 2: wardrobe core completed
- Phase 3: weather skill completed
- Phase 4: recommendation engine completed
- Phase 5: frontend recommendation flow polish completed
- Current runtime surface:
  - Backend `GET /health`
  - Backend clothes CRUD and mock analyze APIs
  - Backend weather skill APIs for `GET /api/weather/current` and `GET /api/weather`
  - Backend recommendation engine API for `POST /api/outfits/recommend`
  - Frontend wardrobe list, add item, edit item, delete, and filters
  - Frontend upload-first Add Item flow with local preview and mock analyze support
  - Frontend polished recommendation page with location-first weather flow, focused Look cards, reasoning, warnings, and regenerate behavior

## Roadmap
- Phase 6: landing page polish, README packaging, portfolio framing, roadmap presentation, and final demo narrative
