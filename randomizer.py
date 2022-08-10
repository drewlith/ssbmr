import melee, sys, random, util, string
from mods import (damage, angle, growth, base, wdsk, element, shield_damage, sfx,
                  hitbox_size, throws, weight, scale, shield_size, movement, jump,
                  landing, chaos, music, log, vanilla, no_bosses, better_low_tiers,
                  harder_bosses, soul_bond, turnips)

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

    # Anything that doesn't exclude data from the randomizer goes below here.
    
    if "-damage" in flags: # "-damage S.B"
        print("Applying damage mod...")
        p = get_values_from_string(flags, "-damage ", " -", ".") # p stands for Parameters
        damage.start_mod(p[0],p[1])

    if "-angle" in flags: # "-angle S.B"
        print("Applying angle mod...")
        p = get_values_from_string(flags, "-angle ", " -", ".")
        angle.start_mod(p[0],p[1])

    if "-kbg" in flags: # "-kbg S.B"
        print("Applying knockback growth mod...")
        p = get_values_from_string(flags, "-kbg ", " -", ".")
        growth.start_mod(p[0],p[1])

    if "-bkb" in flags: # "-bkb S.B"
        print("Applying base knockback mod...")
        p = get_values_from_string(flags, "-bkb ", " -", ".")
        base.start_mod(p[0],p[1])
        
    if "-wdsk" in flags: # "-wdsk %"
        print("Applying weight-dependent set knockback mod...")
        p = get_values_from_string(flags, "-wdsk ", " -", ".")
        wdsk.start_mod(p[0])
        
    if "-element" in flags: # "-element %"
        print("Applying element mod...")
        p = get_values_from_string(flags, "-element ", " -", ".")
        element.start_mod(p[0])
        
    if "-shield_damage" in flags: # "-shield_damage S.B"
        print("Applying shield damage mod...")
        p = get_values_from_string(flags, "-shield_damage ", " -", ".")
        shield_damage.start_mod(p[0],p[1])
        
    if "-sfx" in flags: # "-sfx S"
        print("Applying sound effect mod...")
        p = get_values_from_string(flags, "-sfx ", " -", ".")
        sfx.start_mod(p[0])
        
    if "-hitbox_size" in flags: # "-hitbox_size S"
        print("Applying hitbox size mod...")
        p = get_values_from_string(flags, "-hitbox_size ", " -", ".")
        hitbox_size.start_mod(p[0])

    if "-throws" in flags: # "-throws S"
        print("Applying throw mod...")
        p = get_values_from_string(flags, "-throws ", " -", ".")
        throws.start_mod(p[0])

    if "-weight" in flags: # "-weight S"
        print("Applying weight mod...")
        p = get_values_from_string(flags, "-weight ", " -", ".")
        weight.start_mod(p[0])

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

    if "-blt" in flags: # "-blt"
        print("Applying better low tiers mod...")
        better_low_tiers.start_mod()

    if "-chaos" in flags: # "-chaos S"
        print("Applying chaos mod... uh oh...")
        p = get_values_from_string(flags, "-chaos ", " -", ".")
        chaos.start_mod(flags, p[0])

    if "-soul_bond" in flags: # "-soul_bond"
        print("Applying soul bond mod...")
        soul_bond.start_mod()

    # Anything that affects only visual/audio elements, or creates external files go below here.

    if "-music" in flags: # "-music M"
        print("Applying music mod...")
        p = get_values_from_string(flags, "-music ", " -", ".")
        music.start_mod(p[0])

    if "-log" in flags: # -log
        print("Writing log")
        log.start_mod(old_path, seed, flags)
        
    melee.end(iso_path, output_path)

start()
