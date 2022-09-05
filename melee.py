# Wrapper to get data from iso and perform tasks on iso
import util, os.path, fighter, attack, throw, hitbox, random

fst = bytearray() # Contains pointers to all ISO files and their names and sizes
fst_files = [] # All the FST Files

############# Import melee into other scripts to have access to this useful data
fighters = []
attacks = []
items = []
throws = []
hitboxes = []

attack_tiers = [[],[],[],[],[],[],[],[],[],[],[]] # For balance
item_tiers = [[],[],[],[],[],[],[],[],[],[],[]]
#############

def open_iso(iso_path):
    file = open(iso_path, "rb")
    return file
    
def read_data(data, offset, length):
    new_data = bytearray()
    new_data.extend(data[offset:offset+length])
    return new_data
    
def write_data(data, offset, new_data):
    data[offset:offset+len(new_data)] = new_data

class FST_File(): # This class represents an entry in the fst AND the associated file
    def __init__(self, fst_data, fst_offset):
        self.fst_data = fst_data
        self.fst_offset = fst_offset
        self.file_data = bytearray()

    def get_file_name(self):
        name_offset = read_data(self.fst_data, 1, 3) # 0x01-0x03 is offset to filename in string table
        offset = util.get_value(name_offset,0,3*8)
        offset += 0x38D0 # Start of string table
        name = bytearray()
        i = 0
        
        while True:
            if fst[offset+i] != 0:
                name.append(fst[offset + i])
                i += 1
            else:
                return name

    def get_file_offset(self): #0x4 - 0x8
        offset_data = read_data(self.fst_data, 4, 4)
        offset = util.get_value(offset_data, 0, 4*8)
        return offset

    def set_file_offset(self, offset):
        offset_data = read_data(self.fst_data, 4, 4)
        offset_data = util.set_value(offset_data, 0, 4*8, offset)
        write_data(self.fst_data, 4, offset_data)

    def get_file_length(self): #0x8 - 0x12
        length_data = read_data(self.fst_data, 8, 4)
        length = util.get_value(length_data, 0, 4*8)
        return length

    def set_file_length(self, length):
        length_data = read_data(self.fst_data, 8, 4)
        length_data = util.set_value(length_data, 0, 4*8, length)
        write_data(self.fst_data, 8, length_data)
    
def get_files_from_fst(): # Fills fst_files[] with data using fst
    fst_files.clear()
    i = 0
    while i < 0x38D0: # Size of File/Directory Block
        file_data = bytearray()
        for k in range(12): # Size of 1 File/Directory
            file_data.append(fst[k+i])
        if file_data[0] == 0: # If the header = 0, it's a file. 1 is a Directory
            fst_files.append(FST_File(file_data, i))
        i += 12

def write_files_to_fst(): # Writes updated fst back to disc
    for f in fst_files:
        write_data(fst, f.fst_offset, f.fst_data)

def sort_fst_files_by_offset(): # Files must be in the same order as vanilla for it to boot
    sorted_fst = util.merge_sort(fst_files)
    fst_files.clear()
    for f in sorted_fst:
        fst_files.append(f)

def read_game_files(melee_iso):
    for f in fst_files:
        melee_iso.seek(f.get_file_offset())
        f.file_data = bytearray(melee_iso.read(f.get_file_length()))

def build_iso(melee, output_path):
    melee.seek(0)
    new_iso = open(output_path, "wb")
    new_iso.write(melee.read(0x456E00))
    new_iso.seek(0x456E00)
    new_iso.write(fst)
    for f in fst_files:
        new_iso.seek(f.get_file_offset())
        new_iso.write(f.file_data)
    new_iso.close()

    new_iso = open(output_path, "ab")
    new_iso.write(bytearray((os.path.getsize(output_path) % 0x20) + 0x20)) # Disc fails to read if size isn't divisible by 0x20, with a 0x20 pad
    new_iso.close()

def find_file(name):
    for f in fst_files:
        if name in f.get_file_name():
            return f
    print("Couldn't find file of name: ", name)

