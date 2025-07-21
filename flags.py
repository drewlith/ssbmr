from fighters import (ft_bowser, ft_boy, ft_captain_falcon, ft_crazy_hand, ft_dk, ft_dr_mario, ft_falco, ft_fox, ft_game_and_watch, ft_ganondorf, ft_giga_bowser, 
                      ft_girl, ft_jigglypuff, ft_kirby, ft_link, ft_luigi, ft_mario, ft_marth, ft_master_hand, ft_mewtwo, ft_nana, ft_ness, ft_peach, ft_pichu,
                      ft_pikachu, ft_popo, ft_roy, ft_samus, ft_sheik, ft_yoshi, ft_young_link, ft_zelda)
from random import randint as rng
from random import uniform as rng_f
from structs import hitbox, aura, sfx
from utility import percent_chance
import gecko, fsm, re, custom_flags

# Convention: No underscores since key phrase system use them as delimiters. Variable name will be key phrase name, as in what the user types into the flag
# The ":=" just lets you set a variable name within the ()s
all_fighters = []
all_fighters.append(bowser := ft_bowser.bowser)
all_fighters.append(boy := ft_boy.boy)
all_fighters.append(captainfalcon:= ft_captain_falcon.falcon)
all_fighters.append(crazyhand := ft_crazy_hand.crazy_hand)
all_fighters.append(dk := ft_dk.dk)
all_fighters.append(drmario := ft_dr_mario.dr_mario)
all_fighters.append(falco := ft_falco.falco)
all_fighters.append(fox := ft_fox.fox)
all_fighters.append(gameandwatch := ft_game_and_watch.game_and_watch)
all_fighters.append(ganondorf := ft_ganondorf.ganondorf)
all_fighters.append(gigabowser := ft_giga_bowser.giga_bowser)
all_fighters.append(girl := ft_girl.girl)
all_fighters.append(jigglypuff := ft_jigglypuff.jigglypuff)
all_fighters.append(kirby := ft_kirby.kirby)
all_fighters.append(link := ft_link.link)
all_fighters.append(luigi := ft_luigi.luigi)
all_fighters.append(mario := ft_mario.mario)
all_fighters.append(marth := ft_marth.marth)
all_fighters.append(masterhand := ft_master_hand.master_hand)
all_fighters.append(mewtwo := ft_mewtwo.mewtwo)
all_fighters.append(nana := ft_nana.nana)
all_fighters.append(ness := ft_ness.ness)
all_fighters.append(peach := ft_peach.peach)
all_fighters.append(pichu := ft_pichu.pichu)
all_fighters.append(pikachu := ft_pikachu.pikachu)
all_fighters.append(popo := ft_popo.popo)
all_fighters.append(roy := ft_roy.roy)
all_fighters.append(samus := ft_samus.samus)
all_fighters.append(sheik := ft_sheik.sheik)
all_fighters.append(yoshi := ft_yoshi.yoshi)
all_fighters.append(younglink := ft_young_link.young_link)
all_fighters.append(zelda := ft_zelda.zelda)

property_keys = ["damage", "angle", "growth", "setkb", "element", "shielddamage", "sfx", "size", "zoffset", "yoffset", "xoffset", "bone"]

def get_all_substrings(string, start_delim, end_delim):
    pattern = re.escape(start_delim) + "(.*?)" + re.escape(end_delim)
    results = re.findall(pattern, string)
    return results

def get_succeeding_num(string, character):
    pattern = rf"(?<={re.escape(character)})\s*(\d+)"
    match = re.findall(pattern, string)
    if match:
        return match
    return ""

class Flagset:
    def __init__(self, flags):
        self.flags = flags

    def find_flag(self, searching_for):
        for flag in self.flags:
            if searching_for in flag.original_name:
                return flag
        print("Flag not found.")
        return False

    def get_parameter(self, searching_for, parameter_id=0):
        target_flag = None
        for flag in self.flags:
            if searching_for in flag.text:
                target_flag = flag
                break
        return target_flag.parameters[parameter_id]

