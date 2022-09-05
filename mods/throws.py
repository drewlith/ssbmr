# Random/Shuffled Throws mod by drewlith.
# Shuffle Percent: Amount of attacks to shuffle (as opposed to randomize)
import melee
from util import percent_chance
from random import randint as rng

def randomize(throw, magnitude):
    throw.set_damage(rng(3+magnitude,9+magnitude)) # Damage
    
    # Angle determination
    if percent_chance(5): # Sakurai Angle
        angle = 361
    elif percent_chance(60): # Send Forward
        angle = rng(8,14)*5
    elif percent_chance(70): # Send Backward
        angle = rng(20,28)*5
    elif percent_chance(90): # Send Straight Up
        angle = rng(16,18)*5
    else:
        angle = rng(0,360) # Randomize
    
    throw.set_angle(angle)
    throw.set_growth(rng(5,9+magnitude)*10)
    throw.set_base(rng(4,6+magnitude)*8)
    throw.set_set(0)
    throw.set_element(rng(0,4))

    if throw.get_growth() > 100 and throw.get_base() > 30:
        throw.set_base(30)

def start_mod(magnitude):
    for throw in melee.throws:
        if not throw.shuffled:
            randomize(throw, magnitude)
        

        
