"""Session persistence for Daggerheart Campaign Tool."""
import json
import logging
from pathlib import Path
from typing import Optional

logger = logging.getLogger(__name__)


def save_session(messages: list[dict], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(messages, f, indent=2, ensure_ascii=False)
    logger.info("Session saved to %s (%d messages)", path, len(messages))


def load_session(path: Path, new_system_prompt: Optional[str] = None) -> list[dict]:
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)

    if not isinstance(data, list):
        raise ValueError(f"Session file must contain a JSON array, got {type(data).__name__}")

    messages = []
    for i, item in enumerate(data):
        if not isinstance(item, dict) or "role" not in item or "content" not in item:
            logger.warning("Skipping malformed message at index %d in %s", i, path)
            continue
        messages.append(item)

    if new_system_prompt and messages and messages[0]["role"] == "system":
        messages[0]["content"] = new_system_prompt
        logger.info("Replaced system prompt in loaded session")

    logger.info("Loaded session from %s (%d messages)", path, len(messages))
    return messages
