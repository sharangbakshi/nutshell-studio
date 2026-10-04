---
name: nutshell-animation
description: Plan or animate explanatory 2D shots from narration and approved artwork, specifying meaningful visual events, continuity, timing, and tool-adapted motion prompts. Use for shot choreography rather than treating still images or prompts as a finished film.
---

# Nutshell Animation

Make the explanation happen on screen. A viewer should be able to connect each important spoken idea to an observable change, comparison, interaction, or demonstration. Preserve the user's approved art and narration. Default to Cosmic Curiosity's geometric 2D illustrated direction, while selecting motion that serves the subject rather than claiming that one cadence defines a reference studio.

## Read the handoff

Use the approved shot/art specification and inspect the actual source asset when available. Retain the shot `id`, `sequence_id`, `narration.text`, `asset_ids`, `visual_purpose`, `claim_ids`, palette roles, and `incoming_state`/`outgoing_state`. The corresponding asset's `source` identifies the approved keyframe or layered file; do not silently replace it. Identify whether it is a flat raster, separable layers, or editable vector geometry before choosing a technique.

Use supplied audio as the timing authority. Preserve shot `start`/`end` and project `timing.status`/`timing.basis`. All shot and event times are **global seconds** in the film. When no recording is available, mark timing estimated; when a script and audio differ, identify the discrepancy rather than quietly retiming against invented speech. Do not rewrite approved narration or assume that a new voiceover should be generated. A standalone untimed motion concept may omit numerical bounds rather than invent a film timeline.

Clarify the requested output through context: a choreography specification, copyable prompts, a rendered shot, or an edited sequence. Do not expand prompt-only work into paid generation or claim that a motion prompt is an exported clip.

## Choreograph the explanation

For each shot, lay out `events` with global `start`/`end`, a `narration_cue` quoting the matching words, and an `action` that states the visible event and its explanatory purpose. If a tool needs local shot time, derive it by subtracting the shot's `start`; do not mix local and global coordinates in the handoff. Explicitly identify intentionally held intervals instead of leaving unexplained gaps.

Useful event types include:

- **Reveal:** introduce a field, label, hidden component, or changed viewpoint when the narration establishes it.
- **Demonstrate:** make a quantity vary, a causal interaction occur, or a mechanism evolve through legible states.
- **Compare:** hold a baseline while changing one relevant property; align the comparison spatially and temporally.
- **React:** let a character's gaze and posture direct attention or register a discovery.
- **Resolve:** complete the event, allow a readable pause, then carry a visual anchor into the next shot.

A repeated background loop or still frame may support concentration, but cannot substitute for new explanatory action while the narration advances. A deliberate still moment can be useful; duration must follow its purpose. If the available clip is shorter than the explanation, design additional connected shots, build the missing deterministic animation, or report incomplete coverage. Do not stretch a clip through indiscriminate repetition.

## Motion language

- Use anticipation, acceleration, controlled overshoot, and settling selectively for expressive acting and interface-like reveals. Avoid universal bounce or fixed overshoot percentages.
- Give physical diagrams the motion their mechanism requires. Constant velocity, conserved quantities, phase relationships, and measured comparisons must not acquire decorative easing, elastic deformation, or arbitrary acceleration.
- Choose smooth or stepped animation deliberately. Delivery frame rate and the frequency at which artwork changes are separate decisions; a 12-frame-per-second aesthetic is optional, not something prompt wording guarantees.
- Favor locked compositions, flat tracking/pedestal moves, readable push-ins, match cuts, masked reveals, and scale transitions. Use camera movement to answer an explanatory need. Preserve flat geometry when that is the approved style; avoid unintended perspective distortion or identity morphing.
- Keep secondary motion quieter than the explanatory event. Facial acting and purposeful prop interaction provide more life than perpetual body bobbing. Avoid rapid repetitive flashes; use shape, contrast, and motion to make impacts readable.

Choose transformations that can actually be produced from the assets. A flat image cannot supply hidden geometry or independently moving components merely because a prompt names them. For exact diagrams, text, counters, trajectories, or synchronization, use deterministic 2D animation/compositing where available. Keep decorative effects separate from the scientific claim.

## Continuity and transitions

Carry the same asset identity, semantic colors, spatial orientation, and scale anchors between shots. Record the `outgoing_state` and the next `incoming_state`. Explain whether a `transition` preserves continuity, changes scale, enters a cutaway, or intentionally marks a new setting. A wipe or camera flourish should not obscure the instant at which a causal change occurs.

For looping elements, specify the period and endpoint agreement for position, rotation, deformation, camera, lighting, and phase. Compare motion approaching and leaving the seam, not just two similar still frames. Render several consecutive repetitions and inspect them before calling a loop seamless. If it fails, repair the seam or use a different shot; avoid crossfades that imply false scientific overlap.

## Output and tool adaptation

Deliver a compact shot plan containing the handoff fields above, timed `events`, camera, desired cadence/delivery frame rate, actual or planned technique, and loop use if any. Add layer requirements where the approved art needs preparation. Preserve an existing timeline's schema and IDs; a readable table is sufficient for isolated prompt work.

Then adapt the specification to the chosen tool. Verify supported duration, source-image controls, aspect ratio, timing controls, and whether audio is generated. Do not assume a universal provider syntax or fixed clip length. For a generation prompt, describe the subject's ordered action, unchanged identifying features, controlled secondary movement, camera, and final state. Keep exact time-critical labels and scientific relationships under verifiable controls.

If a tool is unavailable or cannot satisfy a required action, say what remains unproduced and offer a viable available technique or the prompt/specification. Tool names do not imply access, credits, or successful execution.

## Review actual motion when produced

Inspect the entire delivered shot or sequence, including transitions and repeated loops, against the narration. Check whether each claimed event appears at the right time, source identity remains stable, scientific relationships survive motion, and labels stay legible. Verify encoded duration/frame rate and audio sync when exporting. A contact sheet cannot verify motion or a loop seam; technical metadata cannot establish viewing quality. Report the actual review scope and any unresolved defects. A shot-level review is not a complete-film review.
