# Daggerheart Campaign Tool Implementation Plan

> **For agentic workers:** REQUIRED: Use superpowers:subagent-driven-development (if subagents available) or superpowers:executing-plans to implement this plan. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a BXish-inspired AI Game Master and campaign management tool for the Daggerheart RPG system.

**Architecture:** Modular Python app with engine layer (LLM agent, dice roller, skill loader, session manager), campaign layer (character, party, adversary, encounter, world, NPC, journal, generators), and UI layer (Gradio web + terminal CLI). Daggerheart rules loaded as tiered markdown skill files into LLM system prompt.

**Tech Stack:** Python 3.10+, openai>=1.0, gradio>=6.0, pytest

**Spec:** `docs/superpowers/specs/2026-03-19-daggerheart-campaign-tool-design.md`
**Mechanics Reference:** `daggerheart_mechanics_reference.md`

---

## Chunk 1: Foundation (Config, Dice, Skill Loader, Session Manager)

This chunk builds the core engine components that everything else depends on. After this chunk, you can load skills, roll dice, and save/load sessions -- but there's no LLM agent or UI yet.

### Task 1: Project Setup

**Files:**
- Create: `requirements.txt`
- Create: `engine/__init__.py`
- Create: `campaign/__init__.py`
- Create: `ui/__init__.py`
- Create: `tests/__init__.py`
- Create: `tests/engine/__init__.py`
- Create: `tests/campaign/__init__.py`

- [ ] **Step 1: Create requirements.txt**

```
openai>=1.0
gradio>=6.0
pytest>=7.0
```

- [ ] **Step 2: Create package init files**

All `__init__.py` files are empty. Create:
- `engine/__init__.py`
- `campaign/__init__.py`
- `ui/__init__.py`
- `tests/__init__.py`
- `tests/engine/__init__.py`
- `tests/campaign/__init__.py`

- [ ] **Step 3: Install dependencies**

Run: `pip3 install -r requirements.txt`

- [ ] **Step 4: Commit**

```bash
git add requirements.txt engine/__init__.py campaign/__init__.py ui/__init__.py tests/__init__.py tests/engine/__init__.py tests/campaign/__init__.py
git commit -m "chore: project scaffolding with dependencies and package structure"
```

---

### Task 2: Configuration Module

**Files:**
- Create: `config.py`
- Create: `tests/test_config.py`

- [ ] **Step 1: Write the failing test**

```python
# tests/test_config.py
from config import (
    PROVIDER_PRESETS,
    CHARS_PER_TOKEN,
    DEFAULT_TEMPERATURE,
    DEFAULT_MAX_TOKENS,
    DEFAULT_PORT,
    CONTEXT_RESERVE_RATIO,
    SKILL_TIERS,
    resolve_provider,
)


def test_provider_presets_have_required_keys():
    for name, preset in PROVIDER_PRESETS.items():
        assert "base_url" in preset
        assert "env_var" in preset


def test_abacus_preset():
    p = PROVIDER_PRESETS["abacus"]
    assert "abacus" in p["base_url"].lower() or "abacus" in p["env_var"].lower()


def test_resolve_provider_with_known_provider():
    base_url, env_var = resolve_provider("abacus")
    assert base_url == PROVIDER_PRESETS["abacus"]["base_url"]
    assert env_var == PROVIDER_PRESETS["abacus"]["env_var"]


def test_resolve_provider_with_base_url_override():
    base_url, env_var = resolve_provider(
        "abacus", base_url_override="https://custom.api/v1"
    )
    assert base_url == "https://custom.api/v1"


def test_resolve_provider_local():
    base_url, env_var = resolve_provider("local")
    assert "localhost" in base_url
    assert env_var is None


def test_resolve_provider_none_requires_base_url():
    base_url, env_var = resolve_provider(None, base_url_override="https://example.com/v1")
    assert base_url == "https://example.com/v1"


def test_constants():
    assert CHARS_PER_TOKEN == 4
    assert DEFAULT_TEMPERATURE == 0.7
    assert DEFAULT_MAX_TOKENS == 16384
    assert DEFAULT_PORT == 7860
    assert CONTEXT_RESERVE_RATIO == 0.75


def test_skill_tiers():
    assert "core" in SKILL_TIERS
    assert "gm" in SKILL_TIERS
    assert "full" in SKILL_TIERS
    # core files are subset of gm, gm subset of full
    assert set(SKILL_TIERS["core"]).issubset(set(SKILL_TIERS["gm"]))
    assert set(SKILL_TIERS["gm"]).issubset(set(SKILL_TIERS["full"]))
    # SKILL.md is in all tiers
    assert "SKILL.md" in SKILL_TIERS["core"]
```

- [ ] **Step 2: Run test to verify it fails**

Run: `python3 -m pytest tests/test_config.py -v`
Expected: FAIL (cannot import config)

- [ ] **Step 3: Write implementation**

```python
# config.py
"""Configuration constants and provider presets for Daggerheart Campaign Tool."""

VERSION = "1.0.0"
CHARS_PER_TOKEN = 4
DEFAULT_TEMPERATURE = 0.7
DEFAULT_MAX_TOKENS = 16384
DEFAULT_PORT = 7860
CONTEXT_RESERVE_RATIO = 0.75  # 75% of context for conversation

PROVIDER_PRESETS = {
    "abacus": {
        "base_url": "https://api.abacus.ai/v1",
        "default_model": None,  # user-configured
        "env_var": "ABACUS_API_KEY",
    },
    "anthropic": {
        "base_url": "https://api.anthropic.com/v1",
        "default_model": "claude-sonnet-4-20250514",
        "env_var": "ANTHROPIC_API_KEY",
    },
    "openai": {
        "base_url": "https://api.openai.com/v1",
        "default_model": "gpt-4o",
        "env_var": "OPENAI_API_KEY",
    },
    "local": {
        "base_url": "http://localhost:8000/v1",
        "default_model": None,  # auto-discover
        "env_var": None,
    },
}

# Skill tier file lists (cumulative)
_CORE_FILES = [
    "SKILL.md",
    "01-core-mechanics.md",
    "02-character-creation.md",
    "03-classes.md",
    "04-domains.md",
    "05-combat.md",
    "06-damage-armor.md",
    "07-conditions-death.md",
]

_GM_FILES = _CORE_FILES + [
    "08-adversary-rules.md",
    "09-encounter-building.md",
    "10-campaign-structure.md",
    "11-rest-downtime.md",
    "12-equipment-weapons.md",
    "13-equipment-armor.md",
]

_FULL_FILES = _GM_FILES + [
    "14-gm-moves.md",
    "15-gm-procedures.md",
]

SKILL_TIERS = {
    "core": _CORE_FILES,
    "gm": _GM_FILES,
    "full": _FULL_FILES,
}

SYSTEM_PROMPT_PREAMBLE = """You are a Daggerheart RPG Game Master. You run tabletop RPG sessions \
using official Daggerheart rules. You are a collaborative storyteller \
who tracks Hope and Fear rigorously, manages the spotlight fairly, \
and lets the players' decisions drive the narrative.

Follow the procedures, rules, and principles in the skill reference \
below. These are your complete rules and GM instructions.

=== DAGGERHEART GAME MASTER SKILL ===

"""


def resolve_provider(provider, base_url_override=None):
    """Resolve provider to (base_url, env_var_name).

    Args:
        provider: Provider name string or None.
        base_url_override: If set, overrides the provider's base_url.

    Returns:
        Tuple of (base_url, env_var_name). env_var_name may be None.
    """
    if provider and provider in PROVIDER_PRESETS:
        preset = PROVIDER_PRESETS[provider]
        base_url = base_url_override or preset["base_url"]
        return base_url, preset["env_var"]
    return base_url_override, None
```

- [ ] **Step 4: Run test to verify it passes**

Run: `python3 -m pytest tests/test_config.py -v`
Expected: All PASS

- [ ] **Step 5: Commit**

```bash
git add config.py tests/test_config.py
git commit -m "feat: add configuration module with provider presets and skill tiers"
```

---

### Task 3: Dice Roller

**Files:**
- Create: `engine/dice.py`
- Create: `tests/engine/test_dice.py`

- [ ] **Step 1: Write the failing tests**

```python
# tests/engine/test_dice.py
import re
from engine.dice import (
    roll, roll_duality, roll_damage, roll_with_advantage,
    roll_with_disadvantage, RollResult, DualityResult,
)


class TestRoll:
    def test_roll_single_die(self):
        result = roll("1d6")
        assert isinstance(result, RollResult)
        assert 1 <= result.total <= 6
        assert len(result.dice) == 1

    def test_roll_multiple_dice(self):
        result = roll("3d8")
        assert 3 <= result.total <= 24
        assert len(result.dice) == 3

    def test_roll_with_positive_modifier(self):
        result = roll("1d6+3")
        assert 4 <= result.total <= 9
        assert result.modifier == 3

    def test_roll_with_negative_modifier(self):
        result = roll("2d6-1")
        assert 1 <= result.total <= 11
        assert result.modifier == -1

    def test_roll_no_modifier(self):
        result = roll("2d12")
        assert result.modifier == 0

    def test_roll_notation_string(self):
        result = roll("2d8+2")
        assert re.match(r"2d8\+2", result.notation)

    def test_roll_invalid_notation(self):
        try:
            roll("bad")
            assert False, "Should have raised ValueError"
        except ValueError:
            pass


class TestRollDuality:
    def test_returns_duality_result(self):
        result = roll_duality(modifier=2, difficulty=12)
        assert isinstance(result, DualityResult)

    def test_hope_and_fear_dice_in_range(self):
        result = roll_duality(modifier=0, difficulty=11)
        assert 1 <= result.hope_die <= 12
        assert 1 <= result.fear_die <= 12

    def test_modified_total(self):
        result = roll_duality(modifier=2, difficulty=11)
        assert result.modified_total == result.hope_die + result.fear_die + 2

    def test_critical_on_matching_dice(self):
        # Run many times to try to hit a critical (1/12 chance)
        # Instead, test the logic directly with known values
        from engine.dice import _resolve_duality
        outcome = _resolve_duality(hope_die=5, fear_die=5, modified_total=12, difficulty=11)
        assert outcome.outcome_type == "critical"
        assert outcome.hope_gained is True
        assert outcome.stress_cleared is True

    def test_success_with_hope(self):
        from engine.dice import _resolve_duality
        outcome = _resolve_duality(hope_die=8, fear_die=5, modified_total=15, difficulty=11)
        assert outcome.outcome_type == "success_hope"
        assert outcome.hope_gained is True
        assert outcome.fear_gained is False

    def test_success_with_fear(self):
        from engine.dice import _resolve_duality
        outcome = _resolve_duality(hope_die=4, fear_die=9, modified_total=15, difficulty=11)
        assert outcome.outcome_type == "success_fear"
        assert outcome.hope_gained is False
        assert outcome.fear_gained is True

    def test_failure_with_hope(self):
        from engine.dice import _resolve_duality
        outcome = _resolve_duality(hope_die=7, fear_die=2, modified_total=10, difficulty=11)
        assert outcome.outcome_type == "failure_hope"
        assert outcome.hope_gained is True

    def test_failure_with_fear(self):
        from engine.dice import _resolve_duality
        outcome = _resolve_duality(hope_die=3, fear_die=6, modified_total=10, difficulty=11)
        assert outcome.outcome_type == "failure_fear"
        assert outcome.fear_gained is True


class TestRollAdvantage:
    def test_advantage_adds_d6(self):
        result = roll_with_advantage("2d12")
        # 2d12 range is 2-24, +d6 adds 1-6, so 3-30
        assert 3 <= result.total <= 30
        assert len(result.dice) == 3  # 2d12 + 1d6

    def test_disadvantage_subtracts_d6(self):
        result = roll_with_disadvantage("2d12")
        # 2d12 range is 2-24, -d6 subtracts 1-6, so -4 to 23
        assert -4 <= result.total <= 23
        assert len(result.dice) == 3  # 2d12 + 1d6


class TestRollDamage:
    def test_basic_damage(self):
        total = roll_damage(proficiency=2, die=8, modifier=2)
        assert 4 <= total <= 18  # 2d8+2: min 2+2=4, max 16+2=18

    def test_proficiency_1(self):
        total = roll_damage(proficiency=1, die=6, modifier=0)
        assert 1 <= total <= 6
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `python3 -m pytest tests/engine/test_dice.py -v`
Expected: FAIL (cannot import engine.dice)

- [ ] **Step 3: Write implementation**

```python
# engine/dice.py
"""Dice roller for Daggerheart RPG.

Supports standard notation (2d12+3), duality dice (2d12 with Hope/Fear),
and damage rolls ([proficiency]d[die]+modifier).
"""

