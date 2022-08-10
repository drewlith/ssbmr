# Vanilla mod by drewlith. Removes certain objects from the randomizer,
# preserving them as "vanilla". This should be run before other mods.
import melee, random
from util import percent_chance

def start_mod(percent):
    for fighter in melee.fighters:
        if percent_chance(percent):         # Setting this to 0 will prevent attribute
            fighter.properties_offset = 0   # Randomization
        new_attacks = []
        for attack in fighter.attacks:
            if not percent_chance(percent):
                new_attacks.append(attack)
        fighter.attacks = new_attacks
        new_throws = []
        for throw in fighter.throws:
            if not percent_chance(percent):
                new_throws.append(throw)
        fighter.throws = new_throws
        
    
        
