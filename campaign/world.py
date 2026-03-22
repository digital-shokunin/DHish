"""World entity management (locations, factions, lore) for Daggerheart."""
import re
import logging
from pathlib import Path

logger = logging.getLogger(__name__)

def _safe_filename(name: str, entity_type: str) -> str:
    safe = re.sub(r"[^\w\s-]", "", name).strip().replace(" ", "_").lower()
    return f"{entity_type}_{safe}.md"

def save_entity(name: str, content: str, entity_type: str, world_dir: Path) -> Path:
    world_dir.mkdir(parents=True, exist_ok=True)
    path = world_dir / _safe_filename(name, entity_type)
    path.write_text(f"# {name}\n\n{content}", encoding="utf-8")
    return path

def load_entity(name: str, entity_type: str, world_dir: Path) -> str:
    path = world_dir / _safe_filename(name, entity_type)
    return path.read_text(encoding="utf-8")

def list_entities(entity_type: str, world_dir: Path) -> list[str]:
    if not world_dir.exists():
        return []
    prefix = f"{entity_type}_"
    names = []
    for p in sorted(world_dir.glob(f"{prefix}*.md")):
        text = p.read_text(encoding="utf-8")
        first_line = text.split("\n")[0]
        name = first_line.lstrip("# ").strip() if first_line.startswith("#") else p.stem.replace(prefix, "").replace("_", " ")
        names.append(name)
    return names

def delete_entity(name: str, entity_type: str, world_dir: Path) -> bool:
    path = world_dir / _safe_filename(name, entity_type)
    if path.exists():
        path.unlink()
        return True
    return False