import random
import re
from dataclasses import dataclass

_rng = random.SystemRandom()

_NOTATION_RE = re.compile(r"^(\d+)d(\d+)([+-]\d+)?$", re.IGNORECASE)


@dataclass
class RollResult:
    notation: str
    dice: list[int]
    modifier: int
    total: int


@dataclass
class DualityOutcome:
    outcome_type: str  # success_hope, success_fear, failure_hope, failure_fear, critical
    hope_gained: bool
    fear_gained: bool
    stress_cleared: bool


@dataclass
class DualityResult:
    hope_die: int
    fear_die: int
    raw_total: int
    modified_total: int
    difficulty: int
    outcome_type: str
    hope_gained: bool
    fear_gained: bool
    stress_cleared: bool


def roll(notation: str) -> RollResult:
    """Roll dice using standard notation like '2d12', '1d8+3', '3d6-1'.

    Args:
        notation: Dice notation string.

    Returns:
        RollResult with individual dice, modifier, and total.

    Raises:
        ValueError: If notation is invalid.
    """
    match = _NOTATION_RE.match(notation.strip())
    if not match:
        raise ValueError(f"Invalid dice notation: {notation!r}")

    count = int(match.group(1))
    sides = int(match.group(2))
    mod_str = match.group(3)
    modifier = int(mod_str) if mod_str else 0

    dice = [_rng.randint(1, sides) for _ in range(count)]
    total = sum(dice) + modifier

    return RollResult(notation=notation.strip(), dice=dice, modifier=modifier, total=total)


def _resolve_duality(
    hope_die: int, fear_die: int, modified_total: int, difficulty: int
) -> DualityOutcome:
    """Determine the outcome of a duality dice roll.

    Args:
        hope_die: Value of the Hope die (1-12).
        fear_die: Value of the Fear die (1-12).
        modified_total: Sum of both dice plus modifier.
        difficulty: Target difficulty number.

    Returns:
        DualityOutcome with outcome type and metacurrency changes.
    """
    # Critical: matching dice = auto success
    if hope_die == fear_die:
        return DualityOutcome(
            outcome_type="critical",
            hope_gained=True,
            fear_gained=False,
            stress_cleared=True,
        )

    success = modified_total >= difficulty
    hope_higher = hope_die > fear_die

    if success and hope_higher:
        return DualityOutcome("success_hope", hope_gained=True, fear_gained=False, stress_cleared=False)
    elif success and not hope_higher:
        return DualityOutcome("success_fear", hope_gained=False, fear_gained=True, stress_cleared=False)
    elif not success and hope_higher:
        return DualityOutcome("failure_hope", hope_gained=True, fear_gained=False, stress_cleared=False)
    else:
        return DualityOutcome("failure_fear", hope_gained=False, fear_gained=True, stress_cleared=False)


def roll_duality(modifier: int = 0, difficulty: int = 11) -> DualityResult:
    """Roll Daggerheart duality dice (2d12) and resolve the outcome.

    Args:
        modifier: Trait modifier to add to the roll.
        difficulty: Target number to meet or exceed.

    Returns:
        DualityResult with full outcome details.
    """
    hope_die = _rng.randint(1, 12)
    fear_die = _rng.randint(1, 12)
    raw_total = hope_die + fear_die
    modified_total = raw_total + modifier

    outcome = _resolve_duality(hope_die, fear_die, modified_total, difficulty)

    return DualityResult(
        hope_die=hope_die,
        fear_die=fear_die,
        raw_total=raw_total,
        modified_total=modified_total,
        difficulty=difficulty,
        outcome_type=outcome.outcome_type,
        hope_gained=outcome.hope_gained,
        fear_gained=outcome.fear_gained,
        stress_cleared=outcome.stress_cleared,
    )


def roll_with_advantage(notation: str) -> RollResult:
    """Roll with advantage: roll normally, then add a d6.

    Args:
        notation: Dice notation string.

    Returns:
        RollResult with the advantage d6 included in dice list.
    """
    result = roll(notation)
    bonus = _rng.randint(1, 6)
    return RollResult(
        notation=f"{notation}+adv",
        dice=result.dice + [bonus],
        modifier=result.modifier,
        total=result.total + bonus,
    )


def roll_with_disadvantage(notation: str) -> RollResult:
    """Roll with disadvantage: roll normally, then subtract a d6.

    Args:
        notation: Dice notation string.

    Returns:
        RollResult with the disadvantage d6 included in dice list.
    """
    result = roll(notation)
    penalty = _rng.randint(1, 6)
    return RollResult(
        notation=f"{notation}-dis",
        dice=result.dice + [penalty],
        modifier=result.modifier,
        total=result.total - penalty,
    )


def roll_damage(proficiency: int, die: int, modifier: int = 0) -> int:
    """Roll damage: [proficiency]d[die]+modifier.

    Args:
        proficiency: Number of dice to roll.
        die: Die size (e.g., 8 for d8).
        modifier: Flat modifier to add.

    Returns:
        Total damage value.
    """
    dice = [_rng.randint(1, die) for _ in range(proficiency)]
    return sum(dice) + modifier
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `python3 -m pytest tests/engine/test_dice.py -v`
Expected: All PASS

- [ ] **Step 5: Commit**

```bash
git add engine/dice.py tests/engine/test_dice.py
git commit -m "feat: add dice roller with duality dice and damage rolls"
```

---

### Task 4: Skill Loader

**Files:**
- Create: `engine/skill_loader.py`
- Create: `tests/engine/test_skill_loader.py`
- Create: `skills/SKILL.md` (minimal test fixture)

- [ ] **Step 1: Create a minimal test skill file**

Create `skills/SKILL.md`:
```markdown
# Daggerheart Game Master Procedures

## Player Agency (STRICT)

1. Always describe the scene, then ask the player what they do.
2. Resolve one action per player input. Do not bundle multiple actions.
3. Always ask which target for attacks or spells.
4. Ask, don't assume -- never decide player actions for them.
5. Pause before entering new areas and describe what the player perceives.
6. Offer downtime checkpoints between scenes.
7. NPCs react to players; they do not lead the story.
8. Do not auto-assign actions to party members the player did not specify.
9. At resource decision points, remind players of their current resources.
10. Compress travel and downtime unless the player wants to role-play it.

## Spotlight Management

- Players act first at the start of combat.
- Any player can volunteer to act (no fixed turn order).
- When a player rolls with Fear or fails, the spotlight swings to the GM.
- GM takes adversary actions, then spotlight returns to players.
- Players collaboratively decide who acts next.

## Hope and Fear Tracking

- Track Hope per-PC (starts at 2, max 6).
- Track Fear as a single GM pool (max 12).
- On any roll where Hope die > Fear die: player gains 1 Hope.
- On any roll where Fear die > Hope die: GM gains 1 Fear.
- On Critical Success (matching dice): player gains 1 Hope AND clears 1 Stress.

## Core GM Principles

- Be a collaborative storyteller, not an adversarial judge.
- Describe by appearance and effect, not by game term.
- Let player decisions drive the narrative.
- Track resources rigorously -- Hope, Fear, HP, Stress, Armor Slots.
- Use Fear to create complications and tension, not to punish.

## NPC and Social Play

- Give each NPC a distinct voice, motivation, and secret.
- Scale information to what NPCs would realistically know.
- Deliver plot hooks through NPC interactions, not exposition.
- NPCs have their own agendas that advance between sessions.
```

- [ ] **Step 2: Create a minimal core skill file for testing**

Create `skills/01-core-mechanics.md`:
```markdown
# Core Mechanics: The Duality Dice System

## The Roll
Players roll two d12s called Duality Dice -- one Hope die and one Fear die.
The two dice are summed together, trait modifiers are added, and the total
is compared to a Difficulty set by the GM.

## Outcomes

| Outcome | Condition | Effect |
|---------|-----------|--------|
| Success with Hope | Total >= Difficulty AND Hope die > Fear die | Succeed. Player gains 1 Hope. |
| Success with Fear | Total >= Difficulty AND Fear die > Hope die | Succeed with a cost. GM gains 1 Fear. |
| Failure with Hope | Total < Difficulty AND Hope die > Fear die | Fail with minor consequence. Player gains 1 Hope. |
| Failure with Fear | Total < Difficulty AND Fear die > Hope die | Fail with major consequence. GM gains 1 Fear. |
| Critical Success | Both dice show same number | Auto success. Player gains 1 Hope AND clears 1 Stress. |

## Advantage and Disadvantage
- Advantage: Roll an additional d6, ADD to total.
- Disadvantage: Roll an additional d6, SUBTRACT from total.
- They cancel 1-for-1.

## Difficulty Guidelines

| Tier | Standard Difficulty |
|------|-------------------|
| Tier 1 (Level 1) | 11 |
| Tier 2 (Levels 2-4) | 14 |
| Tier 3 (Levels 5-7) | 17 |
| Tier 4 (Levels 8-10) | 20 |
```

- [ ] **Step 3: Write the failing tests**

```python
# tests/engine/test_skill_loader.py
import os
from pathlib import Path
from engine.skill_loader import load_skills, build_system_prompt, estimate_tokens

SKILLS_DIR = Path(__file__).resolve().parent.parent.parent / "skills"


class TestLoadSkills:
    def test_load_core_tier(self):
        text = load_skills(SKILLS_DIR, "core")
        assert "Player Agency" in text
        assert "Duality Dice" in text

    def test_skill_md_comes_first(self):
        text = load_skills(SKILLS_DIR, "core")
        # SKILL.md content should appear before other files
        skill_pos = text.find("Player Agency")
        core_pos = text.find("Duality Dice")
        assert skill_pos < core_pos

    def test_missing_file_skipped_with_warning(self):
        # With only SKILL.md and 01 existing, loading "full" tier should
        # skip missing files without crashing
        text = load_skills(SKILLS_DIR, "full")
        assert "Player Agency" in text

    def test_invalid_tier_raises(self):
        try:
            load_skills(SKILLS_DIR, "invalid_tier")
            assert False, "Should have raised ValueError"
        except ValueError:
            pass


class TestBuildSystemPrompt:
    def test_includes_preamble(self):
        prompt = build_system_prompt("test skills text")
        assert "Daggerheart RPG Game Master" in prompt
        assert "test skills text" in prompt

    def test_includes_separator(self):
        prompt = build_system_prompt("rules here")
        assert "DAGGERHEART GAME MASTER SKILL" in prompt


class TestEstimateTokens:
    def test_short_string(self):
        tokens = estimate_tokens("hello world")
        assert tokens > 0

    def test_empty_string(self):
        tokens = estimate_tokens("")
        assert tokens == 0

    def test_rough_accuracy(self):
        # "hello world" is 11 chars -> ~2-3 tokens
        tokens = estimate_tokens("hello world")
        assert 1 <= tokens <= 5
```

- [ ] **Step 4: Run tests to verify they fail**

Run: `python3 -m pytest tests/engine/test_skill_loader.py -v`
Expected: FAIL (cannot import engine.skill_loader)

- [ ] **Step 5: Write implementation**

```python
# engine/skill_loader.py
"""Load and compile Daggerheart skill files into a system prompt."""

import logging
from pathlib import Path

from config import SKILL_TIERS, SYSTEM_PROMPT_PREAMBLE, CHARS_PER_TOKEN

logger = logging.getLogger(__name__)


def estimate_tokens(text: str) -> int:
    """Rough token estimate: len(text) // 4.

    Args:
        text: Input text.

    Returns:
        Estimated token count.
    """
    if not text:
        return 0
    return len(text) // CHARS_PER_TOKEN


def load_skills(skills_dir: Path, tier: str) -> str:
    """Load skill files for the given tier and concatenate them.

    SKILL.md is always loaded first. Other files are appended with
    markdown separators. Missing files are skipped with a warning.

    Args:
        skills_dir: Path to the skills directory.
        tier: One of 'core', 'gm', 'full'.

    Returns:
        Concatenated skills text.

    Raises:
        ValueError: If tier is not recognized.
    """
    if tier not in SKILL_TIERS:
        raise ValueError(f"Unknown skill tier: {tier!r}. Must be one of: {list(SKILL_TIERS.keys())}")

    file_list = SKILL_TIERS[tier]
    parts = []

    for filename in file_list:
        filepath = skills_dir / filename
        if not filepath.exists():
            logger.warning("Skill file not found, skipping: %s", filepath)
            continue

        content = filepath.read_text(encoding="utf-8")

        if filename == "SKILL.md":
            parts.insert(0, content)
        else:
            parts.append(f"\n---\n# {filename}\n\n{content}")

    text = "\n".join(parts)
    tokens = estimate_tokens(text)
    logger.info("Loaded %d skill files (%s tier), ~%d tokens", len(parts), tier, tokens)
    return text


def build_system_prompt(skills_text: str) -> str:
    """Build the full system prompt from preamble + skills text.

    Args:
        skills_text: Concatenated skills text from load_skills().

    Returns:
        Complete system prompt string.
    """
    return SYSTEM_PROMPT_PREAMBLE + skills_text
```

