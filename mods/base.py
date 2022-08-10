# Random/Shuffled Base Knockback mod by drewlith.
# Shuffle Percent: Amount of attacks to shuffle (as opposed to randomize)
# Balance Percent: Amount of attacks to balance
import melee, random
from util import percent_chance

def shuffle(attack, target):
    for i in range(len(attack.hitboxes)):
        if i > len(target.hitboxes)-1:
            attack.hitboxes[i].set_base(target.hitboxes[0].get_base())
        else:
            temp = attack.hitboxes[i].get_base()
            attack.hitboxes[i].set_base(target.hitboxes[i].get_base())
            target.hitboxes[i].set_base(temp)

def randomize(attack): 
    kb = random.randint(1,15) * 5
    if percent_chance(1):
        kb += 100
    for hb in attack.hitboxes:
        hb.set_base(kb)

def random_balance(attack):
    kb = random.randint(0,attack.strength+3) * 5
    if attack.strength > 5:
        kb += 5
    if attack.strength > 8:
        kb += 30
    for hb in attack.hitboxes:
        hb.set_base(kb)

def start_mod(shuffle_percent, balance_percent):
    for tier in melee.attack_tiers: # Normal Attacks
        for attack in tier:
            if percent_chance(shuffle_percent): # Shuffle
                if percent_chance(balance_percent): # If balance, shuffle within tier
                    shuffle(attack, attack.shuffle_target_balanced)
                    attack.notes.append("Base Knockback shuffled with " +
                                        attack.shuffle_target_balanced.fighter.name + " " +
                                        attack.shuffle_target_balanced.attack_name +
                                        " to " + str(attack.hitboxes[0].get_base()) + ". (Balanced)")

                else: # Else shuffle with anything
                    shuffle(attack, attack.shuffle_target_unbalanced)
                    attack.notes.append("Base Knockback shuffled with " +
                                        attack.shuffle_target_unbalanced.fighter.name + " " +
                                        attack.shuffle_target_unbalanced.attack_name +
                                        " to " + str(attack.hitboxes[0].get_base()) + ". (Unbalanced)")
            else: # Randomize
                if percent_chance(balance_percent):
                    random_balance(attack)
                    attack.notes.append("Base Knockback randomized to " +
                                        str(attack.hitboxes[0].get_base()) + ". (Balanced)")
                else:
                    randomize(attack)
                    attack.notes.append("Base Knockback randomized to " +
                                        str(attack.hitboxes[0].get_base()) + ". (Unbalanced)")
                    
    for tier in melee.item_tiers: # Items
        for item in tier:
            if percent_chance(shuffle_percent):
                if percent_chance(balance_percent):
                    shuffle(item, item.shuffle_target_balanced)
                    item.notes.append("Base Knockback shuffled with " +
                                        item.shuffle_target_balanced.fighter.name + " " +
                                        item.shuffle_target_balanced.attack_name +
                                        " to " + str(item.hitboxes[0].get_base()) + ". (Balanced)")
                else:
                    shuffle(item, item.shuffle_target_unbalanced)
                    item.notes.append("Base Knockback shuffled with " +
                                        item.shuffle_target_unbalanced.fighter.name + " " +
                                        item.shuffle_target_unbalanced.attack_name +
                                        " to " + str(item.hitboxes[0].get_base()) + ". (Unbalanced)")
            else:
                if percent_chance(balance_percent):
                    random_balance(item)
                    item.notes.append("Base Knockback randomized to " +
                                      str(item.hitboxes[0].get_base()) + ". (Balanced)")
                else:
                    randomize(item)
                    item.notes.append("Base Knockback randomized to " +
                                        str(item.hitboxes[0].get_base()) + ". (Unbalanced)")
