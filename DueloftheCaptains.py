import random
from Player_class import Player
from Enemy_class import Enemy

print("[DUEL OF THE CAPTAINS]\n\nWelcome to the seven seas! All the glory and gold in the world just a voyage away!")
print("But you aren't alone in these waters...\nAnother frigate holding similar ambitions closes in on your location.")
print("The ocean isn't big enough for the two of you to coexist, and the other crew knows it.")
action=None
player_action = Player(action)
enemy_decision = Enemy(0)

while True:
    print("\nYour health:",str(player_action.health) + ". Cannons loaded?:", str(player_action.loaded) + ". Bowsprit intact?:",  str(player_action.bowsprit))
    print("Enemy health:", str(enemy_decision.health) + ". Enemy cannons loaded?:", str(enemy_decision.loaded) + ". Enemy bowsprit intact?:", (enemy_decision.bowsprit))
    print("You have 5 options:\n(1) Fire your cannons\n(2) Reload your cannons\n(3) Evade an attack\n(4) Charge your ship into the enemy\n(5) Escape/Quit")
    player_action.action = input()
    enemy_decision.decision = random.randint(1,4)
    player_action.turn()
    enemy_decision.enemy_turn()
    if player_action.action == "1":
        if enemy_decision.decision != 3:
            print("Your attack landed! Enemy has taken 20 damage!")
            enemy_decision.health -= 20
        elif player_action.loaded == False:
            print("You need to reload your cannons first!")
            pass
    if player_action.action == "4":
        if enemy_decision.decision != 3:
            print("You crashed into the enemy ship!!! Enemy has taken 60 damage, but you've lost your evade option and taken 20 damage!")
            enemy_decision.health -= 60
            player_action.health -= 20
            player_action.bowsprit == False
        else:
            pass
    if enemy_decision.decision == 1:
        if player_action.action != "3" and enemy_decision.loaded == True:
            print("The enemy's attack landed! You've taken 20 damage!")
            player_action.health -= 20
        else:
            pass
    if enemy_decision.decision == 4:
        if player_action.action != "3" and enemy_decision.bowsprit == True:
            print("The enemy crashed into your ship!!! You've taken 60 damage, but the enemy has lost their ability to evade and took 20 damage!")
    if player_action.action == "5":
        break
    if player_action.health <= 0 and enemy_decision.health > 0:
        print("\nYou've lost all your health! Abandon ship!!!")
        print("The enemy survived with", enemy_decision.health, "left.")
        print("\n[GAME OVER]")
        break
    if player_action.health <= 0 and enemy_decision.health <= 0:
        print("\nBoth ships lost all their health! Stalemate!!!")
        print("\nGAME OVER")
        break
    elif player_action.health > 0 and enemy_decision.health <= 0:
        print("\nThe enemy lost all their health! Cheers to the captain!!!")
        print("You survived with", player_action.health, "left.")
        print("\nYOU WIN")
        break
    
          
    
