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
| **Dwarf** | Thick Skin: On minor damage, may mark 2 Stress instead of marking a Hit Point | Increased Fortitude: Spend 3 Hope to halve incoming physical damage |
| **Elf** | Quick Reactions: Mark a Stress to gain advantage on a reaction roll | Celestial Trance: Rest via trance; choose an additional downtime move during rest |
| **Faerie** | Luckbender: 1/session, spend 3 Hope to reroll Duality Dice for you or willing ally in Close range | Wings: Fly; mark Stress after adversary attacks to gain +2 Evasion vs that attack |
| **Faun** | Caprine Leap: Leap anywhere within Close range as normal movement | Kick: On melee hit, mark Stress for +2d6 damage and knockback to Very Close |
| **Firbolg** | Charge: On successful Agility roll to advance from Far/Very Far to Melee, mark Stress to deal 1d12 physical damage to all targets in Melee range | Unshakable: When marking Stress, roll d6; on a 6, negate that Stress |
| **Fungril** | Fungril Network: Instinct Roll (12) to communicate with other Fungril across any distance via mycelial array | Death Connection: Touch a recently deceased corpse, spend Stress to retrieve a single memory (choose emotion/sensation) |
| **Galapa** | Shell: Gain bonus to damage thresholds equal to your Proficiency | Retract: Spend Stress to withdraw into shell; gain resistance to physical damage but disadvantage on action rolls and cannot move |
| **Giant** | Endurance: Gain one additional Hit Point slot at character creation | Reach: Melee range weapons/abilities are treated as Very Close range instead |
| **Goblin** | Surefooted: Ignore disadvantage on Agility Rolls | Danger Sense: 1/rest, mark Stress to force adversary to reroll attack against you or ally within Very Close range |
| **Halfling** | Luckbringer: At start of each session, everyone in your party gains a Hope | Internal Compass: When you roll a 1 on your Hope Die, you can reroll it |
| **Human** | High Stamina: Gain one additional Stress slot at character creation | Adaptability: When you fail a roll using one of your Experiences, mark Stress to attempt the roll again |
| **Infernis** | Fearless: On Fear-based rolls, spend 2 Stress to convert roll into a Hope-based roll | Dread Visage: Advantage on intimidation rolls targeting hostile creatures |
| **Katari** | Feline Instincts: On an Agility Roll, spend 2 Hope to reroll your Hope Die | Retracting Claws: Agility Roll to scratch target in Melee range; on success, target becomes temporarily Vulnerable |
| **Orc** | Sturdy: When you have 1 Hit Point remaining, attacks against you have disadvantage | Tusks: On successful melee attack, spend Hope to gore with tusks for extra 1d6 damage |
| **Ribbet** | Amphibious: Breathe and move naturally underwater | Long Tongue: Grab things within Close range; mark Stress to use tongue as Finesse Close weapon dealing d12 physical damage |
| **Simiah** | Natural Climber: Advantage on Agility Rolls involving balancing and climbing | Nimble: Permanent +1 bonus to Evasion at character creation |

### 9 Communities
Each grants **one community feature**.

| Community | Feature Name | Feature Description |
|-----------|-------------|---------------------|
| **Highborne** | Privilege | Advantage on rolls to consort with nobles, negotiate prices, or leverage reputation |
| **Loreborne** | Well-Read | Advantage on rolls involving history, culture, or politics of prominent persons/locations |
| **Orderborne** | Dedicated | Record 3 sayings/values; 1/rest, when embodying one, roll d20 as Hope Die |
| **Ridgeborne** | Steady | Advantage on rolls for traversing cliffs/ledges, navigating harsh environments, survival knowledge |
| **Seaborne** | Know the Tide | Place token on card when rolling with Fear (max = level). Spend tokens before action rolls for +1 per token. Clear all at session end |
| **Slyborne** | Scoundrel | Advantage on rolls to negotiate with criminals, detect lies, or find a safe hiding place |
| **Underborne** | Low-Light Living | Advantage on rolls to hide, investigate, or perceive in low light or heavy shadow |
| **Wanderborne** | Nomadic Pack | Gain Nomadic Pack item; 1/session spend Hope to retrieve a mundane item that suits current situation |
| **Wildborne** | Lightfoot | Movement is naturally silent; advantage on rolls to move without being heard |

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
| Evasion | Class-determined (see below) |
| Hit Points | Class-determined (see below, max 12 slots) |
| Stress | 6 slots (max 12 slots) |
| Hope | 2 (max 6) |

### Class Starting Stats, Equipment, and Features

| Class | HP | Evasion | Domains | Suggested Primary | Suggested Armor | Class Item |
|-------|-----|---------|---------|-------------------|-----------------|------------|
| **Bard** | 5 | 10 | Codex, Grace | Rapier + Small Dagger (secondary) | Gambeson | Romance novel or unopened letter |
| **Druid** | 6 | 10 | Sage, Arcana | Shortstaff + Round Shield (secondary) | Leather | Small bag of rocks/bones or strange pendant |
| **Guardian** | 7 | 9 | Blade, Valor | Battleaxe | Chainmail | Totem from mentor or secret key |
| **Ranger** | 6 | 12 | Bone, Sage | Shortbow | Leather | Trophy from first kill or broken compass |
| **Rogue** | 6 | 12 | Grace, Midnight | Dagger + Small Dagger (secondary) | Gambeson | Forgery tools or grappling hook |
| **Seraph** | 7 | 9 | Splendor, Valor | Hallowed Axe + Round Shield (secondary) | Chainmail | Bundle of offerings or god's sigil |
| **Sorcerer** | 6 | 10 | Arcana, Midnight | Dualstaff | Gambeson | Whispering orb or family heirloom |
| **Warrior** | 6 | 11 | Blade, Bone | Longsword | Chainmail | Drawing of a lover or sharpening stone |
| **Wizard** | 5 | 11 | Codex, Splendor | Greatstaff | Leather | Book being translated or tiny elemental pet |

