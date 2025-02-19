import classes.Item as Item





def grab(player, words):
    if " ".join(words[1:]).lower() in player.current_location.getInventoryLower():
        player.addItemToInventory(player.current_location.grabItem(" ".join(words[1:]).lower()))
        print(f"{' '.join(words[1:])} taken")
    else:
        print("No item in area")


 # finish off                        
def die(player):
    player.health = 0

    # #if you have a blade:
    #     time.sleep(1)
    #     print("You pulled your balde out and held it solemly in your hands...")
    #     time.sleep(2.5)
    #     print("You got your knees ready to slice your stomach with the balde meant for others rather than your own...")
    #     time.sleep(2.9)
    #     print("You sliced your stomach open, blood rushing from your wound...")
    #     time.sleep(2.8)
    #     print("You fall to the ground and perish, but only with one regret...")
    #     time.sleep(3)
    #     print("You left the stove on.")

    # else:
    #     print("You picked up a stone on the ground")    
        
        
def attack(player, words):
    if len(words) < 2:
        print("attack what bro")
        return
    
    target = None
    #checking if enemy is there
    for enemy in player.current_location.enemies:
        if enemy.name.lower() == words[1].lower():
            target = enemy
            break     
    
    damage = 2
    
    if len(words) > 3 and words[2] == "with":
        found_weapon = False

        for item in player.inventory:
            if isinstance(item, Item.Weapon) and item.name.lower() == words[3]:
                damage = item.damage
                found_weapon = True
                break

        if not found_weapon:
            print(f"You don't have {words[3]}")
                

    if target != None:
        target.takeDamage(damage)
        if target.health <= 0:
            player.current_location.enemies.remove(target)
            player.current_location.inventory.append(target.inventory)
            
    else: 
        print(f"No enemy named {words[1]}")
        print("You flung the air with style and destroyed the air particles.")
    
def heal(player, words):
    print("doin a heal")
    
def look(player, words):

    if len(words) > 2 and words[1] == "at":
        player.lookAtItem(" ".join(words[2:]))

    else:    
        #Location description
        print(f"\n{player.current_location.description}")
        
        #Items
        print("\nItems:")
        if len(player.current_location.inventory) > 0:
            for item in player.current_location.inventory:
                print(f"- {item.name}")
        else:
            print("No items can be seen...")
        
        #Enemies
        
        if len(player.current_location.enemies) > 0:
            print("\nEnemies:")
            for enemy in player.current_location.enemies:
                enemy.toString()

        if len(player.current_location.npc) > 0:
            print("People in area:")
            for i in player.current_location.npc:
                i.toString()
        
def go(player, words):
    direction = words[1]
    print(direction)
    if direction in player.current_location.directions.keys():
        player.current_location = player.current_location.directions[direction]
        look(player, words)
    
    else:
        print("That is not a location you can go to, try these instead:")
        print(list(player.current_location.directions.keys()))
            
       
def getDirections(player):
    print(list(player.current_location.directions.keys()))
    
def helpList(player):
    player.helpFunction()