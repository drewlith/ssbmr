# Shuffle mod by drewlith. Run after -balance and -vanilla flag.
# Percent: Percent of moves to shuffle
import melee
from util import percent_chance
from random import randint as rng

def shuffle(attack):
    if attack.balance:
        if "Item" not in attack.type:
            tier = melee.attack_tiers[attack.strength]
        else:
            tier = melee.item_tiers[attack.strength]
        target = tier[rng(0,len(tier)-1)]
    else:
        if "Item" not in attack.type:
            target = melee.attacks[rng(0,len(melee.attacks)-1)]
        else:
            target = melee.items[rng(0,len(melee.items)-1)]
            
    old = []
    old.append(attack.hitboxes[0].get_damage())
    old.append(attack.hitboxes[0].get_angle())
    old.append(attack.hitboxes[0].get_base())
    old.append(attack.hitboxes[0].get_growth())
    old.append(attack.hitboxes[0].get_set())
    old.append(attack.hitboxes[0].get_element())
    old.append(attack.hitboxes[0].get_size())
    old.append(attack.hitboxes[0].get_sfx())
    old.append(attack.hitboxes[0].get_shield())
    
    for hb in attack.hitboxes:
        hb.set_damage(target.hitboxes[0].get_damage())
        hb.set_angle(target.hitboxes[0].get_angle())
        hb.set_base(target.hitboxes[0].get_base())
        hb.set_growth(target.hitboxes[0].get_growth())
        hb.set_set(target.hitboxes[0].get_set())
        hb.set_element(target.hitboxes[0].get_element())
        if not attack.balance:
            hb.set_size(target.hitboxes[0].get_size())
        hb.set_sfx(target.hitboxes[0].get_sfx())
        hb.set_shield(target.hitboxes[0].get_shield())
        
    for hb in target.hitboxes:
        hb.set_damage(old[0])
        hb.set_angle(old[1])
        hb.set_base(old[2])
        hb.set_growth(old[3])
        hb.set_set(old[4])
        hb.set_element(old[5])
        if not attack.balance:
            hb.set_size(old[6])
        hb.set_sfx(old[7])
        hb.set_shield(old[8])
        
    temp = attack.shuffled_with
    attack.shuffled_with = target.shuffled_with
    target.shuffled_with = temp

    attack.shuffled = True
    target.shuffled = True

def shuffle_throw(throw):
    target = melee.throws[rng(0,len(melee.throws)-1)]
    if target.shuffled:
        return
    old = []
    old.append(throw.get_damage())
    old.append(throw.get_base())
    old.append(throw.get_growth())
    old.append(throw.get_set())
    old.append(throw.get_element())
    
    throw.set_damage(target.get_damage())
    angle = throw.get_angle()
    if angle != 361:
        angle = rng(angle-15, angle+15)
        if angle < 0:
            angle = 360 + angle
        if angle > 360:
            angle = angle - 360
        throw.set_angle(angle)
    throw.set_base(target.get_base())
    throw.set_growth(target.get_growth())
    throw.set_set(target.get_set())
    throw.set_element(target.get_element())

    target.set_damage(old[0])
    angle = target.get_angle()
    if angle != 361:
        angle = rng(angle-15, angle+15)
        if angle < 0:
            angle = 360 + angle
        if angle > 360:
            angle = angle - 360
        target.set_angle(angle)
    target.set_base(old[1])
    target.set_growth(old[2])
    target.set_set(old[3])
    target.set_element(old[4])

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
        
