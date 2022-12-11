import melee
from util import percent_chance, get_flag_params
from random import randint as rng
from random import uniform as rng_float

def randomize_element(attack, percent, inclusions):
    if attack.vanilla:
        return
    if len(inclusions) == 0:
        return
    element = inclusions[rng(0,len(inclusions)-1)]
    if percent_chance(percent):
        for hb in attack.hitboxes:
            hb.set_element(element)

def randomize_throw_element(throw, percent, inclusions):
    if throw.vanilla:
        return
    if len(inclusions) == 0:
        return
    element = inclusions[rng(0,len(inclusions)-1)]
    if percent_chance(percent):
        throw.set_element(element)
    
def start_mod(flags):
    inclusions = []
    throw_inclusions = []
    if "-element_normal" in flags:
        inclusions.append(0)
        throw_inclusions.append(0)
    if "-element_fire" in flags:
        inclusions.append(1)
        throw_inclusions.append(1)
    if "-element_electric" in flags:
        inclusions.append(2)
        throw_inclusions.append(2)
    if "-element_slash" in flags:
        inclusions.append(3)
    if "-element_coin" in flags:
        inclusions.append(4)
    if "-element_ice" in flags:
        inclusions.append(5)
        throw_inclusions.append(3)
    if "-element_sleep" in flags:
        inclusions.append(6)
        inclusions.append(7)
    if "-element_ground" in flags:
        inclusions.append(9)
    if "-element_cape" in flags:
        inclusions.append(10)
    if "-element_disable" in flags:
        inclusions.append(12)
    if "-element_dark" in flags:
        inclusions.append(13)
        throw_inclusions.append(4)
    if "-element_screw_attack" in flags:
        inclusions.append(14)
    if "-element_flower" in flags:
        inclusions.append(15)
    if "-element_percent" in flags:
        percent = get_flag_params(flags, "-element_percent")[0]
        for fighter in melee.fighters:
            for attack in fighter.attacks:
                randomize_element(attack, percent, inclusions)
            for throw in fighter.throws:
                randomize_throw_element(throw, percent, throw_inclusions)
