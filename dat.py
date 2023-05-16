import iso, fst
from util import to_word, get_value, set_value

file_data = None

# Basic Stuff
def header():
    return file_data[0x0:0x20]

def data_block():
    return file_data[0x20:data_block_size()]

def data_block_size():
    return to_word(header(), 6)

def file_size():
    return to_word(header(), 7)

# Relocation Table Stuff
def relocation_count():
    return to_word(header(), 5)

def relocation_table_offset():
    return 0x20 + data_block_size()

def get_relocation_table_offsets():
    offsets = []
    table_offset = relocation_table_offset()
    table = file_data[table_offset:table_offset + relocation_count()*4]
    table_word_length = len(table)//4 - 1
    for i in range(relocation_count()):
        offsets.append(to_word(table, table_word_length - i))
    return offsets

def get_relocation_table_data_offsets():
    table_offsets = get_relocation_table_offsets()
    offsets = []
    data = data_block()
    for i in range(len(table_offsets)):
        offset = table_offsets[i]
        offsets.append(data[offset:offset + 4])
    return offsets

# Root Node, Node, and string stuff
def get_string(offset):
    name = bytearray()
    i = 0
    while True:
        if data_block()[offset+i] != 0:
            name.append(data_block()[offset+i])
            i += 1
        else:
            return name
    print("Error.. No string found at ", offset)

def get_strings():
    string_data = file_data[string_table_offset():]
    strings = []
    name = bytearray()
    i = 0
    offset = 0
    while i < len(string_data):
        if string_data[i] != 0:
            name.append(string_data[i])
        else:
            strings.append((name,offset))
            offset += i - offset + 1
            name = bytearray()
        i += 1
    return strings

def find_string(strings, offset):
    for string in strings:
        if string[1] == offset:
            return string[0]
    print("No name found at offset ", offset)
    return(b'No Name!')

def root_counts():
    a = to_word(header(), 3)
    b = to_word(header(), 4)
    return (a,b)

def root_offsets():
    a = relocation_table_offset() + relocation_count() * 4
    b = a + root_counts()[0] * 8
    return (a,b)

def get_nodes():
    nodes = []
    for i in range(root_counts()[0]):
        offset = root_offsets()[0] + (i*8)
        data = file_data[offset:offset + 8]
        data_offset = data[0:4]
        string_offset = data[4:8]
        nodes.append(Node(data_offset, string_offset))
    for i in range(root_counts()[1]):
        offset = root_offsets()[1] + (i*8)
        data = file_data[offset:offset + 8]
        data_offset = data[0:4]
        string_offset = data[4:8]
        nodes.append(Node(data_offset, string_offset))
    return nodes

def string_table_offset():
    return root_offsets()[1] + root_counts()[1] * 8

class Node():
    def __init__(self, data_offset, string_offset):
        strings = get_strings()
        self.data_offset = data_offset
        self.string_offset = string_offset
        self.name = find_string(strings, to_word(string_offset))

# Fighter DAT Specific stuff
def ft_node():
    for node in get_nodes():
        if b'ftData' in node.name:
            return node
    print("No ftData node was found.")

def ft_start_offset():
    return to_word(ft_node().data_offset)

def ft_header():
    offset = ft_start_offset()
    return data_block()[offset:offset + 24]

def ft_attributes_offset():
    return to_word(ft_header(), 5)

def ft_attributes_end():
    return to_word(ft_header(), 4)

def ft_subactions_offset():
    return to_word(ft_header(), 2)

def ft_subactions_end():
    return to_word(ft_header(), 0)

def get_attribute_data():
    return data_block()[ft_attributes_offset():ft_attributes_end()]

def get_subaction_data():
    return data_block()[ft_subactions_offset():ft_subactions_end()]

def ft_subaction_count():
    return len(get_subaction_data()) // 24

def get_subactions():
    subactions = []
    subaction_data = get_subaction_data() 
    for i in range(ft_subaction_count()):
        subaction = Subaction(subaction_data[i*24:i*24+24])
        subactions.append(subaction)
    return subactions

