import struct, fighter, iso
from utility import percent_chance
from random import uniform as rng_f
from structs import async_timer, subroutine, return_to, goto

class FSM(): 
    def __init__(self):
        self.data = bytearray(0xFC00000000000000.to_bytes(8, "big"))

    @property
    def speed_multiplier(self): #b2 and b3
        return struct.unpack('>f',self.data[4:])[0]

    @speed_multiplier.setter
    def speed_multiplier(self, multiplier): 
        self.data[4:8] = struct.pack('>f', multiplier)

    def __str__(self):
        string = "Frame Speed Modifier Event at offset " + str(self.offset) + " with command: " + str(hex(self.data[0])) + " and multiplier: " + str(self.speed_multiplier)
        return string
    
def get_async_frames(subaction):
    frames = 0
    for event in subaction.script:
        if type(event) == async_timer.AsyncTimer:
            frames += event.value
    return frames

def get_script_length(script):
    length = 0
    for event in script:
        length += len(event.data)
    return length

def write_all():
    blacklist = ["Crazy Hand", "Master Hand", "Male Wireframe", "Female Wireframe", "Giga Bowser"]
    for _fighter in fighter.fighters:
        if _fighter.name not in blacklist: # Handle this case later
            insert_offset = _fighter.dat_file.data_block_size() + 0x20
            start_offset = insert_offset
            data_to_write = bytearray()
            for subaction in _fighter.subactions:
                if subaction.custom:
                    fsm_event = FSM()
                    fsm_event.speed_multiplier = subaction.fsm_multiplier
                    fsm_event.offset = subaction.script[0].offset
                    subaction.add_event(0,fsm_event)
                    subaction.write_events_offset(insert_offset - 0x20)
                    for event in subaction.script:
                        data_to_write.extend(event.data)
                    padding = get_script_length(subaction.script) % 0x4
                    data_to_write.extend(bytearray(padding))
                    insert_offset += get_script_length(subaction.script) + padding

            _fighter.dat_file.insert_data(data_to_write, start_offset)
        iso.replace_file_data(_fighter.dat_file.file_name, _fighter.dat_file.file_data)
        
def create_new_events(subaction):
    new_data = bytearray()
    for event in subaction.script:
        new_data.extend(event.data)
    padding = bytearray(16)
    new_data.extend(padding)
    old_file_length = subaction.dat_file.file_size()
    iso.extend_file(subaction.dat_file.file_name, new_data)
    subaction.dat_file.file_data[0:4] = len(subaction.dat_file.file_data).to_bytes(4, "big")
    subaction.write_events_offset(old_file_length-0x20)
        
