# Random Growth mod by drewlith.
# Magnitude: Intensity of the randomization
import melee
from random import randint as rng

def randomize(attack, magnitude):
    if attack.balance:
        growth = rng(magnitude,attack.strength+magnitude)*10
    else:
        growth = rng(0,10+magnitude)*10
    if "Smash" in attack.type:
        growth += rng(2,3)*10
        if growth < 80:
            growth = 80
    if "Aerial" in attack.type:
        growth += 10
        if growth < 60:
            growth = 60
    if "Laser" in attack.type:
        growth = 0
    for hb in attack.hitboxes:
        hb.set_growth(growth)

def start_mod(magnitude):
    for fighter in melee.fighters: # Normal Attacks
        for attack in fighter.attacks:
            if not attack.shuffled:
                randomize(attack, magnitude)
