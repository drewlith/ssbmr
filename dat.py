from util import *

class DAT(): # Class for handling melee's DAT file format
    def __init__(self, fst_file):
        self.fst_file = fst_file
        self.data = fst_file.file_data
        self.header = read_data(self.data, 0, 0x20) # Header is 32 bytes. Then Data Block starts
        self.data_block = read_data(self.data, 0x20, self.data_block_size()) # Grabs the entire data block and puts it in to self.data
        self.relocation_offset = 0x20 + self.data_block_size()
        self.root_offset_a = self.relocation_offset + (self.relocation_table_count() * 4)
        self.root_offset_b = self.root_offset_a + (self.root_count()[0] * 8)
        self.string_table_offset = self.root_offset_b + (self.root_count()[1] * 8)
        self.relocation_table = RelocationTable(self)
        self.strings = self.get_strings()
        self.root_nodes = RootNodes(self)
        self.fighter_data = None
        self.fighter_name = None
        for node in self.root_nodes.nodes:
            if b'ftData' in node.name:
                self.fighter_data = FtData(self, node)
                self.fighter_name = node.name
        
    def file_size(self):
        return get_word(self.header, 7)

    def data_block_size(self):
        return get_word(self.header, 6)

    def relocation_table_count(self):
        return get_word(self.header, 5)

    def root_count(self): # Returns Tuple
        count_a = get_word(self.header, 4)
        count_b = get_word(self.header, 3)
        return [count_a, count_b]

    def unknowns(self):
        unknown_a = get_word(self.header, 2)
        unknown_b = get_word(self.header, 1)
        unknown_c = get_word(self.header, 0)
        return [unknown_a, unknown_b, unknown_c]

    def get_string(self, offset):
        i = 0
        name = bytearray()
        while True:
            if self.data_block[offset+i] != 0:
                name.append(self.data_block[offset+i])
                i += 1
            else:
                return name

    def get_strings(self):
        string_table_data = self.data[self.string_table_offset:]
        string_data = []
        name = bytearray()
        i = 0
        offset = 0
        while i < len(string_table_data):
            if string_table_data[i] != 0:
                name.append(string_table_data[i])
            else:
                string_data.append((name, offset))
                offset += i - offset + 1
                name = bytearray()
            i += 1
        
        return string_data

    def find_string_by_offset(self, offset):
        for data in self.strings:
            if data[1] == offset:
                return data[0]
        print("No name found at offset ", offset)
        return(b'No Name!')

    def get_subactions(self):
        subactions = []
        for data in self.fighter_data:
            for action in data.subactions:
                subactions.append(action)
        return subactions

    def write_to_fst(self):
        write_data(self.fst_file.file_data, 0, self.header)
        write_data(self.fst_file.file_data, 0x20, self.data_block)
         
    def display_info(self):
        print("File Size: ", hex(self.file_size()))
        print("Data Block Size: ", hex(self.data_block_size()))
        print("Relocation Table Count: ", hex(self.relocation_table_count()))
        print("Root Count 1: ", hex(self.root_count()[0]))
        print("Root Count 2: ", hex(self.root_count()[1]))
        print("Relocation Offset: ", hex(self.relocation_offset))
        print("Root 1 Offset: ", hex(self.root_offset_a))
        print("Root 2 Offset: ", hex(self.root_offset_b))
        print("String Table Offset: ", hex(self.string_table_offset))
        print("Unknown 1: ", hex(self.unknowns()[0]))
        print("Unknown 2: ", hex(self.unknowns()[1]))
        print("Unknown 3: ", hex(self.unknowns()[2]))

class Node():
    def __init__(self, dat, data_offset, string_offset):
        self.data_offset = data_offset
        self.string_offset = string_offset
        self.name = dat.find_string_by_offset(get_word(self.string_offset, 0))

class RootNodes():
    def __init__(self, dat):
        self.nodes = []
        for i in range(dat.root_count()[0]):
            data = read_data(dat.data, dat.root_offset_a + (i*8), 8)
            data_offset = read_data(data, 0, 4)
            string_offset = read_data(data, 4, 4)
            node = Node(dat, data_offset, string_offset)
            self.nodes.append(node)
        for i in range(dat.root_count()[1]):
            data = read_data(dat.data, dat.root_offset_b + (i*8), 8)
            data_offset = read_data(data, 0, 4)
            string_offset = read_data(data, 4, 4)
            node = Node(dat, data_offset, string_offset)
            self.nodes.append(node)

