# Random Angle mod by drewlith.
import melee, random
from util import percent_chance
from random import randint as rng

def randomize(attack):
    if attack.balance:
        if percent_chance(75): # Forward/Upwards Angles
            angle = rng(2,9)*10
        elif percent_chance(75): # Sakurai Angle
            angle = 361
        elif percent_chance(20): # Meteor
            angle = 290
        elif percent_chance(20): # Spike
            angle = 270
        else: # Random
            angle = rng(0,362)
        if "Spike" in attack.type:
            if percent_chance(80):
                angle = rng(27,29)*10
        if "Aerial" in attack.type:
            if percent_chance(80):
                angle = 361
    else:
        angle = rng(0,362)
    for hb in attack.hitboxes:
        hb.set_angle(angle)

def deviate(attack):
    angle = attack.hitboxes[0].get_angle()
    if angle == 361:
        return
    angle = rng(angle - 15, angle + 15)
    if angle < 0:
        angle = 360 + angle
    if angle > 360:
        angle = angle - 360
    for hb in attack.hitboxes:
        hb.set_angle(angle)

def all_meteor(attack):
    for hb in attack.hitboxes:
        hb.set_angle(290)

def start_mod(mode = 0):
    for fighter in melee.fighters: # Normal Attacks
        for attack in fighter.attacks:
            if not attack.shuffled:
                if mode == 0:
                    randomize(attack)
                if mode == 1:
                    deviate(attack)
                if mode == 2:
                    all_meteor(attack)
                    
