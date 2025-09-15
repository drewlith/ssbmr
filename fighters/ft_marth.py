import fighter
from iso import DAT

marth = fighter.Fighter("Marth", DAT(b'PlMs.dat'))
fighter.fighters.append(marth)
marth.fighter_id = 0x09

marth.special_attribute_block_size = 0x98

marth.subactions[0x127].friendly_name = "Shield Breaker"
marth.subactions[0x128].friendly_name = "Shield Breaker"
marth.subactions[0x129].friendly_name = "Shield Breaker"
marth.subactions[0x12A].friendly_name = "Shield Breaker"
marth.subactions[0x12B].friendly_name = "Shield Breaker"
marth.subactions[0x12C].friendly_name = "Shield Breaker"
marth.subactions[0x12D].friendly_name = "Shield Breaker"
marth.subactions[0x12E].friendly_name = "Shield Breaker"
marth.subactions[0x12F].friendly_name = "Dancing Blade"
marth.subactions[0x130].friendly_name = "Dancing Blade"
marth.subactions[0x131].friendly_name = "Dancing Blade"
marth.subactions[0x132].friendly_name = "Dancing Blade"
marth.subactions[0x133].friendly_name = "Dancing Blade"
marth.subactions[0x134].friendly_name = "Dancing Blade"
marth.subactions[0x135].friendly_name = "Dancing Blade"
marth.subactions[0x136].friendly_name = "Dancing Blade"
marth.subactions[0x137].friendly_name = "Dancing Blade"
marth.subactions[0x138].friendly_name = "Dancing Blade"
marth.subactions[0x139].friendly_name = "Dancing Blade"
marth.subactions[0x13A].friendly_name = "Dancing Blade"
marth.subactions[0x13B].friendly_name = "Dancing Blade"
marth.subactions[0x13C].friendly_name = "Dancing Blade"
marth.subactions[0x13D].friendly_name = "Dancing Blade"
marth.subactions[0x13E].friendly_name = "Dancing Blade"
marth.subactions[0x13F].friendly_name = "Dancing Blade"
marth.subactions[0x140].friendly_name = "Dancing Blade"
marth.subactions[0x141].friendly_name = "Dolphin Slash"
marth.subactions[0x142].friendly_name = "Dolphin Slash"
marth.subactions[0x143].friendly_name = "Counter"
marth.subactions[0x144].friendly_name = "Counter"
marth.subactions[0x145].friendly_name = "Counter"
marth.subactions[0x146].friendly_name = "Counter"

for action in marth.subactions:
    if "Nameless" not in action.friendly_name:
        action.tags.append(action.friendly_name.lower().replace(" ", ""))

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
#marth.add_attribute(attribute_data, 0x78, "Sword Trail Fade", 1)
#marth.add_attribute(attribute_data, 0x7C, "Sword Trail Length", 1)
#marth.add_attribute(attribute_data, 0x90, "Sword Trail Width", 1)
#marth.add_attribute(attribute_data, 0x94, "Sword Trail Height", 1)