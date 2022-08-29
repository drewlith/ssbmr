import melee, random
from util import percent_chance

def randomize(fighter, magnitude, mode = 0):
    values = fighter.get_jump_attributes()
    if mode == 0: # Faster or Slower
        values[0] = float(random.randint(3,6)) # Jumpsquat
        if percent_chance(5):
            values[0] = values[0] + 1
        if percent_chance(1):
            values[0] = values[0] - 1
        values[1] = 1 # Initial Horizontal Velocity (1 prevents bugs)
        values[2] = random.uniform(values[2] * (1-(magnitude*0.01)), # Initial Vertical Velocity
                                   values[2] * (1+(magnitude*0.01)))
        values[3] = random.uniform(values[3] * (1-(magnitude*0.01)), # Ground to Air Jump Multiplier
                                   values[3] * (1+(magnitude*0.01)))
        values[4] = 1 # Max Horizontal Velocity (1 prevents bugs)
        values[5] = random.uniform(values[5] * (1-(magnitude*0.01)), # Shorthop Vertical Velocity
                                   values[5] * (1+(magnitude*0.01)))
        values[6] = random.uniform(values[6] * (1-(magnitude*0.01)), # Air Jump Multiplier
                                   values[6] * (1+(magnitude*0.01)))
        values[7] = random.uniform(values[7] * (1-(magnitude*0.01)), # Double Jump Momentum
                                   values[7] * (1+(magnitude*0.01)))

    if mode == 1: # Faster only
        values[0] = float(random.randint(3,4)) # Jumpsquat
        if percent_chance(1):
            values[0] = values[0] - 1
        values[1] = 1 # Initial Horizontal Velocity (1 prevents bugs)
        values[2] = random.uniform(values[2], # Initial Vertical Velocity
                                   values[2] * (1+(magnitude*0.01)))
        values[3] = random.uniform(values[3], # Ground to Air Jump Multiplier
                                   values[3] * (1+(magnitude*0.01)))
        values[4] = 1 # Max Horizontal Velocity (1 prevents bugs)
        values[5] = random.uniform(values[5], # Shorthop Vertical Velocity
                                   values[5] * (1+(magnitude*0.01)))
        values[6] = random.uniform(values[6], # Air Jump Multiplier
                                   values[6] * (1+(magnitude*0.01)))
        values[7] = random.uniform(values[7], # Double Jump Momentum
                                   values[7] * (1+(magnitude*0.01)))
                                              
    if mode == 2: # Slower only
        values[0] = float(random.randint(3,8)) # Jumpsquat
        if percent_chance(10):
            values[0] = values[0] + 1
        values[1] = 1 # Initial Horizontal Velocity (1 prevents bugs)
        values[2] = random.uniform(values[2] * (1-(magnitude*0.01)), # Initial Vertical Velocity
                                   values[2])
        values[3] = random.uniform(values[3] * (1-(magnitude*0.01)), # Ground to Air Jump Multiplier
                                   values[3])
        values[4] = 1 # Max Horizontal Velocity (1 prevents bugs)
        values[5] = random.uniform(values[5] * (1-(magnitude*0.01)), # Shorthop Vertical Velocity
                                   values[5])
        values[6] = random.uniform(values[6] * (1-(magnitude*0.01)), # Air Jump Multiplier
                                   values[6])
        values[7] = random.uniform(values[7] * (1-(magnitude*0.01)), # Double Jump Momentum
                                   values[7])

    for value in values:
        if value <= 0:
            value = float(0.01)
    fighter.set_jump_attributes(values)

    

def start_mod(magnitude, mode = 0):
    for fighter in melee.fighters:
        if fighter.properties_offset <= 0:
            return
        randomize(fighter, magnitude, mode)
