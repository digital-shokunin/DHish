# Daggerheart RPG - Comprehensive Mechanics Reference
## For AI Game Master Implementation

---

## 1. CORE MECHANICS: THE DUALITY DICE SYSTEM

### The Roll
Players roll **two d12s** called **Duality Dice** -- one Hope die and one Fear die (must be distinguishable). The two dice are summed together, trait modifiers are added, and the total is compared to a **Difficulty** set by the GM.

### Four Outcomes (determined by total vs. difficulty AND which die is higher)

| Outcome | Condition | Effect |
|---------|-----------|--------|
| **Success with Hope** | Total >= Difficulty AND Hope die > Fear die | Succeed. Player gains 1 Hope. |
| **Success with Fear** | Total >= Difficulty AND Fear die > Hope die | Succeed with a cost/complication. GM gains 1 Fear. |
| **Failure with Hope** | Total < Difficulty AND Hope die > Fear die | Fail with minor consequence. Player gains 1 Hope. Spotlight swings to GM. |
| **Failure with Fear** | Total < Difficulty AND Fear die > Hope die | Fail with major consequence. GM gains 1 Fear. Spotlight swings to GM. |
| **Critical Success** | Both dice show the same number | Automatic success with bonus. Player gains 1 Hope AND clears 1 Stress. |

### Advantage & Disadvantage
- **Advantage**: Roll an additional d6, ADD to total.
- **Disadvantage**: Roll an additional d6, SUBTRACT from total.
- They cancel 1-for-1. Cannot have both simultaneously.

### Difficulty Guidelines by Tier

| Tier | Standard Difficulty |
|------|-------------------|
| Tier 1 (Level 1) | 11 |
| Tier 2 (Levels 2-4) | 14 |
| Tier 3 (Levels 5-7) | 17 |
| Tier 4 (Levels 8-10) | 20 |

GM can adjust difficulty based on circumstance.

---

## 2. HOPE AND FEAR (METACURRENCY)

### Hope (Player Currency)
- **Starting**: 2 Hope per PC
- **Maximum**: 6 Hope per PC
- **Carries over** between sessions
- **Gained**: On any roll where Hope die > Fear die, or on Critical Success

**Ways to Spend Hope:**

| Action | Cost | Effect |
|--------|------|--------|
| Help an Ally | 1 Hope | Describe assistance; ally rolls a d6 advantage die (only highest bonus counts if multiple allies help) |
| Utilize an Experience | 1 Hope per Experience | Add Experience modifier (+2 or more) to a relevant roll |
| Initiate Tag Team Roll | 3 Hope | Two PCs combine actions; both roll, choose one result for both |
| Activate Hope Feature | Varies (often 3) | Use class/subclass features that cost Hope |

### Fear (GM Currency)
- **No starting amount specified** (accumulates during play)
- **Maximum**: 12 Fear
- **Carries over** between sessions
- **Gained**: On any player roll where Fear die > Hope die

**Ways to Spend Fear:**

| Action | Cost | Effect |
|--------|------|--------|
| Place extra action tokens | 1 Fear | Place 2 additional tokens on action tracker for adversary actions |
| Add adversary Experience | 1 Fear | Add adversary's relevant Experience bonus to attack roll or raise Difficulty |
| Activate Fear Feature | 1+ Fear | Use powerful adversary abilities marked as Fear Features |
| End a maintained spell | 1 Fear | Forcibly end a PC's ongoing spell effect |
| Advance a countdown | Varies | Tick a countdown clock forward |
| Narrative hard move | 1+ Fear | Introduce complications, new threats, environmental hazards |

---

## 3. CHARACTER CREATION

### Step-by-Step Process
1. Choose a Class (determines domains, base HP, base Evasion, subclass options)
2. Choose a Subclass (Foundation card)
3. Choose Heritage (Ancestry + Community)
4. Assign Trait Modifiers
5. Select Weapons and Armor
6. Create Background and Experiences
7. Select Domain Cards
8. Establish Connections with other PCs

