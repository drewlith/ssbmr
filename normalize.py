import fighter

def copy_hitbox_properties(ref, hitbox):
    hitbox.damage = ref.damage
    hitbox.angle = ref.angle
    hitbox.growth = ref.growth
    hitbox.setkb = ref.setkb
    hitbox.base = ref.base
    hitbox.element = ref.element
    hitbox.sfx = ref.sfx
    hitbox.size = ref.size
    hitbox.shielddamage = ref.shielddamage

def decrease_statistics(hitbox):
    if hitbox.damage > 4:
        hitbox.damage -= 1
    if hitbox.growth > 40:
        hitbox.growth -= 5
    if hitbox.setkb > 40:
        hitbox.setkb -= 5
    if hitbox.base > 20:
        hitbox.base -= 10
    if hitbox.shielddamage > 10:
        hitbox.shielddamage -= 3

def increase_statistics(hitbox):
    hitbox.damage += 1
    hitbox.growth += 5
    if hitbox.setkb > 0:
        hitbox.setkb += 5
    hitbox.base += 10
    hitbox.shielddamage += 3

def compare_and_normalize(ref, hitboxes, disjointer=False):
    for _hitbox in hitboxes:
        attack_num = 1
        check_for_new_hits = False
        if "hit1" in ref.tags:
            check_for_new_hits = True
        if _hitbox != ref:
            if check_for_new_hits:
                if "hit" + str(attack_num) not in _hitbox.tags:
                    attack_num += 1
                    ref = _hitbox
            copy_hitbox_properties(ref, _hitbox)
        if "weakhit" in _hitbox.tags:
            decrease_statistics(_hitbox)
        if "stronghit" in _hitbox.tags:
            increase_statistics(_hitbox)
        if "sourspot" in _hitbox.tags:
            if disjointer:
                decrease_statistics(_hitbox)
                decrease_statistics(_hitbox)
            decrease_statistics(_hitbox)
        if "sweetspot" in _hitbox.tags:
            if disjointer:
                increase_statistics(_hitbox)
                increase_statistics(_hitbox)
                _hitbox.angle += 25
            increase_statistics(_hitbox)
            if "spike" in _hitbox.tags:
                _hitbox.angle = 290

def normalize_hitboxes():
    for _fighter in fighter.fighters:
        for subaction in _fighter.subactions:
            if len(subaction.hitboxes) > 0:
                reference = subaction.hitboxes[0]
                disjointer = False
                if _fighter.name == "Marth" or _fighter.name == "Roy" or _fighter.name == "Mewtwo":
                    disjointer = True
                compare_and_normalize(reference, subaction.hitboxes, disjointer)