class RelocationTable():
    def __init__(self, dat):
        self.dat = dat
        self.relocation_offsets = self.get_relocation_offsets()
        self.data_offsets = self.get_data_offsets(self.relocation_offsets)

    def get_relocation_offsets(self): 
        offsets = []
        relocation_table = read_data(self.dat.data, self.dat.relocation_offset, self.dat.relocation_table_count()*4)
        word_length = len(relocation_table)//4 -1
        for i in range(self.dat.relocation_table_count()):
            offsets.append(get_word(relocation_table, word_length - i))
        return offsets

    def get_data_offsets(self, relocation_table):
        offsets = []
        for i in range(len(relocation_table)):
            offset = read_data(self.dat.data_block, relocation_table[i], 4)
            offsets.append(offset)
        return offsets

# Source: https://github.com/pfirsich/meleeDat2Json/blob/master/meleedat2json/meleedat2json.py
# Really, I should redo the whole thing to be as neat as the code at the link...
class FtData():
    def __init__(self, dat, node):
        start_offset = get_word(node.data_offset, 0)
        header = read_data(dat.data_block, start_offset, 24)
        self.attributes_offset = get_word(header, 5)
        self.attributes_end = get_word(header, 4)
        self.unknown_a = get_word(header, 3)
        self.subactions_offset = get_word(header, 2)
        self.unknown_b = get_word(header, 1)
        self.subactions_end = get_word(header, 0)

        self.attribute_data = dat.data_block[self.attributes_offset:self.attributes_end]
        self.subaction_data = dat.data_block[self.subactions_offset:self.subactions_end]

        subaction_count = len(self.subaction_data)//24

        self.subactions = []
        
        for i in range(subaction_count):
            data = read_data(self.subaction_data, i*24, 24)
            self.subactions.append(Subaction(data, dat))

class Subaction():
    def __init__(self, subaction_data, dat):
        self.name_offset = get_word(subaction_data, 5)
        self.animation_offset = get_word(subaction_data, 4)
        self.animation_size = get_word(subaction_data, 3)
        self.events_offset = get_word(subaction_data, 2)
        self.position_flags = get_word(subaction_data, 1) # Not sure what this is
        self.character_id = get_word(subaction_data, 0)
        self.name = dat.get_string(self.name_offset)
        
        self.hitboxes = []
        self.throws = []
        self.gfx = []
        self.sfx = []
        self.wait_sync_events = []
        self.wait_async_events = []
        self.loop_events = []
        self.shoot_item = []
        self.other = []
        
        def event_handler(offset):
                command = dat.data_block[offset]
                command = command >> 2
                command = command << 2

                data = dat.data_block
                size = 0x04

                match command:
                    case 0x00:
                        return
                    case 0x04: # Wait Sync
                        self.wait_sync_events.append(WordEvent(data[offset:offset+size], offset))
                    case 0x08: # Wait Async
                        self.wait_sync_events.append(WordEvent(data[offset:offset+size],offset))
                    case 0x0C: # Loops
                        self.loop_events.append(WordEvent(data[offset:offset+size], offset))
                    case 0x14: 
                        size = 0x08
                    case 0x1C:
                        size = 0x08
                    case 0x28: # GFX
                        size = 0x14
                        self.gfx.append(data[offset:offset+size])
                    case 0x2C: # Hitbox
                        size = 0x14
                        self.hitboxes.append(Hitbox(self.name, data[offset:offset+size], offset))
                    case 0x44: # SFX
                        size = 0x0C
                        self.sfx.append(SFX(data[offset:offset+size], offset))
                    case 0x60: # Shoot Item
                        self.shoot_item.append(data[offset:offset+size])
                    case 0x88: # Throws
                        size = 0x0C
                        self.throws.append(Throw(self.name, data[offset:offset+size], offset))
                    case 0x98:
                        size = 0x1C
                    case 0x9C:
                        size = 0x10
                    case 0xD8:
                        size = 0x0C
                    case 0xDC:
                        size = 0x0C
                    case 0xE0:
                        size = 0x08
                    case 0xE8:
                        size = 0x10
                    case _:
                        size = 0x04
                        self.other.append(dat.data_block[offset:offset+size])

                event_handler(offset + size)

        event_handler(self.events_offset)