### The Six Traits
Distribute modifiers: **+2, +1, +1, +0, +0, -1** among:

| Trait | Used For |
|-------|----------|
| **Agility** | Sprint, leap, maneuver, dodge |
| **Strength** | Lift, smash, grapple, physical power |
| **Finesse** | Control, hide, tinker, precision |
| **Instinct** | Perceive, sense, navigate, react |
| **Presence** | Charm, perform, deceive, social influence |
| **Knowledge** | Recall, analyze, comprehend, study |

Trait modifiers are added to action rolls when rolling "with" that trait.

### 9 Classes and Their Domains

| Class | Domains | Subclass 1 | Subclass 2 |
|-------|---------|------------|------------|
| **Bard** | Codex, Grace | Troubadour | Wordsmith |
| **Druid** | Arcana, Sage | Warden of the Elements | Warden of Renewal |
| **Guardian** | Blade, Valor | Stalwart | Vengeance |
| **Ranger** | Bone, Sage | Beastbound | Wayfinder |
| **Rogue** | Grace, Midnight | Nightwalker | Syndicate |
| **Seraph** | Splendor, Valor | Divine Wielder | Winged Sentinel |
| **Sorcerer** | Arcana, Midnight | Elemental Origin | Primal Origin |
| **Warrior** | Blade, Bone | Call of the Brave | Call of the Slayer |
| **Wizard** | Codex, Splendor | School of Knowledge | School of War |

Each subclass grants:
- **Spellcast Trait** (which trait to use for spellcasting)
- **Foundation Feature** (starting subclass ability)
- **Specialization Feature** (gained on level-up)
- **Mastery Feature** (highest-level subclass ability)

### 18 Ancestries
Each provides **two ancestry features** (top and bottom). Mixed ancestry takes one from each of two different ancestries.

| Ancestry | Feature 1 (Top) | Feature 2 (Bottom) |
|----------|----------------|-------------------|
| **Clank** | Purposeful Design: +1 permanent bonus to one Experience aligned with creation purpose | Efficient: Can choose a long rest move instead of short rest move during short rest |
| **Drakona** | Scales: Mark Stress to mark 1 fewer HP on Severe damage | Elemental Breath: d8 magic damage breath weapon (Instinct, Very Close range) |
| **Dwarf** | (sturdy humanoids, features in core book) | (features in core book) |
| **Elf** | (features in core book) | (features in core book) |
| **Faerie** | Luckbender: 1/session, spend 3 Hope to reroll Duality Dice for you or willing ally in Close range | Wings: Fly; mark Stress after adversary attacks to gain +2 Evasion vs that attack |
| **Faun** | Caprine Leap: Leap anywhere within Close range as normal movement | Kick: On melee hit, mark Stress for +2d6 damage and knockback to Very Close |
| **Firbolg** | (features in core book) | (features in core book) |
| **Fungril** | (features in core book) | (features in core book) |
| **Galapa** | (features in core book) | (features in core book) |
| **Giant** | (features in core book) | (features in core book) |
| **Goblin** | (features in core book) | (features in core book) |
| **Halfling** | (features in core book) | (features in core book) |
| **Human** | (features in core book) | (features in core book) |
| **Infernis** | (features in core book) | (features in core book) |
| **Katari** | (features in core book) | (features in core book) |
| **Orc** | (features in core book) | (features in core book) |
| **Ribbet** | (features in core book) | (features in core book) |
| **Simiah** | (features in core book) | (features in core book) |

### 9 Communities
Each grants **one community feature**.

Communities: **Highborne, Loreborne, Orderborne, Ridgeborne, Seaborne, Skyborne, Underborne, Wanderborne, Wildborne**

### Experiences
- Start with **2 Experiences** at +2 modifier each
- Gain new Experiences at levels 2, 5, and 8 (+2 each)
- Can increase existing Experience modifiers by +1 at level-up
- Cannot be too broad or grant mechanical abilities
- To use: spend 1 Hope to add the Experience modifier to a relevant roll
- Categories: Backgrounds (Assassin, Blacksmith, etc.), Characteristics (Charming, Observant), Specialties (Acrobat, Navigator), Skills (Tracker, Negotiator), Phrases

