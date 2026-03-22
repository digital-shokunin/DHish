#!/usr/bin/env python3
"""Daggerheart Campaign Tool -- AI Game Master and Campaign Manager.

A BXish-inspired tool for running Daggerheart RPG sessions with an AI GM.
"""

import argparse
import logging
import os
import sys
from pathlib import Path

from config import (
    VERSION,
    DEFAULT_PORT,
    DEFAULT_TEMPERATURE,
    PROVIDER_PRESETS,
    resolve_provider,
)
from engine.skill_loader import load_skills, build_system_prompt, estimate_tokens
from engine.session import load_session


def parse_args():
    parser = argparse.ArgumentParser(
        description="Daggerheart Campaign Tool -- AI Game Master and Campaign Manager"
    )
    parser.add_argument("--web", action="store_true", help="Launch Gradio web UI")
    parser.add_argument("--port", type=int, default=DEFAULT_PORT, help=f"Web UI port (default: {DEFAULT_PORT})")
    parser.add_argument("--provider", choices=list(PROVIDER_PRESETS.keys()), help="Provider preset")
    parser.add_argument("--model", help="Model name or identifier")
    parser.add_argument("--base-url", help="Custom API base URL (overrides provider)")
    parser.add_argument("--api-key", help="API key (or use env var)")
    parser.add_argument("--tier", choices=["core", "gm", "full"], default="full", help="Skill tier (default: full)")
    parser.add_argument("--skills-dir", type=Path, help="Path to skill files")
    parser.add_argument("--campaign", help="Campaign name to load or create")
    parser.add_argument("--session", type=Path, help="Resume from saved session JSON")
    parser.add_argument("--temperature", type=float, default=DEFAULT_TEMPERATURE)
    parser.add_argument("--dice-mode", choices=["app", "ai", "manual"], default="app")
    parser.add_argument("--list-models", action="store_true", help="Print model info and exit")
    parser.add_argument("--local", action="store_true", help="Use local LLM server (alias for --provider local)")
    parser.add_argument("--verbose", action="store_true", help="Enable debug logging")
    return parser.parse_args()


def main():
    args = parse_args()

    logging.basicConfig(
        level=logging.DEBUG if args.verbose else logging.INFO,
        format="%(levelname)s: %(message)s",
    )
    logger = logging.getLogger(__name__)

    if args.list_models:
        print("Provider Presets:")
        for name, preset in PROVIDER_PRESETS.items():
            model = preset.get("default_model") or "(auto/user-configured)"
            print(f"  {name:12s} {model}")
        sys.exit(0)

    # Resolve provider
    provider = "local" if args.local else args.provider
    if not provider and not args.base_url:
        print("Error: specify --provider, --base-url, or --local", file=sys.stderr)
        sys.exit(1)

    base_url, env_var = resolve_provider(provider, args.base_url)

    # Resolve API key
    api_key = args.api_key
    if not api_key and env_var:
        api_key = os.environ.get(env_var)
    if not api_key and not args.local and provider != "local":
        env_hint = f" (or set {env_var})" if env_var else ""
        print(f"Error: --api-key required{env_hint}", file=sys.stderr)
        sys.exit(1)

    # Resolve model
    model = args.model
    if not model and provider and PROVIDER_PRESETS.get(provider, {}).get("default_model"):
        model = PROVIDER_PRESETS[provider]["default_model"]

    # Set up OpenAI client
    from openai import OpenAI

    client_kwargs = {"base_url": base_url}
    if api_key:
        client_kwargs["api_key"] = api_key
    else:
        client_kwargs["api_key"] = "not-needed"

    client = OpenAI(**client_kwargs)

    # Auto-discover model for local
    if not model:
        if provider == "local" or args.local:
            try:
                models = client.models.list()
                model = models.data[0].id
                logger.info("Auto-discovered local model: %s", model)
            except Exception as e:
                print(f"Error: could not auto-discover local model: {e}", file=sys.stderr)
                sys.exit(1)
        else:
            print("Error: --model required (no default for this provider)", file=sys.stderr)
            sys.exit(1)

    # Load skills
    skills_dir = args.skills_dir or (Path(__file__).parent / "skills")
    skills_text = load_skills(skills_dir, args.tier)
    system_prompt = build_system_prompt(skills_text)
    prompt_tokens = estimate_tokens(system_prompt)
    logger.info("System prompt: ~%d tokens (%s tier)", prompt_tokens, args.tier)

    # Determine context limit (default 128K, reserve 75%)
    from config import CONTEXT_RESERVE_RATIO
    max_context = 128000
    conversation_budget = int(max_context * CONTEXT_RESERVE_RATIO)

    if prompt_tokens > max_context // 2:
        logger.warning(
            "System prompt (~%d tokens) exceeds 50%% of context window (%d). "
            "Consider using a lower tier or a model with a larger context window.",
            prompt_tokens, max_context,
        )

    # Build messages
    messages = [{"role": "system", "content": system_prompt}]

    # Load session if resuming
    if args.session:
        messages = load_session(args.session, new_system_prompt=system_prompt)
        logger.info("Resumed session from %s", args.session)

    # Campaign context injection
    campaign = None
    party = None
    if args.campaign:
        from campaign.state import load_campaign, create_campaign
        from campaign.party import load_party, build_campaign_context

        campaigns_base = Path(__file__).parent / "campaigns"
        try:
            campaign = load_campaign(args.campaign, campaigns_base)
        except FileNotFoundError:
            campaign = create_campaign(args.campaign, campaigns_base)
            logger.info("Created new campaign: %s", args.campaign)

        party = load_party(campaign.campaign_dir / "party")
        context_msg = build_campaign_context(
            characters=party,
            fear=campaign.fear,
            countdowns=campaign.countdowns,
            current_location=campaign.current_location,
        )
        # Insert context at position 1 (after system prompt)
        if len(messages) > 1 and messages[1].get("role") == "system":
            messages[1]["content"] = context_msg
        else:
            messages.insert(1, {"role": "system", "content": context_msg})

    # Create agent
    from engine.agent import DaggerheartAgent

    agent = DaggerheartAgent(
        client=client,
        model=model,
        system_prompt=system_prompt,
        max_context=conversation_budget,
        temperature=args.temperature,
    )

    # Launch
    if args.web:
        # Lazy import for web UI
        from ui.web import launch_web_ui
        campaign_dir = campaign.campaign_dir if args.campaign else None
        launch_web_ui(agent, messages, port=args.port, campaign_dir=campaign_dir)
    else:
        from ui.terminal import run_terminal
        from datetime import datetime as _dt

        session_path = None
        if args.campaign:
            session_path = campaign.campaign_dir / "sessions" / f"session-{_dt.now().strftime('%Y%m%d-%H%M%S')}.json"

        run_terminal(
            agent=agent,
            messages=messages,
            session_path=session_path,
            campaign_name=args.campaign or "",
            tier=args.tier,
            campaign=campaign if args.campaign else None,
            party=party if args.campaign else None,
        )


if __name__ == "__main__":
    main()
