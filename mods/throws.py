# Random/Shuffled Throws mod by drewlith.
# Shuffle Percent: Amount of attacks to shuffle (as opposed to randomize)
import melee
from util import percent_chance
from random import randint as rng

def randomize(throw, magnitude):
    throw.set_damage(rng(3+magnitude,9+magnitude)) # Damage
    
    angle = throw.get_angle()
    if angle != 361:
        angle = rng(angle-15,angle+15)
        if angle < 0:
            angle = 360 + angle
        if angle > 360:
            angle = angle - 360
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
        

        
