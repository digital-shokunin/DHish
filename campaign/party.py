"""Party tracker for Daggerheart Campaign Tool."""
import json
from pathlib import Path
from campaign.character import Character, get_effective_thresholds

def load_party(party_dir: Path) -> list[Character]:
    if not party_dir.exists():
        return []
    characters = []
    for path in sorted(party_dir.glob("*.json")):
        with open(path) as f:
            characters.append(Character.from_dict(json.load(f)))
    return characters

def get_party_summary(characters: list[Character]) -> str:
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

def build_campaign_context(characters, fear=0, countdowns=None, current_location="", journal_summary=""):
    parts = ["=== CURRENT CAMPAIGN STATE ==="]
    parts.append(f"\n## Party\nParty size: {len(characters)}")
    if characters:
        parts.append(get_party_summary(characters))
    parts.append(f"\n## GM Resources\nFear: {fear}/12")
    if countdowns:
        parts.append("\n## Active Countdowns")
        for cd in countdowns:
            parts.append(f"- {cd['name']}: {cd['current']}/{cd['max']} ({cd.get('type', 'standard')})")
    if current_location:
        parts.append(f"\n## Current Location\n{current_location}")
    if journal_summary:
        parts.append(f"\n## Recent Events\n{journal_summary}")
    return "\n".join(parts)
