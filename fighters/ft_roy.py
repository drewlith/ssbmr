import fighter
from iso import DAT

roy = fighter.Fighter("Roy", DAT(b'PlFe.dat'))
fighter.fighters.append(roy)
roy.fighter_id = 0x17

roy.special_attribute_block_size = 0x98

roy.subactions[0x127].friendly_name = "Flare Blade"
roy.subactions[0x128].friendly_name = "Flare Blade"
roy.subactions[0x129].friendly_name = "Flare Blade"
roy.subactions[0x12A].friendly_name = "Flare Blade"
roy.subactions[0x12B].friendly_name = "Flare Blade"
roy.subactions[0x12C].friendly_name = "Flare Blade"
roy.subactions[0x12D].friendly_name = "Flare Blade"
roy.subactions[0x12E].friendly_name = "Flare Blade"
roy.subactions[0x12F].friendly_name = "Double Edge Dance"
roy.subactions[0x130].friendly_name = "Double Edge Dance"
roy.subactions[0x131].friendly_name = "Double Edge Dance"
roy.subactions[0x132].friendly_name = "Double Edge Dance"
roy.subactions[0x133].friendly_name = "Double Edge Dance"
roy.subactions[0x134].friendly_name = "Double Edge Dance"
roy.subactions[0x135].friendly_name = "Double Edge Dance"
roy.subactions[0x136].friendly_name = "Double Edge Dance"
roy.subactions[0x137].friendly_name = "Double Edge Dance"
roy.subactions[0x138].friendly_name = "Double Edge Dance"
roy.subactions[0x139].friendly_name = "Double Edge Dance"
roy.subactions[0x13A].friendly_name = "Double Edge Dance"
roy.subactions[0x13B].friendly_name = "Double Edge Dance"
roy.subactions[0x13C].friendly_name = "Double Edge Dance"
roy.subactions[0x13D].friendly_name = "Double Edge Dance"
roy.subactions[0x13E].friendly_name = "Double Edge Dance"
roy.subactions[0x13F].friendly_name = "Double Edge Dance"
roy.subactions[0x140].friendly_name = "Double Edge Dance"
roy.subactions[0x141].friendly_name = "Blazer"
roy.subactions[0x142].friendly_name = "Blazer"
roy.subactions[0x143].friendly_name = "Counter"
roy.subactions[0x144].friendly_name = "Counter"
roy.subactions[0x145].friendly_name = "Counter"
roy.subactions[0x146].friendly_name = "Counter"

for action in roy.subactions:
    if "Nameless" not in action.friendly_name:
        action.tags.append(action.friendly_name.lower().replace(" ", ""))

attribute_data = roy.dat_file.get_special_attribute_data(roy.special_attribute_block_size)
roy.add_attribute(attribute_data, 0x0, "Flare Blade Loops For Full Charge", 1)
roy.get_attribute("Flare Blade Loops For Full Charge").integer = True
roy.add_attribute(attribute_data, 0x4, "Flare Blade Base Damage", 1)
roy.get_attribute("Flare Blade Base Damage").integer = True
roy.add_attribute(attribute_data, 0x8, "Flare Blade Damage Per Loop", 1)
roy.get_attribute("Flare Blade Damage Per Loop").integer = True
roy.add_attribute(attribute_data, 0xC, "Flare Blade Momentum Preservation", 1)
roy.add_attribute(attribute_data, 0x10, "Flare Blade Deceleration Rate", 1)
roy.add_attribute(attribute_data, 0x14, "Double Edge Dance Aerial Horizontal Momentum Preservation", 1)
roy.add_attribute(attribute_data, 0x18, "Double Edge Dance Aerial Horizontal Deceleration", 1)
roy.add_attribute(attribute_data, 0x1C, "Double Edge Dance Aerial Vertical Boost", 1)
roy.add_attribute(attribute_data, 0x20, "Double Edge Dance Aerial Vertical Deceleration", 1)
roy.add_attribute(attribute_data, 0x24, "Double Edge Dance Gravity", 1)
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
#roy.add_attribute(attribute_data, 0x78, "Sword Trail Fade", 1)
#roy.add_attribute(attribute_data, 0x7C, "Sword Trail Length", 1)
#roy.add_attribute(attribute_data, 0x90, "Sword Trail Width", 1)
#roy.add_attribute(attribute_data, 0x94, "Sword Trail Height", 1)