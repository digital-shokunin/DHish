# Daggerheart Campaign Tool -- Design Spec

## Overview

A BXish-inspired modular Python application that serves as both an AI Game Master for solo/family Daggerheart play and a campaign management toolkit for GMs. The LLM receives the complete Daggerheart ruleset via tiered markdown skill files loaded into the system prompt, enabling mechanically faithful play. Campaign tools (party tracking, encounter building, NPC generation, world management, session journaling) are accessible via a tabbed Gradio web UI or terminal CLI.

## Goals

- Faithful Daggerheart mechanics: duality dice, Hope/Fear economy, spotlight system, damage thresholds, domain cards
- Two modes: AI GM (solo/family play) and campaign prep/management
- Simple setup: API key + `python daggerheart.py --web` to start
- BXish's proven patterns: markdown skills, session persistence, dark-themed UI
- Support 2-4 player party tracking

## Non-Goals

- Multi-user web app / authentication
- Mobile-native UI
- Real-time multiplayer over network
- Replacing the Daggerheart core rulebook (players should own it)

---

## Architecture

### Project Structure

```
daggerheart_campaign/
├── daggerheart.py              # Entry point (CLI args, launch)
├── requirements.txt            # openai, gradio
├── config.py                   # Defaults, model aliases, provider presets
├── engine/
│   ├── __init__.py
│   ├── agent.py                # LLM chat agent (send, prune, retry)
│   ├── skill_loader.py         # Load/compile markdown skills into system prompt
│   ├── dice.py                 # Dice roller (app-rolled, parse notation like 2d12+3)
│   └── session.py              # Save/load session state (JSON)
├── campaign/
│   ├── __init__.py
│   ├── character.py            # Character sheet CRUD (create/import/edit)
│   ├── party.py                # Party tracker (manage 2-4 PCs)
│   ├── adversary.py            # Adversary stat block generator + library
│   ├── encounter.py            # Encounter builder (Battle Points formula)
│   ├── world.py                # Locations, factions, lore, countdowns
│   ├── npc.py                  # NPC generator + registry
│   ├── journal.py              # Session notes/journal
│   └── generators.py           # Random tables (names, encounters, treasure)
├── ui/
│   ├── __init__.py
│   ├── web.py                  # Gradio tabbed UI
│   └── terminal.py             # Terminal chat mode
├── skills/                     # Daggerheart rules as markdown
│   ├── SKILL.md                # Master procedures file (GM behavior)
│   ├── 01-core-mechanics.md    # Duality dice, Hope/Fear
│   ├── 02-character-creation.md
│   ├── 03-classes.md
│   ├── 04-domains.md
│   ├── 05-combat.md
│   ├── 06-damage-armor.md
│   ├── 07-conditions-death.md
│   ├── 08-adversary-rules.md
│   ├── 09-encounter-building.md
│   ├── 10-campaign-structure.md
│   ├── 11-rest-downtime.md
│   ├── 12-equipment-weapons.md
│   ├── 13-equipment-armor.md
│   ├── 14-gm-moves.md
│   └── 15-gm-procedures.md
├── campaigns/                  # User campaign data (created at runtime)
│   └── {campaign-name}/
│       ├── campaign.json       # Campaign metadata, countdowns, Fear tracker
│       ├── party/              # Character sheets (JSON per PC)
│       ├── npcs/               # NPC files (Markdown)
│       ├── adversaries/        # Adversary stat blocks (JSON)
│       ├── world/              # Locations, factions (Markdown)
│       ├── journal/            # Session notes (Markdown per session)
│       └── sessions/           # Chat session saves (JSON)
```

### Dependencies

- `openai>=1.0` -- API client (OpenAI-compatible, works with Abacus/Anthropic/local)
- `gradio>=6.0` -- Web UI (lazy-imported only in `--web` mode)

---

## Engine Design

### LLM Agent (`engine/agent.py`)