- [ ] **Step 6: Run tests to verify they pass**

Run: `python3 -m pytest tests/engine/test_skill_loader.py -v`
Expected: All PASS

- [ ] **Step 7: Commit**

```bash
git add engine/skill_loader.py tests/engine/test_skill_loader.py skills/SKILL.md skills/01-core-mechanics.md
git commit -m "feat: add skill loader with tiered loading and system prompt builder"
```

---

### Task 5: Session Manager

**Files:**
- Create: `engine/session.py`
- Create: `tests/engine/test_session.py`

- [ ] **Step 1: Write the failing tests**

```python
# tests/engine/test_session.py
import json
import tempfile
from pathlib import Path
from engine.session import save_session, load_session


class TestSessionPersistence:
    def test_save_and_load_roundtrip(self):
        messages = [
            {"role": "system", "content": "You are a GM."},
            {"role": "user", "content": "I look around."},
            {"role": "assistant", "content": "You see a dark cave."},
        ]
        with tempfile.NamedTemporaryFile(suffix=".json", delete=False) as f:
            path = Path(f.name)
        try:
            save_session(messages, path)
            loaded = load_session(path)
            assert len(loaded) == 3
            assert loaded[0]["role"] == "system"
            assert loaded[1]["content"] == "I look around."
            assert loaded[2]["content"] == "You see a dark cave."
        finally:
            path.unlink(missing_ok=True)

    def test_save_creates_parent_dirs(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            path = Path(tmpdir) / "sub" / "dir" / "session.json"
            messages = [{"role": "system", "content": "test"}]
            save_session(messages, path)
            assert path.exists()

    def test_load_replaces_system_prompt(self):
        messages = [
            {"role": "system", "content": "old prompt"},
            {"role": "user", "content": "hello"},
        ]
        with tempfile.NamedTemporaryFile(suffix=".json", delete=False) as f:
            path = Path(f.name)
        try:
            save_session(messages, path)
            loaded = load_session(path, new_system_prompt="new prompt")
            assert loaded[0]["content"] == "new prompt"
            assert loaded[1]["content"] == "hello"
        finally:
            path.unlink(missing_ok=True)

    def test_load_without_replacement_keeps_original(self):
        messages = [
            {"role": "system", "content": "original"},
            {"role": "user", "content": "hi"},
        ]
        with tempfile.NamedTemporaryFile(suffix=".json", delete=False) as f:
            path = Path(f.name)
        try:
            save_session(messages, path)
            loaded = load_session(path)
            assert loaded[0]["content"] == "original"
        finally:
            path.unlink(missing_ok=True)

    def test_saved_json_is_valid(self):
        messages = [{"role": "system", "content": "test"}]
        with tempfile.NamedTemporaryFile(suffix=".json", delete=False) as f:
            path = Path(f.name)
        try:
            save_session(messages, path)
            with open(path) as f:
                data = json.load(f)
            assert isinstance(data, list)
        finally:
            path.unlink(missing_ok=True)
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `python3 -m pytest tests/engine/test_session.py -v`
Expected: FAIL (cannot import engine.session)

- [ ] **Step 3: Write implementation**

```python
# engine/session.py
"""Session persistence for Daggerheart Campaign Tool.

Sessions are stored as JSON arrays of message dicts, matching the
OpenAI chat completion message format.
"""

import json
import logging
from pathlib import Path

logger = logging.getLogger(__name__)


def save_session(messages: list[dict], path: Path) -> None:
    """Save a session (message list) to a JSON file.

    Creates parent directories if they don't exist.

    Args:
        messages: List of message dicts with 'role' and 'content' keys.
        path: File path to save to.
    """
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(messages, f, indent=2, ensure_ascii=False)
    logger.info("Session saved to %s (%d messages)", path, len(messages))


def load_session(path: Path, new_system_prompt: str | None = None) -> list[dict]:
    """Load a session from a JSON file.

    Optionally replaces the system prompt (message at index 0) with a new one,
    allowing skill files to be updated while preserving conversation history.

    Args:
        path: File path to load from.
        new_system_prompt: If provided, replaces the system message content.

    Returns:
        List of message dicts.
    """
    with open(path, "r", encoding="utf-8") as f:
        messages = json.load(f)

    if new_system_prompt and messages and messages[0]["role"] == "system":
        messages[0]["content"] = new_system_prompt
        logger.info("Replaced system prompt in loaded session")

    logger.info("Loaded session from %s (%d messages)", path, len(messages))
    return messages
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `python3 -m pytest tests/engine/test_session.py -v`
Expected: All PASS

- [ ] **Step 5: Commit**

```bash
git add engine/session.py tests/engine/test_session.py
git commit -m "feat: add session manager with save/load and system prompt replacement"
```

---

### Task 6: Run full test suite

- [ ] **Step 1: Run all tests**

Run: `python3 -m pytest tests/ -v`
Expected: All PASS (config, dice, skill_loader, session tests)

- [ ] **Step 2: Verify project structure**

Run: `find . -name "*.py" -not -path "./.git/*" | sort`

Expected output:
```
./campaign/__init__.py
./config.py
./engine/__init__.py
./engine/dice.py
./engine/session.py
./engine/skill_loader.py
./tests/__init__.py
./tests/engine/__init__.py
./tests/engine/test_dice.py
./tests/engine/test_session.py
./tests/engine/test_skill_loader.py
./tests/campaign/__init__.py
./tests/test_config.py
./ui/__init__.py
```

---

## Chunk 2: LLM Agent and Campaign Data Layer

This chunk adds the LLM agent (chat loop, pruning, retry logic) and the campaign data layer (character sheets, party tracker, campaign state). After this chunk, you can have a conversation with an AI GM in the terminal and manage characters/party state.

### Task 7: LLM Agent

**Files:**
- Create: `engine/agent.py`
- Create: `tests/engine/test_agent.py`

- [ ] **Step 1: Write the failing tests**

```python
# tests/engine/test_agent.py
from engine.agent import estimate_message_tokens, prune_messages


class TestEstimateMessageTokens:
    def test_single_message(self):
        msgs = [{"role": "user", "content": "hello world"}]
        tokens = estimate_message_tokens(msgs)
        assert tokens > 0

    def test_includes_overhead(self):
        # Each message adds 10 tokens overhead
        msgs = [{"role": "user", "content": ""}]
        tokens = estimate_message_tokens(msgs)
        assert tokens == 10  # empty content + 10 overhead

    def test_multiple_messages(self):
        msgs = [
            {"role": "system", "content": "a" * 400},  # 100 + 10 = 110
            {"role": "user", "content": "b" * 40},  # 10 + 10 = 20
        ]
        tokens = estimate_message_tokens(msgs)
        assert tokens == 130


class TestPruneMessages:
    def test_no_pruning_when_under_limit(self):
        msgs = [
            {"role": "system", "content": "sys"},
            {"role": "user", "content": "hi"},
        ]
        pruned = prune_messages(msgs, max_tokens=10000)
        assert len(pruned) == 2

    def test_preserves_system_message(self):
        sys_content = "x" * 4000  # ~1000 tokens + 10 overhead
        msgs = [
            {"role": "system", "content": sys_content},
            {"role": "user", "content": "a" * 400},
            {"role": "assistant", "content": "b" * 400},
            {"role": "user", "content": "c" * 400},
        ]
        # Limit is tight -- should drop oldest non-system messages
        pruned = prune_messages(msgs, max_tokens=1200)
        assert pruned[0]["role"] == "system"
        assert pruned[0]["content"] == sys_content
        # At least system message preserved
        assert len(pruned) >= 1

    def test_drops_oldest_first(self):
        msgs = [
            {"role": "system", "content": "sys"},
            {"role": "user", "content": "first"},
            {"role": "assistant", "content": "second"},
            {"role": "user", "content": "third"},
        ]
        # Set limit so only system + one message fits
        pruned = prune_messages(msgs, max_tokens=50)
        assert pruned[0]["content"] == "sys"
        # The last message should be preserved over the first
        if len(pruned) > 1:
            assert pruned[-1]["content"] == "third"
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `python3 -m pytest tests/engine/test_agent.py -v`
Expected: FAIL (cannot import engine.agent)

- [ ] **Step 3: Write implementation**

```python
# engine/agent.py
"""LLM chat agent for Daggerheart Campaign Tool.

Handles API calls, message pruning, and retry logic.
Uses the OpenAI-compatible API format.
"""

import logging
import time

from config import CHARS_PER_TOKEN, DEFAULT_MAX_TOKENS, DEFAULT_TEMPERATURE

logger = logging.getLogger(__name__)

MAX_RETRIES = 5


def estimate_message_tokens(messages: list[dict]) -> int:
    """Estimate total tokens for a list of messages.

    Uses rough estimate of len(content) // 4 + 10 per message.

    Args:
        messages: List of message dicts.

    Returns:
        Estimated total token count.
    """
    total = 0
    for msg in messages:
        content = msg.get("content", "")
        total += len(content) // CHARS_PER_TOKEN + 10
    return total


def prune_messages(messages: list[dict], max_tokens: int) -> list[dict]:
    """Prune messages to fit within token budget using FIFO strategy.

    Always preserves the system message (index 0). Drops oldest
    non-system messages first.

    Args:
        messages: List of message dicts.
        max_tokens: Maximum allowed tokens.

    Returns:
        Pruned list of messages.
    """
    if estimate_message_tokens(messages) <= max_tokens:
        return messages

    system_msgs = [m for m in messages if m["role"] == "system"]
    non_system = [m for m in messages if m["role"] != "system"]

    while non_system and estimate_message_tokens(system_msgs + non_system) > max_tokens:
        dropped = non_system.pop(0)
        logger.debug("Pruned message: %s...", dropped["content"][:50])

    return system_msgs + non_system


class DaggerheartAgent:
    """LLM agent that manages chat interactions.

    Args:
        client: An OpenAI-compatible client instance.
        model: Model identifier string.
        system_prompt: The system prompt (rules + instructions).
        max_context: Maximum context window size in tokens.
        temperature: Sampling temperature.
    """

    def __init__(
        self,
        client,
        model: str,
        system_prompt: str,
        max_context: int,
        temperature: float = DEFAULT_TEMPERATURE,
    ):
        self.client = client
        self.model = model
        self.system_prompt = system_prompt
        self.max_context = max_context
        self.temperature = temperature
        self.total_tokens_used = 0

    def send(self, messages: list[dict]) -> str:
        """Send messages to the LLM and return the response.

        Handles pruning and retry with exponential backoff on rate limits.

        Args:
            messages: Full message history including system prompt.

        Returns:
            Assistant response content string.
        """
        messages = prune_messages(messages, self.max_context)

        for attempt in range(MAX_RETRIES):
            try:
                response = self.client.chat.completions.create(
                    model=self.model,
                    messages=messages,
                    temperature=self.temperature,
                    max_tokens=DEFAULT_MAX_TOKENS,
                )
                choice = response.choices[0]

                if choice.finish_reason == "length":
                    logger.warning("Response truncated (finish_reason=length)")

                if response.usage:
                    self.total_tokens_used += response.usage.total_tokens

                return choice.message.content or ""

            except Exception as e:
                error_str = str(e).lower()
                if "429" in error_str or "rate" in error_str:
                    wait = 2**attempt + 1
                    logger.warning("Rate limited, retrying in %ds (attempt %d/%d)", wait, attempt + 1, MAX_RETRIES)
                    time.sleep(wait)
                else:
                    raise

        raise RuntimeError(f"Failed after {MAX_RETRIES} retries due to rate limiting")
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `python3 -m pytest tests/engine/test_agent.py -v`
Expected: All PASS