### Starting Stats

| Stat | Starting Value |
|------|---------------|
| Level | 1 |
| Proficiency | 1 |
| Evasion | Class-determined |
| Hit Points | Class-determined (max 12 slots) |
| Stress | 6 slots (max 12 slots) |
| Hope | 2 (max 6) |

---

## 4. THE 9 DOMAINS (Magic/Ability System)

Domains replace traditional spell lists. Each class accesses 2 domains. Domain cards come in three types:

| Card Type | Description |
|-----------|-------------|
| **Abilities** | Typically non-magical actions and features |
| **Spells** | Magical effects requiring Spellcast rolls |
| **Grimoires** | Unique to Codex domain; grant access to collections of less potent spells |

### Domain Descriptions

| Domain | Theme | Description | Classes |
|--------|-------|-------------|---------|
| **Arcana** | Innate/instinctual magic | Raw, volatile elemental magic; manipulating energy and elements | Druid, Sorcerer |
| **Blade** | Weapon mastery | Skill with weapons of all kinds; power through martial prowess | Guardian, Warrior |
| **Bone** | Tactics and the body | Physical ability, body control, predicting opponent behavior | Ranger, Warrior |
| **Codex** | Intensive magical study | Knowledge from books, scrolls, tattoos; commanding versatile magic | Bard, Wizard |
| **Grace** | Charisma | Storytelling, charming spells, perception manipulation, language mastery | Bard, Rogue |
| **Midnight** | Shadows and secrecy | Obscurity, clever tricks, stealth magic, uncovering hidden things | Rogue, Sorcerer |
| **Sage** | The natural world | Earth power, creature magic, vitality and predator ferocity | Druid, Ranger |
| **Splendor** | Life | Healing, controlling death, giving and sustaining life | Seraph, Wizard |
| **Valor** | Protection | Defense and offense for protecting allies; formidable strength | Guardian, Seraph |

### Domain Card Mechanics
- PCs start with **2 domain cards** (level 1) at character creation
- **Loadout**: Maximum **5 active cards** at a time
- Cards beyond 5 go to the **vault** (inactive)
- **Swapping during rest**: Free
- **Swapping outside rest**: Mark Stress equal to card's **Recall Cost**
- **Level-up**: Gain new cards free; swap existing cards for same-level-or-lower alternatives
- Cards have: Level, Domain symbol, Recall Cost, Title, Type (ability/spell/grimoire), Feature text

### Spellcasting Mechanics
- **Spellcast Rolls**: Use the Spellcast Trait (determined by subclass)
- Made only when a feature requires one
- **Spellcast damage**: Roll dice equal to Spellcast trait value (if +0 or lower, roll nothing)
- **Spell maintenance**: Effects last as described; GM can spend Fear to end; can maintain multiple simultaneously
- Spellcast rolls dealing damage also count as attack rolls

---

## 5. COMBAT SYSTEM

### No Initiative -- The Spotlight System
Daggerheart has **no initiative order**. Instead it uses a fluid **spotlight** system:

1. **Players go first** by default at combat start
2. Any player can volunteer to act (no fixed order)
3. When a player rolls **with Fear** or **fails**, the spotlight swings to the GM
4. GM takes adversary actions, then spotlight returns to players
5. Players collaboratively decide who acts next

**Optional: Spotlight Tracker** -- Each player gets ~3 tokens per scene; remove one each time they take the spotlight. Prevents one player from dominating.

### Action Economy
There is no rigid action/bonus action/movement structure like D&D. On their turn in the spotlight, a PC can:
- Describe what they do narratively
- Make action rolls as needed
- Move within **Close range** as part of an action roll (free)
- Move further requires an **Agility Roll**
- Use abilities, spells, or items

### Attack Rolls
- Roll Duality Dice + relevant trait modifier (determined by weapon or spell)
- Compare total to target's **Evasion** (for adversaries, this is their **Difficulty**)
- Same Hope/Fear outcomes as standard action rolls

