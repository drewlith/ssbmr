# Random size Knockback mod by drewlith.
# Magnitude: Intensity of the randomization
import melee
from random import randint as rng

def randomize(attack, magnitude):
    size = rng(3,25+magnitude)*100
    for hb in attack.hitboxes:
        hb.set_size(size)

def start_mod(magnitude):
    for fighter in melee.fighters: # Normal Attacks
        for attack in fighter.attacks:
            if not attack.shuffled:
                randomize(attack, magnitude)
