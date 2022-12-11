import json, sys, util, struct
from scipy.spatial import distance

from util import *

class Fighter():
    def __init__(self, name, dat):
        self.name = name
        self.dat = dat
        self.attributes = []
        self.attributes_unique = []
        self.attacks = []
        self.grabs = []
        self.item_attacks = []
        self.sounds = []
        self.throws = []
        self.original_stats = []
        self.get_attack_data()
        self.get_throw_data()
        self.attribute_offset = self.dat.fighter_data.attributes_offset
        self.attribute_end = self.dat.fighter_data.attributes_end
        self.attribute_size = self.attribute_end - self.attribute_offset
        self.attribute_data = read_data(self.dat.data_block, self.attribute_offset, self.attribute_size)
        self.fighter_specific_attr_data = read_data(self.dat.data_block, self.attribute_end, self.get_fighter_specific_data_size())
        self.get_fighter_specific_attributes()
        self.get_attribute_data()
        self.set_attributes()
        self.shuffle_target = self
        self.get_sound_data()
        self.shuffled = False
        
    def get_attribute_data(self):
        i = 0
        while i < len(self.attribute_data):
            self.attributes.append(Attribute("???", self.attribute_data[i:i+4], i))
            i += 4

    def get_fighter_specific_attributes(self):
        i = 0
        while i < len(self.fighter_specific_attr_data):
            self.attributes_unique.append(Attribute("???", self.fighter_specific_attr_data[i:i+4], i))
            i += 4

    def get_attributes_by_group_name(self, group, uniques=False):
        attributes = []
        if uniques:
            for attribute in self.attributes_unique:
                if attribute.group == group:
                    attributes.append(attribute)
        else:
            for attribute in self.attributes:
                if attribute.group == group:
                    attributes.append(attribute)
        return attributes

    def get_attribute_by_name(self, name):
        for attribute in self.attributes:
            if name in attribute.name:
                return attribute
        print("No attribute found with name: ", name)

    def write_attribute_data(self):
        for attribute in self.attributes:
            write_data(self.attribute_data, attribute.offset, attribute.data)
        for attribute in self.attributes_unique:
            write_data(self.fighter_specific_attr_data, attribute.offset, attribute.data)
            
    def get_attack_data(self):
        for subaction in self.dat.fighter_data.subactions:
            if len(subaction.hitboxes) > 0:
                name = subaction.name
                name = name.decode("utf-8")
                name = process_name(name)
                attack_exists_already = self.find_attack(name)
                if attack_exists_already != False:
                    attack = attack_exists_already
                    for hb in subaction.hitboxes:
                        attack.hitboxes.append(hb)
                else:
                    attack = Attack(self, name)
                    for hb in subaction.hitboxes:
                        attack.hitboxes.append(hb)  
                    if "Swing" in attack.name or "Item" in attack.name:
                        self.item_attacks.append(attack)
                    elif attack.hitboxes[0].get_element() == 8: # Grabs use this element
                        self.grabs.append(attack)
                    else:
                        if attack.hitboxes[0].get_element() != 11: # Specials use this element
                            self.attacks.append(attack)
                            #self.split_attack(attack)
        attacks = []
        for a in self.attacks:
            new_attacks = self.split_attack(a)
            for attack in new_attacks:
                attacks.append(attack)
        self.attacks = attacks
       
    def get_throw_data(self):
        for subaction in self.dat.fighter_data.subactions:
            for throw in subaction.throws:
                throw.name = process_name(throw.name)
                number_with_name = 1
                original_name = throw.name
                while self.find_throw(throw.name) != False:
                    throw.name = original_name + " " + str(number_with_name + 1)
                    number_with_name += 1
                throw.fighter = self
                if throw.get_type() == 0:
                    self.throws.append(throw)
                    throw.record_original_stats()

    def get_sound_data(self):
        for subaction in self.dat.fighter_data.subactions:
            for sound in subaction.sfx:
                if sound.get() > 0xFFF:
                    self.sounds.append(sound)

    def find_attack(self, name):
        for attack in self.attacks:
            if attack.name == name:
                return attack
        return False

    def find_throw(self, name):
        for throw in self.throws:
            if throw.name == name:
                return throw
        return False

    def split_attack(self, attack): # Splits attacks into parts based on strength
        attacks = []
        def create_new_attack(attack, attacks, name):
            new_attack = Attack(attack.fighter, name)
            new_attack.hitboxes.append(attack.hitboxes[i])
            if new_attack.hitboxes[0].get_element() != 8 and new_attack.hitboxes[0].get_element() != 11:
                attacks.append(new_attack)

        def compare_to_reference(ref, hb):
            if abs(ref.get_base() - hb.get_base()) < 25: # Check for differences in stats
                if abs(ref.get_growth() - hb.get_growth()) < 40:
                    if abs(ref.get_damage() - hb.get_damage()) < 4:
                        if ref.get_element() == hb.get_element():
                            if abs(ref.get_angle() - hb.get_angle()) < 35:
                                return True
            return False

        for i in range(len(attack.hitboxes)):
            proceed = True
            if i == 0:
                create_new_attack(attack, attacks, attack.name)
                proceed = False
            if proceed == True:
                hb = attack.hitboxes[i]
                merged_hitbox = False
                for a in attacks:
                    if merged_hitbox == False:
                        merged_hitbox = compare_to_reference(a.hitboxes[0], hb)
                        if merged_hitbox == True:
                            a.hitboxes.append(hb)
                if merged_hitbox == False:
                    if hb.get_angle() == 290: # Check for Spike
                        create_new_attack(attack, attacks, attack.name + " Spike")
                    else:
                        create_new_attack(attack, attacks, attack.name + " " + str(len(attacks)+1))
        for a in attacks:
            a.determine_balance()
            a.record_original_stats()
        return attacks

    def get_fighter_specific_data_size(self): # Resource: https://drive.google.com/drive/folders/1iNdlRJe8hHq4Ew1IPOf9Ad0E4_MTrGwr
        offsets_dict = {
            "Bowser":0xA0, "Captain Falcon":0x8C,  "Donkey Kong":0x74, "Dr Mario":0x84, "Falco":0xD4, "Fox":0xD4,
            "Mr. Game & Watch":0x94, "Ganondorf":0x8C, "Popo":0x15C, "Nana":0x15C, "Jigglypuff":0x100, "Kirby":0x424,
            "Link":0xDC, "Luigi":0x98, "Mario":0x84, "Marth":0x98, "Mewtwo":0x88, "Ness":0xDC, "Peach":0xC0, "Pichu":0xF8,
            "Pikachu":0xF8, "Roy":0x98, "Samus":0xD3, "Sheik":0x74, "Yoshi":0x138, "Young Link":0xDC, "Zelda":0xA8, "Boy":4, "Girl":4,
            "Giga Koopa":4, "Master Hand":4, "Crazy Hand":4
            }
        return offsets_dict[self.name]

    def set_attribute_properties(self, attribute, name, group, whole=False):
        attribute.name = name
        attribute.group = group
        attribute.whole_number = whole

    def set_attributes(self):
        set_attribute_properties = self.set_attribute_properties
        set_attribute_properties(self.attributes[0], "Initial Walk Velocity", "Walk")
        set_attribute_properties(self.attributes[1], "Walk Acceleration", "Walk")
        set_attribute_properties(self.attributes[2], "Walk Maximum Velocity", "Walk")
        set_attribute_properties(self.attributes[3], "Slow Walk Max Velocity", "Walk")
        set_attribute_properties(self.attributes[4], "Mid Walk Point", "Walk")
        set_attribute_properties(self.attributes[5], "Fast Walk Min.", "Walk")
        set_attribute_properties(self.attributes[6], "Ground Friction", "Friction")
        set_attribute_properties(self.attributes[7], "Dash Initial Velocity", "Dash/Run")
        set_attribute_properties(self.attributes[8], "Dash & Run Acceleration A", "Dash/Run")
        set_attribute_properties(self.attributes[9], "Dash & Run Acceleration B", "Dash/Run")
        set_attribute_properties(self.attributes[10], "Dash & Run Terminal Velocity", "Dash/Run")
        set_attribute_properties(self.attributes[11], "Run Animation Scaling", "Dash/Run")
        set_attribute_properties(self.attributes[12], "Run Acceleration", "Dash/Run")
        # ???
        set_attribute_properties(self.attributes[14], "Jumpsquat", "Jumpsquat", True)
        set_attribute_properties(self.attributes[15], "Jump Horizontal Velocity", "Jump")
        set_attribute_properties(self.attributes[16], "Jump Vertical Velocity", "Jump")
        set_attribute_properties(self.attributes[17], "Jump Momentum Multiplier", "Jump")
        set_attribute_properties(self.attributes[18], "Jump Horizontal Max Velocity", "Jump")
        set_attribute_properties(self.attributes[19], "Shorthop Vertical Velocity", "Jump")
        set_attribute_properties(self.attributes[20], "Air Jump Multiplier", "None")
        set_attribute_properties(self.attributes[21], "Double Jump Momentum", "Jump")
        set_attribute_properties(self.attributes[22], "Number of Jumps", "None")
        set_attribute_properties(self.attributes[23], "Gravity", "Gravity")
        set_attribute_properties(self.attributes[24], "Terminal Velocity", "Gravity")
        set_attribute_properties(self.attributes[25], "Air Mobility A", "Air")
        set_attribute_properties(self.attributes[26], "Air Mobility B", "Air")
        set_attribute_properties(self.attributes[27], "Aerial Horizontal Max Velocity", "Air")
        set_attribute_properties(self.attributes[28], "Air Friction", "Friction")
        set_attribute_properties(self.attributes[29], "Fast Fall Terminal Velocity", "Gravity")
        # ???
        set_attribute_properties(self.attributes[31], "Jab 2 Window", "Jab", True)
        set_attribute_properties(self.attributes[32], "Jab 3 Window", "Jab", True)
        set_attribute_properties(self.attributes[33], "Turnaround Frames", "Turnaround", True)
        set_attribute_properties(self.attributes[34], "Weight", "Weight", True)
        set_attribute_properties(self.attributes[35], "Scale", "Scale")
        set_attribute_properties(self.attributes[36], "Shield Size", "Shield")
        set_attribute_properties(self.attributes[37], "Shield Break Velocity", "Shield")
        set_attribute_properties(self.attributes[38], "Rapid Jab Window", "Jab", True)
        # ??? x 3
        set_attribute_properties(self.attributes[42], "Ledgejump Horizontal Velocity", "Jump")
        set_attribute_properties(self.attributes[43], "Ledgejump Vertical Velocity", "Jump")
        set_attribute_properties(self.attributes[44], "Item Throw Velocity", "Item")
        # ??? x 12
        set_attribute_properties(self.attributes[56], "Kirby Star Damage", "Kirby", True)
        set_attribute_properties(self.attributes[57], "Landing Lag", "Landing Lag", True)
        set_attribute_properties(self.attributes[58], "N-air Landing Lag", "Landing Lag", True)
        set_attribute_properties(self.attributes[59], "F-air Landing Lag", "Landing Lag", True)
        set_attribute_properties(self.attributes[60], "B-air Landing Lag", "Landing Lag", True)
        set_attribute_properties(self.attributes[61], "U-air Landing Lag", "Landing Lag", True)
        set_attribute_properties(self.attributes[62], "D-air Landing Lag", "Landing Lag", True)
        set_attribute_properties(self.attributes[63], "Victory Screen Window Scale", "Scale")
        # ???
        set_attribute_properties(self.attributes[65], "Wall Jump Horizontal Velocity", "Jump")
        set_attribute_properties(self.attributes[66], "Wall Jump Vertical Velocity", "Jump")

        # Fighter Specific
        if self.name == "Bowser":
            set_attribute_properties(self.attributes_unique[0], "Super Armor", "Passive")
            set_attribute_properties(self.attributes_unique[1], "Flame B Button Check Frequency", "Neutral B", True)
            set_attribute_properties(self.attributes_unique[2], "Flame Recharge Rate Fuel", "Neutral B")
            set_attribute_properties(self.attributes_unique[3], "Flame Recharge Rate Flame Size", "Neutral B")
            set_attribute_properties(self.attributes_unique[4], "Flame Max Fuel", "Neutral B")
            set_attribute_properties(self.attributes_unique[5], "Flame Spew Velocity", "Neutral B")
            set_attribute_properties(self.attributes_unique[6], "Flame Scale", "Neutral B")
            # ??? x 2
            set_attribute_properties(self.attributes_unique[9], "Flame X Offset", "Neutral B")
            set_attribute_properties(self.attributes_unique[10], "Flame Y Offset", "Neutral B")
            set_attribute_properties(self.attributes_unique[11], "Koopa Klaw Bite Damage", "Side B", True)
            # ??? x 7
            set_attribute_properties(self.attributes_unique[19], "Koopa Klaw Grab Duration", "Side B")
            # ???
            set_attribute_properties(self.attributes_unique[21], "Whirling Fortress Vertical Momentum", "Up B")
            set_attribute_properties(self.attributes_unique[22], "Whirling Fortress Gravity", "Up B")
            set_attribute_properties(self.attributes_unique[23], "Whirling Fortress 2nd Half Vertical Momentum", "Up B")
            set_attribute_properties(self.attributes_unique[24], "Whirling Fortress Ground Speed", "Up B")
            set_attribute_properties(self.attributes_unique[25], "Whirling Fortress Momentum Preservation", "Up B")
            set_attribute_properties(self.attributes_unique[26], "Whirling Fortress Ground Turn Speed", "Up B")
            set_attribute_properties(self.attributes_unique[27], "Whirling Fortress Aerial Mobility", "Up B")
            # ??? x 4
            set_attribute_properties(self.attributes_unique[32], "Bowser Bomb Horizontal Momentum", "Down B")
            set_attribute_properties(self.attributes_unique[33], "Bowser Bomb Initial Velocity", "Down B")
            set_attribute_properties(self.attributes_unique[34], "Bowser Bomb Horizontal Momentum Preservation", "Down B")
            # ???
            set_attribute_properties(self.attributes_unique[36], "Bowser Bomb Gravity", "Down B")
            set_attribute_properties(self.attributes_unique[37], "Bowser Bomb Descent Speed", "Down B")
        if self.name == "Captain Falcon":
            set_attribute_properties(self.attributes_unique[3], "Falcon Punch Horizontal Momentum", "Neutral B")
            set_attribute_properties(self.attributes_unique[4], "Falcon Punch Angled Vertical Bonus Momentum", "Neutral B")
            set_attribute_properties(self.attributes_unique[5], "Raptor Boost Gravity On-Hit", "Side B")
            set_attribute_properties(self.attributes_unique[6], "Raptor Boost Gravity On-Whiff", "Side B")
            set_attribute_properties(self.attributes_unique[7], "Raptor Boost Gravity On-whiff 2", "Side B")
            # ??? x 8
            set_attribute_properties(self.attributes_unique[16], "Falcon Dive Air Friction Multiplier", "Up B")
            set_attribute_properties(self.attributes_unique[17], "Falcon Dive Horizontal Momentum", "Up B")
            set_attribute_properties(self.attributes_unique[18], "Falcon Dive Free Fall Multiplier", "Up B")
            set_attribute_properties(self.attributes_unique[19], "Falcon Dive Landing Lag", "Up B")
            # ??? x 4
            set_attribute_properties(self.attributes_unique[24], "Falcon Dive On-Catch Gravity", "Up B")
            # ??? x 2
            set_attribute_properties(self.attributes_unique[27], "Falcon Kick Flame Particles Angle", "Down B")
            set_attribute_properties(self.attributes_unique[28], "Falcon Kick Speed Modifier On-Hit", "Down B")
            # ???
            set_attribute_properties(self.attributes_unique[30], "Falcon Kick Ground Lag Multiplier", "Down B")
            set_attribute_properties(self.attributes_unique[31], "Falcon Kick Landing Lag Multiplier", "Down B")
            set_attribute_properties(self.attributes_unique[32], "Falcon Kick Ground Traction", "Down B")
            set_attribute_properties(self.attributes_unique[33], "Falcon Kick Landing Traction", "Down B")
        if self.name == "Donkey Kong":
            # ??? x 7
            set_attribute_properties(self.attributes_unique[8], "Cargo Turn Speed", "Passive")
            set_attribute_properties(self.attributes_unique[9], "Cargo Jump Startup", "Passive")
            set_attribute_properties(self.attributes_unique[10], "Cargo Landing Lag", "Passive")
            set_attribute_properties(self.attributes_unique[11], "Giant Punch Arm Swings For Charge", "Neutral B", True)
            set_attribute_properties(self.attributes_unique[12], "Giant Punch Damage per Arm Swing", "Neutral B", True)
            set_attribute_properties(self.attributes_unique[13], "Giant Punch Ground Horizontal Velocity", "Neutral B")
            set_attribute_properties(self.attributes_unique[14], "Headbutt X-Axis Value Needed For Momentum", "Side B")
            set_attribute_properties(self.attributes_unique[15], "Headbutt Momentum", "Side B")
            set_attribute_properties(self.attributes_unique[16], "Headbutt Gravity", "Side B")
            # ???
            set_attribute_properties(self.attributes_unique[18], "Spinning Kong Vertical Velocity", "Up B")
            set_attribute_properties(self.attributes_unique[19], "Spinning Kong Gravity", "Up B")
            set_attribute_properties(self.attributes_unique[20], "Spinning Kong Ground Velocity", "Up B")
            set_attribute_properties(self.attributes_unique[21], "Spinning Kong Horizontal Aerial Velocity", "Up B")
            set_attribute_properties(self.attributes_unique[22], "Spinning Kong Ground Mobility", "Up B")
            set_attribute_properties(self.attributes_unique[23], "Spinning Kong Air Mobility", "Up B")
        if self.name == "Dr Mario":
            set_attribute_properties(self.attributes_unique[0], "Super Sheet Horizontal Momentum", "Side B")
            set_attribute_properties(self.attributes_unique[1], "Super Sheet Horizontal Velocity", "Side B")
            set_attribute_properties(self.attributes_unique[2], "Super Sheet Vertical Momentum", "Side B")
            set_attribute_properties(self.attributes_unique[3], "Super Sheet Gravity", "Side B")
            set_attribute_properties(self.attributes_unique[4], "Super Sheet Fall Speed", "Side B")
            # ??? Item ID of Cape
            set_attribute_properties(self.attributes_unique[6], "Super Jump Punch Freefall Mobility", "Up B")
            set_attribute_properties(self.attributes_unique[7], "Super Jump Punch Landing Lag", "Up B")
            # ??? x 2
            set_attribute_properties(self.attributes_unique[10], "Super Jump Punch Max Angle Change", "Up B")
            set_attribute_properties(self.attributes_unique[11], "Super Jump Punch Initial Horizontal Velocity", "Up B")
            set_attribute_properties(self.attributes_unique[12], "Super Jump Punch Initial Gravity", "Up B")
            set_attribute_properties(self.attributes_unique[13], "Super Jump Punch Initial Vertical Momentum", "Up B")
            set_attribute_properties(self.attributes_unique[14], "Dr Tornado Ground Rise Resistance", "Down B")
            set_attribute_properties(self.attributes_unique[15], "Dr Tornado Base Air Speed", "Down B")
            set_attribute_properties(self.attributes_unique[16], "Dr Tornado Horizontal Velocity Limit", "Down B")
            set_attribute_properties(self.attributes_unique[17], "Dr Tornado Horizontal Acceleration", "Down B")
            set_attribute_properties(self.attributes_unique[18], "Dr Tornado Horizontal Drift", "Down B")
            set_attribute_properties(self.attributes_unique[19], "Dr Tornado Deceleration Rate", "Down B")
            # ???
            set_attribute_properties(self.attributes_unique[21], "Dr Tornado Vertical Velocity Gained from B Press", "Down B")
            set_attribute_properties(self.attributes_unique[22], "Dr Tornado Terminal Velocity", "Down B")
        if self.name == "Falco":
            # ??? x 4
            set_attribute_properties(self.attributes_unique[4], "Blaster Launch Angle", "Neutral B")
            set_attribute_properties(self.attributes_unique[5], "Blaster Launch Speed", "Neutral B")
            # ??? x 3, 7 is Projectile ID
            set_attribute_properties(self.attributes_unique[9], "Phantasm Frames for Gravity Enable", "Side B")
            # ??? x 4
            set_attribute_properties(self.attributes_unique[14], "Phantasm Ground Friction", "Side B")
            set_attribute_properties(self.attributes_unique[15], "Phantasm Aerial Dash Speed", "Side B")
            set_attribute_properties(self.attributes_unique[16], "Phantasm Aerial Dash Momentum", "Side B")
            set_attribute_properties(self.attributes_unique[17], "Phantasm Aerial Dash Vertical Deceleration", "Side B")
            set_attribute_properties(self.attributes_unique[18], "Phantasm Ending Gravity", "Side B")
            # ???
            set_attribute_properties(self.attributes_unique[20], "Phantasm Landing Lag", "Side B")
            set_attribute_properties(self.attributes_unique[21], "Firebird Frames For Gravity Enable", "Up B")
            set_attribute_properties(self.attributes_unique[22], "Firebird Horizontal Momentum During Startup", "Up B")
            set_attribute_properties(self.attributes_unique[23], "Firebird Momentum Preservation", "Up B")
            set_attribute_properties(self.attributes_unique[24], "Firebird Fall Acceleration", "Up B")
            # ???
            set_attribute_properties(self.attributes_unique[26], "Firebird Frames of Travel", "Up B")
            # ???
            set_attribute_properties(self.attributes_unique[28], "Firebird Aerial Ending Momentum", "Up B")
            set_attribute_properties(self.attributes_unique[29], "Firebird Travel Speed", "Up B")
            set_attribute_properties(self.attributes_unique[30], "Firebird Reverse Acceleration", "Up B")
            set_attribute_properties(self.attributes_unique[31], "Firebird Grounded End Momentum", "Up B")
            # ???
            set_attribute_properties(self.attributes_unique[33], "Firebird Bounce H Velocity", "Up B")
            # ??? x 2
            set_attribute_properties(self.attributes_unique[36], "Firebird Landing Lag", "Up B")
            set_attribute_properties(self.attributes_unique[37], "Firebird Landing Lag After Bounce", "Up B")
            set_attribute_properties(self.attributes_unique[38], "Reflector Release Frames", "Down B")
            set_attribute_properties(self.attributes_unique[39], "Reflector Turn Animation Duration", "Down B")
            # ???
            set_attribute_properties(self.attributes_unique[41], "Reflector Frames for Gravity Enable", "Down B", True)
            set_attribute_properties(self.attributes_unique[42], "Reflector Momentum Preservation", "Down B")
            set_attribute_properties(self.attributes_unique[43], "Reflector Fall Acceleration", "Down B")
            # ???
            set_attribute_properties(self.attributes_unique[45], "Reflector Max Damage Reflectable", "Down B", True)
            # ??? x 3
            set_attribute_properties(self.attributes_unique[49], "Reflector Bubble Size", "Down B")
            set_attribute_properties(self.attributes_unique[50], "Reflector Damage Multiplier", "Down B")
            set_attribute_properties(self.attributes_unique[51], "Reflector Projectile Speed Multiplier", "Down B")

