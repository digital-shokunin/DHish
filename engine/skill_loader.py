"""Load and compile Daggerheart skill files into a system prompt."""
import logging
from pathlib import Path
from config import SKILL_TIERS, SYSTEM_PROMPT_PREAMBLE, CHARS_PER_TOKEN

logger = logging.getLogger(__name__)

def estimate_tokens(text: str) -> int:
    if not text:
        return 0
    return len(text) // CHARS_PER_TOKEN

def load_skills(skills_dir: Path, tier: str) -> str:
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
    return SYSTEM_PROMPT_PREAMBLE + skills_text
