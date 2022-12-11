import melee
from util import percent_chance, get_flag_params
from random import randint as rng

attacks = []
tiers = [[],[],[],[],[],[],[],[],[],[],[]]
throws = []

def sort_attacks():
    global attacks
    global tiers
    global throws
    for tier in tiers:
        tier.clear()
    attacks.clear()
    for fighter in melee.fighters:
        for attack in fighter.attacks:
            tiers[attack.strength].append(attack)
            attacks.append(attack)
        for throw in fighter.throws:
            throws.append(throw)

def shuffle_hitbox(attack, target):
    if attack.vanilla:
        return
    temp_damage = attack.hitboxes[0].get_damage()
    temp_shield = attack.hitboxes[0].get_shield()
    temp_angle = attack.hitboxes[0].get_angle()
    temp_base = attack.hitboxes[0].get_base()
    temp_growth = attack.hitboxes[0].get_growth()
    temp_set = attack.hitboxes[0].get_set()
    #temp_size = attack.hitboxes[0].get_size()
    temp_element = attack.hitboxes[0].get_element()
    temp_sfx = attack.hitboxes[0].get_sfx()
    for hb in attack.hitboxes:
        hb.set_damage(target.hitboxes[0].get_damage())
        hb.set_shield(target.hitboxes[0].get_shield())
        hb.set_angle(target.hitboxes[0].get_angle())
        hb.set_base(target.hitboxes[0].get_base())
        hb.set_growth(target.hitboxes[0].get_growth())
        hb.set_set(target.hitboxes[0].get_set())
        #hb.set_size(target.hitboxes[0].get_size())
        hb.set_element(target.hitboxes[0].get_element())
        hb.set_sfx(target.hitboxes[0].get_sfx())
    for hb in target.hitboxes:
        hb.set_damage(temp_damage)
        hb.set_shield(temp_shield)
        hb.set_angle(temp_angle)
        hb.set_base(temp_base)
        hb.set_growth(temp_growth)
        hb.set_set(temp_set)
        #hb.set_size(temp_size)
        hb.set_element(temp_element)
        hb.set_sfx(temp_sfx)
    attack.shuffled = True
    target.shuffled = True

def shuffle_throw(throw, target):
    if throw.vanilla:
        return
    temp_damage = throw.get_damage()
    temp_angle = throw.get_angle()
    temp_base = throw.get_base()
    temp_growth = throw.get_growth()
    temp_set = throw.get_set()
    temp_element = throw.get_damage()
    throw.set_damage(target.get_damage())
    throw.set_angle(target.get_angle())
    throw.set_base(target.get_base())
    throw.set_growth(target.get_growth())
    throw.set_set(target.get_set())
    throw.set_element(target.get_element())
    target.set_damage(temp_damage)
    target.set_angle(temp_angle)
    target.set_base(temp_base)
    target.set_growth(temp_growth)
    target.set_set(temp_set)
    target.set_element(temp_element)
    throw.shuffled = True
    target.shuffled = True

def shuffle_attribute_group(fighter, target, group):
    fighter_attributes = fighter.get_attributes_by_group_name(group)
    target_attributes = target.get_attributes_by_group_name(group)
    for i in range(len(fighter_attributes)):
        temp = fighter_attributes[i].get_value()
        fighter_attributes[i].set_value(target_attributes[i].get_value())
        target_attributes[i].set_value(temp)

def shuffle_attribute(fighter, target, name):
    attribute = fighter.get_attribute_by_name(name)
    target_attribute = target.get_attribute_by_name(name)
    temp = attribute.get_value()
    attribute.set_value(target_attribute.get_value())
    target_attribute.set_value(temp)

def start_mod(flags):
    sort_attacks()
    for fighter in melee.fighters:
        if "-shuffle_attacks" in flags:
            percent = get_flag_params(flags, "-shuffle_attacks")[0]
            for attack in fighter.attacks:
                if percent_chance(percent):
                    if attack.balance:
                        tier = tiers[attack.strength]
                        target = tier[rng(0, len(tier)-1)]
                    else:
                        target = attacks[rng(0, len(attacks)-1)]
                    attack.shuffle_target, target.shuffle_target = target.shuffle_target, attack.shuffle_target
                    shuffle_hitbox(attack, target)
        if "-shuffle_throws" in flags: 
            percent = get_flag_params(flags, "-shuffle_throws")[0]        
            for throw in fighter.throws:
                if percent_chance(percent):
                    target = throws[rng(0, len(throws)-1)]
                    throw.shuffle_target, target.shuffle_target = target.shuffle_target, throw.shuffle_target
                    shuffle_throw(throw, target)
        if "-shuffle_attributes" in flags:
            percent = get_flag_params(flags, "-shuffle_attributes")[0]
            if percent_chance(percent):
                target = melee.fighters[rng(0,len(melee.fighters)-1)]
                fighter.shuffle_target, target.shuffle_target = target.shuffle_target, fighter.shuffle_target 
                shuffle_attribute_group(fighter, target, "Walk")
                shuffle_attribute_group(fighter, target, "Dash/Run")
                shuffle_attribute_group(fighter, target, "Friction")
                shuffle_attribute_group(fighter, target, "Air")
                shuffle_attribute_group(fighter, target, "Jump")
                shuffle_attribute_group(fighter, target, "Gravity")
                shuffle_attribute_group(fighter, target, "Weight")
                shuffle_attribute_group(fighter, target, "Landing Lag")
                fighter.shuffled = True
                target.shuffled = True
        
