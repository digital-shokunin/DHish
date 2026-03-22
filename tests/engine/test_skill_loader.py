from pathlib import Path
from engine.skill_loader import load_skills, build_system_prompt, estimate_tokens

SKILLS_DIR = Path(__file__).resolve().parent.parent.parent / "skills"

class TestLoadSkills:
    def test_load_core_tier(self):
        text = load_skills(SKILLS_DIR, "core")
        assert "Player Agency" in text
        assert "Duality Dice" in text

    def test_skill_md_comes_first(self):
        text = load_skills(SKILLS_DIR, "core")
        skill_pos = text.find("Player Agency")
        core_pos = text.find("Duality Dice")
        assert skill_pos < core_pos

    def test_missing_file_skipped_with_warning(self):
        text = load_skills(SKILLS_DIR, "full")
        assert "Player Agency" in text

    def test_invalid_tier_raises(self):
        try:
            load_skills(SKILLS_DIR, "invalid_tier")
            assert False, "Should have raised ValueError"
        except ValueError:
            pass

class TestBuildSystemPrompt:
    def test_includes_preamble(self):
        prompt = build_system_prompt("test skills text")
        assert "Daggerheart RPG Game Master" in prompt
        assert "test skills text" in prompt

    def test_includes_separator(self):
        prompt = build_system_prompt("rules here")
        assert "DAGGERHEART GAME MASTER SKILL" in prompt

class TestEstimateTokens:
    def test_short_string(self):
        assert estimate_tokens("hello world") > 0

    def test_empty_string(self):
        assert estimate_tokens("") == 0

    def test_rough_accuracy(self):
        tokens = estimate_tokens("hello world")
        assert 1 <= tokens <= 5
