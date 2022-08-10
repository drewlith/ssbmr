# Harder Bosses mod by drewlith. Makes the bosses and wireframes harder.

import melee, random

bosses = ["Male Wireframe", "Female Wireframe", "Giga Bowser", "Master Hand", "Crazy Hand"]

def start_mod(difficulty):
    if difficulty <= 0: return
    for fighter in melee.fighters:
        make_harder = False
        for name in bosses:
            if fighter.name == name:
                make_harder = True
        if make_harder:
            for attack in fighter.attacks:
                for hb in attack.hitboxes:
                    hb.set_damage(hb.get_damage()+difficulty*3)
                    hb.set_growth(hb.get_growth()+difficulty*20)
                    hb.set_base(hb.get_base()+difficulty*10)
                    hb.set_size(hb.get_size()+difficulty*50)
            

