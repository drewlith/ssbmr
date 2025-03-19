from utility import to_word
from structs.subaction import Subaction

MAX_CAPACITY = 1459978240
CHUNK_SIZE = 5703040 # 256 Chunks
iso_path = "melee.iso"
output_path = "randomized.iso"
source = open(iso_path, 'rb')
melee = open(output_path, 'wb+')
melee.write(source.read())
source.close()

# ISO
def seek_and_read(offset, size):
    melee.seek(offset)
    return bytearray(melee.read(size))

def seek_and_write(offset, data):
    melee.seek(offset)
    melee.write(data)

def seek_and_read_word(offset):
    return seek_and_read(offset, 4)

def get_fst():
    return seek_and_read(fst_offset(), fst_size())

def get_dol():
    return seek_and_read(dol_offset(), dol_size())
    
def dol_offset():
    return to_word(seek_and_read_word(0x420))

def dol_size():
    return fst_offset() - dol_offset()

def fst_offset():
    return to_word(seek_and_read_word(0x0424))

def fst_size():
    return to_word(seek_and_read_word(0x0428))

def get_game_id():
    return seek_and_read(0, 6)

def set_game_id(new):
    seek_and_write(0, new)

def get_game_name():
    name_data = seek_and_read(0x0020, 0x3DF)
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
    seek_and_write(0x0020, new)

def magic_word():
    return seek_and_read_word(0x001C).hex()

def write_dol(new_dol):
    seek_and_write(dol_offset(), new_dol)

### FST/game.toc 
# Modifies ISO file, retrieves and replaces files, and creates new ISO.
STRING_TABLE_OFFSET = 0x38D0 # Is there a way to calculate this offset?
# Would be useful for implementing Akaneia support.
ENTRY_SIZE = 0x0C
# Anything in the whitelist will be files that the randomizer changes
WHITELIST = [b'PlKp.dat', b'PlCa.dat', b'PlCl.dat', b'PlDk.dat', b'PlDr.dat', b'PlFc.dat',
             b'PlFe.dat', b'PlFx.dat', b'PlGn.dat', b'PlGw.dat', b'PlKb.dat', b'PlLg.dat',
             b'PlLk.dat', b'PlMr.dat', b'PlMs.dat', b'PlMt.dat', b'PlNn.dat', b'PlNs.dat',
             b'PlPc.dat', b'PlPe.dat', b'PlPk.dat', b'PlSk.dat', b'PlSs.dat', b'PlYs.dat',
             b'PlZd.dat']

class FST:
    def __init__(self, fst_data):
        self.fst_data = fst_data
        self.entries = self.get_file_entries()

    def get_file_entries(self):
        entries = []
        offset = 0
        while True: # Create Entries
            if offset >= STRING_TABLE_OFFSET:
                break
            new_file = MeleeFile(self.fst_data[offset:offset + ENTRY_SIZE], offset)
            if new_file.type == "File":
                new_file.load_file_data()
                entries.append(new_file)
            offset += ENTRY_SIZE
        sorted_entries = sorted(entries, key=lambda file: file.offset)
        return sorted_entries
    
    def write_file_entries(self):
       for file in self.entries:
           self.fst_data[file.fst_offset:file.fst_offset + ENTRY_SIZE] = file.entry_data

class MeleeFile: # Contains FST data, and File data
    def __init__(self, data, offset):
        self.entry_data = data
        self.file_data = None
        self.fst_offset = offset
        self.changed = False

    @property
    def type(self):
        if self.entry_data[0] == 0:
            return "File"
        return "Directory"

    @property
    def name(self):
        fst = get_fst()
        offset = int.from_bytes(self.entry_data[0x01:0x04], "big") + STRING_TABLE_OFFSET
        name = bytearray()
        i = 0
        while True:
            byte = fst[offset+i]
            if byte == 0:
                return name
            name.append(byte)
            i += 1

    @property
    def offset(self):
        return to_word(self.entry_data[0x04:0x08])

    @offset.setter
    def offset(self, new):
        self.entry_data[0x04:0x08] = new.to_bytes(4, 'big')

    @property
    def size(self):
        return to_word(self.entry_data[0x08:0x0C])

    @size.setter
    def size(self, new):
        self.entry_data[0x08:0x0C] = new.to_bytes(4, 'big')

    def load_file_data(self):
        self.changed = True
        self.file_data = seek_and_read(self.offset, self.size)

def find_file(name):
    for file in fst.entries:
        if name in file.name:
            return file
    print("No file found with name:", name)
    return 0

def replace_file(name, new_file_path):
    file = find_file(name)
    if file != 0: # Overwrite file data  
        new_file = open(new_file_path, "rb") # Get data from new file
        new_file_data = new_file.read()
        new_file.close()

        old_size = file.size 
        old_offset = file.offset
        file.size = len(new_file_data)

        offset_adjustment = old_size - file.size # Calculate offset adjustment
        offset_adjustment += offset_adjustment % 0x20

        for _file in fst.entries: # Update offsets for the rest of the files after this file, since they should remain adjacent and now there's a gap.
            if _file.offset > old_offset:
                _file.offset = _file.offset - offset_adjustment

        file.file_data = new_file_data

def write_files_to_disk(): # Debug/Utility
    for file in fst.entries:
        for name in WHITELIST:
            if file.name in name:
                file_to_write = open(b'melee_files/' + bytes(file.name), "wb")
                file_to_write.write(file.file_data)
                file_to_write.close()