### Class Features

| Class | Class Feature | Hope Feature (3 Hope) |
|-------|--------------|----------------------|
| **Bard** | Rally: 1/session, give self and allies a Rally Die (d6 at L1, d8 at L5) to boost action/reaction/damage rolls or clear Stress | Make a Scene: Temporarily Distract target within Close range, -2 to their Difficulty |
| **Druid** | Beastform: Transform into creatures of your tier or below by marking Stress. Gain creature's Evasion bonus, use specified trait. Wildtouch: Perform harmless nature effects at will | Evolution: Transform without marking Stress; raise one trait by +1 during that Beastform |
| **Guardian** | Unstoppable: 1/long rest, become Unstoppable. Gain Unstoppable Die (d4, d6 at L5) that increases after dealing damage. Reduce physical damage severity by one threshold, add die value to damage, can't be Restrained/Vulnerable | Frontline Tank: Clear 2 Armor Slots |
| **Ranger** | Ranger's Focus: Spend Hope + attack; on success, target becomes your Focus (precise awareness, target marks Stress on damage, reroll Duality Dice on failed attacks) | Hold Them Off: On weapon attack success, use same roll against two additional adversaries within range |
| **Rogue** | Cloaked: When Hidden, become Cloaked instead (enhanced stealth). Sneak Attack: Bonus damage when cloaked or with adjacent ally (1d6 L1, 2d6 L2-4, 3d6 L5-7, 4d6 L8-10) | Rogue's Dodge: +2 to Evasion until next attack succeeds against you or rest |
| **Seraph** | Prayer Dice: Roll d4s equal to Spellcast trait at session start. Use to reduce incoming damage, boost rolls post-roll, or generate Hope. Unspent clear at session end | Life Support: Clear a Hit Point on an ally within Close range |
| **Sorcerer** | Arcane Sense: Sense magical people/objects within Close range. Minor Illusion: Spellcast Roll (10) for visual illusion. Channel Raw Power: 1/long rest, vault a domain card to gain Hope equal to card level or boost spell damage by 2x card level | Volatile Magic: Reroll any number of damage dice on magic damage attacks |
| **Warrior** | Attack of Opportunity: When enemy in Melee tries to leave, reaction roll; on success choose: prevent movement, deal weapon damage, or move with them. Combat Training: Weapons don't count toward burden; physical damage rolls gain bonus equal to level | No Mercy: +1 to attack rolls until next rest |
| **Wizard** | Prestidigitation: Harmless magical effects at will (change colors, light candles, levitate small items, etc.). Strange Patterns: Choose number 1-12; when rolling it on Duality Die, gain Hope or clear Stress (can change after long rest) | Not This Time: Force adversary within Far range to reroll attack or damage roll |

### Suggested Trait Arrays by Class

| Class | Agility | Strength | Finesse | Instinct | Presence | Knowledge |
|-------|---------|----------|---------|----------|----------|-----------|
| **Bard** | 0 | -1 | +1 | 0 | +2 | +1 |
| **Druid** | +1 | 0 | +1 | +2 | -1 | 0 |
| **Guardian** | +1 | +2 | -1 | 0 | +1 | 0 |
| **Ranger** | +2 | 0 | +1 | +1 | -1 | 0 |
| **Rogue** | +1 | -1 | +2 | 0 | +1 | 0 |
| **Seraph** | 0 | +2 | 0 | +1 | +1 | -1 |
| **Sorcerer** | 0 | -1 | +1 | +2 | +1 | 0 |
| **Warrior** | +2 | +1 | 0 | +1 | -1 | 0 |
| **Wizard** | -1 | 0 | 0 | +1 | +1 | +2 |

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

### Domain Card Lists (All Levels)

#### Arcana (Druid, Sorcerer) -- Innate/Instinctual Magic

| Level | Cards |
|-------|-------|
| 1 | Rune Ward, Unleash Chaos, Wall Walk |
| 2 | Cinder Grasp, Floating Eye |
| 3 | Counterspell, Flight |
| 4 | Blink Out, Preservation Blast |
| 5 | Chain Lightning, Premonition |
| 6 | Rift Walker, Telekinesis |
| 7 | Arcana-Touched, Cloaking Blast |
| 8 | Arcane Reflection, Confusing Aura |
| 9 | Earthquake, Sensory Projection |
| 10 | Adjust Reality, Falling Sky |

#### Blade (Guardian, Warrior) -- Weapon Mastery

| Level | Cards |
|-------|-------|
| 1 | Get Back Up, Not Good Enough, Whirlwind |
| 2 | A Soldier's Bond, Reckless |
| 3 | Scramble, Versatile Fighter |
| 4 | Deadly Focus, Fortified Armor |
| 5 | Champion's Edge, Vitality |
| 6 | Battle-Hardened, Rage Up |
| 7 | Blade-Touched, Glancing Blow |
| 8 | Battle Cry, Frenzy |
| 9 | Gore and Glory, Reaper's Strike |
| 10 | Battle Monster, Onslaught |

#### Bone (Ranger, Warrior) -- Tactics and the Body

| Level | Cards |
|-------|-------|
| 1 | Deft Maneuvers, I See It Coming, Untouchable |
| 2 | Ferocity, Strategic Approach |
| 3 | Brace, Tactician |
| 4 | Boost, Redirect |
| 5 | Know Thy Enemy, Signature Move |
| 6 | Rapid Riposte, Recovery |
| 7 | Bone-Touched, Cruel Precision |
| 8 | Breaking Blow, Wrangle |
| 9 | On the Brink, Splintering Strike |
| 10 | Deathrun, Swift Step |

