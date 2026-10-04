---
name: nutshell-video
description: Plan narrator-led educational animation from a topic or approved script and audio, coordinating research, art, timed motion, and production handoffs; execute generation and editing only when requested and supported by available tools.
---

# Nutshell Video

Create a coherent educational film in which the visuals explain the spoken idea. The default deliverable is a **production blueprint**. If the user requests a finished video, continue into generation, assembly, export, and review using available tools; never describe a script, prompt package, or storyboard as a rendered film.

## Establish the brief and preserve inputs

- Inventory the topic, audience, runtime limit, deliverable, approved script, supplied audio, art references, existing assets, and tools. Use what the user has already specified; ask only for consequential missing information.
- Preserve approved narration and recordings. If text and audio disagree, document the discrepancy and align to the recording unless the user authorizes an edit. Do not replace supplied audio, subscribe to a service, or assume credits are available.
- Honor the requested duration. If none is given, target at most 12 minutes; do not pad a shorter explanation to reach it. With fixed audio, measure duration first. If it exceeds a hard limit, surface the conflict and continue unaffected planning without silently cutting or accelerating it.
- Mark timing **estimated** until based on an actual recording. Reading-speed calculations are planning estimates, not measured narration. Keep approved originals alongside derivatives.

## Coordinate the specialist work

For a new or revised script, read [Nutshell Script](../nutshell-script/SKILL.md). For art direction and keyframes, read [Nutshell Art](../nutshell-art/SKILL.md). For shot choreography and animation, read [Nutshell Animation](../nutshell-animation/SKILL.md). Consult each when its work is needed; an approved script need not be rewritten. Reuse their research, asset, and motion decisions rather than producing competing versions.

These are sibling skills in the complete bundle. If one is absent in a standalone installation, say which guidance is unavailable. Use the self-contained requirements below for a bounded plan; request the missing skill only when its specialized capability is necessary. Never claim to have loaded an unavailable resource.

## Develop the blueprint

1. **Research and thesis.** For new scientific content, establish a causal explanation and record consequential claims with authoritative sources, qualifications, and unresolved questions. An existing approved script remains an input, not a guarantee of scientific accuracy: flag material issues for correction. Check depicted mechanisms as well as words. Do not manufacture danger, fine-tuning, or cosmic stakes to fill a narrative template.
2. **Narrative and visual beats.** Split the recording or approved text into explanatory sequences and shots according to its ideas, not a fixed scene count. Transcribe or align exact narration spans; record boundary uncertainty. Text-only timing remains estimated. Each beat needs a visual purpose: reveal a relationship, demonstrate a process, compare alternatives, change scale, resolve a question, or provide an intentional emotional pause.
3. **Art and assets.** Use a coherent original art preset and a reusable asset register. Specify palette roles, shapes, proportions, typography, spatial relationships, and recurring identities. Distinguish raster keyframes from editable vector/layered assets. A prompt cannot guarantee geometry, legible text, or identity continuity. Reference an approved keyframe by its asset ID; record actual approval status.
4. **Timed choreography.** Map every explanation to visible events at the relevant audio time. Define incoming and outgoing states, focal point, movement, labels, transitions, and what changes for the viewer. Use the [timeline contract](references/timeline-contract.md) when preparing a timed handoff. Account for the whole recording, including intentional silence. Do not fill uncovered time with a default still, repeated loop, or alternating camera angle while new concepts continue in narration.
5. **Tool adaptation.** Start with tool-neutral visual specifications, then adapt to the chosen model/editor's verified controls and available budget. Check supported duration, aspect ratio, reference images, layers, audio behavior, and frame-rate controls. Separate animation cadence from delivery frame rate. Label prompt requests as targets until output inspection verifies them.
6. **Assembly and sound.** Specify transitions and asset trim points at exact timeline positions. Plan the full duration rather than assuming every tool returns a fixed clip length. Preserve speech intelligibility, headroom, fades, and appropriate music ducking against the actual recordings. Percentage sliders are starting points, not loudness guarantees. Check delivery requirements and listen to the complete mix; do not claim listening QA from waveform or metadata inspection alone.

A still moment is appropriate when it gives the viewer time to understand an image. A loop is appropriate when its repeated process explains the current narration. For either, justify its duration and purpose. For a loop, define period and matching endpoint states, then inspect consecutive repetitions before calling it seamless. A transition should carry a shared object, relationship, scale, or unresolved question into the next shot rather than merely decorate the cut.

## Handoff and production states

Deliver the requested level of detail, not a fixed number of files. A complete blueprint contains the brief and thesis; sources/claim register; preserved script and audio references; timed shot plan; art/asset register; approved-keyframe references where available; motion and transition specifications; and an assembly/audio plan. Explicitly list unresolved decisions and unavailable assets.

Use the exact field names in the [timeline contract](references/timeline-contract.md) for machine-readable handoffs. The [original short example](references/example-storyboard.json) illustrates structure with **estimated** timing; it is not approved art, a verified source package, or a rendered sample.

If the user refers to files that are not accessible, provide a partial prose handoff identifying what is known and what needs those files. A user-reported duration can support a provisional budget but is not a measurement. Do not invent exact narration or populate placeholder JSON just to satisfy the complete timeline contract.

Keep status factual: **planned → generated → assembled → exported → reviewed**. Status applies to a specific artifact; a reviewed script does not mean a reviewed film. When generation is requested but tools cannot produce a required result, finish the useful authorized work and report the remaining deliverable accurately. Do not quietly substitute a slideshow for requested explanatory animation.

## Verify before delivery

For a blueprint, check coverage, source support, asset continuity, transition states, and whether every advancing explanation has meaningful visual progression. Run the arithmetic helper when a JSON timeline exists:

```bash
python3 scripts/validate_timeline.py path/to/timeline.json
```

Run from this skill's directory or resolve the script relative to it. The helper verifies the contract and timing arithmetic only. It does not inspect media, listen, verify claims, or establish creative quality.

For a finished film, inspect the complete exported video and listen through the complete audio. Check narration sync, scientific diagrams, identity continuity, labels, clipping/obscured elements, transition seams, repetition, audio intelligibility, and export duration/properties. Recheck repaired portions plus their adjoining transitions. Record what was actually reviewed and remaining limitations. A representative frame or technically valid export cannot stand in for a full audiovisual review.
