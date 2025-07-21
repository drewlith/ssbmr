import fighter
from iso import DAT

roy = fighter.Fighter("Roy", DAT(b'PlFe.dat'))
fighter.fighters.append(roy)
roy.fighter_id = 0x17

roy.special_attribute_block_size = 0x98

roy.subactions[296].friendly_name = "Flare Blade"
roy.subactions[297].friendly_name = "Flare Blade"
roy.subactions[298].friendly_name = "Flare Blade (Charged)"
roy.subactions[299].friendly_name = "Flare Blade"
roy.subactions[300].friendly_name = "Flare Blade"
roy.subactions[301].friendly_name = "Flare Blade"
roy.subactions[302].friendly_name = "Flare Blade"
roy.subactions[303].friendly_name = "Double-Edge Dance 1 (Ground)"
roy.subactions[312].friendly_name = "Double-Edge Dance 1 (Aerial)"
roy.subactions[304].friendly_name = "Double-Edge Dance 2 (Ground) (Up)"
roy.subactions[313].friendly_name = "Double-Edge Dance 2 (Aerial) (Up)"
roy.subactions[305].friendly_name = "Double-Edge Dance 2 (Ground) (Down)"
roy.subactions[314].friendly_name = "Double-Edge Dance 2 (Aerial) (Down)"
roy.subactions[306].friendly_name = "Double-Edge Dance 3 (Ground) (Up)"
roy.subactions[315].friendly_name = "Double-Edge Dance 3 (Aerial) (Up)"
roy.subactions[307].friendly_name = "Double-Edge Dance 3 (Ground) (Side)"
roy.subactions[316].friendly_name = "Double-Edge Dance 3 (Aerial) (Side)"
roy.subactions[308].friendly_name = "Double-Edge Dance 3 (Ground) (Down)"
roy.subactions[317].friendly_name = "Double-Edge Dance 3 (Aerial) (Down)"
roy.subactions[309].friendly_name = "Double-Edge Dance 4 (Ground) (Up)"
roy.subactions[318].friendly_name = "Double-Edge Dance 4 (Aerial) (Up)"
roy.subactions[310].friendly_name = "Double-Edge Dance 4 (Ground) (Side)"
roy.subactions[319].friendly_name = "Double-Edge Dance 4 (Aerial) (Side)"
roy.subactions[311].friendly_name = "Double-Edge Dance 4 (Ground) (Down)"
roy.subactions[320].friendly_name = "Double-Edge Dance 4 (Aerial) (Down)"
roy.subactions[321].friendly_name = "Blazer"
roy.subactions[324].friendly_name = "Counter"

attribute_data = roy.dat_file.get_special_attribute_data(roy.special_attribute_block_size)
roy.add_attribute(attribute_data, 0x0, "Flare Blade Loops For Full Charge", 1)
roy.get_attribute("Flare Blade Loops For Full Charge").integer = True
roy.add_attribute(attribute_data, 0x4, "Flare Blade Base Damage", 1)
roy.get_attribute("Flare Blade Base Damage").integer = True
roy.add_attribute(attribute_data, 0x8, "Flare Blade Damage Per Loop", 1)
roy.get_attribute("Flare Blade Damage Per Loop").integer = True
roy.add_attribute(attribute_data, 0xC, "Flare Blade Momentum Preservation", 1)
roy.add_attribute(attribute_data, 0x10, "Flare Blade Deceleration Rate", 1)
roy.add_attribute(attribute_data, 0x14, "Double-Edge Dance Aerial Horizontal Momentum Preservation", 1)
roy.add_attribute(attribute_data, 0x18, "Double-Edge Dance Aerial Horizontal Deceleration", 1)
roy.add_attribute(attribute_data, 0x1C, "Double-Edge Dance Aerial Vertical Boost", 1)
roy.add_attribute(attribute_data, 0x20, "Double-Edge Dance Aerial Vertical Deceleration", 1)
roy.add_attribute(attribute_data, 0x24, "Double-Edge Dance Gravity", 1)
roy.add_attribute(attribute_data, 0x28, "Blazer Freefall Mobility", 1)
roy.add_attribute(attribute_data, 0x2C, "Blazer Landing Lag", 1)
roy.add_attribute(attribute_data, 0x3C, "Blazer Displacement From Input", 1)
roy.add_attribute(attribute_data, 0x40, "Blazer Aerial Height Ratio", 1)
roy.add_attribute(attribute_data, 0x44, "Blazer Gravity After Use", 1)
roy.add_attribute(attribute_data, 0x48, "Blazer Max Fall Speed After Use", 1)
roy.add_attribute(attribute_data, 0x4C, "Counter Horizontal Momentum", 1)
roy.add_attribute(attribute_data, 0x50, "Counter Horizontal Deceleration", 1)
roy.add_attribute(attribute_data, 0x54, "Counter Gravity", 1)
roy.add_attribute(attribute_data, 0x58, "Counter Maximum Falling Speed", 1)
roy.add_attribute(attribute_data, 0x5C, "Counter Damage Multiplier", 1)
roy.add_attribute(attribute_data, 0x60, "Counter Hitlag", 1)
roy.add_attribute(attribute_data, 0x74, "Counter Detection Bubble Size", 1)
roy.add_attribute(attribute_data, 0x78, "Sword Trail Fade", 1)
roy.add_attribute(attribute_data, 0x7C, "Sword Trail Length", 1)
roy.add_attribute(attribute_data, 0x90, "Sword Trail Width", 1)
roy.add_attribute(attribute_data, 0x94, "Sword Trail Height", 1)