class Attribute():
    def __init__(self, name, data, offset):
        self.name = name
        self.data = data
        self.offset = offset
        if len(self.data) > 3:
            self.original_value = self.get_value()
        self.whole_number = False
        self.group = "None"
        self.chaos_threshold_max = 0
        self.chaos_threshold_min = 0

    def get_value(self):
        return struct.unpack('>f',self.data)[0]

    def set_value(self, float_value):
        data = struct.pack('>f', float_value)
        self.data = data

    def get_value_int(self):
        return get_word(self.data)
    
    def set_value_int(self, value):
        self.data = set_value(self.data, 0, 32, value)

class Attack():
    def __init__(self, fighter, name):
        self.fighter = fighter
        self.hitboxes = []
        self.name = name
        self.strength = 0
        self.type = ""
        self.balance = False
        self.vanilla = False
        self.shuffle_target = self
        self.shuffled = False
        # IDs: Damage: 0 | Shield Damage: 1 | Angle: 2 | BKB: 3 | KBG: 4 | WDSK: 5 | Size: 6 | Element: 7 | SFX: 8
        # Values: Unchanged: 0 | Shuffled: 1 | Deviated: 2 | Chaos: 3 
        self.randomization_types = [0,0,0,0,0,0,0,0,0]
        #
        self.original_stats = []
        
    def record_original_stats(self):
        self.original_stats.clear()
        self.original_stats.append(str(self.hitboxes[0].get_damage()))
        self.original_stats.append(str(self.hitboxes[0].get_angle()))
        self.original_stats.append(str(self.hitboxes[0].get_growth()))
        self.original_stats.append(str(self.hitboxes[0].get_base()))
        self.original_stats.append(str(self.hitboxes[0].get_set()))
        self.original_stats.append(str(self.hitboxes[0].get_shield()))
        self.original_stats.append(str(self.hitboxes[0].get_size()))
        self.original_stats.append(self.hitboxes[0].get_element())

    def determine_balance(self):
        # Code by Pelipper
        KB_TO_KILL = 188
        METRIC_1_NORM_FACTOR = 160 #a bit over fox up smash on mario at 70%
        METRIC_2_NORM_FACTOR = 401 #fox jab ko% lol
        def calc_metric_1(opponent_percent, move_damage, opponent_weight, base_kb, kbg, set_kb): #how much kb does this move do at opponent_percent?
            
            kbg_multiplier = kbg/100
            
            if set_kb == 0: #not set kb
                power_score = ( ( ( ( ( (opponent_percent-move_damage) / 10) + (opponent_percent * move_damage / 20) ) * (200 / (opponent_weight + 100) ) * 1.4 ) + 18 ) *  kbg_multiplier) + base_kb
                #subtracating opponent_percent-move_damage is because the formula is for the opponent percent after the attack,
                #and we want to measure this for what percent the opponent as it before the attack (ie a move that does 100% and kos at 0 is still bs lol)
                
            else: #set kb move
                power_score = ( ( ( ( 1 + (10 * set_kb / 20) ) * (200 / (opponent_weight + 100) ) * 1.4 ) + 18 ) *  kbg_multiplier) + base_kb
            
            return power_score
            
        def calc_metric_2(opponent_percent, move_damage, opponent_weight, base_kb, kbg, set_kb): #what percent does this move kill mario on bfield?

            kbg_multiplier = kbg/100
            
            if set_kb == 0:
                percent_to_kill = ( ( (KB_TO_KILL - base_kb)/kbg_multiplier) - 18)*( (opponent_weight+100)/(14*(2+move_damage)) )
                power_score = percent_to_kill - move_damage
                
            else: #this metric doesnt work for set kb so we'll just use the first one only lol
                power_score = calc_metric_1(opponent_percent, move_damage, opponent_weight, base_kb, kbg, set_kb)
            
            return power_score

        def euclidian_distance(move_1_metric_1, move_1_metric_2, move_2_metric_1, move_2_metric_2):
            norm_x = (move_1_metric_1/METRIC_1_NORM_FACTOR, move_1_metric_2/METRIC_2_NORM_FACTOR)
            norm_y = (move_2_metric_1/METRIC_1_NORM_FACTOR, move_2_metric_2/METRIC_2_NORM_FACTOR)
            return distance.euclidean(norm_x,norm_y)

        reference = self.hitboxes[0]
        if reference.get_growth() == 0:
            power_score = 10
        else:
            m1 = calc_metric_1(70, reference.get_damage(), 100, reference.get_base(), reference.get_growth(), reference.get_set())
            m2 = calc_metric_2(70, reference.get_damage(), 100, reference.get_base(), reference.get_growth(), reference.get_set())
            m3 = calc_metric_1(70, 55, 100, 50, 100, 0)
            m4 = calc_metric_2(70, 55, 100, 50, 100, 0)
            power_score = euclidian_distance(m1,m2,m3,m4)
        """
        if reference.get_set() == 0:
            p = 70
            d = reference.get_damage()
        else:
            p = 10
            d = reference.get_set()
        w = 100
        s = reference.get_growth()
        b = reference.get_base()
        
        power_score = ( ( ( (p / 10) + (p * d / 20) * (200 / (w + 100) ) * 1.4 ) + 18 ) * s / 100 ) + b
        """
        if power_score > 4 or (reference.get_growth() == 0 and reference.get_base() == 0) or reference.get_damage() == 0:
            self.strength = 0
        elif power_score > 3:
            self.strength = 1
        elif power_score > 2:
            self.strength = 2
        elif power_score > 1.8:
            self.strength = 3
        elif power_score > 1.6:
            self.strength = 4
        elif power_score > 1.45:
            self.strength = 5
        elif power_score > 1.3:
            self.strength = 6
        elif power_score > 1.1:
            self.strength = 7
        elif power_score > 0.9:
            self.strength = 8
        elif power_score > 0.7:
            self.strength = 9
        else:
            self.strength = 10
        

