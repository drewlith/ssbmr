import melee, random
from util import percent_chance

def randomize(fighter, magnitude, mode = 0):
    values = fighter.get_landing_lags()
    if mode == 0: # Faster or Slower
        values[0] = float(random.randint(2,4)) # Land Lag (Empty Land)
        for i in range(len(values)):
            if i != 0:
                values[i] = float(random.randint(values[i]-magnitude, values[i]+magnitude))
    
    
    if mode == 1: # Faster only
        values[0] = float(random.randint(1,2)) # Land Lag (Empty Land)
        for i in range(len(values)):
            if i != 0:
                values[i] = float(random.randint(values[i]-magnitude, values[i]))
                                              
    if mode == 2: # Slower only
        values[0] = float(random.randint(1,2)) # Land Lag (Empty Land)
        for i in range(len(values)):
            if i != 0:
                values[i] = float(random.randint(values[i], values[i]+magnitude))
                
    fighter.set_landing_lags(values)

def start_mod(magnitude, mode = 0):
    for fighter in melee.fighters:
        if fighter.properties_offset <= 0:
            return
        randomize(fighter, magnitude, mode)
