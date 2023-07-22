from classes.location import Location
from data.descriptions import descriptions
from data.inventory import inventory
from classes.enemy import Enemy
import classes.Item as Item
from classes.NPC import Npc
import random as r

enemies = ["Dragur", "Skeever", "Dragon", "Troll", "Katie", "AirFrance", "Monster"]

weapons = ["Sword", "Dagger", "RPG"]

directions = ["north", "east", "west", "south", "secret_tunnel"]

def init_locations():
    locations = []
    for i in range(r.randint(4, len(descriptions))):
        description_key=r.choice(list(descriptions.keys()))
        description=descriptions[description_key]
        del descriptions[description_key]
        locations.append(Location(
            description = description,
            inventory = [Item.Weapon(r.choice(weapons), 50, 1, r.randint(5,50)) for _ in range(r.randrange(0,3))],
            enemies = [Enemy(r.choice(enemies), 5, 2, "") for i in range(r.randrange(0,10))]
        ))
    for loc in locations:
        
        for _ in range(r.randrange(1, len(directions))):
            used_locs = [loc]
            used_dirs = []
            direction = r.choice([d for d in directions if d not in used_dirs])
            destination = r.choice([l for l in locations if l not in used_locs])
            loc.addDirection(direction, destination)
            used_locs.append(destination)
            used_dirs.append(direction)
            
    starting_loc = r.choice(locations)
    return starting_loc 
#Create location objetcs

    # hut = Location(
    #     description = descriptions["hut"],
    #     inventory   = inventory["hut"], 
    #     enemies     =[
    #         Enemy("Draugr", 20, 8, Item.Item("Draugr Claws", 35, 1)),
    #         Enemy("Skeever", 5, 2, Item.Item("Tail", 10, 1)),
    #         Enemy("Draugr", 30, 8, Item.Item("Draugr head", 40, 1))
    #         ]
    #     )
    # riften = Location(
    #     description = descriptions["riften"],
    #     inventory   = inventory["riften"]
    #     )

    # riften_swamp = Location(
    #     description = descriptions["riften_swamp"]
    #     )

    # secret_cave = Location(
    #     description = descriptions["secret_cave"],
    #     inventory   = inventory["cave"],
    #     enemies=[
    #         Enemy("Draugr", 20, 8, "Draugr Head"),
    #         Enemy("Skeever", 5, 2, "Skeever Tail")
    #         ]
    #     )

    # oasis = Location(
    #     description = descriptions["oasis"],
    #     inventory   =  inventory["oasis"],
    #     enemies     = [
    #         Enemy("Troll", 50, 12, "Troll Fat")
    #         ]
    #     )

    # church = Location(
    #     description = descriptions["church"],
    #     inventory   = inventory["church"],
    #     npcs        = [Npc("Priest", 10, None, 5, 6)]
    #     )

    # shop = Location(
    #     description = descriptions["shop"],
    #     inventory   = inventory["shop"]
    #     )

    # church_vault = Location(
    #     description = descriptions["church_vault"],
    #     inventory   = inventory["church_vault"],
    #     enemies     = [
    #         Enemy("draugr", 20, 8, "draugr teeth")
    #         ]
    #     )


#Set paths that can be taken from each location 

    # hut.setDirections({
    #     "outside": riften_swamp
    #     })

    # riften_swamp.setDirections({
    #     "inside": hut,
    #     "riften": riften,
    #     "cave": secret_cave
    #     })

    # riften.setDirections({
    #     "swamp": riften_swamp,
    #     "church": church,
    #     "shop": shop
    #     })

    # secret_cave.setDirections({
    #     "outside": riften_swamp,
    #     "inside": oasis
    #     })

    # oasis.setDirections({
    #     "outside": secret_cave,
    #     "up": church
    #     })

    # church.setDirections({
    #     "down": oasis,
    #     "outside": riften,
    #     "inside": church_vault
    #      })

    # shop.setDirections({
    #     "outside": riften
    #     })

    # church_vault.setDirections({
    #     "outside" : church
    #     })

    # starting_loc = hut
    # return starting_loc 