"""NPC management for Daggerheart."""
import re
from pathlib import Path

def _safe_filename(name: str) -> str:
    return re.sub(r"[^\w\s-]", "", name).strip().replace(" ", "_").lower() + ".md"

def save_npc(name: str, content: str, npcs_dir: Path) -> Path:
    npcs_dir.mkdir(parents=True, exist_ok=True)
    path = npcs_dir / _safe_filename(name)
    path.write_text(f"# {name}\n\n{content}", encoding="utf-8")
    return path

def load_npc(name: str, npcs_dir: Path) -> str:
    return (npcs_dir / _safe_filename(name)).read_text(encoding="utf-8")

def list_npcs(npcs_dir: Path) -> list[str]:
    if not npcs_dir.exists():
        return []
    names = []
    for p in sorted(npcs_dir.glob("*.md")):
        text = p.read_text(encoding="utf-8")
        first_line = text.split("\n")[0]
        names.append(first_line.lstrip("# ").strip() if first_line.startswith("#") else p.stem.replace("_", " "))
    return names
