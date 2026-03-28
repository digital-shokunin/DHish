# ui/web.py
"""Gradio web UI for Daggerheart Campaign Tool."""

import json
from datetime import datetime
from pathlib import Path

from config import VERSION
from engine.agent import DaggerheartAgent, estimate_message_tokens
from engine.dice import roll, roll_duality
from engine.session import save_session

CSS = """
.gradio-container { background: #0d0d1a !important; min-height: 100vh; }
.chatbot .message.bot { background: #1a1a2e !important; color: #e0d6c2 !important; }
.chatbot .message.user { background: #b8d4e8 !important; color: #111 !important; }
table { border-collapse: collapse; width: 100%; }
th { background: #2a2a3e; padding: 8px; }
td { border: 1px solid #444; padding: 8px; }
pre, code { background: #111 !important; }
.status-bar { font-size: 12px; color: #888; text-align: right; }
footer { display: none !important; max-height: 0 !important; }
"""

GREETING = """Welcome to the world of **Daggerheart**!

Choose how to begin:
1. **Start a new campaign** -- Create characters and begin your adventure
2. **Continue an existing campaign** -- Pick up where you left off
3. **Run a one-shot adventure** -- A standalone session
4. **Create a character** -- Build a new character with guided creation or quick-gen

What would you like to do?"""


