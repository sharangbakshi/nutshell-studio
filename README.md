# Nutshell Studio

**Version 1.2.0** · Four explicitly invoked skills for original educational stories, art direction, meaningful animation, and production planning.

Turn a topic—or an existing script and voiceover—into a researched, connected explanation and a usable visual plan. The default **Cosmic Curiosity** direction combines expressive geometric illustration, dark cosmic spaces, restrained bright accents, and motion that demonstrates the idea being narrated. These are this project's design conventions, inspired by educational animation, not asserted rules of another studio.

The default deliverables are writing, visual specifications, prompts, and timed production blueprints. Installing the package does not supply a video generator, editor, narrator, account, or credits. A request to produce media requires available tools and an actual export/review workflow. A prompt or storyboard is never a finished film.

## The four skills

| Skill | Deliverable | Source |
|---|---|---|
| `nutshell-script` | Researched narration, claim register, and visual beat handoff | [Script](skills/nutshell-script/SKILL.md) |
| `nutshell-art` | Cohesive art direction, keyframe specifications, and asset handoff | [Art](skills/nutshell-art/SKILL.md) |
| `nutshell-animation` | Shot choreography, timed explanatory events, and tool-adapted motion plans | [Animation](skills/nutshell-animation/SKILL.md) |
| `nutshell-video` | Coordinates the other skills into a narration-aligned production blueprint | [Video](skills/nutshell-video/SKILL.md) |

In Codex, explicitly select a skill in the picker or mention it with `$`, for example:

```text
Use $nutshell-script to explain electromagnetic waves for a curious adult.
Use $nutshell-art to design three keyframes for this approved scene.
Use $nutshell-animation to choreograph this shot against the supplied narration.
Use $nutshell-video to plan visuals for script.md and voiceover.mp3. Preserve both.
```

Some hosts display plugin-qualified skill names; select the exact name shown in their picker. The package does **not** register `/nutshell-*` slash commands. Every skill includes `agents/openai.yaml` with `policy.allow_implicit_invocation: false`, the Codex control for explicit-only use. Loading the video skill's explicitly referenced companion instructions is part of that requested workflow, not unrelated automatic selection. Other hosts must be tested for equivalent activation behavior.

## Install in Codex

After this release is pushed to GitHub:

```bash
codex plugin marketplace add sharangbakshi/nutshell-studio
codex plugin add nutshell-studio@nutshell-studio
```

The marketplace is defined in [.agents/plugins/marketplace.json](.agents/plugins/marketplace.json); its source is this repository's root [plugin.json](plugin.json). The catalog's authentication policy is a host installation setting; this instructions-only package has no service login or MCP dependency.

To install a local checkout instead, from its root:

```bash
codex plugin marketplace add .
codex plugin add nutshell-studio@nutshell-studio
```

These commands change your plugin configuration. Do not add competing local and Git sources with the same marketplace name; choose one. Begin a fresh chat/turn and inspect the skill picker after installation. If discovery has not refreshed, restart the host.

### Updating an existing installation

Refresh the configured source and inspect its listing:

```bash
codex plugin marketplace upgrade nutshell-studio
codex plugin list --marketplace nutshell-studio --available --json
```

Use the host's supported update/reinstall flow and verify the installed release and all four explicit-only policies. A Git push alone does not update an installed snapshot. If the four skills were previously installed individually, identify those exact standalone copies before migrating; they can otherwise appear alongside the plugin's skills. Keep the old copies until the replacement is verified, then remove only the redundant copies you selected. Do not delete unrelated skills or configuration.

## Compatibility and verification

| Surface | Status and boundary |
|---|---|
| Codex CLI | Commands checked with `0.159.0-alpha.12.1`; release-specific discovery and validation results are recorded in [verification](docs/VERIFICATION.md). |
| Codex desktop | Uses the documented plugin/skill formats; picker interaction and a fresh-session installation still need host testing. |
| ChatGPT web | A local Codex installation does not install here. Requires a supported plugin distribution/import route; this repository is not a published universal-directory listing. |
| Claude Code and other hosts | Instruction files may be portable, but installation, command naming, and explicit-only policy are unverified. No blanket compatibility claim. |

## Working with a supplied recording

Approved narration remains unchanged unless you request an edit. Its measured duration and spoken boundaries control the timeline. Without recorded narration, timestamps remain estimates. Scene count follows the explanation; there is no mandatory 13-scene structure. Twelve minutes is an optional planning ceiling for an otherwise unspecified brief, not a forced duration or a replacement for the supplied recording.

Every important explanatory beat needs a corresponding visible event. An eight-second clip followed by a long still, or a repeated idle loop, is not the default solution to missing coverage. The plan distinguishes sequences, shots, assets, factual claims, and timed events. It also distinguishes a raster keyframe from an editable vector/layered asset.

See the video skill for its timeline contract, illustrative example, and standard-library timing validator. Illustrative examples are not approved artwork, measured voiceovers, or rendered media.

## Development and checks

Python 3.10+ is required for repository validation; the timeline helper uses the standard library. Development dependencies are isolated from skill use:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements-dev.txt
python scripts/validate_repo.py
python -m unittest discover -s tests -v
```

For full portable-manifest schema validation, download the versioned schema to a temporary file and pass its path to `python scripts/validate_repo.py --schema PATH`. CI performs that check too. The validator checks package wiring, skill names, explicit-only settings, local resources, and example timeline arithmetic; it does not prove scientific accuracy, activation behavior, or creative quality. Use the [evaluation cases](docs/EVALUATION.md) for those reviews.

See [release notes](CHANGELOG.md) for the migration and [verification](docs/VERIFICATION.md) for exactly what was run. No open-source license has been selected for this repository; this update does not choose a reuse license on the owner's behalf.

## Authoring references

- [OpenAI skill invocation and policy](https://learn.chatgpt.com/docs/build-skills)
- [Portable plugins and local marketplaces](https://developers.openai.com/plugins/build/plugins)
- [Manifest field reference](https://developers.openai.com/plugins/deploy/submission)
- [Agent Plugins 1.0.0 schema](https://agent-plugins.org/schemas/1.0.0/plugin.schema.json)
