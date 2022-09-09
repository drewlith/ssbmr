# All Fox mod by drewlith. Makes every fighter have the same properties
# as FOX.

import melee

def start_mod():
    fox = melee.find_fighter("Fox")
    for fighter in melee.fighters:
        if fighter.properties_offset > 0:
            fighter.set_weight(fox.get_weight())
            fighter.set_air_attributes(fox.get_air_attributes())
            fighter.set_jump_attributes(fox.get_jump_attributes())
            fighter.set_ground_attributes(fox.get_ground_attributes())
            fighter.set_landing_lags(fox.get_landing_lags())

    
