# Random Damage mod by drewlith.
# Magnitude: How intense the randomization is.
import melee
from util import percent_chance
from random import randint as rng
    
def randomize(attack, magnitude):
    if attack.balance:
        damage = rng(magnitude,attack.strength+magnitude)
    else:
        damage = rng(0,15+magnitude)
    if "Devastating" in attack.type:
        damage += rng(2,8+magnitude)
    if "Smash" in attack.type:
        damage += rng(2,5)
    if "Aerial" in attack.type:
        damage += rng(0,2)
    if "Projectile" in attack.type or "Multi" in attack.type or "Throw Hitbox" in attack.type:
        damage = damage // 3
    if damage < 0:
        damage = 0
    for hb in attack.hitboxes:
        hb.set_damage(damage)

def start_mod(magnitude):
    for fighter in melee.fighters: # Normal Attacks
        for attack in fighter.attacks:
            if not attack.shuffled:
                randomize(attack, magnitude)
