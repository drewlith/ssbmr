# Random Damage mod by drewlith.
# Magnitude: How intense the randomization is.
import melee
from util import percent_chance
from random import randint as rng
    
def randomize(attack, magnitude):
    if attack.balance:
        damage = rng(attack.strength,attack.strength*2+magnitude)
    else:
        damage = rng(0,18+magnitude)
    for hb in attack.hitboxes:
        hb.set_damage(damage)

def start_mod(magnitude):
    for fighter in melee.fighters: # Normal Attacks
        for attack in fighter.attacks:
            if not attack.shuffled:
                randomize(attack, magnitude)
