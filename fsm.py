import struct, iso, fighter, os
from random import uniform

fsm_data_file = open("FSM.dat", "rb")
fsm_data = fsm_data_file.read()
fsm_data_file.close()
new_data_file = open("FSM_New.dat", "wb")
new_data_file.write(fsm_data)
fsm_file_size = len(fsm_data)

def seek_and_read(offset, size):
    new_data_file.seek(offset)
    return bytearray(fsm_data_file.read(size))

def seek_and_write(offset, data):
    new_data_file.seek(offset)
    new_data_file.write(data)

def add_fsm_code(char_ID, frame, action_ID, speed_multiplier, subaction=False):
    data_to_write = bytearray()
    data_to_write.extend(char_ID.to_bytes(1, "big"))
    data_to_write.extend(frame.to_bytes(1, "big"))
    if subaction:
        action_ID = action_ID | 0x8000
    data_to_write.extend(action_ID.to_bytes(2, "big"))
    data_to_write.extend(struct.pack('>f', speed_multiplier))
    return data_to_write

def write_fsm_file(codes):
    seek_and_write(0x20, codes[0:fsm_file_size-0x22])
    if len(codes) > fsm_file_size - 0x20:
        print("Too many FSMs!!!")
    new_data_file.close()
    dat_file = iso.find_file(b'TyMnView.dat')
    dat_file.name = b'FSM.dat'
    iso.replace_file(b'FSM.dat', "FSM_New.dat")
    os.remove("FSM_New.dat")
    # Patch dol with fsm engine
    patched_dol_file = open("patched.dol", "rb")
    patched_dol_data = patched_dol_file.read()
    patched_dol_file.close()
    iso.write_dol(patched_dol_data)

def randomize_all():
    codes = bytearray()
    sorted_fighters = sorted(fighter.fighters, key=lambda obj: obj.fighter_id)
    for _fighter in sorted_fighters:
        for subaction in _fighter.subactions:
            random_float = uniform(0.8,1.5)
            if "Nana" in _fighter.name:
                pass
            elif "Nameless" in subaction.friendly_name:
                pass
            else:
                codes.extend(add_fsm_code(_fighter.fighter_id,0,subaction.index,random_float,True))
    write_fsm_file(codes)

    

