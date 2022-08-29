import melee, random
from util import percent_chance

def start_mod(flags, scale):
    if scale > 100: scale = 100
    for attack in melee.attacks:
        if "-damage" in flags:
            for hb in attack.hitboxes:
                damage = hb.get_damage()
                damage = random.randint(damage-(scale//5), damage+(scale//5))
                if damage < 1: damage = 1
                hb.set_damage(damage)
        if "-angle" in flags:
            for hb in attack.hitboxes:
                if percent_chance(scale):
                    hb.set_angle(random.randint(0,361))
        if "-kbg" in flags:
            for hb in attack.hitboxes:
                growth = hb.get_growth()
                growth = random.randint(growth - scale, growth + scale)
                if growth < 10: growth = 10
                hb.set_growth(growth)
        if "-bkb" in flags:
            for hb in attack.hitboxes:
                base = hb.get_base()
                base = random.randint(base - scale, base + scale)
                if base < 1: base = 1
                hb.set_base(base)
        if "-wdsk" in flags:
            for hb in attack.hitboxes:
                if percent_chance(scale):
                    hb.set_set(random.randint(0,scale))
        if "-element" in flags:
            for hb in attack.hitboxes:
                if percent_chance(scale):
                    element = random.randint(0,15)
                    if element == 8 or element == 11: element = 0 # These elements will make the hitbox useless
                    if element == 6 or element == 7: element = 12 # Turn sleep into disable, better balanced
                    if element == 14: element = 0 # No Screw Attack!!!
                    hb.set_element(element)
        if "-shield_damage" in flags:
            for hb in attack.hitboxes:
                if percent_chance(scale):
                    damage = random.randint(0,scale)
                    hb.set_shield(damage)
    if "-throw" in flags:
        for throw in melee.throws:
            damage = throw.get_damage()
            damage = random.randint(damage-(scale//10),damage+(scale//10))
            if damage < 1: damage = 1
            throw.set_damage(damage)
            if percent_chance(scale):
                throw.set_angle(random.randint(0,361))
            growth = throw.get_growth()
            growth = random.randint(growth-scale,growth+scale)
            if growth < 10: growth = 10
            throw.set_growth(growth)
            base = throw.get_base()
            base = random.randint(base-scale,base+scale)
            if base < 1: base = 1
            throw.set_base(base)
            if percent_chance(scale):
                throw.set_element(random.randint(0,4))
            wdsk = throw.get_set()
            wdsk = random.randint(wdsk-scale, wdsk+scale)
            if wdsk < 1: wdsk = 1
            throw.set_set(wdsk)
    
