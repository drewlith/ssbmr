# Random Element mod by drewlith.
# Percent: Amount of attacks to give a random element.
import melee, random
from util import percent_chance

elements = ["Normal", "Fire", "Electric", "Slash", "Coin", "Ice", "Sleep", "Sleep",
            "Grounded", "Grounded", "Cape", "None", "Disable", "Dark", "Screw Attack",
            "Flower", "None"]

def randomize(attack): 
    element = random.randint(0,15)
    if element == 12 or element == 11: element = 0 # These elements will make the hitbox useless
    if element == 6 or element == 7: element = 12 # Turn sleep into disable, better balanced
    if element == 14: element = 0 # No Screw Attack!!!
    for hb in attack.hitboxes:
        hb.set_element(element)

def start_mod(percent):
    for tier in melee.attack_tiers: # Normal Attacks
        for attack in tier:
            if percent_chance(percent):
                randomize(attack)
                attack.notes.append("Element randomized to " +
                                elements[attack.hitboxes[0].get_element()] + ".")
                    
    for tier in melee.item_tiers: # Items
        for item in tier:
            if percent_chance(percent):
                randomize(item)
                item.notes.append("Element randomized to " +
                              elements[attack.hitboxes[0].get_element()] + ".")