Mirrors BXish's `BXAgent` pattern:

- OpenAI-compatible client, configurable base URL
- **Provider presets**: `abacus`, `anthropic`, `openai`, `local` -- each sets base URL and default model
- Temperature 0.7 default (configurable via `--temperature`)
- FIFO message pruning preserving system prompt, 75% of context for conversation
- Max output 16384 tokens per response
- Retry with exponential backoff on rate limits (5 attempts)
- Token estimation: `len(text) // 4 + 10` per message (same as BXish)

### Skill Loader (`engine/skill_loader.py`)

Loads Daggerheart rules from markdown files into a system prompt. Three cumulative tiers:

| Tier | Files | ~Tokens | Content |
|------|-------|---------|---------|
| **core** | SKILL.md + 01-07 | ~15K | Mechanics, characters, classes, domains, combat, damage, conditions/death |
| **gm** | core + 08-13 | ~25K | + adversary rules, encounter building, campaign structure, rest/downtime, equipment |
| **full** | gm + 14-15 | ~35K | + GM moves, GM procedures |

SKILL.md always loads first. It contains:
- Player agency rules (adapted from BXish's approach to Daggerheart's spotlight system)
- Hope/Fear tracking procedures
- Spotlight management instructions
- NPC/social play guidelines
- Core GM principles for Daggerheart's narrative style

System prompt format:
```
You are a Daggerheart RPG Game Master. You run tabletop RPG sessions
using official Daggerheart rules. You are a collaborative storyteller
who tracks Hope and Fear rigorously, manages the spotlight fairly,
and lets the players' decisions drive the narrative.

Follow the procedures, rules, and principles in the skill reference
below. These are your complete rules and GM instructions.

=== DAGGERHEART GAME MASTER SKILL ===

{skills_text}
```

### Dice Roller (`engine/dice.py`)

- `roll(notation: str) -> RollResult` -- parses standard notation: `2d12`, `1d8+3`, `3d6-1`
- `roll_duality() -> DualityResult` -- rolls 2d12, returns: hope_die, fear_die, total, outcome_type (success_hope, success_fear, failure_hope, failure_fear, critical)
- `roll_with_advantage(notation) -> RollResult` -- adds d6 to total
- `roll_with_disadvantage(notation) -> RollResult` -- subtracts d6 from total
- `roll_damage(proficiency, die, modifier) -> int` -- rolls [proficiency]d[die]+modifier

Three runtime modes:
- **App Roll**: Real RNG via `random.SystemRandom()`, results injected into chat as system messages for the AI to interpret
- **AI Narrates**: LLM describes rolls as part of narrative (no actual dice, like BXish)
- **Manual Input**: Player types results (e.g., "I rolled 8 and 5"), AI interprets

### Session Manager (`engine/session.py`)

- `save_session(messages, path)` -- JSON dump of full message history
- `load_session(path) -> list` -- JSON load, replaces system prompt at index 0 with current skills
- Auto-save on exit
- Campaign-aware: sessions saved under `campaigns/{name}/sessions/`
- Filename format: `session-YYYYMMDD-HHMMSS.json`

---

## Campaign Management

### Character System (`campaign/character.py`)

Three creation paths:

**Quick-gen**: User provides a concept ("reckless fire mage"), AI generates complete character sheet with all Daggerheart fields. Presented for approval/tweaks before saving.

**Guided wizard**: Step-by-step with AI explanations at each stage:
1. Class (with descriptions of all 9)
2. Subclass (2 options per class)
3. Ancestry (18 options, with feature descriptions)
4. Community (9 options)
5. Trait assignment (+2/+1/+1/+0/+0/-1 spread)
6. Equipment (weapons + armor from tier-appropriate table)
7. Experiences (2 at +2 each, with suggestions)
8. Domain cards (2 from class domains)
9. Connections (with other PCs if applicable)

