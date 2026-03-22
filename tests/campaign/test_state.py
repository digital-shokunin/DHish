import tempfile
from pathlib import Path
from campaign.state import CampaignState, create_campaign, load_campaign

class TestCampaignState:
    def test_create_campaign(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            base = Path(tmpdir) / "campaigns"
            state = create_campaign("test-quest", base)
            assert state.name == "test-quest"
            assert state.fear == 0
            assert (base / "test-quest" / "party").is_dir()
            assert (base / "test-quest" / "encounters").is_dir()
            assert (base / "test-quest" / "campaign.json").is_file()

    def test_save_and_load_roundtrip(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            base = Path(tmpdir) / "campaigns"
            state = create_campaign("roundtrip", base)
            state.fear = 5
            state.consecutive_short_rests = 2
            state.countdowns = [{"name": "Dragon Attack", "current": 3, "max": 6, "type": "campaign"}]
            state.save()
            loaded = load_campaign("roundtrip", base)
            assert loaded.fear == 5
            assert loaded.consecutive_short_rests == 2
            assert len(loaded.countdowns) == 1

    def test_fear_clamped_to_max(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            base = Path(tmpdir) / "campaigns"
            state = create_campaign("fear-test", base)
            state.fear = 15
            assert state.fear == 12

    def test_campaign_path(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            base = Path(tmpdir) / "campaigns"
            state = create_campaign("my-campaign", base)
            assert state.campaign_dir == base / "my-campaign"
