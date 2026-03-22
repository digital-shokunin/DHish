"""Adversary stat block management for Daggerheart."""
import json
from pathlib import Path

def save_adversary(data: dict, adversaries_dir: Path) -> Path:
    adversaries_dir.mkdir(parents=True, exist_ok=True)
    name = data.get("name", "unnamed")
    safe = name.lower().replace(" ", "_")
    path = adversaries_dir / f"{safe}.json"
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    return path

def load_adversary(name: str, adversaries_dir: Path) -> dict:
    safe = name.lower().replace(" ", "_")
    path = adversaries_dir / f"{safe}.json"
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def list_adversaries(adversaries_dir: Path) -> list[str]:
    if not adversaries_dir.exists():
        return []
    names = []
    for p in sorted(adversaries_dir.glob("*.json")):
        with open(p) as f:
            data = json.load(f)
        names.append(data.get("name", p.stem))
    return names
