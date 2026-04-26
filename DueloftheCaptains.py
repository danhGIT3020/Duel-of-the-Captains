import random
from Player_class import Player
from Enemy_class import Enemy

print("[DUEL OF THE CAPTAINS]\n\nWelcome to the seven seas! All the glory and gold in the world just a voyage away!")
print("But you aren't alone in these waters...\nAnother frigate holding similar ambitions closes in on your location.")
print("The ocean isn't big enough for the two of you to coexist, and the other crew knows it.")

player_action = Player("")
enemy_decision = Enemy(0)
while True:
     print("\nYour health:",str(player_action.health) + ". Cannons loaded?:", str(player_action.loaded) + ". Bowsprit intact?:",  str(player_action.bowsprit))
     print("Enemy health:", str(enemy_decision.health) + ". Enemy cannons loaded?:", str(enemy_decision.loaded) + ". Enemy bowsprit intact?:", (enemy_decision.bowsprit))
     print("You have 5 options:\n(1) Fire your cannons\n(2) Reload your cannons\n(3) Evade an attack\n(4) Charge your ship into the enemy\n(5) Escape/Quit")
     action = input()
     player_action = Player(action)
     enemy_decision = Enemy(random.randint(1,4))
     if player_action.turn() == "1":
        if enemy_decision.decision() != 3:
            print("Your attack landed! Enemy has taken 20 damage!")
            enemy_decision.health -= 20
        else:
            pass
