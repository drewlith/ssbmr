import iso, fighter, music, flags, gecko

# iso and fighter scripts initialize when imported, might change cuz seems like bad practice

def generate_seed(_flagset, code=""):
    flagset = flags.parse_flags(_flagset)
    # Aesthetic Mods First
    #music.custom_music()
    # Base Gecko mods (These always activate no matter the flagset)
    gecko.expand_dol()
    gecko.activate_gecko_code("codes/C-Stick in Single Player - Zauron.txt")
    gecko.activate_gecko_code("codes/Disable CSS BG Anim - UnclePunch.txt")
    gecko.activate_gecko_code("codes/Unlock All - standardtoaster, Achilles.txt")
    #gecko.activate_gecko_code("codes/Tournament to Debug - Magus, donny2112.txt")
    gecko.activate_gecko_code("codes/UCF v084 - Altimor, Practical TAS, CarVac, Krohnos.txt")
    # Apply mods from flags
    flags.activate_flags(flagset)
    # Character Specific Data Mods
    # Write Data to new ISO
    #output_debug_log()
    fighter.write_fighter_data()
    iso.build_iso()

def output_debug_log():
    debug = open("debug.txt", "w")
    debug_text = ""
    for _fighter in fighter.fighters:
        for subaction in _fighter.subactions:
            debug_text += subaction.__str__()
            debug_text += "\n\n"
    debug.write(debug_text)
    debug.close()

generate_seed("|hitbox_damage [>20 !25] 18:30| |hitbox_damage [<3 !20 !30 !40] 1:4| |hitbox_angle 75%:150%| /chaos_turnips/")