#### Codex (Bard, Wizard) -- Intensive Magical Study

| Level | Cards |
|-------|-------|
| 1 | Book of Ava, Book of Illiat, Book of Tyfar |
| 2 | Book of Sitil, Book of Vagras |
| 3 | Book of Korvax, Book of Norai |
| 4 | Book of Exota, Book of Grynn |
| 5 | Manifest Wall, Teleport |
| 6 | Banish, Sigil of Retribution |
| 7 | Book of Homet, Codex-Touched |
| 8 | Book of Vyola, Safe Haven |
| 9 | Book of Ronin, Disintegration Wave |
| 10 | Book of Yarrow, Transcendent Union |

#### Grace (Bard, Rogue) -- Charisma

| Level | Cards |
|-------|-------|
| 1 | Deft Deceiver, Enrapture, Inspirational Words |
| 2 | Tell No Lies, Troublemaker |
| 3 | Hypnotic Shimmer, Invisibility |
| 4 | Soothing Speech, Through Your Eyes |
| 5 | Thought Delver, Words of Discord |
| 6 | Never Upstaged, Share the Burden |
| 7 | Endless Charisma, Grace-Touched |
| 8 | Astral Projection, Mass Enrapture |
| 9 | Copycat, Master of the Craft |
| 10 | Encore, Notorious |

#### Midnight (Rogue, Sorcerer) -- Shadows and Secrecy

| Level | Cards |
|-------|-------|
| 1 | Pick and Pull, Rain of Blades, Uncanny Disguise |
| 2 | Midnight Spirit, Shadowbind |
| 3 | Chokehold, Veil of Night |
| 4 | Stealth Expertise, Glyph of Nightfall |
| 5 | Hush, Phantom Retreat |
| 6 | Dark Whispers, Mass Disguise |
| 7 | Midnight-Touched, Vanishing Dodge |
| 8 | Shadowhunter, Spellcharge |
| 9 | Night Terror, Twilight Toll |
| 10 | Eclipse, Specter of the Dark |

#### Sage (Druid, Ranger) -- The Natural World

| Level | Cards |
|-------|-------|
| 1 | Gifted Tracker, Nature's Tongue, Vicious Entangle |
| 2 | Conjure Swarm, Natural Familiar |
| 3 | Corrosive Projectile, Towering Stalk |
| 4 | Death Grip, Healing Field |
| 5 | Thorn Skin, Wild Fortress |
| 6 | Conjured Steeds, Forager |
| 7 | Sage-Touched, Wild Surge |
| 8 | Forest Sprites, Rejuvenation Barrier |
| 9 | Fane of the Wilds, Plant Dominion |
| 10 | Force of Nature, Tempest |

#### Splendor (Seraph, Wizard) -- Life and Healing

| Level | Cards |
|-------|-------|
| 1 | Bolt Beacon, Mending Touch, Reassurance |
| 2 | Final Words, Healing Hands |
| 3 | Second Wind, Voice of Reason |
| 4 | Divination, Life Ward |
| 5 | Shape Material, Smite |
| 6 | Restoration, Zone of Protection |
| 7 | Healing Strike, Splendor-Touched |
| 8 | Shield Aura, Stunning Sunlight |
| 9 | Overwhelming Aura, Salvation Beam |
| 10 | Invigoration, Resurrection |

#### Valor (Guardian, Seraph) -- Protection

| Level | Cards |
|-------|-------|
| 1 | Bare Bones, Forceful Push, I Am Your Shield |
| 2 | Body Basher, Bold Presence |
| 3 | Critical Inspiration, Lean on Me |
| 4 | Goad Them On, Support Tank |
| 5 | Armorer, Rousing Strike |
| 6 | Inevitable, Rise Up |
| 7 | Shrug It Off, Valor-Touched |
| 8 | Full Surge, Ground Pound |
| 9 | Hold the Line, Lead by Example |
| 10 | Unbreakable, Unyielding Armor |

### Level 1 Domain Card Descriptions

#### Arcana Level 1
- **Rune Ward** (Spell, Recall 0): Infuse a personal trinket with protective magic. Holder spends Hope to reduce incoming damage by 1d8. If die shows 8, ward exhausts until next rest.
- **Unleash Chaos** (Spell, Recall 1): Place tokens = Spellcast trait at session start. Spellcast Roll vs target in Far range; spend tokens to roll that many d10s as magic damage. Mark Stress to replenish tokens. Unspent clear at session end.
- **Wall Walk** (Spell, Recall 1): Spend Hope to allow touched creature to climb walls/ceilings as easily as walking. Lasts until scene ends or recast.

#### Blade Level 1
- **Get Back Up** (Ability, Recall 1): When taking Severe damage, mark Stress to reduce severity by one threshold.
- **Not Good Enough** (Ability, Recall 1): When rolling damage dice, reroll any 1s or 2s.
- **Whirlwind** (Ability, Recall 0): On successful hit at Very Close range, spend Hope to extend attack to all other adversaries within Very Close range. Additional targets take half damage.

#### Bone Level 1
- **Deft Maneuvers** (Ability, Recall 0): 1/rest, mark Stress to sprint within Far range without Agility Roll. If ending in Melee range and attacking immediately, +1 to attack roll.
- **I See It Coming** (Ability, Recall 1): When targeted by ranged attack, spend Stress and roll d4 to add result as Evasion bonus for that attack.
- **Untouchable** (Ability, Recall 1): Gain bonus to Evasion equal to half your Agility.

