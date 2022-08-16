# Random/Shuffled Damage mod by drewlith.
# Shuffle Percent: Amount of attacks to shuffle (as opposed to randomize)
import melee, random
from util import percent_chance

def shuffle(attack, target):
    for i in range(len(attack.hitboxes)):
        if i > len(target.hitboxes)-1:
            attack.hitboxes[i].set_damage(target.hitboxes[0].get_damage())
        else:
            temp = attack.hitboxes[i].get_damage()
            attack.hitboxes[i].set_damage(target.hitboxes[i].get_damage())
            target.hitboxes[i].set_damage(temp)

def randomize(attack):
    damage = random.randint(1,20)
    if (percent_chance(2)): # Small chance to make a move much more powerful
        damage += 10
    for hb in attack.hitboxes:
        hb.set_damage(damage)

def random_balance(attack):
    damage = random.randint(attack.strength+1,attack.strength*2+1)
    if attack.strength > 4:
        damage += 4
    if attack.strength > 8:
        damage += 4
    if attack.strength == 10:
        damage += 10
    for hb in attack.hitboxes:
        hb.set_damage(damage)

def start_mod(shuffle_percent):
    for tier in melee.attack_tiers: # Normal Attacks
        for attack in tier:
            if percent_chance(shuffle_percent): # Shuffle
                if attack.balance: # If balance, shuffle within tier
                    shuffle(attack, attack.shuffle_target_balanced)
                    attack.notes.append("Damage shuffled with " +
                                        attack.shuffle_target_balanced.fighter.name + " " +
                                        attack.shuffle_target_balanced.attack_name +
                                        " to " + str(attack.hitboxes[0].get_damage()) + ". (Balanced)")
                else: # Else shuffle with anything
                    shuffle(attack, attack.shuffle_target_unbalanced)
                    attack.notes.append("Damage shuffled with " +
                                        attack.shuffle_target_unbalanced.fighter.name + " " +
                                        attack.shuffle_target_unbalanced.attack_name +
                                        " to " + str(attack.hitboxes[0].get_damage()) + ". (Unbalanced)")
            else: # Randomize
                if attack.balance:
                    random_balance(attack)
                    attack.notes.append("Damage randomized to " +
                                        str(attack.hitboxes[0].get_damage()) + ". (Balanced)")
                else:
                    randomize(attack)
                    attack.notes.append("Damage randomized to " +
                                        str(attack.hitboxes[0].get_damage()) + ". (Unbalanced)")
                    
    for tier in melee.item_tiers: # Items
        for item in tier:
            if percent_chance(shuffle_percent):
                if item.balance:
                    shuffle(item, item.shuffle_target_balanced)
                    item.notes.append("Damage shuffled with " +
                                        item.shuffle_target_balanced.fighter.name + " " +
                                        item.shuffle_target_balanced.attack_name +
                                        " to " + str(item.hitboxes[0].get_damage()) + ". (Balanced)")
                else:
                    shuffle(item, item.shuffle_target_unbalanced)
                    item.notes.append("Damage shuffled with " +
                                        item.shuffle_target_unbalanced.fighter.name + " " +
                                        item.shuffle_target_unbalanced.attack_name +
                                        " to " + str(item.hitboxes[0].get_damage()) + ". (Unbalanced)")
            else:
                if item.balance:
                    random_balance(item)
                    item.notes.append("Damage randomized to " +
                                      str(item.hitboxes[0].get_damage()) + ". (Balanced)")
                else:
                    randomize(item)
                    item.notes.append("Damage randomized to " +
                                        str(item.hitboxes[0].get_damage()) + ". (Unbalanced)")
        

    
