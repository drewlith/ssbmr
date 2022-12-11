# Wrapper to get data from iso and perform tasks on iso
# Special Thanks: DRGN
import os.path, random, os, subprocess
from util import *
from dat import DAT
from fst import FST
from dol import DOL
from fighter import Fighter

############# Import melee into other scripts to have access to this useful data
fighters = []
boss_fighters = []
items = None
#############

fst_file = None
dol_file = None

def find_file(name):
    global fst_file
    for f in fst_file.files:
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

        for f in fst_file.files:
            if f.get_file_offset() > old_offset: # For any offset greater than thi
                new_offset = f.get_file_offset() - offset_adjustment
                f.set_file_offset(new_offset) # Adjust the offset

        file.file_data = new_file_data # Update file data for file

def get_fighter_data():
    fighters.clear()
    fighters.append(Fighter("Bowser", DAT(find_file(b'PlKp.dat'))))
    fighters.append(Fighter("Captain Falcon", DAT(find_file(b'PlCa.dat'))))
    fighters.append(Fighter("Donkey Kong", DAT(find_file(b'PlDk.dat'))))
    fighters.append(Fighter("Dr Mario", DAT(find_file(b'PlDr.dat'))))
    fighters.append(Fighter("Falco", DAT(find_file(b'PlFc.dat'))))
    fighters.append(Fighter("Fox", DAT(find_file(b'PlFx.dat'))))
    fighters.append(Fighter("Mr. Game & Watch", DAT(find_file(b'PlGw.dat'))))
    fighters.append(Fighter("Ganondorf", DAT(find_file(b'PlGn.dat'))))
    fighters.append(Fighter("Popo", DAT(find_file(b'PlPp.dat'))))
    fighters.append(Fighter("Nana", DAT(find_file(b'PlNn.dat'))))
    fighters.append(Fighter("Jigglypuff", DAT(find_file(b'PlPr.dat'))))
    fighters.append(Fighter("Kirby", DAT(find_file(b'PlKb.dat'))))
    fighters.append(Fighter("Link", DAT(find_file(b'PlLk.dat'))))
    fighters.append(Fighter("Luigi", DAT(find_file(b'PlLg.dat'))))
    fighters.append(Fighter("Mario", DAT(find_file(b'PlMr.dat'))))
    fighters.append(Fighter("Marth", DAT(find_file(b'PlMs.dat'))))
    fighters.append(Fighter("Mewtwo", DAT(find_file(b'PlMt.dat'))))
    fighters.append(Fighter("Ness", DAT(find_file(b'PlNs.dat'))))
    fighters.append(Fighter("Peach", DAT(find_file(b'PlPe.dat'))))
    fighters.append(Fighter("Pichu", DAT(find_file(b'PlPc.dat'))))
    fighters.append(Fighter("Pikachu", DAT(find_file(b'PlPk.dat'))))
    fighters.append(Fighter("Roy", DAT(find_file(b'PlFe.dat'))))
    fighters.append(Fighter("Samus", DAT(find_file(b'PlSs.dat'))))
    fighters.append(Fighter("Sheik", DAT(find_file(b'PlSk.dat'))))
    fighters.append(Fighter("Yoshi", DAT(find_file(b'PlYs.dat'))))
    fighters.append(Fighter("Young Link", DAT(find_file(b'PlCl.dat'))))
    fighters.append(Fighter("Zelda", DAT(find_file(b'PlZd.dat'))))

    boss_fighters.append(Fighter("Boy", DAT(find_file(b'PlBo.dat'))))
    boss_fighters.append(Fighter("Girl", DAT(find_file(b'PlGl.dat'))))
    boss_fighters.append(Fighter("Giga Koopa", DAT(find_file(b'PlGk.dat'))))
    boss_fighters.append(Fighter("Master Hand", DAT(find_file(b'PlMh.dat'))))
    boss_fighters.append(Fighter("Crazy Hand", DAT(find_file(b'PlCh.dat'))))

    items = DAT(find_file(b'ItCo.usd'))

def write_fighter_data():
    for fighter in fighters:
        for attack in fighter.attacks:
            for hb in attack.hitboxes:
                write_data(fighter.dat.data_block, hb.offset, hb.data)
        for throw in fighter.throws:
            write_data(fighter.dat.data_block, throw.offset, throw.data)
        for sound in fighter.sounds:
            write_data(fighter.dat.data_block, sound.offset, sound.data)
        #for loop in fighter.loops:
            #write_data(fighter.dat.data_block, loop.offset, loop.data)
        #for timer in fighter.timers:
            #write_data(fighter.dat.data_block, timer.offset, timer.data)
        fighter.write_attribute_data()
        write_data(fighter.dat.data_block, fighter.attribute_offset, fighter.attribute_data)
        write_data(fighter.dat.data_block, fighter.attribute_end, fighter.fighter_specific_attr_data)
        fighter.dat.write_to_fst()

def find_fighter(name):
    for f in fighters:
        if name == f.name:
            return f
    for f in boss_fighters:
        if name == f.name:
            return f

def start(iso_path):
    global fst_file
    global dol_file
    melee = open(iso_path, "rb")
    fst_file = FST(melee)
    dol_file = DOL(melee)
    melee.close()
    replace_file(b'MvHowto.mth', "data/none.mth") # Delete Movies
    replace_file(b'MvOmake15.mth', "data/none.mth")
    get_fighter_data()

def end(iso_path, output_path, code = ""):
    global fst_file
    global dol_file
    write_fighter_data()
    fst_file.write_files_to_fst()
    melee = open(iso_path, "rb")
    melee.seek(0)
    new_iso = open(output_path, "wb")
    new_iso.write(melee.read(0x456E00))
    new_iso.seek(0x1E800)
    new_iso.write(dol_file.data)
    new_iso.seek(0x456E00)
    new_iso.write(fst_file.data)
    for f in fst_file.files:
        new_iso.seek(f.get_file_offset())
        new_iso.write(f.file_data)
    #new_iso.write(bytearray((os.path.getsize(output_path) % 0x20) + 0x20)) # Disc fails to read if size isn't divisible by 0x20, with a 0x20 pad
    melee.seek(0, os.SEEK_END)
    melee_size = melee.tell()
    new_size = new_iso.tell()
    new_iso.write(bytearray(melee_size - new_size)) # Make size same as vanilla for it to be a valid GC ISO and not NKIT
    melee.close()
    new_iso.close()
    # Create Xdelta
    if len(code) > 0:
        try:
            # Linux
            subprocess.run(['xdelta3', '-S', '-e', '-B 1430679552', '-s', iso_path, output_path, "seeds/" + code + ".xdelta"])
        except:
            # Windows
            subprocess.run('xdelta.exe -S -e -B 1430679552 -s ' + iso_path + ' ' + output_path + ' ' + "seeds/" + code + '.xdelta')
        os.remove(output_path)
    fst_file.clear_fst()
    dol_file.clear_dol()
    fighters.clear()
    boss_fighters.clear()
    del(fst_file)
    del(dol_file)
