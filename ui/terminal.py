# ui/terminal.py
"""Terminal chat interface for Daggerheart Campaign Tool."""

import sys
from datetime import datetime
from pathlib import Path

from config import VERSION
from engine.agent import DaggerheartAgent, estimate_message_tokens
from engine.dice import roll, roll_duality
from engine.session import save_session


GREETING = """Welcome to the world of Daggerheart!

Choose how to begin:
1. Start a new campaign
2. Continue an existing campaign
3. Run a one-shot adventure
4. Create a character

What would you like to do?"""


def _print_status(agent, messages, campaign=None, party=None):
    tokens = estimate_message_tokens(messages)
    msg_count = len([m for m in messages if m["role"] != "system"])
    parts = [
        f"Model: {agent.model}",
        f"Tokens: ~{tokens}",
        f"Messages: {msg_count}",
        f"API tokens: {agent.total_tokens_used}",
    ]
    if campaign:
        parts.append(f"Fear: {campaign.fear}/12")
    if party:
        for c in party:
            parts.append(f"{c.name}: HP {c.hp['marked']}/{c.hp['max']} Stress {c.stress['marked']}/{c.stress['max']} Hope {c.hope['current']}/{c.hope['max']}")
    print("\n[Status] " + " | ".join(parts))


def _handle_roll_command(args: str) -> str | None:
    """Handle the 'roll' command, returning a result string."""
    if not args:
        return "Usage: roll <notation> (e.g., roll 2d12, roll 1d8+3)"
    try:
        result = roll(args)
        return f"Rolled {result.notation}: {result.dice} + {result.modifier} = {result.total}"
    except ValueError as e:
        return f"Invalid dice notation: {e}"


def _handle_duality_command(args: str) -> str:
    """Handle the 'duality' command. Optional args: modifier difficulty."""
    parts = args.split() if args else []
    modifier = int(parts[0]) if len(parts) >= 1 else 0
    difficulty = int(parts[1]) if len(parts) >= 2 else 11
    result = roll_duality(modifier=modifier, difficulty=difficulty)
    outcome_labels = {
        "success_hope": "Success with Hope",
        "success_fear": "Success with Fear",
        "failure_hope": "Failure with Hope",
        "failure_fear": "Failure with Fear",
        "critical": "CRITICAL SUCCESS!",
    }
    label = outcome_labels.get(result.outcome_type, result.outcome_type)
    lines = [
        f"Duality Roll: Hope [{result.hope_die}] Fear [{result.fear_die}]",
        f"   Total: {result.raw_total} + {modifier} = {result.modified_total} vs Difficulty {result.difficulty}",
        f"   Result: {label}",
    ]
    if result.hope_gained:
        lines.append("   -> Player gains 1 Hope")
    if result.fear_gained:
        lines.append("   -> GM gains 1 Fear")
    if result.stress_cleared:
        lines.append("   -> Player clears 1 Stress")
    return "\n".join(lines)


def run_terminal(
    agent: DaggerheartAgent,
    messages: list[dict],
    session_path: Path | None = None,
    campaign_name: str = "",
    tier: str = "full",
    campaign=None,
    party: list | None = None,
):
    """Run the interactive terminal chat loop.

    Args:
        agent: Configured DaggerheartAgent.
        messages: Initial message list (with system prompt).
        session_path: Path to save session files.
        campaign_name: Name of active campaign (for display).
        tier: Skill tier loaded (for display).
        campaign: CampaignState instance (or None).
        party: List of Character instances (or None).
    """
    if session_path is None:
        session_path = Path("sessions") / f"session-{datetime.now().strftime('%Y%m%d-%H%M%S')}.json"

    # Header
    parts = [f"Daggerheart GM v{VERSION}", f"Model: {agent.model}", f"Tier: {tier}"]
    if campaign_name:
        parts.append(f"Campaign: {campaign_name}")
    print(" | ".join(parts))
    print("Type 'help' for commands.\n")

    # Show greeting if this is a new session
    if len(messages) <= 2:  # system prompt + optional context
        print(f"GM> {GREETING}\n")
        messages.append({"role": "assistant", "content": GREETING})

    while True:
        try:
            user_input = input("> ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\n")
            user_input = "quit"

        if not user_input:
            continue

        # Handle commands
        cmd = user_input.lower().split()[0]
        cmd_args = user_input[len(cmd):].strip()

        if cmd in ("quit", "exit"):
            save_session(messages, session_path)
            print(f"Session saved to {session_path}. Goodbye!")
            break

        elif cmd == "save":
            save_session(messages, session_path)
            print(f"Session saved to {session_path}")
            continue

        elif cmd == "status":
            _print_status(agent, messages, campaign, party)
            continue

        elif cmd == "roll":
            print(_handle_roll_command(cmd_args))
            continue

        elif cmd == "duality":
            print(_handle_duality_command(cmd_args))
            continue

        elif cmd == "party":
            if party:
                from campaign.party import get_party_summary
                print(f"\n{get_party_summary(party)}\n")
            else:
                print("No party loaded. Use --campaign to load a campaign.")
            continue

        elif cmd == "hope":
            if party:
                for c in party:
                    print(f"  {c.name}: Hope {c.hope['current']}/{c.hope['max']} (Scars: {c.hope['scars']})")
            else:
                print("No party loaded.")
            continue

        elif cmd == "fear":
            if campaign:
                print(f"  GM Fear: {campaign.fear}/12")
            else:
                print("No campaign loaded.")
            continue

        elif cmd == "help":
            print("Commands: save, status, roll <notation>, duality [modifier] [difficulty],")
            print("          party, hope, fear, help, quit")
            continue

        # Regular chat input
        messages.append({"role": "user", "content": user_input})

        try:
            response = agent.send(messages)
            messages.append({"role": "assistant", "content": response})
            print(f"\nGM> {response}\n")
        except Exception as e:
            print(f"\n[Error] {e}\n")
            messages.pop()  # Remove the failed user message