**Manual import**: Upload or paste a JSON character sheet. Validates against Daggerheart rules:
- Trait spread sums correctly
- Class/domain combinations are valid
- HP/Stress within class range
- Equipment appropriate for tier

Character sheet format (JSON):
```json
{
  "name": "Kira Ashveil",
  "class": "Sorcerer",
  "subclass": "Elemental Origin",
  "level": 1,
  "tier": 1,
  "ancestry": "Drakona",
  "community": "Wildborne",
  "traits": {
    "agility": 0,
    "strength": -1,
    "finesse": 1,
    "instinct": 1,
    "presence": 0,
    "knowledge": 2
  },
  "evasion": 10,
  "proficiency": 1,
  "hp": {"max": 6, "marked": 0},
  "stress": {"max": 6, "marked": 0},
  "hope": {"current": 2, "max": 6, "scars": 0},
  "armor": {
    "name": "Gambeson",
    "base_score": 3,
    "slots_marked": 0,
    "major": 5,
    "severe": 11,
    "feature": "Flexible: +1 Evasion"
  },
  "weapons": [
    {
      "name": "Staff",
      "trait": "knowledge",
      "range": "melee",
      "damage": "d8+2",
      "burden": "two-handed",
      "type": "physical"
    }
  ],
  "domains": ["Arcana", "Midnight"],
  "domain_cards": {
    "loadout": [],
    "vault": []
  },
  "subclass_card": "foundation",
  "ancestry_features": [],
  "community_feature": "",
  "experiences": [
    {"name": "Volcano-born", "modifier": 2},
    {"name": "Reckless", "modifier": 2}
  ],
  "connections": []
}
```

### Party Tracker (`campaign/party.py`)

- Load/save all PCs from `campaigns/{name}/party/`
- Track party-level state: current tier, GM Fear counter
- Update HP/Stress/Hope/Armor slots during play
- Level-up flow: apply tier achievements, select advancements, update thresholds

### Encounter Builder (`campaign/encounter.py`)

- Battle Points formula: `(3 x party_size) + 2` base budget
- Adjustments: +/- for difficulty, adversary type constraints, tier mixing
- AI-powered: given party composition and narrative context, generates thematically appropriate encounters
- Validates BP math against adversary type costs
- Output: adversary list with stat blocks, tactical notes, environment suggestions
- Save/reuse encounters as JSON

### Adversary Manager (`campaign/adversary.py`)

- Library of common adversaries (stored as JSON stat blocks)
- Custom adversary builder with Daggerheart fields: name, tier, type, difficulty, thresholds, HP, stress, attack modifier, standard attack, features (action/reaction/passive/fear)
- AI generation: describe a creature concept, AI builds a mechanically valid stat block
- Tier scaling: auto-adjust stats to match party tier

### NPC Generator (`campaign/npc.py`)

- AI generates: name, role, appearance, personality, motivations, secrets, faction ties
- Optional combat stat block for combat-relevant NPCs
- Context-aware: generates NPCs fitting current campaign locations/factions
- Stored as markdown files in `campaigns/{name}/npcs/`

### World Manager (`campaign/world.py`)

- **Locations**: markdown with name, description, features, connections, NPCs present
- **Factions**: name, goals, resources, relationships, associated NPCs, countdown clocks
- **Countdowns**: standard (tick per roll), dynamic (tick per outcome), campaign (tick per session)
- **Lore**: freeform world notes
- All stored as markdown in `campaigns/{name}/world/`

### Journal (`campaign/journal.py`)

- One markdown file per session: `journal/session-001.md`
- Auto-summarize: AI reads chat session, produces structured notes:
  - Key events and decisions
  - NPC interactions
  - Combat outcomes
  - Loot/treasure gained
  - Countdown changes
  - Consequences pending
- Manual entry/editing
- Session numbering auto-incremented

### Random Generators (`campaign/generators.py`)

