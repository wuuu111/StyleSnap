# StyleSnap

## 1. Project Overview
StyleSnap is an AI-powered personal outfit assistant that helps users build a digital wardrobe from clothing images and generate daily outfit recommendations based on personal wardrobe items, target style, occasion, weather context, color harmony, and user preferences.

StyleSnap 是一款基于个人衣橱的 AI 每日穿搭助手。用户可以通过拍照或相册上传衣物，构建个人数字衣橱。系统结合天气上下文、今日场景、目标风格、色彩搭配和用户偏好，生成 2-3 套可解释的每日穿搭 Look。

The MVP is intentionally designed as a complete AI product loop rather than a collection of disconnected UI pages. It demonstrates wardrobe digitization, contextual recommendation, deterministic scoring, explainable reasoning, and responsive demo UX.

## 2. Target Users
- Students and young professionals who often ask “what should I wear today?”
- Users who already own enough clothes but struggle to combine them well
- Users who want to approximate a target style using their existing wardrobe
- Reviewers, interviewers, and hiring managers evaluating AI product design and execution

## 3. Product Problem
StyleSnap focuses on a practical decision problem:
- people often repeat the same safe outfits even when they own many clothes
- target styles are easy to admire but hard to recreate from an existing wardrobe
- weather affects comfort, layering, shoes, and materials in ways users do not always model explicitly
- most outfit advice tools are not grounded in the clothes the user already owns

StyleSnap solves this by making the wardrobe the source of truth, then layering weather context, occasion constraints, style direction, and user preference on top of it.

## 4. Core User Flow
1. Add clothing by camera, album, drag-and-drop, or local upload
2. Review or edit mock AI-generated metadata
3. Save items into a digital wardrobe
4. Allow location or enter a city to build outfit-aware weather context
5. Choose occasion, target style, and optional preference text
6. Generate 2-3 explainable Looks
7. Compare one focused Look card at a time through previous / next navigation

## 5. MVP Features
- Upload-first wardrobe intake flow
- Mock clothing metadata analysis with manual correction
- Wardrobe CRUD and filters
- Weather Skill with location-first flow and city fallback
- Rule-based outfit recommendation from persisted wardrobe items
- Explainable score breakdown, reasoning, and warnings
- Responsive landing, wardrobe, add-item, and recommendation experience
- Mock-to-real architecture with replaceable service seams

## 6. AI Capability Design
StyleSnap separates the product into four AI-facing capabilities:

### Wardrobe Digitization
- Users add clothing through realistic image intake
- Mock vision logic produces editable metadata such as category, color, style, season, and occasion tags

### Weather Skill
- Raw weather data is transformed into outfit-aware context
- The system produces constraints such as:
  - `layering_needed`
  - `outerwear_needed`
  - `rain_protection_needed`
  - `uv_protection_needed`
  - `shoe_constraints`
  - `styling_hints`

### Recommendation Engine
- The engine builds bounded outfit candidates from the actual wardrobe
- It scores each candidate with deterministic rules across weather, style, color, occasion, and preference

### Explainable Outfit Reasoning
- StyleSnap does not only rank looks
- It also explains why a look works, how it scored, and what risks or warnings remain

## 7. System Architecture

### Frontend
- React + Vite + TypeScript + TailwindCSS + React Router
- Route-level pages:
  - landing
  - wardrobe
  - add item
  - edit item
  - recommendation
- UI decomposition:
  - upload panel
  - weather context panel
  - recommendation form
  - outfit carousel
  - result cards

### Backend
- FastAPI + SQLAlchemy 2 + Pydantic + SQLite
- Stable API surface for:
  - clothes CRUD and mock analyze
  - weather skill
  - outfit recommendation

### Replaceable Service Boundaries
- `ai_vision_service.py`
- `weather_service.py`
- `recommendation_service.py`
- `scoring_service.py`
- `outfit_reasoning_service.py`

The MVP keeps these adapters mockable and deterministic so the product can be demoed without external vendors or secrets.

## 8. Recommendation Logic

### Scoring Formula
```txt
OutfitScore =
0.30 * Weather Fit
+ 0.25 * Style Match
+ 0.20 * Color Harmony
+ 0.15 * Occasion Fit
+ 0.10 * User Preference
```

### Score Dimensions
- `Weather Fit`
  - measures whether thickness, layering, outerwear, rain suitability, UV coverage, and shoe choice match the current outfit context
- `Style Match`
  - measures alignment between wardrobe tags and the requested target style
- `Color Harmony`
  - measures whether the selected color combination stays cohesive and practical
- `Occasion Fit`
  - measures whether the chosen items and style cues suit the requested occasion
- `User Preference`
  - measures whether the outfit reflects optional preferences such as comfort, warmth, reduced formality, or a cleaner silhouette

### Recommendation Strategy
- load persisted wardrobe data
- build bounded outfit candidates
- score every candidate deterministically
- sort and return the top 2-3 Looks
- attach reasoning and warnings for explainability

## 9. Weather Skill
Weather is not the main product feature. It is modeled as a contextual skill that converts raw weather signals into outfit-aware constraints, such as layering needs, rain protection, UV protection, material suggestions, and shoe constraints.

天气不是 StyleSnap 的主功能，而是穿搭推荐的环境上下文能力。Weather Skill 会将温度、降雨概率、风速、湿度和紫外线等信息转化为穿搭推荐可用的约束和提示，例如是否需要外套、是否需要防雨鞋、是否建议防晒、是否避免麂皮材质等。

