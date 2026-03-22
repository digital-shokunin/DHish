import tempfile
from pathlib import Path
from campaign.encounter import (
    calculate_battle_points, get_adversary_bp_cost,
    validate_encounter, save_encounter, load_encounter, list_encounters,
)

class TestEncounter:
    def test_battle_points_4_pcs(self):
        assert calculate_battle_points(4) == 14

    def test_battle_points_2_pcs(self):
        assert calculate_battle_points(2) == 8

    def test_adversary_bp_costs(self):
        assert get_adversary_bp_cost("minion") == 1
        assert get_adversary_bp_cost("standard") == 2
        assert get_adversary_bp_cost("leader") == 3
        assert get_adversary_bp_cost("bruiser") == 4
        assert get_adversary_bp_cost("solo") == 5

    def test_validate_under_budget(self):
        adversaries = [{"type": "standard"}, {"type": "minion"}]
        result = validate_encounter(adversaries, 4)
        assert result["budget"] == 14
        assert result["total_cost"] == 3
        assert not result["over_budget"]

    def test_validate_over_budget(self):
        adversaries = [{"type": "solo"}, {"type": "solo"}, {"type": "solo"}]
        result = validate_encounter(adversaries, 2)
        assert result["over_budget"]

    def test_save_and_load(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            d = Path(tmpdir)
            data = {"name": "Ambush", "adversaries": [{"name": "Wolf", "type": "standard"}]}
            save_encounter(data, d)
            loaded = load_encounter("Ambush", d)
            assert loaded["name"] == "Ambush"

    def test_list_encounters(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            d = Path(tmpdir)
            save_encounter({"name": "Fight One"}, d)
            save_encounter({"name": "Fight Two"}, d)
            assert len(list_encounters(d)) == 2