All LLM-powered using loaded Daggerheart context:
- Names (by ancestry)
- Random encounters (by tier and environment type)
- Treasure/loot (by tier)
- Location details and descriptions
- Tavern/shop inventories with prices
- Quest hooks fitting campaign context

---

## Web UI Design (`ui/web.py`)

### Theme

Dark fantasy theme (like BXish):
- Background: `#0d0d1a` (near-black)
- Bot messages: `#1a1a2e` (dark blue-black)
- User messages: `#b8d4e8` background with `#111` text
- Text: `#e0d6c2` (parchment)
- Accent: amber/gold (`#8b6914`)
- Font: Inter (Google Font)
- Tables: `#2a2a3e` headers, `#444` borders

### Tab 1: "Adventure" (AI GM Chat)

- `gr.Chatbot` -- main chat, height `calc(100vh - 250px)`
- `gr.Row`: text input (scale=9, placeholder "What do you do?", autofocus) + Send button (scale=1)
- `gr.Row`: dice mode radio (App Roll / AI Narrates / Manual), dice input field (shown in Manual mode)
- `gr.Row`: Save Session, New Session, Load Context (file upload .md/.txt/.json)
- `gr.Markdown`: status bar (model, tokens, messages, Hope/Fear counters)
- Greeting on first load: options for new campaign, continue existing, one-shot, character creation

### Tab 2: "Party"

- `gr.Dataframe` or card-style HTML for each PC: name, class, ancestry, HP/Stress/Hope/Armor as progress bars, traits
- `gr.Row`: Create Character (dropdown: Wizard/Quick-Gen), Import Character (JSON upload), Edit, Remove
- Campaign dropdown to switch between campaigns
- Party-level display: tier, GM Fear counter, active countdowns

### Tab 3: "Campaign World"

- Sub-tabs via `gr.Tab`: Locations, Factions, NPCs, Countdowns, Lore
- Each sub-tab: list of entities as cards (name + summary), click to expand
- "Generate" buttons per entity type (AI creates new ones fitting campaign context)
- Edit/save inline
- For Countdowns: visual progress display with tick/untick buttons

### Tab 4: "Encounter Workshop"

- `gr.Row`: party size (number, auto-filled), tier selector (dropdown), difficulty modifier (slider)
- Battle Points budget display (auto-calculated)
- Adversary list: add from library or generate custom, shows BP cost per adversary
- Running BP total with over/under budget indicator
- "Generate Encounter" button (AI builds thematic encounter)
- "Save Encounter" button
- Output area: full stat blocks, tactical notes, environment description

### Tab 5: "Journal"

- Session selector dropdown (auto-populated from journal files)
- `gr.Markdown` display of selected session notes
- "Auto-Summarize Current Session" button
- "New Entry" / "Edit" buttons
- `gr.Textbox` for manual entry/editing

### Shared UI Patterns

- All "Generate" actions show a loading spinner and stream the AI response
- Confirmation dialogs for destructive actions (delete character, new session)
- Info/status bar at bottom of each tab for feedback messages

---

## Terminal UI Design (`ui/terminal.py`)

Standard REPL chat loop (like BXish terminal mode):

```
Daggerheart GM v1.0 | Model: claude-sonnet-4 | Tier: full | Campaign: ashveil-quest
Type 'help' for commands.

GM> Welcome to the world of Daggerheart! ...

> [player input]
```

In-session commands:
- `save` -- save session to disk
- `status` -- show token usage, Hope/Fear, party HP/Stress summary
- `roll [notation]` -- app dice roll (e.g., `roll 2d12`, `roll 1d8+3`)
- `duality` -- roll duality dice with full outcome display
- `party` -- show party summary table
- `hope` / `fear` -- show/modify Hope and Fear counters
- `help` -- list commands
- `quit` / `exit` -- auto-save and exit

---

## CLI Interface (`daggerheart.py`)

### Arguments

