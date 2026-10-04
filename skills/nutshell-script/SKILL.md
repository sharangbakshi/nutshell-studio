---
name: nutshell-script
description: Write or revise research-grounded narration for animated educational films, with a connected story, spoken cadence, evidence notes, and a visual-production handoff. Invoke explicitly for scriptwriting; this skill does not generate narration or video.
---

# Nutshell Script

Make an explanation feel like a discovery: an ordinary observation opens a question, the mechanism changes how we see it, and the ending returns us to the world with a richer understanding.

Use when explicitly selected as `$nutshell-script`, through a skill picker, or as a script stage of an explicitly requested Nutshell Video workflow. The user's brief, existing approvals, and supplied material take priority over the defaults below.

## 1. Establish the working material

- Identify the subject, audience, intended takeaway, delivery language, available references, approved text/audio, and requested duration. Infer routine creative choices from the brief; ask only about missing information that would change the work materially.
- For a new film with no duration specified, choose the shortest satisfying treatment with a **12-minute maximum**. This is a default, not a requirement to fill 12 minutes or override a user's different duration.
- Distinguish the requested deliverable: a new script, a revision, or a production handoff from an already approved script. Do not turn a narrow edit into a replacement documentary.

### If approved narration or audio already exists

- Preserve originals and work in a separate annotated copy. Keep approved wording and the supplied recording as the source of truth unless the user requests revision.
- Inspect the actual audio duration and transcript; record mismatches, omissions, and uncertain words. If word/phrase alignment is available, inspect it around pauses, rapid passages, and edits rather than trusting it blindly.
- Annotate the existing story and visuals against that recording. Do not create replacement speech, assume TTS access, or silently stretch/cut audio to satisfy a preferred structure.
- If a factual problem or incompatible duration is discovered, explain it and propose the smallest correction. Do not label known errors as verified or alter approved audio without authorization.
- If audio cannot be inspected or aligned, continue with a clearly **estimated** handoff; do not report measured synchronization.

## 2. Research the explanation before finalizing factual narration

Research material scientific or historical claims using accessible primary research, authoritative technical documentation, standards, and research institutions appropriate to the subject. Review sources themselves, not just search snippets or another model's summary. Use reviews to understand consensus and original studies where their detail matters. Check current information when the topic may have changed.

Keep a compact claim register alongside the script. Assign IDs such as `C01` to quantitative, causal, surprising, disputed, or central explanatory claims; group genuinely repeated claims. Each entry includes:

| Field | What to record |
|---|---|
| Claim | The precise statement, scope, conditions, and units where relevant |
| Evidence | Source title, author/institution, date, URL/DOI, and supporting page/section |
| Interpretation | Established result, live hypothesis, inference, toy-model result, or explanatory simplification |
| Limits | Uncertainty, competing findings, relevant exclusions, and analogy boundaries |
| Use | Sequence/shot IDs where the claim is spoken or visually implied |

- Independently check calculations, unit conversions, scales, and comparisons. Show enough working to reproduce any derived number.
- Do not turn one study into a universal conclusion. Carry qualifications into the spoken explanation when omitting them would materially mislead.
- Treat visual claims as claims: relative sizes, propagation directions, particle behavior, and causal arrows need the same scrutiny as words.
- If essential evidence is unavailable, narrow the claim, omit it, or label the output **research-incomplete draft** and identify the gap. Creative drafting can continue, but “fact-checked” is reserved for the scope actually checked.
- Keep source IDs and citations in production notes, not in text intended for a narrator to read aloud.

## 3. Shape a causal story

Write a short narrative premise: the viewer's starting question, the core explanatory mechanism, the main change in understanding, and the feeling the ending should earn. This is a creative compass, not an additional spoken introduction.

The following four movements are a useful starting shape, not four equal timed blocks:

1. **Notice something.** Start with a concrete observation, small puzzle, or consequential question. Let the viewer care before adding terminology. A simple definition is welcome when it is the clearest opening; do not manufacture a false misconception.
2. **Open the mechanism.** Reveal the actors, rules, and interactions in a sequence the viewer can follow. Each explanation should answer the question raised by the previous one. Change scale when the new scale reveals a cause or consequence.
3. **Test the understanding.** Vary one condition, compare cases, explore a useful limit, or show a real consequence. Choose examples that discriminate between explanations rather than accumulating an unrelated “zoo” of facts.
4. **Return with a new perspective.** Resolve the opening question. Connect the mechanism to life, technology, or a familiar experience when relevant. Let curiosity, intimacy, humor, or awe emerge from what was established.

Keep the voice warm, lucid, inquisitive, lightly ironic, and confident in proportion to the evidence. Favor precise action verbs, concrete images, and occasional dry humor. Alternate close human-scale moments with larger views when the explanation warrants them. A playful recurring object or visual joke can make a difficult idea memorable without carrying the scientific argument.