### Damage Rolls
- Format: **[Proficiency]d[weapon die]+[modifier]**
- Example: Proficiency 2 with a d8+2 weapon = 2d8+2
- **Unarmed**: [Proficiency]d4 damage
- **Critical Damage**: Normal damage + maximum possible dice result (e.g., 2d8+1 becomes 2d8+1+16)
- **Damage Types**: Physical (weapons) or Magic (spells)

### Damage Thresholds (How HP Is Marked)
Armor has two thresholds: **Major** and **Severe** (both increase by character level).

| Damage Result | HP Marked |
|--------------|-----------|
| Below Major threshold | 1 HP |
| At/above Major, below Severe | 2 HP |
| At/above Severe | 3 HP |
| >= 2x Severe (optional rule) | 4 HP (Massive Damage) |
| Damage reduced to 0 or less | 0 HP (no damage) |

### Armor Slots
- Each armor has a **Base Score** (number of armor slots)
- When taking damage, **mark an available Armor Slot** to reduce damage by one threshold level
- Armor slots are restored during rests (Repair Armor downtime move)

### Stress System
- Maximum 12 slots; all PCs start with 6
- Triggers: certain abilities, GM consequences, conversion from sub-threshold damage
- When **all Stress is marked**: character becomes **Vulnerable**
- If must mark Stress but cannot: mark 1 HP instead
- Cleared through downtime moves or specific abilities

### Resistance and Immunity
- **Resistance**: Halve damage of that type before comparing to thresholds
- **Immunity**: Ignore damage of that type completely
- Multiple resistances to same type don't stack
- Dual-damage attacks require resistance/immunity to both types

### Range/Distance (Zone-Based)

| Range | Description | Grid Equivalent |
|-------|-------------|----------------|
| **Melee** | Within arm's reach | 1 square |
| **Very Close** | 5-10 feet | 3 squares |
| **Close** | 10-30 feet | 6 squares |
| **Far** | 30-100 feet | 12 squares |
| **Very Far** | 100-300 feet | 13+ squares |
| **Out of Range** | Beyond reach | -- |

### Conditions

| Condition | Effect |
|-----------|--------|
| **Hidden** | Location unknown; rolls against you have disadvantage. Lost when enemies see you, you attack, or enter line of sight. |
| **Restrained** | Cannot move but can still act from position. |
| **Vulnerable** | All rolls targeting you have advantage. |

Temporary conditions can be cleared by making successful action rolls or at narrative moments.

### Death Mechanics
When a PC marks their **last Hit Point**, they make a **Death Move** (choose one):

1. **Blaze of Glory**: Take one final action (auto-crits with GM approval), then **die permanently**.
2. **Avoid Death**: Fall unconscious. GM describes situation worsening. Can't move/act/be targeted. Regain consciousness when ally clears 1+ HP or after long rest. Roll Hope Die: if value <= character level, gain a **Scar** (permanently cross out a Hope slot with narrative impact). If last Hope slot is crossed out, character **dies**.
3. **Risk It All**: Roll Duality Dice. Hope die higher = stay up, clear HP or Stress equal to Hope die value. Fear die higher = **die**. Matching = stay up, clear nothing.

### Multi-Target and Group Mechanics
- **Multi-target attacks**: One attack roll + one damage roll applied individually to each target
- **Multiple damage sources**: Total all simultaneous damage before comparing to thresholds
- **Group Action Roll**: Leader rolls action, allies roll reaction (no Hope/Fear generated). Leader gets +1 per successful ally, -1 per failed ally.
- **Tag Team Roll** (3 Hope): Two PCs roll separately, choose one result for both. Both roll damage and add totals together.

---

## 6. GM TOOLS AND ADVERSARY SYSTEM

