# Portfolio Polish Test Plan

## Build Tests
- `cd frontend && npm run build`
- `cd backend && pytest`

## Manual Acceptance
- Landing Page 首屏能看懂产品
- Hero 区能一眼看出这是基于个人衣橱的 AI 每日穿搭助手
- CTA 能进入 Wardrobe 和 Recommendation
- Landing Page 的 Problem / Solution / AI Capability / Demo Flow / Roadmap Preview 区块完整
- Add Item 上传体验正常
- Recommendation Flow 正常
- Look carousel 正常
- PC 端页面可读
- 手机端页面可读
- README 能独立说明项目
- README 能说明 mock 与 future real service 的关系
- 不存在明显旧的紧凑评分维度命名残留
- 不存在将天气误描述为主功能的问题
- 不存在 API key 泄露
- 不存在上传隐私误导
- 明确说明本地 preview 为 MVP 限制

## Naming And Copy Audit
- Search for legacy compact score wording
- Search for weather-utility framing
- Search for weather-dominant product framing
- Search for misleading “weather-first” framing
- Verify revised copy still preserves the documented scoring formula where needed

## Security And Privacy Audit
- No real third-party provider calls introduced in this phase
- No API keys or tokens checked into docs or code
- No README copy implies cloud upload already exists
- No README copy implies user login or multi-user isolation exists

## Exit Criteria
- Frontend build passes
- Backend regression tests pass
- Landing page is screenshot-ready
- README is portfolio-ready
- Current specs and archive are updated
