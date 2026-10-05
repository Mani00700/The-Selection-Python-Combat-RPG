warrior_win = False
tank_win = False
assassin_win = False

# ⚔️ BATTLE GAME — CHARACTERS
# 🥊 Warrior
# HP: 100 | DMG: 10–20 | Crit: 5% | Heal: 20 | CD: 4
# Ability — Power Strike: The Warrior performs a powerful attack with damage temporarily increased to 25–35 for that attack.

# 🛡️ Tank
# HP: 125 | DMG: 10–15 | Crit: 3% | Heal: 25 | CD: 5
# Ability — Fortify: Creates a shield that completely blocks the next 3 enemy attacks.

# 🗡️ Assassin
# HP: 90 | DMG: 15–25 | Crit: 10% | Heal: 15 | CD: 5
# Ability — Desperate Strike: Can only be used below 10 HP. The closer the Assassin is to defeat, the more damage the attack deals.

# 🧬 Adapter
# HP: 150 | DMG: 12–22 | Crit: 8% | Heal: 15 | CD: 5
# Ability — Adaptation: Deals 20 damage to the opponent while restoring 20 HP.

# 👽 Alien Commander
# HP: 400 | DMG: 10–20 → 15–30 | Crit: 5% → 10% | Heal: 15 | CD: 6
# Phase 1
# Orbital Laser: Deals 25–40 damage.
# Shield Barrier: Blocks the next 3 attacks.
# Repair Drone: Restores 30 HP.
# Phase 2
# System Overwrite: Randomly locks Attack, Heal, or Ability for 2 rounds.
# Predictive Vision: Predicts the player's next action. If correct, the move is cancelled and the player takes 30 damage.


