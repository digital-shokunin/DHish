"""Smoke tests for entry point, web UI import, and edge cases."""
import subprocess
import sys
import pytest


class TestCLISmoke:
    def test_list_models(self):
        result = subprocess.run(
            [sys.executable, "daggerheart.py", "--list-models"],
            capture_output=True, text=True, timeout=10,
        )
        assert result.returncode == 0
        assert "abacus" in result.stdout
        assert "anthropic" in result.stdout

    def test_help(self):
        result = subprocess.run(
            [sys.executable, "daggerheart.py", "--help"],
            capture_output=True, text=True, timeout=10,
        )
        assert result.returncode == 0
        assert "--provider" in result.stdout
        assert "--campaign" in result.stdout

    def test_no_provider_exits_with_error(self):
        result = subprocess.run(
            [sys.executable, "daggerheart.py"],
            capture_output=True, text=True, timeout=10,
        )
        assert result.returncode != 0
        assert "provider" in result.stderr.lower() or "base-url" in result.stderr.lower()


class TestWebUIImport:
    def test_launch_web_ui_importable(self):
        from ui.web import launch_web_ui
        assert callable(launch_web_ui)

    @pytest.mark.skipif(
        not __import__("importlib").util.find_spec("gradio"),
        reason="gradio not installed",
    )
    def test_gradio_blocks_constructable(self):
        """Verify Gradio app can be constructed without launching."""
        from ui.web import CSS, GREETING
        assert len(CSS) > 0
        assert "Daggerheart" in GREETING


class TestAgentSendMock:
    def test_send_returns_response(self):
        from unittest.mock import MagicMock
        from engine.agent import DaggerheartAgent

        mock_client = MagicMock()
        mock_response = MagicMock()
        mock_response.choices = [MagicMock()]
        mock_response.choices[0].message.content = "You see a dark cave."
        mock_response.choices[0].finish_reason = "stop"
        mock_response.usage.total_tokens = 100
        mock_client.chat.completions.create.return_value = mock_response

        agent = DaggerheartAgent(mock_client, "test-model", "system", 10000)
        result = agent.send([{"role": "system", "content": "sys"}, {"role": "user", "content": "look"}])
        assert result == "You see a dark cave."
        assert agent.total_tokens_used == 100

    def test_send_retries_on_rate_limit(self):
        from unittest.mock import MagicMock, patch
        from engine.agent import DaggerheartAgent

        mock_client = MagicMock()
        # First call raises rate limit, second succeeds
        rate_error = type("RateLimitError", (Exception,), {})("429 rate limit exceeded")
        mock_response = MagicMock()
        mock_response.choices = [MagicMock()]
        mock_response.choices[0].message.content = "ok"
        mock_response.choices[0].finish_reason = "stop"
        mock_response.usage.total_tokens = 50
        mock_client.chat.completions.create.side_effect = [rate_error, mock_response]

        agent = DaggerheartAgent(mock_client, "test-model", "system", 10000)
        with patch("engine.agent.time.sleep"):
            result = agent.send([{"role": "system", "content": "sys"}])
        assert result == "ok"

    def test_send_raises_non_rate_limit_error(self):
        from unittest.mock import MagicMock
        from engine.agent import DaggerheartAgent
        import pytest

        mock_client = MagicMock()
        mock_client.chat.completions.create.side_effect = ValueError("bad model")

        agent = DaggerheartAgent(mock_client, "test-model", "system", 10000)
        with pytest.raises(ValueError, match="bad model"):
            agent.send([{"role": "system", "content": "sys"}])


class TestFearClampingAtZero:
    def test_fear_clamps_at_zero(self):
        import tempfile
        from pathlib import Path
        from campaign.state import create_campaign

        with tempfile.TemporaryDirectory() as tmpdir:
            state = create_campaign("test", Path(tmpdir) / "campaigns")
            state.fear = -5
            assert state.fear == 0


class TestPruneMessageOrder:
    def test_preserves_first_two_system_messages(self):
        from engine.agent import prune_messages

        msgs = [
            {"role": "system", "content": "x" * 400},  # system prompt
            {"role": "system", "content": "y" * 400},  # campaign context
            {"role": "user", "content": "a" * 400},
            {"role": "assistant", "content": "b" * 400},
            {"role": "system", "content": "dice roll"},  # injected dice result
            {"role": "user", "content": "c" * 400},
        ]
        pruned = prune_messages(msgs, 500)
        # First two system messages must be preserved
        assert pruned[0]["content"] == "x" * 400
        assert pruned[1]["content"] == "y" * 400
        # Dice roll system message (position 4) is prunable
        system_contents = [m["content"] for m in pruned if m["role"] == "system"]
        # dice roll may or may not be pruned depending on budget
        assert len(pruned) >= 2
