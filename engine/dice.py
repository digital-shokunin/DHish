"""Dice roller for Daggerheart RPG."""
import random
import re
from dataclasses import dataclass

_rng = random.SystemRandom()
_NOTATION_RE = re.compile(r"^(\d+)d(\d+)([+-]\d+)?$", re.IGNORECASE)

@dataclass
class RollResult:
    notation: str
    dice: list[int]
    modifier: int
    total: int

@dataclass
class DualityOutcome:
    outcome_type: str
    hope_gained: bool
    fear_gained: bool
    stress_cleared: bool

@dataclass
class DualityResult:
    hope_die: int
    fear_die: int
    raw_total: int
    modified_total: int
    difficulty: int
    outcome_type: str
    hope_gained: bool
    fear_gained: bool
    stress_cleared: bool

def roll(notation: str) -> RollResult:
    match = _NOTATION_RE.match(notation.strip())
    if not match:
        raise ValueError(f"Invalid dice notation: {notation!r}")
    count = int(match.group(1))
    sides = int(match.group(2))
    mod_str = match.group(3)
    modifier = int(mod_str) if mod_str else 0
    dice = [_rng.randint(1, sides) for _ in range(count)]
    total = sum(dice) + modifier
    return RollResult(notation=notation.strip(), dice=dice, modifier=modifier, total=total)

def _resolve_duality(hope_die, fear_die, modified_total, difficulty):
    if hope_die == fear_die:
        return DualityOutcome("critical", True, False, True)
    success = modified_total >= difficulty
    hope_higher = hope_die > fear_die
    if success and hope_higher:
        return DualityOutcome("success_hope", True, False, False)
    elif success and not hope_higher:
        return DualityOutcome("success_fear", False, True, False)
    elif not success and hope_higher:
        return DualityOutcome("failure_hope", True, False, False)
    else:
        return DualityOutcome("failure_fear", False, True, False)

def roll_duality(modifier=0, difficulty=11):
    hope_die = _rng.randint(1, 12)
    fear_die = _rng.randint(1, 12)
    raw_total = hope_die + fear_die
    modified_total = raw_total + modifier
    outcome = _resolve_duality(hope_die, fear_die, modified_total, difficulty)
    return DualityResult(hope_die, fear_die, raw_total, modified_total, difficulty,
        outcome.outcome_type, outcome.hope_gained, outcome.fear_gained, outcome.stress_cleared)

def roll_with_advantage(notation: str) -> RollResult:
    result = roll(notation)
    bonus = _rng.randint(1, 6)
    return RollResult(f"{notation}+adv", result.dice + [bonus], result.modifier, result.total + bonus)

def roll_with_disadvantage(notation: str) -> RollResult:
    result = roll(notation)
    penalty = _rng.randint(1, 6)
    return RollResult(f"{notation}-dis", result.dice + [penalty], result.modifier, result.total - penalty)

def roll_damage(proficiency, die, modifier=0):
    dice = [_rng.randint(1, die) for _ in range(proficiency)]
    return sum(dice) + modifier