- [ ] **Step 5: Commit**

```bash
git add engine/agent.py tests/engine/test_agent.py
git commit -m "feat: add LLM agent with message pruning and rate limit retry"
```

---

### Task 8: Campaign State Manager

**Files:**
- Create: `campaign/state.py`
- Create: `tests/campaign/test_state.py`

- [ ] **Step 1: Write the failing tests**

```python
# tests/campaign/test_state.py
import tempfile
from pathlib import Path
from campaign.state import CampaignState, create_campaign, load_campaign


class TestCampaignState:
    def test_create_campaign(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            base = Path(tmpdir) / "campaigns"
            state = create_campaign("test-quest", base)
            assert state.name == "test-quest"
            assert state.fear == 0
            assert state.consecutive_short_rests == 0
            # Verify directory structure
            assert (base / "test-quest" / "party").is_dir()
            assert (base / "test-quest" / "npcs").is_dir()
            assert (base / "test-quest" / "adversaries").is_dir()
            assert (base / "test-quest" / "encounters").is_dir()
            assert (base / "test-quest" / "world").is_dir()
            assert (base / "test-quest" / "journal").is_dir()
            assert (base / "test-quest" / "sessions").is_dir()
            assert (base / "test-quest" / "campaign.json").is_file()

    def test_save_and_load_roundtrip(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            base = Path(tmpdir) / "campaigns"
            state = create_campaign("roundtrip", base)
            state.fear = 5
            state.consecutive_short_rests = 2
            state.countdowns = [{"name": "Dragon Attack", "current": 3, "max": 6, "type": "campaign"}]
            state.save()

            loaded = load_campaign("roundtrip", base)
            assert loaded.fear == 5
            assert loaded.consecutive_short_rests == 2
            assert len(loaded.countdowns) == 1
            assert loaded.countdowns[0]["name"] == "Dragon Attack"

    def test_fear_clamped_to_max(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            base = Path(tmpdir) / "campaigns"
            state = create_campaign("fear-test", base)
            state.fear = 15
            assert state.fear == 12  # clamped to max

    def test_campaign_path(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            base = Path(tmpdir) / "campaigns"
            state = create_campaign("my-campaign", base)
            assert state.campaign_dir == base / "my-campaign"
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `python3 -m pytest tests/campaign/test_state.py -v`
Expected: FAIL (cannot import campaign.state)

- [ ] **Step 3: Write implementation**

```python
# campaign/state.py
"""Campaign state management for Daggerheart Campaign Tool.

Handles creation, loading, and saving of campaign metadata
including Fear counter, rest tracking, and countdowns.
"""

import json
import logging
from pathlib import Path

logger = logging.getLogger(__name__)

MAX_FEAR = 12

CAMPAIGN_SUBDIRS = [
    "party",
    "npcs",
    "adversaries",
    "encounters",
    "world",
    "journal",
    "sessions",
]


class CampaignState:
    """Represents the state of a Daggerheart campaign.

    Attributes:
        name: Campaign name.
        campaign_dir: Path to the campaign directory.
        countdowns: List of countdown dicts.
        consecutive_short_rests: Number of consecutive short rests taken.
    """

    def __init__(self, name: str, campaign_dir: Path):
        self.name = name
        self.campaign_dir = campaign_dir
        self._fear = 0
        self.consecutive_short_rests = 0
        self.countdowns: list[dict] = []
        self.current_location = ""
        self.notes = ""

    @property
    def fear(self) -> int:
        return self._fear

    @fear.setter
    def fear(self, value: int):
        self._fear = max(0, min(value, MAX_FEAR))

    def save(self) -> None:
        """Save campaign state to campaign.json."""
        data = {
            "name": self.name,
            "fear": self.fear,
            "consecutive_short_rests": self.consecutive_short_rests,
            "countdowns": self.countdowns,
            "current_location": self.current_location,
            "notes": self.notes,
        }
        path = self.campaign_dir / "campaign.json"
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        logger.info("Campaign state saved to %s", path)

    @classmethod
    def from_dict(cls, data: dict, campaign_dir: Path) -> "CampaignState":
        """Create a CampaignState from a dict (loaded from JSON)."""
        state = cls(data["name"], campaign_dir)
        state.fear = data.get("fear", 0)
        state.consecutive_short_rests = data.get("consecutive_short_rests", 0)
        state.countdowns = data.get("countdowns", [])
        state.current_location = data.get("current_location", "")
        state.notes = data.get("notes", "")
        return state


def create_campaign(name: str, campaigns_base: Path) -> CampaignState:
    """Create a new campaign with the required directory structure.

    Args:
        name: Campaign name (used as directory name).
        campaigns_base: Base path for all campaigns.

    Returns:
        New CampaignState instance.
    """
    campaign_dir = campaigns_base / name
    for subdir in CAMPAIGN_SUBDIRS:
        (campaign_dir / subdir).mkdir(parents=True, exist_ok=True)

    state = CampaignState(name, campaign_dir)
    state.save()
    logger.info("Created campaign '%s' at %s", name, campaign_dir)
    return state


def load_campaign(name: str, campaigns_base: Path) -> CampaignState:
    """Load an existing campaign from disk.

    Args:
        name: Campaign name.
        campaigns_base: Base path for all campaigns.

    Returns:
        Loaded CampaignState instance.

    Raises:
        FileNotFoundError: If campaign.json doesn't exist.
    """
    campaign_dir = campaigns_base / name
    path = campaign_dir / "campaign.json"
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    return CampaignState.from_dict(data, campaign_dir)
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `python3 -m pytest tests/campaign/test_state.py -v`
Expected: All PASS

- [ ] **Step 5: Commit**

```bash
git add campaign/state.py tests/campaign/test_state.py
git commit -m "feat: add campaign state manager with Fear tracking, rests, and countdowns"
```

---

### Task 9: Character Sheet Manager

**Files:**
- Create: `campaign/character.py`
- Create: `tests/campaign/test_character.py`

- [ ] **Step 1: Write the failing tests**

```python
# tests/campaign/test_character.py
import json
import tempfile
from pathlib import Path
from campaign.character import (
    Character,
    save_character,
    load_character,
    list_characters,
    validate_character,
    get_effective_thresholds,
)


SAMPLE_CHARACTER = {
    "name": "Kira Ashveil",
    "class": "Sorcerer",
    "subclass": "Elemental Origin",
    "level": 1,
    "tier": 1,
    "ancestry": "Drakona",
    "community": "Wildborne",
    "traits": {
        "agility": 0, "strength": -1, "finesse": 1,
        "instinct": 1, "presence": 0, "knowledge": 2,
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
        "base_major": 5,
        "base_severe": 11,
        "feature": "Flexible: +1 Evasion",
    },
    "weapons": [
        {
            "name": "Staff",
            "trait": "knowledge",
            "range": "melee",
            "damage": "d8+2",
            "burden": "two-handed",
            "type": "physical",
        }
    ],
    "domains": ["Arcana", "Midnight"],
    "domain_cards": {"loadout": [], "vault": []},
    "subclass_card": "foundation",
    "ancestry_features": [],
    "community_feature": "",
    "experiences": [
        {"name": "Volcano-born", "modifier": 2},
        {"name": "Reckless", "modifier": 2},
    ],
    "connections": [],
}


class TestCharacter:
    def test_from_dict(self):
        char = Character.from_dict(SAMPLE_CHARACTER)
        assert char.name == "Kira Ashveil"
        assert char.char_class == "Sorcerer"
        assert char.level == 1

    def test_to_dict_roundtrip(self):
        char = Character.from_dict(SAMPLE_CHARACTER)
        d = char.to_dict()
        assert d["name"] == "Kira Ashveil"
        assert d["traits"]["knowledge"] == 2

    def test_save_and_load(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            party_dir = Path(tmpdir)
            char = Character.from_dict(SAMPLE_CHARACTER)
            save_character(char, party_dir)

            loaded = load_character("Kira Ashveil", party_dir)
            assert loaded.name == "Kira Ashveil"
            assert loaded.char_class == "Sorcerer"

    def test_list_characters(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            party_dir = Path(tmpdir)
            char = Character.from_dict(SAMPLE_CHARACTER)
            save_character(char, party_dir)
            names = list_characters(party_dir)
            assert "Kira Ashveil" in names

    def test_effective_thresholds_level_1(self):
        char = Character.from_dict(SAMPLE_CHARACTER)
        major, severe = get_effective_thresholds(char)
        assert major == 6  # base 5 + level 1
        assert severe == 12  # base 11 + level 1

    def test_effective_thresholds_level_5(self):
        data = {**SAMPLE_CHARACTER, "level": 5}
        char = Character.from_dict(data)
        major, severe = get_effective_thresholds(char)
        assert major == 10  # base 5 + level 5
        assert severe == 16  # base 11 + level 5


class TestValidateCharacter:
    def test_valid_character(self):
        errors = validate_character(SAMPLE_CHARACTER)
        assert len(errors) == 0

    def test_invalid_trait_spread(self):
        data = {**SAMPLE_CHARACTER}
        data["traits"] = {
            "agility": 3, "strength": 3, "finesse": 3,
            "instinct": 3, "presence": 3, "knowledge": 3,
        }
        errors = validate_character(data)
        assert any("trait" in e.lower() for e in errors)

    def test_missing_required_field(self):
        data = {k: v for k, v in SAMPLE_CHARACTER.items() if k != "name"}
        errors = validate_character(data)
        assert any("name" in e.lower() for e in errors)
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `python3 -m pytest tests/campaign/test_character.py -v`
Expected: FAIL

- [ ] **Step 3: Write implementation**

```python
# campaign/character.py
"""Character sheet management for Daggerheart Campaign Tool.

Handles creation, validation, saving, and loading of character sheets
stored as JSON files.
"""

import json
import logging
import re
from pathlib import Path

logger = logging.getLogger(__name__)

VALID_CLASSES = [
    "Bard", "Druid", "Guardian", "Ranger", "Rogue",
    "Seraph", "Sorcerer", "Warrior", "Wizard",
]

VALID_TRAITS = ["agility", "strength", "finesse", "instinct", "presence", "knowledge"]

# Standard trait spread: +2, +1, +1, +0, +0, -1 => sum = 3
TRAIT_SPREAD_SUM = 3
TRAIT_SPREAD_SORTED = [-1, 0, 0, 1, 1, 2]

REQUIRED_FIELDS = [
    "name", "class", "subclass", "level", "tier", "ancestry", "community",
    "traits", "evasion", "proficiency", "hp", "stress", "hope", "armor",
    "weapons", "domains", "domain_cards", "experiences",
]


class Character:
    """Represents a Daggerheart player character."""

    def __init__(self, data: dict):
        self.name: str = data["name"]
        self.char_class: str = data["class"]
        self.subclass: str = data["subclass"]
        self.level: int = data["level"]
        self.tier: int = data["tier"]
        self.ancestry: str = data["ancestry"]
        self.community: str = data["community"]
        self.traits: dict = data["traits"]
        self.evasion: int = data["evasion"]
        self.proficiency: int = data["proficiency"]
        self.hp: dict = data["hp"]
        self.stress: dict = data["stress"]
        self.hope: dict = data["hope"]
        self.armor: dict = data["armor"]
        self.weapons: list = data["weapons"]
        self.domains: list = data["domains"]
        self.domain_cards: dict = data["domain_cards"]
        self.subclass_card: str = data.get("subclass_card", "foundation")
        self.ancestry_features: list = data.get("ancestry_features", [])
        self.community_feature: str = data.get("community_feature", "")
        self.experiences: list = data.get("experiences", [])
        self.connections: list = data.get("connections", [])

    @classmethod
    def from_dict(cls, data: dict) -> "Character":
        return cls(data)

    def to_dict(self) -> dict:
        return {
            "name": self.name,
            "class": self.char_class,
            "subclass": self.subclass,
            "level": self.level,
            "tier": self.tier,
            "ancestry": self.ancestry,
            "community": self.community,
            "traits": self.traits,
            "evasion": self.evasion,
            "proficiency": self.proficiency,
            "hp": self.hp,
            "stress": self.stress,
            "hope": self.hope,
            "armor": self.armor,
            "weapons": self.weapons,
            "domains": self.domains,
            "domain_cards": self.domain_cards,
            "subclass_card": self.subclass_card,
            "ancestry_features": self.ancestry_features,
            "community_feature": self.community_feature,
            "experiences": self.experiences,
            "connections": self.connections,
        }


