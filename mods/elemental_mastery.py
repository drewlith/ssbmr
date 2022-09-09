# Elemental Mastery mod by drewlith. If an attack has fire, it will
# have increased damage. If an attack has Darkness, it will have increased
# Base knockback. If an attack has Electric, it will do extra shield damage.
# If an attack has Slash, it will have extra knockback growth. If an attack
# has Flower, it's growth will decrease but its base knockback will increase.

import melee, random
from util import percent_chance
from random import randint as rng

def start_mod():
    for attack in melee.attacks:
        for hb in attack.hitboxes:
            if hb.get_element() == 1:
                damage = hb.get_damage()
                damage = damage + 3
                hb.set_damage(damage)
            if hb.get_element() == 2:
                damage = hb.get_shield()
                damage = damage + 6
                hb.set_shield(damage)
            if hb.get_element() == 3:
                growth = hb.get_growth()
                growth = growth + 30
                hb.set_growth(growth)
            if hb.get_element() == 13:
                base = hb.get_base()
                base = base + 20
                hb.set_base(base)
            if hb.get_element() == 15:
                base = hb.get_base()
                base = base + 40
                hb.set_base(base)

                growth = hb.get_growth()
                growth = growth - 70
                if growth < 1:
                    growth = 1
                hb.set_growth(growth)
