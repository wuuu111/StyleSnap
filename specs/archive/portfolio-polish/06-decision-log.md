# Portfolio Polish Decision Log

## Decision 1: Do Not Add New Core Features In Phase 6
- Decision:
  - Keep Phase 6 focused on portfolio polish, launch-readiness notes, and presentation quality.
- Why:
  - The core AI demo loop is already complete.
  - More features would add regression risk and weaken the clarity of the product story.
- Alternatives Rejected:
  - Adding more recommendation logic
  - Adding auth, cloud storage, or richer AI integrations during the polish phase
- Future Extension:
  - New capability work should happen in later explicitly scoped phases.

## Decision 2: Prioritize Portfolio Communication
- Decision:
  - Spend the phase on landing-page clarity, README depth, demo narrative, and roadmap framing.
- Why:
  - Portfolio reviewers evaluate product framing, architecture thinking, and execution quality, not just raw feature count.
- Alternatives Rejected:
  - Treating the repo as developer-only documentation
  - Leaving the homepage and README in an internal-demo state
- Future Extension:
  - The same content can later be adapted into a portfolio site, case study, or slide deck.

## Decision 3: Keep Mock Providers In Place
- Decision:
  - Preserve mock vision, mock weather, local preview, and deterministic reasoning for the MVP.
- Why:
  - The mock stack keeps the demo reproducible, private, and runnable without external dependencies.
  - The architecture already exposes replaceable seams for future production services.
- Alternatives Rejected:
  - Partially integrating one real provider during a documentation phase
- Future Extension:
  - Replace mocks through dedicated provider-integration phases without changing the user-facing flow.

## Decision 4: Put Real Service Integration Into The Roadmap
- Decision:
  - Document production upgrades instead of implementing them now.
- Why:
  - It demonstrates product maturity and systems thinking without destabilizing the working MVP.
- Alternatives Rejected:
  - Hiding production gaps
  - Overpromising a production architecture without clear migration steps
- Future Extension:
  - Roadmap items can become later scoped phases with independent test plans.

## Decision 5: Defer Login And Cloud Storage
- Decision:
  - Do not add login or storage infrastructure in Phase 6.
- Why:
  - These are real production concerns, but they are outside the polish-only scope of this phase.
  - They would require broader backend, deployment, and privacy changes than this phase should absorb.
- Alternatives Rejected:
  - Minimal auth scaffolding without real ownership semantics
  - Ad hoc object storage without a complete upload lifecycle
- Future Extension:
  - A production version should add user ownership, secure asset storage, and lifecycle cleanup.

## Decision 6: Document What Production Still Needs
- Decision:
  - Explicitly list future needs such as real multimodal analysis, weather providers, persistent storage, auth, deployment hardening, and production database upgrades.
- Why:
  - A portfolio project is stronger when it is honest about what is demo-ready versus production-ready.
- Alternatives Rejected:
  - Presenting the MVP as if it were already production-complete
- Future Extension:
  - The documented gaps become the acceptance criteria for a future launch-oriented phase.