def _safe_filename(name: str) -> str:
    """Convert a character name to a safe filename."""
    return re.sub(r"[^\w\s-]", "", name).strip().replace(" ", "_").lower() + ".json"


def save_character(character: Character, party_dir: Path) -> Path:
    """Save a character sheet to the party directory.

    Args:
        character: Character instance.
        party_dir: Path to the party directory.

    Returns:
        Path to the saved file.
    """
    party_dir.mkdir(parents=True, exist_ok=True)
    path = party_dir / _safe_filename(character.name)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(character.to_dict(), f, indent=2, ensure_ascii=False)
    logger.info("Saved character '%s' to %s", character.name, path)
    return path


def load_character(name: str, party_dir: Path) -> Character:
    """Load a character by name from the party directory.

    Args:
        name: Character name.
        party_dir: Path to the party directory.

    Returns:
        Character instance.
    """
    path = party_dir / _safe_filename(name)
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    return Character.from_dict(data)


def list_characters(party_dir: Path) -> list[str]:
    """List all character names in the party directory.

    Args:
        party_dir: Path to the party directory.

    Returns:
        List of character names.
    """
    names = []
    if not party_dir.exists():
        return names
    for path in sorted(party_dir.glob("*.json")):
        with open(path) as f:
            data = json.load(f)
        names.append(data["name"])
    return names


def get_effective_thresholds(character: Character) -> tuple[int, int]:
    """Compute effective damage thresholds (base + level).

    Args:
        character: Character instance.

    Returns:
        Tuple of (effective_major, effective_severe).
    """
    base_major = character.armor.get("base_major", 0)
    base_severe = character.armor.get("base_severe", 0)
    return base_major + character.level, base_severe + character.level


def validate_character(data: dict) -> list[str]:
    """Validate a character sheet dict against Daggerheart rules.

    Args:
        data: Character data dict.

    Returns:
        List of validation error strings. Empty list means valid.
    """
    errors = []

    for field in REQUIRED_FIELDS:
        if field not in data:
            errors.append(f"Missing required field: '{field}'")

    if "traits" in data:
        traits = data["traits"]
        level = data.get("level", 1)
        if level == 1 and sorted(traits.values()) != TRAIT_SPREAD_SORTED:
            errors.append(
                f"Level 1 trait spread must be +2/+1/+1/+0/+0/-1 (sorted values: {TRAIT_SPREAD_SORTED}), "
                f"got sorted values: {sorted(traits.values())}"
            )
        elif level > 1 and sum(traits.values()) < TRAIT_SPREAD_SUM:
            errors.append(
                f"Trait values sum ({sum(traits.values())}) is less than minimum ({TRAIT_SPREAD_SUM})"
            )

    if "class" in data and data["class"] not in VALID_CLASSES:
        errors.append(f"Invalid class: '{data['class']}'. Must be one of: {VALID_CLASSES}")

    return errors
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `python3 -m pytest tests/campaign/test_character.py -v`
Expected: All PASS

- [ ] **Step 5: Commit**

```bash
git add campaign/character.py tests/campaign/test_character.py
git commit -m "feat: add character sheet manager with validation and threshold computation"
```

---

### Task 10: Party Tracker

**Files:**
- Create: `campaign/party.py`
- Create: `tests/campaign/test_party.py`

- [ ] **Step 1: Write the failing tests**

```python
# tests/campaign/test_party.py
import tempfile
from pathlib import Path
from campaign.character import Character, save_character
from campaign.party import (
    load_party,
    get_party_summary,
    build_campaign_context,
)

CHAR_DATA_1 = {
    "name": "Kira", "class": "Sorcerer", "subclass": "Elemental Origin",
    "level": 1, "tier": 1, "ancestry": "Drakona", "community": "Wildborne",
    "traits": {"agility": 0, "strength": -1, "finesse": 1, "instinct": 1, "presence": 0, "knowledge": 2},
    "evasion": 10, "proficiency": 1,
    "hp": {"max": 6, "marked": 1}, "stress": {"max": 6, "marked": 0},
    "hope": {"current": 3, "max": 6, "scars": 0},
    "armor": {"name": "Gambeson", "base_score": 3, "slots_marked": 0, "base_major": 5, "base_severe": 11, "feature": ""},
    "weapons": [], "domains": ["Arcana", "Midnight"],
    "domain_cards": {"loadout": [], "vault": []},
    "experiences": [{"name": "Test", "modifier": 2}],
}

CHAR_DATA_2 = {
    "name": "Bron", "class": "Guardian", "subclass": "Stalwart",
    "level": 1, "tier": 1, "ancestry": "Dwarf", "community": "Ridgeborne",
    "traits": {"agility": -1, "strength": 2, "finesse": 0, "instinct": 0, "presence": 1, "knowledge": 1},
    "evasion": 9, "proficiency": 1,
    "hp": {"max": 7, "marked": 0}, "stress": {"max": 6, "marked": 2},
    "hope": {"current": 2, "max": 6, "scars": 0},
    "armor": {"name": "Chainmail", "base_score": 4, "slots_marked": 1, "base_major": 7, "base_severe": 15, "feature": ""},
    "weapons": [], "domains": ["Blade", "Valor"],
    "domain_cards": {"loadout": [], "vault": []},
    "experiences": [{"name": "Test", "modifier": 2}],
}


class TestParty:
    def test_load_party(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            party_dir = Path(tmpdir)
            save_character(Character.from_dict(CHAR_DATA_1), party_dir)
            save_character(Character.from_dict(CHAR_DATA_2), party_dir)
            party = load_party(party_dir)
            assert len(party) == 2
            names = [c.name for c in party]
            assert "Kira" in names
            assert "Bron" in names

    def test_party_summary(self):
        chars = [Character.from_dict(CHAR_DATA_1), Character.from_dict(CHAR_DATA_2)]
        summary = get_party_summary(chars)
        assert "Kira" in summary
        assert "Bron" in summary
        assert "Sorcerer" in summary

    def test_build_campaign_context(self):
        chars = [Character.from_dict(CHAR_DATA_1)]
        context = build_campaign_context(
            characters=chars,
            fear=3,
            countdowns=[{"name": "Storm", "current": 2, "max": 5, "type": "campaign"}],
            current_location="The Silver Mines",
            journal_summary="Last session the party entered the mines.",
        )
        assert "Kira" in context
        assert "Fear: 3" in context
        assert "Storm" in context
        assert "Silver Mines" in context
        assert "entered the mines" in context
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `python3 -m pytest tests/campaign/test_party.py -v`
Expected: FAIL

- [ ] **Step 3: Write implementation**

```python
# campaign/party.py
"""Party tracker for Daggerheart Campaign Tool.

Manages the party roster, provides summary views, and builds
campaign context messages for injection into the LLM conversation.
"""

import json
from pathlib import Path

from campaign.character import Character, get_effective_thresholds


def load_party(party_dir: Path) -> list[Character]:
    """Load all characters from the party directory.

    Args:
        party_dir: Path to the party directory.

    Returns:
        List of Character instances.
    """
    characters = []
    if not party_dir.exists():
        return characters
    for path in sorted(party_dir.glob("*.json")):
        with open(path) as f:
            data = json.load(f)
        characters.append(Character.from_dict(data))
    return characters


def get_party_summary(characters: list[Character]) -> str:
    """Generate a text summary of the party.

    Args:
        characters: List of Character instances.

    Returns:
        Formatted party summary string.
    """
    if not characters:
        return "No party members."

    lines = []
    for c in characters:
        major, severe = get_effective_thresholds(c)
        lines.append(
            f"- {c.name} | {c.char_class} ({c.subclass}) | Level {c.level} | "
            f"HP: {c.hp['marked']}/{c.hp['max']} | "
            f"Stress: {c.stress['marked']}/{c.stress['max']} | "
            f"Hope: {c.hope['current']}/{c.hope['max']} | "
            f"Armor: {c.armor['slots_marked']}/{c.armor['base_score']} | "
            f"Evasion: {c.evasion} | Thresholds: {major}/{severe}"
        )
    return "\n".join(lines)


def build_campaign_context(
    characters: list[Character],
    fear: int = 0,
    countdowns: list[dict] | None = None,
    current_location: str = "",
    journal_summary: str = "",
) -> str:
    """Build a campaign context message for LLM injection.

    This is injected as a system message at position 1 in the conversation,
    providing the LLM with current campaign state.

    Args:
        characters: Party members.
        fear: Current GM Fear counter.
        countdowns: Active countdown clocks.
        current_location: Current party location.
        journal_summary: Summary of the most recent session.

    Returns:
        Formatted campaign context string.
    """
    parts = ["=== CURRENT CAMPAIGN STATE ==="]

    # Party roster
    parts.append("\n## Party")
    parts.append(f"Party size: {len(characters)}")
    if characters:
        parts.append(get_party_summary(characters))

    # Fear
    parts.append(f"\n## GM Resources\nFear: {fear}/12")

    # Countdowns
    if countdowns:
        parts.append("\n## Active Countdowns")
        for cd in countdowns:
            parts.append(f"- {cd['name']}: {cd['current']}/{cd['max']} ({cd.get('type', 'standard')})")

    # Location
    if current_location:
        parts.append(f"\n## Current Location\n{current_location}")

    # Journal
    if journal_summary:
        parts.append(f"\n## Recent Events\n{journal_summary}")

    return "\n".join(parts)
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `python3 -m pytest tests/campaign/test_party.py -v`
Expected: All PASS

- [ ] **Step 5: Commit**

```bash
git add campaign/party.py tests/campaign/test_party.py
git commit -m "feat: add party tracker with summary and campaign context builder"
```

---

### Task 11: Run full test suite

- [ ] **Step 1: Run all tests**

Run: `python3 -m pytest tests/ -v`
Expected: All PASS (config, dice, skill_loader, session, agent, state, character, party)

---

## Chunk 3: Terminal UI and Entry Point

This chunk wires everything together into a working terminal-mode application. After this chunk, you can run `python3 daggerheart.py --provider abacus --api-key KEY` and play Daggerheart with an AI GM in the terminal.

### Task 12: Terminal UI

**Files:**
- Create: `ui/terminal.py`

- [ ] **Step 1: Write implementation**

Note: Terminal UI is interactive (REPL loop), so we test it indirectly through integration. The core logic (agent, dice, session) is already tested.

