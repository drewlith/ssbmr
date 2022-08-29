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
        values[0] = float(random.randint(2,9)) # Land Lag (Empty Land)
        for i in range(len(values)):
            if i != 0:
                values[i] = float(random.randint(values[i], values[i]+magnitude))

    for i in range(len(values)): # Prevent underflow and set a floor on landing lag frames.
        if values[i] <= 6 and i != 0:
            values[i] = 6
                
    fighter.set_landing_lags(values)

def start_mod(magnitude, mode = 0):
    for fighter in melee.fighters:
        if fighter.properties_offset <= 0:
            return
        randomize(fighter, magnitude, mode)
