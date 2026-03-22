# Damage, Armor, and Stress

## Damage Thresholds

Armor defines two thresholds: **Major** and **Severe** (both increase by character level).

| Damage Result | HP Marked |
|--------------|-----------|
| Below Major threshold | 1 HP (Minor) |
| >= Major, < Severe | 2 HP (Major) |
| >= Severe | 3 HP (Severe) |
| >= 2x Severe (optional) | 4 HP (Massive) |
| Damage reduced to 0 or less | 0 HP |

**Important**: Damage is NOT subtracted from HP. It is compared to thresholds to determine how many HP slots to mark.

### Threshold Scaling
Thresholds = armor base value + character level. As characters level, thresholds increase by 1 per level.

## Armor Slot Mechanics

- Each armor has a **Base Score** (number of armor slots)
- When taking damage, **mark 1 available Armor Slot** to reduce damage severity by one threshold level (e.g., Severe becomes Major, Major becomes Minor)
- Only 1 Armor Slot per hit (unless a feature says otherwise)
- Armor Slots restored during rests (Repair Armor downtime move)

### Armor Restoration
- **Short rest**: Repair Armor move clears 1d4+Tier slots
- **Long rest**: Repair All Armor clears all slots

## Stress System

| Property | Value |
|----------|-------|
| Starting slots | 6 |
| Maximum slots | 12 |
| Triggers | Abilities, GM consequences, certain ancestry/class features |

- When **all Stress is marked**: character becomes **Vulnerable** (all rolls targeting you have advantage)
- If must mark Stress but cannot: **mark 1 HP instead**
- Cleared through downtime moves or specific abilities

### Stress Clearing
- **Short rest**: Clear Stress move = 1d4+Tier Stress
- **Long rest**: Clear All Stress

## Resistance and Immunity

- **Resistance**: Halve damage of that type before comparing to thresholds
- **Immunity**: Ignore damage of that type completely
- Multiple resistances to same type do NOT stack
- Dual-damage attacks require resistance/immunity to BOTH types to benefit