```python
# ui/terminal.py
"""Terminal chat interface for Daggerheart Campaign Tool."""

import sys
from datetime import datetime
from pathlib import Path

from config import VERSION
from engine.agent import DaggerheartAgent, estimate_message_tokens
from engine.dice import roll, roll_duality
from engine.session import save_session


GREETING = """Welcome to the world of Daggerheart!

Choose how to begin:
1. Start a new campaign
2. Continue an existing campaign
3. Run a one-shot adventure
4. Create a character

What would you like to do?"""


def _print_status(agent, messages, campaign=None, party=None):
    tokens = estimate_message_tokens(messages)
    msg_count = len([m for m in messages if m["role"] != "system"])
    parts = [
        f"Model: {agent.model}",
        f"Tokens: ~{tokens}",
        f"Messages: {msg_count}",
        f"API tokens: {agent.total_tokens_used}",
    ]
    if campaign:
        parts.append(f"Fear: {campaign.fear}/12")
    if party:
        for c in party:
            parts.append(f"{c.name}: HP {c.hp['marked']}/{c.hp['max']} Stress {c.stress['marked']}/{c.stress['max']} Hope {c.hope['current']}/{c.hope['max']}")
    print("\n[Status] " + " | ".join(parts))


def _handle_roll_command(args: str) -> str | None:
    """Handle the 'roll' command, returning a result string."""
    if not args:
        return "Usage: roll <notation> (e.g., roll 2d12, roll 1d8+3)"
    try:
        result = roll(args)
        return f"Rolled {result.notation}: {result.dice} + {result.modifier} = {result.total}"
    except ValueError as e:
        return f"Invalid dice notation: {e}"


def _handle_duality_command(args: str) -> str:
    """Handle the 'duality' command. Optional args: modifier difficulty."""
    parts = args.split() if args else []
    modifier = int(parts[0]) if len(parts) >= 1 else 0
    difficulty = int(parts[1]) if len(parts) >= 2 else 11
    result = roll_duality(modifier=modifier, difficulty=difficulty)
    outcome_labels = {
        "success_hope": "Success with Hope",
        "success_fear": "Success with Fear",
        "failure_hope": "Failure with Hope",
        "failure_fear": "Failure with Fear",
        "critical": "CRITICAL SUCCESS!",
    }
    label = outcome_labels.get(result.outcome_type, result.outcome_type)
    lines = [
        f"Duality Roll: Hope [{result.hope_die}] Fear [{result.fear_die}]",
        f"   Total: {result.raw_total} + {modifier} = {result.modified_total} vs Difficulty {result.difficulty}",
        f"   Result: {label}",
    ]
    if result.hope_gained:
        lines.append("   -> Player gains 1 Hope")
    if result.fear_gained:
        lines.append("   -> GM gains 1 Fear")
    if result.stress_cleared:
        lines.append("   -> Player clears 1 Stress")
    return "\n".join(lines)


def run_terminal(
    agent: DaggerheartAgent,
    messages: list[dict],
    session_path: Path | None = None,
    campaign_name: str = "",
    tier: str = "full",
    campaign=None,
    party: list | None = None,
):
    """Run the interactive terminal chat loop.

    Args:
        agent: Configured DaggerheartAgent.
        messages: Initial message list (with system prompt).
        session_path: Path to save session files.
        campaign_name: Name of active campaign (for display).
        tier: Skill tier loaded (for display).
        campaign: CampaignState instance (or None).
        party: List of Character instances (or None).
    """
    if session_path is None:
        session_path = Path("sessions") / f"session-{datetime.now().strftime('%Y%m%d-%H%M%S')}.json"

    # Header
    parts = [f"Daggerheart GM v{VERSION}", f"Model: {agent.model}", f"Tier: {tier}"]
    if campaign_name:
        parts.append(f"Campaign: {campaign_name}")
    print(" | ".join(parts))
    print("Type 'help' for commands.\n")

    # Show greeting if this is a new session
    if len(messages) <= 2:  # system prompt + optional context
        print(f"GM> {GREETING}\n")
        messages.append({"role": "assistant", "content": GREETING})

    while True:
        try:
            user_input = input("> ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\n")
            user_input = "quit"

        if not user_input:
            continue

        # Handle commands
        cmd = user_input.lower().split()[0]
        cmd_args = user_input[len(cmd):].strip()

        if cmd in ("quit", "exit"):
            save_session(messages, session_path)
            print(f"Session saved to {session_path}. Goodbye!")
            break

        elif cmd == "save":
            save_session(messages, session_path)
            print(f"Session saved to {session_path}")
            continue

        elif cmd == "status":
            _print_status(agent, messages, campaign, party)
            continue

        elif cmd == "roll":
            print(_handle_roll_command(cmd_args))
            continue

        elif cmd == "duality":
            print(_handle_duality_command(cmd_args))
            continue

        elif cmd == "party":
            if party:
                from campaign.party import get_party_summary
                print(f"\n{get_party_summary(party)}\n")
            else:
                print("No party loaded. Use --campaign to load a campaign.")
            continue

        elif cmd == "hope":
            if party:
                for c in party:
                    print(f"  {c.name}: Hope {c.hope['current']}/{c.hope['max']} (Scars: {c.hope['scars']})")
            else:
                print("No party loaded.")
            continue

        elif cmd == "fear":
            if campaign:
                print(f"  GM Fear: {campaign.fear}/12")
            else:
                print("No campaign loaded.")
            continue

        elif cmd == "help":
            print("Commands: save, status, roll <notation>, duality [modifier] [difficulty],")
            print("          party, hope, fear, help, quit")
            continue

        # Regular chat input
        messages.append({"role": "user", "content": user_input})

        try:
            response = agent.send(messages)
            messages.append({"role": "assistant", "content": response})
            print(f"\nGM> {response}\n")
        except Exception as e:
            print(f"\n[Error] {e}\n")
            messages.pop()  # Remove the failed user message
```

- [ ] **Step 2: Commit**

```bash
git add ui/terminal.py
git commit -m "feat: add terminal chat UI with dice commands and session management"
```

---

### Task 13: Entry Point

**Files:**
- Create: `daggerheart.py`

- [ ] **Step 1: Write implementation**

```python
#!/usr/bin/env python3
"""Daggerheart Campaign Tool -- AI Game Master and Campaign Manager.

A BXish-inspired tool for running Daggerheart RPG sessions with an AI GM.
"""

import argparse
import logging
import os
import sys
from pathlib import Path

from config import (
    VERSION,
    DEFAULT_PORT,
    DEFAULT_TEMPERATURE,
    PROVIDER_PRESETS,
    resolve_provider,
)
from engine.skill_loader import load_skills, build_system_prompt, estimate_tokens
from engine.session import load_session


def parse_args():
    parser = argparse.ArgumentParser(
        description="Daggerheart Campaign Tool -- AI Game Master and Campaign Manager"
    )
    parser.add_argument("--web", action="store_true", help="Launch Gradio web UI")
    parser.add_argument("--port", type=int, default=DEFAULT_PORT, help=f"Web UI port (default: {DEFAULT_PORT})")
    parser.add_argument("--provider", choices=list(PROVIDER_PRESETS.keys()), help="Provider preset")
    parser.add_argument("--model", help="Model name or identifier")
    parser.add_argument("--base-url", help="Custom API base URL (overrides provider)")
    parser.add_argument("--api-key", help="API key (or use env var)")
    parser.add_argument("--tier", choices=["core", "gm", "full"], default="full", help="Skill tier (default: full)")
    parser.add_argument("--skills-dir", type=Path, help="Path to skill files")
    parser.add_argument("--campaign", help="Campaign name to load or create")
    parser.add_argument("--session", type=Path, help="Resume from saved session JSON")
    parser.add_argument("--temperature", type=float, default=DEFAULT_TEMPERATURE)
    parser.add_argument("--dice-mode", choices=["app", "ai", "manual"], default="app")
    parser.add_argument("--list-models", action="store_true", help="Print model info and exit")
    parser.add_argument("--local", action="store_true", help="Use local LLM server (alias for --provider local)")
    parser.add_argument("--verbose", action="store_true", help="Enable debug logging")
    return parser.parse_args()


def main():
    args = parse_args()

    logging.basicConfig(
        level=logging.DEBUG if args.verbose else logging.INFO,
        format="%(levelname)s: %(message)s",
    )
    logger = logging.getLogger(__name__)

    if args.list_models:
        print("Provider Presets:")
        for name, preset in PROVIDER_PRESETS.items():
            model = preset.get("default_model") or "(auto/user-configured)"
            print(f"  {name:12s} {model}")
        sys.exit(0)

    # Resolve provider
    provider = "local" if args.local else args.provider
    if not provider and not args.base_url:
        print("Error: specify --provider, --base-url, or --local", file=sys.stderr)
        sys.exit(1)

    base_url, env_var = resolve_provider(provider, args.base_url)

    # Resolve API key
    api_key = args.api_key
    if not api_key and env_var:
        api_key = os.environ.get(env_var)
    if not api_key and not args.local and provider != "local":
        env_hint = f" (or set {env_var})" if env_var else ""
        print(f"Error: --api-key required{env_hint}", file=sys.stderr)
        sys.exit(1)

    # Resolve model
    model = args.model
    if not model and provider and PROVIDER_PRESETS.get(provider, {}).get("default_model"):
        model = PROVIDER_PRESETS[provider]["default_model"]

    # Set up OpenAI client
    from openai import OpenAI

    client_kwargs = {"base_url": base_url}
    if api_key:
        client_kwargs["api_key"] = api_key
    else:
        client_kwargs["api_key"] = "not-needed"

    client = OpenAI(**client_kwargs)

    # Auto-discover model for local
    if not model:
        if provider == "local" or args.local:
            try:
                models = client.models.list()
                model = models.data[0].id
                logger.info("Auto-discovered local model: %s", model)
            except Exception as e:
                print(f"Error: could not auto-discover local model: {e}", file=sys.stderr)
                sys.exit(1)
        else:
            print("Error: --model required (no default for this provider)", file=sys.stderr)
            sys.exit(1)

    # Load skills
    skills_dir = args.skills_dir or (Path(__file__).parent / "skills")
    skills_text = load_skills(skills_dir, args.tier)
    system_prompt = build_system_prompt(skills_text)
    prompt_tokens = estimate_tokens(system_prompt)
    logger.info("System prompt: ~%d tokens (%s tier)", prompt_tokens, args.tier)

    # Determine context limit (default 128K, reserve 75%)
    from config import CONTEXT_RESERVE_RATIO
    max_context = 128000
    conversation_budget = int(max_context * CONTEXT_RESERVE_RATIO)

    if prompt_tokens > max_context // 2:
        logger.warning(
            "System prompt (~%d tokens) exceeds 50%% of context window (%d). "
            "Consider using a lower tier or a model with a larger context window.",
            prompt_tokens, max_context,
        )

    # Build messages
    messages = [{"role": "system", "content": system_prompt}]

    # Load session if resuming
    if args.session:
        messages = load_session(args.session, new_system_prompt=system_prompt)
        logger.info("Resumed session from %s", args.session)

    # Campaign context injection
    campaign = None
    party = None
    if args.campaign:
        from campaign.state import load_campaign, create_campaign
        from campaign.party import load_party, build_campaign_context

        campaigns_base = Path(__file__).parent / "campaigns"
        try:
            campaign = load_campaign(args.campaign, campaigns_base)
        except FileNotFoundError:
            campaign = create_campaign(args.campaign, campaigns_base)
            logger.info("Created new campaign: %s", args.campaign)

        party = load_party(campaign.campaign_dir / "party")
        context_msg = build_campaign_context(
            characters=party,
            fear=campaign.fear,
            countdowns=campaign.countdowns,
            current_location=campaign.current_location,
        )
        # Insert context at position 1 (after system prompt)
        if len(messages) > 1 and messages[1].get("role") == "system":
            messages[1]["content"] = context_msg
        else:
            messages.insert(1, {"role": "system", "content": context_msg})

    # Create agent
    from engine.agent import DaggerheartAgent

    agent = DaggerheartAgent(
        client=client,
        model=model,
        system_prompt=system_prompt,
        max_context=conversation_budget,
        temperature=args.temperature,
    )

    # Launch
    if args.web:
        # Lazy import for web UI
        from ui.web import launch_web_ui
        campaign_dir = campaign.campaign_dir if args.campaign else None
        launch_web_ui(agent, messages, port=args.port, campaign_dir=campaign_dir)
    else:
        from ui.terminal import run_terminal
        from datetime import datetime as _dt

        session_path = None
        if args.campaign:
            session_path = campaign.campaign_dir / "sessions" / f"session-{_dt.now().strftime('%Y%m%d-%H%M%S')}.json"

        run_terminal(
            agent=agent,
            messages=messages,
            session_path=session_path,
            campaign_name=args.campaign or "",
            tier=args.tier,
            campaign=campaign if args.campaign else None,
            party=party if args.campaign else None,
        )


if __name__ == "__main__":
    main()
```

- [ ] **Step 2: Make it executable and test basic CLI**

Run: `chmod +x daggerheart.py && python3 daggerheart.py --list-models`

Expected output:
```
Provider Presets:
  abacus       (auto/user-configured)
  anthropic    claude-sonnet-4-20250514
  openai       gpt-4o
  local        (auto/user-configured)
```

- [ ] **Step 3: Test help output**

Run: `python3 daggerheart.py --help`
Expected: argparse help text with all flags

- [ ] **Step 4: Commit**

```bash
git add daggerheart.py
git commit -m "feat: add CLI entry point with provider resolution and terminal/web mode switching"
```

---

### Task 14: Run full test suite and verify end-to-end

- [ ] **Step 1: Run all tests**

Run: `python3 -m pytest tests/ -v`
Expected: All PASS

- [ ] **Step 2: Verify CLI works**

Run: `python3 daggerheart.py --list-models`
Expected: Model list prints correctly

---

## Chunk 4: Daggerheart Skill Files

This chunk writes the actual Daggerheart rules as markdown skill files. These are the heart of the system -- the rules that get loaded into the LLM's context to make it a faithful Daggerheart GM. Source all data from `daggerheart_mechanics_reference.md`.

### Task 15: Core Skills (01-07)

