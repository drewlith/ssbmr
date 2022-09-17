import melee
elements = ["Normal", "Fire", "Electric", "Slash", "Coin", "Ice", "Sleep", "Sleep",
            "BUGGED REPORT TO DREWLITH", "Grounded", "Cape", "None", "Disable", "Dark", "Screw Attack",
            "Flower", "None"]
throw_elements = ["Normal", "Fire", "Electric", "Ice", "Darkness"]
def start_mod(output_dir, seed, flags, debug = False):
    log = open(output_dir + "\SSBMr-" + seed + "-log.txt", "w")
    log.write("Super Smash Bros. Melee Randomizer | Created by drewlith\n\n")
    log.write("Seed: " + seed)
    log.write("\nFlags: " + flags[:-2])
    log.write("\n\nAny Attacks, Fighters, or Attributes not included in this log were not randomized.")
    log.write("\n\nItem changes will not be listed to avoid clutter.")
    for fighter in melee.fighters:
        log.write("\n\n" + "[" + fighter.name + "]")
        if fighter.properties_offset > 0:
            log.write("\n\nATTRIBUTES")
            weight = str(fighter.get_weight())[0:5]
            log.write("\n -Weight: " + str(fighter.original_stats[0])[0:5] + " > " + weight)
            scale = str(fighter.get_scale())[0:4]
            log.write("\n -Scale: " + str(fighter.original_stats[1])[0:4] + " > " + scale)
            shield_size = str(fighter.get_shield_size())[0:4]
            log.write("\n -Shield Size: " + str(fighter.original_stats[2])[0:4] + " > " + shield_size)
            air_attributes = fighter.get_air_attributes()
            gravity = str(air_attributes[0])[0:4]
            log.write("\n -Gravity: " + str(fighter.original_stats[3][0])[0:4] + " > " + gravity)
            terminal_velocity = str(air_attributes[1])[0:4]
            log.write("\n -Terminal Velocity: " + str(fighter.original_stats[3][1])[0:4] + " > " + terminal_velocity)
            air_mobility_a = str(air_attributes[2])[0:4]
            log.write("\n -Air Mobility A: " + str(fighter.original_stats[3][2])[0:4] + " > " + air_mobility_a)
            air_mobility_b = str(air_attributes[3])[0:4]
            log.write("\n -Air Mobility B: " + str(fighter.original_stats[3][3])[0:4] + " > " + air_mobility_b)
            max_h_velocity = str(air_attributes[4])[0:4]
            log.write("\n -Max Air Horizontal Velocity: " + str(fighter.original_stats[3][4])[0:4] + " > " + max_h_velocity)
            air_friction = str(air_attributes[5])[0:4]
            log.write("\n -Air Friction: " + str(fighter.original_stats[3][5])[0:4] + " > " + air_friction)
            ff_terminal_velocity = str(air_attributes[6])[0:4]
            log.write("\n -Fast Fall Terminal Velocity: " + str(fighter.original_stats[3][6])[0:4] + " > " + ff_terminal_velocity)
            ground_attributes = fighter.get_ground_attributes()
            walk_init_velocity = str(ground_attributes[0])[0:4]
            log.write("\n -Walk Initial Velocity: " + str(fighter.original_stats[4][0])[0:4] + " > " + walk_init_velocity)
            walk_max_velocity = str(ground_attributes[2])[0:4]
            log.write("\n -Walk Max Velocity: " + str(fighter.original_stats[4][2])[0:4] + " > " + walk_max_velocity)
            ground_friction = str(ground_attributes[6])[0:4]
            log.write("\n -Ground Friction: " + str(fighter.original_stats[4][6])[0:4] + " > " + ground_friction)
            dash_velocity = str(ground_attributes[7])[0:4]
            log.write("\n -Dash/Run Initial/Terminal Velocity: " + str(fighter.original_stats[4][7])[0:4] + " > " + dash_velocity)
            jump_attributes = fighter.get_jump_attributes()
            jumpsquat = str(jump_attributes[0])
            log.write("\n -Jumpsquat: " + str(fighter.original_stats[5][0])[0:4] + " > " + jumpsquat)
            initial_v_velocity = str(jump_attributes[2])[0:4]
            log.write("\n -Jump Initial Vertical Velocity: " + str(fighter.original_stats[5][2])[0:4] + " > "  + initial_v_velocity)
            g_to_a_multiplier = str(jump_attributes[3])[0:4]
            log.write("\n -Ground to Air Jump Multiplier: " + str(fighter.original_stats[5][3])[0:4] + " > " + g_to_a_multiplier)
            sh_v_velocity = str(jump_attributes[5])[0:4]
            log.write("\n -Shorthop Vertical Velocity: " + str(fighter.original_stats[5][5])[0:4] + " > " + sh_v_velocity)
            air_jump_multiplier = str(jump_attributes[6])[0:4]
            log.write("\n -Air Jump Multiplier: " + str(fighter.original_stats[5][6])[0:4] + " > " + air_jump_multiplier)
            dj_momentum = str(jump_attributes[7])[0:4]
            log.write("\n -Double Jump Momentum: " + str(fighter.original_stats[5][7])[0:4] + " > " + dj_momentum)
            landing_attributes = fighter.get_landing_lags()
            empty = str(landing_attributes[0])
            log.write("\n -Empty Landing Lag Frames: " + str(fighter.original_stats[6][0]) + " > " + empty)
            nair = str(landing_attributes[1])
            log.write("\n -N-air Lag Frames: " + str(fighter.original_stats[6][1]) + " > " + nair)
            fair = str(landing_attributes[2])
            log.write("\n -F-air Lag Frames: " + str(fighter.original_stats[6][2]) + " > " + fair)
            bair = str(landing_attributes[3])
            log.write("\n -B-air Lag Frames: " + str(fighter.original_stats[6][3]) + " > " + bair)
            uair = str(landing_attributes[4])
            log.write("\n -U-air Lag Frames: " + str(fighter.original_stats[6][4]) + " > " + uair)
            dair = str(landing_attributes[5])
            log.write("\n -D-air Lag Frames: " + str(fighter.original_stats[6][5]) + " > " + dair)
        log.write("\n\nATTACKS")
        for attack in fighter.attacks:
            if "Item" not in attack.type or debug:
                log.write("\n\n[" + fighter.name + " " + attack.attack_name+"]")
                if attack.shuffled:
                    log.write("\nShuffled with " + attack.shuffled_with)
                else:
                    log.write("\nRandomized")
                log.write("\n -Damage: " + attack.original_stats[0] +
                          " > " + str(attack.hitboxes[0].get_damage()))
                log.write("\n -Angle: " + attack.original_stats[1] +
                          " > " + str(attack.hitboxes[0].get_angle()))
                log.write("\n -Knockback Growth: " + attack.original_stats[2] +
                          " > " + str(attack.hitboxes[0].get_growth()))
                log.write("\n -Base Knockback: " + attack.original_stats[3] +
                          " > " + str(attack.hitboxes[0].get_base()))
                log.write("\n -Set Knockback: " + attack.original_stats[4] +
                          " > " + str(attack.hitboxes[0].get_set()))
                log.write("\n -Shield Damage: " + attack.original_stats[5] +
                          " > " + str(attack.hitboxes[0].get_shield()))
                log.write("\n -Size: " + attack.original_stats[6] +
                          " > " + str(attack.hitboxes[0].get_size()))
                log.write("\n -Element: " + elements[attack.original_stats[7]] +
                          " > " + elements[attack.hitboxes[0].get_element()])
                       
        log.write("\n\nTHROWS")
        for throw in fighter.throws:
            log.write("\n\n[" + fighter.name + " " + throw.name + "]")
            if throw.shuffled:
                log.write("\nShuffled with " + throw.shuffled_with)
            else:
                log.write("\nRandomized")
            log.write("\n -Damage: " + throw.original_stats[0] +
                      " > " + str(throw.get_damage()))
            log.write("\n -Angle: " + throw.original_stats[1] +
                      " > " + str(throw.get_angle()))
            log.write("\n -Knockback Growth: " + throw.original_stats[2] +
                      " > " + str(throw.get_growth()))
            log.write("\n -Base Knockback: " + throw.original_stats[3] +
                      " > " + str(throw.get_base()))
            log.write("\n -Set Knockback: " + throw.original_stats[4] +
                       " > " + str(throw.get_set()))
            if throw.get_element() > 4 or throw.original_stats[5] > 4:
                log.write( "\n -Element: ??? > Normal")
            else:
                log.write( "\n -Element: " + throw_elements[throw.original_stats[5]] + " > " + throw_elements[throw.get_element()])
            
        log.write("\n\n")
