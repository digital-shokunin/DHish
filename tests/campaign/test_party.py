import tempfile
from pathlib import Path
from campaign.character import Character, save_character
from campaign.party import load_party, get_party_summary, build_campaign_context

C1 = {
    "name": "Kira", "class": "Sorcerer", "subclass": "Elemental Origin",
    "level": 1, "tier": 1, "ancestry": "Drakona", "community": "Wildborne",
    "traits": {"agility": 0, "strength": -1, "finesse": 1, "instinct": 1, "presence": 0, "knowledge": 2},
    "evasion": 10, "proficiency": 1,
    "hp": {"max": 6, "marked": 1}, "stress": {"max": 6, "marked": 0},
    "hope": {"current": 3, "max": 6, "scars": 0},
    "armor": {"name": "Gambeson", "base_score": 3, "slots_marked": 0, "base_major": 5, "base_severe": 11, "feature": ""},
    "weapons": [], "domains": ["Arcana", "Midnight"], "domain_cards": {"loadout": [], "vault": []},
    "experiences": [{"name": "Test", "modifier": 2}],
}
C2 = {
    "name": "Bron", "class": "Guardian", "subclass": "Stalwart",
    "level": 1, "tier": 1, "ancestry": "Dwarf", "community": "Ridgeborne",
    "traits": {"agility": -1, "strength": 2, "finesse": 0, "instinct": 0, "presence": 1, "knowledge": 1},
    "evasion": 9, "proficiency": 1,
    "hp": {"max": 7, "marked": 0}, "stress": {"max": 6, "marked": 2},
    "hope": {"current": 2, "max": 6, "scars": 0},
    "armor": {"name": "Chainmail", "base_score": 4, "slots_marked": 1, "base_major": 7, "base_severe": 15, "feature": ""},
    "weapons": [], "domains": ["Blade", "Valor"], "domain_cards": {"loadout": [], "vault": []},
    "experiences": [{"name": "Test", "modifier": 2}],
}

class TestParty:
    def test_load_party(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            save_character(Character.from_dict(C1), Path(tmpdir))
            save_character(Character.from_dict(C2), Path(tmpdir))
            party = load_party(Path(tmpdir))
            assert len(party) == 2

    def test_party_summary(self):
        summary = get_party_summary([Character.from_dict(C1), Character.from_dict(C2)])
        assert "Kira" in summary and "Bron" in summary and "Sorcerer" in summary

    def test_build_campaign_context(self):
        context = build_campaign_context(
            [Character.from_dict(C1)], fear=3,
            countdowns=[{"name": "Storm", "current": 2, "max": 5, "type": "campaign"}],
            current_location="The Silver Mines",
            journal_summary="Last session the party entered the mines.",
        )
        assert "Kira" in context and "Fear: 3" in context and "Storm" in context
        assert "Silver Mines" in context and "entered the mines" in context
