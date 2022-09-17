# Random Damage mod by drewlith.
# Magnitude: How intense the randomization is.
import melee
from util import percent_chance
from random import randint as rng
    
def randomize(attack, magnitude):
    if attack.balance:
        damage = rng(attack.strength // 2 + magnitude // 2 + 2, attack.strength + magnitude + 2)
    else:
        damage = rng(0,15+magnitude)
    if "Devastating" in attack.type:
        damage += rng(4,6 + magnitude // 2)
    if "Smash" in attack.type:
        damage += rng(2,4)
    if "Aerial" in attack.type:
        damage += rng(1,2)
    if "Projectile" in attack.type:
        if damage > attack.strength * 2:
            damage = attack.strength * 2
    if "Multi" in attack.type:
        if damage > 4:
            damage = 4
    if damage < 1:
        damage = 1
    for hb in attack.hitboxes:
        hb.set_damage(damage)

def start_mod(magnitude):
    for fighter in melee.fighters: # Normal Attacks
        for attack in fighter.attacks:
            if not attack.shuffled:
                randomize(attack, magnitude)
