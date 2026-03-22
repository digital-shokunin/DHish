"""Encounter builder for Daggerheart."""
import json
import logging
from pathlib import Path

logger = logging.getLogger(__name__)

ADVERSARY_BP_COSTS = {
    "minion": 1, "social": 1, "support": 1,
    "horde": 2, "ranged": 2, "skulk": 2, "standard": 2,
    "leader": 3, "bruiser": 4, "solo": 5,
}

def calculate_battle_points(party_size: int) -> int:
    return (3 * party_size) + 2

def get_adversary_bp_cost(adversary_type: str) -> int:
    return ADVERSARY_BP_COSTS.get(adversary_type.lower(), 2)

def validate_encounter(adversaries: list[dict], party_size: int) -> dict:
    budget = calculate_battle_points(party_size)
    total_cost = sum(get_adversary_bp_cost(a.get("type", "standard")) for a in adversaries)
    return {"budget": budget, "total_cost": total_cost, "remaining": budget - total_cost,
            "over_budget": total_cost > budget}

def save_encounter(encounter_data: dict, encounters_dir: Path) -> Path:
    encounters_dir.mkdir(parents=True, exist_ok=True)
    name = encounter_data.get("name", "unnamed")
    safe = name.lower().replace(" ", "_")
    path = encounters_dir / f"encounter_{safe}.json"
    with open(path, "w", encoding="utf-8") as f:
        json.dump(encounter_data, f, indent=2, ensure_ascii=False)
    return path

def load_encounter(name: str, encounters_dir: Path) -> dict:
    safe = name.lower().replace(" ", "_")
    path = encounters_dir / f"encounter_{safe}.json"
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def list_encounters(encounters_dir: Path) -> list[str]:
    if not encounters_dir.exists():
        return []
    names = []
    for p in sorted(encounters_dir.glob("encounter_*.json")):
        with open(p) as f:
            data = json.load(f)
        names.append(data.get("name", p.stem))
    return names
