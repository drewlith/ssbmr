# Wrapper to get data from iso and perform tasks on iso
import util, os.path, fighter, attack, throw, hitbox

fst = bytearray() # Contains pointers to all ISO files and their names and sizes
fst_files = [] # All the FST Files
custom_only = False
############# Import melee into other scripts to have access to this useful data
fighters = []
attacks = []
throws = []
hitboxes = []
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
        offset_adjustment += offset_adjustment % 4

        for f in fst_files:
            if f.get_file_offset() > old_offset: # For any offset greater than thi
                new_offset = f.get_file_offset() - offset_adjustment
                f.set_file_offset(new_offset) # Adjust the offset

        file.file_data = new_file_data # Update file data for file

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
                f.attacks.append(a)
                attacks.append(a)
            elif "Throw" in data[key]:  # Get throws
                t = throw.Throw(key)
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

        if f.properties_offset > 0:
            f.property_data = read_data(f.dat.fst_file.file_data, f.properties_offset, 384) # Get Attributes

def write_fighter_data(): # Writes everything to new iso data.
    for f in fighters:
        if f.properties_offset > 0:
            write_data(f.dat.fst_file.file_data, f.properties_offset, f.property_data) # Attributes
        for t in f.throws:
            write_data(f.dat.fst_file.file_data, t.offset, t.data) # Throws
        for a in f.attacks:
            for hb in a.hitboxes:
                write_data(f.dat.fst_file.file_data, hb.offset, hb.data) # All hitboxes

