from dol import activate_gecko_code

def start_mod(flags):
    credit_string = "\n\nGecko Codes"
    activate_gecko_code("codes/C-Stick in Single Player - Zauron.txt")
    credit_string += "\nC-Stick in Single Player - Zauron"
    activate_gecko_code("codes/Disable CSS BG Anim - Uncle Punch.txt")
    credit_string += "\nDisable CSS BG Anim - Uncle Punch"
    activate_gecko_code("codes/Tournament to Debug - Magus, donny2112.txt")
    credit_string += "\nTournament to Debug - Magus, donny2112"
    activate_gecko_code("codes/Unlock All - standardtoaster, Achilles.txt")
    credit_string += "\nUnlock All - standardtoaster, Achilles"
    if "all_characters_float" in flags:
        activate_gecko_code("codes/All Characters Float - Uncle Punch.txt")
        credit_string += "\nAll Characters Float - Uncle Punch"
    if "fastfall_whenever" in flags:
        activate_gecko_code("codes/Fastfall Whenever - Uncle Punch.txt")
        credit_string += "\nFastfall Whenever - Uncle Punch"
    if "paper_mode" in flags:
        activate_gecko_code("codes/All Characters 2D - DRGN.txt")
        credit_string += "\nAll Characters 2D - DRGN"
    return credit_string
