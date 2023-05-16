import characters

# Attack11: Jab
# Attack12: Jab 2
# Attack13: Jab 3
# Attack S3: Forward Tilt
# Attack L3: Down Tilt
# Attack S4: Forward Smash
# Attack Hi4: Up Smash
# Attack Lw4: Down Smash
# AirN: Neutral Air
# AirF: Fair
# AirB: Back Aerial
# AirHi: Up Air
# AirLw: Down Air
# DownAttackU /D: Get Up Attack
# CliffAttackSlow: Ledge Attack Hi%
# CliffAttackQuick: Ledge Attack Low%

def add_attacks():
    bowser = characters.find_fighter("Bowser")
    subactions = bowser.subactions
    
    def create_attack_hitboxes(subaction_id): # Adds all hitboxes from a subaction to an attack
        hitboxes = []
        for hitbox in subactions[subaction_id].hitboxes:
            hitboxes.append(hitbox)
        return hitboxes

    def merge_hitboxes(subaction_ids):
        hitboxes = []
        for i in range(len(subaction_ids)):
            for hitbox in create_attack_hitboxes(subaction_ids[i]):
                hitboxes.append(hitbox)
        return hitboxes

    def split_hitboxes(subaction_id, index_to_split_at):
        hitboxes = create_attack_hitboxes(subaction_id)
        a = []
        b = []
        for i in range(len(hitboxes)):
            if i < index_to_split_at:
                a.append(hitboxes[i])
            else:
                b.append(hitboxes[i])
        return (a,b)
    
    bowser.add_attack(create_attack_hitboxes(46), "Jab 1", 3, ["Jab"])
    bowser.add_attack(create_attack_hitboxes(47), "Jab 2", 3, ["Jab"])
    bowser.add_attack(create_attack_hitboxes(52), "Dash Attack", 6, ["Dash Attack"])
    bowser.add_attack(merge_hitboxes([53, 55, 57]), "F Tilt", 6, ["F Tilt"])
    bowser.add_attack(create_attack_hitboxes(58), "Up Tilt", 6, ["Up Tilt"])
    dtilt_split = split_hitboxes(59, 2)
    bowser.add_attack(dtilt_split[0], "Down Tilt 1", 6, ["Down Tilt"])
    bowser.add_attack(dtilt_split[1], "Down Tilt 2", 5, ["Down Tilt"])
    bowser.add_attack(create_attack_hitboxes(62), "F Smash", 9, ["F Smash", "KO"])
    upsmash_split = split_hitboxes(66, 2)
    bowser.add_attack(upsmash_split[0], "Up Smash 1", 8, ["Up Smash"], "KO")
    bowser.add_attack(upsmash_split[1], "Up Smash 2", 7, ["Up Smash"])
    downsmash_split = split_hitboxes(67, 4)
    bowser.add_attack(downsmash_split[0], "Down Smash 1", 1, ["Down Smash"], "Weak")
    bowser.add_attack(downsmash_split[1], "Down Smash 2", 8, ["Down Smash"])
    bowser.add_attack(create_attack_hitboxes(68), "N Air", 6, ["N Air", "Aerial"])
    bowser.add_attack(create_attack_hitboxes(69), "F Air", 7, ["F Air", "Aerial"])
    bowser.add_attack(create_attack_hitboxes(70), "B Air", 7, ["B Air", "Aerial"])
    bowser.add_attack(create_attack_hitboxes(71), "Up Air", 8, ["Up Air", "Aerial"])
    bowser.add_attack(create_attack_hitboxes(72), "Down Air", 2, ["Down Air", "Aerial"])
    bowser.add_attack(create_attack_hitboxes(77), "Down Air Landing", 2, ["Landing"])
    for i in range(len(bowser.subactions)):
        bowser.show_subaction_hitboxes(i)
