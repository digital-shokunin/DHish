# CLAUDE.md

## Project Overview

DHish is a BXish-inspired AI Game Master and campaign management tool for the Daggerheart RPG. It loads Daggerheart rules as tiered markdown skill files into an LLM's system prompt to enable mechanically faithful gameplay.

## Architecture

- **Engine layer** (`engine/`): LLM agent, dice roller, skill loader, session persistence
- **Campaign layer** (`campaign/`): Character sheets, party tracker, world entities, NPCs, encounters, adversaries, journal, generators
- **UI layer** (`ui/`): Gradio web interface and terminal REPL
- **Skills** (`skills/`): 16 markdown files containing the complete Daggerheart ruleset
- **Entry point**: `daggerheart.py` with argparse CLI

## Key Patterns

- **OpenAI-compatible API**: Uses the `openai` Python client for all providers (Abacus, Anthropic, OpenAI, local vLLM/Ollama)
- **Markdown skills → system prompt**: Rules loaded from `skills/` and concatenated into the LLM system prompt. Three tiers: core, gm, full.
- **Campaign context injection**: Campaign state injected as a system message at position 1 (after system prompt), updated in-place during play
- **FIFO message pruning**: Oldest non-system messages dropped first when context budget exceeded
- **Data storage**: JSON for mechanical data (character sheets, adversary stat blocks, campaign state), Markdown for narrative content (NPCs, locations, journal)
- **Closure-based Gradio state**: Web UI uses closure-captured mutable state (single-user design)
- **Daggerheart-specific dice**: Duality dice (2d12 Hope/Fear), advantage/disadvantage (+/-d6), damage rolls ([proficiency]d[die]+mod)

## Development

```bash
# Set up
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# Run tests
python3 -m pytest tests/ -v

# Run the app
python3 daggerheart.py --web --provider abacus --api-key KEY
```

## Testing

- 83 tests covering engine (dice, agent, skill loader, session) and campaign (state, character, party, world, NPC, encounter, adversary, journal) modules
- Tests use `tempfile.TemporaryDirectory` for filesystem isolation
- Run with: `python3 -m pytest tests/ -v`

## Daggerheart Mechanics to Know

- **Duality Dice**: 2d12 (Hope die + Fear die). Hope higher = player gains Hope. Fear higher = GM gains Fear. Matching = Critical Success.
- **Hope/Fear economy**: Hope is per-PC (max 6), Fear is a single GM pool (max 12). Both are metacurrencies spent for effects.
- **Spotlight system**: No initiative. Players act first, spotlight swings to GM on Fear/failure rolls.
- **Player-facing rolls**: Only players roll dice. GM does not roll to attack.
- **Damage thresholds**: Damage compared to Major/Severe thresholds → marks 1-4 HP (not subtracted directly).
- **Domain cards**: 5-card loadout from 2 class domains, swappable at rest.

## Design Documents

- **Spec**: `docs/superpowers/specs/2026-03-19-daggerheart-campaign-tool-design.md`
- **Plan**: `docs/superpowers/plans/2026-03-21-daggerheart-campaign-tool.md`
- **Mechanics reference**: `daggerheart_mechanics_reference.md`

## File Conventions

- Campaign data: `campaigns/{name}/` with subdirs for party, npcs, adversaries, encounters, world, journal, sessions
- Character sheets: JSON in `campaigns/{name}/party/{safe_name}.json`
- NPCs/locations/factions: Markdown in `campaigns/{name}/npcs/` and `campaigns/{name}/world/`
- Skill files: Markdown in `skills/`, numbered 01-15 plus SKILL.md
- Thresholds: Store base values in JSON, compute effective at runtime (`base + level`)