#### Codex Level 1 (Grimoires -- each contains 3 spells)
- **Book of Ava** (Grimoire, Recall 2): Power Push (Spellcast Roll, push target to distance, d10+2 magic damage), Tava's Armor (spend Hope, +1 Armor Score to ally until rest), Ice Spike (d6 physical damage at range).
- **Book of Illiat** (Grimoire, Recall 2): Slumber (Spellcast Roll, target falls unconscious until damaged or GM spends Fear), Arcane Barrage (1/rest, spend any Hope to roll that many d6 as damage), Telepathy (spend Hope for mental communication until rest).
- **Book of Tyfar** (Grimoire, Recall 2): Wild Flame (Spellcast Roll vs up to 3 nearby adversaries, 2d6 magic damage, targets mark Stress), Magic Hand (conjure hand at Far range), Mysterious Mist (Spellcast Roll 13, create thick fog in Very Close area).

#### Grace Level 1
- **Deft Deceiver** (Ability, Recall 0): Spend Hope to gain advantage on a roll to deceive or trick someone.
- **Enrapture** (Spell, Recall 0): Spellcast Roll vs nearby target; on success, target becomes Enraptured (focused entirely on you). 1/rest, mark Stress to force enraptured target to also mark Stress.
- **Inspirational Words** (Ability, Recall 1): Place tokens = Presence after long rest. During conversation with allies, spend tokens: clear 1 Stress, recover 1 HP, or gain 1 Hope per token. Clear unspent at long rest.

#### Midnight Level 1
- **Pick and Pull** (Ability, Recall 0): Advantage on rolls to pick nonmagical locks, disarm nonmagical traps, or take items from targets.
- **Rain of Blades** (Spell, Recall 1): Spend Hope, Spellcast Roll to summon blades targeting all in Very Close range. d8+2 magic damage. Vulnerable targets take extra 1d8.
- **Uncanny Disguise** (Spell, Recall 0): Mark Stress to disguise as any humanoid you picture clearly. Advantage on Presence Rolls to avoid detection. Place tokens = Spellcast trait; each action spends one token; disguise drops when last token spent.

#### Sage Level 1
- **Gifted Tracker** (Ability, Recall 0): When tracking creatures, spend any Hope to ask that many questions about them (direction, timing, activities, count). Gain +1 Evasion against tracked creatures when encountered.
- **Nature's Tongue** (Ability, Recall 0): Instinct Roll (12) to converse with flora/fauna. In natural settings, spend Hope for +2 to Spellcast Rolls.
- **Vicious Entangle** (Spell, Recall 1): Spellcast Roll vs target in Far range; 1d8+1 physical damage, temporarily restrain with roots/vines. Spend Hope to restrain a second adversary within Very Close of initial target.

#### Splendor Level 1
- **Bolt Beacon** (Spell, Recall 1): Spellcast Roll vs target in Far range; spend Hope to deal d8+2 magic damage. Target becomes temporarily Vulnerable and glows until condition cleared.
- **Mending Touch** (Spell, Recall 1): Spend a few minutes with target; spend 2 Hope to clear a Hit Point or Stress. 1/long rest, if you share something personal or learn something meaningful, clear 2 HP or 2 Stress instead.
- **Reassurance** (Ability, Recall 0): 1/rest, after ally attempts action roll but before results, offer support to let them reroll.

#### Valor Level 1
- **Bare Bones** (Ability, Recall 0): When not wearing armor, Armor Score = 3 + Strength. Modified thresholds: T1 9/19, T2 11/24, T3 13/31, T4 15/38.
- **Forceful Push** (Ability, Recall 0): Attack with primary weapon in Melee; on success, deal damage and push target to Close range. Spend Hope to add d6 to damage and make target Vulnerable.
- **I Am Your Shield** (Ability, Recall 1): Mark Stress to redirect attack from ally within Very Close to yourself. May mark any quantity of Armor Slots for the redirected damage.

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

### Weapon Features Reference

| Feature | Effect |
|---------|--------|
| **Barrier** | +N Armor Score; -1 Evasion |
| **Bouncing** | Mark Stress to hit multiple targets |
| **Brave** | -1 Evasion; +3 to Severe damage threshold |
| **Brutal** | Max roll on damage die triggers an additional die |
| **Burning** | On d6 roll, target marks Stress |
| **Concussive** | Spend Hope to knock target back to Far range |
| **Cumbersome** | -1 to Finesse |
| **Deadly** | Target marks extra HP on Severe damage |
| **Destructive** | -1 Agility; nearby targets mark Stress |
| **Double Duty** | +1 Armor, +1 primary weapon damage (Melee) |
| **Doubled Up** | Deal damage to a second Melee target |
| **Eruptive** | Others within Very Close range make reaction roll |
| **Grappling** | Spend Hope to Restrain or pull target |
| **Heavy** | -1 to Evasion |
| **Hooked** | Pull target to Melee range on success |
| **Invigorating** | Roll d4; on 4, clear Stress |
| **Lifestealing** | Roll d6; on 6, clear HP or Stress |
| **Locked On** | Next primary attack auto-succeeds |
| **Massive** | -1 Evasion; Powerful feature |
| **Paired** | +N to primary weapon damage (Melee) |
| **Painful** | Mark Stress on each successful attack |
| **Persuasive** | Mark Stress for +2 to Presence Roll |
| **Powerful** | Roll additional damage die, discard lowest |
| **Protective** | +N to Armor Score |
| **Quick** | Mark Stress to target another creature |
| **Reliable** | +1 to attack rolls |
| **Reloading** | Roll d6; on 1, mark Stress |
| **Retractable** | Blade hidden in hilt for stealth |
| **Returning** | Weapon reappears in hand after throw |
| **Scary** | Target marks Stress on hit |
| **Self-Correcting** | d1 roll deals 6 damage |
| **Serrated** | d1 roll deals 8 damage |
| **Sharpening** | Bonus to damage rolls equals Agility |
| **Startling** | Mark Stress to push adversaries back |
| **Timebending** | Choose attack target after roll |
| **Versatile** | Alternate trait/range/damage mode available |
| **Very Heavy** | -2 Evasion, -1 Agility |

