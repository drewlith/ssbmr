import melee, random
from util import percent_chance

def randomize(fighter, magnitude, mode = 0):
    if mode == 0: # Bigger or smaller
        fighter.set_shield_size(random.uniform(fighter.get_shield_size() * (1-(magnitude*0.01)),
                                           fighter.get_shield_size() * (1+(magnitude*0.01))))
    if mode == 1: # Bigger only
        fighter.set_shield_size(random.uniform(fighter.get_shield_size(),
                                           fighter.get_shield_size() * (1+(magnitude*0.01))))
    if mode == 2: # Smaller only
        fighter.set_shield_size(random.uniform(fighter.get_shield_size() * (1-(magnitude*0.01)),
                                           fighter.get_shield_size()))
    if fighter.get_shield_size() <= 0:
        fighter.set_shield_size(float(1))
    if fighter.get_shield_size() > 40:
        fighter.set_shield_size(float(40))

def start_mod(magnitude, mode = 0):
    for fighter in melee.fighters:
        if fighter.properties_offset <= 0:
            return
        randomize(fighter, magnitude, mode)
