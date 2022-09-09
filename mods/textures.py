# Custom Texture mod by drewlith.

import random, melee
from os import listdir
from os.path import exists

def randomize(path, file):
    if not exists(path):
        print("Path not found! " + path)
        return ""
    files = listdir(path)
    customs = []
    credits_file_path = ""
    for i in range(len(files)): # Separate credits files and texture files
        if ".usd" in files[i] or ".dat" in files[i]:
            if ".txt" not in files[i]:
                customs.append(files[i])
    if len (customs) == 0: return
    rng = random.randint(0, len(customs)-1)
    credits_file_path = customs[rng][:-4] + ".txt"
    melee.replace_file(file, path + "/" + customs[rng])
    print(customs[rng])
    if exists(path + "/" + credits_file_path):
        credits_file = open(path + "/" + credits_file_path, "r")
        credits_file.close()
        return credits_file.read() + "\n\n"
    return ""
    
def custom_textures(output_dir = None):
    credits_file = ""
    credits_file += randomize("data/Bowser/Black", b'PlKpBk.dat') # Bowser
    credits_file += randomize("data/Bowser/Blue", b'PlKpBu.dat')
    credits_file += randomize("data/Bowser/Red", b'PlKpRe.dat')

    credits_file += randomize("data/Captain Falcon/Blue", b'PlCaBu.dat') # Falcon
    credits_file += randomize("data/Captain Falcon/Gray", b'PlCaGy.dat')
    credits_file += randomize("data/Captain Falcon/Green", b'PlCaGr.dat')
    credits_file += randomize("data/Captain Falcon/Red", b'PlCaRe.usd')
    credits_file += randomize("data/Captain Falcon/White", b'PlCaWh.dat')

    credits_file += randomize("data/DK/Black", b'PlDkBk.dat') # DK
    credits_file += randomize("data/DK/Blue", b'PlDkBu.dat')
    credits_file += randomize("data/DK/Green", b'PlDkGr.dat')
    credits_file += randomize("data/DK/Red", b'PlDkRe.dat')

    credits_file += randomize("data/Dr Mario/Black", b'PlDrBk.dat') # Dr Mario
    credits_file += randomize("data/Dr Mario/Blue", b'PlDrBu.dat')
    credits_file += randomize("data/Dr Mario/Green", b'PlDrGr.dat')
    credits_file += randomize("data/Dr Mario/Red", b'PlDrRe.dat')

    credits_file += randomize("data/Falco/Blue", b'PlFcBu.dat') # Falco
    credits_file += randomize("data/Falco/Green", b'PlFcGr.dat')
    credits_file += randomize("data/Falco/Red", b'PlFcRe.dat')

    credits_file += randomize("data/Fox/Green", b'PlFxGr.dat') # Fox
    credits_file += randomize("data/Fox/Lavender", b'PlFxLa.dat')
    credits_file += randomize("data/Fox/Orange", b'PlFxOr.dat')

    credits_file += randomize("data/Ganondorf/Blue", b'PlGnBu.dat') # Ganondorf
    credits_file += randomize("data/Ganondorf/Green", b'PlGnGr.dat')
    credits_file += randomize("data/Ganondorf/Lavender", b'PlGnLa.dat')
    credits_file += randomize("data/Ganondorf/Red", b'PlGnRe.dat')

    credits_file += randomize("data/Jigglypuff/Blue", b'PlPrBu.dat') # Jigglypuff
    credits_file += randomize("data/Jigglypuff/Green", b'PlPrGr.dat')
    credits_file += randomize("data/Jigglypuff/Red", b'PlPrRe.dat')
    credits_file += randomize("data/Jigglypuff/Yellow", b'PlPrYe.dat')

    credits_file += randomize("data/Link/Black", b'PlLkBk.dat') # Link
    credits_file += randomize("data/Link/Blue", b'PlLkBu.dat')
    credits_file += randomize("data/Link/Red", b'PlLkRe.dat')
    credits_file += randomize("data/Link/White", b'PlLkWh.dat')

    credits_file += randomize("data/Luigi/Aqua", b'PlLgAq.dat') # Luigi
    credits_file += randomize("data/Luigi/Pink", b'PlLgPi.dat')
    credits_file += randomize("data/Luigi/White", b'PlLgWh.dat')

    credits_file += randomize("data/Mario/Black", b'PlMrBk.dat') # Mario
    credits_file += randomize("data/Mario/Blue", b'PlMrBu.dat')
    credits_file += randomize("data/Mario/Green", b'PlMrGr.dat')
    credits_file += randomize("data/Mario/Yellow", b'PlMrYe.dat')

    credits_file += randomize("data/Marth/Black", b'PlMsBk.dat') # Marth
    credits_file += randomize("data/Marth/Green", b'PlMsGr.dat')
    credits_file += randomize("data/Marth/Red", b'PlMsRe.dat')
    credits_file += randomize("data/Marth/White", b'PlMsWh.dat')

    credits_file += randomize("data/Mewtwo/Blue", b'PlMtBu.dat') # Mewtwo
    credits_file += randomize("data/Mewtwo/Green", b'PlMtGr.dat')
    credits_file += randomize("data/Mewtwo/Red", b'PlMtRe.dat')

    credits_file += randomize("data/Nana/Aqua", b'PlNnAq.dat') # Nana
    credits_file += randomize("data/Nana/White", b'PlNnWh.dat')
    credits_file += randomize("data/Nana/Yellow", b'PlNnYe.dat')

    credits_file += randomize("data/Ness/Blue", b'PlNsBu.dat') # Ness
    credits_file += randomize("data/Ness/Green", b'PlNsGr.dat')
    credits_file += randomize("data/Ness/Yellow", b'PlNsYe.dat')

    credits_file += randomize("data/Peach/Blue", b'PlPeBu.dat') # Peach
    credits_file += randomize("data/Peach/Green", b'PlPeGr.dat')
    credits_file += randomize("data/Peach/White", b'PlPeWh.dat')
    credits_file += randomize("data/Peach/Yellow", b'PlPeYe.dat')

    credits_file += randomize("data/Pichu/Blue", b'PlPcBu.dat') # Pichu
    credits_file += randomize("data/Pichu/Green", b'PlPcGr.dat')
    credits_file += randomize("data/Pichu/Red", b'PlPcRe.dat')

    credits_file += randomize("data/Pikachu/Blue", b'PlPkBu.dat') # Pikachu
    credits_file += randomize("data/Pikachu/Green", b'PlPkGr.dat')
    credits_file += randomize("data/Pikachu/Red", b'PlPkRe.dat')

    credits_file += randomize("data/Popo/Green", b'PlPpGr.dat') # Popo
    credits_file += randomize("data/Popo/Orange", b'PlPpOr.dat')
    credits_file += randomize("data/Popo/Red", b'PlPpRe.dat')

    credits_file += randomize("data/Roy/Blue", b'PlFeBu.dat') # Roy
    credits_file += randomize("data/Roy/Green", b'PlFeGr.dat')
    credits_file += randomize("data/Roy/Red", b'PlFeRe.dat')
    credits_file += randomize("data/Roy/Yellow", b'PlFeYe.dat')

    credits_file += randomize("data/Samus/Black", b'PlSsBk.dat') # Samus
    credits_file += randomize("data/Samus/Green", b'PlSsGr.dat')
    credits_file += randomize("data/Samus/Lavender", b'PlSsLa.dat')
    credits_file += randomize("data/Samus/Pink", b'PlSsPi.dat')

    credits_file += randomize("data/Sheik/Blue", b'PlSkBu.dat') # Sheik
    credits_file += randomize("data/Sheik/Green", b'PlSkGr.dat')
    credits_file += randomize("data/Sheik/Red", b'PlSkRe.dat')
    credits_file += randomize("data/Sheik/White", b'PlSkWh.dat')

    credits_file += randomize("data/Yoshi/Aqua", b'PlYsAq.dat') # Yoshi
    credits_file += randomize("data/Yoshi/Blue", b'PlYsBu.dat')
    credits_file += randomize("data/Yoshi/Pink", b'PlYsPi.dat')
    credits_file += randomize("data/Yoshi/Red", b'PlYsRe.dat')
    credits_file += randomize("data/Yoshi/Yellow", b'PlYsYe.dat')

    credits_file += randomize("data/Young Link/Black", b'PlClBk.dat') # Young Link
    credits_file += randomize("data/Young Link/Blue", b'PlClBu.dat')
    credits_file += randomize("data/Young Link/Red", b'PlClRe.dat')
    credits_file += randomize("data/Young Link/White", b'PlClWh.dat')

    credits_file += randomize("data/Zelda/Blue", b'PlZdBu.dat') # Zelda
    credits_file += randomize("data/Zelda/Green", b'PlZdGr.dat')
    credits_file += randomize("data/Zelda/Red", b'PlZdRe.dat')
    credits_file += randomize("data/Zelda/White", b'PlZdWh.dat')

    credits_file += randomize("data/stages/bf", b'GrNBa.dat') # Battlefield
    credits_file += randomize("data/stages/dl", b'GrOp.dat') # Dreamland
    credits_file += randomize("data/stages/fd", b'GrNLa.dat') # FD
    credits_file += randomize("data/stages/fod", b'GrIz.dat') # Fountain
    credits_file += randomize("data/stages/ps", b'GrPs.usd') # Stadium
    credits_file += randomize("data/stages/ys", b'GrSt.dat') # Yoshi's

    credits_file += randomize("data/css", b'MnSlChr.usd') # CSS
    credits_file += randomize("data/stageselect", b'MnSlMap.usd') # Stage Select

    if len (credits_file) == 0: return
    if output_dir == None: return
    path = output_dir.replace(".iso", "-credits.txt")
    credits_output = open(path, "w")
    credits_output.write(credits_file)
    credits_output.close()
    
