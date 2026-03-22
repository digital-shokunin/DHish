import re
from engine.dice import (
    roll, roll_duality, roll_damage, roll_with_advantage,
    roll_with_disadvantage, RollResult, DualityResult, _resolve_duality,
)

class TestRoll:
    def test_roll_single_die(self):
        result = roll("1d6")
        assert isinstance(result, RollResult)
        assert 1 <= result.total <= 6
        assert len(result.dice) == 1

    def test_roll_multiple_dice(self):
        result = roll("3d8")
        assert 3 <= result.total <= 24
        assert len(result.dice) == 3

    def test_roll_with_positive_modifier(self):
        result = roll("1d6+3")
        assert 4 <= result.total <= 9
        assert result.modifier == 3

    def test_roll_with_negative_modifier(self):
        result = roll("2d6-1")
        assert 1 <= result.total <= 11
        assert result.modifier == -1

    def test_roll_no_modifier(self):
        result = roll("2d12")
        assert result.modifier == 0

    def test_roll_invalid_notation(self):
        try:
            roll("bad")
            assert False, "Should have raised ValueError"
        except ValueError:
            pass

class TestRollDuality:
    def test_returns_duality_result(self):
        result = roll_duality(modifier=2, difficulty=12)
        assert isinstance(result, DualityResult)

    def test_hope_and_fear_dice_in_range(self):
        result = roll_duality(modifier=0, difficulty=11)
        assert 1 <= result.hope_die <= 12
        assert 1 <= result.fear_die <= 12

    def test_modified_total(self):
        result = roll_duality(modifier=2, difficulty=11)
        assert result.modified_total == result.hope_die + result.fear_die + 2

    def test_critical_on_matching_dice(self):
        outcome = _resolve_duality(5, 5, 12, 11)
        assert outcome.outcome_type == "critical"
        assert outcome.hope_gained is True
        assert outcome.stress_cleared is True

    def test_success_with_hope(self):
        outcome = _resolve_duality(8, 5, 15, 11)
        assert outcome.outcome_type == "success_hope"
        assert outcome.hope_gained is True
        assert outcome.fear_gained is False

    def test_success_with_fear(self):
        outcome = _resolve_duality(4, 9, 15, 11)
        assert outcome.outcome_type == "success_fear"
        assert outcome.fear_gained is True

    def test_failure_with_hope(self):
        outcome = _resolve_duality(7, 2, 10, 11)
        assert outcome.outcome_type == "failure_hope"
        assert outcome.hope_gained is True

    def test_failure_with_fear(self):
        outcome = _resolve_duality(3, 6, 10, 11)
        assert outcome.outcome_type == "failure_fear"
        assert outcome.fear_gained is True

class TestRollAdvantage:
    def test_advantage_adds_d6(self):
        result = roll_with_advantage("2d12")
        assert 3 <= result.total <= 30
        assert len(result.dice) == 3

    def test_disadvantage_subtracts_d6(self):
        result = roll_with_disadvantage("2d12")
        assert -4 <= result.total <= 23
        assert len(result.dice) == 3

class TestRollDamage:
    def test_basic_damage(self):
        total = roll_damage(proficiency=2, die=8, modifier=2)
        assert 4 <= total <= 18

    def test_proficiency_1(self):
        total = roll_damage(proficiency=1, die=6, modifier=0)
        assert 1 <= total <= 6
