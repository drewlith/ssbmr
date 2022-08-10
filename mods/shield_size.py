import melee, random
from util import percent_chance

def randomize(fighter, magnitude, mode = 0):
    if mode == 0: # Bigger or smaller
        fighter.set_shield_size(random.uniform(fighter.get_shield_size()-magnitude,
                                           fighter.get_shield_size()+magnitude))
    if mode == 1: # Bigger only
        fighter.set_shield_size(random.uniform(fighter.get_shield_size(),
                                           fighter.get_shield_size()+magnitude))
    if mode == 2: # Smaller only
        fighter.set_shield_size(random.uniform(fighter.get_shield_size()-magnitude,
                                           fighter.get_shield_size()))

def start_mod(magnitude, mode = 0):
    for fighter in melee.fighters:
        if fighter.properties_offset <= 0:
            return
        randomize(fighter, magnitude, mode)