class Flag:
    def __init__(self, text):
        self.text = text
        self.original_text = text
        self.parameters = []
        self.key_phrases = []
        self.separator = False
        self.percents = False
        self.property_index = -1
        self.greater_than = False
        self.less_than = False
        self.not_equals = []
        self.equals = []
        self.chance = False
        self.excepts = []

    def __str__(self):
        string = "My key phrases are: " 
        for key_phrase in self.key_phrases:
            string += key_phrase + " "
        string += "\nMy parameters are: "
        for parameter in self.parameters:
            string += str(parameter) + " "
        if self.percents:
            string += "\nThis flag should randomize within a percentage range"
        return string

def get_custom_flags(_flags):
    _flags = _flags + " /"
    c_flags = get_all_substrings(_flags, "/", "/")
    for c_flag in c_flags:
        _flags = _flags.replace(c_flag, "")
    _flags = _flags.replace("/", "")
    _flags += custom_flags.standard(c_flags)
    _flags += custom_flags.custom(c_flags)
    return _flags

def parse_flags(_flags):
    _flags = get_custom_flags(_flags)
    print(_flags)
    # Step one, separate all the flags, into variable "flags"
    all_flags = get_all_substrings(_flags, "|", "|")
    flags = []
    for flag in all_flags:
        flags.append(Flag(flag))
    # Step GAIDEN CHAPTER get special instructions
    for flag in flags:
        special_instructions = get_all_substrings(flag.text, "[", "]")
        if len(special_instructions) > 0:
            special_instructions = special_instructions[0]
            special_instructions.replace(" ", "")
            flag.text = flag.text.replace(special_instructions, "")
            flag.text = flag.text.replace(" [", "")
            flag.text = flag.text.replace("] ", " ")

            def check_float(string):
                if "." in string:
                    return float(string)
                return int(string)

            greater_than = get_succeeding_num(special_instructions, ">")
            if len(greater_than) > 0:
                flag.greater_than = check_float(greater_than[0])
            
            less_than = get_succeeding_num(special_instructions, "<")
            if len(less_than) > 0:
                flag.less_than = check_float(less_than[0])

            nots = get_succeeding_num(special_instructions, "!")
            for _not in nots:
                flag.not_equals.append(check_float(_not))

            equals = get_succeeding_num(special_instructions, "=")
            for _equal in equals:
                flag.equals.append(check_float(_equal))

            chance = get_succeeding_num(special_instructions, "%")
            if len(chance) > 0:
                flag.chance = int(chance[0])

            excepts = get_succeeding_num(special_instructions, "$")
            for _except in excepts:
                flag.excepts.append(int(_except))

    # Step two, get all key phrases in each flag
        key_phrases = flag.text.split("_")
        last_phrase = key_phrases[len(key_phrases) - 1]
        flag.property_index = len(key_phrases) - 1
        last_phrase_check = last_phrase.split(" ")
        if len(last_phrase_check) > 1: # Step three, does a parameter exist for this flag?
            parameter_phrase = last_phrase_check[1]
            key_phrases[len(key_phrases) - 1] = last_phrase.replace(" " + parameter_phrase, "")
            parameters = parameter_phrase.replace(" ", "").split(":") # Get the parameters
            for p in parameters:
                # Step Four is there a percent?
                if "%" in p:
                    p = p.replace("%", "")
                    flag.percents = True
                flag.parameters.append(int(p))
            # Step Five, is there more than one parameter?
            if len(flag.parameters) > 1: # This flag should have a ":"
                flag.separator = True
            
        flag.key_phrases = key_phrases
        #print(flag.text, flag.key_phrases, flag.parameters, "Property:", flag.key_phrases[flag.property_index])
    flagset = Flagset(flags)
    return flagset