def replace_file(name, new_file_path):
    file = find_file(name)
    if file != None: # Overwrite file data  
        new_file = open(new_file_path, "rb") # Get data from new file
        new_file_data = new_file.read()
        new_file.close()

        old_length = file.get_file_length() # Change length in fst
        old_offset = file.get_file_offset()
        file.set_file_length(len(new_file_data))

        offset_adjustment = old_length - file.get_file_length() # Calculate offset adjustment
        offset_adjustment += offset_adjustment % 0x20

        for f in fst_files:
            if f.get_file_offset() > old_offset: # For any offset greater than thi
                new_offset = f.get_file_offset() - offset_adjustment
                f.set_file_offset(new_offset) # Adjust the offset

        file.file_data = new_file_data # Update file data for file

def replace_file_data(name, data): # Like replace file but it can just be data, for shuffling
    file = find_file(name)

    old_length = file.get_file_length() # Change length in fst
    old_offset = file.get_file_offset()
    file.set_file_length(len(data))

    offset_adjustment = old_length - file.get_file_length() # Calculate offset adjustment
    offset_adjustment += offset_adjustment % 0x20

    for f in fst_files:
        if f.get_file_offset() > old_offset: # For any offset greater than thi
            new_offset = f.get_file_offset() - offset_adjustment
            f.set_file_offset(new_offset) # Adjust the offset

    file.file_data = data # Update file data for file

class DAT():
    def __init__(self, fst_file):
        self.fst_file = fst_file
        self.header = read_data(fst_file.file_data, 0, 0x20) # Header is 32 bytes. Then Data Block starts
        self.data = read_data(fst_file.file_data, 0x20, self.data_block_size()) # Grabs the entire data block and puts it in to self.data

    def data_block_size(self):
        block_size_data = read_data(self.header, 0x04, 4)
        return util.get_value(self.header, 0, 32)

def get_fighter_data(): # Gets data from Fighters about their moves from offsets given by .json files.
    fighters.clear()
    fighters.append(fighter.Fighter("Bowser", DAT(find_file(b'PlKp.dat')), 13892))
    fighters.append(fighter.Fighter("Captain Falcon", DAT(find_file(b'PlCa.dat')), 14196))
    fighters.append(fighter.Fighter("DK", DAT(find_file(b'PlDk.dat')), 14768))
    fighters.append(fighter.Fighter("Dr Mario", DAT(find_file(b'PlDr.dat')), 13632))
    fighters.append(fighter.Fighter("Falco", DAT(find_file(b'PlFc.dat')), 14308))
    fighters.append(fighter.Fighter("Fox", DAT(find_file(b'PlFx.dat')), 14100))
    fighters.append(fighter.Fighter("Game & Watch", DAT(find_file(b'PlGw.dat')), 13844))
    fighters.append(fighter.Fighter("Ganondorf", DAT(find_file(b'PlGn.dat')), 14108))
    fighters.append(fighter.Fighter("Popo", DAT(find_file(b'PlPp.dat')), 12964))
    fighters.append(fighter.Fighter("Nana", DAT(find_file(b'PlNn.dat')), 4488))
    fighters.append(fighter.Fighter("Jigglypuff", DAT(find_file(b'PlPr.dat')), 14524))
    fighters.append(fighter.Fighter("Kirby", DAT(find_file(b'PlKb.dat')), 19688))
    fighters.append(fighter.Fighter("Link", DAT(find_file(b'PlLk.dat')), 13308))
    fighters.append(fighter.Fighter("Luigi", DAT(find_file(b'PlLg.dat')), 13216))
    fighters.append(fighter.Fighter("Mario", DAT(find_file(b'PlMr.dat')), 13016))
    fighters.append(fighter.Fighter("Marth", DAT(find_file(b'PlMs.dat')), 14148))
    fighters.append(fighter.Fighter("Mewtwo", DAT(find_file(b'PlMt.dat')), 14160))
    fighters.append(fighter.Fighter("Ness", DAT(find_file(b'PlNs.dat')), 13536))
    fighters.append(fighter.Fighter("Peach", DAT(find_file(b'PlPe.dat')), 14484))
    fighters.append(fighter.Fighter("Pichu", DAT(find_file(b'PlPc.dat')), 13396))
    fighters.append(fighter.Fighter("Pikachu", DAT(find_file(b'PlPk.dat')), 13700))
    fighters.append(fighter.Fighter("Roy", DAT(find_file(b'PlFe.dat')), 14492))
    fighters.append(fighter.Fighter("Samus", DAT(find_file(b'PlSs.dat')), 13444))
    fighters.append(fighter.Fighter("Sheik", DAT(find_file(b'PlSk.dat')), 13336))
    fighters.append(fighter.Fighter("Yoshi", DAT(find_file(b'PlYs.dat')), 13148))
    fighters.append(fighter.Fighter("Young Link", DAT(find_file(b'PlCl.dat')), 13728))
    fighters.append(fighter.Fighter("Zelda", DAT(find_file(b'PlZd.dat')), 14324))

    fighters.append(fighter.Fighter("Male Wireframe", DAT(find_file(b'PlBo.dat')), 12744))
    fighters.append(fighter.Fighter("Female Wireframe", DAT(find_file(b'PlGl.dat')), 12276))
    fighters.append(fighter.Fighter("Giga Bowser", DAT(find_file(b'PlGk.dat')), 13520))
    fighters.append(fighter.Fighter("Master Hand", DAT(find_file(b'PlMh.dat')), 2356))
    fighters.append(fighter.Fighter("Crazy Hand", DAT(find_file(b'PlCh.dat')), 2232))

    fighters.append(fighter.Fighter("Items", DAT(find_file(b'ItCo.usd')), 0))

    attacks.clear()
    throws.clear()
    hitboxes.clear()
    for f in fighters:
        f.attacks.clear()
        f.throws.clear()
        data = f.get_json_data()
        for key in data:
            if "Type" in data[key] and "Strength" in data[key]:  # Get Attacks
                a = attack.Attack(f, key)
                a.type = data[key]["Type"]
                f.attacks.append(a)
                attacks.append(a)
            elif "Throw" in data[key]:  # Get throws
                t = throw.Throw(key, f)
                t.offset = f.get_json_data()[key]["Throw"]["Offset"]
                t.data = read_data(f.dat.fst_file.file_data, t.offset, 12)
                t.original_owner = f.name
                throws.append(t)
                f.throws.append(t)
                
        for a in f.attacks: # Get hitbox data from attacks
            if a.attack_name in data:
                a.strength = data[a.attack_name]["Strength"]
                a.type = data[a.attack_name]["Type"]
                for key in data[a.attack_name]:
                    if "Hitbox" in key:
                        hb = hitbox.Hitbox(key)
                        hb.offset = data[a.attack_name][key]["Offset"]
                        hb.data = read_data(f.dat.fst_file.file_data, hb.offset, 20)
                        a.hitboxes.append(hb)
                        hitboxes.append(hb)
            a.record_original_stats()
        for t in f.throws:
            t.record_original_stats()
        if f.properties_offset > 0:
            f.property_data = read_data(f.dat.fst_file.file_data, f.properties_offset, 2236) # Get Attributes
            f.record_original_stats()

