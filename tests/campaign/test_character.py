import tempfile
from pathlib import Path
from campaign.character import Character, save_character, load_character, list_characters, validate_character, get_effective_thresholds

SAMPLE = {
    "name": "Kira Ashveil", "class": "Sorcerer", "subclass": "Elemental Origin",
    "level": 1, "tier": 1, "ancestry": "Drakona", "community": "Wildborne",
    "traits": {"agility": 0, "strength": -1, "finesse": 1, "instinct": 1, "presence": 0, "knowledge": 2},
    "evasion": 10, "proficiency": 1,
    "hp": {"max": 6, "marked": 0}, "stress": {"max": 6, "marked": 0},
    "hope": {"current": 2, "max": 6, "scars": 0},
    "armor": {"name": "Gambeson", "base_score": 3, "slots_marked": 0, "base_major": 5, "base_severe": 11, "feature": "Flexible: +1 Evasion"},
    "weapons": [{"name": "Staff", "trait": "knowledge", "range": "melee", "damage": "d8+2", "burden": "two-handed", "type": "physical"}],
    "domains": ["Arcana", "Midnight"], "domain_cards": {"loadout": [], "vault": []},
    "experiences": [{"name": "Volcano-born", "modifier": 2}, {"name": "Reckless", "modifier": 2}],
}

class TestCharacter:
    def test_from_dict(self):
        char = Character.from_dict(SAMPLE)
        assert char.name == "Kira Ashveil"
        assert char.char_class == "Sorcerer"

    def test_to_dict_roundtrip(self):
        d = Character.from_dict(SAMPLE).to_dict()
        assert d["name"] == "Kira Ashveil"
        assert d["traits"]["knowledge"] == 2

    def test_save_and_load(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            save_character(Character.from_dict(SAMPLE), Path(tmpdir))
            loaded = load_character("Kira Ashveil", Path(tmpdir))
            assert loaded.char_class == "Sorcerer"

    def test_list_characters(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            save_character(Character.from_dict(SAMPLE), Path(tmpdir))
            assert "Kira Ashveil" in list_characters(Path(tmpdir))

    def test_effective_thresholds_level_1(self):
        major, severe = get_effective_thresholds(Character.from_dict(SAMPLE))
        assert major == 6 and severe == 12

    def test_effective_thresholds_level_5(self):
        major, severe = get_effective_thresholds(Character.from_dict({**SAMPLE, "level": 5}))
        assert major == 10 and severe == 16

class TestValidate:
    def test_valid(self):
        assert len(validate_character(SAMPLE)) == 0

    def test_invalid_trait_spread(self):
        data = {**SAMPLE, "traits": {k: 3 for k in SAMPLE["traits"]}}
        assert any("trait" in e.lower() for e in validate_character(data))

    def test_missing_field(self):
        data = {k: v for k, v in SAMPLE.items() if k != "name"}
        assert any("name" in e.lower() for e in validate_character(data))
