# Random Scale mod by drewlith.
import melee, random
from util import percent_chance

def randomize(fighter, magnitude, mode = 0):
    if mode == 0: # Bigger or smaller
        fighter.set_scale(random.uniform(fighter.get_scale() - (magnitude*0.01),
                                         fighter.get_scale() + (magnitude*0.01)))
    if mode == 1: # Bigger only
        fighter.set_scale(random.uniform(fighter.get_scale(),
                                         fighter.get_scale() + (magnitude*0.01)))
    if mode == 2: # Smaller only
        fighter.set_scale(random.uniform(fighter.get_scale() - (magnitude*0.01),
                                         fighter.get_scale()))
def start_mod(magnitude, mode = 0):
    for fighter in melee.fighters:
        if fighter.properties_offset <= 0:
            return
        randomize(fighter, magnitude, mode)
        
