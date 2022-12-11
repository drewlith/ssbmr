import melee, struct
from util import *
from random import uniform as rng_float

def start_mod():
    plco = melee.find_file(b'PlCo.dat')
    #set_word(plco, 0xA0FC, rng_float(1.0,2.0)) # Knockback Multiplier
    set_word(plco, 0xA134, rng_float(0.533,0.544)) # Hitstun Multiplier
    
def set_word(plco, offset, value):
    data = struct.pack('>f', value)
    plco.file_data[offset:offset+4] = data

def get_word(plco, offset):
    data = plco.file_data[offset:offset+4]
    return struct.unpack('>f', data)[0]

def get_word_hex(plco, offset):
    return get_word_string(plco.file_data[offset:offset+4])
