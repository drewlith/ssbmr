# Custom Texture mod by drewlith.

import random, iso
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
    if len (customs) == 0: return ""
    rng = random.randint(0, len(customs)-1)
    credits_file_path = customs[rng][:-4] + ".txt"
    iso.replace_file(file, path + "/" + customs[rng])
    print(customs[rng])
    if exists(path + "/" + credits_file_path):
        credits_file = open(path + "/" + credits_file_path, "r")
        output = credits_file.read() + "\n\n"
        credits_file.close()
        return output
    return ""
    
def custom_textures(output_dir = None):
    credits_file = ""
    
    credits_file += randomize("Textures/Bowser/Black", b'PlKpBk.dat') # Bowser
    credits_file += randomize("Textures/Bowser/Blue", b'PlKpBu.dat')
    credits_file += randomize("Textures/Bowser/Red", b'PlKpRe.dat')
    credits_file += randomize("Textures/Bowser/Neutral", b'PlKpNr.dat') 

    credits_file += randomize("Textures/Captain Falcon/Blue", b'PlCaBu.dat') # Falcon
    credits_file += randomize("Textures/Captain Falcon/Gray", b'PlCaGy.dat')
    credits_file += randomize("Textures/Captain Falcon/Green", b'PlCaGr.dat')
    credits_file += randomize("Textures/Captain Falcon/Red", b'PlCaRe.usd')
    credits_file += randomize("Textures/Captain Falcon/White", b'PlCaWh.dat')
    credits_file += randomize("Textures/Captain Falcon/Neutral", b'PlCaNr.dat')

    credits_file += randomize("Textures/DK/Black", b'PlDkBk.dat') # DK
    credits_file += randomize("Textures/DK/Blue", b'PlDkBu.dat')
    credits_file += randomize("Textures/DK/Green", b'PlDkGr.dat')
    credits_file += randomize("Textures/DK/Red", b'PlDkRe.dat')
    credits_file += randomize("Textures/DK/Neutral", b'PlDkNr.dat')

    credits_file += randomize("Textures/Dr Mario/Black", b'PlDrBk.dat') # Dr Mario
    credits_file += randomize("Textures/Dr Mario/Blue", b'PlDrBu.dat')
    credits_file += randomize("Textures/Dr Mario/Green", b'PlDrGr.dat')
    credits_file += randomize("Textures/Dr Mario/Red", b'PlDrRe.dat')
    credits_file += randomize("Textures/Dr Mario/Neutral", b'PlDrNr.dat')

    credits_file += randomize("Textures/Falco/Blue", b'PlFcBu.dat') # Falco
    credits_file += randomize("Textures/Falco/Green", b'PlFcGr.dat')
    credits_file += randomize("Textures/Falco/Red", b'PlFcRe.dat')
    credits_file += randomize("Textures/Falco/Neutral", b'PlFcNr.dat')

    credits_file += randomize("Textures/Fox/Green", b'PlFxGr.dat') # Fox
    credits_file += randomize("Textures/Fox/Lavender", b'PlFxLa.dat')
    credits_file += randomize("Textures/Fox/Orange", b'PlFxOr.dat')
    credits_file += randomize("Textures/Fox/Neutral", b'PlFxNr.dat')

    credits_file += randomize("Textures/Ganondorf/Blue", b'PlGnBu.dat') # Ganondorf
    credits_file += randomize("Textures/Ganondorf/Green", b'PlGnGr.dat')
    credits_file += randomize("Textures/Ganondorf/Lavender", b'PlGnLa.dat')
    credits_file += randomize("Textures/Ganondorf/Red", b'PlGnRe.dat')
    credits_file += randomize("Textures/Ganondorf/Neutral", b'PlGnNr.dat')

    credits_file += randomize("Textures/Jigglypuff/Blue", b'PlPrBu.dat') # Jigglypuff
    credits_file += randomize("Textures/Jigglypuff/Green", b'PlPrGr.dat')
    credits_file += randomize("Textures/Jigglypuff/Red", b'PlPrRe.dat')
    credits_file += randomize("Textures/Jigglypuff/Yellow", b'PlPrYe.dat')
    credits_file += randomize("Textures/Jigglypuff/Neutral", b'PlPrNr.dat')

    credits_file += randomize("Textures/Link/Black", b'PlLkBk.dat') # Link
    credits_file += randomize("Textures/Link/Blue", b'PlLkBu.dat')
    credits_file += randomize("Textures/Link/Red", b'PlLkRe.dat')
    credits_file += randomize("Textures/Link/White", b'PlLkWh.dat')
    credits_file += randomize("Textures/Link/Neutral", b'PlLkNr.dat')

    credits_file += randomize("Textures/Luigi/Aqua", b'PlLgAq.dat') # Luigi
    credits_file += randomize("Textures/Luigi/Pink", b'PlLgPi.dat')
    credits_file += randomize("Textures/Luigi/White", b'PlLgWh.dat')
    credits_file += randomize("Textures/Luigi/Neutral", b'PlLgNr.dat')

    credits_file += randomize("Textures/Mario/Black", b'PlMrBk.dat') # Mario
    credits_file += randomize("Textures/Mario/Blue", b'PlMrBu.dat')
    credits_file += randomize("Textures/Mario/Green", b'PlMrGr.dat')
    credits_file += randomize("Textures/Mario/Yellow", b'PlMrYe.dat')
    credits_file += randomize("Textures/Mario/Neutral", b'PlMrNr.dat')

    credits_file += randomize("Textures/Marth/Black", b'PlMsBk.dat') # Marth
    credits_file += randomize("Textures/Marth/Green", b'PlMsGr.dat')
    credits_file += randomize("Textures/Marth/Red", b'PlMsRe.dat')
    credits_file += randomize("Textures/Marth/White", b'PlMsWh.dat')
    credits_file += randomize("Textures/Marth/Neutral", b'PlMsNr.dat')

    credits_file += randomize("Textures/Mewtwo/Blue", b'PlMtBu.dat') # Mewtwo
    credits_file += randomize("Textures/Mewtwo/Green", b'PlMtGr.dat')
    credits_file += randomize("Textures/Mewtwo/Red", b'PlMtRe.dat')
    credits_file += randomize("Textures/Mewtwo/Neutral", b'PlMtNr.dat')

    credits_file += randomize("Textures/Nana/Aqua", b'PlNnAq.dat') # Nana
    credits_file += randomize("Textures/Nana/White", b'PlNnWh.dat')
    credits_file += randomize("Textures/Nana/Yellow", b'PlNnYe.dat')
    credits_file += randomize("Textures/Nana/Neutral", b'PlNnNr.dat')

    credits_file += randomize("Textures/Ness/Blue", b'PlNsBu.dat') # Ness
    credits_file += randomize("Textures/Ness/Green", b'PlNsGr.dat')
    credits_file += randomize("Textures/Ness/Yellow", b'PlNsYe.dat')
    credits_file += randomize("Textures/Ness/Neutral", b'PlNsNr.dat')

    credits_file += randomize("Textures/Peach/Blue", b'PlPeBu.dat') # Peach
    credits_file += randomize("Textures/Peach/Green", b'PlPeGr.dat')
    credits_file += randomize("Textures/Peach/White", b'PlPeWh.dat')
    credits_file += randomize("Textures/Peach/Yellow", b'PlPeYe.dat')
    credits_file += randomize("Textures/Peach/Neutral", b'PlPeNr.dat')

    credits_file += randomize("Textures/Pichu/Blue", b'PlPcBu.dat') # Pichu
    credits_file += randomize("Textures/Pichu/Green", b'PlPcGr.dat')
    credits_file += randomize("Textures/Pichu/Red", b'PlPcRe.dat')
    credits_file += randomize("Textures/Pichu/Neutral", b'PlPcNr.dat')

    credits_file += randomize("Textures/Pikachu/Blue", b'PlPkBu.dat') # Pikachu
    credits_file += randomize("Textures/Pikachu/Green", b'PlPkGr.dat')
    credits_file += randomize("Textures/Pikachu/Red", b'PlPkRe.dat')
    credits_file += randomize("Textures/Pikachu/Neutral", b'PlPkNr.dat')

    credits_file += randomize("Textures/Popo/Green", b'PlPpGr.dat') # Popo
    credits_file += randomize("Textures/Popo/Orange", b'PlPpOr.dat')
    credits_file += randomize("Textures/Popo/Red", b'PlPpRe.dat')
    credits_file += randomize("Textures/Popo/Neutral", b'PlPpNr.dat')

    credits_file += randomize("Textures/Roy/Blue", b'PlFeBu.dat') # Roy
    credits_file += randomize("Textures/Roy/Green", b'PlFeGr.dat')
    credits_file += randomize("Textures/Roy/Red", b'PlFeRe.dat')
    credits_file += randomize("Textures/Roy/Yellow", b'PlFeYe.dat')
    credits_file += randomize("Textures/Roy/Neutral", b'PlFeNr.dat')

    credits_file += randomize("Textures/Samus/Black", b'PlSsBk.dat') # Samus
    credits_file += randomize("Textures/Samus/Green", b'PlSsGr.dat')
    credits_file += randomize("Textures/Samus/Lavender", b'PlSsLa.dat')
    credits_file += randomize("Textures/Samus/Pink", b'PlSsPi.dat')
    credits_file += randomize("Textures/Samus/Neutral", b'PlSsNr.dat')

    credits_file += randomize("Textures/Sheik/Blue", b'PlSkBu.dat') # Sheik
    credits_file += randomize("Textures/Sheik/Green", b'PlSkGr.dat')
    credits_file += randomize("Textures/Sheik/Red", b'PlSkRe.dat')
    credits_file += randomize("Textures/Sheik/White", b'PlSkWh.dat')
    credits_file += randomize("Textures/Sheik/Neutral", b'PlSkNr.dat')

    credits_file += randomize("Textures/Yoshi/Aqua", b'PlYsAq.dat') # Yoshi
    credits_file += randomize("Textures/Yoshi/Blue", b'PlYsBu.dat')
    credits_file += randomize("Textures/Yoshi/Pink", b'PlYsPi.dat')
    credits_file += randomize("Textures/Yoshi/Red", b'PlYsRe.dat')
    credits_file += randomize("Textures/Yoshi/Yellow", b'PlYsYe.dat')
    credits_file += randomize("Textures/Yoshi/Neutral", b'PlYsNr.dat')

    credits_file += randomize("Textures/Young Link/Black", b'PlClBk.dat') # Young Link
    credits_file += randomize("Textures/Young Link/Blue", b'PlClBu.dat')
    credits_file += randomize("Textures/Young Link/Red", b'PlClRe.dat')
    credits_file += randomize("Textures/Young Link/White", b'PlClWh.dat')
    credits_file += randomize("Textures/Young Link/Neutral", b'PlClNr.dat')

    credits_file += randomize("Textures/Zelda/Blue", b'PlZdBu.dat') # Zelda
    credits_file += randomize("Textures/Zelda/Green", b'PlZdGr.dat')
    credits_file += randomize("Textures/Zelda/Red", b'PlZdRe.dat')
    credits_file += randomize("Textures/Zelda/White", b'PlZdWh.dat')
    credits_file += randomize("Textures/Zelda/Neutral", b'PlZdNr.dat')

    credits_file += randomize("Textures/stages/Battlefield", b'GrNBa.dat') # Battlefield
    credits_file += randomize("Textures/stages/Dreamland", b'GrOp.dat') # Dreamland
    credits_file += randomize("Textures/stages/Final Destination", b'GrNLa.dat') # FD
    credits_file += randomize("Textures/stages/Fountain of Dreams", b'GrIz.dat') # Fountain
    credits_file += randomize("Textures/stages/Pokemon Stadium", b'GrPs.usd') # Stadium
    credits_file += randomize("Textures/stages/Yoshi's Story", b'GrSt.dat') # Yoshi's
    credits_file += randomize("Textures/stages/Brinstar Depths", b'GrKr.dat') # Brinstar Depths
    credits_file += randomize("Textures/stages/Corneria", b'GrCn.dat') # Corneria
    credits_file += randomize("Textures/stages/Fourside", b'GrFs.dat') # Fourside
    credits_file += randomize("Textures/stages/Hyrule Temple", b'GrSh.dat') # Temple
    #credits_file += randomize("Textures/stages/Kongo Jungle", b'GrKg.dat') # Kongo Jungle
    credits_file += randomize("Textures/stages/Mushroom Kingdom", b'GrI1.dat') # Mushroom Kingdom
    #credits_file += randomize("Textures/stages/Onett", b'GrOt.dat') # Onett
    credits_file += randomize("Textures/stages/Poke Floats", b'GrPu.dat') # Poke Floats
    #credits_file += randomize("Textures/stages/Princess Peach's Castle", b'GrCs.dat') # Castle
    #credits_file += randomize("Textures/stages/Great Bay", b'GrGb.dat') # Great Bay
    #credits_file += randomize("Textures/stages/Green Greens", b'GrGr.dat') # Green Greens
    #credits_file += randomize("Textures/stages/Jungle Japes", b'GrGd.dat') # Jungle Japes
    #credits_file += randomize("Textures/stages/Kongo Jungle N64", b'GrOk.dat') # Kongo N64
    #credits_file += randomize("Textures/stages/Mute City", b'GrMc.dat') # Mute City
    #credits_file += randomize("Textures/stages/Poke Floats", b'GrGr.dat') # Poke Floats
    #credits_file += randomize("Textures/stages/Rainbow Cruise", b'GrRc.dat') # Rainbow Cruise
    #credits_file += randomize("Textures/stages/Yoshi's Island", b'GrYt.dat') # Yoshi's Island
    
    credits_file += randomize("Textures/CSS", b'MnSlChr.usd') # CSS
    credits_file += randomize("Textures/Stage Select", b'MnSlMap.usd') # Stage Select

    if len (credits_file) == 0: return
    if output_dir == None: return
    path = output_dir.replace(".iso", "-credits.txt")
    credits_output = open(path, "w")
    credits_output.write(credits_file)
    credits_output.close()
    
