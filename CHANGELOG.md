# Release notes

## 1.2.0 — 2026-10-04

- Replace the unsupported `.codex/plugin.json` with a portable root manifest and a repository marketplace. Use actual publisher metadata and an original package icon.
- Retain the four public skill names; rename their source folders to match. Add explicit-only Codex policy to every skill and correct invocation/installation documentation.
- Scope the video skill to a production blueprint by default. Distinguish generation, assembly, export, and actual review when production is requested.
- Preserve supplied script/audio, derive timing from narration, remove conflicting scene counts, and add a timeline contract and arithmetic validator.
- Add factual research and analogy boundaries while keeping connected, curious storytelling. Treat the narrative structure and Cosmic Curiosity styling as adaptable project conventions.
- Replace static/loop filler with explanatory motion, asset continuity, verified loop boundaries, tool-specific adaptation, and voice-led mixing/review.
- Add an illustrative handoff, regression cases, packaging checks, and CI. Record structural validation separately from host activation and audiovisual testing.

### Migration

Skill source paths change from `skills/script`, `skills/art`, `skills/animation`, and `skills/video` to `skills/nutshell-*`. Existing installed copies do not update automatically. Use the README's source-refresh instructions after publishing; resolve duplicate standalone/plugin skills deliberately. No service integrations or credentials are required by this package.

### License status

No reuse license was present in the source repository. No new license grant is added by this release; the owner can choose one in a later change.
