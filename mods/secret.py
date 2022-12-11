import melee
from util import percent_chance, get_flag_params
from random import randint as rng
from random import uniform as rng_float

# These sfx don't crash on console, there may be more.
sfx = [65, 70, 66, 34, 67, 35, 72, 40, 5, 33, 69, 1, 2, 38, 39, 37,
       18, 76, 8, 168, 71, 36, 42, 10, 3, 74, 6, 167, 24, 17, 11,
       135, 68, 7, 146, 44, 12]

def random_sfx(attack):
    sound = rng(0,len(sfx)-1)
    for hb in attack.hitboxes:
        hb.set_sfx(sfx[sound])
        
def start_mod(flags):
    if "-super_punch" in flags:
        dk = melee.find_fighter("Donkey Kong")
        dk.attributes_unique[11].set_value_int(1) # Swings Needed
        dk.attributes_unique[12].set_value_int(15) # Damage per swing
        dk.attributes_unique[13].set_value(4) # H Velocity
    if "-up_launchers" in flags:
        for fighter in melee.fighters:
            for attack in fighter.attacks:
                if "Up Tilt" in attack.name and fighter.name != "Ganondorf":
                    for hb in attack.hitboxes:
                        hb.set_angle(90)
                        hb.set_set(100)
                        hb.set_growth(70)
                        hb.set_base(40)
                if "Up Smash" in attack.name:
                    for hb in attack.hitboxes:
                        hb.set_angle(90)
                        hb.set_set(120)
                        hb.set_growth(70)
                        hb.set_base(60)
    if "-sound" in flags:
        for fighter in melee.fighters:
            for sound in fighter.sounds:
                target = fighter.sounds[rng(0, len(fighter.sounds)-1)]
                temp = sound.data
                sound.data = target.data
                target.data = temp
            for attack in fighter.attacks:
                random_sfx(attack)