In the MVP, weather data and location resolution are mocked. The provider seam is kept explicit so real weather and geocoding services can replace the mock layer later.

## 10. Image Upload UX
On mobile, users can add clothing by taking a photo or selecting from their album. On desktop, users can upload or drag-and-drop an image. In the MVP, uploaded images are previewed locally and passed to the mock vision service for metadata generation. Future versions can replace this with Supabase Storage or S3.

Additional Phase 5 / 6 upload constraints:
- file type must start with `image/`
- file size must be `<= 5MB`
- URL input remains available only as a demo fallback, not the primary user entry

## 11. API Overview

### Health
- `GET /health`

### Clothes
- `POST /api/clothes`
- `GET /api/clothes`
- `GET /api/clothes/{id}`
- `PUT /api/clothes/{id}`
- `DELETE /api/clothes/{id}`
- `POST /api/clothes/analyze`

### Weather Skill
- `GET /api/weather?city=...`
- `GET /api/weather/current?lat=...&lon=...`

### Recommendation
- `POST /api/outfits/recommend`

### API Notes
- clothes analyze remains mock-only in the MVP
- weather remains mock-only in the MVP
- recommendation responses include score breakdown, reasoning, warnings, and meta information
- backend contracts stay stable across the current demo phases

## 12. Local Development

### Backend
```bash
cd backend
uv venv .venv --python 3.13
uv pip install --python .venv/bin/python --index-url https://pypi.tuna.tsinghua.edu.cn/simple -r requirements.txt
.venv/bin/python -m uvicorn app.main:app --reload
```

### Frontend
```bash
cd frontend
npm install
npm run dev
```

### Demo Seed Data
- The backend inserts demo wardrobe items when the clothes table is empty
- Seed insertion is guarded to avoid duplication
- Backend tests disable seed behavior for isolation

## 13. Test Commands
```bash
cd frontend
npm run build

cd ../backend
pytest
```

If `pytest` is not available on `PATH`, use:

```bash
cd backend
.venv/bin/python -m pytest
```

## 14. Demo Flow
Recommended interview or screen-recording flow:
1. Open the landing page and explain the product in one sentence
2. Go to `Wardrobe`
3. Open `Add Item` and show mobile/desktop upload-first UX
4. Run Mock AI analyze and show that metadata remains editable
5. Save the item and return to wardrobe
6. Open `Recommendation`
7. Use location or city fallback to resolve Weather Skill context
8. Choose occasion, target style, and optional preference text
9. Generate Looks
10. Switch between Look cards and explain score breakdown, reasoning, and warnings

## 15. Privacy Notes
- StyleSnap is currently a single-user local MVP
- The MVP does not send wardrobe data to third-party AI services by default
- Uploaded images are previewed locally in the frontend during the current session
- The MVP does not yet provide cloud asset persistence, auth, or multi-user isolation
- No API keys are required for the current demo loop
- Users should understand that current uploaded preview behavior is local-demo oriented rather than production-grade storage

## 16. Mock-to-Real Roadmap

| MVP Mock Layer | Future Real Service |
|---|---|
| Mock Vision Service | GPT-4o / Gemini Vision / Qwen-VL / InternVL |
| Local Preview Image | Supabase Storage / S3 |
| Mock Weather Provider | OpenWeatherMap / 和风天气 / 高德天气 |
| Mock Location Resolver | 高德 / Google / Mapbox reverse geocoding |
| Rule-based Scoring | LLM-assisted stylist reasoning + learning-to-rank |
| Template Explanation | LLM-generated personalized explanation |

## 17. Portfolio Description
Designed and implemented StyleSnap, an AI personal outfit assistant that transforms uploaded clothing images into a digital wardrobe and generates explainable daily outfit recommendations using weather context, style goals, occasion constraints, color harmony, and user preferences.

The project demonstrates a complete AI product loop: wardrobe digitization, context-aware recommendation, rule-based scoring, explainable reasoning, responsive UX, and mock-to-real service architecture.

设计并实现 StyleSnap，一款基于个人衣橱的 AI 每日穿搭助手。用户可通过拍照或相册上传衣物构建数字衣橱，系统结合天气上下文、目标风格、今日场景、色彩搭配和个人偏好，生成可解释的每日穿搭推荐。

项目展示了从用户痛点、AI 能力拆解、推荐评分设计、Weather Skill 封装，到移动端/PC 端适配 Demo 的完整 AI 产品闭环。

## 18. Future Roadmap
- replace mock vision with real multimodal clothing understanding
- persist wardrobe images through production storage
- replace mock weather and mock location resolution with real providers
- add richer preference modeling and stylist personalization
- introduce LLM-assisted explanation or reranking after privacy boundaries are defined
- migrate from SQLite to PostgreSQL or Supabase in production environments
- add auth and ownership isolation in a dedicated multi-user phase

## 19. Deployment Notes

### Frontend
- Vercel
- Netlify

### Backend
- Railway
- Render
- Fly.io

### Database
- SQLite for local MVP
- PostgreSQL or Supabase for production

### Storage
- Local preview for MVP
- Supabase Storage or S3 for production

### Deployment Positioning
- The current repository is deployment-aware but still MVP-oriented
- Production deployment should be paired with:
  - auth and user ownership
  - persistent asset storage
  - environment-managed secrets
  - production database migration
  - privacy and lifecycle policies for wardrobe images
