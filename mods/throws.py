# Random/Shuffled Throws mod by drewlith.
# Shuffle Percent: Amount of attacks to shuffle (as opposed to randomize)
import melee
from util import percent_chance
from random import randint as rng

def randomize(throw, magnitude):
    throw.set_damage(rng(3+magnitude,9+magnitude)) # Damage
    
    # Angle determination
    if percent_chance(20): # Sakurai Angle
        angle = 361
    elif percent_chance(80): # Send Forward
        angle = rng(2,6)*10
    elif percent_chance(80): # Send Straight Up
        angle = rng(8,9)*10
    else:
        angle = rng(0,360) # Randomize
    
    throw.set_angle(angle)
    throw.set_growth(rng(5+magnitude,12+magnitude)*10)
    throw.set_base(rng(1,5+magnitude)*5)
    throw.set_set(rng(0,2+magnitude)*5)
    throw.set_element(rng(0,4))

def start_mod(magnitude):
    for throw in melee.throws:
        if not throw.shuffled:
            randomize(throw, magnitude)
        

        
