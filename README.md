# ⚔️ The Selection — A Python Combat RPG

> **"Humanity was never promised a perfect future. It was only given the chance to have one."**

**The Selection** is a story-driven, turn-based combat RPG written in **Python**.

Set in the year **2072**, humanity receives an unknown message from deep space. An alien civilization gives humanity one final opportunity to prove that it deserves to exist: fight a series of replicated humans, each designed to test a different aspect of humanity.

You are selected as humanity's defender.

Choose your combat style, survive five chapters, defeat the Alien Commander, and discover what the Selection was really about.

---

## 🎮 Features

- Turn-based terminal combat
- Story-driven campaign with **5 chapters**
- Three playable classes
- Unique abilities and combat statistics for each class
- Critical-hit system
- Healing and ability cooldowns
- Temporary shields
- Enemy AI with different combat behaviors
- Phase-based final boss
- Boss prediction mechanic
- Temporary combat locks
- One-time revival mechanic during the final battle
- Multiple endings
- **Secret ending** unlocked by completing the game with all three playable classes
- Typewriter-style story presentation with timed dialogue

---

## 📖 Story

### YEAR 2072

Humanity receives a mysterious signal from deep space.

The message is simple:

**Prove that your species deserves to exist.**

The aliens offer humanity a final test.

Fight their creations — replicated versions of humans designed to test different aspects of the species.

Billions of people watch.

One person is selected.

**You.**

The Selection begins.

What initially appears to be an alien invasion gradually becomes something much more complicated. The enemies are not simply monsters. Each one represents a different aspect of humanity, and every battle reveals another piece of the mystery.

By the time you reach the final battle, the real question is no longer:

> **"Can humanity survive?"**

It is:

> **"Why was humanity chosen?"**

---

# ⚔️ Playable Classes

You can choose between three playable classes at the beginning of the game.

| Class | HP | Damage | Crit Chance | Heal | Ability CD |
|---|---:|---:|---:|---:|---:|
| 🥊 Warrior | 100 | 10–20 | 5% | 20 | 4 |
| 🛡️ Tank | 125 | 10–15 | 3% | 25 | 5 |
| 🗡️ Assassin | 90 | 15–25 | 10% | 15 | 5 |

### 🥊 Warrior — Power Strike

Temporarily increases the Warrior's damage by 15 for one attack.

The ability is focused on dealing a powerful burst of damage.

### 🛡️ Tank — Fortify

Creates a shield that blocks the next **3 enemy attacks**.

The Tank sacrifices offensive power for survivability and defensive control.

### 🗡️ Assassin — Desperate Strike

Can only be used when the Assassin has **less than 10 HP**.

The lower the Assassin's HP, the more powerful the attack becomes.

This makes the ability a high-risk, high-reward mechanic.

---

# 👽 The Enemies

Each chapter introduces a different replicated human.

### Chapter 1 — The Warrior

**Theme:** Strength

The first replicated human tests humanity's physical strength.

### Chapter 2 — The Tank

**Theme:** Endurance

The second subject represents humanity's ability to endure and refuse to surrender.

### Chapter 3 — The Assassin

**Theme:** Instinct

The Assassin represents caution, adaptation, and the instinct to survive when hope disappears.

### Chapter 4 — The Adapter

**Theme:** Adaptation

The Adapter is designed to take what the player has and make it its own.

Its ability deals damage while restoring its own HP.

### Chapter 5 — The Alien Commander

**Theme:** Choice

The final opponent is not another replica.

The Alien Commander personally enters the Selection to conduct the final evaluation.

---

# 👑 Alien Commander

The Alien Commander is the final boss and has **two phases**.

## Phase 1

- HP: 400
- Damage: 10–20
- Critical Chance: 5%
- Heal: 15
- Ability Cooldown: 6

### Mothership Support

The Commander has three special support charges:

**⚡ Orbital Laser**
- Deals 25–40 damage.

**🛡️ Shield Barrier**
- Blocks the next 3 attacks.

**🤖 Repair Drone**
- Restores up to 30 HP.

---

## Phase 2

When the Commander's HP reaches **200 or below**, Phase 2 begins.

Its stats change to:

- Damage: 15–30
- Critical Chance: 10%

The Commander gains two dangerous abilities.

### 🔒 System Overwrite

Randomly locks one of the player's:

- Attack
- Heal
- Ability

The selected action remains locked for 2 rounds.

### 👁️ Predictive Vision

The Commander predicts the player's next action.

If the prediction is correct:

- The player's move is prevented.
- The player takes 30 damage.

This makes the final battle more strategic than simply attacking every turn.

---

# 🎯 Combat System

During the player's turn, four actions are available:

```text
1) ⚔️ Attack
2) ❤️ Heal
3) 🔥 Ability
4) ⏭️ Skip
```

