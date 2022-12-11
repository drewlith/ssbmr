import melee, random
from os import listdir
from os.path import exists

BF_PATH = "data/music/battlefield"
BONUS_PATH = "data/music/bonus"
BOSS_PATH = "data/music/boss"
CHIPTUNE_PATH = "data/music/chiptune"
CHIPTUNE_INTENSE_PATH = "data/music/chiptuneintense"
DEPTHS_PATH = "data/music/depths"
DK_PATH = "data/music/dk"
FANFARE_PATH = "data/music/fanfare"
FD_PATH = "data/music/final"
FE_PATH = "data/music/fireemblem"
FOUNTAIN_PATH = "data/music/fountain"
FZERO_PATH = "data/music/fzero"
GAMEOVER_PATH = "data/music/gameover"
ICE_PATH = "data/music/ice"
KIRBY_PATH = "data/music/kirby"
MARIO_PATH = "data/music/mario"
MENU_PATH = "data/music/menu"
METROID_PATH = "data/music/metroid"
MOTHER_PATH = "data/music/mother"
OPENING_PATH = "data/music/opening"
POKEMON_PATH = "data/music/pokemon"
SIREN_PATH = "data/music/siren"
SLEEP_PATH = "data/music/sleep"
STARFOX_PATH = "data/music/starfox"
YOSHI_PATH = "data/music/yoshi"
YOUNG_PATH = "data/music/young"
ZELDA_PATH = "data/music/zelda"

used_songs = []

def random_music(path, file, attempts = 0):
    if not exists(path):
        print("Path not found! " + path)
        return ""
    songs = listdir(path)
    if len(songs) == 0:
        return ""
    rng = random.randint(0, len(songs)-1)
    for song in used_songs: # Make songs unique
        if song == songs[rng] and attempts < 10: # Attempts break infinite loop
            random_music(path, file, attempts + 1)
            return ""
    print(songs[rng])
    melee.replace_file(file, path + "/" + songs[rng])
    used_songs.append(songs[rng])
    return songs[rng]

def specific_music(path, file):
    melee.replace_file(file, path)

def custom_music():
    if not exists("data/music"):
        return
    used_songs.clear()
    random_music(BF_PATH, b'hyaku.hps')
    random_music(BF_PATH, b'sp_metal.hps')
    random_music(BF_PATH, b'sp_zako.hps')
    random_music(BONUS_PATH, b'target.hps')
    random_music(BONUS_PATH, b'menu02.hps')
    random_music(BOSS_PATH, b'sp_giga.hps')
    song = random_music(CHIPTUNE_PATH, b'inis1_01.hps')
    specific_music(CHIPTUNE_INTENSE_PATH + "/" + song, b'inis1_02.hps')
    song = random_music(CHIPTUNE_PATH, b'inis2_01.hps')
    specific_music(CHIPTUNE_INTENSE_PATH + "/" + song, b'inis2_02.hps')
    random_music(CHIPTUNE_PATH, b'mrider.hps')
    random_music(CHIPTUNE_PATH, b'baloon.hps')
    random_music(CHIPTUNE_PATH, b'flatzone.hps')
    random_music(DEPTHS_PATH, b'kraid.hps')
    random_music(DK_PATH, b'garden.hps')
    random_music(DK_PATH, b'kongo.hps')
    random_music(DK_PATH, b'old_dk.hps')
    random_music(FE_PATH, b'akaneia.hps')
    random_music(FD_PATH, b'hyaku2.hps')
    random_music(FD_PATH, b'sp_end.hps')
    random_music(FOUNTAIN_PATH, b'izumi.hps')
    random_music(FZERO_PATH, b'mutecity.hps')
    random_music(FZERO_PATH, b'bigblue.hps')
    random_music(GAMEOVER_PATH, b'continue.hps')
    random_music(ICE_PATH, b'icemt.hps')
    random_music(KIRBY_PATH, b'old_kb.hps')
    random_music(KIRBY_PATH, b'greens.hps')
    random_music(MARIO_PATH, b'docmari.hps')
    random_music(MARIO_PATH, b'rcruise.hps')
    random_music(MARIO_PATH, b'castle.hps')
    random_music(MARIO_PATH, b'smari3.hps')
    random_music(MENU_PATH, b'menu01.hps')
    random_music(MENU_PATH, b'menu3.hps')
    random_music(METROID_PATH, b'zebes.hps')
    random_music(MOTHER_PATH, b'fourside.hps')
    random_music(MOTHER_PATH, b'onetto.hps')
    random_music(MOTHER_PATH, b'onetto2.hps')
    random_music(OPENING_PATH, b'opening.hps')
    random_music(POKEMON_PATH, b'pokesta.hps')
    random_music(POKEMON_PATH, b'pstadium.hps')
    random_music(POKEMON_PATH, b'pura.hps')
    random_music(SIREN_PATH, b'siren.hps')
    random_music(SLEEP_PATH, b'1p_qk.hps')
    random_music(STARFOX_PATH, b'corneria.hps')
    random_music(STARFOX_PATH, b'venom.hps')
    random_music(YOSHI_PATH, b'ystory.hps')
    random_music(YOSHI_PATH, b'yorster.hps')
    random_music(YOSHI_PATH, b'old_ys.hps')
    random_music(YOUNG_PATH, b'saria.hps')
    random_music(ZELDA_PATH, b'shrine.hps')
    random_music(ZELDA_PATH, b'greatbay.hps')
