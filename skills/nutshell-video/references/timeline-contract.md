# Timeline contract, version 1

Use this contract for a machine-readable handoff between script, art, motion, and assembly. It carries narration, visual intent, and continuity together. All times are **global seconds from the beginning of the narration track**, not shot-relative seconds. Additional fields are allowed for provider settings, labels, detailed sources, review evidence, or delivery information.

## Required fields

| Object | Fields and meaning |
|---|---|
| Root | `schema_version`: integer `1`; `project_title`: nonempty string; `timing`: object; `assets`: array; `claims`: array; `shots`: nonempty array in chronological order. Optional `duration_limit_seconds`: finite positive number. |
| `timing` | `status`: `estimated` or `measured`; `audio_source`: recording path/identifier, or an explicit statement that recording does not exist; `audio_duration_seconds`: finite positive number; `basis`: how duration and boundaries were obtained, including alignment uncertainty. |
| Each asset | `id`: unique nonempty string; `kind`: e.g. `raster-keyframe`, `layered-vector`, `character-design`, `generated-clip`; `status`: `planned`, `generated`, or `approved`; `source`: real path/identifier, or an explicit planned description when no asset exists. |
| Each claim | `id`: unique nonempty string; `statement`: claim being checked; `status`: `verified`, `provisional`, `disputed`, or `illustrative`; `sources`: array of nonempty source references; `qualification`: limitations/uncertainty, allowed empty only for `verified`. A verified claim needs at least one source. |
| Each shot | `id`: unique nonempty string; `sequence_id`: grouping ID; `start`, `end`: nonnegative finite numbers with `end > start`; `narration`: object; `visual_purpose`: explanatory or emotional function; `asset_ids`, `claim_ids`: arrays referencing the registers; `incoming_state`, `outgoing_state`: observable continuity states; `transition`: handoff into the next shot or ending; `events`: nonempty array. |
| Shot narration | `kind`: `spoken` or `silence`; `text`: exact words for spoken narration, empty string for an intentional silent interval. Do not insert performance directions into spoken text. |
| Each event | `start`, `end`: finite numbers with positive duration wholly inside its shot; `action`: specific visible change or justified hold; `narration_cue`: exact associated spoken fragment, or reason for a silent beat. Events may overlap when motion is coordinated. |

Empty asset/claim arrays are valid when the shot genuinely needs none; they do not waive research for scientific assertions. `illustrative` describes a constructed model or fiction, not a way to label unverified real-world science as fact. `approved` means approved under the project's existing process; do not infer user approval from generation or structural validation.

`status: measured` requires the actual recording and an honest account of how its boundaries were aligned. Duration metadata alone measures the endpoint, not every spoken phrase. If some boundaries are still estimates, leave the overall status `estimated` and state the mixed evidence in `basis`. Record individual uncertainties in additional fields if useful.

For a text-only plan, `audio_duration_seconds` means the proposed duration of the future narration track, including deliberate nonspoken intervals; it does not imply an audio file exists. Explain that estimate in `basis` and use `status: estimated`. This contract describes a complete proposed or measured timeline. If approved text or referenced audio is inaccessible and exact shot content is unknown, use a partial prose handoff instead of invented narration or a fake passing JSON document.

## Coverage and continuity

- First shot starts at `0`; each next start equals the previous end; final end equals the declared audio duration. The validator tolerates rounding within **0.000001 seconds**, not a missing video frame.
- Shots describe exclusive ownership of timeline intervals. A dissolve can span both visual layers, but it must have one documented timeline owner; represent its overlap in events/transition details rather than overlapping shot ranges. A transition that crosses a boundary needs an event on each side, with matching states.
- Events have positive durations and stay within the owning shot. They need not occupy every instant: review the intervening state and purpose manually. The helper cannot decide whether a hold is thoughtful or merely filler.
- Identify the exact approved source keyframe through `asset_ids` and its register `source`. Additional `source_keyframe_id` fields may disambiguate several assets. Incoming and outgoing states should explain object identity, position, scale, labeling, and motion phase where relevant.
- Caption/label content, mathematical constraints, references, animation cadence, export frame rate, shot-local motion controls, sound cues, and asset rights may be added without changing the core schema. Use a separate creative review to check them.

For a prose handoff, use the same meanings. Common alternate labels map explicitly: `shot_id → shots[].id`; `audio_start/audio_end → start/end`; `narration_span → narration.text`; `entry_state/exit_state → incoming_state/outgoing_state`; `beat_events → events`; `timing_basis → timing.basis`. `visual_claim` should be resolved into `visual_purpose` plus any relevant `claim_ids`.

## Running the check

From the skill directory:

```bash
python3 scripts/validate_timeline.py references/example-storyboard.json
python3 scripts/validate_timeline.py /path/to/project/timeline.json
```

The helper uses Python's standard library, prints diagnostics, and exits `0` on success or `1` on invalid input. The exported `validate_timeline(data)` function returns a list of errors. It checks required fields, enum values, unique IDs, register references, numerical bounds, chronological coverage, duration limits, and event containment. Duplicate JSON keys are rejected by the command-line reader. The helper never opens a media file, contacts a service, or changes the input.

**A pass is not evidence of actual timing, scientific accuracy, permissions, asset approval, good pacing, or a reviewed film.** Those require inspecting the recording, sources, assets, and complete export. The adjacent original example is a fictional queue explanation with estimated timing; it is a schema fixture, not the user's approved script or an example of achieved video quality.
