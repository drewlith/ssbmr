import fighter
from iso import DAT

marth = fighter.Fighter("Marth", DAT(b'PlMs.dat'))
fighter.fighters.append(marth)
marth.fighter_id = 0x09

marth.special_attribute_block_size = 0x98

marth.subactions[296].friendly_name = "Shield Breaker"
marth.subactions[297].friendly_name = "Shield Breaker"
marth.subactions[298].friendly_name = "Shield Breaker (Charged)"
marth.subactions[299].friendly_name = "Shield Breaker"
marth.subactions[300].friendly_name = "Shield Breaker"
marth.subactions[301].friendly_name = "Shield Breaker"
marth.subactions[302].friendly_name = "Shield Breaker"
marth.subactions[303].friendly_name = "Dancing Blade 1 (Ground)"
marth.subactions[312].friendly_name = "Dancing Blade 1 (Aerial)"
marth.subactions[304].friendly_name = "Dancing Blade 2 (Ground) (Up)"
marth.subactions[313].friendly_name = "Dancing Blade 2 (Aerial) (Up)"
marth.subactions[305].friendly_name = "Dancing Blade 2 (Ground) (Down)"
marth.subactions[314].friendly_name = "Dancing Blade 2 (Aerial) (Down)"
marth.subactions[306].friendly_name = "Dancing Blade 3 (Ground) (Up)"
marth.subactions[315].friendly_name = "Dancing Blade 3 (Aerial) (Up)"
marth.subactions[307].friendly_name = "Dancing Blade 3 (Ground) (Side)"
marth.subactions[316].friendly_name = "Dancing Blade 3 (Aerial) (Side)"
marth.subactions[308].friendly_name = "Dancing Blade 3 (Ground) (Down)"
marth.subactions[317].friendly_name = "Dancing Blade 3 (Aerial) (Down)"
marth.subactions[309].friendly_name = "Dancing Blade 4 (Ground) (Up)"
marth.subactions[318].friendly_name = "Dancing Blade 4 (Aerial) (Up)"
marth.subactions[310].friendly_name = "Dancing Blade 4 (Ground) (Side)"
marth.subactions[319].friendly_name = "Dancing Blade 4 (Aerial) (Side)"
marth.subactions[311].friendly_name = "Dancing Blade 4 (Ground) (Down)"
marth.subactions[320].friendly_name = "Dancing Blade 4 (Aerial) (Down)"
marth.subactions[321].friendly_name = "Dolphin Slash"
marth.subactions[324].friendly_name = "Counter"

attribute_data = marth.dat_file.get_special_attribute_data(marth.special_attribute_block_size)
marth.add_attribute(attribute_data, 0x0, "Shield Breaker Loops For Full Charge", 1)
marth.get_attribute("Shield Breaker Loops For Full Charge").integer = True
marth.add_attribute(attribute_data, 0x4, "Shield Breaker Base Damage", 1)
marth.get_attribute("Shield Breaker Base Damage").integer = True
marth.add_attribute(attribute_data, 0x8, "Shield Breaker Damage Per Loop", 1)
marth.get_attribute("Shield Breaker Damage Per Loop").integer = True
marth.add_attribute(attribute_data, 0xC, "Shield Breaker Momentum Preservation", 1)
marth.add_attribute(attribute_data, 0x10, "Shield Breaker Deceleration Rate", 1)
marth.add_attribute(attribute_data, 0x14, "Dancing Blade Aerial Horizontal Momentum Preservation", 1)
marth.add_attribute(attribute_data, 0x18, "Dancing Blade Aerial Horizontal Deceleration", 1)
marth.add_attribute(attribute_data, 0x1C, "Dancing Blade Aerial Vertical Boost", 1)
marth.add_attribute(attribute_data, 0x20, "Dancing Blade Aerial Vertical Deceleration", 1)
marth.add_attribute(attribute_data, 0x24, "Dancing Blade Gravity", 1)
marth.add_attribute(attribute_data, 0x28, "Dolphin Slash Freefall Mobility", 1)
marth.add_attribute(attribute_data, 0x2C, "Dolphin Slash Landing Lag", 1)
marth.add_attribute(attribute_data, 0x3C, "Dolphin Slash Displacement From Input", 1)
marth.add_attribute(attribute_data, 0x40, "Dolphin Slash Aerial Height Ratio", 1)
marth.add_attribute(attribute_data, 0x44, "Dolphin Slash Gravity After Use", 1)
marth.add_attribute(attribute_data, 0x48, "Dolphin Slash Max Fall Speed After Use", 1)
marth.add_attribute(attribute_data, 0x4C, "Counter Horizontal Momentum", 1)
marth.add_attribute(attribute_data, 0x50, "Counter Horizontal Deceleration", 1)
marth.add_attribute(attribute_data, 0x54, "Counter Gravity", 1)
marth.add_attribute(attribute_data, 0x58, "Counter Maximum Falling Speed", 1)
marth.add_attribute(attribute_data, 0x5C, "Counter Damage Multiplier", 1)
marth.add_attribute(attribute_data, 0x60, "Counter Hitlag", 1)
marth.add_attribute(attribute_data, 0x74, "Counter Detection Bubble Size", 1)
marth.add_attribute(attribute_data, 0x78, "Sword Trail Fade", 1)
marth.add_attribute(attribute_data, 0x7C, "Sword Trail Length", 1)
marth.add_attribute(attribute_data, 0x90, "Sword Trail Width", 1)
marth.add_attribute(attribute_data, 0x94, "Sword Trail Height", 1)