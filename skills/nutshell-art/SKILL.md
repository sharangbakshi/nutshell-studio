---
name: nutshell-art
description: Design Cosmic Curiosity educational illustrations, style frames, and keyframe prompts with a consistent visual language and clear animation handoffs. Use for art direction or visual assets rather than scriptwriting or finished video assembly.
---

# Nutshell Art

Create beautiful, readable illustrations that explain the narrated idea. The default **Cosmic Curiosity** direction is this project's own convention: geometric forms, expressive original characters, expansive compositions, dark cosmic fields, and carefully placed bright accents. It is not a claim about universal rules used by a reference studio. Honor the user's approved style, aspect ratio, assets, and topic when they call for a different treatment.

## Establish the actual deliverable

Identify whether the request needs art direction, copyable prompts, generated raster keyframes, or editable vector/layered assets. Prompts are a deliverable, but they are not generated images. A raster image with a vector-like appearance is not editable vector geometry. Name the format and what can actually be animated independently.

Read supplied narration/storyboard and inspect available approved references. When a shot has measured audio timing, retain it. When only a scene description or script exists, mark timing as estimated; omit unsupported numerical timings rather than invent audio synchronization. If the request is only for prompts, provide them without requiring access to a generation service.

## Visual direction

- **Shape:** Use a small vocabulary of circles, arcs, tapered beams, pill shapes, clean polygons, and purposeful silhouettes. Favor flat fills and selective stepped shading. Avoid photorealistic texture, decorative surface noise, and accidental 3D rendering in this default direction. A justified gradient or different treatment may serve a user-approved concept; it is not forbidden by an alleged studio rule.
- **Hierarchy:** Give the viewer one dominant subject or relationship per beat. Preserve negative space for motion and labels. Use selective contrast and scale before adding more detail. Frame small subjects against vast systems when scale is the point.
- **Color:** Start with deep navy `#0B0F2A` or violet-black `#120D31`, structural blues/teals `#1E3A5F` and `#2A4365`, and a restrained focal accent such as yellow `#FFDF00`, cyan `#00F0FF`, or magenta `#FF007F`. A roughly 60/30/10 hierarchy is an optional composition aid, not a measurable guarantee or requirement. Assign colors semantic roles and preserve them across shots. Do not rely on color alone to distinguish scientific quantities.
- **Line and texture:** Choose either clean silhouettes or consistent selective outlines. Keep outline weight appropriate to final size. Detail should survive viewing at delivery resolution rather than merely reward zooming into a still.
- **Characters:** Create an original silhouette, face, proportions, and accessory language. Record a character's identifying features before varying pose. Express curiosity through gaze, posture, and reaction; do not use a reference channel's signature mascot by default.

Vary composition according to the explanation. Useful starting points include a tiny observer beneath a vast system, a front-facing cutaway, a spatial scale comparison, a close-up experimental apparatus, a before/after pairing, and an isolated microscopic interaction. Do not force every shot into the same template. Use common visual anchors to make changes of scale or viewpoint understandable.

## Draw the mechanism faithfully

State what each explanatory image should let the viewer infer about the mechanism. Retain any claim/source IDs from the script's research. Check directions, relative relationships, labels, quantities, and comparison baselines against those claims. If sources are absent for a material scientific assertion, flag the needed verification rather than certify the image as accurate.

Separate literal mechanism from metaphor. State the analogy's useful correspondence and where it stops; mark schematic or not-to-scale diagrams when their omission would mislead. Decorative particle paths, rings, collisions, and glow must not imply an unsupported mechanism. Use deterministic drawing/diagram tools for geometry, labels, counts, or relationships that must be exact; generative imagery can supply atmosphere and illustrative elements.

## Preserve continuity and make animation possible

Maintain a compact shared asset register with `id`, `kind`, `status`, and `source` (actual file/reference when available; explicitly planned otherwise). Record identifying features, semantic palette roles, and approved version alongside the register. Reuse approved designs. A prompt must not silently substitute a new character or scientific diagram for an established one.

Plan separable elements when motion needs them: background, subject, mechanism components, labels, foreground, and masks. Decide which elements are delivered as layers/vector objects versus a single flattened image. For a key transformation, choose useful incoming, intermediate, or outgoing frames; do not manufacture checkpoint counts unrelated to the narration.

Use these handoff names, which also map into the video skill's timeline contract:

| Field | What to record |
|---|---|
| Shot `id`, `sequence_id`, `narration.text` | Stable IDs and exact spoken words explained |
| `start`, `end`; project `timing.status` and `timing.basis` | Global seconds if available; estimated until based on the actual recording |
| `visual_purpose`, `claim_ids` | Explanatory relationship, relevant research claims and caveats |
| `asset_ids`; asset `source` | Register IDs and approved source keyframe file, or explicitly planned asset |
| `incoming_state`, `outgoing_state`, `transition` | Visible state and connection to adjacent shots |
| `events` | Intended reveals/interactions with `action`, `narration_cue`, and global `start`/`end` only when known |

Add a short art specification for composition, palette roles, raster/vector/layered delivery, size/aspect, separable elements, and labels. A standalone untimed concept need not invent a complete film timeline. If contributing to an existing timeline, preserve its IDs and time coordinate system rather than producing a competing schema.

## Produce and review

Write the tool-neutral scene specification first. A useful prompt orders information as subject and action → explanatory relationship → composition → established identity/palette → visual treatment → delivery framing. Adapt it to the selected provider's verified controls rather than hardcoding model versions or promising that prompt language enforces exact geometry.

When generation is requested and tools are available, create the assets, inspect the actual results, and revise visible errors. Compare continuity, focal clarity, scientific relationships, cropping, and legibility at intended viewing size. Use an editor for exact labels if generated text is unreliable. Report which images were reviewed and which are only planned. If generation is unavailable, deliver the usable specification and identify the missing capability; do not claim an image was produced.
