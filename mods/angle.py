# Random/Shuffled Angle mod by drewlith.
# Shuffle Percent: Amount of attacks to shuffle (as opposed to randomize)
# Balance Percent: Amount of attacks to balance
import melee, random
from util import percent_chance

def shuffle(attack, target):
    for i in range(len(attack.hitboxes)):
        if i > len(target.hitboxes)-1:
            attack.hitboxes[i].set_angle(target.hitboxes[0].get_angle())
        else:
            temp = attack.hitboxes[i].get_angle()
            attack.hitboxes[i].set_angle(target.hitboxes[i].get_angle())
            target.hitboxes[i].set_angle(temp)

def randomize(attack): # heavily favors forward angles
    if percent_chance(5): # Sakurai Angle
        angle = 361
    elif percent_chance(80): # Forwards to above angles
        angle = random.randint(0,90)
    else:
        angle = random.randint(90,360) # Behind angles
        
    for hb in attack.hitboxes:
        hb.set_angle(angle)

def random_balance(attack):
    if percent_chance(15): # Sakurai Angle
        angle = 361
    elif percent_chance(85): # Send Forward
        angle = random.randint(6,14)*5
    elif percent_chance(80): # Send Straight Up
        angle = random.randint(8,9)*10
    elif percent_chance(50): # Meteor
        angle = 270
    elif percent_chance(50): # Spike
        angle = 290
    else:
        angle = random.randint(0,360) # Randomize
    for hb in attack.hitboxes:
        hb.set_angle(angle)

def start_mod(shuffle_percent, balance_percent):
    for tier in melee.attack_tiers: # Normal Attacks
        for attack in tier:
            if percent_chance(shuffle_percent): # Shuffle
                if percent_chance(balance_percent): # If balance, shuffle within tier
                    shuffle(attack, attack.shuffle_target_balanced)
                    attack.notes.append("Angle shuffled with " +
                                        attack.shuffle_target_balanced.fighter.name + " " +
                                        attack.shuffle_target_balanced.attack_name +
                                        " to " + str(attack.hitboxes[0].get_angle()) + ". (Balanced)")
                else: # Else shuffle with anything
                    shuffle(attack, attack.shuffle_target_unbalanced)
                    attack.notes.append("Angle shuffled with " +
                                        attack.shuffle_target_unbalanced.fighter.name + " " +
                                        attack.shuffle_target_unbalanced.attack_name +
                                        " to " + str(attack.hitboxes[0].get_angle()) + ". (Unbalanced)")
            else: # Randomize
                if percent_chance(balance_percent):
                    random_balance(attack)
                    attack.notes.append("Angle randomized to " +
                                        str(attack.hitboxes[0].get_angle()) + ". (Balanced)")
                else:
                    randomize(attack)
                    attack.notes.append("Angle randomized to " +
                                        str(attack.hitboxes[0].get_angle()) + ". (Unbalanced)")
                    
    for tier in melee.item_tiers: # Items
        for item in tier:
            if percent_chance(shuffle_percent):
                if percent_chance(balance_percent):
                    shuffle(item, item.shuffle_target_balanced)
                    item.notes.append("Angle shuffled with " +
                                        item.shuffle_target_balanced.fighter.name + " " +
                                        item.shuffle_target_balanced.attack_name +
                                        " to " + str(item.hitboxes[0].get_angle()) + ". (Balanced)")
                else:
                    shuffle(item, item.shuffle_target_unbalanced)
                    item.notes.append("Angle shuffled with " +
                                        item.shuffle_target_unbalanced.fighter.name + " " +
                                        item.shuffle_target_unbalanced.attack_name +
                                        " to " + str(item.hitboxes[0].get_angle()) + ". (Unbalanced)")
            else:
                if percent_chance(balance_percent):
                    random_balance(item)
                    item.notes.append("Angle randomized to " +
                                      str(item.hitboxes[0].get_angle()) + ". (Balanced)")
                else:
                    randomize(item)
                    item.notes.append("Angle randomized to " +
                                        str(item.hitboxes[0].get_angle()) + ". (Unbalanced)")