# How flags work:
# Flags have key phrases divided by "_"
# Flags have parameters (ints or floats) divided by ":" or there may be only 1 parameter with no ":"
# Key Phrase 1 is special and can change what happens completely: shuffle, exclude, etc... if left out, it turns the flag into a global flag
# Key Phrase 2..X-1 are tags and pick what character, what hitbox, what attribute, etc... Example: marth_fsmash_hitbox3, jigglypuff_pound
# Key Phrase X determines which property of the thing chosen above should be modified Example: damage, angle
# Some things like attributes don't need further specification from Key Phrase X so it won't be used in that regard
# You can add % sign to the parameters to randomize between percentages of the original, for example: fox_shine_damage 50%:200%
# Otherwise it's just a range fox_shine_damage 5:12 (damage will be randomly chosen a number from 5 to 12)
# Having just one parameter hard sets the value fox_shine_damage 20 (Fox's shine will do 20 damage)
# Some flags are just one key phrase, like -chaos

def percent_range(value, low, high):
    is_float = True
    if low > high:
        low, high = high, low
    if value == 0:
        return value
    if type(value) == int:
        value = float(value)
        is_float = False
    low = low * 0.01
    high = high * 0.01
    value = value * rng_f(low, high)
    if value < 0.0001 and value > 0:
        value = 0.0001
    if not is_float:
        value = round(value)
        value = int(value)
    return value

def get_fighter(fighter_name):
    for fighter in all_fighters:
        clean_name = fighter.name.replace("_", "")
        if fighter_name.lower() in clean_name.lower():
            return fighter
    print("No fighter found...")

def fighter_key(key_phrase):
    for fighter in all_fighters:
        clean_name = fighter.name.replace("_", "")
        if key_phrase.lower() in clean_name.lower():
            return True
    return False

def property_key(key_phrase):
    if len(key_phrase) < 1:
        return False
    for property in property_keys:
        if key_phrase.lower() in property:
            return True
    return False

def get_tag_keys(flag):
    tags = []
    for key_phrase in flag.key_phrases:
        if not fighter_key(key_phrase) and not property_key(key_phrase):
            tags.append(key_phrase)
    return tags

def compare_tags(object, tags):
    tags_exist = []
    for tag in tags:
        if tag in object.tags:
            tags_exist.append(True)
        else:
            tags_exist.append(False)
    for tag in tags_exist:
        if tag == False:
            return False
    return True

def hitbox_throw_changes(hitbox, flag):
    if hitbox.check_tags("exclude"):
        return
    if flag.property_index < 0: # Probably an attribute flag or bugged flag
        return
    # Special Instructions
    value = getattr(hitbox, flag.key_phrases[flag.property_index])
    if flag.greater_than:
        if value <= flag.greater_than:
            return
    if flag.less_than:
        if value >= flag.less_than:
            return
    if len(flag.not_equals) > 0:
        for exclusion in flag.not_equals:
            if value == exclusion:
                return
    if len(flag.equals) > 0:
        its_fine = False
        for inclusion in flag.equals:
            if value == inclusion:
                its_fine = True
        if not its_fine:
            return
    if flag.chance:
        inverse = 100 - flag.chance
        if percent_chance(inverse):
            return
    ###########################
    if len(flag.parameters) == 1: # Hard set the value if only one parameter given
        setattr(hitbox, flag.key_phrases[flag.property_index], flag.parameters[0])
        return
    if flag.percents and flag.separator: # If the flag has percentages associated with it, randomize a percentage range of the original value
        new_value = percent_range(getattr(hitbox, flag.key_phrases[flag.property_index]), flag.parameters[0], flag.parameters[1])
        setattr(hitbox, flag.key_phrases[flag.property_index], new_value)
        return
    if flag.separator: # If it doesn't have a percentage, randomize within a fixed range
        new_value = rng(flag.parameters[0], flag.parameters[1])
        if len(flag.excepts) > 0: # $ excepts included
            num_of_rerolls = 0
            while new_value in flag.excepts:
                new_value = rng(flag.parameters[0], flag.parameters[1])
                num_of_rerolls += 1
                if num_of_rerolls > 1000:
                    print("Too many rerolls from $ (Excepts condition). Seed might crash")
                    break
        setattr(hitbox, flag.key_phrases[flag.property_index], new_value)
        return
    
