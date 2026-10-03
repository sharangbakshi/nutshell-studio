# nutshell-studio

A modular production skill suite for OpenAI Codex, Claude Code, and ChatGPT enabling full-pipeline creation of 12-minute scientific documentaries in the signature *Kurzgesagt – In a Nutshell* narrative and flat 2D vector animation style.

## Included Skills & Commands

| Command | Skill Path | Purpose |
| :--- | :--- | :--- |
| `/nutshell-script [Topic]` | `skills/script/SKILL.md` | Generates full 12-minute, 4-act scripts with TTS audio-timing cues. |
| `/nutshell-art [Subject]` | `skills/art/SKILL.md` | Produces Bauhaus-inspired flat 2D vector prompts (Imagen / Midjourney). |
| `/nutshell-animation [Action]` | `skills/animation/SKILL.md` | Produces 12 fps stepped motion prompts (Veo / Runway / Sora). |
| `/nutshell-video [Topic]` | `skills/video/SKILL.md` | Generates a full 13-scene synchronized production blueprint. |

## Installation

### Via Codex CLI
```bash
codex plugin marketplace add sharangbakshi/nutshell-studio
codex plugin add nutshell-studio@nutshell-studio