Do not require existential danger, optimistic nihilism, quantum detail, a “Goldilocks” condition, or cosmic scale for every topic. Do not claim intuition is wrong when it merely needs refinement. Stakes should follow from the evidence; the emotional landing should follow from the story.

For every transition, write its reason in the outline: “Having learned X, we now need Y because Z.” If that connection is weak, reorder, cut, or replace the section. An intriguing tangent is not automatically part of this film.

## 4. Make invisible ideas understandable

Choose the representation that clarifies the mechanism: a direct diagram, observable example, comparison, demonstration, or physical analogy. Tangible metaphors are valuable, not mandatory.

For a substantial analogy, record:

- **Correspondence:** What the familiar object/action represents.
- **Limit:** Where the analogy predicts the wrong behavior.
- **Exit:** How narration or visuals return to the actual mechanism before the limitation matters.

Introduce necessary terminology after the viewer has something to attach it to. Reuse terms consistently. Avoid stacking several new abstractions into one sentence or mapping a metaphor onto a second metaphor. Mark schematic scale, omitted dimensions, or nonliteral characters in production notes and on screen when needed for understanding.

## 5. Write for a voice, then budget time

- Deliver clean, complete spoken prose. Use varied sentence lengths, deliberate emphasis, concrete verbs, and room for a difficult idea to settle. Read it aloud when possible; do not report a listening review if only text was inspected.
- Keep narration separate from pause intentions, pronunciation guidance, music, foley, captions, and visual directions. Never make a narrator read technical annotations or claim IDs.
- Punctuation suggests phrasing; it does not enforce a precise pause. Write an intended pause in the production notes. Exact timing depends on the performed/generated recording and, when appropriate, audio editing.
- Use pronunciation notes for names, symbols, abbreviations, or ambiguous readings. Avoid arbitrary phonetic spellings inside the spoken master unless required by the selected narrator's tested workflow.
- For estimates, calculate speech time from word count and an explicitly stated delivery-rate assumption, then add nonspoken intervals separately. A starting range of 135–155 words/minute is a planning choice to test, not a guaranteed voice speed. Count intended spoken words consistently.
- For a fixed duration limit, leave room for breaths, reveals, and transitions. Revise scope or prose when the estimate exceeds the budget; do not solve an overcrowded explanation merely by speaking faster.
- Once narration exists, replace estimates with measured timings. Separate narrative sequences from shots: a sequence can need many visual beats. Never fix a universal scene count or force one static image to cover a long explanation.

## 6. Deliver a usable handoff

Provide only the artifacts the request needs, typically a spoken script plus a production companion and claim register. A Markdown document with clearly separated sections is sufficient for a short task; do not create empty production folders.

Use stable sequence IDs (`S01`) and shot IDs (`SH001`). Keep explanatory beats as timed events within shots. The human-readable handoff uses these fields so it can map into the full video timeline without renaming:

| Field | Requirement |
|---|---|
| `id`, `sequence_id` | Stable shot ID and its narrative sequence |
| `narration` | `kind` (`spoken` or `silence`) and exact `text` from the approved master |
| `start`, `end` | Global seconds; do not restart the clock in each sequence |
| `claim_ids` | Evidence entries supporting spoken and depicted assertions |
| `visual_purpose` | What the viewer must understand and the visible change that demonstrates it |
| `incoming_state`, `outgoing_state`, `transition` | Continuous visual states and the reason for the next transition |
| `events` | Timed explanatory actions, each with global `start`, `end`, `action`, and `narration_cue` |

At project level, record `timing.status` as `estimated` or `measured`, `timing.basis`, `timing.audio_source`, and `timing.audio_duration_seconds`. For an unrecorded draft, state that no audio exists and the duration is a forecast. Include analogy limits, pronunciation, and optional sound/pause intentions in separate production notes.

Visual intent describes explanatory action, not a claim that animation has been produced. Detailed assets and motion choreography belong to subsequent art/animation work. Carry approved asset/style IDs forward when already supplied; do not redesign them casually.

For an audio-based handoff, cover the complete recording contiguously, including deliberate nonspoken intervals. Explain any overlap or silence explicitly. Estimated timestamps must remain visibly estimated until measured against the final recording.

When participating in the full Nutshell Video workflow, use its available `references/timeline-contract.md` for the complete JSON format, including asset and claim records. Standalone script work remains useful without that sibling skill; the inline fields above are sufficient for a text handoff.

## 7. Review the actual script

Before delivery, check the opening promise is fulfilled, the causal chain is understandable, humor does not distort the mechanism, and no essential uncertainty disappeared during simplification. Reconcile central spoken/visual claims with the evidence register. Check duration arithmetic and missing, repeated, or unaligned narration.

Report the work actually done: research scope, timing basis, and whether a read-aloud or audio-alignment review occurred. Do not call a script an exported film or imply that a structural check proves audience engagement.

For a small original example of a hook, causal bridge, bounded analogy, and separate production notes, consult [references/annotated-example.md](references/annotated-example.md) when an example would help. It is a writing demonstration, not a scientific source, user-approved template, or tested video.
