from util import to_word

MAX_CAPACITY = 1459978240
iso_data = bytearray()

def get_fst():
    return iso_data[fst_offset():fst_offset()+fst_size()]

def get_dol():
    return iso_data[dol_offset():dol_offset()+dol_size()]
    
def dol_offset():
    return to_word(iso_data[0x0420:0x0424])

def dol_size():
    return fst_offset() - dol_offset()

def fst_offset():
    return to_word(iso_data[0x0424:0x0428])

def fst_size():
    return to_word(iso_data[0x0428:0x042C])

def get_game_id():
    return iso_data[0:0x0006]

def set_game_id(new):
    iso_data[0:0x0006] = new

def get_game_name():
    name_data = iso_data[0x0020:0x03FF]
    name = bytearray()
    for byte in name_data:
        if byte == 0:
            break
        name.append(byte)
    return name

def set_game_name(new):
    if type(new) == str:
        new = new.encode('utf-8')
    new = bytearray(new)
    for i in range(0x3FF - len(new)):
        new.append(0)
    iso_data[0x0020:0x041F] = new

def magic_word():
    return iso_data[0x001C:0x0020].hex()

def write_dol(new_dol):
    offset = dol_offset()
    iso_data[offset:offset + dol_size()] = new_dol