def process_name(name):
    prefixes = ["Koopa", "Captain", "Donkey", "Falco", "Fox", "Gamewatch",
                "Ganon", "Popo", "Purin", "Kirby", "Link", "Luigi",
                "Mario", "Mars", "Mewtwo", "Ness", "Peach", "Pichu",
                "Pikachu", "Emblem", "Samus", "Seak", "Yoshi", "Clink",
                "Zelda"]
    name = name.replace('5K_Share_ACTION_', '')
    name = name.replace('Ply', '')
    name = name.replace('_figatree', '')
    for prefix in prefixes:
        name = name.replace(prefix, "")

    if name == "Attack11":
        name = "Jab"
    if name == "Attack12":
        name = "Jab 2"
    if name == "Attack13":
        name = "Jab 3"
    if name == "AttackDash":
        name = "Dash Attack"
    if "AttackS3" in name:
        name = "Forward Tilt"
    if name == "AttackHi3":
        name = "Up Tilt"
    if name == "AttackLw3":
        name = "Down Tilt"
    if "AttackS4" in name:
        name = "Forward Smash"
    if name == "AttackHi4":
        name = "Up Smash"
    if name == "AttackLw4":
        name = "Down Smash"
    if name == "AttackAirN":
        name = "Neutral Aerial"
    if name == "AttackAirF":
        name = "Forward Aerial"
    if name == "AttackAirB":
        name = "Back Aerial"
    if name == "LandingAirB":
        name = "Back Aerial Landing"
    if name == "AttackAirHi":
        name = "Up Aerial"
    if name == "AttackAirLw":
        name = "Down Aerial"
    if name == "LandingAirLw":
        name = "Down Aerial Landing"
    if name == "DownAttackU":
        name = "Get-up Attack 1"
    if name == "DownAttackD":
        name = "Get-up Attack 2"
    if name == "CliffAttackSlow":
        name = "Ledge Attack High %"
    if name == "CliffAttackQuick":
        name = "Ledge Attack Low %"
    if name == "Catch":
        name = "Grab"
    if name == "CatchDash":
        name = "Dashing Grab"
    if name == "CatchAttack":
        name = "Pummel"
    if name == "ThrowF":
        name = "Forward Throw"
    if name == "ThrowFF":
        name = "Cargo Forward Throw"
    if name == "ThrowFB":
        name = "Cargo Back Throw"
    if name == "ThrowFHi":
        name = "Cargo Up Throw"
    if name == "ThrowFLw":
        name = "Cargo Down Throw"
    if name == "ThrowB":
        name = "Back Throw"
    if name == "ThrowHi":
        name = "Up Throw"
    if name == "ThrowLw":
        name = "Down Throw"
    if "SpecialN" in name:
        name = "Neutral Special"
    if "SpecialAirN" in name:
        name = "Aerial Neutral Special"
    if "SpecialS" in name:
        name = "Side Special"
    if "SpecialAirS" in name:
        name = "Aerial Side Special"
    if "SpecialHi" in name:
        name = "Up Special"
    if "SpecialAirHi" in name:
        name = "Aerial Up Special"
    if "SpecialLw" in name:
        name = "Down Special"
    if "SpecialAirLw" in name:
        name = "Aerial Down Special"
    if "SpecialLwLanding" in name:
        name = "Down Special Landing"
    return name