class Subaction():
    def __init__(self, subaction_data):
        self.data = subaction_data
        self.name = self.get_name()
        self.hitboxes = []
        self.throws = []
        self.sfx = []
        self.other = []
        self.get_events(self.events_offset())

    def name_offset(self):
        return to_word(self.data, 5)
    
    def animation_offset(self):
        return to_word(self.data, 4)

    def animation_size(self):
        return to_word(self.data, 3)

    def events_offset(self):
        return to_word(self.data, 2)

    def position_flags(self):
        return to_word(self.data, 1)

    def character_id(self):
        return to_word(self.data, 0)

    def get_name(self):
        return get_string(self.name_offset())

    def get_events(self, offset):
        command = data_block()[offset]
        command = command >> 2
        command = command << 2
        size = 0x04
        match command:
            case 0x00:
                return
            case 0x04: # Wait Sync
                self.other.append(data_block()[offset:offset+size])
            case 0x08: # Wait Async
                self.other.append(data_block()[offset:offset+size])
            case 0x0C: # Loop
                self.other.append(data_block()[offset:offset+size])
            case 0x14:
                size = 0x08
            case 0x1C:
                size = 0x08
            case 0x28: # GFX
                size = 0x14
            case 0x2C: # Hitbox
                size = 0x14
                self.hitboxes.append(Hitbox(data_block()[offset:offset+size], offset))
            case 0x44: # SFX
                size = 0x0C
                self.sfx.append(SFX(data_block()[offset:offset+size], offset))
            case 0x60: # Shoot Item
                self.other.append(data_block()[offset:offset+size])
            case 0x88: # Throws
                size = 0x0C
                self.throws.append(Throw(data_block()[offset:offset+size], offset))
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
                self.other.append(data_block()[offset:offset+size])
            
        self.get_events(offset+size)

class Hitbox(): # Class for handling Hitbox Event
    def __init__(self, data, offset):
        self.data = data
        self.offset = offset
        
    @property
    def damage(self): #b2 and b3 xxxxxxxD DDDDDDDD
        return get_value(self.data, 128, 9)
    
    @damage.setter
    def damage(self, value): 
        self.data = set_value(self.data, 128, 9, value)

    @property
    def angle(self): #b12 and b13 AAAAAAAA Axxxxxxx
        return get_value(self.data, 55, 9)

    @angle.setter
    def angle(self, value):
        self.data = set_value(self.data, 55, 9, value)

    @property
    def growth(self): #b13 and b14 xGGGGGGG GGxxxxxx
        return get_value(self.data, 46, 9)

    @growth.setter
    def growth(self, value):
        self.data = set_value(self.data, 46, 9, value)

    @property
    def set_kb(self): #b14 and b15 xxWWWWWW WWWxxxxx
        return get_value(self.data, 37, 9)

    @set_kb.setter
    def set_kb(self, value):
        self.data = set_value(self.data, 37, 9, value)

    @property
    def base(self): #b16 and b17 BBBBBBBB Bxxxxxxx
        return get_value(self.data, 23, 9)

    @base.setter
    def base(self, value):
        self.data = set_value(self.data, 23, 9, value)

    @property
    def element(self): #b17 xEEEEExx
        return get_value(self.data, 18, 5)

    @element.setter
    def element(self, value):
        self.data = set_value(self.data, 18, 5, value)

    @property
    def shield_damage(self): #b17 and b18 xxxxxxxS SSSSSSxx
        return get_value(self.data, 10, 7)

    @shield_damage.setter
    def shield_damage(self, value):
        self.data = set_value(self.data, 10, 7, value)

    @property
    def sfx(self): #b18 and b19 xxxxxxFF FFFFFFxx
        return get_value(self.data, 2, 8)

    @sfx.setter
    def sfx(self, value):
        self.data = set_value(self.data, 2, 8, value)

    @property
    def size(self): #b4 and b5 SSSSSSSS SSSSSSSS
        return get_value(self.data, 112, 16)

    @size.setter
    def size(self, value):
        self.data = set_value(self.data, 112, 16, value)

class Throw(): # Class for handling Throw Event
    def __init__(self, data, offset):
        self.data = data
        self.offset = offset

    def get_type(self):
        return get_value(self.data, 87, 3)

    @property
    def damage(self): #b2 and b3
        return get_value(self.data, 64, 9)

    @damage.setter
    def set_damage(self, value): 
        self.data = set_value(self.data, 64, 9, value)

    @property
    def angle(self): #b4 and b5 AAAAAAAA Axxxxxxx
        return get_value(self.data, 55, 9)

    @angle.setter
    def angle(self, value):
        self.data = set_value(self.data, 55, 9, value)

    @property
    def growth(self): #b5 and b6 xGGGGGGG GGxxxxxx
        return get_value(self.data, 46, 9)

    @growth.setter
    def growth(self, value):
        self.data = set_value(self.data, 46, 9, value)

    @property
    def set_kb(self): #b6 and b7 xxWWWWWW WWWxxxxx
        return get_value(self.data, 37, 9)

    @set_kb.setter
    def set_kb(self, value):
        self.data = set_value(self.data, 37, 9, value)

    @property
    def base(self): #b8 and b9 BBBBBBBB Bxxxxxxx
        return get_value(self.data, 23, 9)

    @base.setter
    def base(self, value):
        self.data = set_value(self.data, 23, 9, value)

    @property
    def element(self): #b9 xEEEExxx
        return get_value(self.data, 19, 4)

    @element.setter
    def element(self, value):
        self.data = set_value(self.data, 19, 4, value)

class SFX():
    def __init__(self, data, offset):
        self.offset = offset
        self.data = data
    def get_sfx(self):
        return get_value(self.data, 32, 20)
