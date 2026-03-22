import tempfile
from pathlib import Path
from campaign.adversary import save_adversary, load_adversary, list_adversaries

class TestAdversary:
    def test_save_and_load(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            d = Path(tmpdir)
            data = {"name": "Shadow Wolf", "tier": 1, "type": "standard", "difficulty": 11, "hp": 5}
            save_adversary(data, d)
            loaded = load_adversary("Shadow Wolf", d)
            assert loaded["name"] == "Shadow Wolf"
            assert loaded["hp"] == 5

    def test_list_adversaries(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            d = Path(tmpdir)
            save_adversary({"name": "Goblin"}, d)
            save_adversary({"name": "Orc"}, d)
            names = list_adversaries(d)
            assert len(names) == 2