### Primary Weapon Tables

#### Tier 1 Primary Weapons

| Name | Trait | Range | Damage | Burden | Type | Feature |
|------|-------|-------|--------|--------|------|---------|
| Arcane Gauntlets | Strength | Melee | d10+3 | Two-Handed | Magic | -- |
| Battleaxe | Strength | Melee | d10+3 | Two-Handed | Physical | -- |
| Broadsword | Agility | Melee | d8 | One-Handed | Physical | Reliable: +1 attack |
| Crossbow | Finesse | Far | d6+1 | One-Handed | Physical | -- |
| Cutlass | Presence | Melee | d8+1 | One-Handed | Physical | -- |
| Dagger | Finesse | Melee | d8+1 | One-Handed | Physical | -- |
| Dualstaff | Instinct | Far | d6+3 | Two-Handed | Magic | -- |
| Glowing Rings | Agility | Very Close | d10+2 | Two-Handed | Magic | -- |
| Greatstaff | Knowledge | Very Far | d6 | Two-Handed | Magic | Powerful |
| Greatsword | Strength | Melee | d10+3 | Two-Handed | Physical | Massive: -1 Evasion; Powerful |
| Halberd | Strength | Very Close | d10+2 | Two-Handed | Physical | Cumbersome: -1 Finesse |
| Hallowed Axe | Strength | Melee | d8+1 | One-Handed | Magic | -- |
| Hand Runes | Instinct | Very Close | d10 | One-Handed | Magic | -- |
| Longbow | Agility | Very Far | d8+3 | Two-Handed | Physical | Cumbersome: -1 Finesse |
| Longsword | Agility | Melee | d10+3 | Two-Handed | Physical | -- |
| Mace | Strength | Melee | d8+1 | One-Handed | Physical | -- |
| Quarterstaff | Instinct | Melee | d10+3 | Two-Handed | Physical | -- |
| Rapier | Presence | Melee | d8 | One-Handed | Physical | Quick: Mark Stress to target another |
| Returning Blade | Finesse | Close | d8 | One-Handed | Magic | Returning |
| Scepter | Presence | Far | d6 | Two-Handed | Magic | Versatile: Presence, Melee, d8 |
| Shortbow | Agility | Far | d6+3 | Two-Handed | Physical | -- |
| Shortstaff | Instinct | Close | d8+1 | One-Handed | Magic | -- |
| Spear | Finesse | Very Close | d8+3 | Two-Handed | Physical | -- |
| Wand | Knowledge | Far | d6+1 | One-Handed | Magic | -- |
| Warhammer | Strength | Melee | d12+3 | Two-Handed | Physical | Heavy: -1 Evasion |

#### Tier 2 Primary Weapons

| Name | Trait | Range | Damage | Burden | Type | Feature |
|------|-------|-------|--------|--------|------|---------|
| Bladed Whip | Agility | Very Close | d8+3 | One-Handed | Physical | Quick |
| Blunderbuss | Finesse | Close | d8+6 | Two-Handed | Physical | Reloading |
| Casting Sword | Strength | Melee | d10+4 | Two-Handed | Magic | Versatile: Knowledge, Far, d6+3 |
| Devouring Dagger | Finesse | Melee | d8+4 | One-Handed | Magic | Scary |
| Elder Bow | Instinct | Far | d6+4 | Two-Handed | Magic | Powerful |
| Finehair Bow | Agility | Very Far | d6+5 | Two-Handed | Physical | Reliable |
| Gilded Falchion | Strength | Melee | d10+4 | One-Handed | Physical | Powerful |
| Greatbow | Strength | Far | d6+6 | Two-Handed | Physical | Powerful |
| Hammer of Exota | Instinct | Melee | d8+6 | Two-Handed | Magic | Eruptive |
| Improved Arcane Gauntlets | Strength | Melee | d10+6 | Two-Handed | Magic | -- |
| Improved Battleaxe | Strength | Melee | d10+6 | Two-Handed | Physical | -- |
| Improved Broadsword | Agility | Melee | d8+3 | One-Handed | Physical | Reliable |
| Improved Crossbow | Finesse | Far | d6+4 | One-Handed | Physical | -- |
| Improved Cutlass | Presence | Melee | d8+4 | One-Handed | Physical | -- |
| Improved Dagger | Finesse | Melee | d8+4 | One-Handed | Physical | -- |
| Improved Dualstaff | Instinct | Far | d6+6 | Two-Handed | Magic | -- |
| Improved Glowing Rings | Agility | Very Close | d10+5 | Two-Handed | Magic | -- |
| Improved Greatstaff | Knowledge | Very Far | d6+3 | Two-Handed | Magic | Powerful |
| Improved Greatsword | Strength | Melee | d10+6 | Two-Handed | Physical | Massive |
| Improved Halberd | Strength | Very Close | d10+5 | Two-Handed | Physical | Cumbersome |
| Improved Hallowed Axe | Strength | Melee | d8+4 | One-Handed | Magic | -- |
| Improved Hand Runes | Instinct | Very Close | d10+3 | One-Handed | Magic | -- |
| Improved Longbow | Agility | Very Far | d8+6 | Two-Handed | Physical | Cumbersome |
| Improved Longsword | Agility | Melee | d10+6 | Two-Handed | Physical | -- |
| Improved Mace | Strength | Melee | d8+4 | One-Handed | Physical | -- |
| Improved Quarterstaff | Instinct | Melee | d10+6 | Two-Handed | Physical | -- |
| Improved Rapier | Presence | Melee | d8+3 | One-Handed | Physical | Quick |
| Improved Returning Blade | Finesse | Close | d8+3 | One-Handed | Magic | Returning |
| Improved Scepter | Presence | Far | d6+3 | Two-Handed | Magic | Versatile: Presence, Melee, d8+3 |
| Improved Shortbow | Agility | Far | d6+6 | Two-Handed | Physical | -- |
| Improved Shortstaff | Instinct | Close | d8+4 | One-Handed | Magic | -- |
| Improved Spear | Finesse | Very Close | d8+6 | Two-Handed | Physical | -- |
| Improved Wand | Knowledge | Far | d6+4 | One-Handed | Magic | -- |
| Improved Warhammer | Strength | Melee | d12+6 | Two-Handed | Physical | Heavy |
| Keeper's Staff | Knowledge | Far | d6+4 | Two-Handed | Magic | Reliable |
| Knuckle Blades | Strength | Melee | d10+6 | One-Handed | Physical | Brutal |
| Scepter of Elias | Presence | Far | d6+3 | One-Handed | Magic | Invigorating |
| Urok Broadsword | Finesse | Melee | d8+3 | One-Handed | Physical | Deadly |
| Wand of Enthrallment | Presence | Far | d6+4 | One-Handed | Magic | Persuasive |
| War Scythe | Finesse | Very Close | d8+5 | Two-Handed | Physical | Reliable |
| Yutari Bloodbow | Finesse | Far | d6+4 | Two-Handed | Magic | Brutal |

