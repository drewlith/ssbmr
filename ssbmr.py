import iso, random, sys, log, utility
def generate_seed(_flagset, iso_path, output_path, seed, generate_log=False, code=""):
    utility.set_seed(seed)
    random.seed(seed)
    if len(code) > 0:
        output_path = "output.iso"
    iso.init(iso_path, output_path)
    import flags, fighter, gecko, banner
    from structs import fsm, colors
    flagset = flags.parse_flags(_flagset)
    iso.patch_dol()
    gecko.expand_dol()
    iso.set_game_name(b'Melee Randomizer v1.0 by drewlith')
    banner.set_name(seed)
    iso.replace_file(b'opening.bnr', "Data/opening.bnr")
    iso.replace_file(b'GmTtAll.usd', "Data/GmTtAll-ssbmr.usd") # Add custom title screen
    iso.replace_file(b'MnSlChr.usd', "Data/MnSlChr-rando.usd") # Add custom CSS
    iso.replace_file(b'GrPs.usd', "Data/GrPs-patched.usd") # Better Pokemon Stadium
    colors.color_mod(seed)
    flags.activate_flags(flagset)
    fsm.write_all()
    fighter.write_fighter_data()
    if generate_log:
        log.make_log(output_path, seed)
    f = open("ssbmr_debug.txt", "w")
    f.write(str(len(fighter.fighters)))
    f.close()
    iso.build_iso(code)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        iso_path = sys.argv[1]
        out_path = sys.argv[2]
        seed = sys.argv[3]
        flags = sys.argv[4]
        code = ""
        if len(sys.argv) > 5:
            code = sys.argv[5]
        
        generate_seed(flags, iso_path, out_path, seed, False, code)
