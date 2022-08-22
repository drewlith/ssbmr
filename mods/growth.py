# Random Growth mod by drewlith.
# Magnitude: Intensity of the randomization
import melee
from random import randint as rng

def randomize(attack, magnitude):
    if attack.balance:
        growth = rng(2,attack.strength+magnitude+2)*15
    else:
        growth = rng(0,120+magnitude)
    for hb in attack.hitboxes:
        hb.set_growth(growth)

def start_mod(magnitude):
    for fighter in melee.fighters: # Normal Attacks
        for attack in fighter.attacks:
            if not attack.shuffled:
                randomize(attack, magnitude)
