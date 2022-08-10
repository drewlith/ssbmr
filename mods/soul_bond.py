# Soul bond mod by drewlith. Makes Nana the exact same as Popo, to make Ice
# Climbers more true to their intended design.

import melee

def start_mod():
    popo = melee.find_fighter("Popo")
    nana = melee.find_fighter("Nana")
    for attack in nana.attacks:
        p_attack = popo.find_attack(attack.attack_name)
        if p_attack != None: 
            i = 0
            for hb in attack.hitboxes:
                hb.set_damage(p_attack.hitboxes[i].get_damage())
                hb.set_angle(p_attack.hitboxes[i].get_angle())
                hb.set_growth(p_attack.hitboxes[i].get_growth())
                hb.set_base(p_attack.hitboxes[i].get_base())
                hb.set_set(p_attack.hitboxes[i].get_set())
                hb.set_element(p_attack.hitboxes[i].get_element())
                hb.set_shield(p_attack.hitboxes[i].get_shield())
                hb.set_sfx(p_attack.hitboxes[i].get_sfx())
                hb.set_size(p_attack.hitboxes[i].get_size())
                i += 1
    for throw in nana.throws:
        p_throw = popo.find_throw(throw.name)
        if p_throw != None:
            throw.set_damage(p_throw.get_damage())
            throw.set_angle(p_throw.get_angle())
            throw.set_growth(p_throw.get_growth())
            throw.set_set(p_throw.get_set())
            throw.set_base(p_throw.get_base())
            throw.set_element(p_throw.get_element())
    nana.set_weight(popo.get_weight())
    nana.set_scale(popo.get_scale())
    nana.set_shield_size(popo.get_shield_size())
    nana.set_air_attributes(popo.get_air_attributes())
    nana.set_jump_attributes(popo.get_jump_attributes())
    nana.set_ground_attributes(popo.get_ground_attributes())
    nana.set_landing_lags(popo.get_landing_lags())
