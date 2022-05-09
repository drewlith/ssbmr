import random, melee
from os import listdir
from os.path import exists

all_credits = ""

def randomize(path, file):
    global all_credits
    files = listdir(path)
    customs = []
    credits_file_path = ""
    for i in range(len(files)):
        if ".hps" or ".usd" or ".dat" in files[i]:
            if ".txt" not in files[i]:
                customs.append(files[i])
    if len (customs) == 0: return
    rng = random.randint(0, len(customs)-1)
    credits_file_path = customs[rng] + ".txt"
    melee.replace_file(file, path + "/" + customs[rng])
    if exists(path + "/" + credits_file_path):
        credits_file = open(path + "/" + credits_file_path, "r")
        all_credits += credits_file.read() + "\n\n"
        credits_file.close()
    
def random_all(seed, output_dir):
    random.seed(seed)
    random_textures()
    random_stages()
    random_music()
    random_misc()
    if len (all_credits) == 0: return
    path = output_dir.replace(".iso", "-credits.txt")
    credits_output = open(path, "w")
    credits_output.write(all_credits)
    credits_output.close()

def random_textures():
    randomize("data/Bowser/Black", b'PlKpBk.dat') # Bowser
    randomize("data/Bowser/Blue", b'PlKpBu.dat')
    randomize("data/Bowser/Red", b'PlKpRe.dat')

    randomize("data/Captain Falcon/Blue", b'PlCaBu.dat') # Falcon
    randomize("data/Captain Falcon/Gray", b'PlCaGy.dat')
    randomize("data/Captain Falcon/Green", b'PlCaGr.dat')
    randomize("data/Captain Falcon/Red", b'PlCaRe.usd')
    randomize("data/Captain Falcon/White", b'PlCaWh.dat')

    randomize("data/DK/Black", b'PlDkBk.dat') # DK
    randomize("data/DK/Blue", b'PlDkBu.dat')
    randomize("data/DK/Green", b'PlDkGr.dat')
    randomize("data/DK/Red", b'PlDkRe.dat')

    randomize("data/Dr Mario/Black", b'PlDrBk.dat') # Dr Mario
    randomize("data/Dr Mario/Blue", b'PlDrBu.dat')
    randomize("data/Dr Mario/Green", b'PlDrGr.dat')
    randomize("data/Dr Mario/Red", b'PlDrRe.dat')

    randomize("data/Falco/Blue", b'PlFcBu.dat') # Falco
    randomize("data/Falco/Green", b'PlFcGr.dat')
    randomize("data/Falco/Red", b'PlFcRe.dat')

    randomize("data/Fox/Green", b'PlFxGr.dat') # Fox
    randomize("data/Fox/Lavender", b'PlFxLa.dat')
    randomize("data/Fox/Orange", b'PlFxOr.dat')

    randomize("data/Ganondorf/Blue", b'PlGnBu.dat') # Ganondorf
    randomize("data/Ganondorf/Green", b'PlGnGr.dat')
    randomize("data/Ganondorf/Lavender", b'PlGnLa.dat')
    randomize("data/Ganondorf/Red", b'PlGnRe.dat')

    randomize("data/Jigglypuff/Blue", b'PlPrBu.dat') # Jigglypuff
    randomize("data/Jigglypuff/Green", b'PlPrGr.dat')
    randomize("data/Jigglypuff/Red", b'PlPrRe.dat')
    randomize("data/Jigglypuff/Yellow", b'PlPrYe.dat')

    randomize("data/Link/Black", b'PlLkBk.dat') # Link
    randomize("data/Link/Blue", b'PlLkBu.dat')
    randomize("data/Link/Red", b'PlLkRe.dat')
    randomize("data/Link/White", b'PlLkWh.dat')

    randomize("data/Luigi/Aqua", b'PlLgAq.dat') # Luigi
    randomize("data/Luigi/Pink", b'PlLgPi.dat')
    randomize("data/Luigi/White", b'PlLgWh.dat')

    randomize("data/Mario/Black", b'PlMrBk.dat') # Mario
    randomize("data/Mario/Blue", b'PlMrBu.dat')
    randomize("data/Mario/Green", b'PlMrGr.dat')
    randomize("data/Mario/Yellow", b'PlMrYe.dat')

    randomize("data/Marth/Black", b'PlMsBk.dat') # Marth
    randomize("data/Marth/Green", b'PlMsGr.dat')
    randomize("data/Marth/Red", b'PlMsRe.dat')
    randomize("data/Marth/White", b'PlMsWh.dat')

    randomize("data/Mewtwo/Blue", b'PlMtBu.dat') # Mewtwo
    randomize("data/Mewtwo/Green", b'PlMtGr.dat')
    randomize("data/Mewtwo/Red", b'PlMtRe.dat')

    randomize("data/Nana/Aqua", b'PlNnAq.dat') # Nana
    randomize("data/Nana/White", b'PlNnWh.dat')
    randomize("data/Nana/Yellow", b'PlNnYe.dat')

    randomize("data/Ness/Blue", b'PlNsBu.dat') # Ness
    randomize("data/Ness/Green", b'PlNsGr.dat')
    randomize("data/Ness/Yellow", b'PlNsYe.dat')

    randomize("data/Peach/Blue", b'PlPeBu.dat') # Peach
    randomize("data/Peach/Green", b'PlPeGr.dat')
    randomize("data/Peach/White", b'PlPeWh.dat')
    randomize("data/Peach/Yellow", b'PlPeYe.dat')

    randomize("data/Pichu/Blue", b'PlPcBu.dat') # Pichu
    randomize("data/Pichu/Green", b'PlPcGr.dat')
    randomize("data/Pichu/Red", b'PlPcRe.dat')

    randomize("data/Pikachu/Blue", b'PlPkBu.dat') # Pikachu
    randomize("data/Pikachu/Green", b'PlPkGr.dat')
    randomize("data/Pikachu/Red", b'PlPkRe.dat')

    randomize("data/Popo/Green", b'PlPpGr.dat') # Popo
    randomize("data/Popo/Orange", b'PlPpOr.dat')
    randomize("data/Popo/Red", b'PlPpRe.dat')

    randomize("data/Roy/Blue", b'PlFeBu.dat') # Roy
    randomize("data/Roy/Green", b'PlFeGr.dat')
    randomize("data/Roy/Red", b'PlFeRe.dat')
    randomize("data/Roy/Yellow", b'PlFeYe.dat')

    randomize("data/Samus/Black", b'PlSsBk.dat') # Samus
    randomize("data/Samus/Green", b'PlSsGr.dat')
    randomize("data/Samus/Lavender", b'PlSsLa.dat')
    randomize("data/Samus/Pink", b'PlSsPi.dat')

    randomize("data/Sheik/Blue", b'PlSkBu.dat') # Sheik
    randomize("data/Sheik/Green", b'PlSkGr.dat')
    randomize("data/Sheik/Red", b'PlSkRe.dat')
    randomize("data/Sheik/White", b'PlSkWh.dat')

    randomize("data/Yoshi/Aqua", b'PlYsAq.dat') # Yoshi
    randomize("data/Yoshi/Blue", b'PlYsBu.dat')
    randomize("data/Yoshi/Pink", b'PlYsPi.dat')
    randomize("data/Yoshi/Red", b'PlYsRe.dat')
    randomize("data/Yoshi/Yellow", b'PlYsYe.dat')

    randomize("data/Young Link/Black", b'PlClBk.dat') # Young Link
    randomize("data/Young Link/Blue", b'PlClBu.dat')
    randomize("data/Young Link/Red", b'PlClRe.dat')
    randomize("data/Young Link/White", b'PlClWh.dat')

    randomize("data/Zelda/Blue", b'PlZdBu.dat') # Zelda
    randomize("data/Zelda/Green", b'PlZdGr.dat')
    randomize("data/Zelda/Red", b'PlZdRe.dat')
    randomize("data/Zelda/White", b'PlZdWh.dat')