def custom_content_test():
    replace_file(b'PlKpBk.dat', "data/Bowser/Black/PlKpBk-Fury.dat") # Bowser
    replace_file(b'PlKpBu.dat', "data/Bowser/Blue/PlKpBu-blue.dat")
    replace_file(b'PlKpRe.dat', "data/Bowser/Red/PlKpRe-hooktail.dat")

    replace_file(b'PlCaBu.dat', "data/Captain Falcon/Blue/PlCaBu-blackblue.dat") # Falcon
    replace_file(b'PlCaGy.dat', "data/Captain Falcon/Gray/PlCaGy-batman.dat")
    replace_file(b'PlCaGr.dat', "data/Captain Falcon/Green/PlCaGr-ganon.dat")
    replace_file(b'PlCaRe.usd', "data/Captain Falcon/Red/PlCaRe-bulls.usd")
    replace_file(b'PlCaWh.dat', "data/Captain Falcon/White/PlCaWh-bronzekneecap.dat")

    replace_file(b'PlDkBk.dat', "data/DK/Black/PlDkBk-kingkong.dat") # DK
    replace_file(b'PlDkBu.dat', "data/DK/Blue/PlDkBu-sonic.dat")
    replace_file(b'PlDkGr.dat', "data/DK/Green/PlDkGr-brawl.dat")
    replace_file(b'PlDkRe.dat', "data/DK/Red/PlDkRe-boxing.dat")

    replace_file(b'PlDrBk.dat', "data/Dr Mario/Black/PlDrBk-cia.dat") # Dr Mario
    replace_file(b'PlDrBu.dat', "data/Dr Mario/Blue/PlDrBu-bluekhaki.dat")
    replace_file(b'PlDrGr.dat', "data/Dr Mario/Green/PlDrGr-greenkhaki.dat")
    replace_file(b'PlDrRe.dat', "data/Dr Mario/Red/PlDrRe-Crimson.dat")

    replace_file(b'PlFcBu.dat', "data/Falco/Blue/PlFcBu-adidas.dat") # Falco
    replace_file(b'PlFcGr.dat', "data/Falco/Green/PlFcGr-blackout.dat")
    replace_file(b'PlFcRe.dat', "data/Falco/Red/PlFcRe-bulls.dat")

    replace_file(b'PlFxGr.dat', "data/Fox/Green/PlFxGr-bucky.dat") # Fox
    replace_file(b'PlFxLa.dat', "data/Fox/Lavender/PlFxLa-ash.dat")
    replace_file(b'PlFxOr.dat', "data/Fox/Orange/PlFxOr-blaze.dat")

    replace_file(b'PlGnBu.dat', "data/Ganondorf/Blue/PlGnBu-C9.dat") # Ganon
    replace_file(b'PlGnGr.dat', "data/Ganondorf/Green/PlGnGr-apu.dat")
    replace_file(b'PlGnLa.dat', "data/Ganondorf/Lavender/PlGnLa-agent.dat")
    replace_file(b'PlGnRe.dat', "data/Ganondorf/Red/PlGnRe-christmas.dat")

    replace_file(b'PlPrBu.dat', "data/Jigglypuff/Blue/PlPrBu-bow.dat") # Puff
    replace_file(b'PlPrGr.dat', "data/Jigglypuff/Green/PlPrGr-alien.dat")
    replace_file(b'PlPrRe.dat', "data/Jigglypuff/Red/PlPrRe-albino.dat")
    replace_file(b'PlPrYe.dat', "data/Jigglypuff/Yellow/PlPrYe-c9.dat")

    replace_file(b'PlLkBk.dat', "data/Link/Black/PlLkBk-dark.dat") # Link
    replace_file(b'PlLkBu.dat', "data/Link/Blue/PlLkBu-botw.dat")
    replace_file(b'PlLkRe.dat', "data/Link/Red/PlLkRe-betweenworlds.dat")
    replace_file(b'PlLkWh.dat', "data/Link/White/PlLkWh-assassin.dat")

    replace_file(b'PlLgAq.dat', "data/Luigi/Aqua/PlLgAq-blue.dat") # Luigi
    replace_file(b'PlLgPi.dat', "data/Luigi/Pink/PlLgPi-casino.dat")
    replace_file(b'PlLgWh.dat', "data/Luigi/White/PlLgWh-casino.dat")

    replace_file(b'PlMrBk.dat', "data/Mario/Black/PlMrBk-captainsyrup.dat") # Mario
    replace_file(b'PlMrBu.dat', "data/Mario/Blue/PlMrBu-dark.dat")
    replace_file(b'PlMrGr.dat', "data/Mario/Green/PlMrGr-4pgolf.dat")
    replace_file(b'PlMrYe.dat', "data/Mario/Yellow/PlMrYe-fire.dat")

    replace_file(b'PlMsBk.dat', "data/Marth/Black/PlMsBk-bot.dat") # Marth
    replace_file(b'PlMsGr.dat', "data/Marth/Green/PlMsGr-capeless.dat")
    replace_file(b'PlMsRe.dat', "data/Marth/Red/PlMsRe-caesar.dat")
    replace_file(b'PlMsWh.dat', "data/Marth/White/PlMsWh-capeless.dat")

    replace_file(b'PlMtBu.dat', "data/Mewtwo/Blue/PlMtBu-cooler.dat") # Mewtwo
    replace_file(b'PlMtGr.dat', "data/Mewtwo/Green/PlMtGr-armor.dat")
    replace_file(b'PlMtRe.dat', "data/Mewtwo/Red/PlMtRe-redtail.dat")

    replace_file(b'PlNnAq.dat', "data/Nana/Aqua/PlNnAq-amongus.dat") # Nana
    replace_file(b'PlNnWh.dat', "data/Nana/White/PlNnWh-dreamland.dat")
    replace_file(b'PlNnYe.dat', "data/Nana/Yellow/PlNnYe-camo.dat")

    replace_file(b'PlNsBu.dat', "data/Ness/Blue/PlNsBu-blue.dat") # Ness
    replace_file(b'PlNsGr.dat', "data/Ness/Green/PlNsGr-chase.dat")
    replace_file(b'PlNsYe.dat', "data/Ness/Yellow/PlNsYe-charlie.dat")

    replace_file(b'PlPeBu.dat', "data/Peach/Blue/PlPeBu-alice.dat") # Peach
    replace_file(b'PlPeGr.dat', "data/Peach/Green/PlPeGr-arkel.dat")
    replace_file(b'PlPeWh.dat', "data/Peach/White/PlPeWh-agent.dat")
    replace_file(b'PlPeYe.dat', "data/Peach/Yellow/PlPeYe-arkel.dat")

    replace_file(b'PlPcBu.dat', "data/Pichu/Blue/PlPcBu-minun.dat") # Pichu
    replace_file(b'PlPcGr.dat', "data/Pichu/Green/PlPcGr-mimikyu.dat")
    replace_file(b'PlPcRe.dat', "data/Pichu/Red/PlPcRe-jirachi.dat")

    replace_file(b'PlPkBu.dat', "data/Pikachu/Blue/PlPkBu-axe.dat") # Pikachu
    replace_file(b'PlPkGr.dat', "data/Pikachu/Green/PlPkGr-alien.dat")
    replace_file(b'PlPkRe.dat', "data/Pikachu/Red/PlPkRe-ash.dat")

    replace_file(b'PlPpGr.dat', "data/Popo/Green/PlPpGr-camo.dat") # Popo
    replace_file(b'PlPpOr.dat', "data/Popo/Orange/PlPpOr-amongus.dat")
    replace_file(b'PlPpRe.dat', "data/Popo/Red/PlPpRe-dreamland.dat")

    replace_file(b'PlFeBu.dat', "data/Roy/Blue/PlFeBu-arkel.dat") # Roy
    replace_file(b'PlFeGr.dat', "data/Roy/Green/PlFeGr-arkel.dat")
    replace_file(b'PlFeRe.dat', "data/Roy/Red/PlFeRe-arkel.dat")
    replace_file(b'PlFeYe.dat', "data/Roy/Yellow/PlFeYe-arkel.dat")

    replace_file(b'PlSsBk.dat', "data/Samus/Black/PlSsBk-daftpunk.dat") # Samus
    replace_file(b'PlSsGr.dat', "data/Samus/Green/PlSsGr-better.dat")
    replace_file(b'PlSsLa.dat', "data/Samus/Lavender/PlSsLa-arwing.dat")
    replace_file(b'PlSsPi.dat', "data/Samus/Pink/PlSsPi-fusion.dat")

    replace_file(b'PlSkBu.dat', "data/Sheik/Blue/PlSkBu-greninja.dat") # Sheik
    replace_file(b'PlSkGr.dat', "data/Sheik/Green/PlSkGr-Cammy.dat")
    replace_file(b'PlSkRe.dat', "data/Sheik/Red/PlSkRe-DiZ.dat")
    replace_file(b'PlSkWh.dat', "data/Sheik/White/PlSkWh-goldwhite.dat")

    replace_file(b'PlYsAq.dat', "data/Yoshi/Aqua/PlYsAq-c9.dat") # Yoshi
    replace_file(b'PlYsBu.dat', "data/Yoshi/Blue/PlYsBu-boshi.dat")
    replace_file(b'PlYsPi.dat', "data/Yoshi/Pink/PlYsPi-magenta.dat")
    replace_file(b'PlYsRe.dat', "data/Yoshi/Red/PlYsRe-orange.dat")
    replace_file(b'PlYsYe.dat', "data/Yoshi/Yellow/PlYsYe-black.dat")

    replace_file(b'PlClBk.dat', "data/Young Link/Black/PlClBk-blackgreen.dat") # Young Link
    replace_file(b'PlClBu.dat', "data/Young Link/Blue/PlClBu-blueblack.dat")
    replace_file(b'PlClRe.dat', "data/Young Link/Red/PlClRe-orange.dat")
    replace_file(b'PlClWh.dat', "data/Young Link/White/PlClWh-fierce.dat")

    replace_file(b'PlZdBu.dat', "data/Zelda/Blue/PlZdBu-gown.dat") # Zelda
    replace_file(b'PlZdGr.dat', "data/Zelda/Green/PlZdGr-gown.dat")
    replace_file(b'PlZdRe.dat', "data/Zelda/Red/PlZdRe-bubblegum.dat")
    replace_file(b'PlZdWh.dat', "data/Zelda/White/PlZdWh-leffen.dat")

    # Stages
    replace_file(b'GrNBa.dat', "data/stages/bf/GrNBa-pink.dat") # Battlefield
    replace_file(b'GrOp.dat', "data/stages/dl/GrOp-mgs3.dat") # Dreamland
    replace_file(b'GrNLa.dat', "data/stages/fd/GrNLa-undertale.dat") # Final Destination
    replace_file(b'GrIz.dat', "data/stages/fod/GrIz-northernlights.dat") # Fountain of Dreams
    replace_file(b'GrPs.usd', "data/stages/ps/GrPs-riptide.usd") # Pokemon Stadium
    replace_file(b'GrSt.dat', "data/stages/ys/GrSt-peach.dat") # Yoshi's Story

    # Music, just use main menu to test
    music_path = "data/music/boss/Pokey Means Business!.hps"
    replace_file(b'menu01.hps', music_path)
    replace_file(b'menu02.hps', music_path)
    replace_file(b'menu3.hps', music_path)

    # Misc.
    replace_file(b'MnSlChr.usd', "data/css/MnSlChr-vapor.usd") # CSS
    replace_file(b'MnSlMap.usd', "data/stageselect/MnSlMap-vb.usd") # Stage Select
    
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
    #custom_content_test() # Comment in build
    if not custom_only:
        get_fighter_data()

def end(iso_path, output_path):
    if not custom_only:
        write_fighter_data()
    write_files_to_fst()
    melee = open_iso(iso_path)
    build_iso(melee, output_path)
    melee.close()
    fst_files.clear()