#### Tier 3 Primary Weapons

| Name | Trait | Range | Damage | Burden | Type | Feature |
|------|-------|-------|--------|--------|------|---------|
| Advanced Arcane Gauntlets | Strength | Melee | d10+9 | Two-Handed | Magic | -- |
| Advanced Battleaxe | Strength | Melee | d10+9 | Two-Handed | Physical | -- |
| Advanced Broadsword | Agility | Melee | d8+6 | One-Handed | Physical | Reliable |
| Advanced Crossbow | Finesse | Far | d6+7 | One-Handed | Physical | -- |
| Advanced Cutlass | Presence | Melee | d8+7 | One-Handed | Physical | -- |
| Advanced Dagger | Finesse | Melee | d8+7 | One-Handed | Physical | -- |
| Advanced Dualstaff | Instinct | Far | d6+9 | Two-Handed | Magic | -- |
| Advanced Glowing Rings | Agility | Very Close | d10+8 | Two-Handed | Magic | -- |
| Advanced Greatstaff | Knowledge | Very Far | d6+6 | Two-Handed | Magic | Powerful |
| Advanced Greatsword | Strength | Melee | d10+9 | Two-Handed | Physical | Massive |
| Advanced Halberd | Strength | Very Close | d10+8 | Two-Handed | Physical | Cumbersome |
| Advanced Hallowed Axe | Strength | Melee | d8+7 | One-Handed | Magic | -- |
| Advanced Hand Runes | Instinct | Very Close | d10+6 | One-Handed | Magic | -- |
| Advanced Longbow | Agility | Very Far | d8+9 | Two-Handed | Physical | Cumbersome |
| Advanced Longsword | Agility | Melee | d10+9 | Two-Handed | Physical | -- |
| Advanced Mace | Strength | Melee | d8+7 | One-Handed | Physical | -- |
| Advanced Quarterstaff | Instinct | Melee | d10+9 | Two-Handed | Physical | -- |
| Advanced Rapier | Presence | Melee | d8+6 | One-Handed | Physical | Quick |
| Advanced Returning Blade | Finesse | Close | d8+6 | One-Handed | Magic | Returning |
| Advanced Scepter | Presence | Far | d6+6 | Two-Handed | Magic | Versatile |
| Advanced Shortbow | Agility | Far | d6+9 | Two-Handed | Physical | -- |
| Advanced Shortstaff | Instinct | Close | d8+7 | One-Handed | Magic | -- |
| Advanced Spear | Finesse | Very Close | d8+9 | Two-Handed | Physical | -- |
| Advanced Wand | Knowledge | Far | d6+7 | One-Handed | Magic | -- |
| Advanced Warhammer | Strength | Melee | d12+9 | Two-Handed | Physical | Heavy |
| Axe of Fortunis | Strength | Melee | d10+8 | Two-Handed | Magic | Lucky: Mark Stress to reroll failed attack |
| Black Powder Revolver | Finesse | Far | d6+8 | One-Handed | Physical | Reloading |
| Bravesword | Strength | Melee | d12+7 | Two-Handed | Physical | Brave: -1 Evasion; +3 Severe threshold |
| Double Flail | Agility | Very Close | d10+8 | Two-Handed | Physical | Powerful |
| Firestaff | Instinct | Far | d6+7 | Two-Handed | Magic | Burning |
| Flickerfly Blade | Agility | Melee | d8+5 | One-Handed | Physical | Sharpening: damage bonus = Agility |
| Ghostblade | Presence | Melee | d10+7 | One-Handed | Phys/Magic | Otherworldly: choose damage type |
| Gilded Bow | Finesse | Far | d6+7 | Two-Handed | Magic | Self-Correcting |
| Hammer of Wrath | Strength | Melee | d10+7 | Two-Handed | Physical | Devastating: Mark Stress for d20 damage die |
| Ilmari's Rifle | Finesse | Very Far | d6+6 | One-Handed | Magic | Reloading |
| Labrys Axe | Strength | Melee | d10+7 | Two-Handed | Physical | Protective: +1 Armor Score |
| Mage Orb | Knowledge | Far | d6+7 | One-Handed | Magic | Powerful |
| Meridian Cutlass | Presence | Melee | d10+5 | One-Handed | Physical | Dueling: Advantage when target is alone |
| Retractable Saber | Presence | Melee | d10+7 | One-Handed | Physical | Retractable |
| Runes of Ruination | Knowledge | Very Close | d20+4 | One-Handed | Magic | Painful |
| Spiked Bow | Agility | Very Far | d6+7 | Two-Handed | Physical | Versatile: Agility, Melee, d10+5 |
| Talon Blades | Finesse | Close | d10+7 | Two-Handed | Physical | Brutal |
| Widgast Pendant | Knowledge | Close | d10+5 | One-Handed | Magic | Timebending |

