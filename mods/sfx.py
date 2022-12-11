import melee
from util import percent_chance
from random import randint as rng

def start_mod():
    for fighter in melee.fighters:
        for sound in fighter.sounds:
            target = fighter.sounds[rng(0, len(fighter.sounds)-1)]
            temp = sound.data
            sound.data = target.data
            target.data = temp
