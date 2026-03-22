"""LLM-powered generators for Daggerheart campaign content."""


def _generate(agent, system_messages, prompt):
    """Helper: send a generation prompt to the agent and return the response."""
    messages = list(system_messages) + [{"role": "user", "content": prompt}]
    return agent.send(messages)


def generate_location(agent, messages, context=""):
    prompt = f"Generate a detailed Daggerheart location. Include: name, description, notable features, potential hooks, NPCs present. {f'Context: {context}' if context else ''}"
    return _generate(agent, messages, prompt)


def generate_shop_inventory(agent, messages, tier=1, context=""):
    prompt = f"Generate a Daggerheart shop or tavern inventory for Tier {tier}. Include item names, descriptions, and prices in gold. {f'Context: {context}' if context else ''}"
    return _generate(agent, messages, prompt)


def generate_encounter(agent, messages, party_size=4, tier=1, context=""):
    from campaign.encounter import calculate_battle_points
    bp = calculate_battle_points(party_size)
    prompt = f"Generate a Daggerheart encounter for {party_size} PCs at Tier {tier}. Battle Points budget: {bp}. Include adversary names, types, stat blocks, tactics, and environment. {f'Context: {context}' if context else ''}"
    return _generate(agent, messages, prompt)


def generate_quest_hook(agent, messages, context=""):
    prompt = f"Generate a Daggerheart quest hook. Include: hook summary, key NPCs involved, potential complications, rewards. {f'Context: {context}' if context else ''}"
    return _generate(agent, messages, prompt)


def generate_name(agent, messages, ancestry="Human"):
    prompt = f"Generate a single Daggerheart character name for a {ancestry} character. Return ONLY the name, nothing else."
    return _generate(agent, messages, prompt)


def generate_treasure(agent, messages, tier=1):
    prompt = f"Generate Daggerheart treasure/loot appropriate for Tier {tier}. Include items, gold amounts, and any special properties."
    return _generate(agent, messages, prompt)
