"""LLM chat agent for Daggerheart Campaign Tool."""
import logging
import time
from config import CHARS_PER_TOKEN, DEFAULT_MAX_TOKENS, DEFAULT_TEMPERATURE

logger = logging.getLogger(__name__)
MAX_RETRIES = 5

def estimate_message_tokens(messages: list[dict]) -> int:
    total = 0
    for msg in messages:
        content = msg.get("content", "")
        total += len(content) // CHARS_PER_TOKEN + 10
    return total

def prune_messages(messages: list[dict], max_tokens: int) -> list[dict]:
    if estimate_message_tokens(messages) <= max_tokens:
        return messages
    system_msgs = [m for m in messages if m["role"] == "system"]
    non_system = [m for m in messages if m["role"] != "system"]
    while non_system and estimate_message_tokens(system_msgs + non_system) > max_tokens:
        non_system.pop(0)
    return system_msgs + non_system

class DaggerheartAgent:
    def __init__(self, client, model, system_prompt, max_context, temperature=DEFAULT_TEMPERATURE):
        self.client = client
        self.model = model
        self.system_prompt = system_prompt
        self.max_context = max_context
        self.temperature = temperature
        self.total_tokens_used = 0

    def send(self, messages: list[dict]) -> str:
        messages = prune_messages(messages, self.max_context)
        for attempt in range(MAX_RETRIES):
            try:
                response = self.client.chat.completions.create(
                    model=self.model, messages=messages,
                    temperature=self.temperature, max_tokens=DEFAULT_MAX_TOKENS,
                )
                choice = response.choices[0]
                if choice.finish_reason == "length":
                    logger.warning("Response truncated (finish_reason=length)")
                if response.usage:
                    self.total_tokens_used += response.usage.total_tokens
                return choice.message.content or ""
            except Exception as e:
                error_str = str(e).lower()
                if "429" in error_str or "rate" in error_str:
                    wait = 2**attempt + 1
                    logger.warning("Rate limited, retrying in %ds (%d/%d)", wait, attempt+1, MAX_RETRIES)
                    time.sleep(wait)
                else:
                    raise
        raise RuntimeError(f"Failed after {MAX_RETRIES} retries due to rate limiting")
