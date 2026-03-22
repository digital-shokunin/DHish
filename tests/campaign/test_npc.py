import tempfile
from pathlib import Path
from campaign.npc import save_npc, load_npc, list_npcs

class TestNpc:
    def test_save_and_load(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            d = Path(tmpdir)
            save_npc("Mira the Sage", "A wise elder who knows ancient secrets.", d)
            content = load_npc("Mira the Sage", d)
            assert "Mira the Sage" in content
            assert "ancient secrets" in content

    def test_list_npcs(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            d = Path(tmpdir)
            save_npc("Guard Captain", "Stern but fair.", d)
            save_npc("Tavern Keep", "Friendly and talkative.", d)
            names = list_npcs(d)
            assert len(names) == 2

    def test_list_empty(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            assert list_npcs(Path(tmpdir)) == []