def attribute_changes(attribute, flag):
    if len(flag.parameters) == 1: # Hard set the value if only one parameter given
        attribute.value = flag.parameters[0]
        return
    if flag.percents and flag.separator: # If the flag has percentages associated with it, randomize a percentage range of the original value
        new_value = percent_range(attribute.value, flag.parameters[0], flag.parameters[1])
        attribute.value = new_value
        return
    if flag.separator: # If it doesn't have a percentage, randomize within a fixed range
        if type(flag.parameters[0]) == float or type(flag.parameters[1]) == float:
            new_value = rng_f(flag.parameters[0], flag.parameters[1])
            attribute.value = new_value
            return
        else:
            new_value = rng(flag.parameters[0], flag.parameters[1])
            if len(flag.excepts) > 0: # $ excepts included
                num_of_rerolls = 0
                while new_value in flag.excepts:
                    new_value = rng(flag.parameters[0], flag.parameters[1])
                    num_of_rerolls += 1
                    if num_of_rerolls > 1000:
                        print("Too many rerolls from $ (Excepts condition). Seed might crash")
                        break
            attribute.value = new_value
            return

def apply_changes(fighter, flag):
    tags = get_tag_keys(flag)
    for projectile in fighter.projectile_hitboxes:
        if compare_tags(projectile, tags):
            hitbox_throw_changes(projectile, flag)
    for subaction in fighter.subactions:
        for hitbox in subaction.hitboxes:
            if compare_tags(hitbox, tags):
                hitbox_throw_changes(hitbox, flag)
        for throw in subaction.throws:
            if compare_tags(throw, tags):
                hitbox_throw_changes(throw, flag)
    for attribute in fighter.attributes:
        if compare_tags(attribute, tags):
            attribute_changes(attribute, flag)

def activate_flags(flagset):
    hitbox.determine_power_ratings()
    for flag in flagset.flags:
        if "animations" in flag.key_phrases[0]:
            fsm.randomize_all()
        if "gecko" in flag.key_phrases[0]:
            if "shinebros" in flag.key_phrases[1]:
                gecko.activate_gecko_code("codes/Super Shine Bros - Uncle Punch.txt")
        if "exclude" in flag.key_phrases[0]: # Exclude Flag detected
            hitbox.exclude_hitboxes(flag.key_phrases[1])
        if "shuffle" in flag.key_phrases[0]: # Shuffle Flag detected
            if "hitboxes" in flag.key_phrases[1]: # Hitboxes
                if "balanced" in flag.key_phrases[2]:
                    hitbox.balanced_shuffle_all(flag.parameters[0])
                else:
                    hitbox.unbalanced_shuffle_all(flag.parameters[0])
            if "auras" in flag.key_phrases[1]: # Auras
                aura.shuffle(flag.parameters[0])
            
        if "randomize" in flag.key_phrases[0]: # Randomize Flag detected
            if "auras" in flag.key_phrases[1]:
                aura.randomize(flag.parameters[0])
            if "sfx" in flag.key_phrases[1]:
                sfx.randomize(flag.parameters[0])
        if not fighter_key(flag.key_phrases[0]): # Global Flag detected
            for fighter in all_fighters:
                apply_changes(fighter, flag)
        if fighter_key(flag.key_phrases[0]): # Fighter-specific Flag detected
            fighter = get_fighter(flag.key_phrases[0])
            apply_changes(fighter, flag)
        


        

        
            

                    


