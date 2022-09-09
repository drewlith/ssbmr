import melee
from util import set_value

#TEST
def read_data(data, offset, length):
    new_data = bytearray()
    new_data.extend(data[offset:offset+length])
    return new_data
    
def write_data(data, offset, new_data):
    data[offset:offset+len(new_data)] = new_data

def enable_c_stick_single_player(dol): # Credit: Zauron
    offset = 0x168060
    data = read_data(dol, offset, 4)
    data = set_value(data, 0, 32, 0x60000000)
    write_data(dol, offset, data)

def code_converter():
    return
    
def start_mod():
    enable_c_stick_single_player(melee.dol)


    
    
    