def launch_web_ui(
    agent: DaggerheartAgent,
    messages: list[dict],
    port: int = 7860,
    campaign_dir: Path | None = None,
):
    """Launch the Gradio web interface.

    Args:
        agent: Configured DaggerheartAgent.
        messages: Initial message list (with system prompt).
        port: Port to serve on.
        campaign_dir: Path to active campaign directory (or None).
    """
    import gradio as gr

    # Mutable state (closure-captured, single-user)
    conversation = list(messages)
    if campaign_dir:
        session_file = campaign_dir / "sessions" / f"session-{datetime.now().strftime('%Y%m%d-%H%M%S')}.json"
    else:
        session_file = Path("sessions") / f"session-{datetime.now().strftime('%Y%m%d-%H%M%S')}.json"
    dice_mode = ["app"]  # mutable list for closure capture

    def respond(user_msg, chat_history):
        if not user_msg.strip():
            return chat_history, "", _status_text()

        conversation.append({"role": "user", "content": user_msg})

        try:
            response = agent.send(conversation)
        except Exception as e:
            response = f"[Error: {e}]"

        conversation.append({"role": "assistant", "content": response})
        chat_history = chat_history or []
        chat_history.append({"role": "user", "content": user_msg})
        chat_history.append({"role": "assistant", "content": response})
        return chat_history, "", _status_text()

    def do_save():
        save_session(conversation, session_file)
        return f"Session saved to {session_file}"

    def do_new():
        nonlocal conversation
        conversation = [conversation[0]]  # Keep system prompt
        return [], _status_text(), "New session started"

    def do_roll(notation):
        if not notation.strip():
            return "Enter dice notation (e.g., 2d12, 1d8+3)"
        try:
            result = roll(notation.strip())
            return f"Rolled {result.notation}: {result.dice} = {result.total}"
        except ValueError as e:
            return str(e)

    def do_duality():
        result = roll_duality(modifier=0, difficulty=11)
        outcome_labels = {
            "success_hope": "Success with Hope",
            "success_fear": "Success with Fear",
            "failure_hope": "Failure with Hope",
            "failure_fear": "Failure with Fear",
            "critical": "CRITICAL SUCCESS!",
        }
        label = outcome_labels.get(result.outcome_type, result.outcome_type)
        return (
            f"Hope [{result.hope_die}] Fear [{result.fear_die}] | "
            f"Total: {result.modified_total} vs {result.difficulty} | "
            f"{label}"
        )

    def do_load_context(files, chat_history):
        if not files:
            return chat_history, "No files selected"
        contents = []
        for f in files:
            text = Path(f.name).read_text(encoding="utf-8", errors="replace")
            contents.append(text)
        combined = "\n\n---\n\n".join(contents)
        context_msg = (
            "Here are transcripts from previous adventure sessions. "
            "Use these as background context for the current campaign. "
            "Do not repeat this content in chat.\n\n" + combined
        )
        conversation.append({"role": "user", "content": context_msg})
        try:
            response = agent.send(conversation)
        except Exception as e:
            response = f"[Error loading context: {e}]"
        conversation.append({"role": "assistant", "content": response})
        chat_history = chat_history or []
        chat_history.append({"role": "assistant", "content": response})
        return chat_history, f"Loaded {len(files)} context file(s)"

    def _status_text():
        tokens = estimate_message_tokens(conversation)
        msg_count = len([m for m in conversation if m["role"] not in ("system",)])
        parts = [f"Model: {agent.model}", f"Tokens: ~{tokens}", f"Messages: {msg_count}"]
        # Add Hope/Fear if campaign is loaded
        if campaign_dir:
            try:
                from campaign.state import load_campaign
                camp = load_campaign(campaign_dir.name, campaign_dir.parent)
                parts.append(f"Fear: {camp.fear}/12")
            except Exception:
                pass
            try:
                from campaign.party import load_party
                party = load_party(campaign_dir / "party")
                hope_total = sum(c.hope["current"] for c in party)
                parts.append(f"Party Hope: {hope_total}")
            except Exception:
                pass
        return " | ".join(parts)

    def _on_dice_mode_change(mode):
        dice_mode[0] = mode.lower().replace(" ", "_")

    # Build UI
    theme = gr.themes.Base(
        primary_hue="amber",
        secondary_hue="stone",
        neutral_hue="stone",
    )

    with gr.Blocks(title="Daggerheart Campaign Tool") as app:
        gr.Markdown(f"# Daggerheart Campaign Tool v{VERSION}")

        with gr.Tabs():
            # Tab 1: Adventure
            with gr.Tab("Adventure"):
                chatbot = gr.Chatbot(
                    value=[{"role": "assistant", "content": GREETING}],
                    height=500,
                )
                with gr.Row():
                    msg_input = gr.Textbox(
                        placeholder="What do you do?",
                        scale=9,
                        show_label=False,
                        autofocus=True,
                    )
                    send_btn = gr.Button("Send", variant="primary", scale=1)
                with gr.Row():
                    dice_mode_radio = gr.Radio(
                        choices=["App Roll", "AI Narrates", "Manual"],
                        value="App Roll", label="Dice Mode", scale=3,
                    )
                    roll_input = gr.Textbox(placeholder="e.g. 2d12+3", scale=3, show_label=False)
                    roll_btn = gr.Button("Roll", scale=1)
                    duality_btn = gr.Button("Duality Roll", scale=1)
                    roll_output = gr.Textbox(interactive=False, scale=4, show_label=False)
                with gr.Row():
                    save_btn = gr.Button("Save Session", size="sm", scale=1)
                    new_btn = gr.Button("New Session", size="sm", scale=1)
                    context_upload = gr.File(
                        label="Load Context",
                        file_count="multiple",
                        file_types=[".md", ".txt", ".json"],
                        scale=4,
                    )
                    info_box = gr.Textbox(interactive=False, show_label=False, scale=4)
                status_bar = gr.Markdown(_status_text(), elem_classes=["status-bar"])

                # Event handlers
                send_btn.click(respond, [msg_input, chatbot], [chatbot, msg_input, status_bar])
                msg_input.submit(respond, [msg_input, chatbot], [chatbot, msg_input, status_bar])
                save_btn.click(do_save, [], [info_box])
                new_btn.click(do_new, [], [chatbot, status_bar, info_box])
                roll_btn.click(do_roll, [roll_input], [roll_output])
                duality_btn.click(do_duality, [], [roll_output])
                context_upload.change(do_load_context, [context_upload, chatbot], [chatbot, info_box])
                dice_mode_radio.change(_on_dice_mode_change, [dice_mode_radio], [])

            # Tab 2: Party (placeholder)
            with gr.Tab("Party"):
                gr.Markdown("## Party Management\n*Coming soon -- manage your party members here.*")

            # Tab 3: Campaign World (placeholder)
            with gr.Tab("Campaign World"):
                gr.Markdown("## Campaign World\n*Coming soon -- locations, factions, NPCs, countdowns.*")

            # Tab 4: Encounter Workshop (placeholder)
            with gr.Tab("Encounter Workshop"):
                gr.Markdown("## Encounter Workshop\n*Coming soon -- build balanced encounters.*")

            # Tab 5: Journal (placeholder)
            with gr.Tab("Journal"):
                gr.Markdown("## Session Journal\n*Coming soon -- session notes and summaries.*")

        # Initialize greeting in conversation
        if not any(m.get("role") == "assistant" for m in conversation):
            conversation.append({"role": "assistant", "content": GREETING})

    app.launch(server_name="0.0.0.0", server_port=port, share=False, inbrowser=True, css=CSS)