### Adversary Stat Block Structure
- **Name, Tier, Type, Description**
- **Motives & Tactics** (roleplay guidance)
- **Difficulty** (equivalent to PC Evasion -- target number for PC attacks)
- **Damage Thresholds** (Major/Severe)
- **Hit Points**
- **Stress**
- **Attack Modifier** (added to adversary attack rolls)
- **Standard Attack** (default damage)
- **Experience** (optional bonus the GM can activate by spending Fear)
- **Features**: Actions, Reactions, Passives, Fear Features

### Adversary Feature Types

| Type | Activation |
|------|-----------|
| **Action** | GM must spend a spotlight/action token to use |
| **Reaction** | Triggers automatically on specified condition; no token needed |
| **Passive** | Always active; no cost |
| **Fear Feature** | Costs 1+ Fear to activate; high-impact |

### 10 Adversary Types

| Type | Cost (Battle Points) | Description |
|------|---------------------|-------------|
| **Minion** (group) | 1 | Easily dispatched but dangerous in numbers; group equals party size |
| **Social** | 1 | Challenges via conversation, not combat |
| **Support** | 1 | Enhances allies and disrupts opponents |
| **Horde** | 2 | Group of identical creatures acting as single unit |
| **Ranged** | 2 | Fragile up close, high damage at range |
| **Skulk** | 2 | Maneuvers and ambushes |
| **Standard** | 2 | Representative of their group; balanced |
| **Leader** | 3 | Commands and summons other adversaries |
| **Bruiser** | 4 | Tough; delivers powerful attacks |
| **Solo** | 5 | Formidable challenge to entire party |

### Encounter Building (Battle Points Formula)
**Starting Pool**: **(3 x number of PCs) + 2** Battle Points

**Adjustments:**
- -1: easier/shorter fight
- -2: using 2+ Solos
- -2: adding +1d4 or static +2 damage to all adversaries
- +1: using lower-tier adversary
- +1: excluding Bruisers, Hordes, Leaders, or Solos
- +2: harder/longer fight

### Tier Scaling Benchmarks

| Stat | Tier 1 | Tier 2 | Tier 3 | Tier 4 |
|------|--------|--------|--------|--------|
| Attack Modifier | +1 | +2 | +3 | +4 |
| Damage Dice | 1d6+2 to 1d12+4 | 2d6+3 to 2d12+4 | 3d8+3 to 3d12+5 | 4d8+10 to 4d12+15 |
| Difficulty | 11 | 14 | 17 | 20 |
| Major/Severe | 7/12 | 10/20 | 20/32 | 25/45 |

### Adversary Actions (When GM Has Spotlight)
- Move within Close range + standard attack
- Move within Close range + use an adversary Action feature
- Clear a condition
- Sprint within Far/Very Far range
- Other fiction-appropriate actions
- GM can spend Fear to spotlight additional adversaries

### GM Moves
The GM should make moves when:
- A player rolls with Fear
- A player fails an action roll
- An action has consequences
- The GM is given a golden opportunity
- Players look to the GM for what happens next

**Categories of Fear-Spending Moves:**
1. **Environmental trouble**: Weather shifts, structural collapse, fauna disturbance, ward breakages
2. **Resource pressure**: Supply spoilage, tool breakage, unexpected costs, sickness
3. **Social instability**: Reputation damage, authority suspicion, alliance strain, NPC wavering
4. **Pressure on party**: Consequences from past choices, personal fears manifesting, tempting shortcuts
5. **Escalations**: Future doom hints, faction actions, off-screen advancement, lost opportunities
6. **Combat enhancements**: Extra adversary actions, powerful abilities, reinforcements

---

## 7. CAMPAIGN AND ADVENTURE STRUCTURE

### 10 Levels Across 4 Tiers

| Tier | Levels | Adversary Tier |
|------|--------|---------------|
| Tier 1 | Level 1 | Tier 0 |
| Tier 2 | Levels 2-4 | Tier 1 |
| Tier 3 | Levels 5-7 | Tier 2 |
| Tier 4 | Levels 8-10 | Tier 3 |

### Leveling Up
- Party levels at **GM-determined narrative milestones** (typically ~3 sessions)
- All party members level simultaneously

