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
    """Prune messages to fit within token budget.

    Preserves message order. Drops oldest non-system messages first.
    System messages at positions 0 and 1 (system prompt + campaign context)
    are always preserved. Later system messages (e.g., dice roll injections)
    are prunable like any other message.
    """
    if estimate_message_tokens(messages) <= max_tokens:
        return messages

    # Preserve the first two messages if they are system messages
    # (position 0 = system prompt, position 1 = campaign context)
    preserved = []
    prunable = []
    for i, m in enumerate(messages):
        if i < 2 and m["role"] == "system":
            preserved.append(m)
        else:
            prunable.append(m)

    while prunable and estimate_message_tokens(preserved + prunable) > max_tokens:
        prunable.pop(0)

    return preserved + prunable


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
                # Only retry on rate limit errors, not on any exception
                # containing "rate" in its string representation
                error_type = type(e).__name__
                if error_type in ("RateLimitError", "APIStatusError") and "429" in str(e):
                    wait = 2**attempt + 1
                    logger.warning("Rate limited, retrying in %ds (%d/%d)", wait, attempt + 1, MAX_RETRIES)
                    time.sleep(wait)
                else:
                    raise
        raise RuntimeError(f"Failed after {MAX_RETRIES} retries due to rate limiting")