def write_fighter_data(): # Writes everything to new iso data.
    for f in fighters:
        if f.properties_offset > 0:
            write_data(f.dat.fst_file.file_data, f.properties_offset, f.property_data) # Attributes
        for t in f.throws:
            write_data(f.dat.fst_file.file_data, t.offset, t.data) # Throws
        for a in f.attacks:
            for hb in a.hitboxes:
                write_data(f.dat.fst_file.file_data, hb.offset, hb.data) # All hitboxes

def find_fighter(name):
    for f in fighters:
        if name == f.name:
            return f

def sort_attacks(): # Puts attacks into strength tiers and separates items
    throws.clear()
    attacks.clear()
    items.clear()
    for t in attack_tiers:
        t.clear()
    for t in item_tiers:
        t.clear()
    for f in fighters:
        for a in f.attacks:
            if "Item" not in a.type:
                attack_tiers[a.strength].append(a)
                attacks.append(a)
            else:
                item_tiers[a.strength].append(a)
                items.append(a)
        for t in f.throws:
            throws.append(t)

def start(iso_path):
    fst.clear()
    melee = open_iso(iso_path)
    melee.seek(0x456E00)
    fst.extend(melee.read(0x7529))
    get_files_from_fst()
    sort_fst_files_by_offset()
    read_game_files(melee)
    melee.close()
    replace_file(b'MvHowto.mth', "data/none.mth") # Delete Movies
    replace_file(b'MvOmake15.mth', "data/none.mth")
    get_fighter_data()
    sort_attacks()

def end(iso_path, output_path):
    write_fighter_data()
    write_files_to_fst()
    melee = open_iso(iso_path)
    build_iso(melee, output_path)
    melee.close()
    fst_files.clear()