def build_iso():
    replace_file(b'MvHowto.mth', "blank.mth") # Delete Movies
    replace_file(b'MvOmake15.mth', "blank.mth")
    fst.write_file_entries()
    seek_and_write(fst_offset(), fst.fst_data)
    # Change later once gecko is reimplemented, get_dol to new dol
    seek_and_write(dol_offset(), get_dol())
    for file in fst.entries:
        seek_and_write(file.offset, file.file_data)
    while True: # Add padding at end. Could be 0x20 but 0x8000 lines up better with an actual disk.
        if melee.tell() % 0x8000 != 0:
            melee.write(bytes(1))
        else:
            break
    melee.truncate()
    melee.close()

class Node(): # Used by DAT
    def __init__(self, dat, data_offset, string_offset):
        strings = dat.get_strings()
        self.data_offset = data_offset
        self.string_offset = string_offset
        self.name = dat.find_string(strings, to_word(string_offset))

# DAT File Handling, for Fighters
class DAT:
    def __init__(self, file_name):
        self.file_name = file_name
        self.file_data = find_file(file_name).file_data
        self.header = self.file_data[0x0:0x20]
        self.data_block = self.file_data[0x20:0x20+self.data_block_size()]

    # Basic Stuff
    def data_block_size(self):
        return to_word(self.header, 6)

    def file_size(self):
        return to_word(self.header, 7)

    # Relocation Table Stuff
    def relocation_count(self):
        return to_word(self.header, 5)

    def relocation_table_offset(self):
        return 0x20 + self.data_block_size()

    def get_relocation_table_offsets(self):
        offsets = []
        table_offset = self.relocation_table_offset()
        table = self.file_data[table_offset:table_offset + self.relocation_count()*4]
        table_word_length = len(table)//4 - 1
        for i in range(self.relocation_count()):
            offsets.append(to_word(table, table_word_length - i))
        return offsets

    def get_relocation_table_data_offsets(self):
        table_offsets = self.get_relocation_table_offsets()
        offsets = []
        data = self.data_block
        for i in range(len(table_offsets)):
            offset = table_offsets[i]
            offsets.append(data[offset:offset + 4])
        return offsets

    # Root Node, Node, and string stuff
    def get_string(self, offset):
        name = bytearray()
        i = 0
        while True:
            if self.data_block[offset+i] != 0:
                name.append(self.data_block[offset+i])
                i += 1
            else:
                return name
        print("Error.. No string found at ", offset)

    def get_strings(self):
        string_data = self.file_data[self.string_table_offset():]
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

    def find_string(self, strings, offset):
        for string in strings:
            if string[1] == offset:
                return string[0]
        print("No name found at offset ", offset)
        return(b'No Name!')

    def root_counts(self):
        a = to_word(self.header, 3)
        b = to_word(self.header, 4)
        return (a,b)

    def root_offsets(self):
        a = self.relocation_table_offset() + self.relocation_count() * 4
        b = a + self.root_counts()[0] * 8
        return (a,b)

    def get_nodes(self):
        nodes = []
        for i in range(self.root_counts()[0]):
            offset = self.root_offsets()[0] + (i*8)
            data = self.file_data[offset:offset + 8]
            data_offset = data[0:4]
            string_offset = data[4:8]
            nodes.append(Node(self, data_offset, string_offset))
        for i in range(self.root_counts()[1]):
            offset = self.root_offsets()[1] + (i*8)
            data = self.file_data[offset:offset + 8]
            data_offset = data[0:4]
            string_offset = data[4:8]
            nodes.append(Node(self, data_offset, string_offset))
        return nodes

    def string_table_offset(self):
        return self.root_offsets()[1] + self.root_counts()[1] * 8
    # Fighter DAT Specific stuff
    def ft_node(self):
        for node in self.get_nodes():
            if b'ftData' in node.name:
                return node
        print("No ftData node was found.")

    def ft_start_offset(self):
        return to_word(self.ft_node().data_offset)

    def ft_header(self):
        offset = self.ft_start_offset()
        return self.data_block[offset:offset + 24]

    def ft_attributes_offset(self):
        return to_word(self.ft_header(), 5)

    def ft_attributes_end(self):
        return to_word(self.ft_header(), 4)

    def ft_subactions_offset(self):
        return to_word(self.ft_header(), 2)

    def ft_subactions_end(self):
        return to_word(self.ft_header(), 0)

    def get_attribute_data(self):
        return self.data_block[self.ft_attributes_offset():self.ft_attributes_end()]

    def get_subaction_data(self):
        return self.data_block[self.ft_subactions_offset():self.ft_subactions_end()]
    
    def write_subaction_data(self, data):
        self.file_data[self.ft_subactions_offset()+0x20:self.ft_subactions_end()+0x20] = data

    def ft_subaction_count(self):
        return len(self.get_subaction_data()) // 24

    def get_special_attribute_data(self, special_attribute_block_size):
        return self.data_block[self.ft_attributes_end():self.ft_attributes_end()+special_attribute_block_size]

    def get_article_data(self, fighter):
        articles_datas = []
        for i in range(len(fighter.articles_offsets)):
            articles_datas.append(self.data_block[fighter.articles_offsets[i]:fighter.articles_offsets[i]+fighter.articles_sizes[i]])
        return articles_datas

    def get_subactions(self):
        subactions = []
        subaction_data = self.get_subaction_data() 
        for i in range(self.ft_subaction_count()):
            subaction = Subaction(subaction_data[i*24:i*24+24], self, i)
            subactions.append(subaction)
        return subactions

fst = FST(get_fst())