while True:
    import random
    import time
    def type_text(text, speed=0.03):
        for char in text:
            print(char, end="", flush=True)
            time.sleep(speed)
        print()

    def story(text, delay=2, speed=0.03):
        type_text(text, speed)
        time.sleep(delay)

    class Character:
        def __init__(self,hp,max_hp,d1,d2,crit_chance,heal_amount,ability_cooldown,ability_max_cooldown):
            self.hp = hp
            self.max_hp = max_hp
            self.d1 = d1
            self.d2 = d2
            self.crit_chance = crit_chance
            self.heal_amount = heal_amount
            self.ability_cooldown = ability_cooldown
            self.ability_max_cooldown = ability_max_cooldown
            self.attack_lock = False
            self.heal_lock = False
            self.ability_lock = False
            self.lock = 0
            self.shield =0
            self.prediction = 0
            self.prediction_active = False        
            self.win = False
            self.revived = False
            
        def Attack(self):
            damage = random.randint(self.d1,self.d2)
            if random.randint(1,100) <= self.crit_chance:
                damage = damage * 2 
                print("💥 CRITICAL HIT!")
            return damage

        def Heal(self):
            if self.hp + self.heal_amount > self.max_hp:
                heal_message = self.max_hp - self.hp
            else:
                heal_message = self.heal_amount
            self.hp = min(self.hp + self.heal_amount, self.max_hp)
            return heal_message

    class Warrior(Character):
        def __init__(self):
            super().__init__(100,100,10,20,5,20,0,4)
        def Ability(self):
            self.d1 += 15
            self.d2 += 15
            damage = self.Attack()
            self.d1, self.d2 = 10, 20
            self.ability_cooldown = self.ability_max_cooldown
            return damage

    class Tank(Character):
        def __init__(self):
            super().__init__(125,125,10,15,3,25,0,5)
        def Ability(self):
            self.shield = 3
            self.ability_cooldown = self.ability_max_cooldown

    class Assassin(Character):
        def __init__(self):
            super().__init__(90,90,15,25,10,15,0,5)
        def Ability(self):
            self.d1, self.d2 = (self.d1 + 35 - (self.hp * 2)), (self.d1 + 35 - (self.hp * 2))
            damage = self.Attack()
            self.d1, self.d2 = 15, 25
            self.ability_cooldown = self.ability_max_cooldown
            return damage

    class Adapter(Character):
        def __init__(self):
            super().__init__(150,150,12,22,8,15,0,5)
        def Ability(self):
            damage = 20
            self.hp = min(self.hp + 20, self.max_hp)
            self.ability_cooldown = self.ability_max_cooldown 
            return damage

    class Alien_Commander(Character):
        def __init__(self):
            super().__init__(400,400,10,20,5,15,0,6)
            self.shield = 0
            self.charge = 3
            self.phase = 1
        def Phase_1_Ability(self):
            if self.charge == 3:
                self.charge -= 1            
                print("Alien Commander Requested Help From The MotherShip!")
                print(f"⚡ {self.charge} MotherShip Support Charges Left")
                print("⚠️ PREPARE FOR THE ORBITAL LASER ATTACK!")
                damage = random.randint(25,40)
                self.ability_cooldown = self.ability_max_cooldown            
                return damage
            elif self.charge == 2:
                self.charge -= 1
                print("Alien Commander Requested Help From The MotherShip!")
                print(f"⚡ {self.charge} MotherShip Support Charges Left")
                print("🛡️ FORTIFIED SHIELD BARRIER LANDING ON THE COMMANDER!")
                self.shield = 3        
                self.ability_cooldown = self.ability_max_cooldown            
            elif self.charge == 1:
                self.charge -= 1
                print("Alien Commander Requested Help From The Mothership!")
                print(f"⚡ The MotherShip Is UnAvailable From Now On")
                print("🤖 REPAIR DRONE DEPLOYED!")
                if self.hp + 30 > self.max_hp:
                    heal_message = self.max_hp - self.hp
                else:
                    heal_message = 30
                self.hp = min(self.hp + 30, self.max_hp)
                self.ability_cooldown = self.ability_max_cooldown            
                return heal_message
        def System_Overwrite(self):
            x = random.randint(1,3)
            if x == 1:
                print("👽 Alien Commander Used System OverWrite!")
                print("🔒 Your Attack Is Locked For 2 Rounds!!!")
                self.ability_cooldown = self.ability_max_cooldown 
                return x           
            elif x == 2:
                print("👽 Alien Commander Used System OverWrite!")
                print("🔒 Your Heal Is Locked For 2 Rounds!!!")            
                self.ability_cooldown = self.ability_max_cooldown
                return x            
            elif x == 3:
                print("👽 Alien Commander Used System OverWrite!")
                print("🔒 Your Ability Is Locked For 2 Rounds!!!")            
                self.ability_cooldown = self.ability_max_cooldown            
                return x            
        def Predictive_Vision(self):
            print("👽 Alien Commander Used Predective Vision!")
            print("👁️ Alien Commander Is Predicting Your Next Move!")
            self.prediction_active = True
            self.ability_cooldown = self.ability_max_cooldown        
        def Phase_change(self):
            self.phase = 2
            story("""
    The Battle Stopped

    The Ground Started To Shake.""",3)
            story("""
    The Alien Commander Slowly Started To Float In The Air.

    Its Eyes Began To Glow.""",3)
            story("""
    
    The Alien Commander Spoke With An Angry Tone:

    "You Puny Human...
    How Dare You Even Think About Defeating ME?

    I Am The Commander Of The Largest Spaceship
    Across The Entire Galaxy!""",5)
            story("""
    "Now...

    You Will Witness My True Form!"

    The Alien Commander Started To Transform.

    Its Eyes Glowed Brighter.

    Its Body Started To Grow Bigger.

    The Air Around It Began To Shake.""",5)
            story("""
    
    "DIE, HUMAN!"

    You Unlocked The Commander's Second Phase.

    The Battle Has Changed.

    You Are Humanity's Only Hope.""",3)

            print("\n" + "=" * 45)
            print("           ⚠️ PHASE 2 ⚠️")
            print("=" * 45)
            print("⚔️ Damage      : 15 - 30")
            print("💥 Crit Chance : 10%")
            print("💀 Ability Changed!")
            print("=" * 45)
            time.sleep(3)
            self.d1 = 15
            self.d2 = 30
            self.crit_chance = 10

    def Combat(player,enemy):
        turn = 1
        phase_change = False
        while True:

            # ================= PLAYER TURN =================

            print("\n" + "=" * 45)
            print(f"                 TURN {turn}")
            print("=" * 45)

            print(f"YOU   : HP {player.hp}/{player.max_hp}"
                f" | Ability CD: {player.ability_cooldown}")

            print(f"ENEMY : HP {enemy.hp}/{enemy.max_hp}"
                f" | Ability CD: {enemy.ability_cooldown}")
            if player.attack_lock == True:
                print(f"🔒 Your Attack Is Locked: {player.lock}")
            if player.heal_lock == True:
                print(f"🔒 Your Heal Is Locked: {player.lock}")
            if player.ability_lock == True:
                print(f"🔒 Your Ability Is Locked: {player.lock}")                        
            if player.shield > 0:
                print(f"🛡️ Your Shield: {player.shield}")
            if enemy.shield > 0:
                print(f"🛡️ Enemy Shield: {enemy.shield}")

            print("-" * 45)
            if (turn % 2) == 1:
                try:
                    choice = int(input('Select Your Action:\n 1) ⚔️  Attack \n 2) ❤️  Heal \n 3) 🔥 Ability \n 4) ⏭️  Skip \n-->'))
                    if enemy.prediction_active == False or enemy.prediction != choice:
                        if enemy.prediction_active == True:
                            print("❌ PREDICTION FAILED!")
                            enemy.prediction_active = False
                            enemy.prediction = 0
                        if choice == 1:
                            if player.attack_lock == False:
                                damage = player.Attack()
                                if enemy.shield == 0:
                                    enemy.hp -= damage
                                    print(f"\n⚔️ You dealt {damage} damage!")
                                else:
                                    print("\n🛡️ Enemy blocked the attack!")                                                             
                            else:
                                print("🔒 Your Attack Is Locked By The Alien Commander!")
                                continue
                        elif choice == 2:
                            if player.heal_lock == False:
                                if player.hp == player.max_hp:
                                    print("\n❤️ Your HP is already full!")
                                    continue
                                else:
                                    x = player.Heal()
                                print(f"\n❤️ You healed {x} HP!") 
                            else:
                                print("🔒 Your Heal Is Locked By The Alien Commander!")
                                continue                        
                        elif choice == 3:
                            if player.ability_lock == False:
                                if player.ability_cooldown == 0:
                                    if isinstance(player, Warrior):
                                        damage = player.Ability()
                                        if enemy.shield == 0:
                                            enemy.hp -= damage
                                            print(f"\n🔥 Warrior Ability dealt {damage} damage!")
                                        else:
                                            print("\n🛡️ Enemy blocked your ability!")                                                        
                                    elif isinstance(player, Tank):
                                        player.Ability()
                                        print("\n🛡️ SHIELD ACTIVATED!")
                                        print(f"Shield duration: {player.shield} turns")                        
                                    elif isinstance(player, Assassin):
                                        if player.hp < 10:
                                            damage = player.Ability()
                                            if enemy.shield == 0:
                                                enemy.hp -= damage
                                                print(f"\n💀 Assassin Ability dealt {damage} damage!")
                                            else:
                                                print("\n🛡️ Enemy blocked your ability!")                                                                
                                        else:
                                            print("\n❌ Assassin Ability requires HP below 10!")
                                            continue
                                else:
                                    print(
                                        f"\n❌ Ability is on cooldown!"
                                        f" ({player.ability_cooldown} turns remaining)"
                                    )      
                                    continue                           
                            else:
                                print("🔒 Your Ability Is Locked By The Alien Commander!")
                                continue                        
                        elif choice == 4:
                            print("\n⏭️ You skipped your turn.")                        
                    else:
                        enemy.prediction = 0
                        enemy.prediction_active = False
                        print("🎯 PREDICTION CORRECT!")
                        print("💥 ALIEN COMMANDER PREVENTED YOUR MOVE AND DAMAGED YOU FOR 30 HP")
                        player.hp -= 30
                    if choice not in (1,2,3,4):
                        print("\n❌ Enter a valid value!")
                        continue                    
                except ValueError:
                    print("\n❌ Enter a number!")
                    continue
                player.ability_cooldown -= 1 if player.ability_cooldown > 0 else player.ability_cooldown
                player.shield -= 1 if player.shield > 0 else player.shield
                player.lock -= 1 if player.lock > 0 else player.lock
                turn += 1
                time.sleep(1)
                if player.lock == 0:
                    player.attack_lock = False
                    player.heal_lock = False
                    player.ability_lock = False
            # ================= ENEMY TURN =================
            
            else:

                if isinstance(enemy,Alien_Commander) and phase_change == False:
                    if enemy.hp <=200:
                        time.sleep(3)
                        enemy.Phase_change()
                        phase_change = True


                print("             ENEMY TURN")
                print("-" * 45)
                
                choice = random.randint(1,100)
                enemy_hp_percent = enemy.hp / enemy.max_hp
                if enemy_hp_percent > 0.3:
                    if enemy.ability_cooldown == 0:
                        if choice > 50:
                            damage = enemy.Attack()
                            if player.shield == 0:
                                player.hp -= damage
                                print(f"\n⚔️ Enemy dealt {damage} damage!")
                            else:
                                print("\n🛡️ You blocked the attack!")                                                
                        elif choice > 20 and choice <= 50:
                            if isinstance(enemy, Warrior):
                                damage = enemy.Ability()
                                if player.shield == 0:
                                    player.hp -= damage
                                    print(f"\n🔥 Enemy Warrior used Ability!")
                                    print(f"Damage: {damage}")
                                else:
                                    print("\n🛡️ You blocked the ability!")                            
                            elif isinstance(enemy, Tank):
                                enemy.Ability()
                                print("\n🛡️ Enemy Tank activated Shield!")
                            elif isinstance(enemy, Assassin):
                                if enemy.hp < 10:
                                    damage = enemy.Ability()
                                    if player.shield == 0:
                                        player.hp -= damage
                                        print(f"\n💀 Enemy Assassin used Ability!")
                                        print(f"Damage: {damage}")
                                    else:
                                        print("\n🛡️ You blocked the ability!")                                
                                else:
                                    continue   
                            elif isinstance(enemy, Adapter):
                                player.hp -= enemy.Ability()
                                print(f"\n💀 Enemy Adapter used Ability!")                            
                                print(f"🩸 Enemy Drained 20 Hp From You And Gained It To Itself")      
                            elif isinstance(enemy, Alien_Commander):
                                if enemy.phase == 1:
                                        if enemy.charge == 3:
                                            damage = enemy.Phase_1_Ability()
                                            player.hp -= damage
                                            print(f"\n💀 Alien Commander used Ability!") 
                                            print(f"Damage : {damage}")  
                                        elif enemy.charge == 2:
                                            enemy.Phase_1_Ability()                             
                                            print("\n🛡️ Alien Commander activated Shield!")
                                        elif enemy.charge == 1:
                                            if enemy.hp != enemy.max_hp:
                                                x = enemy.Phase_1_Ability()
                                                print(f"\n❤️ Alien Commander healed {x} HP!")                                    
                                            else:
                                                continue
                                        else:
                                            continue
                                else:
                                    a = random.randint(1,2)
                                    if a == 1:
                                            print(f"\n💀 Alien Commander used Ability!")
                                            x = enemy.System_Overwrite()
                                            if x == 1:
                                                player.attack_lock = True
                                                player.lock = 2
                                            elif x == 2:
                                                player.heal_lock = True
                                                player.lock = 2
                                            else:
                                                player.ability_lock = True
                                                player.lock = 2
                                                                                
                                    else:
                                        print(f"\n💀 Alien Commander used Ability!")    
                                        if isinstance(player,Assassin):
                                            if player.hp == player.max_hp:
                                                enemy.prediction = random.randint(1,2)
                                                if enemy.prediction == 2:
                                                    enemy.prediction = 4
                                            else:
                                                if player.hp >= 10:
                                                    enemy.prediction = random.randint(1,3)
                                                    if enemy.prediction == 3:
                                                        enemy.prediction = 4
                                                else:
                                                    if player.ability_cooldown == 0:
                                                        enemy.prediction = random.randint(1,4)
                                                    else:
                                                        enemy.prediction = random.randint(1,3)
                                                        if enemy.prediction == 3:
                                                            enemy.prediction = 4
                                        else:
                                            if player.hp == player.max_hp:
                                                if player.ability_cooldown == 0:
                                                    x = random.randint(1,3)
                                                    if x == 1:
                                                        enemy.prediction = 1
                                                    elif x == 2:
                                                        enemy.prediction = 3
                                                    elif x == 3:
                                                        enemy.prediction = 4
                                                else:
                                                    x = random.randint(1,2)
                                                    if x == 1:
                                                        enemy.prediction = 1
                                                    else:
                                                        enemy.prediction = 4
                                            else:
                                                if enemy.ability_cooldown == 0:
                                                    enemy.prediction = random.randint(1,4)
                                                else:
                                                    x = random.randint(1,3)                                                                                 
                                                    if x == 3:
                                                        enemy.prediction = 4
                                                    else:
                                                        enemy.prediction = x
                                        enemy.Predictive_Vision()
                        else:
                            if enemy.hp != enemy.max_hp:
                                x = enemy.Heal()   
                                print(f"\n❤️ Enemy healed {x} HP!")                                     
                            else:
                                continue
                    else:
                        if choice >20:
                            damage = enemy.Attack()
                            if player.shield == 0:                    
                                player.hp -= damage
                                print(f"\n⚔️ Enemy dealt {damage} damage!")
                            else:
                                print("\n🛡️ You blocked the attack!")                        
                        else:
                            if enemy.hp == enemy.max_hp:
                                continue
                            else:
                                x = enemy.Heal()
                                print(f"\n❤️ Enemy healed {x} HP!")                         
                else:
                    print("⚠️ Enemy is LOW HP!")            
                    if enemy.ability_cooldown == 0:
                        if choice > 80:
                            damage = enemy.Attack()
                            if player.shield == 0:
                                player.hp -= damage
                                print(f"\n⚔️ Enemy dealt {damage} damage!")
                            else:
                                print("\n🛡️ You blocked the attack!")                        
                        elif choice > 30 and choice <= 80:
                            if enemy.hp != enemy.max_hp:
                                x = enemy.Heal()
                                print(f"\n❤️ Enemy healed {x} HP!")                    
                            else:
                                continue
                        else:
                            if isinstance(enemy, Warrior):
                                damage = enemy.Ability()
                                if player.shield == 0:
                                    player.hp -= damage
                                    print(f"\n🔥 Enemy Warrior used Ability!")
                                    print(f"Damage: {damage}")
                                else:
                                    print("\n🛡️ You blocked the ability!")                            
                            elif isinstance(enemy, Tank):
                                enemy.Ability()
                                print("\n🛡️ Enemy Tank activated Shield!")
                            elif isinstance(enemy, Assassin):
                                if enemy.hp < 10:
                                    damage = enemy.Ability()
                                    if player.shield == 0:
                                        player.hp -= damage
                                        print(f"\n💀 Enemy Assassin used Ability!")
                                        print(f"Damage: {damage}")
                                    else:
                                        print("\n🛡️ You blocked the ability!")                                
                                else:
                                    continue
                            elif isinstance(enemy, Adapter):
                                player.hp -= enemy.Ability()
                                print(f"\n💀 Enemy Adapter used Ability!")                            
                                print(f"🩸 Enemy Drained 20 Hp From You And Gained It To Itself(Cannot Be Blocked)")
                                enemy.ability_cooldown = enemy.ability_max_cooldown
                            elif isinstance(enemy, Alien_Commander):
                                if enemy.phase == 1:
                                        if enemy.charge == 3:
                                            damage = enemy.Phase_1_Ability()
                                            player.hp -= damage
                                            print(f"\n💀 Alien Commander used Ability!") 
                                            print(f"Damage : {damage}")  
                                        elif enemy.charge == 2:
                                            enemy.Phase_1_Ability()                             
                                            print("\n🛡️ Alien Commander activated Shield!")
                                        elif enemy.charge == 1:
                                            if enemy.hp != enemy.max_hp:
                                                x = enemy.Phase_1_Ability()
                                                print(f"\n❤️ Alien Commander healed {x} HP!")                                    
                                            else:
                                                continue
                                        else:
                                            continue
                                else:
                                    a = random.randint(1,2)
                                    if a == 1:
                                            print(f"\n💀 Alien Commander used Ability!")
                                            x = enemy.System_Overwrite()
                                            if x == 1:
                                                player.attack_lock = True
                                                player.lock = 2
                                            elif x == 2:
                                                player.heal_lock = True
                                                player.lock = 2
                                            else:
                                                player.ability_lock = True
                                                player.lock = 2
                                                                                
                                    else:
                                        print(f"\n💀 Alien Commander used Ability!")    
                                        if isinstance(player,Assassin):
                                            if player.hp == player.max_hp:
                                                enemy.prediction = 1
                                            else:
                                                if player.hp >= 10:
                                                    enemy.prediction = random.randint(1,2)
                                                else:
                                                    if player.ability_cooldown == 0:
                                                        enemy.prediction = random.randint(1,3)
                                                    else:
                                                        enemy.prediction = random.randint(1,2)
                                        else:
                                            if player.hp == player.max_hp:
                                                if player.ability_cooldown == 0:
                                                    x = random.randint(1,2)
                                                    if x == 1:
                                                        enemy.prediction = 1
                                                    else:
                                                        enemy.prediction = 3
                                                else:
                                                    enemy.prediction = 1
                                            else:
                                                if enemy.ability_cooldown == 0:
                                                    enemy.prediction = random.randint(1,3)
                                                else:
                                                    enemy.prediction = random.randint(1,2)                                                                                 
                                        enemy.Predictive_Vision()                                                    
                    else:
                        if choice >50:
                            damage = enemy.Attack()
                            if player.shield == 0:
                                player.hp -= damage
                                print(f"\n⚔️ Enemy dealt {damage} damage!")
                            else:
                                print("\n🛡️ You blocked the attack!")                        
                        else:
                            if enemy.hp == enemy.max_hp:
                                continue
                            else:
                                if enemy.hp != enemy.max_hp:
                                    x = enemy.Heal()
                                    print(f"\n❤️ Enemy healed {x} HP!")                        
                                else:
                                    continue

            # ================= END OF TURN =================
                enemy.ability_cooldown -= 1 if enemy.ability_cooldown > 0 else enemy.ability_cooldown
                enemy.shield -= 1 if enemy.shield > 0 else enemy.shield        
                turn += 1
                time.sleep(1)
            player.hp = 0 if player.hp < 0 else player.hp
            enemy.hp = 0 if enemy.hp < 0 else enemy.hp


            print("\n" + "-" * 45)
            print(f"Your HP  : {player.hp}/{player.max_hp}")
            print(f"Enemy HP : {enemy.hp}/{enemy.max_hp}")
            print("-" * 45)

            if enemy.hp <= 0:
                print("\n" + "=" * 45)
                print("             🏆 ENEMY DEFEATED!")
                print("             YOU WIN!")
                print("=" * 45)
                player.hp = player.max_hp
                player.ability_cooldown = 0
                enemy.hp = enemy.max_hp
                enemy.ability_cooldown = 0
                player.win = True
                break

            elif player.hp <= 0:
                if isinstance(enemy, Alien_Commander) and player.revived == False:
                    time.sleep(4)
                    player.revived = True
                    story("You Fall To The Ground.",2)
                    story("""
    You Cannot Fight Anymore

    You Close Your Eyes

    And Then...""",3)
                    story("""
    "GET UP"
    "YOU CAN DO IT"
    "STAND UP"
    "DONT GIVE UP"
    """,3)
                    story("""
    You Hear People's Voices.

    They Are Shouting At You To Continue

    You Remember That Humanity Is At Stake
                    """,4)
                    story("""
    You Gather Up All Your Strength

    And Rise For One Final Time""")
                    story("""
    (HP Healed For 50%)
    (Ability Cooldown Reset)
    (Your Damage Increased By 5 )""",4)
                    player.ability_cooldown = 0
                    player.d1 += 5
                    player.d2 += 5
                    if isinstance(player,Tank):
                        player.hp = 63
                    else:
                        player.hp = int(player.max_hp / 2)

                else:
                    print("\n" + "=" * 45)
                    print("             💀 YOU WERE DEFEATED")
                    print("             GAME OVER")
                    print("=" * 45)
                    player.hp = player.max_hp
                    player.ability_cooldown = 0
                    enemy.hp = enemy.max_hp
                    enemy.ability_cooldown = 0            
                    player.win = False
                    time.sleep(3)
                    type_text("...",0.5)
                    story("""
        You Fall To The Ground.""",2)
                    story("""
        You Accept Your Demise And Close Your Eyes
        """,2)
                    story("""
        But Then

        You Hear An Unfamiliar Voice:

        "Wake Up" 

        "Get Up"

        "FIGHT"

        """,3)
                    story("""
        You Open Your Eyes And Get Back On Your Feet

        The Battle Continues

        """,2)
                    type_text("        You Are Filled With",0.1)
                    time.sleep(2)
                    type_text("        DETERMINATION", 0.2)
                    time.sleep(2)                
                    break

    if warrior_win == True and tank_win == True and assassin_win == True:
        story("""
🔓 SECRET ENDING UNLOCKED

You Have Completed The Game With All Three Classes.

👁️ The Truth Awaits...
""",5)
        type_text("""
            [CLASSIFIED — HUMANITY ARCHIVES]

YEAR: 2072

  SUBJECT: THE ALIEN MESSAGE

The message was received simultaneously across the entire world.

No satellite detected its origin.

No government claimed responsibility.

No known language could identify it.

Yet every human being understood it.

**"We are coming."**

For the first time in human history, every nation agreed on the same decision.

Humanity would choose its defenders.

A worldwide vote was held.

And the result was clear.

Three individuals were selected.

They were sent to investigate the first confirmed alien activity.

At the time, everyone believed they were fighting an invasion.

They were wrong.

The creatures they encountered were not an army.

They were obstacles.

Each one was protecting something.

Something buried beneath the events of the invasion.

---

CHAPTER 02 — RECOVERED DATA

After the first encounters, our researchers discovered something disturbing.

The aliens were not attacking randomly.

They were searching for specific people.

And every time one of those people came close to discovering the truth...

The aliens became stronger.

More intelligent.

More organized.

Then came the Assassin.

Then the Adapter.

And finally...

The Alien Commander.

---

CHAPTER 05 — FINAL RECORD

The Commander was different from the others.

It didn't behave like a soldier.

It behaved like someone who already knew the outcome.

It could predict attacks.

It could interfere with our systems.

It could even temporarily prevent its opponent from using basic abilities.

We originally believed these were advanced alien technologies.

They weren't.

The Commander wasn't controlling our systems.

It was accessing them.

Because the system was built from technology that humanity had discovered years earlier.

Technology we were never supposed to find.

---

THE TRUTH

The first alien message was not a declaration of war.

It was a warning.

Humanity had discovered something buried beneath the Earth.

Something that had existed long before human civilization.

We tried to communicate with it.

We tried to control it.

And eventually...

We activated it.

The aliens didn't come to conquer Earth.

They came because we had awakened something they had spent centuries trying to contain.

The creatures we fought were sent to stop humanity from reaching it.

The Commander was the final guardian.

Not our enemy.

Its mission was simple:

Prevent humanity from making the same mistake twice.

----

The report ends here.

There is one final note written by an unknown researcher.

"If you're reading this, then the Commander has already fallen.

That means humanity has reached the final door.

And if the stories are true...

There was never an invasion.

We were the ones who started it."

[FILE TERMINATED]

[ACCESS LEVEL: UNKNOWN]
""",0.03)
        break
    story_play = int(input("Enter '1' To Play The Intro:"))
    if story_play == 1:
        story("""
    YEAR 2072.

    Humanity was no longer fighting wars against itself.

    Not because they found peace...

    But because something far worse had arrived.
        """, 5)


        story("""
    An unknown signal reached Earth from deep space.
        """, 3)


        story("""
    The message was simple:
        """, 2)


        story("""
    "Humans.

    We have observed your species for centuries.

    Your conflicts, your violence, your endless struggle...

    Once, it was fascinating.
        """, 5)


        story("""
    But now...

    You have become predictable.
        """, 3)


        story("""
    So we offer you a final opportunity.
        """, 2)


        story("""
    Prove that your species deserves to exist.
        """, 2)


        story("""
    Fight our creations.

    Replicated versions of your own kind.

    Each one designed to test a different aspect of humanity.
        """, 5)


        story("""
    Survive the selection.

    Or disappear."
        """, 4)


        story("""
    The entire world watched.
        """, 2)


        story("""
    Billions voted.
        """, 2)


        story("""
    And one person was chosen.
        """, 2)


        story("""
    You.
        """, 3)


        story("""
    The future of humanity depends on your survival.
        """, 5)

        story("""
    The alien ship descended above Earth.

    A voice echoed:

    "Your combat ability will be enhanced.

    Choose your fighting style."

        """,3)

    print("\n" + "=" * 50)
    type_text("               THE SELECTION BEGINS...", 0.05)
    print("=" * 50)
    time.sleep(2)

    try:
        choice_class = int(input("Choose Your Class:\n 1)Warrior\n 2)Tank \n 3)Assassin\n-->"))
        if choice_class == 1:
            player = Warrior()
        elif choice_class == 2:
            player = Tank()
        elif choice_class == 3:
            player = Assassin()
        else:
            print("Invalid Number")
    except ValueError:
        print("Enter A Number!")

    def Chapter1():
        enemy = Warrior()
        story("""
    A figure stepped out of the alien ship.

    At first glance, it looked human.

    But something was wrong...

    Its movements were unnatural.
    Its eyes were empty.

    The alien message appeared:

    "Subject created from humanity's greatest warriors.

    Let's see if your species can defeat itself."
            """,
            3
        )

        while player.win == False:
            Combat(player,enemy)
        player.win = False
        time.sleep(2)
        story("""
    The battlefield became silent.

    The replicated soldier fell to the ground.

    For a few seconds...

    Nothing happened.

    """, 3)
        story("""
    Then the alien voice returned.

    "RESULT:

    Subject defeated."

    """, 3)
        story("""
    The entire world watched in silence.

    Humanity had just witnessed its first victory.

    But nobody celebrated.

    Because everyone had the same question...

    "What exactly did we just kill?"
    """, 4)
        story("""
    The body of the replicated soldier began to disappear.

    Not like a machine.

    Not like a creature.

    Like a human.

    """, 4)
        story("""
    Your scanners detected something unusual.

    Analyzing genetic structure...

    Processing...

    Error.
    """, 3)
        story("""
    A second message appeared:

    "Genetic similarity with human population:

    99.8%"

    """, 4)
        story("""
    The alien voice spoke again:

    "Interesting."

    "Your species still possesses unexpected potential."

    """, 3)
        story("""
    "However...

    One victory proves nothing."

    "More subjects are waiting."

    """, 3)
        story("""
    The battlefield changed.

    Somewhere in the distance...

    Another signal appeared.

    Stronger.

    Faster.

    More dangerous.

    """, 4)
        story("""
    The Selection was not over.

    It had only begun.
    """, 3)

    def Chapter2():
        enemy = Tank()
        story("""
    CHAPTER 2:
    THE WILL TO SURVIVE

    """, 2)
        story("""
    Hours passed after the first battle.

    The world was still trying to understand what happened.

    The creature you defeated...

    Was not an alien.

    Was not a machine.

    It was something far worse.

    A reflection of humanity itself.
    """, 4)
        story("""
    But the aliens did not care about humanity's questions.

    They only cared about one thing:

    The results.
    """, 3)
        story("""
    A new signal appeared above the battlefield.

    The alien ship opened once again.

    This time...

    Something heavier stepped out.
    """, 4)
        story("""
    The ground shook with every step.

    A massive figure emerged from the darkness.

    Covered in advanced armor.

    Built to withstand damage.

    Built to never stop moving.
    """, 4)
        story("""
    The alien voice announced:

    "SECOND SUBJECT DEPLOYED."

    "Classification:
    Replicated Human.

    Combat Pattern:
    Tank."

    """, 3)
        story("""
    "This model represents another fundamental aspect of your species."

    "Your ability to endure."

    "Your refusal to surrender."

    """, 4)
        story("""
    The replicated soldier looked at you.

    Unlike the first one...

    This one showed no aggression.

    No anger.

    No emotion.

    Only one purpose.
    """, 3)
        story("""
    Survive.

    At any cost.
    """, 3)
        story("""
    The alien voice continued:

    "Your first victory measured your strength."

    "Now..."

    "We will measure your persistence."

    """, 4)
        story("""
    The Tank raised its shield.

    The battlefield was ready.

    The second selection begins.
    """, 4)
        while player.win == False:
            Combat(player,enemy)
        player.win = False
        time.sleep(2)
        story("""
    The battlefield fell silent once again.

    The Sentinel stood motionless for a final moment...

    Then its armor began to crack.

    The massive figure collapsed.

    """, 4)
        story("""
    SECOND SUBJECT:

    DEFEATED.

    """, 3)
        story("""
    The world erupted.

    Another victory.

    Another impossible survival.

    But this time...

    Something was different.
    """, 4)
        story("""
    As the replicated soldier disappeared...

    A strange signal was detected.

    Not from the alien ship.

    From the creature itself.
    """, 4)
        story("""
    Your equipment began analyzing the remains.

    Searching for answers.

    Searching for the truth.
    """, 3)
        story("""
    Analysis complete.

    Warning:

    Artificial construction detected.

    But biological origin confirmed.
    """, 4)
        story("""
    The results were impossible.

    This was not a machine.

    This was not a normal clone.

    It was a living being.

    Created from human information.
    """, 4)
        story("""
    The alien voice interrupted:

    "Fascinating."

    "Your species continues to demonstrate unexpected behavior."

    """, 3)
        story("""
    "You do not simply fight to survive."

    "You fight to understand."

    """, 3)
        story("""
    A pause followed.

    For the first time...

    The alien voice sounded uncertain.
    """, 4)
        story("""
    "Perhaps the next subject will provide a better answer."

    """, 3)
        story("""
    A new signal appeared.

    The battlefield changed.

    The temperature dropped.

    The lights disappeared.

    Something was approaching...
    """, 4)
        story("""
    The Selection continued.

    But now...

    You were no longer fighting only for humanity.

    You were fighting to discover why humanity was chosen.
    """, 5)

    def Chapter3():
        enemy = Assassin()
        story("""
    CHAPTER 3:
    THE SHADOW WITHIN

    """, 2)
        story("""
    After two battles...

    Humanity began to believe.

    Maybe this was possible.

    Maybe one person could actually survive the Selection.
    """, 4)
        story("""
    But you knew the truth.

    The enemies were not getting weaker.

    They were learning.
    """, 3)
        story("""
    The alien ship remained silent for a long time.

    No announcement.

    No warning.

    Only darkness.
    """, 4)
        story("""
    Then...

    Every light on the battlefield disappeared.

    Your sensors failed.

    Your connection with Earth was lost.
    """, 4)
        story("""
    A voice finally appeared.

    But this time...

    It was different.
    """, 3)
        story("""
    "THIRD SUBJECT DEPLOYED."

    "Classification:
    Replicated Human.

    Combat Pattern:
    Assassin."
    """, 3)
        story("""
    Something moved in the darkness.

    Too fast to see.

    Too quiet to hear.
    """, 4)
        story("""
    Unlike the previous subjects...

    This one was not built to overpower you.

    It was not built to survive your attacks.

    It was built to wait.

    To observe.

    To strike at the perfect moment.
    """, 5)
        story("""
    The alien voice continued:

    "Your species has always feared death."

    "But fear has also created your greatest instincts."

    "Your caution."

    "Your adaptation."

    "Your ability to survive when hope disappears."
    """, 5)
        story("""
    The figure stepped into the light.

    It looked almost identical to you.

    Not physically...

    But in its eyes.
    """, 4)
        story("""
    For the first time...

    You felt something unexpected.

    Not anger.

    Not fear.

    Recognition.
    """, 3)
        story("""
    The alien voice whispered:

    "Every human carries a shadow."

    "Now..."

    "We will see if you can defeat yours."
    """, 4)
        story("""
    The Assassin disappeared.

    The battle had already begun.
    """, 4)
        while player.win == False:
            Combat(player,enemy)
        player.win = False
        time.sleep(2)
        story("""
    The battlefield remained silent.

    The Assassin stood frozen in the darkness...

    Its final attack never came.

    Slowly...

    The figure collapsed.
    """, 4)
        story("""
    THIRD SUBJECT:

    DEFEATED.
    """, 3)
        story("""
    For the first time...

    The alien ship did not immediately announce the next battle.
    """, 4)
        story("""
    No celebration.

    No analysis.

    No comment.
    """, 3)
        story("""
    The silence was unsettling.

    Almost as if...

    They were surprised.
    """, 4)
        story("""
    Your sensors activated.

    Scanning the remains of the third subject...

    """, 3)
        story("""
    Analysis complete.

    Genetic similarity:

    99.9%

    Combat data:

    Transferred.
    """, 4)
        story("""
    A message appeared.

    But this time...

    It was not from the aliens.
    """, 3)
        story("""
    UNKNOWN SIGNAL DETECTED.

    SOURCE:

    REPLICATED HUMAN NETWORK.
    """, 4)
        story("""
    For a moment...

    You saw something impossible.

    Images.

    Memories.

    Fragments of lives that were never supposed to exist.
    """, 5)
        story("""
    The replicated humans were not empty copies.

    They remembered.

    They felt.

    They existed.
    """, 4)
        story("""
    The alien voice finally returned:

    "Interesting."

    "Your reaction is unexpected."

    """, 3)
        story("""
    "You were supposed to see them as enemies."

    "But instead..."

    "You questioned their existence."
    """, 4)
        story("""
    A pause followed.

    Then the alien continued:

    "Perhaps humanity's most unique trait..."

    "Is not its strength."

    "Not its ability to survive."

    """, 4)
        story("""
    "But its ability to see itself in others."
    """, 3)
        story("""
    The battlefield changed.

    Three subjects defeated.

    Three aspects of humanity tested.
    """, 4)
        story("""
    But somewhere above you...

    A new signal appeared.

    Different from the others.

    Stronger.

    More complex.
    """, 4)
        story("""
    The aliens had collected enough data.

    Now...

    They were ready for the final experiment.
    """, 5)
        story("""
    The Selection was entering its next phase.
    """, 3)

    def Chapter4():
        enemy = Adapter()
        story("""
    CHAPTER 4:
    THE HUNGER WITHIN

    """, 2)
        story("""
    The battlefield was quiet.

    Three subjects had fallen.

    Three experiments had failed.
    """, 4)
        story("""
    But the aliens were not disappointed.

    They were learning.
    """, 3)
        story("""
    Every attack.

    Every decision.

    Every moment of hesitation...

    Was recorded.
    """, 4)
        story("""
    You looked toward the sky.

    For the first time...

    You wondered.

    Were you fighting for humanity?

    Or were you simply helping them understand it?
    """, 4)
        story("""
    A new signal appeared.

    Different from the previous ones.
    """, 3)
        story("""
    No footsteps.

    No sound.

    No movement.
    """, 3)
        story("""
    The alien voice spoke:

    "Previous subjects tested your physical capabilities."

    "Your strength."

    "Your endurance."

    "Your instincts."
    """, 5)
        story("""
    "But there is another reason your species survived."

    "Adaptation."
    """, 3)
        story("""
    "Humans do not only overcome obstacles."

    "They use them."
    """, 3)
        story("""
    "They consume."

    "They change."

    "They become something new."
    """, 4)
        story("""
    The ground beneath you began to move.
    """, 3)
        story("""
    Something emerged from the darkness.

    Not a warrior.

    Not a defender.

    Not a hunter.
    """, 4)
        story("""
    A creature designed with one purpose:

    Adapt.
    """, 3)
        story("""
    The alien voice continued:

    "Subject P-04."

    "Classification:
    Replicated Parasite."
    """, 4)
        story("""
    "It will not defeat you through power."

    "It will not defeat you through speed."
    """, 3)
        story("""
    "It will simply take what you have..."

    "And make it its own."
    """, 4)
        story("""
    The creature looked at you.

    Almost like it was studying you.

    Waiting.
    """, 3)
        story("""
    Then...

    It smiled.
    """, 2)
        story("""
    The experiment continued.
    """, 3)
        while player.win == False:
            Combat(player,enemy)
        player.win = False
        time.sleep(2)
        story("""
    The creature fell.

    Its body slowly lost the energy that kept it alive.
    """, 4)
        story("""
    The final traces of the stolen biological energy disappeared.

    SUBJECT P-04:

    DEFEATED.
    """, 4)
        story("""
    For a moment...

    There was nothing.
    """, 3)
        story("""
    No new enemy appeared.

    No new challenge was announced.
    """, 3)
        story("""
    The alien ship remained completely silent.
    """, 4)
        story("""
    You raised your weapon.

    Waiting for the next experiment.
    """, 3)
        story("""
    But instead...

    A different voice spoke.
    """, 4)
        story("""
    Not the artificial voice used during the selection.

    A real voice.
    """, 3)
        story("""
    "You have exceeded our expectations."
    """, 4)
        story("""
    The voice came from the largest structure above Earth.
    """, 4)
        story("""
    The alien commander had been watching all along.
    """, 4)
        story("""
    "Four subjects."

    "Four experiments."

    "Four attempts to understand your species."
    """, 5)
        story("""
    "We studied your strength."

    "We studied your endurance."

    "We studied your instincts."

    "We studied your ability to adapt."
    """, 5)
        story("""
    "But every result created the same question."
    """, 3)
        story("""
    "Why?"
    """, 3)
        story("""
    "Why does a species full of conflict..."

    "Continue to fight for its existence?"
    """, 5)
        story("""
    The battlefield changed.

    The selection area disappeared.

    The entire planet became silent.
    """, 4)
        story("""
    The alien commander finally revealed himself.
    """, 4)
        story("""
    "You defeated our creations."

    "But you have not defeated the purpose of this experiment."
    """, 4)
        story("""
    "Because the final answer..."

    "Was never inside them."
    """, 4)
        story("""
    A massive energy signature appeared.
    """, 3)
        story("""
    The alien ship opened.
    """, 3)
        story("""
    "For centuries, we have observed civilizations."

    "We have seen countless species rise..."

    "And disappear."
    """, 5)
        story("""
    "Humanity was supposed to be another example."
    """, 3)
        story("""
    "But now..."

    "We must see the answer ourselves."
    """, 4)
        story("""
    The voice became colder.
    """, 3)
        story("""
    "I will conduct the final test personally."
    """, 4)
        story("""
    No more replicas.

    No more experiments.
    """, 3)
        story("""
    Only the creator...

    Against the creation that refused to be erased.
    """, 5)

    def Chapter5():
        enemy = Alien_Commander()
        story("""
    CHAPTER 5:
    THE LAST JUDGMENT

    """, 3)
        story("""
    The battlefield was silent.

    The experiments were over.
    """, 4)
        story("""
    Four subjects had fallen.

    Four creations designed to represent humanity's greatest traits.
    """, 5)
        story("""
    Strength.

    Endurance.

    Instinct.

    Adaptation.
    """, 4)
        story("""
    You had survived them all.
    """, 3)
        story("""
    But there was no celebration.

    No escape.

    No victory.
    """, 3)
        story("""
    Because the one who created the tests...

    Had finally arrived.
    """, 4)
        story("""
    The sky above Earth began to change.
    """, 4)
        story("""
    The massive alien ship opened.

    A figure stepped forward.
    """, 4)
        story("""
    Unlike the previous subjects...

    This was not a replica.

    Not an experiment.

    Not a creation.
    """, 4)
        story("""
    This was the mind behind everything.
    """, 3)
        story("""
    The alien commander looked at you.
    """, 3)
        story("""
    "Fascinating."

    "After all these years..."

    "After countless civilizations..."

    "We finally found something unexpected."
    """, 5)
        story("""
    "You were never the strongest subject."

    "You were never the fastest."

    "You were never the most efficient."
    """, 5)
        story("""
    "Yet you continued."
    """, 3)
        story("""
    The commander stepped closer.
    """, 3)
        story("""
    "We created warriors."

    "We created survivors."

    "We created perfect copies."
    """, 4)
        story("""
    "But every creation had something missing."
    """, 3)
        story("""
    "The one thing we could not replicate."
    """, 3)
        story("""
    "Choice."
    """, 3)
        story("""
    A powerful energy surrounded the alien commander.
    """, 4)
        story("""
    "But understanding something..."

    "Does not mean accepting it."
    """, 4)
        story("""
    "You have proven that humanity is unique."
    """, 3)
        story("""
    "Now prove that it deserves to continue."
    """, 4)
        story("""
    The alien commander raised his weapon.
    """, 3)
        story("""
    "Final evaluation begins."
    """, 3)
        story("""
    No more experiments.

    No more replicas.

    No more tests.
    """, 4)
        story("""
    Only one final battle remains.
    """, 4)
        story("""
    Humanity's future...

    Will be decided now.
    """, 5)    
        while player.win == False:
            Combat(player,enemy)
        player.win = False
        time.sleep(5)
        story("""
    The Alien Commander Fell.

    For A Moment...

    Everything Was Silent.
    """, 3)

        story("""
    Then...

    The World Exploded In Celebration.
    """, 4)

        story("""
    Millions Of Voices Filled The Streets.

    People Shouted.

    People Cried.

    People Hugged Each Other.

    Across Every Continent...

    Humanity Celebrated.
    """, 5)

        story("""
    The Same People Who Had Watched You Fight...

    Had Finally Seen The Impossible.

    A Human Had Defeated The Alien Commander.
    """, 5)

        story("""
    Across The World...

    Flags Were Raised.

    Crowds Filled The Streets.

    People Who Had Never Met Each Other...

    Celebrated Together.
    """, 4)

        story("""
    For The First Time...

    The Entire Planet Had One Reason To Celebrate.
    """, 4)

        story("""
    Above Earth...

    The Alien Ship Remained Completely Still.
    """, 3)

        story("""
    Its Weapons Were Silent.

    Its Lights Began To Fade.

    And Then...

    A Final Message Appeared.
    """, 4)

        story("""
    "SELECTION COMPLETE."
    """, 3)

        story("""
    "FINAL SUBJECT:

    HUMAN."
    """, 4)

        story("""
    The Alien Commander's Voice Returned.

    Weak.

    Broken.
    """, 3)

        story("""
    "You Were Never Supposed To Win."
    """, 4)

        story("""
    "We Studied Your Strength."

    "Your Endurance."

    "Your Instinct."

    "Your Ability To Adapt."
    """, 5)

        story("""
    "But None Of Those Things Explained You."
    """, 4)

        story("""
    "We Created Replicas."

    "Perfect Soldiers."

    "Beings That Could Survive Almost Anything."
    """, 5)

        story("""
    "And Yet..."

    "They Always Followed Their Design."
    """, 4)

        story("""
    "You Did Not."
    """, 3)

        story("""
    "You Chose."
    """, 3)

        story("""
    "You Chose When To Fight."

    "When To Heal."

    "When To Take A Risk."

    "You Chose To Continue..."
    """, 5)

        story("""
    "Even When There Was No Guarantee Of Victory."
    """, 4)

        story("""
    The Commander Became Silent.
    """, 3)

        story("""
    Then It Spoke One Final Time.
    """, 3)

        story("""
    "Now I Understand."
    """, 4)

        story("""
    "The Reason Humanity Survives..."

    "Is Not Because Humans Are The Strongest Or The Smartest Or The Most Efficient."
    """, 4)

        story("""
    "It Is Because..."

    "They Can Choose What They Become."
    """, 5)

        story("""
    The Alien Commander Lowered Its Weapon.
    """, 3)

        story("""
    "For Centuries..."

    "We Judged Civilizations By Their Strength."
    """, 4)

        story("""
    "We Destroyed Those That Failed."

    "We Ignored Those That Were Weak."

    "We Never Asked Them Why They Wanted To Live."
    """, 5)

        story("""
    "But Humanity..."

    "You Made Us Ask."
    """, 4)

        story("""
    The Alien Ship Slowly Began To Rise.
    """, 4)

        story("""
    No Final Attack Came.

    No Threat Was Made.

    No Warning Was Given.
    """, 3)

        story("""
    The Ship Turned Away From Earth.

    And Slowly...

    It Disappeared Into The Stars.
    """, 5)

        story("""
    The Crowds Below Continued To Celebrate.

    For The First Time In Years...

    People Looked Toward The Future Without Fear.
    """, 5)

        story("""
    You Had Fought Warriors.

    Survived The Strongest Defenders.

    Faced Your Own Shadow.

    And Defeated A Creature That Could Turn Your Strength Against You.
    """, 5)

        story("""
    And At The End...

    You Faced The One Who Had Created Them All.
    """, 4)

        story("""
    You Did Not Win Because You Were Perfect.

    You Won Because You Were Human.
    """, 5)

        story("""
    Humanity Would Still Make Mistakes.

    There Would Still Be Conflict.

    There Would Still Be Fear.

    There Would Still Be Things Worth Fighting For.
    """, 5)

        story("""
    But None Of That Meant Humanity Had To Give Up.
    """, 4)

        story("""
    The World Had Been Given A Choice.

    And Humanity Had Chosen To Live.
    """, 5)


        story("""
    The Sun Began To Rise Over The Horizon.
    """, 4)

        story("""
    The First Light Of Morning Slowly Covered The Cities.

    The Streets Were Still Filled With Voices.

    Laughter.

    Tears.

    Celebration.

    For The First Time...

    The World Was Looking At The Same Sky
    For The Same Reason.
    """, 5)

        story("""
    You Stood Alone On The Battlefield.

    The Wind Moved Through The Empty Ground.

    There Was Nothing Left To Fight.
    """, 4)

        story("""
    You Looked At The Sky.

    The Same Sky That Had Watched You Enter The Selection.

    The Same Sky That Had Witnessed Every Battle.

    The Same Sky That Had Once Felt Like The End Of Everything.
    """, 5)

        story("""
    But Now...

    It Was Quiet.
    """, 3)

        story("""
    And Somehow...

    That Silence Felt Different.
    """, 4)

        story("""
    You Slowly Lowered Your Weapon.
    """, 3)

        story("""
    You Had Not Become Stronger Than Humanity.

    You Had Not Become Its Greatest Warrior.

    You Had Simply Refused To Stop Choosing.
    """, 5)

        story("""
    And Perhaps...

    That Was Enough.
    """, 4)

        story("""
    Humanity Would Continue.

    It Would Make Mistakes.

    It Would Lose.

    It Would Love.

    It Would Fight.

    It Would Build.

    It Would Break.

    And Then...

    It Would Try Again.
    """, 6)

        story("""
    Because Humanity Was Never Promised A Perfect Future.
    """, 4)

        story("""
    It Was Only Given The Chance To Have One.
    """, 5)

        story("""
    And This Time...

    It Chose To Take It.
    """, 5)

        story("""
    The Morning Light Reached The Battlefield.
    """, 4)

        story("""
    You Took One Last Look At The Sky.

    Then You Turned Away...

    And Walked Toward The Light.
    """, 6)

        print("\n" + "=" * 50)
        type_text("                 THE END", 0.2)
        print("=" * 50)
        time.sleep(5)    
        if isinstance(player, Warrior):
            warrior_win = True
            print("----------------------------------------------------------------")            
            print("\n🏆 You completed the game as a Warrior!")
            print("Complete The Game With All 3 Classes To Unlock A Secret Ending!")
            print("----------------------------------------------------------------")            
        elif isinstance(player, Tank):
            tank_win = True
            print("----------------------------------------------------------------")
            print("\n🏆 You completed the game as a Tank!")
            print("Complete The Game With All 3 Classes To Unlock A Secret Ending!")
            print("----------------------------------------------------------------")            
        elif isinstance(player, Assassin):
            assassin_win = True
            print("----------------------------------------------------------------")            
            print("\n🏆 You completed the game as an Assassin!")
            print("Complete The Game With All 3 Classes To Unlock A Secret Ending!")
            print("----------------------------------------------------------------")            

    Chapter1()
    Chapter2()
    Chapter3()
    Chapter4()
    Chapter5()
