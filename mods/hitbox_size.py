# Random/Shuffled Hitbox Size mod by drewlith.
# Shuffle Percent: Amount of attacks to shuffle (as opposed to randomize)
import melee, random
from util import percent_chance

def shuffle(attack, target):
    for i in range(len(attack.hitboxes)):
        if i > len(target.hitboxes)-1:
            attack.hitboxes[i].set_size(target.hitboxes[0].get_size())
        else:
            temp = attack.hitboxes[i].get_size()
            attack.hitboxes[i].set_size(target.hitboxes[i].get_size())
            target.hitboxes[i].set_size(temp)

def randomize(attack): 
    for hb in attack.hitboxes: # Each hitbox will actually have a unique size
        size = random.randint(3,25)*100
        hb.set_size(size)

def start_mod(shuffle_percent):
    for tier in melee.attack_tiers: # Normal Attacks
        for attack in tier:
            if percent_chance(shuffle_percent): # Shuffle
                shuffle(attack, attack.shuffle_target_unbalanced)
                attack.notes.append("Hitbox Size shuffled with " +
                                        attack.shuffle_target_unbalanced.fighter.name + " " +
                                        attack.shuffle_target_unbalanced.attack_name +
                                        " to " + str(attack.hitboxes[0].get_size()) + ".")
            else: # Randomize
                randomize(attack)
                attack.notes.append("Hitbox Size randomized to " +
                                        str(attack.hitboxes[0].get_size()) + ".")
                    
    for tier in melee.item_tiers: # Items
        for item in tier:
            if percent_chance(shuffle_percent):
                shuffle(item, item.shuffle_target_unbalanced)
                item.notes.append("Hitbox Size shuffled with " +
                                        item.shuffle_target_unbalanced.fighter.name + " " +
                                        item.shuffle_target_unbalanced.attack_name +
                                        " to " + str(item.hitboxes[0].get_size()) + ".")
            else:
                randomize(item)
                item.notes.append("Hitbox Size randomized to " +
                                        str(item.hitboxes[0].get_size()) + ".")
