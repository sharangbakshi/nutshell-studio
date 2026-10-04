# Release 1.2.0 verification

Review date: 2026-10-04. Source checkout started clean at `109624ad5cac496475440593d3317d929cd0b939`. Changes are intentionally uncommitted for the owner to review and push.

## Scope

This is a repository/skill update. No film, narration, or generated media was produced. No paid provider was called. The existing personal skill installation was not replaced, and no repository changes were pushed.

## Verified

- Codex CLI `0.159.0-alpha.12.1` accepts the documented marketplace/add command syntax.
- Read-only plugin discovery with command-local marketplace configuration resolves `nutshell-studio@nutshell-studio`, version `1.2.0`, from this checkout. It reports `installed: false` and `enabled: false`; this is package discovery, not installation or activation testing. No persistent marketplace configuration was written.
- All four source folders match their declared skill names and contain explicit-only `agents/openai.yaml` policies.
- The 18-second illustrative timeline passes the helper. Its timing is explicitly estimated; the helper does not open or measure audio.
- The portable manifest passes the published Agent Plugins 1.0.0 JSON schema, fetched from its versioned URL.
- All four skills pass the bundled official `quick_validate.py` structural validator.
- Repository validation passes: manifest/catalog wiring, exact skill folder/name set, boolean explicit-only policies, icon/resources, Markdown links/fences and timeline fixture.
- All **26 regression tests** pass: nine packaging cases and seventeen timeline cases. They cover malformed metadata, missing policies/resources, incorrect paths, duplicate JSON keys, invalid numbers, duration/coverage errors, event containment and register references.
- Independent read-only review found a duplicate-JSON-key inconsistency between the package validator and timeline CLI. Both now reject overwritten fields; two regressions cover the repair. No other actionable finding was reported in that review's scope.
- `git diff --check` passes. A separate scan of new text files found no trailing whitespace or missing final newlines.

## Scenario review

An independent agent exercised two planning scenarios against the revised instructions:

- Text-only fictional counting machine: preserved the supplied words, produced seven estimated shots covering a requested 45 seconds, separated deliberate silence, and marked assets planned and claims illustrative. Its JSON passed the timeline helper. No audio or visuals were generated.
- Claimed locked 73-second MP3 under a 90-second ceiling, with neither file actually accessible in the test: treated duration as user-reported, preserved the approval constraints, and provided a partial handoff rather than inventing measured timings or narration.

The review prompted two clarifications: video planning can start from approved text as well as a recording; the timeline's duration field is a proposed track duration when estimated. Incomplete inputs now explicitly call for a prose partial handoff rather than placeholder JSON. These scenarios do not establish host activation behavior, factual research performance, or audiovisual quality.

## Audit-to-change map

| Audit concern | Resolution |
|---|---|
| Activation, fake slash registration, folder naming | Four canonical `nutshell-*` folders and explicit-only policies; supported picker/mention guidance. |
| Invalid manifest and absent marketplace | Portable root manifest, publisher metadata, original icon and repo catalog; CLI discovery verified. |
| Cross-platform and end-to-end overclaims | Tested/unverified surface table; blueprint scope; separate planned/generated/assembled/exported/reviewed states. |
| Runtime math, inconsistent scene counts, audio preservation | No fixed shot count; actual recording controls timing; estimates explicitly labeled; timeline arithmetic checks. |
| Research, forced scientific stakes, misleading analogies | Evidence register, source review, uncertainty and bounded analogies; adaptable causal story structure. |
| Exact punctuation pauses and fixed audio percentages | Separate direction metadata; measured speech and actual-mix review; no enforcement claim from punctuation or sliders. |
| Static/loop filler and missing synchronization | Timed explanatory events, intentional holds, explicit transitions and complete narration coverage. |
| Prompt guarantees, alleged universal studio rules, provider lock-in | Project art preset and design targets; raster/vector distinction; tool-neutral planning plus verified tool adaptation. |
| Continuity and orchestration | Shared asset/claim/shot contract; explicit sibling references and missing-resource fallback. |
| Missing examples and acceptance checks | Original illustrative examples, evaluation cases, validators, regressions and CI workflow. |
| README formatting, upgrades and license | Closed fences, actual commands, migration guidance and explicit undecided license status. No license grant was invented. |

## Not established by these checks

- Fresh-session installation, picker interaction, and implicit/explicit activation behavior in each host.
- Installation from GitHub after the owner pushes this release, or successful GitHub Actions execution on the remote service.
- ChatGPT web distribution or Claude Code compatibility.
- Quality of generated illustrations, true motion, speech synchronization, audio mixing, or a complete exported film. Those require an actual production and the audiovisual evaluation in [EVALUATION.md](EVALUATION.md).

The original examples demonstrate the contract and writing choices; they are not user-approved work or evidence that an audience will prefer the result.
