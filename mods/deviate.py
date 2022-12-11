import melee
from util import percent_chance, get_flag_params
from random import randint as rng
from random import uniform as rng_float

def deviate_value(value, floor, ceiling):
    if floor > ceiling:
        floor, ceiling = ceiling, floor
    if value == 0:
        return value
    # Convert to Float
    is_float = True
    if type(value) == int:
        value = float(value)
        is_float = False
    # Convert Floor/Ceiling to multipliers
    floor = floor * 0.01
    ceiling = ceiling * 0.01
    value = value * rng_float(floor, ceiling)
    if value < 0.01 and value > 0:
        value = 0.01
    if not is_float:
        value = round(value)
        value = int(value)
    return value

def deviate_angle(value, degrees): # Deviates by whole numbers and not percent
    if value == 361:
        return value
    value = rng(value - degrees, value + degrees)
    if value < 0:
        value = 360 + value
    if value > 360:
        value = value - 360
    return value

def hitbox_deviate_flag(flags, flag_name, get_func, set_func, angle=False): # Wrappers, checks for flag name, gets parameters from flags
    if flag_name in flags:                                                  # Wraps get/set functions too, for like damage for example.
        p = get_flag_params(flags, flag_name) # Angle boolean just because it's an exception to the pattern.
        for fighter in melee.fighters:
            for attack in fighter.attacks:
                value = -1
                for hb in attack.hitboxes:
                    get_ = getattr(hb,get_func)
                    set_ = getattr(hb,set_func)
                    if value == -1: # If a reference value hasn't been decided yet.
                        if angle:
                            value = deviate_angle(get_(),p[0])
                        else:
                            value = deviate_value(get_(),p[0],p[1])
                    set_(value)

def throw_deviate_flag(flags, flag_name, get_func, set_func, angle=False):
    if flag_name in flags:
        p = get_flag_params(flags, flag_name)
        for fighter in melee.fighters:
            for throw in fighter.throws:
                get_ = getattr(throw, get_func)
                set_ = getattr(throw, set_func)
                if angle:
                    set_(deviate_angle(get_(),p[0]))
                else:
                    set_(deviate_value(get_(),p[0],p[1]))

def attribute_deviate_flag(flags, flag_name, group):
    if flag_name in flags:
        p = get_flag_params(flags, flag_name)
        for fighter in melee.fighters:
            attributes = fighter.get_attributes_by_group_name(group)
            for attribute in attributes:
                attribute.set_value(deviate_value(attribute.get_value(), p[0], p[1]))

def unique_deviate_flag(flags, flag_name, fighter_name, group):
    if flag_name in flags:
        p = get_flag_params(flags, flag_name)
        fighter = melee.find_fighter(fighter_name)
        attributes = fighter.get_attributes_by_group_name(group, True)
        for attribute in attributes:
            if attribute.whole_number:
                attribute.set_value_int(deviate_value(attribute.get_value_int(), p[0], p[1]))
            else:
                attribute.set_value(deviate_value(attribute.get_value(), p[0], p[1]))

def start_mod(flags):
    hitbox_deviate_flag(flags, "-hitbox_damage", "get_damage", "set_damage")
    hitbox_deviate_flag(flags, "-hitbox_angle", "get_angle", "set_angle", True)
    hitbox_deviate_flag(flags, "-hitbox_shield_damage", "get_shield", "set_shield")
    hitbox_deviate_flag(flags, "-hitbox_growth", "get_growth", "set_growth")
    hitbox_deviate_flag(flags, "-hitbox_base", "get_base", "set_base")
    hitbox_deviate_flag(flags, "-hitbox_wdsk", "get_set", "set_set")
    hitbox_deviate_flag(flags, "-hitbox_size", "get_size", "set_size")
    throw_deviate_flag(flags, "-throw_damage", "get_damage", "set_damage")
    throw_deviate_flag(flags, "-throw_angle", "get_angle", "set_angle", True)
    throw_deviate_flag(flags, "-throw_growth", "get_growth", "set_growth")
    throw_deviate_flag(flags, "-throw_base", "get_base", "set_base")
    throw_deviate_flag(flags, "-throw_wdsk", "get_set", "set_set")
    attribute_deviate_flag(flags, "-attribute_walk", "Walk")
    attribute_deviate_flag(flags, "-attribute_dash", "Dash/Run")
    attribute_deviate_flag(flags, "-attribute_friction", "Friction")
    attribute_deviate_flag(flags, "-attribute_air", "Air")
    attribute_deviate_flag(flags, "-attribute_jump", "Jump")
    attribute_deviate_flag(flags, "-attribute_gravity", "Gravity")
    attribute_deviate_flag(flags, "-attribute_weight", "Weight")
    attribute_deviate_flag(flags, "-attribute_scale", "Scale")
    attribute_deviate_flag(flags, "-attribute_shield_size", "Shield")
    attribute_deviate_flag(flags, "-attribute_landing_lag", "Landing Lag")
    unique_deviate_flag(flags, "-bowser_super_armor", "Bowser", "Passive")
    unique_deviate_flag(flags, "-bowser_flames", "Bowser", "Neutral B")
    unique_deviate_flag(flags, "-koopa_klaw", "Bowser", "Side B")
    unique_deviate_flag(flags, "-whirling_fortress", "Bowser", "Up B")
    unique_deviate_flag(flags, "-bowser_bomb", "Bowser", "Down B")
    unique_deviate_flag(flags, "-falcon_punch", "Captain Falcon", "Neutral B")
    unique_deviate_flag(flags, "-raptor_boost", "Captain Falcon", "Side B")
    unique_deviate_flag(flags, "-falcon_dive", "Captain Falcon", "Up B")
    unique_deviate_flag(flags, "-falcon_kick", "Captain Falcon", "Down B")
    unique_deviate_flag(flags, "-cargo", "Donkey Kong", "Passive")
    unique_deviate_flag(flags, "-giant_punch", "Donkey Kong", "Neutral B")
    unique_deviate_flag(flags, "-headbutt", "Donkey Kong", "Side B")
    unique_deviate_flag(flags, "-spinning_kong", "Donkey Kong", "Up B")
    unique_deviate_flag(flags, "-super_sheet", "Dr Mario", "Side B")
    unique_deviate_flag(flags, "-super_jump_punch", "Dr Mario", "Up B")
    unique_deviate_flag(flags, "-dr_tornado", "Dr Mario", "Down B")
    unique_deviate_flag(flags, "-falco_blaster", "Falco", "Neutral B")
    unique_deviate_flag(flags, "-phantasm", "Falco", "Side B")
    unique_deviate_flag(flags, "-fire_bird", "Falco", "Up B")
    unique_deviate_flag(flags, "-falco_reflector", "Falco", "Down B")
    
    
