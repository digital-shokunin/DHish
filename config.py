"""Configuration constants and provider presets for Daggerheart Campaign Tool."""

VERSION = "1.0.0"
CHARS_PER_TOKEN = 4
DEFAULT_TEMPERATURE = 0.7
DEFAULT_MAX_TOKENS = 16384
DEFAULT_PORT = 7860
CONTEXT_RESERVE_RATIO = 0.75

PROVIDER_PRESETS = {
    "abacus": {
        "base_url": "https://api.abacus.ai/v1",
        "default_model": "route-llm",
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
        "default_model": None,
        "env_var": None,
    },
}

_CORE_FILES = [
    "SKILL.md", "01-core-mechanics.md", "02-character-creation.md",
    "03-classes.md", "04-domains.md", "05-combat.md",
    "06-damage-armor.md", "07-conditions-death.md",
]
_GM_FILES = _CORE_FILES + [
    "08-adversary-rules.md", "09-encounter-building.md",
    "10-campaign-structure.md", "11-rest-downtime.md",
    "12-equipment-weapons.md", "13-equipment-armor.md",
]
_FULL_FILES = _GM_FILES + ["14-gm-moves.md", "15-gm-procedures.md"]

SKILL_TIERS = {"core": _CORE_FILES, "gm": _GM_FILES, "full": _FULL_FILES}

SYSTEM_PROMPT_PREAMBLE = """You are a Daggerheart RPG Game Master. You run tabletop RPG sessions \
using official Daggerheart rules. You are a collaborative storyteller \
who tracks Hope and Fear rigorously, manages the spotlight fairly, \
and lets the players' decisions drive the narrative.

Follow the procedures, rules, and principles in the skill reference \
below. These are your complete rules and GM instructions.

=== DAGGERHEART GAME MASTER SKILL ===

"""


def resolve_provider(provider, base_url_override=None):
    if provider and provider in PROVIDER_PRESETS:
        preset = PROVIDER_PRESETS[provider]
        base_url = base_url_override or preset["base_url"]
        return base_url, preset["env_var"]
    return base_url_override, None
