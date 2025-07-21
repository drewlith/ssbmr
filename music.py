import iso, random
from os import listdir
from os.path import exists

BF_PATH = "music/battlefield"
BONUS_PATH = "music/bonus"
BOSS_PATH = "music/boss"
CHIPTUNE_PATH = "music/chiptune"
CHIPTUNE_INTENSE_PATH = "music/chiptuneintense"
DEPTHS_PATH = "music/depths"
DK_PATH = "music/dk"
FANFARE_PATH = "music/fanfare"
FD_PATH = "music/final"
FE_PATH = "music/fireemblem"
FOUNTAIN_PATH = "music/fountain"
FZERO_PATH = "music/fzero"
GAMEOVER_PATH = "music/gameover"
ICE_PATH = "music/ice"
KIRBY_PATH = "music/kirby"
MARIO_PATH = "music/mario"
MENU_PATH = "music/menu"
METROID_PATH = "music/metroid"
MOTHER_PATH = "music/mother"
OPENING_PATH = "music/opening"
POKEMON_PATH = "music/pokemon"
SIREN_PATH = "music/siren"
SLEEP_PATH = "music/sleep"
STARFOX_PATH = "music/starfox"
YOSHI_PATH = "music/yoshi"
YOUNG_PATH = "music/young"
ZELDA_PATH = "music/zelda"

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
    iso.replace_file(file, path + "/" + songs[rng])
    used_songs.append(songs[rng])
    return songs[rng]

def specific_music(path, file):
    iso.replace_file(file, path)

def custom_music():
    if not exists("music"):
        return
    used_songs.clear()

    random_music(BF_PATH, b'hyaku.hps')
    random_music(BF_PATH, b'sp_metal.hps')
    random_music(BF_PATH, b'sp_zako.hps')
    random_music(BONUS_PATH, b'target.hps')
    random_music(BONUS_PATH, b'menu02.hps')
    random_music(BOSS_PATH, b'sp_giga.hps')
    song = random_music(CHIPTUNE_PATH, b'inis1_01.hps')
    if len(song) > 0:
        specific_music(CHIPTUNE_INTENSE_PATH + "/" + song, b'inis1_02.hps')
    else:
        print("MUSIC ERROR???")
    song = random_music(CHIPTUNE_PATH, b'inis2_01.hps')
    if len(song) > 0:
        specific_music(CHIPTUNE_INTENSE_PATH + "/" + song, b'inis2_02.hps')
    else:
        print("MUSIC ERROR???")
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
