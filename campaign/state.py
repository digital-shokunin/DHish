"""Campaign state management for Daggerheart Campaign Tool."""
import json
import logging
from pathlib import Path

logger = logging.getLogger(__name__)
MAX_FEAR = 12
CAMPAIGN_SUBDIRS = ["party", "npcs", "adversaries", "encounters", "world", "journal", "sessions"]

class CampaignState:
    def __init__(self, name: str, campaign_dir: Path):
        self.name = name
        self.campaign_dir = campaign_dir
        self._fear = 0
        self.consecutive_short_rests = 0
        self.countdowns: list[dict] = []
        self.current_location = ""
        self.notes = ""

    @property
    def fear(self) -> int:
        return self._fear

    @fear.setter
    def fear(self, value: int):
        self._fear = max(0, min(value, MAX_FEAR))

    def save(self) -> None:
        data = {
            "name": self.name, "fear": self.fear,
            "consecutive_short_rests": self.consecutive_short_rests,
            "countdowns": self.countdowns,
            "current_location": self.current_location,
            "notes": self.notes,
        }
        path = self.campaign_dir / "campaign.json"
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

    @classmethod
    def from_dict(cls, data: dict, campaign_dir: Path) -> "CampaignState":
        state = cls(data["name"], campaign_dir)
        state.fear = data.get("fear", 0)
        state.consecutive_short_rests = data.get("consecutive_short_rests", 0)
        state.countdowns = data.get("countdowns", [])
        state.current_location = data.get("current_location", "")
        state.notes = data.get("notes", "")
        return state

def create_campaign(name: str, campaigns_base: Path) -> CampaignState:
    campaign_dir = campaigns_base / name
    for subdir in CAMPAIGN_SUBDIRS:
        (campaign_dir / subdir).mkdir(parents=True, exist_ok=True)
    state = CampaignState(name, campaign_dir)
    state.save()
    return state

def load_campaign(name: str, campaigns_base: Path) -> CampaignState:
    campaign_dir = campaigns_base / name
    path = campaign_dir / "campaign.json"
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    return CampaignState.from_dict(data, campaign_dir)
