# Random SFX mod by drewlith.
import melee
from util import percent_chance
from random import randint as rng

def randomize(attack): 
    sfx = [65, 70, 66, 34, 67, 35, 72, 40, 5, 33, 69, 1, 2, 38, 39, 37,
           18, 76, 8, 168, 71, 36, 42, 10, 3, 74, 6, 167, 24, 17, 11,
           135, 68, 7, 146, 44, 12]
    # These sfx don't crash on console, there may be more.
    sound = rng(0,len(sfx)-1)
    for hb in attack.hitboxes:
        hb.set_sfx(sfx[sound])

def start_mod():
    for tier in melee.attack_tiers: # Normal Attacks
        for attack in tier:
            if not attack.shuffled:
                randomize(attack)
                    
    for tier in melee.item_tiers: # Items
        for item in tier:
            if not attack.shuffled:
                randomize(item)
