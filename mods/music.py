import melee, random
from os import listdir
from os.path import exists

jingles = []
cutscenes = []
music = []

BF_PATH = "data/music/battlefield"
BONUS_PATH = "data/music/bonus"
BOSS_PATH = "data/music/boss"
CHIPTUNE_PATH = "data/music/chiptune"
DK_PATH = "data/music/dk"
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

def sort_music():
    jingles.append(melee.find_file(b's_newcom.hps'))
    jingles.append(melee.find_file(b's_new2.hps'))
    jingles.append(melee.find_file(b's_new1.hps'))
    jingles.append(melee.find_file(b's_info3.hps'))
    jingles.append(melee.find_file(b's_info2.hps'))
    jingles.append(melee.find_file(b's_info1.hps'))
    jingles.append(melee.find_file(b'intro_nm.hps'))
    jingles.append(melee.find_file(b'intro_es.hps'))
    jingles.append(melee.find_file(b'gameover.hps'))
    jingles.append(melee.find_file(b'ff_yoshi.hps'))
    jingles.append(melee.find_file(b'ff_step3.hps'))
    jingles.append(melee.find_file(b'ff_step2.hps'))
    jingles.append(melee.find_file(b'ff_step1.hps'))
    jingles.append(melee.find_file(b'ff_samus.hps'))
    jingles.append(melee.find_file(b'ff_poke.hps'))
    jingles.append(melee.find_file(b'ff_nes.hps'))
    jingles.append(melee.find_file(b'ff_mario.hps'))
    jingles.append(melee.find_file(b'ff_link.hps'))
    jingles.append(melee.find_file(b'ff_kirby.hps'))
    jingles.append(melee.find_file(b'ff_ice.hps'))
    jingles.append(melee.find_file(b'ff_fox.hps'))
    jingles.append(melee.find_file(b'ff_flat.hps'))
    jingles.append(melee.find_file(b'ff_fzero.hps'))
    jingles.append(melee.find_file(b'ff_emb.hps'))
    jingles.append(melee.find_file(b'ff_dk.hps'))
    jingles.append(melee.find_file(b'ff_1p02.hps'))
    jingles.append(melee.find_file(b'ff_1p01.hps'))
    jingles.append(melee.find_file(b'continue.hps'))

    cutscenes.append(melee.find_file(b'vl_last_v2.hps'))
    cutscenes.append(melee.find_file(b'vl_fzero.hps'))
    cutscenes.append(melee.find_file(b'vl_figure2.hps'))
    cutscenes.append(melee.find_file(b'vl_figure1.hps'))
    cutscenes.append(melee.find_file(b'vl_cosmos.hps'))
    cutscenes.append(melee.find_file(b'vl_corneria.hps'))
    cutscenes.append(melee.find_file(b'vl_castle.hps'))
    cutscenes.append(melee.find_file(b'vl_battle.hps'))

    music.append(melee.find_file(b'1p_qk.hps'))
    music.append(melee.find_file(b'akaneia.hps'))
    music.append(melee.find_file(b'baloon.hps'))
    music.append(melee.find_file(b'bigblue.hps'))
    music.append(melee.find_file(b'castle.hps'))
    music.append(melee.find_file(b'corneria.hps'))
    music.append(melee.find_file(b'docmari.hps'))
    music.append(melee.find_file(b'flatzone.hps'))
    music.append(melee.find_file(b'garden.hps'))
    music.append(melee.find_file(b'greatbay.hps'))
    music.append(melee.find_file(b'greens.hps'))
    music.append(melee.find_file(b'howto.hps'))
    music.append(melee.find_file(b'howto_s.hps'))
    music.append(melee.find_file(b'hyaku.hps'))
    music.append(melee.find_file(b'hyaku2.hps'))
    music.append(melee.find_file(b'icemt.hps'))
    music.append(melee.find_file(b'inis1_01.hps'))
    music.append(melee.find_file(b'inis2_01.hps'))
    music.append(melee.find_file(b'inis1_02.hps'))
    music.append(melee.find_file(b'inis2_02.hps'))
    music.append(melee.find_file(b'item_h.hps'))
    music.append(melee.find_file(b'item_s.hps'))
    music.append(melee.find_file(b'izumi.hps'))
    music.append(melee.find_file(b'kongo.hps'))
    music.append(melee.find_file(b'kraid.hps'))
    music.append(melee.find_file(b'menu01.hps'))
    music.append(melee.find_file(b'menu3.hps'))
    music.append(melee.find_file(b'menu02.hps'))
    music.append(melee.find_file(b'mrider.hps'))
    music.append(melee.find_file(b'mutecity.hps'))
    music.append(melee.find_file(b'old_dk.hps'))
    music.append(melee.find_file(b'old_kb.hps'))
    music.append(melee.find_file(b'old_ys.hps'))
    music.append(melee.find_file(b'onetto.hps'))
    music.append(melee.find_file(b'onetto2.hps'))
    music.append(melee.find_file(b'opening.hps'))
    music.append(melee.find_file(b'pokesta.hps'))
    music.append(melee.find_file(b'pstadium.hps'))
    music.append(melee.find_file(b'pura.hps'))
    music.append(melee.find_file(b'rcruise.hps'))
    music.append(melee.find_file(b'saria.hps'))
    music.append(melee.find_file(b'sp_end.hps'))
    music.append(melee.find_file(b'sp_giga.hps'))
    music.append(melee.find_file(b'sp_metal.hps'))
    music.append(melee.find_file(b'sp_zako.hps'))
    music.append(melee.find_file(b'shrine.hps'))
    music.append(melee.find_file(b'siren.hps'))
    music.append(melee.find_file(b'smari3.hps'))
    music.append(melee.find_file(b'target.hps'))
    music.append(melee.find_file(b'venom.hps'))
    music.append(melee.find_file(b'vs_hyou1.hps'))
    music.append(melee.find_file(b'vs_hyou2.hps'))
    music.append(melee.find_file(b'yorster.hps'))
    music.append(melee.find_file(b'ystory.hps'))
    music.append(melee.find_file(b'zebes.hps'))
    
