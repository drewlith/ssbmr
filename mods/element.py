# Random Element mod by drewlith.
# Percent: Amount of attacks to give a random element.
import melee, random
from util import percent_chance

elements = ["Normal", "Fire", "Electric", "Slash", "Coin", "Ice", "Sleep", "Sleep",
            "BUGGED REPORT TO DREWLITH", "Grounded", "Cape", "None", "Disable", "Dark", "Screw Attack",
            "Flower", "None"]

def randomize(attack): 
    element = random.randint(0,15)
    if element == 8 or element == 11: element = 0 # These elements will make the hitbox useless
    if element == 6 or element == 7: element = 0 # No Sleep
    if element == 14: element = 0 # No Screw Attack
    for hb in attack.hitboxes:
        hb.set_element(element)

def start_mod(percent):
    for fighter in melee.fighters: # Normal Attacks
        for attack in fighter.attacks:
            if not attack.shuffled and percent_chance(percent):
                randomize(attack)
