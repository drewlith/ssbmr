# Random Base Knockback mod by drewlith.
# Magnitude: Intensity of the randomization
import melee, random
from util import percent_chance
from random import randint as rng

def randomize(attack, magnitude):
    if attack.balance:
        base = rng(0,attack.strength+magnitude)*5
    else:
        base = rng(0,100+magnitude)
    for hb in attack.hitboxes:
        hb.set_base(base)

def start_mod(magnitude):
    for fighter in melee.fighters: # Normal Attacks
        for attack in fighter.attacks:
            if not attack.shuffled:
                randomize(attack, magnitude)
