# Random Weight Mod by drewlith
# Mode 0 = heavier or lighter, 1 = heavier only, 2 = lighter only
import melee, random
from util import percent_chance

def randomize(fighter, magnitude, mode = 0):
    if mode == 0:
        fighter.set_weight(random.uniform(fighter.get_weight() - magnitude*0.01,
                                          fighter.get_weight() + magnitude*0.01))
    if mode == 1:
        fighter.set_weight(random.uniform(fighter.get_weight(),
                                          fighter.get_weight() + magnitude*0.01))
    if mode == 2:
        fighter.set_weight(random.uniform(fighter.get_weight() - magnitude*0.01,
                                          fighter.get_weight()))

def start_mod(magnitude, mode):
    for fighter in melee.fighters:
        if fighter.properties_offset <= 0:
            return
        randomize(fighter)
        
        
