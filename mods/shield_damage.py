# Random Shield damage mod by drewlith.
# Magnitude: Intensity of the randomization
import melee, random
from util import percent_chance
from random import randint as rng

def randomize(attack, magnitude):
    if attack.balance:
        damage = rng(0,attack.strength+magnitude)*4
    else:
        damage = rng(0,50+magnitude)
    for hb in attack.hitboxes:
        hb.set_shield(damage)

def start_mod(magnitude):
    for fighter in melee.fighters: # Normal Attacks
        for attack in fighter.attacks:
            if not attack.shuffled:
                randomize(attack, magnitude)
