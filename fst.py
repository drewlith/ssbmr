import iso
from util import to_word

# Modifies ISO file, retrieves and replaces files, and creates new ISO.

STRING_TABLE_OFFSET = 0x38D0 # Is there a way to calculate this offset?
# Would be useful for implementing Akaneia support.
ENTRY_SIZE = 0x0C

class ISOFile: # Contains FST data, and File data
    def __init__(self, data):
        self.entry_data = data
        self.file_data = None # Added via get_files()

    @property
    def type(self):
        if self.entry_data[0] == 0:
            return "File"
        return "Directory"

    @property
    def name(self):
        fst = iso.get_fst()
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

def get_files():
    fst = iso.get_fst()
    entries = []
    offset = 0
    while True: # Create Entries
        if offset >= STRING_TABLE_OFFSET:
            break
        entries.append(ISOFile(fst[offset:offset + ENTRY_SIZE]))
        offset += ENTRY_SIZE

    for entry in entries: # Add file data
        if entry.type == "File":
            end_of_file = entry.size + entry.offset
            entry.file_data = iso.iso_data[entry.offset:end_of_file]

    return entries

def write_files(files):
    last_offset = 0
    for file in files:
        if file.type == "File":
            iso.iso_data[file.offset:file.offset+file.size] = file.file_data
            if file.offset + file.size > last_offset:
                last_offset = file.offset + file.size
    # Fill the rest of the iso with zeroes.
    data = iso.iso_data[:last_offset] 
    free_space = bytearray(iso.MAX_CAPACITY - last_offset)
    data.extend(free_space)
    iso.iso_data = data

def export_file(file): # Probably won't be used, but is cool!
    name = file.name.decode()
    export = open(name, 'wb')
    export.write(file.file_data)
    export.close()

def find_file(files, name):
    if len(files) <= 0:
        print("Error: No file entries!")
    for file in files:
        if name in file.name:
            return file
    print("No file found with name:", name)

def replace_file(files, name, new_file_path):
    new_file = open(new_file_path, 'rb')
    new_file_data = new_file.read()
    new_file.close()
    
    file = find_file(files, name)
    if file == None:
        return
    old_size = file.size
    old_offset = file.offset
    file.size = len(new_file_data)

    offset_adjust = old_size - file.size
    offset_adjust += offset_adjust % 0x20 # Keeps it word-aligned

    file.file_data = new_file_data

    for f in files:
        if f.offset > old_offset:
            f.offset = f.offset - offset_adjust

def write_fst(files):
    fst = iso.get_fst()
    offset = 0
    for file in files: # Create Entries
        fst[offset:offset + ENTRY_SIZE] = file.entry_data
        offset += ENTRY_SIZE
    iso.iso_data[iso.fst_offset():iso.fst_offset() + iso.fst_size()] = fst

def build_iso(files):
    replace_file(files, b'MvHowto.mth', "none.mth") # Frees up space
    replace_file(files, b'MvOmake15.mth', "none.mth")
    write_fst(files)
    write_files(files)
    new_melee = open("output.iso", "wb")
    new_melee.write(iso.iso_data)
    new_melee.close()
    # Clean up
    iso.iso_data = None