def shuffle_jingle(jingle):
    temp = bytearray()
    temp.extend(jingle.file_data)
    target = random.randint(0, len(jingles)-1)
    melee.replace_file_data(jingle.get_file_name(), jingles[target].file_data)
    melee.replace_file_data(jingles[target].get_file_name(), temp)

def shuffle_cutscene(track):
    temp = bytearray()
    temp.extend(track.file_data)
    target = random.randint(0, len(cutscenes)-1)
    melee.replace_file_data(track.get_file_name(), cutscenes[target].file_data)
    melee.replace_file_data(cutscenes[target].get_file_name(), temp)
    
def shuffle_music(track):
    temp = bytearray()
    temp.extend(track.file_data)
    target = random.randint(0, len(music)-1)
    melee.replace_file_data(track.get_file_name(), music[target].file_data)
    melee.replace_file_data(music[target].get_file_name(), temp)

def random_music(path, file, attempts = 0):
    if not exists(path):
        print("Path not found! " + path)
        return
    songs = listdir(path)
    if len(songs) == 0:
        return
    rng = random.randint(0, len(songs)-1)
    for song in used_songs: # Make songs unique
        if song == songs[rng] and attempts < 10: # Attempts break infinite loop
            random_music(path, file, attempts + 1)
            return
    print(songs[rng])
    melee.replace_file(file, path + "/" + songs[rng])
    used_songs.append(songs[rng])

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
    random_music(CHIPTUNE_PATH, b'inis1_01.hps')
    random_music(CHIPTUNE_PATH, b'inis2_01.hps')
    random_music(CHIPTUNE_PATH, b'inis1_02.hps')
    random_music(CHIPTUNE_PATH, b'inis2_02.hps')
    random_music(CHIPTUNE_PATH, b'mrider.hps')
    random_music(CHIPTUNE_PATH, b'baloon.hps')
    random_music(CHIPTUNE_PATH, b'flatzone.hps')
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
    random_music(METROID_PATH, b'kraid.hps')
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

def start_mod(mode = 0):
    if mode == 0: return
    sort_music()
    for jingle in jingles:
        shuffle_jingle(jingle)
    for track in cutscenes:
        shuffle_cutscene(track)
    for track in music:
        shuffle_music(track)
        
                                     
