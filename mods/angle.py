# Random Angle mod by drewlith.
import melee, random
from util import percent_chance
from random import randint as rng

def randomize(attack):
    if attack.balance:
        if percent_chance(80): # Forward Angles
            angle = rng(2,9)*10
        elif percent_chance(50): # Sakurai Angle
            angle = 361
        elif percent_chance(50): # Meteor
            angle = 290
        elif percent_chance(50): # Spike
            angle = 270
        else: # Random
            angle = rng(0,362)
    else:
        angle = rng(0,362)
    for hb in attack.hitboxes:
        hb.set_angle(angle)

def start_mod():
    for fighter in melee.fighters: # Normal Attacks
        for attack in fighter.attacks:
            if not attack.shuffled:
                randomize(attack)
