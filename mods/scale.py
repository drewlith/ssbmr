# Random Scale mod by drewlith.
import melee, random
from util import percent_chance

def randomize(fighter, magnitude, mode = 0):
    if mode == 0: # Bigger or smaller
        fighter.set_scale(random.uniform(fighter.get_scale() * (1-(magnitude*0.01)),
                                         fighter.get_scale() * (1+(magnitude*0.01))))
    if mode == 1: # Bigger only
        fighter.set_scale(random.uniform(fighter.get_scale(),
                                         fighter.get_scale() * (1+(magnitude*0.01))))
    if mode == 2: # Smaller only
        fighter.set_scale(random.uniform(fighter.get_scale() * (1-(magnitude*0.01)),
                                         fighter.get_scale()))
    if fighter.get_scale() <= 0:
        fighter.set_scale(float(0.1))
        
def start_mod(magnitude, mode = 0):
    for fighter in melee.fighters:
        if fighter.properties_offset <= 0:
            return
        randomize(fighter, magnitude, mode)
        
