"""Session journal management for Daggerheart."""
from pathlib import Path

def _session_filename(session_number: int) -> str:
    return f"session-{session_number:03d}.md"

def save_journal_entry(content: str, session_number: int, journal_dir: Path) -> Path:
    journal_dir.mkdir(parents=True, exist_ok=True)
    path = journal_dir / _session_filename(session_number)
    path.write_text(content, encoding="utf-8")
    return path

def load_journal_entry(session_number: int, journal_dir: Path) -> str:
    return (journal_dir / _session_filename(session_number)).read_text(encoding="utf-8")

def list_journal_entries(journal_dir: Path) -> list[int]:
    if not journal_dir.exists():
        return []
    entries = []
    for p in sorted(journal_dir.glob("session-*.md")):
        try:
            num = int(p.stem.split("-")[1])
            entries.append(num)
        except (IndexError, ValueError):
            pass
    return entries

def get_next_session_number(journal_dir: Path) -> int:
    entries = list_journal_entries(journal_dir)
    return max(entries) + 1 if entries else 1