### Level-Up Steps
1. **Tier Achievements** (at levels 2, 5, 8):
   - New Experience (+2)
   - +1 Proficiency
   - Clear marked traits (levels 5, 8)
2. **Choose 2 Advancements** (from current tier or below):
   - Increase two unmarked traits (+1 each)
   - Add 1+ HP slots
   - Add 1+ Stress slots
   - Increase two Experiences (+1 each)
   - Acquire domain card (at/below level; multiclass at half level)
   - Increase Evasion (+1)
   - Take upgraded subclass card (Foundation -> Specialization -> Mastery)
   - Increase Proficiency (costs 2 advancement slots)
   - Multiclass (costs 2 advancement slots; available level 5+)
3. **Damage Thresholds**: All increase by 1
4. **Domain Cards**: Acquire new card at level or below from class domains

### Countdown Mechanics
- **Standard Countdown**: Starts at a number (e.g., "Countdown 4"), ticks down each time a player makes an action roll regardless of result. At 0, effect triggers.
- **Dynamic Countdown**: Ticks based on player roll outcomes/choices rather than automatically.
- **Campaign Countdowns**: Track long-term threats (political tensions, faction schemes, looming wars), tick session-by-session.

### Campaign Frames
The core rulebook includes 6 campaign frames as starter kits providing structure: initial hooks, twists, and turns for campaigns.

### Rest and Downtime

**Short Rest** (~1 hour, 2 downtime moves):
- Tend to Wounds: Clear 1d4+Tier HP
- Clear Stress: Clear 1d4+Tier Stress
- Repair Armor: Clear 1d4+Tier Armor Slots
- Prepare: Gain 1 Hope (solo) or 2 Hope (with party)
- GM gains 1d4 Fear

**Long Rest** (several hours, 2 downtime moves):
- Tend to All Wounds: Clear all HP
- Clear All Stress: Clear all Stress
- Repair All Armor: Clear all Armor Slots
- Prepare: Same as short rest
- Work on a Project: Advance long-term project countdown
- GM gains 1d4 + number of PCs Fear + advance one long-term countdown

Three consecutive short rests force the next rest to be long.

---

## 8. UNIQUE MECHANICS (vs. D&D)

### Key Differentiators

1. **No Initiative**: Fluid spotlight system instead of turn order. Players volunteer to act; spotlight passes to GM on Fear/failure rolls.

2. **Player-Facing Rolls**: Only players roll dice (the GM does not roll to attack). Adversary attacks are resolved by players rolling to defend or the GM simply applying damage on spotlight.

3. **Duality Dice (2d12)**: Every roll generates either Hope or Fear as a metacurrency, creating a dynamic resource economy.

4. **No Rigid Action Economy**: No action/bonus action/reaction structure. Players narrate what they do and roll as needed.

5. **GM Moves via Fear Currency**: The GM is reactive, making moves when prompted by dice results. Fear spending creates narrative complications.

6. **Card-Based Abilities**: Domain cards replace spell slots and class features. Loadout of 5 active cards with a vault for storage.

7. **Damage Thresholds Instead of Flat HP Loss**: Damage is compared to thresholds to determine HP marked (1-4), not subtracted directly.

8. **Stress as Second Resource Track**: Mental/emotional strain separate from HP; feeds into Vulnerable condition.

9. **Zone-Based Range**: Abstract distances (Melee, Very Close, Close, Far, Very Far) instead of exact feet.

10. **Death is a Choice**: Players choose their death move (Blaze of Glory, Avoid Death, Risk It All) rather than making death saves.

11. **Experiences Replace Skills**: Freeform player-created Experiences replace fixed skill lists; cost Hope to activate.

12. **Collaborative Worldbuilding**: Heritage system (Ancestry + Community) encourages player-driven backstory.

13. **Rest Costs Fear**: Every rest gives the GM Fear, creating tension around resource recovery.

---

## 9. EQUIPMENT REFERENCE

### Armor Table (All Tiers)

