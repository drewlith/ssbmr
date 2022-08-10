import melee
elements = ["Normal", "Fire", "Electric", "Slash", "Coin", "Ice", "Sleep", "Sleep",
            "Grounded", "Grounded", "Cape", "None", "Disable", "Dark", "Screw Attack",
            "Flower", "None"]
throw_elements = ["Normal", "Fire", "Electric", "Ice", "Darkness"]
def start_mod(output_dir, seed, flags, debug = False):
    log = open(output_dir + "\SSBMr-" + seed + "-log.txt", "w")
    log.write("Super Smash Bros. Melee Randomizer | Created by drewlith\n\n")
    log.write("Seed: " + seed)
    log.write("\nFlags: " + flags[:-2])
    log.write("\n\nAny Attacks, Fighters, or Attributes not included in this log were not randomized.")
    log.write("\n\nAnything affected by Chaos or 'buff' mods will not have those changes reflected here.")
    log.write("\n\nItem changes will not be listed to avoid clutter.")
    for fighter in melee.fighters:
        log.write("\n\n" + "[" + fighter.name + "]")
        if fighter.properties_offset > 0:
            log.write("\n\nATTRIBUTES")
            weight = str(fighter.get_weight())[0:6]
            log.write("\n -Weight: " + weight)
            scale = str(fighter.get_scale())[0:6]
            log.write("\n -Scale: " + scale)
            shield_size = str(fighter.get_shield_size())[0:6]
            log.write("\n -Shield Size: " + shield_size)
            air_attributes = fighter.get_air_attributes()
            gravity = str(air_attributes[0])[0:6]
            log.write("\n -Gravity: " + gravity)
            terminal_velocity = str(air_attributes[1])[0:6]
            log.write("\n -Terminal Velocity: " + terminal_velocity)
            air_mobility_a = str(air_attributes[2])[0:6]
            log.write("\n -Air Mobility A: " + air_mobility_a)
            air_mobility_b = str(air_attributes[3])[0:6]
            log.write("\n -Air Mobility B: " + air_mobility_b)
            max_h_velocity = str(air_attributes[4])[0:6]
            log.write("\n -Max Air Horizontal Velocity: " + max_h_velocity)
            air_friction = str(air_attributes[5])[0:6]
            log.write("\n -Air Friction: " + air_friction)
            ff_terminal_velocity = str(air_attributes[6])[0:6]
            log.write("\n -Fast Fall Terminal Velocity: " + ff_terminal_velocity)
            ground_attributes = fighter.get_ground_attributes()
            walk_init_velocity = str(ground_attributes[0])[0:6]
            log.write("\n -Walk Initial Velocity: " + walk_init_velocity)
            walk_max_velocity = str(ground_attributes[2])[0:6]
            log.write("\n -Walk Max Velocity: " + walk_max_velocity)
            ground_friction = str(ground_attributes[6])[0:6]
            log.write("\n -Ground Friction: " + ground_friction)
            dash_velocity = str(ground_attributes[7])[0:6]
            log.write("\n -Dash/Run Initial/Terminal Velocity: " + dash_velocity)
            jump_attributes = fighter.get_jump_attributes()
            jumpsquat = str(jump_attributes[0])
            log.write("\n -Jumpsquat: " + jumpsquat)
            initial_v_velocity = str(jump_attributes[2])[0:6]
            log.write("\n -Jump Initial Vertical Velocity: " + initial_v_velocity)
            g_to_a_multiplier = str(jump_attributes[3])[0:6]
            log.write("\n -Ground to Air Jump Multiplier: " + g_to_a_multiplier)
            sh_v_velocity = str(jump_attributes[5])[0:6]
            log.write("\n -Shorthop Vertical Velocity: " + sh_v_velocity)
            air_jump_multiplier = str(jump_attributes[6])[0:6]
            log.write("\n -Air Jump Multiplier: " + air_jump_multiplier)
            dj_momentum = str(jump_attributes[7])[0:6]
            log.write("\n -Double Jump Momentum: " + dj_momentum)
            landing_attributes = fighter.get_landing_lags()
            empty = str(landing_attributes[0])
            log.write("\n -Empty Landing Lag Frames: " + empty)
            nair = str(landing_attributes[1])
            log.write("\n -N-air Lag Frames: " + nair)
            fair = str(landing_attributes[2])
            log.write("\n -F-air Lag Frames: " + fair)
            bair = str(landing_attributes[3])
            log.write("\n -B-air Lag Frames: " + bair)
            uair = str(landing_attributes[4])
            log.write("\n -U-air Lag Frames: " + uair)
            dair = str(landing_attributes[5])
            log.write("\n -D-air Lag Frames: " + dair)
        log.write("\n\nATTACKS")
        for attack in fighter.attacks:
            if attack.type < 6 or debug:
                log.write("\n\n[" + fighter.name + " " + attack.attack_name+"]")
                for note in attack.notes:
                    log.write("\n" + note)
                if debug:
                    for hb in attack.hitboxes:
                        log.write("\n\n {" + hb.name + "}")
                        log.write("\n  -Damage: " + str(hb.get_damage()))
                        log.write("\n  -Angle: " + str(hb.get_angle()))
                        log.write("\n  -Knockback Growth: " + str(hb.get_growth()))
                        log.write("\n  -Base Knockback: " + str(hb.get_base()))
                        log.write("\n  -Weight-Dependent Set Knockback: " + str(hb.get_set()))
                        log.write("\n  -Shield Damage: " + str(hb.get_shield()))
                        log.write("\n  -Element: " + elements[hb.get_element()])
                        log.write("\n  -SFX: " + str(hb.get_sfx()))
                        log.write("\n  -Size: " + str(hb.get_size()))
        log.write("\n\nTHROWS")
        for throw in fighter.throws:
            log.write("\n\n[" + fighter.name + " " + throw.name + "]")
            for note in throw.notes:
                log.write("\n" + note)
            if debug:
                log.write("\n -Damage: " + str(throw.get_damage()))
                log.write("\n -Angle: " + str(throw.get_angle()))
                log.write("\n -Knockback Growth: " + str(throw.get_growth()))
                log.write("\n -Base Knockback: " + str(throw.get_base()))
                log.write("\n -Weight-Dependent Set Knockback: " + str(throw.get_set()))
                if throw.get_element() > 4:
                    log.write( "\n-Element: Normal")
                else:
                    log.write( "\n-Element: " + throw_elements[throw.get_element()])
            
        log.write("\n\n")