#### Tier 4 Primary Weapons

| Name | Trait | Range | Damage | Burden | Type | Feature |
|------|-------|-------|--------|--------|------|---------|
| Aantari Bow | Finesse | Far | d6+11 | Two-Handed | Physical | Reliable |
| Bloodstaff | Instinct | Far | d20+7 | Two-Handed | Magic | Painful |
| Curved Dagger | Finesse | Melee | d8+9 | One-Handed | Physical | Serrated |
| Dual-Ended Sword | Agility | Melee | d10+9 | Two-Handed | Physical | Quick |
| Extended Polearm | Finesse | Very Close | d8+10 | Two-Handed | Physical | Long: attack all adversaries in line |
| Floating Bladeshards | Instinct | Close | d8+9 | One-Handed | Magic | Powerful |
| Fusion Gloves | Knowledge | Very Far | d6+9 | Two-Handed | Magic | Bonded: damage bonus = level |
| Hand Cannon | Finesse | Very Far | d6+12 | One-Handed | Physical | Reloading |
| Impact Gauntlet | Strength | Melee | d10+11 | One-Handed | Physical | Concussive |
| Knuckle Claws | Strength | Melee | d6+8 | One-Handed | Physical | Doubled Up |
| Legendary Arcane Gauntlets | Strength | Melee | d10+12 | Two-Handed | Magic | -- |
| Legendary Battleaxe | Strength | Melee | d10+12 | Two-Handed | Physical | -- |
| Legendary Broadsword | Agility | Melee | d8+9 | One-Handed | Physical | Reliable |
| Legendary Crossbow | Finesse | Far | d6+10 | One-Handed | Physical | -- |
| Legendary Cutlass | Presence | Melee | d8+10 | One-Handed | Physical | -- |
| Legendary Dagger | Finesse | Melee | d8+10 | One-Handed | Physical | -- |
| Legendary Dualstaff | Instinct | Far | d8+12 | Two-Handed | Magic | -- |
| Legendary Glowing Rings | Agility | Very Close | d10+11 | One-Handed | Magic | -- |
| Legendary Greatstaff | Knowledge | Very Far | d6+9 | Two-Handed | Magic | Powerful |
| Legendary Greatsword | Strength | Melee | d10+12 | Two-Handed | Physical | Massive |
| Legendary Halberd | Strength | Very Close | d10+11 | Two-Handed | Physical | Cumbersome |
| Legendary Hallowed Axe | Strength | Melee | d8+10 | One-Handed | Magic | -- |
| Legendary Hand Runes | Instinct | Very Close | d10+9 | One-Handed | Magic | -- |
| Legendary Longbow | Agility | Very Far | d8+12 | Two-Handed | Physical | Cumbersome |
| Legendary Longsword | Agility | Melee | d10+12 | Two-Handed | Physical | -- |
| Legendary Mace | Strength | Melee | d8+10 | One-Handed | Physical | -- |
| Legendary Quarterstaff | Instinct | Melee | d10+12 | Two-Handed | Physical | -- |
| Legendary Rapier | Presence | Melee | d8+9 | One-Handed | Physical | Quick |
| Legendary Returning Blade | Finesse | Close | d8+9 | One-Handed | Magic | Returning |
| Legendary Scepter | Presence | Far | d6+9 | Two-Handed | Magic | Versatile |
| Legendary Shortbow | Agility | Far | d6+12 | Two-Handed | Physical | -- |
| Legendary Shortstaff | Instinct | Close | d8+10 | One-Handed | Magic | -- |
| Legendary Spear | Finesse | Very Close | d8+12 | Two-Handed | Physical | -- |
| Legendary Wand | Knowledge | Far | d6+10 | One-Handed | Magic | -- |
| Legendary Warhammer | Strength | Melee | d12+12 | Two-Handed | Physical | Heavy |
| Magus Revolver | Finesse | Very Far | d6+13 | One-Handed | Magic | Reloading |
| Midas Scythe | Knowledge | Melee | d10+9 | Two-Handed | Magic | Greedy: spend gold for +1 Proficiency on damage |
| Ricochet Axes | Agility | Far | d6+11 | Two-Handed | Physical | Bouncing |
| Siphoning Gauntlets | Presence | Melee | d10+9 | Two-Handed | Magic | Lifestealing |
| Sledge Axe | Strength | Melee | d12+13 | Two-Handed | Physical | Destructive |
| Sword of Light and Flame | Strength | Melee | d10+11 | Two-Handed | Magic | Hot: cuts through solid material |
| Swinging Ropeblade | Presence | Close | d8+9 | One-Handed | Physical | Grappling |
| Thistlebow | Instinct | Far | d6+13 | Two-Handed | Magic | Reliable |
| Wand of Essek | Knowledge | Far | d8+13 | One-Handed | Magic | Timebending |

### Secondary Weapon Tables

