# No bosses mod by drewlith. Will exclude bosses from the randomizer.
# Run this before any hitbox mods. Will make "harder bosses" mod pointless.

import melee, random

exclude_list = ["Male Wireframe", "Female Wireframe", "Giga Bowser", "Master Hand", "Crazy Hand"]

def start_mod():
    old_fighters = []
    for fighter in melee.fighters:
        old_fighters.append(fighter)
    melee.fighters.clear()
    for fighter in old_fighters:
        include = True
        for boss in exclude_list:
            if fighter.name == boss:
                include = False
        if include:
            melee.fighters.append(fighter)
    melee.sort_attacks()
    melee.set_shuffle_targets()

