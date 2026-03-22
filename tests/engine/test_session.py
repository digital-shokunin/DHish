import json
import tempfile
from pathlib import Path
from engine.session import save_session, load_session

class TestSessionPersistence:
    def test_save_and_load_roundtrip(self):
        messages = [
            {"role": "system", "content": "You are a GM."},
            {"role": "user", "content": "I look around."},
            {"role": "assistant", "content": "You see a dark cave."},
        ]
        with tempfile.NamedTemporaryFile(suffix=".json", delete=False) as f:
            path = Path(f.name)
        try:
            save_session(messages, path)
            loaded = load_session(path)
            assert len(loaded) == 3
            assert loaded[1]["content"] == "I look around."
        finally:
            path.unlink(missing_ok=True)

    def test_save_creates_parent_dirs(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            path = Path(tmpdir) / "sub" / "dir" / "session.json"
            save_session([{"role": "system", "content": "test"}], path)
            assert path.exists()

    def test_load_replaces_system_prompt(self):
        messages = [{"role": "system", "content": "old"}, {"role": "user", "content": "hi"}]
        with tempfile.NamedTemporaryFile(suffix=".json", delete=False) as f:
            path = Path(f.name)
        try:
            save_session(messages, path)
            loaded = load_session(path, new_system_prompt="new")
            assert loaded[0]["content"] == "new"
            assert loaded[1]["content"] == "hi"
        finally:
            path.unlink(missing_ok=True)

    def test_load_without_replacement(self):
        messages = [{"role": "system", "content": "original"}]
        with tempfile.NamedTemporaryFile(suffix=".json", delete=False) as f:
            path = Path(f.name)
        try:
            save_session(messages, path)
            loaded = load_session(path)
            assert loaded[0]["content"] == "original"
        finally:
            path.unlink(missing_ok=True)

    def test_saved_json_is_valid(self):
        messages = [{"role": "system", "content": "test"}]
        with tempfile.NamedTemporaryFile(suffix=".json", delete=False) as f:
            path = Path(f.name)
        try:
            save_session(messages, path)
            with open(path) as f:
                data = json.load(f)
            assert isinstance(data, list)
        finally:
            path.unlink(missing_ok=True)
