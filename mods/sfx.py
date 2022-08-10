# Random/Shuffled SFX mod by drewlith.
# Shuffle Percent: Amount of attacks to shuffle (as opposed to randomize)
import melee, random
from util import percent_chance

def shuffle(attack, target):
    for i in range(len(attack.hitboxes)):
        if i > len(target.hitboxes)-1:
            attack.hitboxes[i].set_sfx(target.hitboxes[0].get_sfx())
        else:
            temp = attack.hitboxes[i].get_sfx()
            attack.hitboxes[i].set_sfx(target.hitboxes[i].get_sfx())
            target.hitboxes[i].set_sfx(temp)

def randomize(attack): 
    sfx = [65, 70, 66, 34, 67, 35, 72, 40, 5, 33, 69, 1, 2, 38, 39, 37,
           18, 76, 8, 168, 71, 36, 42, 10, 3, 74, 6, 167, 24, 17, 11,
           135, 68, 7, 146, 44, 12]
    # These sfx don't crash on console, there may be more.
    for hb in attack.hitboxes:
        hb.set_sfx(sfx[random.randint(0,len(sfx)-1)])

def start_mod(shuffle_percent):
    for tier in melee.attack_tiers: # Normal Attacks
        for attack in tier:
            if percent_chance(shuffle_percent): # Shuffle
                shuffle(attack, attack.shuffle_target_balanced)
                attack.notes.append("SFX shuffled with " +
                                        attack.shuffle_target_balanced.fighter.name + " " +
                                        attack.shuffle_target_balanced.attack_name +
                                        " to " + str(attack.hitboxes[0].get_sfx()) + ".")
            else: # Randomize
                randomize(attack)
                attack.notes.append("SFX randomized to " +
                                        str(attack.hitboxes[0].get_sfx()) + ".")
                    
    for tier in melee.item_tiers: # Items
        for item in tier:
            if percent_chance(shuffle_percent):
                shuffle(item, item.shuffle_target_unbalanced)
                item.notes.append("SFX shuffled with " +
                                        item.shuffle_target_balanced.fighter.name + " " +
                                        item.shuffle_target_balanced.attack_name +
                                        " to " + str(item.hitboxes[0].get_sfx()) + ".")
            else:
                randomize(item)
                item.notes.append("SFX randomized to " +
                                      str(item.hitboxes[0].get_sfx()) + ".")
