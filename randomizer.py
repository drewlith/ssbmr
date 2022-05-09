# drewlith 2022 Super Smash Bros. Melee Randomizer v1.0
import random, melee, custom, sys

seed = "default"
chaos = 5
random_percent = 100
balance_percent = 0
inclusion_percent = 100
attributes = True
a_floor = 0.9 # Attribute Multiplier Floor
a_ceiling = 1.1 # Attribute Multiplier Ceiling
customs = True
custom_only = False

elements = ["Normal", "Fire", "Electric", "Slash", "Coin", "Ice", "Sleep", "Sleep", "Grounded", "Grounded", "Cape", "None", "Disable", "Dark", "Screw Attack", "Flower", "None"]
sfx = [65, 70, 66, 34, 67, 35, 72, 40, 5, 33, 69, 1, 2, 38, 39, 37, 18, 76, 8, 168, 71, 36, 42, 10, 3, 74, 6, 167, 24, 17, 11, 135, 68, 7, 146, 44, 12]

def percent_chance(chance): # Util, enter chance in %
    rng = random.randint(0,99)
    if rng < chance:
        return True
    else:
        return False
                
def random_damage(attack, target, balance = False): # Damage
    if attack.random: # Random
        if balance:
            attack.damage = random.randint(attack.strength+1,attack.strength*2+2)
            if attack.strength >= 4:
                attack.damage += attack.strength-3
        else:
            attack.damage = random.randint(1,22)
            if percent_chance(2):
                attack.damage += 10
    else: # Shuffle
        temp = attack.damage
        attack.damage = target.damage
        target.damage = temp

    if percent_chance(chaos):
        attack.damage += random.randint(1, chaos//25+1)
        attack.chaos = True

def random_shield(attack, target, balance = False): # Shield Damage
    if attack.random:
        if percent_chance(10):
            if balance:
                attack.shield = random.randint(attack.strength*2,attack.strength*6)
            else:
                attack.shield = random.randint(1,60)
        else:
            attack.shield = 1
    else: 
        temp = attack.shield
        attack.shield = target.shield
        target.shield = temp

    if percent_chance(chaos//4):
        attack.shield += 10
        attack.chaos = True

def random_angle(attack, target): # Angle
    if attack.random:
        if percent_chance(40): # Sakurai
            angle = 361
        elif percent_chance(40): # Star KO
            angle = random.randint(60,85)
        elif percent_chance(30): # Send out to side
            angle = random.randint(35,60)

        elif percent_chance(4): # Meteor
            angle = random.randint(250,270)
        elif percent_chance(7): # Semi-Spike/Side KO
            angle = random.randint(25,32)
        elif percent_chance(10): # Spike
            angle = random.randint(290,300)
        else:
            angle = random.randint(0,360) # Random
        attack.angle = angle
    else:
        temp = attack.angle
        attack.angle = target.angle
        target.angle = temp

    if percent_chance(chaos):
        attack.angle += 20
        if attack.angle > 361:
            attack.angle = 361
        attack.chaos = True

def random_kb(attack, target, balance = False): # Knockback growth/base
    if attack.random:
        if balance:
            if percent_chance(40):
                attack.growth = random.randint((attack.strength+1)*10+10,attack.strength*16+35)
                attack.base = random.randint(attack.strength*2,attack.strength*6)
            else:
                attack.growth = random.randint(attack.strength*5,attack.strength*12)
                attack.base = random.randint(attack.strength*10,attack.strength*14)
        else:
            attack.growth = random.randint(70,160)
            attack.base = random.randint(10,100)
    else:
        temp = attack.growth
        attack.growth = target.growth
        target.growth = temp

        temp = attack.base
        attack.base = target.base
        target.base = temp

    if percent_chance(chaos//8):
        attack.growth += 20
        attack.base += 10
        
def random_wdsk(attack, target): # Weight dependent set knockback
    if attack.random:
        if percent_chance(20):
            attack.set = random.randint(10,20)
        elif percent_chance(2):
            attack.set = random.randint(30,140)
        else:
            attack.set = 0
    else:
        temp = attack.set
        attack.set = target.set
        target.set = temp

    if percent_chance(chaos//20):
        attack.set += 25
        attack.chaos = True

def random_element(attack, target, throw = False): # Element
    if attack.random:
        if throw:
            if percent_chance(10):
                attack.element = random.randint(0,4)
        else:
            if percent_chance(10):
                element = random.randint(0,15)
                if element == 12 or element == 11: element = 0 # These elements will make the hitbox useless
                attack.element = element
    else:
        temp = attack.element
        attack.element = target.element
        target.element = temp
    if attack.element == 6 or attack.element == 7: attack.element = 12 # Turn sleep into disable, better balanced

def random_sfx(attack, target): # SFX
    if attack.random:
        attack.sfx = sfx[random.randint(0,len(sfx)-1)]
    else:
        temp = attack.sfx
        attack.sfx = target.sfx
        target.sfx= temp

def random_size(attack, target): # Siz
    if attack.random:
        attack.size = random.randint(200,2500)
    else:
        temp = attack.size
        attack.size = target.size
        target.size = temp
        
    if percent_chance(chaos//10):
        attack.size += 500
        attack.chaos = True

def random_weight(_fighter):
    if not attributes: return
    if not percent_chance(inclusion_percent): return
    _fighter.set_weight(float(random.randint(50,120)))
    _fighter.swaps[0] = "Random"
        
    if percent_chance(chaos):
        if percent_chance(50):
            _fighter.set_weight(_fighter.get_weight()+20)
        else:
            _fighter.set_weight(_fighter.get_weight()-20)

def random_scale(_fighter):
    if not attributes: return
    if not percent_chance(inclusion_percent): return
    _fighter.set_scale(random.uniform(_fighter.get_scale() * a_floor, _fighter.get_scale() * a_ceiling))
    _fighter.swaps[1] = "Random"
    if percent_chance(chaos):
        if percent_chance(50):
            _fighter.set_scale(_fighter.get_scale()+0.1)
        else:
            _fighter.set_scale(_fighter.get_scale()-0.1)

def random_shield_size(_fighter):
    if not attributes: return
    if not percent_chance(inclusion_percent): return
    _fighter.set_shield_size(random.uniform(_fighter.shield_min,_fighter.shield_max))
    _fighter.swaps[2] = "Random"
    if percent_chance(chaos):
        if percent_chance(50):
            _fighter.set_shield_size(_fighter.get_shield_size()+3)
        else:
            _fighter.set_shield_size(_fighter.get_shield_size()-3)

def random_air_movement(_fighter):
    if not attributes: return
    if not percent_chance(inclusion_percent): return
    values = _fighter.get_air_attributes()
    values[0] = random.uniform(values[0] * a_floor, values[0] * a_ceiling)  # Gravity
    values[1] = random.uniform(values[1] * a_floor, values[1] * a_ceiling)  # Terminal Velocity
    values[2] = random.uniform(values[2] * a_floor, values[2] * a_ceiling)  # Air Mobility A
    values[3] = random.uniform(values[3] * a_floor, values[3] * a_ceiling)  # Air Mobility B
    values[4] = random.uniform(values[4] * a_floor, values[4] * a_ceiling)  # Max Air H Velocity
    values[5] = random.uniform(values[5] * a_floor, values[5] * a_ceiling)  # Air Friction
    values[6] = random.uniform(values[6] * a_floor, values[6] * a_ceiling)  # Fast Fall Terminal Velocity
    _fighter.set_air_attributes(values)
    _fighter.swaps[3] = "Random"

def random_ground_movement(_fighter):
    if not attributes: return
    if not percent_chance(inclusion_percent): return
    values = _fighter.get_ground_attributes()
    values[0] = random.uniform(values[0] * a_floor, values[0] * a_ceiling)  # Walk Initial Velocity
    values[2] = random.uniform(values[2] * a_floor, values[2] * a_ceiling)  # Walk Max Velocity
    values[6] = random.uniform(values[6] * a_floor, values[6] * a_ceiling)  # Friction
    values[7] = random.uniform(values[7] * a_floor, values[7] * a_ceiling)  # Dash Initial Velocity
    values[10] = values[7]                                                  # Dash/Run Terminal Velocity
    _fighter.set_ground_attributes(values)
    _fighter.swaps[4] = "Random"

def random_jump(_fighter):
    if not attributes: return
    if not percent_chance(inclusion_percent): return
    values = _fighter.get_jump_attributes()
    values[0] = float(random.randint(3,6))                                  # Jumpsquat
    values[1] = 1                                                           # Initial H Velocity
    values[2] = random.uniform(values[2] * a_floor, values[2] * a_ceiling)  # Initial V Velocity
    values[3] = random.uniform(values[3] * a_floor, values[3] * a_ceiling)  # G to A Jump Multiplier
    values[4] = 1                                                           # Max H Velocity
    values[5] = random.uniform(values[5] * a_floor, values[5] * a_ceiling)  # Shorthop V Velocity
    values[6] = random.uniform(values[6] * a_floor, values[6] * a_ceiling)  # Air Jump Multiplier
    values[7] = random.uniform(values[7] * a_floor, values[7] * a_ceiling)  # Double Jump Momentum
    _fighter.set_jump_attributes(values)
    _fighter.swaps[5] = "Random"

def random_landing(_fighter):
    if not attributes: return
    if not percent_chance(inclusion_percent): return
    values = _fighter.get_landing_lags()
    values[0] = float(random.randint(2,5)) # Normal Landing Lag
    for i in range(len(values)):
        if i != 0:
            values[i] = float(random.randint(12,22)) # L-Cancel. Laggy moves will be buffed
    _fighter.set_landing_lags(values)
    _fighter.swaps[6] = "Random"

def randomize_attacks(attacks):
    for a in attacks:
        if percent_chance(balance_percent):
            t = attacks[random.randint(0,len(attacks)-1)]
            a.balance = True
        else:
            t = melee.attacks[random.randint(0,len(melee.attacks)-1)]
            
        if percent_chance(inclusion_percent):
            random_damage(a,t,a.balance)
            random_shield(a,t,a.balance)
            random_angle(a,t)
            random_kb(a,t,a.balance)
            random_wdsk(a,t)
            random_element(a,t)
            random_sfx(a,t)
            #random_size(a,t)

        if not a.random:
            temp = a.shuffled_with
            a.shuffled_with = t.shuffled_with
            t.shuffled_with = temp
        
def randomize():
    tiers = [[],[],[],[],[],[],[],[],[],[],[]]
    item_tiers = [[],[],[],[],[],[],[],[],[],[],[]]
    for attack in melee.attacks:
        attack.get_parameters_from_reference_hitbox()
        if attack.type == 6:
            item_tiers[attack.strength].append(attack)
            if percent_chance(random_percent):
                attack.random = True
        else:
            tiers[attack.strength].append(attack)
            if percent_chance(random_percent):
                attack.random = True
            
    for tier in tiers:
        randomize_attacks(tier)

    for item in item_tiers:
        randomize_attacks(item)

    for throw in melee.throws:
        throw.get_parameters()
        if percent_chance(random_percent):
            throw.random = True

    for throw in melee.throws:
        t = melee.throws[random.randint(0,len(melee.throws)-1)]
        if percent_chance(inclusion_percent):
            random_damage(throw,t, False)
            random_angle(throw,t)
            random_kb(throw,t)
            random_wdsk(throw,t)
            random_element(throw,t, True)
        if not throw.random:
            temp = throw.shuffled_with
            throw.shuffled_with = t.shuffled_with
            t.shuffled_with = temp

            temp = throw.original_owner
            throw.original_owner = t.original_owner
            t.original_owner = temp
            
    for attack in melee.attacks:
        attack.set_parameters()

    for throw in melee.throws:
        throw.set_parameters()
        
    for f in melee.fighters:
        if f.properties_offset > 0: # If not Items
            f.set_thresholds()
            random_weight(f)
            random_shield_size(f)
            random_scale(f)
            random_ground_movement(f)
            random_air_movement(f)
            random_jump(f)
            random_landing(f)
    
    failsafes()

def log_spoilers(log):
    for f in melee.fighters:
        log.write("\n=====" + f.name + "=====\n")
        log.write("\n--Attributes:\n")
        if len(f.swaps[0]) > 0: log.write("\nWeight >>> " + f.swaps[0] + " (" + str(f.get_weight()) + ")" + "\n")
        if len(f.swaps[1]) > 0: log.write("\nScale >>> " + f.swaps[1] + " (" + str(f.get_scale()) + ")"+ "\n")
        if len(f.swaps[2]) > 0: log.write("\nShield Size >>> " + f.swaps[2] + " (" + str(f.get_shield_size()) + ")" + "\n")
        if len(f.swaps[3]) > 0:
            log.write("\nAir Speed >>> " + f.swaps[3] + "\n")
            values = f.get_air_attributes()
            log.write("Gravity: " + str(values[0]) + "\n")
            log.write("Terminal Velocity: " + str(values[1]) + "\n")
            log.write("Mobility A: " + str(values[2]) + "\n")
            log.write("Mobility B: " + str(values[3]) + "\n")
            log.write("Horizontal T. Velocity: " + str(values[4]) + "\n")
            log.write("Air Friction: " + str(values[5]) + "\n")
            log.write("Fast Fall T. Velocity: " + str(values[6]) + "\n")
        if len(f.swaps[4]) > 0:
            log.write("\nGround Speed >>> " + f.swaps[4] + "\n")
            values = f.get_ground_attributes()
            log.write("Walk Initial Velocity: " + str(values[0]) + "\n")
            log.write("Walk Max Velocity: " + str(values[2]) + "\n")
            log.write("Friction: " + str(values[6]) + "\n")
            log.write("Dash Initial Velocity: " + str(values[7]) + "\n")
            log.write("Dash/Run Terminal Velocity: " + str(values[10]) + "\n")
        if len(f.swaps[5]) > 0:
            log.write("\nJump Properties >>> " + f.swaps[5] + "\n")
            values = f.get_jump_attributes()
            log.write("Jumpsquat: " + str(values[0]) + "\n")
            log.write("Initial H Velocity: " + str(values[1]) + "\n")
            log.write("Initial V Velocity: " + str(values[2]) + "\n")
            log.write("Ground to Air Multiplier: " + str(values[3]) + "\n")
            log.write("Max H Velocity: " + str(values[4]) + "\n")
            log.write("Shorthop V Velocity: " + str(values[5]) + "\n")
            log.write("Air Jump Multiplier: " + str(values[6]) + "\n")
            log.write("Double Jump Momentum: " + str(values[7]) + "\n")
        if len(f.swaps[6]) > 0:
            log.write("\nLanding Frames >>> " + f.swaps[6] + "\n")
            values = f.get_landing_lags()
            log.write("Landing Lag: " + str(values[0]) + "\n")
            log.write("N-air Lag: " + str(values[1]) + "\n")
            log.write("F-air Lag: " + str(values[2]) + "\n")
            log.write("B-air Lag: " + str(values[3]) + "\n")
            log.write("U-air Lag: " + str(values[4]) + "\n")
            log.write("D-air Lag: " + str(values[5]) + "\n")

        log.write("\n--Attacks:\n")
        for a in f.attacks:
            log_string = ""
            if a.chaos: log_string += "[Chaos] "
            if a.balance: log_string += "[Balanced] "
            log_string += a.attack_name
            if a.random:
                log_string += " >>> Random \n"
            else:
                log_string += " >>> " + a.shuffled_with + " \n"
            log_string += "DAM: " + str(a.hitboxes[0].get_damage()) + " | "
            log_string += "SHD: " + str(a.hitboxes[0].get_shield()) + " | "
            log_string += "ANG: " + str(a.hitboxes[0].get_angle()) + " | "
            log_string += "KBG: " + str(a.hitboxes[0].get_growth()) + " | "
            log_string += "BKB: " + str(a.hitboxes[0].get_base()) + " | "
            log_string += "SET: " + str(a.hitboxes[0].get_set()) + " | "
            log_string += "SFX: " + str(a.hitboxes[0].get_sfx()) + " | "
            log_string += "STR: " + str(a.strength) + " | "
            log_string += "ELE: " + elements[a.hitboxes[0].get_element()] + " | "
            log_string += "OFF: " + str(a.hitboxes[0].offset)
            log_string += "\n\n"
            log.write(log_string)
        log.write("\n--Throws:\n")
        for t in f.throws:
            log_string = ""
            if t.chaos: log_string += "[Chaos] "
            if t.balance: log_string += "[Balanced] "
            log_string += t.name
            if t.random:
                log_string += " >>> Random \n"
            else:
                log_string += " >>> " + t.original_owner + " " + t.shuffled_with + " \n"
            log_string += "DAM: " + str(t.get_damage()) + " | "
            log_string += "ANG: " + str(t.get_angle()) + " | "
            log_string += "KBG: " + str(t.get_growth()) + " | "
            log_string += "BKB: " + str(t.get_base()) + " | "
            log_string += "SET: " + str(t.get_set()) + " | "
            log_string += "ELE: " + str(t.get_element()) + " | "
            log_string += "OFF: " + str(t.offset)
            log_string += "\n\n"
            log.write(log_string)

def failsafes():
    for f in melee.fighters:
        if f.properties_offset > 0: # If not Items
            if f.get_shield_size() < f.shield_min: f.set_shield_size(f.shield_min)
            if f.get_shield_size() > f.shield_max: f.set_shield_size(f.shield_max)
            jump_values = f.get_jump_attributes()
            if jump_values[6] <= 0.1: jump_values[6] = 1 # Air Jump Multiplier
            if jump_values[7] <= 0.1: jump_values[7] = 1 # Double Jump Momentum
    # Disable Stun on Fox Laser
    melee.fighters[5].attacks[20].hitboxes[0].set_growth(0)
    melee.fighters[5].attacks[20].hitboxes[0].set_base(0)
    melee.fighters[5].attacks[20].hitboxes[0].set_set(0)

    for t in melee.throws:
        if t.get_base() > 50:
            t.set_base(50) # Base Knockback cap for throws so they don't immediately kill.

def main(iso_path = None, output_path = None):
    if iso_path == None: iso_path = sys.argv[0]
    if output_path == None: output_path = sys.argv[1]
    
    spoiler_path = output_path.replace(".iso", "")
    spoiler = open(spoiler_path + " Log.txt", "w")

    random.seed(seed)

    melee.custom_only = custom_only
        
    melee.start(iso_path)

    print(custom_only)
    
    if not custom_only: randomize()
    
    if customs or custom_only:
        custom.random_all(seed, output_path)

    log_spoilers(spoiler)

    melee.end(iso_path, output_path)

    spoiler.close()

    
