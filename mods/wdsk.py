# Random Set Knockback mod by drewlith.
# Magnitude: Intensity of the randomization and chance of it being applied
import melee, random
from util import percent_chance
from random import randint as rng

def randomize(attack, magnitude):
    if not percent_chance(magnitude):
        return
    if attack.balance:
        wdsk = rng(magnitude,attack.strength+magnitude)*5
    else:
        wdsk = rng(magnitude,70+magnitude)
    if "Laser" in attack.type:
        wdsk = 0
    if wdsk > 80:
        wdsk = 80
    for hb in attack.hitboxes:
        hb.set_set(wdsk)

def start_mod(magnitude):
    for fighter in melee.fighters: # Normal Attacks
        for attack in fighter.attacks:
            if not attack.shuffled:
                randomize(attack, magnitude)