def random_stages():
    randomize("data/stages/bf", b'GrNBa.dat') # Battlefield
    randomize("data/stages/dl", b'GrOp.dat') # Dreamland
    randomize("data/stages/fd", b'GrNLa.dat') # FD
    randomize("data/stages/fod", b'GrIz.dat') # Fountain
    randomize("data/stages/ps", b'GrPs.usd') # Stadium
    randomize("data/stages/ys", b'GrSt.dat') # Yoshi's

def random_music():
    randomize("data/music/gameover", b'continue.hps')
    randomize("data/music/stage", b'hyaku.hps')
    randomize("data/music/stage", b'hyaku2.hps')
    randomize("data/music/stage", b'izumi.hps')
    randomize("data/music/menu", b'menu01.hps')
    randomize("data/music/menu", b'menu02.hps')
    randomize("data/music/menu", b'menu3.hps')
    randomize("data/music/stage", b'old_kb.hps')
    randomize("data/music/opening", b'opening.hps')
    randomize("data/music/stage", b'pokesta.hps')
    randomize("data/music/stage", b'pstadium.hps')
    randomize("data/music/stage", b'pura.hps')
    randomize("data/music/stage", b'sp_end.hps')
    randomize("data/music/boss", b'sp_giga.hps')
    randomize("data/music/boss", b'sp_metal.hps')
    randomize("data/music/stage", b'sp_zako.hps')
    randomize("data/music/stage", b'target.hps')
    randomize("data/music/stage", b'ystory.hps')

def random_misc():
    randomize("data/css", b'MnSlChr.usd') # CSS
    randomize("data/stageselect", b'MnSlMap.usd') # Stage Select


    