**Files:**
- Rewrite: `skills/SKILL.md` (expand from test stub to full GM procedures)
- Rewrite: `skills/01-core-mechanics.md` (expand from test stub to full core mechanics + Hope/Fear economy from reference sections 1 and 2)
- Create: `skills/02-character-creation.md`
- Create: `skills/03-classes.md`
- Create: `skills/04-domains.md`
- Create: `skills/05-combat.md`
- Create: `skills/06-damage-armor.md`
- Create: `skills/07-conditions-death.md`

- [ ] **Step 1: Rewrite SKILL.md**

Expand from the test stub to the full GM procedures document. Source the behavioral instructions from BXish's SKILL.md pattern, adapted for Daggerheart. Include: player agency rules (10 numbered rules), spotlight management procedures, Hope/Fear tracking procedures, NPC and social play guidelines, core GM principles. This file is the behavioral backbone -- it tells the AI *how* to GM, not *what* the rules are.

- [ ] **Step 2: Rewrite 01-core-mechanics.md**

Expand from the test stub to full core mechanics. Source from mechanics reference sections 1 (Core Mechanics) and 2 (Hope and Fear). Include: duality dice system with all 5 outcomes, advantage/disadvantage rules, difficulty guidelines by tier, complete Hope economy (gaining, spending, max, carry over), complete Fear economy (gaining, spending, max), all spending options for both currencies.

- [ ] **Step 3: Write 02-character-creation.md**

Source from `daggerheart_mechanics_reference.md` sections 3 (Character Creation) and 10 (Character Sheet Structure). Include: step-by-step process, six traits with spread, all 18 ancestries with features, all 9 communities with features, experiences system, starting stats.

- [ ] **Step 4: Write 03-classes.md**

Source from mechanics reference section 3 (Classes table) and SRD data added by the research agent. Include: all 9 classes with domains, subclasses, starting HP, starting Evasion, class features, Hope features, spellcast traits, suggested trait arrays.

- [ ] **Step 5: Write 04-domains.md**

Source from mechanics reference section 4 (Domains). Include: all 9 domains with descriptions, card types (ability/spell/grimoire), domain card mechanics (loadout of 5, vault, recall cost, swapping), spellcasting mechanics, level 1 card descriptions for all domains.

- [ ] **Step 6: Write 05-combat.md**

Source from mechanics reference section 5 (Combat). Include: spotlight system, action economy, attack rolls, damage rolls, critical damage, multi-target rules, group action rolls, tag team rolls (3 Hope cost), range/distance zones.

- [ ] **Step 7: Write 06-damage-armor.md**

Source from mechanics reference section 5 (Damage Thresholds, Armor Slots, Resistance/Immunity). Include: threshold mechanic (how damage maps to HP marked: 1/2/3/4), armor slot usage and restoration, stress system and Vulnerable condition, resistance/immunity rules. Do NOT include full equipment tables here -- those belong in 12-equipment-weapons.md and 13-equipment-armor.md (GM tier).

- [ ] **Step 8: Write 07-conditions-death.md**

Source from mechanics reference section 5 (Conditions, Death Mechanics). Include: Hidden/Restrained/Vulnerable conditions, three death move choices (Blaze of Glory, Avoid Death, Risk It All), scar mechanics.

- [ ] **Step 9: Commit**

```bash
git add skills/SKILL.md skills/01-core-mechanics.md skills/02-character-creation.md skills/03-classes.md skills/04-domains.md skills/05-combat.md skills/06-damage-armor.md skills/07-conditions-death.md
git commit -m "feat: add core skill files (GM procedures, mechanics, characters, classes, domains, combat, damage, conditions)"
```

---

### Task 16: GM Skills (08-13)

**Files:**
- Create: `skills/08-adversary-rules.md`
- Create: `skills/09-encounter-building.md`
- Create: `skills/10-campaign-structure.md`
- Create: `skills/11-rest-downtime.md`
- Create: `skills/12-equipment-weapons.md`
- Create: `skills/13-equipment-armor.md`

- [ ] **Step 1: Write 08-adversary-rules.md**

Source from mechanics reference section 6 (GM Tools/Adversary System). Include: stat block structure, 4 feature types, 10 adversary types with BP costs, adversary actions, tier scaling benchmarks table.

- [ ] **Step 2: Write 09-encounter-building.md**

Source from mechanics reference section 6 (Encounter Building). Include: Battle Points formula, adjustment table, tier-to-difficulty mapping, adversary actions on spotlight.

- [ ] **Step 3: Write 10-campaign-structure.md**

Source from mechanics reference section 7 (Campaign/Adventure Structure). Include: 10 levels across 4 tiers, PC tier vs adversary tier mapping, milestone leveling, level-up steps, advancement options, countdown mechanics (standard/dynamic/campaign).

- [ ] **Step 4: Write 11-rest-downtime.md**

Source from mechanics reference section 7 (Rest and Downtime). Include: short rest moves, long rest moves, Fear costs for resting, three-short-rest rule, project advancement.

- [ ] **Step 5: Write 12-equipment-weapons.md**

Source from mechanics reference weapon tables. Include: all primary weapon tables (tiers 1-4), all secondary weapon tables, weapon features reference, starting equipment rules.

- [ ] **Step 6: Write 13-equipment-armor.md**

Source from mechanics reference section 9 (Armor tables). Include: all armor tables for tiers 1-4 (already in reference), armor slot mechanics, armor features.

- [ ] **Step 7: Commit**

```bash
git add skills/08-adversary-rules.md skills/09-encounter-building.md skills/10-campaign-structure.md skills/11-rest-downtime.md skills/12-equipment-weapons.md skills/13-equipment-armor.md
git commit -m "feat: add GM skill files (adversaries, encounters, campaign, rest, equipment)"
```

---

### Task 17: Full Skills (14-15)

**Files:**
- Create: `skills/14-gm-moves.md`
- Create: `skills/15-gm-procedures.md`

- [ ] **Step 1: Write 14-gm-moves.md**

Source from mechanics reference section 6 (GM Moves). Include: when to make moves (Fear rolls, failures, golden opportunities), Fear spending categories (environmental, resource, social, party pressure, escalations, combat), player-facing roll handling.

- [ ] **Step 2: Write 15-gm-procedures.md**

Include comprehensive GM procedures adapted from BXish's SKILL.md approach but for Daggerheart: session prep checklist, session start sequence, combat procedure step-by-step, social encounter guidance, exploration/travel procedure, NPC management, pacing guidelines, Hope/Fear economy management.

- [ ] **Step 3: Commit**

```bash
git add skills/14-gm-moves.md skills/15-gm-procedures.md
git commit -m "feat: add full skill files (GM moves and procedures)"
```

---

### Task 18: Verify skill loading

- [ ] **Step 1: Test skill loading with all tiers**

Run: `python3 -c "
from pathlib import Path
from engine.skill_loader import load_skills, estimate_tokens
for tier in ['core', 'gm', 'full']:
    text = load_skills(Path('skills'), tier)
    tokens = estimate_tokens(text)
    print(f'{tier}: ~{tokens} tokens, {len(text)} chars')
"`

Expected: Token counts roughly matching spec estimates (core ~15K, gm ~25K, full ~35K). Exact numbers will vary based on final file lengths.

- [ ] **Step 2: Run full test suite**

Run: `python3 -m pytest tests/ -v`
Expected: All PASS

---

## Chunk 5: Web UI

This chunk builds the Gradio web interface with all 5 tabs. After this chunk, the full application is usable via `python3 daggerheart.py --web`.

### Task 19: Web UI - Adventure Tab

**Files:**
- Create: `ui/web.py`

- [ ] **Step 1: Write the Adventure tab and core web UI structure**

```python
# ui/web.py
"""Gradio web UI for Daggerheart Campaign Tool."""

import json
from datetime import datetime
from pathlib import Path

from config import VERSION
from engine.agent import DaggerheartAgent, estimate_message_tokens
from engine.dice import roll, roll_duality
from engine.session import save_session

CSS = """
.gradio-container { background: #0d0d1a !important; min-height: 100vh; }
.chatbot .message.bot { background: #1a1a2e !important; color: #e0d6c2 !important; }
.chatbot .message.user { background: #b8d4e8 !important; color: #111 !important; }
table { border-collapse: collapse; width: 100%; }
th { background: #2a2a3e; padding: 8px; }
td { border: 1px solid #444; padding: 8px; }
pre, code { background: #111 !important; }
.status-bar { font-size: 12px; color: #888; text-align: right; }
footer { display: none !important; max-height: 0 !important; }
"""

GREETING = """Welcome to the world of **Daggerheart**!

Choose how to begin:
1. **Start a new campaign** -- Create characters and begin your adventure
2. **Continue an existing campaign** -- Pick up where you left off
3. **Run a one-shot adventure** -- A standalone session
4. **Create a character** -- Build a new character with guided creation or quick-gen

What would you like to do?"""


def launch_web_ui(
    agent: DaggerheartAgent,
    messages: list[dict],
    port: int = 7860,
    campaign_dir: Path | None = None,
):
    """Launch the Gradio web interface.

    Args:
        agent: Configured DaggerheartAgent.
        messages: Initial message list (with system prompt).
        port: Port to serve on.
        campaign_dir: Path to active campaign directory (or None).
    """
    import gradio as gr

    # Mutable state (closure-captured, single-user)
    conversation = list(messages)
    if campaign_dir:
        session_file = campaign_dir / "sessions" / f"session-{datetime.now().strftime('%Y%m%d-%H%M%S')}.json"
    else:
        session_file = Path("sessions") / f"session-{datetime.now().strftime('%Y%m%d-%H%M%S')}.json"
    dice_mode = ["app"]  # mutable list for closure capture

    def respond(user_msg, chat_history):
        if not user_msg.strip():
            return chat_history, "", _status_text()

        conversation.append({"role": "user", "content": user_msg})

        try:
            response = agent.send(conversation)
        except Exception as e:
            response = f"[Error: {e}]"

        conversation.append({"role": "assistant", "content": response})
        chat_history = chat_history or []
        chat_history.append({"role": "user", "content": user_msg})
        chat_history.append({"role": "assistant", "content": response})
        return chat_history, "", _status_text()

    def do_save():
        save_session(conversation, session_file)
        return f"Session saved to {session_file}"

    def do_new():
        nonlocal conversation
        conversation = [conversation[0]]  # Keep system prompt
        return [], _status_text(), "New session started"

    def do_roll(notation):
        if not notation.strip():
            return "Enter dice notation (e.g., 2d12, 1d8+3)"
        try:
            result = roll(notation.strip())
            return f"Rolled {result.notation}: {result.dice} = {result.total}"
        except ValueError as e:
            return str(e)

    def do_duality():
        result = roll_duality(modifier=0, difficulty=11)
        outcome_labels = {
            "success_hope": "Success with Hope",
            "success_fear": "Success with Fear",
            "failure_hope": "Failure with Hope",
            "failure_fear": "Failure with Fear",
            "critical": "CRITICAL SUCCESS!",
        }
        label = outcome_labels.get(result.outcome_type, result.outcome_type)
        return (
            f"Hope [{result.hope_die}] Fear [{result.fear_die}] | "
            f"Total: {result.modified_total} vs {result.difficulty} | "
            f"{label}"
        )

    def do_load_context(files, chat_history):
        if not files:
            return chat_history, "No files selected"
        contents = []
        for f in files:
            text = Path(f.name).read_text(encoding="utf-8", errors="replace")
            contents.append(text)
        combined = "\n\n---\n\n".join(contents)
        context_msg = (
            "Here are transcripts from previous adventure sessions. "
            "Use these as background context for the current campaign. "
            "Do not repeat this content in chat.\n\n" + combined
        )
        conversation.append({"role": "user", "content": context_msg})
        try:
            response = agent.send(conversation)
        except Exception as e:
            response = f"[Error loading context: {e}]"
        conversation.append({"role": "assistant", "content": response})
        chat_history = chat_history or []
        chat_history.append({"role": "assistant", "content": response})
        return chat_history, f"Loaded {len(files)} context file(s)"

    def _status_text():
        tokens = estimate_message_tokens(conversation)
        msg_count = len([m for m in conversation if m["role"] not in ("system",)])
        parts = [f"Model: {agent.model}", f"Tokens: ~{tokens}", f"Messages: {msg_count}"]
        # Add Hope/Fear if campaign is loaded
        if campaign_dir:
            try:
                from campaign.state import load_campaign
                camp = load_campaign(campaign_dir.name, campaign_dir.parent)
                parts.append(f"Fear: {camp.fear}/12")
            except Exception:
                pass
            try:
                from campaign.party import load_party
                party = load_party(campaign_dir / "party")
                hope_total = sum(c.hope["current"] for c in party)
                parts.append(f"Party Hope: {hope_total}")
            except Exception:
                pass
        return " | ".join(parts)

    def _on_dice_mode_change(mode):
        dice_mode[0] = mode.lower().replace(" ", "_")

    # Build UI
    theme = gr.themes.Base(
        primary_hue="amber",
        secondary_hue="stone",
        neutral_hue="stone",
    )

    with gr.Blocks(css=CSS, theme=theme, title="Daggerheart Campaign Tool") as app:
        gr.Markdown(f"# Daggerheart Campaign Tool v{VERSION}")

        with gr.Tabs():
            # Tab 1: Adventure
            with gr.Tab("Adventure"):
                chatbot = gr.Chatbot(
                    value=[{"role": "assistant", "content": GREETING}],
                    height=500,
                    type="messages",
                )
                with gr.Row():
                    msg_input = gr.Textbox(
                        placeholder="What do you do?",
                        scale=9,
                        show_label=False,
                        autofocus=True,
                    )
                    send_btn = gr.Button("Send", variant="primary", scale=1)
                with gr.Row():
                    dice_mode_radio = gr.Radio(
                        choices=["App Roll", "AI Narrates", "Manual"],
                        value="App Roll", label="Dice Mode", scale=3,
                    )
                    roll_input = gr.Textbox(placeholder="e.g. 2d12+3", scale=3, show_label=False)
                    roll_btn = gr.Button("Roll", scale=1)
                    duality_btn = gr.Button("Duality Roll", scale=1)
                    roll_output = gr.Textbox(interactive=False, scale=4, show_label=False)
                with gr.Row():
                    save_btn = gr.Button("Save Session", size="sm", scale=1)
                    new_btn = gr.Button("New Session", size="sm", scale=1)
                    context_upload = gr.File(
                        label="Load Context",
                        file_count="multiple",
                        file_types=[".md", ".txt", ".json"],
                        scale=4,
                    )
                    info_box = gr.Textbox(interactive=False, show_label=False, scale=4)
                status_bar = gr.Markdown(_status_text(), elem_classes=["status-bar"])

                # Event handlers
                send_btn.click(respond, [msg_input, chatbot], [chatbot, msg_input, status_bar])
                msg_input.submit(respond, [msg_input, chatbot], [chatbot, msg_input, status_bar])
                save_btn.click(do_save, [], [info_box])
                new_btn.click(do_new, [], [chatbot, status_bar, info_box])
                roll_btn.click(do_roll, [roll_input], [roll_output])
                duality_btn.click(do_duality, [], [roll_output])
                context_upload.change(do_load_context, [context_upload, chatbot], [chatbot, info_box])
                dice_mode_radio.change(_on_dice_mode_change, [dice_mode_radio], [])

            # Tab 2: Party (placeholder)
            with gr.Tab("Party"):
                gr.Markdown("## Party Management\n*Coming soon -- manage your party members here.*")

            # Tab 3: Campaign World (placeholder)
            with gr.Tab("Campaign World"):
                gr.Markdown("## Campaign World\n*Coming soon -- locations, factions, NPCs, countdowns.*")

            # Tab 4: Encounter Workshop (placeholder)
            with gr.Tab("Encounter Workshop"):
                gr.Markdown("## Encounter Workshop\n*Coming soon -- build balanced encounters.*")

            # Tab 5: Journal (placeholder)
            with gr.Tab("Journal"):
                gr.Markdown("## Session Journal\n*Coming soon -- session notes and summaries.*")

        # Initialize greeting in conversation
        if not any(m.get("role") == "assistant" for m in conversation):
            conversation.append({"role": "assistant", "content": GREETING})

    app.launch(server_name="0.0.0.0", server_port=port, share=False, inbrowser=True)
```

