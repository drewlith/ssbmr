# Random Set Knockback mod by drewlith.
# Magnitude: Intensity of the randomization and chance of it being applied
import melee, random
from util import percent_chance
from random import randint as rng

def randomize(attack, magnitude):
    if not percent_chance(magnitude):
        return
    if attack.balance:
        wdsk = rng(0,attack.strength+magnitude)*6
    else:
        wdsk = rng(0,40+magnitude)
    for hb in attack.hitboxes:
        hb.set_set(wdsk)

def start_mod(magnitude):
    for fighter in melee.fighters: # Normal Attacks
        for attack in fighter.attacks:
            if not attack.shuffled:
                randomize(attack, magnitude)