| Argument | Default | Description |
|----------|---------|-------------|
| `--web` | False | Launch Gradio web UI |
| `--port` | 7860 | Web UI port |
| `--provider` | None | Provider preset: abacus, anthropic, openai, local |
| `--model` | Provider default | Model name or alias |
| `--base-url` | None | Custom API base URL (overrides provider) |
| `--api-key` | None | API key (or env var) |
| `--tier` | `full` | Skill tier: core, gm, full |
| `--skills-dir` | `./skills/` | Path to skill files |
| `--campaign` | None | Campaign name to load/create |
| `--session` | None | Resume from saved session JSON |
| `--temperature` | 0.7 | LLM temperature |
| `--dice-mode` | `app` | Default dice mode: app, ai, manual |
| `--list-models` | False | Print model aliases and exit |
| `--local` | False | Shortcut for local vLLM/Ollama |

### Environment Variables

- `ABACUS_API_KEY` -- Abacus AI API key
- `OPENAI_API_KEY` -- OpenAI API key
- `ANTHROPIC_API_KEY` -- Anthropic API key
- `OPENROUTER_API_KEY` -- OpenRouter API key (fallback)

### Provider Presets

| Provider | Base URL | Default Model | Env Var |
|----------|----------|---------------|---------|
| `abacus` | `https://api.abacus.ai/v1` | (user-configured) | `ABACUS_API_KEY` |
| `anthropic` | `https://api.anthropic.com/v1` | `claude-sonnet-4-20250514` | `ANTHROPIC_API_KEY` |
| `openai` | `https://api.openai.com/v1` | `gpt-4o` | `OPENAI_API_KEY` |
| `local` | `http://localhost:8000/v1` | (auto-discover) | None |

---

## Data Storage Summary

| Data Type | Format | Location | Rationale |
|-----------|--------|----------|-----------|
| Character sheets | JSON | `campaigns/{name}/party/` | Structured mechanical data |
| Adversary stat blocks | JSON | `campaigns/{name}/adversaries/` | Structured mechanical data |
| Campaign metadata | JSON | `campaigns/{name}/campaign.json` | State tracking (Fear, countdowns) |
| Chat sessions | JSON | `campaigns/{name}/sessions/` | Message history for LLM |
| Saved encounters | JSON | `campaigns/{name}/adversaries/` | Structured with BP costs |
| NPCs | Markdown | `campaigns/{name}/npcs/` | Narrative-heavy, human-readable |
| Locations | Markdown | `campaigns/{name}/world/` | Narrative-heavy |
| Factions | Markdown | `campaigns/{name}/world/` | Narrative-heavy |
| Lore | Markdown | `campaigns/{name}/world/` | Freeform notes |
| Session journal | Markdown | `campaigns/{name}/journal/` | Narrative summaries |
| Game rules/skills | Markdown | `skills/` | System prompt source |

---

## Key Design Decisions

1. **Modular but simple**: Split into logical modules, but still a `pip install -r requirements.txt && python daggerheart.py --web` experience. No build step, no database, no Docker required.

2. **BXish patterns preserved**: Markdown skills, FIFO pruning, system prompt replacement on resume, closure-based Gradio state, rough token estimation. Proven to work well for TTRPG AI GM use cases.

3. **Daggerheart-specific adaptations**: Hope/Fear tracking in the status bar (not just token counts), spotlight management in GM instructions, damage threshold calculations, domain card tracking -- mechanics that don't exist in B/X D&D.

4. **Single-user design**: Like BXish, this is a personal tool for one GM/player and their party. No auth, no multi-session concurrency.

5. **LLM-powered generators over static tables**: Daggerheart has fewer published random tables than B/X D&D. Generators use the LLM with loaded rules context rather than hardcoded tables, producing more creative and contextually appropriate results.

6. **Three dice modes**: Maximizes flexibility for different play styles -- solo players may want app rolls for fairness, family games may prefer physical dice, casual play may enjoy AI narration.