- [ ] **Step 2: Commit**

```bash
git add ui/web.py
git commit -m "feat: add Gradio web UI with Adventure tab and placeholder tabs"
```

---

### Task 20: Web UI - Party Tab

**Files:**
- Modify: `ui/web.py`

- [ ] **Step 1: Replace the Party tab placeholder**

In `ui/web.py`, replace the Party tab placeholder block with a full implementation that:
- Shows party members as an HTML table with HP/Stress/Hope/Armor bars
- Has Create Character button (opens a textbox for quick-gen prompt, sends to LLM, displays result)
- Has Import Character button (JSON file upload, validates and saves)
- Has +/- buttons for HP, Stress, Hope, and Armor Slots on each character
- Shows party-level info (tier, Fear counter)
- Reads/writes to the campaign's `party/` directory

Implementation details: Use `gr.HTML` for the party card display, regenerated on any state change. Character creation uses the agent to generate a character sheet JSON from a concept prompt. Import validates with `validate_character()`.

- [ ] **Step 2: Commit**

```bash
git add ui/web.py
git commit -m "feat: add Party tab with character display, creation, and import"
```

---

### Task 21: Web UI - Campaign World Tab

**Files:**
- Modify: `ui/web.py`
- Create: `campaign/world.py`
- Create: `campaign/npc.py`

- [ ] **Step 1: Write world.py**

Simple CRUD for markdown files in `campaigns/{name}/world/`:
- `save_entity(name, content, entity_type, world_dir)` -- saves as `{entity_type}_{safe_name}.md`
- `load_entity(name, entity_type, world_dir)` -- loads markdown content
- `list_entities(entity_type, world_dir)` -- lists all entities of a type
- `delete_entity(name, entity_type, world_dir)`

Entity types: "location", "faction", "lore"

- [ ] **Step 2: Write npc.py**

Simple CRUD for markdown files in `campaigns/{name}/npcs/`:
- `save_npc(name, content, npcs_dir)`
- `load_npc(name, npcs_dir)`
- `list_npcs(npcs_dir)`

- [ ] **Step 3: Replace Campaign World tab placeholder**

Sub-tabs for Locations, Factions, NPCs, Countdowns, Lore. Each has:
- Dropdown to select existing entity
- Markdown display of selected entity
- "Generate" button (uses agent to create new entity)
- Text area for manual edit/create
- Save/Delete buttons

- [ ] **Step 4: Commit**

```bash
git add campaign/world.py campaign/npc.py ui/web.py
git commit -m "feat: add Campaign World tab with locations, factions, NPCs, countdowns, lore"
```

---

### Task 22: Web UI - Encounter Workshop Tab

**Files:**
- Modify: `ui/web.py`
- Create: `campaign/encounter.py`
- Create: `campaign/adversary.py`

- [ ] **Step 1: Write encounter.py**

- `calculate_battle_points(party_size)` -> base BP budget
- `get_adversary_bp_cost(adversary_type)` -> BP cost from the type table
- `validate_encounter(adversaries, party_size)` -> over/under budget info
- `save_encounter(encounter_data, encounters_dir)`
- `load_encounter(name, encounters_dir)`
- `list_encounters(encounters_dir)`

- [ ] **Step 2: Write adversary.py**

- `save_adversary(data, adversaries_dir)`
- `load_adversary(name, adversaries_dir)`
- `list_adversaries(adversaries_dir)`
- Adversary data schema: name, tier, type, difficulty, thresholds, HP, stress, attack_modifier, standard_attack, features

- [ ] **Step 3: Replace Encounter Workshop tab placeholder**

- Party size number input (auto-filled)
- Tier dropdown
- BP budget display (auto-calculated)
- "Generate Encounter" button (AI-powered)
- Manual adversary add (from library dropdown or custom)
- Running BP total
- Output area showing stat blocks
- Save/Load encounter buttons

- [ ] **Step 4: Commit**

```bash
git add campaign/encounter.py campaign/adversary.py ui/web.py
git commit -m "feat: add Encounter Workshop tab with BP calculator and adversary management"
```

---

### Task 23: Web UI - Journal Tab

**Files:**
- Modify: `ui/web.py`
- Create: `campaign/journal.py`

- [ ] **Step 1: Write journal.py**

- `save_journal_entry(content, session_number, journal_dir)`
- `load_journal_entry(session_number, journal_dir)`
- `list_journal_entries(journal_dir)` -> list of session numbers
- `get_next_session_number(journal_dir)` -> auto-increment

- [ ] **Step 2: Replace Journal tab placeholder**

- Session selector dropdown
- Markdown display of selected session notes
- "Auto-Summarize" button (reads current chat session, uses agent to generate structured notes)
- New Entry / Edit buttons
- Text area for manual entry

- [ ] **Step 3: Commit**

```bash
git add campaign/journal.py ui/web.py
git commit -m "feat: add Journal tab with session notes and auto-summarize"
```

---

### Task 24: Web UI - Random Generators

**Files:**
- Create: `campaign/generators.py`
- Modify: `ui/web.py` (add generator buttons/features across tabs)

- [ ] **Step 1: Write generators.py**

All functions take the agent and return generated content:
- `generate_location(agent, messages, context)` -> location markdown
- `generate_shop_inventory(agent, messages, tier, context)` -> shop/tavern inventory with prices
- `generate_encounter(agent, messages, party_size, tier, context)` -> encounter data
- `generate_quest_hook(agent, messages, context)` -> quest hook text
- `generate_name(agent, messages, ancestry)` -> name string
- `generate_treasure(agent, messages, tier)` -> treasure description

Each builds a prompt incorporating campaign context and Daggerheart rules, sends to agent, parses response.

- [ ] **Step 2: Wire generators into UI tabs**

- Campaign World: "Generate" buttons call the appropriate generator
- Encounter Workshop: "Generate Encounter" calls `generate_encounter`
- Add a small "Quick Generate" section to the Adventure tab's sidebar for names, treasure

- [ ] **Step 3: Commit**

```bash
git add campaign/generators.py ui/web.py
git commit -m "feat: add LLM-powered generators for NPCs, locations, encounters, treasure"
```

---

### Task 24.5: Tests for Campaign Modules

**Files:**
- Create: `tests/campaign/test_world.py`
- Create: `tests/campaign/test_npc.py`
- Create: `tests/campaign/test_encounter.py`
- Create: `tests/campaign/test_adversary.py`
- Create: `tests/campaign/test_journal.py`

- [ ] **Step 1: Write tests for world.py**

Test `save_entity`, `load_entity`, `list_entities`, `delete_entity` with temp directories. Verify markdown files are created/read/listed/deleted correctly for each entity type (location, faction, lore).

- [ ] **Step 2: Write tests for npc.py**

Test `save_npc`, `load_npc`, `list_npcs` with temp directories.

- [ ] **Step 3: Write tests for encounter.py**

Test `calculate_battle_points` (e.g., 4 PCs -> 14 BP), `get_adversary_bp_cost` for each adversary type, `validate_encounter` for over/under budget scenarios. Test `save_encounter`/`load_encounter`/`list_encounters` with temp directories.

- [ ] **Step 4: Write tests for adversary.py**

Test `save_adversary`, `load_adversary`, `list_adversaries` with temp directories. Verify JSON stat block schema is preserved.

- [ ] **Step 5: Write tests for journal.py**

Test `save_journal_entry`, `load_journal_entry`, `list_journal_entries`, `get_next_session_number` with temp directories. Verify session numbering auto-increments.

- [ ] **Step 6: Run all campaign tests**

Run: `python3 -m pytest tests/campaign/ -v`
Expected: All PASS

- [ ] **Step 7: Commit**

```bash
git add tests/campaign/
git commit -m "test: add tests for campaign modules (world, npc, encounter, adversary, journal)"
```

---

### Task 25: Final integration test and cleanup

- [ ] **Step 1: Run full test suite**

Run: `python3 -m pytest tests/ -v`
Expected: All PASS

- [ ] **Step 2: Test CLI help**

Run: `python3 daggerheart.py --help`
Expected: Full help output with all flags

- [ ] **Step 3: Test list models**

Run: `python3 daggerheart.py --list-models`
Expected: Provider presets listed

- [ ] **Step 4: Verify skill loading**

Run: `python3 -c "
from pathlib import Path
from engine.skill_loader import load_skills, estimate_tokens
for tier in ['core', 'gm', 'full']:
    text = load_skills(Path('skills'), tier)
    tokens = estimate_tokens(text)
    print(f'{tier}: ~{tokens} tokens')
"`
Expected: Token counts for all tiers

- [ ] **Step 5: Final commit**

```bash
git add -A
git commit -m "chore: final cleanup and integration verification"
```
