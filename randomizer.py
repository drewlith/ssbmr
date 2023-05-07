import melee, sys, random, util, string, flag_groups, os.path

from util import percent_chance, get_flag_params

from mods import (chaos, element, log, music, sfx, shuffle, deviate, fighter_adjust,
                  fighter_common, secret, gecko)

def start(params = None, code=""): # Use array of parameters for module usage.
    if len(code) > 0:
        if os.path.exists("seeds/" + code + ".xdelta"):
            print("Seed already has patch.")
            return -1
    seed = ""
    if params == None:
        iso_path = sys.argv[1] # For command line usage.
        output_path = sys.argv[2]
        flags = sys.argv[3]
    else:
        iso_path = params[0]
        output_path = params[1]
        flags = params[2]

    if "-seed" in flags:
        seed = get_flag_params(flags, "-seed", True)
    else:
        seed = ''.join(random.choices(string.digits + string.ascii_lowercase, k=8))
        flags = "-seed " + seed + " " + flags
    pretty_flags = " ".join(flags.split())
    flags = flags.replace(" ", "")
    flags = flag_groups.decode(flags)
    file_name = "SSBMr-" + seed + ".iso"
    random.seed(seed)
    original_path = output_path
    output_path += "/" + file_name
    if len(original_path) < 1:
        output_path = "seeds/" + file_name
    melee.start(iso_path)

    if "-vanilla" in flags:
        percent = get_flag_params(flags, "-vanilla")[0]
        if percent > 95:
            percent = 95
        for fighter in melee.fighters:
            for attack in fighter.attacks:
                if percent_chance(percent):
                    attack.vanilla = True
    if "-balance" in flags:
        for fighter in melee.fighters:
            for attack in fighter.attacks:
                attack.balance = True
    if "-chaos_percent" in flags:
        percent = get_flag_params(flags, "-chaos_percent")[0]
        chaos.start_mod(flags, percent)
    shuffle.start_mod(flags)
    deviate.start_mod(flags)
    fighter_adjust.start_mod(flags)
    element.start_mod(flags)
    secret.start_mod(flags)
    fighter_common.start_mod(flags)
    code_credits = gecko.start_mod(flags)

    txt_log = log.start_mod_old(seed, pretty_flags)
    log.start_mod(pretty_flags, code)
    credit = "SSBM Randomizer created by drewlith."    # Enter seed-specific credits here.
    credit += code_credits
    melee.end(iso_path, output_path, code)

    return (txt_log, credit)

if __name__ == '__main__':
    start()
