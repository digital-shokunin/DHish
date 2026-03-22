"""Character sheet management for Daggerheart Campaign Tool."""
import json
import logging
import re
from pathlib import Path

logger = logging.getLogger(__name__)

VALID_CLASSES = ["Bard", "Druid", "Guardian", "Ranger", "Rogue", "Seraph", "Sorcerer", "Warrior", "Wizard"]
VALID_TRAITS = ["agility", "strength", "finesse", "instinct", "presence", "knowledge"]
TRAIT_SPREAD_SUM = 3
TRAIT_SPREAD_SORTED = [-1, 0, 0, 1, 1, 2]
REQUIRED_FIELDS = [
    "name", "class", "subclass", "level", "tier", "ancestry", "community",
    "traits", "evasion", "proficiency", "hp", "stress", "hope", "armor",
    "weapons", "domains", "domain_cards", "experiences",
]

class Character:
    def __init__(self, data: dict):
        self.name = data["name"]
        self.char_class = data["class"]
        self.subclass = data["subclass"]
        self.level = data["level"]
        self.tier = data["tier"]
        self.ancestry = data["ancestry"]
        self.community = data["community"]
        self.traits = data["traits"]
        self.evasion = data["evasion"]
        self.proficiency = data["proficiency"]
        self.hp = data["hp"]
        self.stress = data["stress"]
        self.hope = data["hope"]
        self.armor = data["armor"]
        self.weapons = data["weapons"]
        self.domains = data["domains"]
        self.domain_cards = data["domain_cards"]
        self.subclass_card = data.get("subclass_card", "foundation")
        self.ancestry_features = data.get("ancestry_features", [])
        self.community_feature = data.get("community_feature", "")
        self.experiences = data.get("experiences", [])
        self.connections = data.get("connections", [])

    @classmethod
    def from_dict(cls, data: dict) -> "Character":
        return cls(data)

    def to_dict(self) -> dict:
        return {
            "name": self.name, "class": self.char_class, "subclass": self.subclass,
            "level": self.level, "tier": self.tier, "ancestry": self.ancestry,
            "community": self.community, "traits": self.traits, "evasion": self.evasion,
            "proficiency": self.proficiency, "hp": self.hp, "stress": self.stress,
            "hope": self.hope, "armor": self.armor, "weapons": self.weapons,
            "domains": self.domains, "domain_cards": self.domain_cards,
            "subclass_card": self.subclass_card, "ancestry_features": self.ancestry_features,
            "community_feature": self.community_feature, "experiences": self.experiences,
            "connections": self.connections,
        }

def _safe_filename(name: str) -> str:
    return re.sub(r"[^\w\s-]", "", name).strip().replace(" ", "_").lower() + ".json"

def save_character(character: Character, party_dir: Path) -> Path:
    party_dir.mkdir(parents=True, exist_ok=True)
    path = party_dir / _safe_filename(character.name)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(character.to_dict(), f, indent=2, ensure_ascii=False)
    return path

def load_character(name: str, party_dir: Path) -> Character:
    path = party_dir / _safe_filename(name)
    with open(path, "r", encoding="utf-8") as f:
        return Character.from_dict(json.load(f))

def list_characters(party_dir: Path) -> list[str]:
    if not party_dir.exists():
        return []
    names = []
    for path in sorted(party_dir.glob("*.json")):
        with open(path) as f:
            names.append(json.load(f)["name"])
    return names

def get_effective_thresholds(character: Character) -> tuple[int, int]:
    base_major = character.armor.get("base_major", 0)
    base_severe = character.armor.get("base_severe", 0)
    return base_major + character.level, base_severe + character.level

def validate_character(data: dict) -> list[str]:
    errors = []
    for field in REQUIRED_FIELDS:
        if field not in data:
            errors.append(f"Missing required field: '{field}'")
    if "traits" in data:
        traits = data["traits"]
        level = data.get("level", 1)
        if level == 1 and sorted(traits.values()) != TRAIT_SPREAD_SORTED:
            errors.append(f"Level 1 trait spread must be +2/+1/+1/+0/+0/-1, got sorted values: {sorted(traits.values())}")
        elif level > 1 and sum(traits.values()) < TRAIT_SPREAD_SUM:
            errors.append(f"Trait values sum ({sum(traits.values())}) is less than minimum ({TRAIT_SPREAD_SUM})")
    if "class" in data and data["class"] not in VALID_CLASSES:
        errors.append(f"Invalid class: '{data['class']}'")
    return errors
