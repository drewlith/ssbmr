# Random Base Knockback mod by drewlith.
# Magnitude: Intensity of the randomization
import melee, random
from util import percent_chance
from random import randint as rng

def randomize(attack, magnitude):
    if attack.balance:
        base = rng(magnitude,attack.strength+magnitude)*2
    else:
        base = rng(magnitude,20+magnitude*2)
    if "Smash" in attack.type:
        base += rng(1,2+magnitude)*10
        if base < 30:
            base = 30
    if "Laser" in attack.type:
        base = 0
    for hb in attack.hitboxes:
        hb.set_base(base)

def start_mod(magnitude):
    for fighter in melee.fighters: # Normal Attacks
        for attack in fighter.attacks:
            if not attack.shuffled:
                randomize(attack, magnitude)
                