### Attack

Deals random damage based on the character's damage range.

There is also a chance to land a critical hit, which deals double damage.

### Heal

Restores HP up to the character's maximum HP.

### Ability

Every class has its own unique ability.

Abilities have cooldowns, so timing is important.

### Skip

Allows the player to intentionally skip a turn.

This also gives the player another legal action when other moves are temporarily unavailable.

---

# 💀 Revival Mechanic

During the Alien Commander fight, the player can survive defeat **once**.

After reaching 0 HP for the first time against the Commander:

- HP is restored to approximately 50%
- Ability cooldown is reset
- Damage is increased by 5
- The battle continues

This creates a final comeback moment instead of immediately ending the campaign.

---

# 📚 Campaign Structure

The game contains five chapters:

```text
Chapter 1 — The Warrior
       ↓
Chapter 2 — The Will to Survive
       ↓
Chapter 3 — The Shadow Within
       ↓
Chapter 4 — The Hunger Within
       ↓
Chapter 5 — The Last Judgment
       ↓
Alien Commander
       ↓
The End
```

Each chapter contains both combat and story sequences.

The story is displayed through a typewriter-style text system, with configurable text speed and delays between scenes.

---

# 🔓 Secret Ending

The game has a hidden ending.

To unlock it, you must complete the game with all three playable classes:

- Warrior
- Tank
- Assassin

After all three victories are recorded, the **Secret Ending** becomes available.

The secret ending reveals additional information about the alien message, the replicated humans, the Alien Commander, and the true purpose behind the Selection.

It reveals that the apparent invasion was not what humanity believed it was.

---

# 🧠 Technical Overview

The project was built using core Python concepts including:

- Classes and objects
- Inheritance
- Methods
- Encapsulation of character state
- `isinstance()` for class-specific behavior
- Random number generation
- Conditional logic
- Loops
- Functions
- Exception handling
- Timed terminal output
- State management
- Cooldown systems
- AI decision-making
- Phase-based boss logic

The main character system is built around a base `Character` class.

Playable classes and enemies inherit from this structure and implement their own abilities and behaviors.

---

# 🏗️ Class Structure

Conceptually, the character system is organized like this:

```text
Character
│
├── Warrior
├── Tank
├── Assassin
├── Adapter
└── Alien_Commander
```

The base `Character` class manages common properties such as:

- HP
- Maximum HP
- Damage range
- Critical chance
- Healing
- Ability cooldown
- Shields
- Combat locks
- Prediction state
- Revival state

Specialized classes then define their unique abilities and behavior.

---

# 💻 Requirements

The project is written in Python and is designed to run in a terminal.

Recommended:

- **Python 3.10+**
- Windows / Linux / macOS
- No external libraries are required for the core game.

The project uses Python's standard library, including:

```python
random
time
```

---

# ▶️ How to Run

Clone the repository:

```bash
git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY.git
```

Enter the project directory:

```bash
cd YOUR-REPOSITORY
```

Run the game:

```bash
python main.py
```

If your Python installation uses the Windows Python launcher:

```bash
py main.py
```

---

# 🕹️ Controls

The game is controlled through terminal input.

When prompted, enter the number corresponding to your desired action.

Example:

```text
Select Your Action:

1) ⚔️ Attack
2) ❤️ Heal
3) 🔥 Ability
4) ⏭️ Skip
-->
```

Enter:

```text
1
```

to attack.

---

# 🎯 Goal

Your objective is simple:

**Survive the Selection.**

But if you want to uncover everything the game has to offer:

1. Complete the campaign.
2. Defeat the Alien Commander.
3. Complete the game as the Warrior.
4. Complete the game as the Tank.
5. Complete the game as the Assassin.
6. Unlock the Secret Ending.

---

# 🌌 Themes

The game explores several ideas through its combat system and story:

- Strength
- Endurance
- Instinct
- Adaptation
- Survival
- Humanity
- Choice
- The consequences of scientific discovery

The central idea of the final chapter is that humanity's defining characteristic is not simply strength or intelligence.

It is the ability to **choose what it becomes**.

---

# 🚧 Project Status

**Playable**

The core combat system, campaign, classes, boss mechanics, story progression, multiple endings, and secret ending are implemented.

Future improvements could include:

- Graphical interface
- Sound effects and music
- Save/load system
- More playable classes
- More enemy types
- Difficulty modes
- Better AI
- Improved code organization
- Dedicated game engine version

---

# 👨‍💻 Author

Created as a Python programming project focused on learning and applying:

**Object-Oriented Programming + Game Logic + AI-style Decision Making + Storytelling**

---

# ⭐ If You Like The Project

Feel free to star the repository, explore the code, and experiment with the combat system.

**The Selection has begun.**

**Can humanity survive?**
