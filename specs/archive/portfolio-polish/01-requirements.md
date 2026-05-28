# Portfolio Polish Requirements

## Feature Goal
Turn StyleSnap into a portfolio-ready and launch-readable AI product demo without expanding core feature scope.

## Functional Requirements
1. The landing page must clearly communicate the product positioning:
   - `StyleSnap：基于个人衣橱的 AI 每日穿搭助手`
   - slogan: `用你已有的衣服，搭出今天最适合的 Look。`
   - English subtitle: `An AI outfit assistant powered by your personal wardrobe, weather context, style goals, and occasion needs.`
2. The landing page must explain the core product problem.
3. The landing page must explain the end-to-end solution loop.
4. The landing page must include an AI capability breakdown section.
5. The landing page must include a clear CTA to:
   - build wardrobe
   - generate today’s look
6. The landing page must include a demo flow section.
7. The landing page must include a roadmap preview section.
8. The landing page must remain screenshot-friendly on mobile and desktop.
9. README must include a complete project introduction suitable for interview review.
10. README must include:
   - Project Overview
   - Target Users
   - Product Problem
   - Core User Flow
   - MVP Features
   - AI Capability Design
   - System Architecture
   - Recommendation Logic
   - Weather Skill
   - Image Upload UX
   - API Overview
   - Local Development
   - Test Commands
   - Demo Flow
   - Privacy Notes
   - Mock-to-Real Roadmap
   - Portfolio Description
   - Future Roadmap
   - Deployment Notes
11. README must include the required bilingual overview copy for StyleSnap.
12. README must include the recommendation scoring formula and explain each score dimension.
13. README must state that Weather Skill is contextual capability rather than the main product.
14. README must state the MVP upload/storage limitation:
   - local preview only
   - no real object storage yet
15. README must include mock-to-real upgrade mapping for:
   - vision
   - storage
   - weather provider
   - location resolver
   - scoring
   - explanation
16. README must include deployment suggestions for frontend, backend, database, and storage.
17. Phase 6 must audit global naming and copywriting for outdated or misleading phrasing.
18. The codebase and docs must not leave obvious residual phrasing such as:
   - framing weather as the primary product
   - framing the app as a weather utility
   - legacy compact score-dimension naming
19. The implementation must not re-open or change core backend contracts for:
   - clothes API
   - weather API
   - recommendation API
20. `specs/current/` must be updated to reflect final accepted product state after archive.
21. `specs/archive/lessons-learned.md` must be updated with Phase 6 conclusions.

## Manual Product Messaging Requirements

### Landing Page Sections
- Hero Section
- Problem Section
- Solution Section
- AI Capability Breakdown
- Demo Flow Section
- Roadmap Preview

### AI Capability Breakdown Items
1. Wardrobe Digitization
2. Weather Skill
3. Recommendation Engine
4. Explainable Outfit Reasoning

## Deployment Notes Requirements
- Frontend suggestions:
  - Vercel
  - Netlify
- Backend suggestions:
  - Railway
  - Render
  - Fly.io
- Database suggestions:
  - SQLite for local MVP
  - PostgreSQL or Supabase for production
- Storage suggestions:
  - local preview for MVP
  - Supabase Storage or S3 for production

## Non-Goals
- No real AI Vision integration
- No real weather API integration
- No real object storage integration
- No virtual try-on
- No user login
- No payments
- No community features
- No complex animation system
- No backend scoring rewrite
- No major route or data model expansion
