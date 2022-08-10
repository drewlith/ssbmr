# Random/Shuffled Knockback Growth mod by drewlith.
# Shuffle Percent: Amount of attacks to shuffle (as opposed to randomize)
# Balance Percent: Amount of attacks to balance
import melee, random
from util import percent_chance

def shuffle(attack, target):
    for i in range(len(attack.hitboxes)):
        if i > len(target.hitboxes)-1:
            attack.hitboxes[i].set_growth(target.hitboxes[0].get_growth())
        else:
            temp = attack.hitboxes[i].get_growth()
            attack.hitboxes[i].set_growth(target.hitboxes[i].get_growth())
            target.hitboxes[i].set_growth(temp)

def randomize(attack): 
    kbg = random.randint(2,20) * 10
    if percent_chance(2):
        kbg = 0
    for hb in attack.hitboxes:
        hb.set_growth(kbg)

def random_balance(attack):
    kbg = random.randint(attack.strength+3,attack.strength+6) * 10
    if percent_chance(2):
        kbg = 0
    for hb in attack.hitboxes:
        hb.set_growth(kbg)

def start_mod(shuffle_percent, balance_percent):
    for tier in melee.attack_tiers: # Normal Attacks
        for attack in tier:
            if percent_chance(shuffle_percent): # Shuffle
                if percent_chance(balance_percent): # If balance, shuffle within tier
                    shuffle(attack, attack.shuffle_target_balanced)
                    attack.notes.append("Knockback Growth shuffled with " +
                                        attack.shuffle_target_balanced.fighter.name + " " +
                                        attack.shuffle_target_balanced.attack_name +
                                        " to " + str(attack.hitboxes[0].get_growth()) + ". (Balanced)")
                else: # Else shuffle with anything
                    shuffle(attack, attack.shuffle_target_unbalanced)
                    attack.notes.append("Knockback Growth shuffled with " +
                                        attack.shuffle_target_unbalanced.fighter.name + " " +
                                        attack.shuffle_target_unbalanced.attack_name +
                                        " to " + str(attack.hitboxes[0].get_growth()) + ". (Unbalanced)")

            else: # Randomize
                if percent_chance(balance_percent):
                    random_balance(attack)
                    attack.notes.append("Knockback Growth randomized to " +
                                        str(attack.hitboxes[0].get_growth()) + ". (Balanced)")
                else:
                    randomize(attack)
                    attack.notes.append("Knockback Growth randomized to " +
                                        str(attack.hitboxes[0].get_growth()) + ". (Unbalanced)")
                    
    for tier in melee.item_tiers: # Items
        for item in tier:
            if percent_chance(shuffle_percent):
                if percent_chance(balance_percent):
                    shuffle(item, item.shuffle_target_balanced)
                    item.notes.append("Knockback Growth shuffled with " +
                                        item.shuffle_target_balanced.fighter.name + " " +
                                        item.shuffle_target_balanced.attack_name +
                                        " to " + str(item.hitboxes[0].get_growth()) + ". (Balanced)")
                else:
                    shuffle(item, item.shuffle_target_unbalanced)
                    item.notes.append("Knockback Growth shuffled with " +
                                        item.shuffle_target_unbalanced.fighter.name + " " +
                                        item.shuffle_target_unbalanced.attack_name +
                                        " to " + str(item.hitboxes[0].get_growth()) + ". (Unbalanced)")
            else:
                if percent_chance(balance_percent):
                    random_balance(item)
                    item.notes.append("Knockback Growth randomized to " +
                                      str(item.hitboxes[0].get_growth()) + ". (Balanced)")
                else:
                    randomize(item)
                    item.notes.append("Knockback Growth randomized to " +
                                        str(item.hitboxes[0].get_growth()) + ". (Unbalanced)")
