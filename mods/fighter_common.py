import melee, struct
from util import *
from random import uniform as rng_float

def start_mod(flags):
    plco = melee.find_file(b'PlCo.dat')
    if "-knockback" in flags:
        amount = get_flag_float(flags, "-knockback")[0]
        set_word(plco, 0xA0FC, amount) # Knockback Multiplier
    if "-hitstun" in flags:
        amount = get_flag_float(flags, "-hitstun")[0]
        set_word(plco, 0xA134, amount) # Hitstun Multiplier
    if "-hitlag" in flags:
        amount = get_flag_float(flags, "-hitlag")[0]
        set_word(plco, 0xA17C, amount) # Base Hitlag
    if "-l_cancel_leniency" in flags:
        amount = get_flag_params(flags, "-l_cancel_leniency")[0]
        set_word_int(plco, 0xA0C4, amount) # L Cancel Leniency
    if "-l_cancel_division" in flags:
        amount = get_flag_float(flags, "-l_cancel_division")[0]
        set_word(plco, 0xA0C8, amount) # L Cancel Division
    if "-shield_hp" in flags:
        amount = get_flag_float(flags, "-shield_hp")[0]
        set_word(plco, 0xA240, amount) # Shield HP
    if "-shield_release" in flags:
        amount = get_flag_float(flags, "-shield_release")[0]
        set_word(plco, 0xA248, amount) # Shield Release
    if "-shield_stun" in flags:
        amount = get_flag_float(flags, "-shield_stun")[0]
        set_word(plco, 0xA270, amount) # Shield Stun
    if "-air_dodge_speed" in flags:
        amount = get_flag_float(flags, "-air_dodge_speed")[0]
        set_word(plco, 0xA318, amount) # Air Dodge Speed
    if "-air_dodge_lag" in flags:
        amount = get_flag_float(flags, "-air_dodge_lag")[0]
        set_word(plco, 0xA324, amount) # Air Dodge Lag
    if "-ledge_timeout" in flags:
        amount = get_flag_params(flags, "-ledge_timeout")[0]
        set_word_int(plco, 0xA478, amount) # Ledge Timeout
    if "-ledge_invincible" in flags:
        amount = get_flag_params(flags, "-ledge_invincible")[0]
        set_word_int(plco, 0xA47C, amount) # Ledge Invincibility
    if "-respawn_timer" in flags:
        amount = get_flag_params(flags, "-respawn_timer")[0]
        set_word_int(plco, 0xA4E0, amount) # Respawn Timer
    
def set_word(plco, offset, value):
    data = struct.pack('>f', value)
    plco.file_data[offset:offset+4] = data

def set_word_int(plco, offset, value):
    data = value.to_bytes(4, "big")
    plco.file_data[offset:offset+4] = data

def get_word(plco, offset):
    data = plco.file_data[offset:offset+4]
    return struct.unpack('>f', data)[0]

def get_word_hex(plco, offset):
    return get_word_string(plco.file_data[offset:offset+4])
