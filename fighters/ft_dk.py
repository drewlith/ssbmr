import fighter
from iso import DAT

dk = fighter.Fighter("Donkey Kong", DAT(b'PlDk.dat'))
fighter.fighters.append(dk)
dk.fighter_id = 0x01

dk.special_attribute_block_size = 0x74
dk.subactions[322].friendly_name = "Giant Punch (Ground, No Charge)"
dk.subactions[323].friendly_name = "Giant Punch (Ground, Charged)"
dk.subactions[327].friendly_name = "Giant Punch (Aerial, No Charge)"
dk.subactions[328].friendly_name = "Giant Punch (Aerial, Charged)"
dk.subactions[329].friendly_name = "Headbutt (Ground)"
dk.subactions[330].friendly_name = "Headbutt (Aerial)"
dk.subactions[331].friendly_name = "Spinning Kong (Ground)"
dk.subactions[332].friendly_name = "Spinning Kong (Aerial)"
dk.subactions[334].friendly_name = "Hand Slap"

attribute_data = dk.dat_file.get_special_attribute_data(dk.special_attribute_block_size)
dk.add_attribute(attribute_data, 0x20, "Cargo Hold Turn Speed", 1)
dk.add_attribute(attribute_data, 0x24, "Cargo Hold Jump Startup", 1)
dk.add_attribute(attribute_data, 0x28, "Cargo Hold Jump Landing Lag", 1)
dk.add_attribute(attribute_data, 0x2C, "Giant Punch Arm Swings Needed To Full Charge", 1)
dk.get_attribute("Giant Punch Arm Swings Needed To Full Charge").integer = True
dk.add_attribute(attribute_data, 0x30, "Giant Punch Damage Increase Per Swing", 1)
dk.get_attribute("Giant Punch Damage Increase Per Swing").integer = True
dk.add_attribute(attribute_data, 0x34, "Giant Punch Grounded Forward Velocity (Charged)", 1)
dk.add_attribute(attribute_data, 0x38, "Giant Punch Landing Lag", 1)
dk.add_attribute(attribute_data, 0x40, "Headbutt Momentum Transfer Modifier", 1)
dk.add_attribute(attribute_data, 0x44, "Headbutt Gravity", 1)
dk.add_attribute(attribute_data, 0x4C, "Spinning Kong Aerial Vertical Velocity", 1)
dk.add_attribute(attribute_data, 0x50, "Spinning Kong Aerial Gravity", 1)
dk.add_attribute(attribute_data, 0x54, "Spinning Kong Grounded Horizontal Velocity", 1)
dk.add_attribute(attribute_data, 0x58, "Spinning Kong Aerial Horizontal Velocity", 1)
dk.add_attribute(attribute_data, 0x5C, "Spinning Kong Grounded Mobility", 1)
dk.add_attribute(attribute_data, 0x60, "Spinning Kong Aerial Mobility", 1)
dk.add_attribute(attribute_data, 0x64, "Spinning Kong Landing Lag", 1)
dk.add_attribute(attribute_data, 0x68, "Hand Slap Hitbox X Offset 1", 1)
dk.add_attribute(attribute_data, 0x6C, "Hand Slap Hitbox X Offset 2", 1)