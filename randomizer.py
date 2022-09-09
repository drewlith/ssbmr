import melee, sys, random, util, string, dol
from mods import (damage, angle, growth, base, wdsk, element, shield_damage, sfx,
                  hitbox_size, throws, weight, scale, shield_size, movement, jump,
                  landing, chaos, music, log, vanilla, no_bosses, better_low_tiers,
                  harder_bosses, soul_bond, turnips, balance, shuffle, all_fox,
                  elemental_mastery, textures)

def start(iso_path = None, output_path = None, flags = ""):
    seed = ""
    
    if iso_path == None: iso_path = sys.argv[1]
    if output_path == None: output_path = sys.argv[2]
    if len(flags) == 0: flags = sys.argv[3]

    flags += " -" # This is just for delimiting.

    if "-seed" in flags:
        seed = util.get_string_between(flags, "-seed ", " -")
    else:
        seed = ''.join(random.choices(string.digits + string.ascii_lowercase, k=8))
        flags = "-seed " + seed + " " + flags

    old_path = output_path
    output_path += "\SSBMr-" + seed + ".iso"

    random.seed(seed)
        
    melee.start(iso_path)

    def get_values_from_string(string, start, end, delimiter):
        value_string = util.get_string_between(string, start, end)
        values = value_string.split(delimiter)
        int_values = []
        for v in values:
            int_values.append(int(v))
        return int_values

    if "-no_bosses" in flags: # "-no_bosses"
        print("Applying no bosses mod...")
        no_bosses.start_mod()

    if "-vanilla" in flags: # "-vanilla %"
        print("Applying vanilla mod...")
        p = get_values_from_string(flags, "-vanilla ", " -", ".") # p stands for Parameters
        vanilla.start_mod(p[0])
        
    melee.sort_attacks()

    # Anything that doesn't exclude data from the randomizer goes below here.
    
    if "-balance" in flags: # "-balance %"
        print("Applying balance mod...")
        balance.start_mod()

    if "-shuffle" in flags: # "-shuffle %"
        print("Applying shuffle mod...")
        p = get_values_from_string(flags, "-shuffle ", " -", ".") 
        shuffle.start_mod(p[0])

    if "-damage" in flags: # "-damage M"
        print("Applying damage mod...")
        p = get_values_from_string(flags, "-damage ", " -", ".")
        damage.start_mod(p[0])

    if "-angle" in flags: # "-angle"
        print("Applying angle mod...")
        if "-angle 0" in flags or "-angle 1" in flags or "-angle 2" in flags:
            p = get_values_from_string(flags, "-angle ", " -", ".")
            angle.start_mod(p[0])
        else:
            angle.start_mod()

    if "-growth" in flags: # "-growth M"
        print("Applying knockback growth mod...")
        p = get_values_from_string(flags, "-growth ", " -", ".")
        growth.start_mod(p[0])

    if "-base_knockback" in flags: # "-base_knockback M"
        print("Applying base knockback mod...")
        p = get_values_from_string(flags, "-base_knockback ", " -", ".")
        base.start_mod(p[0])
        
    if "-wdsk" in flags: # "-wdsk M"
        print("Applying weight-dependent set knockback mod...")
        p = get_values_from_string(flags, "-wdsk ", " -", ".")
        wdsk.start_mod(p[0])
        
    if "-element " in flags: # "-element %"
        print("Applying element mod...")
        p = get_values_from_string(flags, "-element ", " -", ".")
        element.start_mod(p[0])
        
    if "-shield_damage" in flags: # "-shield_damage M"
        print("Applying shield damage mod...")
        p = get_values_from_string(flags, "-shield_damage ", " -", ".")
        shield_damage.start_mod(p[0])
        
    if "-sfx" in flags: # "-sfx"
        print("Applying sound effect mod...")
        sfx.start_mod()
        
    if "-hitbox_size" in flags: # "-hitbox_size S%"
        print("Applying hitbox size mod...")
        p = get_values_from_string(flags, "-hitbox_size ", " -", ".")
        hitbox_size.start_mod(p[0])

    if "-throws" in flags: # "-throws M"
        print("Applying throw mod...")
        p = get_values_from_string(flags, "-throws ", " -", ".")
        throws.start_mod(p[0])

    if "-weight" in flags: # "-weight Mag.Mo"
        print("Applying weight mod...")
        p = get_values_from_string(flags, "-weight ", " -", ".")
        if len(p) < 2:
            weight.start_mod(p[0])
        else:
            weight.start_mod(p[0],p[1])

    if "-scale" in flags: # "-scale Mag.Mo(Optional)" Mode 0 = Bigger/smaller, 1 = Big only, 2 = Small only
        print("Applying scale mod...")
        p = get_values_from_string(flags, "-scale ", " -", ".")
        if len(p) < 2:
            scale.start_mod(p[0])
        else:
            scale.start_mod(p[0],p[1])

    if "-shield_size" in flags: # "-shield_size Mag.Mo(Optional)" Mode 0 = Bigger/smaller, 1 = Big only, 2 = Small only
        print("Applying shield size mod...")
        p = get_values_from_string(flags, "-shield_size ", " -", ".")
        if len(p) < 2:
            shield_size.start_mod(p[0])
        else:
            shield_size.start_mod(p[0],p[1])

    if "-movement" in flags: # "-movement Mag.Mo(Optional)" Mode 0 = Faster/Slower, 1 = Faster only, 2 = Slower only
        print("Applying movement mod...")
        p = get_values_from_string(flags, "-movement ", " -", ".")
        if len(p) < 2:
            movement.start_mod(p[0])
        else:
            movement.start_mod(p[0],p[1])
        
    if "-jump" in flags: # "-jump Mag.Mo(Optional)" Mode 0 = Faster/Slower, 1 = Faster only, 2 = Slower only
        print("Applying jump mod...")
        p = get_values_from_string(flags, "-movement ", " -", ".")
        if len(p) < 2:
            jump.start_mod(p[0])
        else:
            jump.start_mod(p[0],p[1])
        
    if "-landing" in flags: # "-landing Mag.Mo(Optional)" Mode 0 = Faster/Slower, 1 = Faster only, 2 = Slower only
        print("Applying landing mod...")
        p = get_values_from_string(flags, "-landing ", " -", ".")
        if len(p) < 2:
            landing.start_mod(p[0])
        else:
            landing.start_mod(p[0],p[1])

    if "-turnips" in flags: # "-turnips M"
        print("Applying turnips mod...")
        p = get_values_from_string(flags, "-turnips ", " -", ".") # p stands for Parameters
        turnips.start_mod(p[0])

    # Anything that is meant to modify stuff after randomization goes below here

    if "-harder_bosses" in flags: # "-harder_bosses D"
        print("Applying harder bosses mod...")
        p = get_values_from_string(flags, "-harder_bosses ", " -", ".")
        harder_bosses.start_mod(p[0])

    if "-better_low_tiers" in flags: # "-better_low_tiers"
        print("Applying better low tiers mod...")
        better_low_tiers.start_mod()

    if "-chaos" in flags: # "-chaos S"
        print("Applying chaos mod... uh oh...")
        p = get_values_from_string(flags, "-chaos ", " -", ".")
        chaos.start_mod(flags, p[0])

    if "-soul_bond" in flags: # "-soul_bond"
        print("Applying soul bond mod...")
        soul_bond.start_mod()

    if "-all_fox" in flags: # "-all_fox"
        print("Applying Fox Only mod...")
        all_fox.start_mod()

    if "-elemental_mastery" in flags: # "-elemental_mastery"
        print("Applying Elemental Master mod...")
        elemental_mastery.start_mod()

    # Anything that affects only visual/audio elements, or creates external files go below here.

    if "-music" in flags: # "-music M"
        print("Applying music mod...")
        p = get_values_from_string(flags, "-music ", " -", ".")
        music.start_mod(p[0])

    if "-log" in flags: # -log
        print("Writing log")
        log.start_mod(old_path, seed, flags)

    # Music test
    #melee.replace_file(b'menu01.hps', 'test.hps')
    #melee.replace_file(b'menu3.hps', 'test.hps')
    #melee.replace_file(b'MvOpen.mth', 'test.mth')

    dol.start_mod()

    music.custom_music()

    textures.custom_textures(output_path)
        
    melee.end(iso_path, output_path)

    return(flags[:-2])

if __name__ == '__main__':
    start()
