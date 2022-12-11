import melee
from util import percent_chance, get_flag_params
from random import randint as rng
from random import uniform as rng_float

def chaos_hitbox_damage(attack, magnitude): # Damage and shield damage
    if attack.vanilla:
        return
    if attack.balance:
        damage = rng(attack.strength + (magnitude // 2) + 1, attack.strength * 2 + magnitude + 1)
        shield_damage = rng(attack.strength // 4 + magnitude // 5, attack.strength // 3 + magnitude // 3 + 1)
        if attack.strength < 3: # Damage cap for weak moves
            if damage > attack.strength + 1:
                damage = attack.strength + 1
        if attack.strength > 6: # Damage bonus for strong moves
            damage += 4
    else:
        damage = rng(0, 7 + magnitude * 2)
        shield_damage = rng(0, magnitude * 2)
    
    if damage < 1:
        damage = 1
    if shield_damage < 0:
        shield_damage = 0

    for hb in attack.hitboxes:
        hb.set_damage(damage)
        hb.set_shield(shield_damage)

def chaos_hitbox_angle(attack):
    if attack.vanilla:
        return
    if attack.balance:
        if percent_chance(90): # Forward/Upwards Angles
            angle = rng(5,21)*5 # Between 25 and 105 Degrees
        elif percent_chance(50): # Sakurai Angle
            angle = 361
        elif percent_chance(20): # Meteor
            angle = 290
        elif percent_chance(20): # Spike
            angle = 270
        else: # Random
            angle = rng(0,362)
    else:
        angle = rng(0,362)
    for hb in attack.hitboxes:
        hb.set_angle(angle)

def chaos_hitbox_base(attack, magnitude):
    if attack.vanilla:
        return
    if attack.balance:
        base = rng(magnitude // 2 + attack.strength // 2, attack.strength + magnitude) * 2
    else:
        base = rng(magnitude, 20 + magnitude * 2)
    for hb in attack.hitboxes:
        hb.set_base(base)

def chaos_hitbox_growth(attack, magnitude):
    if attack.vanilla:
        return
    if attack.balance:
        growth = rng((magnitude + attack.strength) * 7, (attack.strength + magnitude) * 10)
    else:
        growth = rng(magnitude * 5, magnitude * 15)
    for hb in attack.hitboxes:
        hb.set_growth(growth)

def chaos_hitbox_wdsk(attack, magnitude):
    if attack.vanilla:
        return
    wdsk = attack.hitboxes[0].get_set()
    if wdsk <= 0:
        return
    wdsk = rng(0, magnitude)*5
    for hb in attack.hitboxes:
        hb.set_set(wdsk)

def chaos_hitbox_size(attack, magnitude):
    if attack.vanilla:
        return
    size = rng(magnitude + 1, magnitude + 10) * 100
    for hb in attack.hitboxes:
        hb.set_size(size)

def chaos_throw_damage(throw, magnitude):
    if throw.vanilla:
        return
    throw.set_damage(rng(magnitude // 2 + 1, magnitude + 3))

def chaos_throw_angle(throw):
    if throw.vanilla:
        return
    if percent_chance(85):
        angle = rng(20,160)
    elif percent_chance(50):
        angle = 290
    else:
        angle = rng(180,360)
    throw.set_angle(angle)

def chaos_throw_base(throw, magnitude):
    if throw.vanilla:
        return
    throw.set_base(rng(magnitude * 2 + 1, magnitude * 5 + 1))

def chaos_throw_growth(throw, magnitude):
    if throw.vanilla:
        return
    throw.set_base(rng(magnitude * 5 + 1, magnitude * 15 + 1))

def chaos_throw_wdsk(throw, magnitude):
    if throw.vanilla:
        return
    if throw.get_set() <= 0:
        return
    throw.set_set(rng(magnitude * 5 + 1, magnitude * 10 + 1))
    
def chaos_throw_element(throw):
    if throw.vanilla:
        return
    throw.set_element(rng(0,4))

def chaos_attribute_group(fighter, group):
    attributes = fighter.get_attributes_by_group_name(group)
    for attribute in attributes:
        chaos_attribute(fighter, attribute.name)

def chaos_attribute(fighter, name):
    min_value = 1000000
    max_value = 0
    for f in melee.fighters:
        attribute = f.get_attribute_by_name(name)
        if attribute.get_value() < min_value:
            min_value = attribute.get_value()
        if attribute.get_value() > max_value:
            max_value = attribute.get_value()
    attribute = fighter.get_attribute_by_name(name)
    value = rng_float(min_value, max_value)
    if attribute.whole_number:
        value = round(value)
    attribute.set_value(value)

def start_mod(flags, chaos_percent):
    for fighter in melee.fighters: 
        for attack in fighter.attacks: # Attacks
            if "-chaos_hitbox_damage" in flags:
                if percent_chance(chaos_percent):
                    p = get_flag_params(flags, "-chaos_hitbox_damage")
                    chaos_hitbox_damage(attack, p[0])
            if "-chaos_hitbox_angle" in flags:
                if percent_chance(chaos_percent):
                    chaos_hitbox_angle(attack)
            if "-chaos_hitbox_base" in flags:
                if percent_chance(chaos_percent):
                    p = get_flag_params(flags, "-chaos_hitbox_base")
                    chaos_hitbox_base(attack, p[0])
            if "-chaos_hitbox_growth" in flags:
                if percent_chance(chaos_percent):
                    p = get_flag_params(flags, "-chaos_hitbox_growth ")
                    chaos_hitbox_growth(attack, p[0])
            if "-chaos_hitbox_wdsk" in flags:
                if percent_chance(chaos_percent):
                    p = get_flag_params(flags, "-chaos_hitbox_wdsk ")
                    chaos_hitbox_wdsk(attack, p[0])
            if "-chaos_hitbox_size" in flags:
                if percent_chance(chaos_percent):
                    p = get_flag_params(flags, "-chaos_hitbox_size ")
                    chaos_hitbox_size(attack, p[0])
        for throw in fighter.throws:
            if "-chaos_throw_damage" in flags:
                if percent_chance(chaos_percent):
                    p = get_flag_params(flags, "-chaos_throw_damage ")
                    chaos_throw_damage(throw, p[0])
            if "-chaos_throw_angle" in flags:
                if percent_chance(chaos_percent):
                    chaos_throw_angle(throw)
            if "-chaos_throw_base" in flags:
                if percent_chance(chaos_percent):
                    p = get_flag_params(flags, "-chaos_throw_base ")
                    chaos_throw_base(throw, p[0])
            if "-chaos_throw_growth" in flags:
                if percent_chance(chaos_percent):
                    p = get_flag_params(flags, "-chaos_throw_growth ")
                    chaos_throw_growth(throw, p[0])
            if "-chaos_throw_wdsk" in flags:
                if percent_chance(chaos_percent):
                    p = get_flag_params(flags, "-chaos_throw_wdsk ")
                    chaos_throw_wdsk(throw, p[0])
        if "-chaos_attribute_walk" in flags:
            if percent_chance(chaos_percent):
                chaos_attribute_group(fighter, "Walk")
        if "-chaos_attribute_dash" in flags:
            if percent_chance(chaos_percent):
                chaos_attribute_group(fighter, "Dash/Run")
        if "-chaos_attribute_air" in flags:
            if percent_chance(chaos_percent):
                chaos_attribute_group(fighter, "Air")
        if "-chaos_attribute_jump" in flags:
            if percent_chance(chaos_percent):
                chaos_attribute_group(fighter, "Jump")
        if "-chaos_attribute_gravity" in flags:
            if percent_chance(chaos_percent):
                chaos_attribute_group(fighter, "Gravity")
        if "-chaos_attribute_friction" in flags:
            if percent_chance(chaos_percent):
                chaos_attribute_group(fighter, "Friction")
        if "-chaos_attribute_weight" in flags:
            if percent_chance(chaos_percent):
                chaos_attribute(fighter, "Weight")
        if "-chaos_attribute_landing_lag" in flags:
            if percent_chance(chaos_percent):
                chaos_attribute_group(fighter, "Landing Lag")
                
