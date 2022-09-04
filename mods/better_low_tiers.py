# Better Low Tiers (BLT) mod by drewlith. Gives low tiers some stat boosts.

import melee, random

low_tiers = ["Bowser", "DK", "Game & Watch", "Ganondorf", "Kirby", "Link",
             "Mario", "Mewtwo", "Ness", "Pichu", "Roy", "Young Link", "Zelda"]

def start_mod():
    for fighter in melee.fighters:
        buff = False
        for name in low_tiers:
            if fighter.name == name:
                buff = True
        if buff:
            for attack in fighter.attacks:
                for hb in attack.hitboxes:
                    hb.set_damage(hb.get_damage()+random.randint(0,2))
                    hb.set_growth(hb.get_growth()+random.randint(1,2)*10)
                    hb.set_base(hb.get_base()+random.randint(0,2)*5)
                    hb.set_size(hb.get_size()+random.randint(1,5)*50)
            fighter.set_weight(fighter.get_weight()+random.randint(1,6)*5)
            fighter.set_shield_size(fighter.get_shield_size()+random.randint(2,4))
            air_attributes = fighter.get_air_attributes()
            for attribute in air_attributes:
                attribute = attribute * random.uniform(1.05,1.15)
            fighter.set_air_attributes(air_attributes)
            ground_attributes = fighter.get_ground_attributes()
            ground_attributes[0] = ground_attributes[0] * random.uniform(1.05,1.15)
            ground_attributes[2] = ground_attributes[2] * random.uniform(1.05,1.15)
            ground_attributes[6] = ground_attributes[6] * random.uniform(1.05,1.15)
            ground_attributes[7] = ground_attributes[7] * random.uniform(1.05,1.15)
            ground_attributes[10] = ground_attributes[10] * random.uniform(1.05,1.15)
            fighter.set_ground_attributes(ground_attributes)
            jump_attributes = fighter.get_jump_attributes()
            for attribute in jump_attributes:
                attribute = attribute * random.uniform(1.05,1.15)
            fighter.set_jump_attributes(jump_attributes)
            landing_attributes = fighter.get_landing_lags()
            for i in range(len(landing_attributes)-1):
                if i == 0:
                    landing_attributes[0] = float(2)
                else:
                    landing_attributes[i] = landing_attributes[i] - random.randint(2,6)
                    if landing_attributes[i] < 6:
                        landing_attributes[i] = float(6)
            fighter.set_landing_lags(landing_attributes)
            
            
                    