#### Tier 1 (Level 1)
| Armor | Major/Severe | Base Score | Feature |
|-------|-------------|------------|---------|
| Gambeson | 5/11 | 3 | Flexible: +1 Evasion |
| Leather | 6/13 | 3 | -- |
| Chainmail | 7/15 | 4 | Heavy: -1 Evasion |
| Full Plate | 8/17 | 4 | Very Heavy: -2 Evasion, -1 Agility |

#### Tier 2 (Levels 2-4)
| Armor | Major/Severe | Base Score | Feature |
|-------|-------------|------------|---------|
| Improved Gambeson | 7/16 | 4 | Flexible: +1 Evasion |
| Improved Leather | 9/20 | 4 | -- |
| Improved Chainmail | 11/24 | 5 | Heavy: -1 Evasion |
| Improved Full Plate | 13/28 | 5 | Very Heavy: -2 Evasion, -1 Agility |
| Elundrian Chain | 9/21 | 4 | Warded: reduce magic damage by Armor Score |
| Harrowbone | 9/21 | 4 | Resilient: d6 on last slot, 6 = reduce severity |
| Irontree Breastplate | 9/20 | 4 | Reinforced: +2 thresholds on last slot |
| Runetan Floating | 9/20 | 4 | Shifting: mark slot for attack disadvantage |
| Tyris Soft | 8/18 | 5 | Quiet: +2 stealth |
| Rosewild | 11/23 | 5 | Hopeful: mark Armor Slot instead of spending Hope |

#### Tier 3 (Levels 5-7)
| Armor | Major/Severe | Base Score | Feature |
|-------|-------------|------------|---------|
| Advanced Gambeson | 9/23 | 5 | Flexible: +1 Evasion |
| Advanced Leather | 11/27 | 5 | -- |
| Advanced Chainmail | 13/31 | 6 | Heavy: -1 Evasion |
| Advanced Full Plate | 15/35 | 6 | Very Heavy: -2 Evasion, -1 Agility |
| Bellamie Fine | 11/27 | 5 | Gilded: +1 Presence |
| Dragonscale | 11/27 | 5 | Impenetrable: 1/short rest, Stress instead of last HP |
| Spiked Plate | 10/25 | 5 | Sharp: +d4 melee damage |
| Bladefare | 16/39 | 6 | Physical only (can't reduce magic damage) |
| Monett's Cloak | 16/39 | 6 | Magic only (can't reduce physical damage) |
| Runes of Fortification | 17/43 | 6 | Painful: must mark Stress each Armor Slot use |

#### Tier 4 (Levels 8-10)
| Armor | Major/Severe | Base Score | Feature |
|-------|-------------|------------|---------|
| Legendary Gambeson | 11/32 | 6 | Flexible: +1 Evasion |
| Legendary Leather | 13/36 | 6 | -- |
| Legendary Chainmail | 15/40 | 7 | Heavy: -1 Evasion |
| Legendary Full Plate | 17/44 | 7 | Very Heavy: -2 Evasion, -1 Agility |
| Dunamis Silkchain | 13/36 | 7 | Timeslowing: mark slot, roll d4 add to Evasion |
| Channeling | 13/36 | 5 | Channeling: +1 Spellcast Rolls |
| Emberwoven | 13/36 | 6 | Burning: adversaries mark Stress in Melee |
| Full Fortified | 15/40 | 4 | Fortified: reduce severity by 2 thresholds |
| Veritas Opal | 13/36 | 6 | Truthseeking: glows when creatures lie in Close range |
| Savior Chainmail | 18/48 | 8 | Difficult: -1 to all traits and Evasion |

### Weapon Mechanics
- **Trait**: Determines which trait modifier to use for attack rolls
- **Range**: Maximum attack distance
- **Damage**: Format is die type + modifier (e.g., d8+2)
- **Proficiency**: Determines number of damage dice rolled (not modifier)
- **Burden**: One-handed or two-handed
- Starting characters select from Tier 1 weapons: one two-handed OR one one-handed primary + one one-handed secondary
- Proficiency starts at 1, max 6

