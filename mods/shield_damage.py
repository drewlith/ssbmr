# Random/Shuffled Shield Damage by drewlith.
# Shuffle Percent: Amount of attacks to shuffle (as opposed to randomize)
import melee, random
from util import percent_chance

def shuffle(attack, target):
    for i in range(len(attack.hitboxes)):
        if i > len(target.hitboxes)-1:
            attack.hitboxes[i].set_shield(target.hitboxes[0].get_shield())
        else:
            temp = attack.hitboxes[i].get_shield()
            attack.hitboxes[i].set_shield(target.hitboxes[i].get_shield())
            target.hitboxes[i].set_shield(temp)

def randomize(attack):
    sdmg = random.randint(0,60)
    for hb in attack.hitboxes:
        hb.set_shield(sdmg)

def random_balance(attack):
    sdmg = random.randint(0,attack.strength*6)
    for hb in attack.hitboxes:
        hb.set_shield(sdmg)

def start_mod(shuffle_percent):
    for tier in melee.attack_tiers: # Normal Attacks
        for attack in tier:
            if attack.balance: # Shuffle
                if percent_chance(balance_percent): # If balance, shuffle within tier
                    shuffle(attack, attack.shuffle_target_balanced)
                    attack.notes.append("Shield Damage shuffled with " +
                                        attack.shuffle_target_balanced.fighter.name + " " +
                                        attack.shuffle_target_balanced.attack_name +
                                        " to " + str(attack.hitboxes[0].get_shield()) + ". (Balanced)")
                else: # Else shuffle with anything
                    shuffle(attack, attack.shuffle_target_unbalanced)
                    attack.notes.append("Shield Damage shuffled with " +
                                        attack.shuffle_target_unbalanced.fighter.name + " " +
                                        attack.shuffle_target_unbalanced.attack_name +
                                        " to " + str(attack.hitboxes[0].get_shield()) + ". (Unbalanced)")
            else: # Randomize
                if attack.balance:
                    random_balance(attack)
                    attack.notes.append("Shield Damage randomized to " +
                                        str(attack.hitboxes[0].get_shield()) + ". (Balanced)")
                else:
                    randomize(attack)
                    attack.notes.append("Shield Damage randomized to " +
                                        str(attack.hitboxes[0].get_shield()) + ". (Unbalanced)")
                    
    for tier in melee.item_tiers: # Items
        for item in tier:
            if percent_chance(shuffle_percent):
                if item.balance:
                    shuffle(item, item.shuffle_target_balanced)
                    item.notes.append("Shield Damage shuffled with " +
                                        item.shuffle_target_balanced.fighter.name + " " +
                                        item.shuffle_target_balanced.attack_name +
                                        " to " + str(item.hitboxes[0].get_shield()) + ". (Balanced)")
                else:
                    shuffle(item, item.shuffle_target_unbalanced)
                    item.notes.append("Shield Damage shuffled with " +
                                        item.shuffle_target_unbalanced.fighter.name + " " +
                                        item.shuffle_target_unbalanced.attack_name +
                                        " to " + str(item.hitboxes[0].get_shield()) + ". (Unbalanced)")
            else:
                if item.balance:
                    random_balance(item)
                    item.notes.append("Shield Damage randomized to " +
                                      str(item.hitboxes[0].get_shield()) + ". (Balanced)")
                else:
                    randomize(item)
                    item.notes.append("Shield Damage randomized to " +
                                        str(item.hitboxes[0].get_shield()) + ". (Unbalanced)")
