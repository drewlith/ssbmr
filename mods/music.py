import melee, random

jingles = []
cutscenes = []
music = []
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

def start_mod(mode = 0):
    sort_music()
    for jingle in jingles:
        shuffle_jingle(jingle)
    for track in cutscenes:
        shuffle_cutscene(track)
    for track in music:
        shuffle_music(track)
        
                                     
