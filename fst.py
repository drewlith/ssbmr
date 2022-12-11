from util import *

class FST():
    def __init__(self, iso, web=False): # iso is an opened .iso melee v1.02 file
        iso.seek(0x456E00)
        self.data = bytearray()
        self.data.extend(iso.read(0x7529))
        self.files = []
        self.get_files_from_fst()
        self.sort_fst_files_by_offset()
        self.read_game_files(iso)

    def get_files_from_fst(self): # Fills fst_files with data using fst
        self.files.clear()
        i = 0
        while i < 0x38D0: # Size of File/Directory Block
            file_data = bytearray()
            for k in range(12): # Size of 1 File/Directory
                file_data.append(self.data[k+i])
            if file_data[0] == 0: # If the header = 0, it's a file. 1 is a Directory
                self.files.append(FST_Entry(file_data, i, self))    
            i += 12

    def write_files_to_fst(self): # Writes updated fst back to disc
        for f in self.files:
            write_data(self.data, f.fst_offset, f.fst_data)

    def sort_fst_files_by_offset(self): # Files must be in the same order as vanilla for it to boot
        sorted_fst = merge_sort(self.files)
        self.files.clear()
        for f in sorted_fst:
            self.files.append(f)

    def read_game_files(self, iso, web=False):
        for f in self.files:
            iso.seek(f.get_file_offset())
            f.file_data = bytearray(iso.read(f.get_file_length()))

    def clear_fst(self):
        self.files.clear()

class FST_Entry(): # This class represents an entry in the fst AND the associated file
    def __init__(self, fst_data, fst_offset, fst):
        self.fst_data = fst_data
        self.fst_offset = fst_offset
        self.file_data = bytearray()
        self.fst = fst

    def get_file_name(self):
        name_offset = read_data(self.fst_data, 1, 3) # 0x01-0x03 is offset to filename in string table
        offset = get_value(name_offset,0,3*8)
        offset += 0x38D0 # Start of string table
        name = bytearray()
        i = 0
        
        while True:
            if self.fst.data[offset+i] != 0:
                name.append(self.fst.data[offset + i])
                i += 1
            else:
                return name

    def get_file_offset(self): #0x4 - 0x8
        offset_data = read_data(self.fst_data, 4, 4)
        offset = get_value(offset_data, 0, 4*8)
        return offset

    def set_file_offset(self, offset):
        offset_data = read_data(self.fst_data, 4, 4)
        offset_data = set_value(offset_data, 0, 4*8, offset)
        write_data(self.fst_data, 4, offset_data)

    def get_file_length(self): #0x8 - 0x12
        length_data = read_data(self.fst_data, 8, 4)
        length = get_value(length_data, 0, 4*8)
        return length

    def set_file_length(self, length):
        length_data = read_data(self.fst_data, 8, 4)
        length_data = set_value(length_data, 0, 4*8, length)
        write_data(self.fst_data, 8, length_data)


