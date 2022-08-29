import melee, random
from util import percent_chance

def randomize(fighter, magnitude, mode = 0):
    air_values = fighter.get_air_attributes()
    ground_values = fighter.get_ground_attributes()
    if mode == 0: # Faster or Slower
        air_values[0] = random.uniform(air_values[0] * (1-(magnitude*0.01)), # Gravity
                                       air_values[0] * (1+(magnitude*0.01)))
        air_values[1] = random.uniform(air_values[1] * (1-(magnitude*0.01)), # Terminal Velocity
                                       air_values[1] * (1+(magnitude*0.01)))
        air_values[2] = random.uniform(air_values[2] * (1-(magnitude*0.01)), # Mobility A
                                       air_values[2] * (1+(magnitude*0.01)))
        air_values[3] = random.uniform(air_values[3] * (1-(magnitude*0.01)), # Mobility B
                                       air_values[3] * (1+(magnitude*0.01)))
        air_values[4] = random.uniform(air_values[4] * (1-(magnitude*0.01)), # Max Air Horizontal Velocity
                                       air_values[4] * (1+(magnitude*0.01)))
        air_values[5] = random.uniform(air_values[5] * (1-(magnitude*0.01)), # Air Friction
                                       air_values[5] * (1+(magnitude*0.01)))
        air_values[6] = random.uniform(air_values[6] * (1-(magnitude*0.01)), # Fast Fall Terminal Velocity
                                       air_values[6] * (1+(magnitude*0.01)))
        
        ground_values[0] = random.uniform(ground_values[0] * (1-(magnitude*0.01)), # Walk Initial Velocity
                                          ground_values[0] * (1+(magnitude*0.01)))
        ground_values[2] = random.uniform(ground_values[2] * (1-(magnitude*0.01)), # Walk Max Velocity
                                          ground_values[2] * (1+(magnitude*0.01)))
        ground_values[6] = random.uniform(ground_values[6] * (1-(magnitude*0.01)), # Ground Friction
                                          ground_values[6] * (1+(magnitude*0.01)))
        ground_values[7] = random.uniform(ground_values[7] * (1-(magnitude*0.01)), # Dash Initial Velocity
                                          ground_values[7] * (1+(magnitude*0.01)))
        ground_values[10] = ground_values[7]  # Dash/Run Terminal Velocity (Making this the same as Dash Initial
                                              # Velocity prevents bugs involving super wavedashes.

    if mode == 1: # Faster only
        air_values[0] = random.uniform(air_values[0], # Gravity
                                       air_values[0] * (1+(magnitude*0.01)))
        air_values[1] = random.uniform(air_values[1], # Terminal Velocity
                                       air_values[1] * (1+(magnitude*0.01)))
        air_values[2] = random.uniform(air_values[2], # Mobility A
                                       air_values[2] * (1+(magnitude*0.01)))
        air_values[3] = random.uniform(air_values[3], # Mobility B
                                       air_values[3] * (1+(magnitude*0.01)))
        air_values[4] = random.uniform(air_values[4], # Max Air Horizontal Velocity
                                       air_values[4] * (1+(magnitude*0.01)))
        air_values[5] = random.uniform(air_values[5], # Air Friction
                                       air_values[5] * (1+(magnitude*0.01)))
        air_values[6] = random.uniform(air_values[6], # Fast Fall Terminal Velocity
                                       air_values[6] * (1+(magnitude*0.01)))
        
        ground_values[0] = random.uniform(ground_values[0], # Walk Initial Velocity
                                          ground_values[0] * (1+(magnitude*0.01)))
        ground_values[2] = random.uniform(ground_values[2], # Walk Max Velocity
                                          ground_values[2] * (1+(magnitude*0.01)))
        ground_values[6] = random.uniform(ground_values[6], # Ground Friction
                                          ground_values[6] * (1+(magnitude*0.01)))
        ground_values[7] = random.uniform(ground_values[7], # Dash Initial Velocity
                                          ground_values[7] * (1+(magnitude*0.01)))
        ground_values[10] = ground_values[7] # Dash/Run Terminal Velocity (Making this the same as Dash Initial
                                              # Velocity prevents bugs involving super wavedashes.
                                              
    if mode == 2: # Slower only
        air_values[0] = random.uniform(air_values[0] * (1-(magnitude*0.01)), # Gravity
                                       air_values[0])
        air_values[1] = random.uniform(air_values[1] * (1-(magnitude*0.01)), # Terminal Velocity
                                       air_values[1])
        air_values[2] = random.uniform(air_values[2] * (1-(magnitude*0.01)), # Mobility A
                                       air_values[2])
        air_values[3] = random.uniform(air_values[3] * (1-(magnitude*0.01)), # Mobility B
                                       air_values[3])
        air_values[4] = random.uniform(air_values[4] * (1-(magnitude*0.01)), # Max Air Horizontal Velocity
                                       air_values[4])
        air_values[5] = random.uniform(air_values[5] * (1-(magnitude*0.01)), # Air Friction
                                       air_values[5])
        air_values[6] = random.uniform(air_values[6] * (1-(magnitude*0.01)), # Fast Fall Terminal Velocity
                                       air_values[6])
        
        ground_values[0] = random.uniform(ground_values[0] * (1-(magnitude*0.01)), # Walk Initial Velocity
                                          ground_values[0])
        ground_values[2] = random.uniform(ground_values[2] * (1-(magnitude*0.01)), # Walk Max Velocity
                                          ground_values[2])
        ground_values[6] = random.uniform(ground_values[6] * (1-(magnitude*0.01)), # Ground Friction
                                          ground_values[6])
        ground_values[7] = random.uniform(ground_values[7] * (1-(magnitude*0.01)), # Dash Initial Velocity
                                          ground_values[7])
        ground_values[10] = ground_values[7] # Dash/Run Terminal Velocity (Making this the same as Dash Initial
                                              # Velocity prevents bugs involving super wavedashes.

    for value in air_values:
        if value <= 0:
            value = float(0.01)
    for value in ground_values:
        if value <= 0:
            value = float(0.01)
    fighter.set_air_attributes(air_values)
    fighter.set_ground_attributes(ground_values)

def start_mod(magnitude, mode = 0):
    for fighter in melee.fighters:
        if fighter.properties_offset <= 0:
            return
        randomize(fighter, magnitude, mode)
