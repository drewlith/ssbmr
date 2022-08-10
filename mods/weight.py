import melee, random
from util import percent_chance

def randomize(fighter):
    fighter.set_weight(float(random.randint(5,12)*10))

def shuffle(fighter):
    t = fighter.get_weight()
    fighter.set_weight(fighter.shuffle_target.get_weight())
    fighter.shuffle_target.set_weight(t)

def start_mod(shuffle_percent):
    for fighter in melee.fighters:
        if fighter.properties_offset <= 0:
            return
        if percent_chance(shuffle_percent):
            shuffle(fighter)
        else:
            randomize(fighter)
        
        