#### Tier 1 Secondary Weapons

| Name | Trait | Range | Damage | Type | Feature |
|------|-------|-------|--------|------|---------|
| Grappler | Finesse | Close | d6 | Physical | Hooked: pull target to Melee on success |
| Hand Crossbow | Finesse | Far | d6+1 | Physical | -- |
| Round Shield | Strength | Melee | d4 | Physical | Protective: +1 Armor Score |
| Shortsword | Agility | Melee | d8 | Physical | Paired: +2 primary weapon damage (Melee) |
| Small Dagger | Finesse | Melee | d8 | Physical | Paired: +2 primary weapon damage (Melee) |
| Tower Shield | Strength | Melee | d6 | Physical | Barrier: +2 Armor Score; -1 Evasion |
| Whip | Presence | Very Close | d6 | Physical | Startling: Mark Stress to push adversaries back |

#### Tier 2 Secondary Weapons

| Name | Trait | Range | Damage | Type | Feature |
|------|-------|-------|--------|------|---------|
| Improved Grappler | Finesse | Close | d6+2 | Physical | Hooked |
| Improved Hand Crossbow | Finesse | Far | d6+3 | Physical | -- |
| Improved Round Shield | Strength | Melee | d4+2 | Physical | Protective: +2 Armor Score |
| Improved Shortsword | Agility | Melee | d8+2 | Physical | Paired: +3 primary damage (Melee) |
| Improved Small Dagger | Finesse | Melee | d8+2 | Physical | Paired: +3 primary damage (Melee) |
| Improved Tower Shield | Strength | Melee | d6+2 | Physical | Barrier: +3 Armor Score; -1 Evasion |
| Improved Whip | Presence | Very Close | d6+2 | Physical | Startling |
| Parrying Dagger | Finesse | Melee | d6+2 | Physical | Parry: discard matching damage dice from attacks |
| Returning Axe | Agility | Close | d6+4 | Physical | Returning |
| Spiked Shield | Strength | Melee | d6+2 | Physical | Double Duty: +1 Armor, +1 primary damage (Melee) |

#### Tier 3 Secondary Weapons

| Name | Trait | Range | Damage | Type | Feature |
|------|-------|-------|--------|------|---------|
| Advanced Grappler | Finesse | Close | d6+4 | Physical | Hooked |
| Advanced Hand Crossbow | Finesse | Far | d6+5 | Physical | -- |
| Advanced Round Shield | Strength | Melee | d4+4 | Physical | Protective: +3 Armor Score |
| Advanced Shortsword | Agility | Melee | d8+4 | Physical | Paired: +4 primary damage (Melee) |
| Advanced Small Dagger | Finesse | Melee | d8+4 | Physical | Paired: +4 primary damage (Melee) |
| Advanced Tower Shield | Strength | Melee | d6+4 | Physical | Barrier: +4 Armor Score; -1 Evasion |
| Advanced Whip | Presence | Very Close | d6+4 | Physical | Startling |
| Buckler | Agility | Melee | d4+4 | Physical | Deflecting: mark Armor Slot for Evasion bonus |
| Hand Sling | Finesse | Very Close | d6+4 | Physical | Versatile: also Finesse, Close, d8+4 |
| Powered Gauntlet | Knowledge | Close | d6+4 | Physical | Charged: mark Stress for +1 Proficiency |

#### Tier 4 Secondary Weapons

| Name | Trait | Range | Damage | Type | Feature |
|------|-------|-------|--------|------|---------|
| Braveshield | Agility | Melee | d4+6 | Physical | Sheltering: armor reduction applies to allies |
| Knuckle Claws | Strength | Melee | d6+8 | Physical | Doubled Up: deal damage to second Melee target |
| Legendary Grappler | Finesse | Close | d6+6 | Physical | Hooked |
| Legendary Hand Crossbow | Finesse | Far | d6+7 | Physical | -- |
| Legendary Round Shield | Strength | Melee | d4+6 | Physical | Protective: +4 Armor Score |
| Legendary Shortsword | Agility | Melee | d8+6 | Physical | Paired: +5 primary damage (Melee) |
| Legendary Small Dagger | Finesse | Melee | d8+6 | Physical | Paired: +5 primary damage (Melee) |
| Legendary Tower Shield | Strength | Melee | d6+6 | Physical | Barrier: +5 Armor Score; -1 Evasion |
| Legendary Whip | Presence | Very Close | d6+6 | Physical | Startling |
| Primer Shard | Instinct | Very Close | d4 | Physical | Locked On: next primary attack auto-succeeds |

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
- [Daggerheart SRD - Primary Weapons](https://daggerheartsrd.com/primary-weapons/)
- [Daggerheart SRD - Secondary Weapons](https://daggerheartsrd.com/secondary-weapons/)
- [Daggerheart SRD - Downtime](https://daggerheartsrd.com/rules/downtime/)
- [Daggerheart Official Site](https://www.daggerheart.com/)
- [Daggerheart.org - Overview](https://daggerheart.org/overview)
- [Daggerheart.org - Combat](https://daggerheart.org/core-mechanics/combat)
- [Daggerheart.org - Domains](https://daggerheart.org/reference/domains)
- [Daggerheart.org - All Domain Cards](https://daggerheart.org/reference/all-domain-cards)
- [Daggerheart.org - Adversaries](https://daggerheart.org/reference/adversaries)
- [GitHub - seansbox/daggerheart-srd](https://github.com/seansbox/daggerheart-srd) (MD/CSV/JSON format SRD)
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
- [Daggerheart SRD PDF (Sept 2025)](https://www.daggerheart.com/wp-content/uploads/2025/09/Daggerheart-SRD-9-09-25.pdf)
