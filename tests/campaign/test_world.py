import tempfile
from pathlib import Path
from campaign.world import save_entity, load_entity, list_entities, delete_entity

class TestWorld:
    def test_save_and_load_location(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            d = Path(tmpdir)
            save_entity("Silver Mines", "A deep mine with silver veins.", "location", d)
            content = load_entity("Silver Mines", "location", d)
            assert "Silver Mines" in content
            assert "silver veins" in content

    def test_list_entities(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            d = Path(tmpdir)
            save_entity("Town Square", "A bustling square.", "location", d)
            save_entity("Dark Forest", "An eerie forest.", "location", d)
            names = list_entities("location", d)
            assert len(names) == 2

    def test_delete_entity(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            d = Path(tmpdir)
            save_entity("Old Ruins", "Crumbling ruins.", "location", d)
            assert delete_entity("Old Ruins", "location", d)
            assert len(list_entities("location", d)) == 0

    def test_list_empty(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            assert list_entities("location", Path(tmpdir)) == []

    def test_faction_entity(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            d = Path(tmpdir)
            save_entity("Iron Guild", "A merchant guild.", "faction", d)
            assert "Iron Guild" in list_entities("faction", d)
