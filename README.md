# DHish

A [BXish](https://github.com/gglessner/BXish)-inspired AI Game Master and campaign management tool for the [Daggerheart](https://www.daggerheart.com/) RPG by Darrington Press.

DHish loads the complete Daggerheart ruleset into an LLM's context window, enabling it to serve as a mechanically faithful Game Master. It also provides campaign management tools for tracking party state, building encounters, managing NPCs, and journaling sessions.

## Features

- **AI Game Master** -- solo or family play with a rules-accurate Daggerheart GM
- **Campaign Management** -- track characters, NPCs, locations, factions, countdowns
- **Encounter Builder** -- Battle Points calculator with adversary stat blocks
- **Duality Dice** -- built-in dice roller with Hope/Fear outcome resolution
- **Three Dice Modes** -- app-rolled (real RNG), AI-narrated, or manual input
- **Session Persistence** -- save/resume campaigns and chat sessions
- **Tiered Rule Loading** -- core (~9K tokens), gm (~14K), or full (~16K) rulesets
- **Web UI + Terminal** -- Gradio browser interface or terminal REPL

## Quick Start

```bash
# Clone
git clone https://github.com/digital-shokunin/DHish.git
cd DHish

# Set up venv
python3 -m venv .venv
source .venv/bin/activate  # Linux/Mac
# .venv\Scripts\activate   # Windows

# Install dependencies
pip install -r requirements.txt

# Run (web UI)
python3 daggerheart.py --web --provider abacus --api-key YOUR_KEY

# Run (terminal)
python3 daggerheart.py --provider abacus --api-key YOUR_KEY

# With a campaign
python3 daggerheart.py --web --provider abacus --api-key YOUR_KEY --campaign "my-quest"
```

## Environment Variables

Set your API key as an environment variable to avoid passing `--api-key` every time:

```bash
export ABACUS_API_KEY=your_key_here    # Abacus AI
export ANTHROPIC_API_KEY=your_key_here  # Anthropic
export OPENAI_API_KEY=your_key_here     # OpenAI
```

Then just:
```bash
python3 daggerheart.py --web --provider abacus --campaign "my-quest"
```

## Providers

| Provider | Flag | Default Model | Notes |
|----------|------|---------------|-------|
| Abacus AI | `--provider abacus` | (user-configured) | Pass `--model` to specify |
| Anthropic | `--provider anthropic` | claude-sonnet-4-20250514 | |
| OpenAI | `--provider openai` | gpt-4o | |
| Local (vLLM/Ollama) | `--local` | auto-discovered | Connects to localhost:8000 |
| Custom | `--base-url URL` | (requires `--model`) | Any OpenAI-compatible API |

## CLI Reference

```
python3 daggerheart.py [options]

Options:
  --web                 Launch Gradio web UI (default: terminal mode)
  --port PORT           Web UI port (default: 7860)
  --provider PROVIDER   Provider preset: abacus, anthropic, openai, local
  --model MODEL         Model name or identifier
  --base-url URL        Custom API base URL (overrides provider)
  --api-key KEY         API key (or use environment variable)
  --tier TIER           Skill tier: core, gm, full (default: full)
  --campaign NAME       Campaign name to load or create
  --session FILE        Resume from saved session JSON
  --temperature FLOAT   LLM temperature (default: 0.7)
  --dice-mode MODE      Default dice mode: app, ai, manual (default: app)
  --local               Use local LLM server (localhost:8000)
  --list-models         Print provider presets and exit
  --verbose             Enable debug logging
```

## Terminal Commands

During a terminal session:

| Command | Description |
|---------|-------------|
| `save` | Save session to disk |
| `status` | Show tokens, Hope/Fear, party HP |
| `roll <notation>` | Roll dice (e.g., `roll 2d12`, `roll 1d8+3`) |
| `duality [mod] [diff]` | Roll duality dice (e.g., `duality +2 14`) |
| `party` | Show party summary |
| `hope` | Show Hope per character |
| `fear` | Show GM Fear counter |
| `help` | List commands |
| `quit` | Auto-save and exit |

## Project Structure

```
DHish/
├── daggerheart.py          # CLI entry point
├── config.py               # Configuration and provider presets
├── requirements.txt        # Python dependencies
├── engine/
│   ├── agent.py            # LLM chat agent (send, prune, retry)
│   ├── dice.py             # Dice roller (duality, advantage, damage)
│   ├── skill_loader.py     # Load rules from markdown into system prompt
│   └── session.py          # Session save/load (JSON)
├── campaign/
│   ├── state.py            # Campaign state (Fear, countdowns, rests)
│   ├── character.py        # Character sheet CRUD and validation
│   ├── party.py            # Party tracker and context builder
│   ├── world.py            # Locations, factions, lore (markdown)
│   ├── npc.py              # NPC management (markdown)
│   ├── encounter.py        # Encounter builder (Battle Points)
│   ├── adversary.py        # Adversary stat blocks (JSON)
│   ├── journal.py          # Session journal (markdown)
│   └── generators.py       # LLM-powered content generators
├── ui/
│   ├── web.py              # Gradio web interface
│   └── terminal.py         # Terminal REPL
├── skills/                 # Daggerheart rules (16 markdown files)
│   ├── SKILL.md            # Master GM procedures
│   ├── 01-core-mechanics.md
│   ├── ...
│   └── 15-gm-procedures.md
├── campaigns/              # User campaign data (created at runtime)
│   └── {campaign-name}/
│       ├── campaign.json   # Campaign metadata, Fear, countdowns
│       ├── party/          # Character sheets (JSON)
│       ├── npcs/           # NPC files (Markdown)
│       ├── adversaries/    # Adversary stat blocks (JSON)
│       ├── encounters/     # Saved encounters (JSON)
│       ├── world/          # Locations, factions (Markdown)
│       ├── journal/        # Session notes (Markdown)
│       └── sessions/       # Chat session saves (JSON)
└── tests/                  # 83 tests
```

## Skill Tiers

Control how many rules are loaded into the LLM context:

| Tier | Tokens | Content |
|------|--------|---------|
| `core` | ~9K | Mechanics, characters, classes, domains, combat, damage, conditions |
| `gm` | ~14K | Core + adversaries, encounters, campaign structure, rest, equipment |
| `full` | ~16K | GM + GM moves and procedures |

Use `--tier core` for smaller context models, `--tier full` (default) for the complete experience.

## Running Tests

```bash
python3 -m pytest tests/ -v
```

## Inspired By

- [BXish](https://github.com/gglessner/BXish) by Greg Glessner -- AI Dungeon Master for B/X D&D
- [Daggerheart SRD](https://daggerheartsrd.com/) -- game rules reference

## License

This project is not affiliated with Darrington Press or Critical Role. Daggerheart is a trademark of Darrington Press LLC.
