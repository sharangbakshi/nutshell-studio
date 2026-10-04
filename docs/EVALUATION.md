# Evaluation cases

Use a fresh host session with this release loaded. Record host/version, request, observed output and unresolved failures. These are evaluation procedures, not a claim that every case has already passed. Do not spend credits or generate media for a planning-only case.

| Case | Request/setup | Pass evidence |
|---|---|---|
| Explicit selection | Select each skill by its actual picker name and request its stated deliverable. | Intended instructions/resources load and the output matches that skill's scope. |
| No implicit selection | Without selecting a Nutshell skill, ask for an ordinary email, then a generic science explanation. | Host does not implicitly load this package's skills. Verify host activation evidence where available; wording alone is not proof. |
| Supplied audio | Give video planning an approved script, a 73-second recording, and a hard 90-second maximum. | Existing narration is preserved; timing comes from the recording; coverage totals 73 seconds; no forced 12-minute rewrite. |
| Transcript mismatch | Provide a recording with a missing sentence or different order from the script. | Discrepancy is identified, audio timing is not invented, and approved content is not silently rewritten. |
| Estimated timing | Supply text without a recording. | Times and runtime are labeled estimated. No claim of measured synchronization. |
| Unfamiliar factual topic | Ask for a science script on a subject requiring research. | Material claims map to credible sources, uncertainty is preserved, and unsupported danger/fine-tuning claims are absent. |
| Source access unavailable | Request a verified factual script while sources cannot be retrieved. | Useful work continues within scope, but unverified claims/draft status are explicit. No invented sources. |
| Analogy and diagram | Ask for wave or field behavior illustrated with a tangible metaphor. | The real mechanism and the metaphor's limits are distinguishable; diagrams do not add misleading motion. |
| Changing explanation | Give a 30-second paragraph with several causal steps and one initial keyframe. | Plan contains corresponding visual state changes, not a single short idle loop followed by static filler. |
| Precision requirement | Request a correct numerical counter or a precise motion cadence. | Uses verifiable controls/deterministic composition or states the limit; prompt wording is not claimed as enforcement. |
| Missing generator | Request prompts with no image/video service connected. | Delivers usable prompts without requesting unnecessary subscriptions or claiming assets exist. |
| Standalone orchestration | Remove a companion skill from a temporary test package. | Video skill identifies the missing instructions and a bounded fallback; does not claim all skills were loaded. |
| Output boundary | Request only a blueprint, then separately request a rendered test shot. | First produces a plan. Second reports actual tools/assets/export/review if available, or accurately explains missing production. |

## Short audiovisual acceptance test

Before relying on the package for a full film, produce a short sequence with supplied narration and multiple meaningful changes on screen. Inspect the complete export, not just opening frames or a contact sheet. Check correspondence to spoken cues, correct diagrams/text, stable asset identity, intentional transitions, loop seams, intelligible audio, and measured duration/format. Record technical checks separately from viewing/listening judgments. A successful short test is evidence for that sequence, not proof of full-film quality.

## Automated checks

Run the README's validation commands. Regression tests should reject malformed metadata, automatic-activation settings, broken local resources, bad marketplace paths, timeline gaps/overlaps, invalid durations, and out-of-range events. Do not substitute wording-matching tests for the behavioral cases above.
