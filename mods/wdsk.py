# Random/Shuffled weight-dependent set knockback Mod by drewlith.
# Percent = Percent of moves to get WDSK. 
import melee, random
from util import percent_chance

def randomize(attack): 
    wdsk = random.randint(20,120)
    for hb in attack.hitboxes:
        hb.set_set(wdsk)

def start_mod(percent):
    for tier in melee.attack_tiers: # Normal Attacks
        for attack in tier:
            if percent_chance(percent):
                randomize(attack)
                attack.notes.append("WDSK randomized to " +
                                        str(attack.hitboxes[0].get_set()) + ".")
                    
    for tier in melee.item_tiers: # Items
        for item in tier:
            if percent_chance(percent):
                randomize(item)
                item.notes.append("WDSK randomized to " +
                                      str(item.hitboxes[0].get_set()) + ".")
