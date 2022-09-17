# Harder Bosses mod by drewlith. Makes the bosses and wireframes harder.

import melee, random

def start_mod(difficulty):
    if difficulty <= 0: return
    for fighter in melee.boss_fighters:
        for attack in fighter.attacks:
            for hb in attack.hitboxes:
                hb.set_damage(hb.get_damage()+difficulty*3)
                hb.set_growth(hb.get_growth()+difficulty*20)
                hb.set_base(hb.get_base()+difficulty*10)
                hb.set_size(hb.get_size()+difficulty*100)
            

