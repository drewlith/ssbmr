import melee
from util import percent_chance, get_flag_params
from random import randint as rng
from random import uniform as rng_float
from mods.deviate import deviate_value
def start_mod(flags):
    flag_names = ["bowser", "captain_falcon", "dk", "dr_mario", "falco", "fox",
                  "game_and_watch", "ganondorf", "popo", "nana", "jigglypuff",
                  "kirby", "link", "luigi", "mario", "marth", "mewtwo",
                  "ness", "peach", "pichu", "pikachu", "roy", "samus",
                  "sheik", "yoshi", "young_link", "zelda", "boy", "girl",
                  "giga_koopa", "master_hand", "crazy_hand"]
    fighter_names = ["Bowser", "Captain Falcon", "Donkey Kong", "Dr Mario",
                     "Falco", "Fox", "Mr. Game & Watch", "Ganondorf", "Popo",
                     "Nana", "Jigglypuff", "Kirby", "Link", "Luigi", "Mario",
                     "Marth", "Mewtwo", "Ness", "Peach", "Pichu", "Pikachu",
                     "Roy", "Samus", "Sheik", "Yoshi", "Young Link", "Zelda",
                     "Boy", "Girl", "Giga Koopa", "Master Hand", "Crazy Hand"]
    attribute_flags = ["walk", "dash", "friction", "air", "jump", "gravity", "weight",
                       "scale", "shield_size", "landing_lag"]
    attribute_types = ["Walk", "Dash/Run", "Friction", "Air", "Jump", "Gravity", "Weight",
                       "Scale", "Shield", "Landing Lag"]
    for i, flag in enumerate(flag_names):
        fighter = melee.find_fighter(fighter_names[i])
        for attack in fighter.attacks:
            for hb in attack.hitboxes:
                if "-" + flag + "_hitbox_damage" in flags:
                    mod = get_flag_params(flags, "-" + flag + "_hitbox_damage")[0]
                    hb.set_damage(deviate_value(hb.get_damage(),mod,mod))
                if "-" + flag + "_hitbox_shield_damage" in flags:
                    mod = get_flag_params(flags, "-" + flag + "_hitbox_shield_damage")[0]
                    hb.set_shield(deviate_value(hb.get_shield(),mod,mod))
                if "-" + flag + "_hitbox_base" in flags:
                    mod = get_flag_params(flags, "-" + flag + "_hitbox_base")[0]
                    hb.set_base(deviate_value(hb.get_base(),mod,mod))
                if "-" + flag + "_hitbox_growth" in flags:
                    mod = get_flag_params(flags, "-" + flag + "_hitbox_growth")[0]
                    hb.set_growth(deviate_value(hb.get_growth(),mod,mod))
                if "-" + flag + "_hitbox_wdsk" in flags:
                    mod = get_flag_params(flags, "-" + flag + "_hitbox_wdsk")[0]
                    hb.set_set(deviate_value(hb.get_set(),mod,mod))
                if "-" + flag + "_hitbox_size" in flags:
                    mod = get_flag_params(flags, "-" + flag + "_hitbox_size")[0]
                    hb.set_size(deviate_value(hb.get_size(),mod,mod))
        for throw in fighter.throws:
            if "-" + flag + "_throw_damage" in flags:
                mod = get_flag_params(flags, "-" + flag + "_throw_damage")[0]
                throw.set_damage(deviate_value(throw.get_damage(),mod,mod))
            if "-" + flag + "_throw_base" in flags:
                mod = get_flag_params(flags, "-" + flag + "_throw_base")[0]
                throw.set_base(deviate_value(throw.get_base(),mod,mod))
            if "-" + flag + "_throw_growth" in flags:
                mod = get_flag_params(flags, "-" + flag + "_throw_growth")[0]
                throw.set_growth(deviate_value(throw.get_growth(),mod,mod))
            if "-" + flag + "_throw_wdsk" in flags:
                mod = get_flag_params(flags, "-" + flag + "_throw_wdsk")[0]
                throw.set_set(deviate_value(throw.get_set(),mod,mod))
        for i, attribute in enumerate(attribute_flags):
            if "-" + flag + "_attribute_" + attribute in flags:
                mod = get_flag_params(flags, "-" + flag + "_attribute_" + attribute)[0]
                attributes = fighter.get_attributes_by_group_name(attribute_types[i])
                for a in attributes:
                    a.set_value(deviate_value(a.get_value(),mod,mod))                
