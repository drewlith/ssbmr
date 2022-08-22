# Shuffle mod by drewlith. Run after -balance and -vanilla flag.
# Percent: Percent of moves to shuffle
import melee, copy
from util import percent_chance
from random import randint as rng

def shuffle(attack):
    temp = copy.deepcopy(attack)
    if attack.balance:
        if attack.type < 6:
            tier = melee.attack_tiers[attack.strength]
        else:
            tier = melee.item_tiers[attack.strength]
        target = tier[rng(0,len(tier)-1)]
    else:
        if attack.type < 6:
            target = melee.attacks[rng(0,len(melee.attacks)-1)]
        else:
            target = melee.items[rng(0,len(melee.items)-1)]
    if target.shuffled:
        return
    for i in range(len(attack.hitboxes)-1):
        if i > len(target.hitboxes)-1:
            hb_id = 0
        else:
            hb_id = i
        attack.hitboxes[i].set_damage(target.hitboxes[hb_id].get_damage())
        attack.hitboxes[i].set_angle(target.hitboxes[hb_id].get_angle())
        attack.hitboxes[i].set_base(target.hitboxes[hb_id].get_base())
        attack.hitboxes[i].set_growth(target.hitboxes[hb_id].get_growth())
        attack.hitboxes[i].set_set(target.hitboxes[hb_id].get_set())
        attack.hitboxes[i].set_element(target.hitboxes[hb_id].get_element())
        attack.hitboxes[i].set_size(target.hitboxes[hb_id].get_size())
        attack.hitboxes[i].set_sfx(target.hitboxes[hb_id].get_sfx())
        attack.hitboxes[i].set_shield(target.hitboxes[hb_id].get_shield())
    for i in range(len(target.hitboxes)-1):
        if i > len(temp.hitboxes)-1:
            hb_id = 0
        else:
            hb_id = i
        target.hitboxes[i].set_damage(temp.hitboxes[hb_id].get_damage())
        target.hitboxes[i].set_angle(temp.hitboxes[hb_id].get_angle())
        target.hitboxes[i].set_base(temp.hitboxes[hb_id].get_base())
        target.hitboxes[i].set_growth(temp.hitboxes[hb_id].get_growth())
        target.hitboxes[i].set_set(temp.hitboxes[hb_id].get_set())
        target.hitboxes[i].set_element(temp.hitboxes[hb_id].get_element())
        target.hitboxes[i].set_size(temp.hitboxes[hb_id].get_size())
        target.hitboxes[i].set_sfx(temp.hitboxes[hb_id].get_sfx())
        target.hitboxes[i].set_shield(temp.hitboxes[hb_id].get_shield())
    attack.shuffled = True
    target.shuffled = True
    temp = attack.shuffled_with
    attack.shuffled_with = target.shuffled_with
    target.shuffled_with = temp

def shuffle_throw(throw):
    temp = copy.deepcopy(throw)
    target = melee.throws[rng(0,len(melee.throws)-1)]
    if target.shuffled:
        return
    throw.set_damage(target.get_damage())
    throw.set_angle(target.get_angle())
    throw.set_base(target.get_base())
    throw.set_growth(target.get_growth())
    throw.set_set(target.get_set())
    throw.set_element(target.get_element())

    target.set_damage(temp.get_damage())
    target.set_angle(temp.get_angle())
    target.set_base(temp.get_base())
    target.set_growth(temp.get_growth())
    target.set_set(temp.get_set())
    target.set_element(temp.get_element())

    throw.shuffled = True
    target.shuffled = True
    temp = throw.shuffled_with
    throw.shuffled_with = target.shuffled_with
    target.shuffled_with = temp

def start_mod(percent):
    for attack in melee.attacks:
        if percent_chance(percent):
            shuffle(attack)
    for item in melee.items:
        if percent_chance(percent):
            shuffle(item)
    for throw in melee.throws:
        if percent_chance(percent):
            shuffle_throw(throw)
        