### Starting Equipment
- Torch, 50 feet of rope, basic supplies
- One handful of gold
- One Minor Health Potion OR Minor Stamina Potion
- One class-specific item
- Spell-carrying item (if applicable)

---

## 10. CHARACTER SHEET STRUCTURE SUMMARY

A Daggerheart character sheet tracks:

**Identity:**
- Name, Class, Subclass, Level, Tier
- Ancestry, Community
- Background (narrative, no mechanics)

**Core Stats:**
- Six Trait Modifiers (Agility, Strength, Finesse, Instinct, Presence, Knowledge)
- Evasion (base from class + modifiers)
- Proficiency (starts at 1, determines damage dice count)

**Resources (tracked with slot marks):**
- Hit Points (class-determined, max 12 slots)
- Stress (starts at 6 slots, max 12)
- Hope (starts at 2, max 6, with scar slots)
- Armor Slots (from equipped armor's Base Score)

**Damage Thresholds:**
- Major Threshold (armor base + character level)
- Severe Threshold (armor base + character level)

**Equipment:**
- Primary Weapon (trait, range, damage dice, type, burden)
- Secondary Weapon (optional)
- Armor (name, base score, base thresholds, feature)

**Abilities:**
- Domain Card Loadout (max 5 active cards)
- Domain Card Vault (inactive storage)
- Subclass Card (Foundation/Specialization/Mastery)
- Ancestry Features (2)
- Community Feature (1)

**Experiences:**
- 2+ Experiences with modifiers (starting +2 each)

**Connections:**
- Relationships with other PCs

---

## SOURCES

- [Daggerheart SRD - Rules & Mechanics](https://daggerheartsrd.com/rules/)
- [Daggerheart SRD - Character Creation](https://daggerheartsrd.com/rules/character-creation/)
- [Daggerheart SRD - Classes](https://daggerheartsrd.com/rules/classes/)
- [Daggerheart SRD - Domains](https://daggerheartsrd.com/rules/domains/)
- [Daggerheart SRD - Adversaries](https://daggerheartsrd.com/rules/adversaries/)
- [Daggerheart SRD - Armor Tables](https://daggerheartsrd.com/rules/armor-tables/)
- [Daggerheart SRD - Downtime](https://daggerheartsrd.com/rules/downtime/)
- [Daggerheart Official Site](https://www.daggerheart.com/)
- [Daggerheart.org - Overview](https://daggerheart.org/overview)
- [Daggerheart.org - Combat](https://daggerheart.org/core-mechanics/combat)
- [Daggerheart.org - Domains](https://daggerheart.org/reference/domains)
- [Daggerheart.org - Adversaries](https://daggerheart.org/reference/adversaries)
- [Daggerheart Wiki - Duality Dice](https://daggerheart.fandom.com/wiki/Duality_Dice)
- [EN World - How Hope and Fear Work](https://www.enworld.org/threads/how-hope-and-fear-work-in-critical-roles-daggerheart.703341/)
- [The Gamer - How Duality Dice Work](https://www.thegamer.com/daggerheart-duality-dice-critical-role-ttrpg-explained-guide/)
- [The Gamer - How Combat Works](https://www.thegamer.com/daggerheart-combat-critical-role-ttrpg-guide/)
- [Patchwork Paladin - Fear Moves](https://patchworkpaladin.com/2025/11/03/daggerheart-fear-moves/)
- [Goonhammer - Player Review](https://www.goonhammer.com/turn-order-a-players-review-of-daggerheart/)
- [ComicBook - Action Tracker Changes](https://comicbook.com/gaming/news/daggerheart-testing-action-tracker-removal-in-post-beta-development/)
- [TechRaptor - Character Creation Guide](https://techraptor.net/tabletop/guides/daggerheart-rpg-character-creation-guide)
- [Escapist - Ancestries Explained](https://www.escapistmagazine.com/daggerhearts-races-ancestries-explained/)
- [Daggerheart Official SRD PDF](https://www.daggerheart.com/wp-content/uploads/2025/05/DH-SRD-May202025.pdf)