class Hitbox(): # Class for handling Hitbox Event
    def __init__(self, name, data, offset):
        self.name = name
        self.data = data
        self.offset = offset

    def get_damage(self): #b2 and b3 xxxxxxxD DDDDDDDD
        return get_value(self.data, 128, 9)

    def set_damage(self, value): 
        self.data = set_value(self.data, 128, 9, value)
    
    def get_angle(self): #b12 and b13 AAAAAAAA Axxxxxxx
        return get_value(self.data, 55, 9)
    
    def set_angle(self, value):
        self.data = set_value(self.data, 55, 9, value)

    def get_growth(self): #b13 and b14 xGGGGGGG GGxxxxxx
        return get_value(self.data, 46, 9)

    def set_growth(self, value):
        self.data = set_value(self.data, 46, 9, value)
        
    def get_set(self): #b14 and b15 xxWWWWWW WWWxxxxx
        return get_value(self.data, 37, 9)

    def set_set(self, value):
        self.data = set_value(self.data, 37, 9, value)

    def get_base(self): #b16 and b17 BBBBBBBB Bxxxxxxx
        return get_value(self.data, 23, 9)

    def set_base(self, value):
        self.data = set_value(self.data, 23, 9, value)
    
    def get_element(self): #b17 xEEEEExx
        return get_value(self.data, 18, 5)

    def set_element(self, value):
        self.data = set_value(self.data, 18, 5, value)

    def get_shield(self): #b17 and b18 xxxxxxxS SSSSSSxx
        return get_value(self.data, 10, 7)

    def set_shield(self, value):
        self.data = set_value(self.data, 10, 7, value)

    def get_sfx(self): #b18 and b19 xxxxxxFF FFFFFFxx
        return get_value(self.data, 2, 8)

    def set_sfx(self, value):
        self.data = set_value(self.data, 2, 8, value)

    def get_size(self): #b4 and b5 SSSSSSSS SSSSSSSS
        return get_value(self.data, 112, 16)

    def set_size(self, value):
        self.data = set_value(self.data, 112, 16, value)

class Throw(): # Class for handling Throw Event
    def __init__(self, name, data, offset):
        self.name = name.decode("utf-8")
        self.data = data
        self.offset = offset
        self.fighter = None
        self.original_stats = []
        self.vanilla = False
        self.shuffle_target = self
        self.shuffled = False
        # IDs: Damage: 0 | Angle: 1 | BKB: 2 | KBG: 3 | WDSK: 4 | Element: 5
        # Values: Unchanged: 0 | Shuffled: 1 | Deviated: 2 | Randomized: 3 
        self.randomization_types = [0,0,0,0,0,0]

    def get_type(self):
        return get_value(self.data, 87, 3)

    def get_damage(self): #b2 and b3
        return get_value(self.data, 64, 9)

    def set_damage(self, value): 
        self.data = set_value(self.data, 64, 9, value)

    def get_angle(self): #b4 and b5 AAAAAAAA Axxxxxxx
        return get_value(self.data, 55, 9)

    def set_angle(self, value):
        self.data = set_value(self.data, 55, 9, value)

    def get_growth(self): #b5 and b6 xGGGGGGG GGxxxxxx
        return get_value(self.data, 46, 9)

    def set_growth(self, value):
        self.data = set_value(self.data, 46, 9, value)

    def get_set(self): #b6 and b7 xxWWWWWW WWWxxxxx
        return get_value(self.data, 37, 9)

    def set_set(self, value):
        self.data = set_value(self.data, 37, 9, value)

    def get_base(self): #b8 and b9 BBBBBBBB Bxxxxxxx
        return get_value(self.data, 23, 9)

    def set_base(self, value):
        self.data = set_value(self.data, 23, 9, value)

    def get_element(self): #b9 xEEEExxx
        return get_value(self.data, 19, 4)

    def set_element(self, value):
        self.data = set_value(self.data, 19, 4, value)

    def record_original_stats(self):
        self.original_stats.clear()
        self.original_stats.append(str(self.get_damage()))
        self.original_stats.append(str(self.get_angle()))
        self.original_stats.append(str(self.get_growth()))
        self.original_stats.append(str(self.get_base()))
        self.original_stats.append(str(self.get_set()))
        self.original_stats.append(self.get_element())

class SFX():
    def __init__(self, data, offset):
        self.offset = offset
        self.data = data
    def get(self):
        return get_value(self.data, 32, 20)

class WordEvent():
    def __init__(self, data, offset):
        self.offset = offset
        self.data = data
    def get(self):
        return self.data[3]
    def set(self, value):
        set_value(self.data, 0, 8, value)
