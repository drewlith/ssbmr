from dol import activate_gecko_code

def start_mod(flags):
    credit_string = "\n\nGecko Codes"
    activate_gecko_code("codes/C-Stick in Single Player - Zauron.txt")
    credit_string += "\nC-Stick in Single Player - Zauron"
    activate_gecko_code("codes/Disable CSS BG Anim - UnclePunch.txt")
    credit_string += "\nDisable CSS BG Anim - UnclePunch"
    activate_gecko_code("codes/Tournament to Debug - Magus, donny2112.txt")
    credit_string += "\nTournament to Debug - Magus, donny2112"
    activate_gecko_code("codes/Unlock All - standardtoaster, Achilles.txt")
    credit_string += "\nUnlock All - standardtoaster, Achilles"
    if "paper_mode" in flags:
        activate_gecko_code("codes/All Characters 2D - DRGN.txt")
        credit_string += "\nAll Characters 2D - DRGN"
    if "all_characters_float" in flags:
        activate_gecko_code("codes/All Characters Float - UnclePunch.txt")
        credit_string += "\nAll Characters Float - UnclePunch"
    if "airdodge_catch" in flags:
        activate_gecko_code("codes/Air Dodge to Grab Items - UnclePunch.txt")
        credit_string += "\nAir Dodge to Grab Items - UnclePunch"
    if "air_grabs" in flags:
        activate_gecko_code("codes/Air Grabs - UnclePunch.txt")
        credit_string += "\nAir Grabs - UnclePunch"
    if "auto_lcancel" in flags:
        activate_gecko_code("codes/Auto L Cancel - Dan Salvato.txt")
        credit_string += "\nAuto L Cancel - Dan Salvato"
    if "b_reverse" in flags:
        activate_gecko_code("codes/B Reverse - UnclePunch.txt")
        credit_string += "\nB Reverse - UnclePunch"
    if "flame_cancel" in flags:
        activate_gecko_code("codes/Bowser Flame Cancel - Achilles.txt")
        credit_string += "\nBowser Flame Cancel - Achilles"
    if "brawl_airdodge" in flags:
        activate_gecko_code("codes/Brawl Airdodge on L - UnclePunch.txt")
        credit_string += "\nBrawl Airdodge on L - UnclePunch"
    if "all_walljump" in flags:
        activate_gecko_code("codes/Every Character can Walljump - Achilles, Geuse.txt")
        credit_string += "\nEvery Character can Walljump - Achilles, Geuse"
    if "fastfall_whenever" in flags:
        activate_gecko_code("codes/Fastfall Whenever - UnclePunch.txt")
        credit_string += "\nFastfall Whenever - UnclePunch"
    if "meteors_spike" in flags:
        activate_gecko_code("codes/No Meteor Cancel - flieskiller.txt")
        credit_string += "\nNo Meteor Cancel - flieskiller"
    if "no_shield" in flags:
        activate_gecko_code("codes/No Shield - Achilles1515.txt")
        credit_string += "\nNo Shield - Achilles1515"
    if "perfect_shield" in flags:
        activate_gecko_code("codes/Perfect Shield - UnclePunch.txt")
        credit_string += "\nPerfect Shield - UnclePunch"
    if "reverse_aerial_rush" in flags:
        activate_gecko_code("codes/Reverse Aerial Rush - MagicScrumpy.txt")
        credit_string += "\nReverse Aerial Rush - MagicScrumpy"
    if "shadow_mode" in flags:
        activate_gecko_code("codes/Shadow Mode.txt")
        credit_string += "\nShadow Mode - ???"
    
    return credit_string
