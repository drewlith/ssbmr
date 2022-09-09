# Shuffle mod by drewlith. Run after -balance and -vanilla flag.
# Percent: Percent of moves to shuffle
import melee, copy
from util import percent_chance
from random import randint as rng

bosses = ["Crazy Hand", "Master Hand", "Giga Bowser"]
def shuffle(attack):
    temp = copy.deepcopy(attack)
    boss = False
    if attack.balance:
        if "Item" not in attack.type:
            tier = melee.attack_tiers[attack.strength]
        else:
            tier = melee.item_tiers[attack.strength]
        target = tier[rng(0,len(tier)-1)]
    else:
        if "Item" not in attack.type:
            target = melee.attacks[rng(0,len(melee.attacks)-1)]
        else:
            target = melee.items[rng(0,len(melee.items)-1)]
    for boss in bosses:
        if target.fighter.name == boss:
            boss = True
        if attack.fighter.name == boss:
            boss = True
    if attack.hitboxes[0].get_growth() == 0 and attack.hitboxes[0].get_base == 0: # Fix hitboxes with no knockback
        for hb in attack.hitboxes:
            hb.set_growth(rng(1,10)*10)
            hb.set_base(rng(2,12)*5)
    if target.hitboxes[0].get_growth() == 0 and target.hitboxes[0].get_base == 0:
        for hb in target.hitboxes:
            hb.set_growth(rng(1,10)*10)
            hb.set_base(rng(2,12)*5)
    for i in range(len(attack.hitboxes)):
        if i > len(target.hitboxes)-1:
            hb_id = 0
        else:
            hb_id = i
        attack.hitboxes[i].set_damage(target.hitboxes[hb_id].get_damage())
        attack.hitboxes[i].set_angle(target.hitboxes[hb_id].get_angle())
        attack.hitboxes[i].set_base(target.hitboxes[hb_id].get_base())
        attack.hitboxes[i].set_growth(target.hitboxes[hb_id].get_growth())
        attack.hitboxes[i].set_set(target.hitboxes[hb_id].get_set())
        attack.hitboxes[i].set_element(target.hitboxes[hb_id].get_element())
        attack.hitboxes[i].set_size(target.hitboxes[hb_id].get_size())
        attack.hitboxes[i].set_sfx(target.hitboxes[hb_id].get_sfx())
        attack.hitboxes[i].set_shield(target.hitboxes[hb_id].get_shield())
    for i in range(len(target.hitboxes)):
        if i > len(temp.hitboxes)-1:
            hb_id = 0
        else:
            hb_id = i
        target.hitboxes[i].set_damage(temp.hitboxes[hb_id].get_damage())
        target.hitboxes[i].set_angle(temp.hitboxes[hb_id].get_angle())
        target.hitboxes[i].set_base(temp.hitboxes[hb_id].get_base())
        target.hitboxes[i].set_growth(temp.hitboxes[hb_id].get_growth())
        target.hitboxes[i].set_set(temp.hitboxes[hb_id].get_set())
        target.hitboxes[i].set_element(temp.hitboxes[hb_id].get_element())
        target.hitboxes[i].set_size(temp.hitboxes[hb_id].get_size())
        target.hitboxes[i].set_sfx(temp.hitboxes[hb_id].get_sfx())
        target.hitboxes[i].set_shield(temp.hitboxes[hb_id].get_shield())
    temp = attack.shuffled_with
    attack.shuffled_with = target.shuffled_with
    target.shuffled_with = temp

    if "Multi" in attack.type and not attack.shuffled:
        for hb in attack.hitboxes:
            damage = hb.get_damage() // 3
            if damage < 0:
                damage = 0
            hb.set_damage(damage)

    if "Multi" in target.type and not target.shuffled:
        for hb in target.hitboxes:
            damage = hb.get_damage() // 3
            if damage < 0:
                damage = 0
            hb.set_damage(damage)

    if "Projectile" in attack.type and not attack.shuffled:
        if attack.hitboxes[0].get_damage() > 7:
            for hb in attack.hitboxes:
                damage = hb.get_damage() // 2
                if damage < 0:
                    damage = 0
                hb.set_damage(damage)

    if "Projectile" in target.type and not target.shuffled:
        if target.hitboxes[0].get_damage() > 7:
            for hb in target.hitboxes:
                damage = hb.get_damage() // 2
                if damage < 0:
                    damage = 0
                hb.set_damage(damage)

    if boss:    # Balance bosses gigantic hitboxes
        for hb in attack.hitboxes:
            if hb.get_size() > 2500:
                hb.set_size(2500)

    attack.shuffled = True
    target.shuffled = True

def shuffle_throw(throw):
    temp = copy.deepcopy(throw)
    target = melee.throws[rng(0,len(melee.throws)-1)]
    if target.shuffled:
        return
    throw.set_damage(target.get_damage())
    angle = throw.get_angle()
    if angle != 361:
        angle = rng(angle-15, angle+15)
        if angle < 0:
            angle = 360 + angle
        if angle > 360:
            angle = angle - 360
        throw.set_angle(angle)
    throw.set_base(target.get_base())
    throw.set_growth(target.get_growth())
    throw.set_set(target.get_set())
    throw.set_element(target.get_element())

    target.set_damage(temp.get_damage())
    angle = target.get_angle()
    if angle != 361:
        angle = rng(angle-15, angle+15)
        if angle < 0:
            angle = 360 + angle
        if angle > 360:
            angle = angle - 360
        target.set_angle(angle)
    target.set_base(temp.get_base())
    target.set_growth(temp.get_growth())
    target.set_set(temp.get_set())
    target.set_element(temp.get_element())

    throw.shuffled = True
    target.shuffled = True
    temp = throw.shuffled_with
    throw.shuffled_with = target.shuffled_with
    target.shuffled_with = temp

def start_mod(percent):
    for attack in melee.attacks:
        if percent_chance(percent):
            shuffle(attack)
    for item in melee.items:
        if percent_chance(percent):
            shuffle(item)
    for throw in melee.throws:
        if percent_chance(percent):
            shuffle_throw(throw)
        
