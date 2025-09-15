import fighter
from iso import DAT

dk = fighter.Fighter("Donkey Kong", DAT(b'PlDk.dat'))
fighter.fighters.append(dk)
dk.fighter_id = 0x01

dk.special_attribute_block_size = 0x74

dk.subactions[0x106].friendly_name = "Cargo Throw"
dk.subactions[0x107].friendly_name = "Cargo Throw"
dk.subactions[0x108].friendly_name = "Cargo Throw"
dk.subactions[0x109].friendly_name = "Cargo Throw"
dk.subactions[0x10B].friendly_name = "Cargo Throw"
dk.subactions[0x10C].friendly_name = "Cargo Throw"
dk.subactions[0x10D].friendly_name = "Cargo Throw"
dk.subactions[0x10E].friendly_name = "Cargo Throw"
dk.subactions[0x10F].friendly_name = "Cargo Throw"
dk.subactions[0x110].friendly_name = "Cargo Throw"
dk.subactions[0x111].friendly_name = "Cargo Throw"
dk.subactions[0x112].friendly_name = "Cargo Throw"
dk.subactions[0x113].friendly_name = "Cargo Throw"
dk.subactions[0x127].friendly_name = "Cargo Throw"
dk.subactions[0x128].friendly_name = "Cargo Throw"
dk.subactions[0x129].friendly_name = "Cargo Throw"
dk.subactions[0x12A].friendly_name = "Cargo Throw"
dk.subactions[0x12B].friendly_name = "Cargo Throw"
dk.subactions[0x12C].friendly_name = "Cargo Throw"
dk.subactions[0x12D].friendly_name = "Cargo Throw"
dk.subactions[0x12E].friendly_name = "Cargo Throw"
dk.subactions[0x12F].friendly_name = "Cargo Throw"
dk.subactions[0x130].friendly_name = "Cargo Throw"
dk.subactions[0x131].friendly_name = "Cargo Throw"
dk.subactions[0x132].friendly_name = "Cargo Throw"
dk.subactions[0x133].friendly_name = "Cargo Throw"
dk.subactions[0x134].friendly_name = "Cargo Throw"
dk.subactions[0x135].friendly_name = "Cargo Throw"
dk.subactions[0x136].friendly_name = "Cargo Throw"
dk.subactions[0x137].friendly_name = "Cargo Throw"
dk.subactions[0x138].friendly_name = "Cargo Throw"
dk.subactions[0x139].friendly_name = "Cargo Throw"
dk.subactions[0x13A].friendly_name = "Cargo Throw"
dk.subactions[0x13B].friendly_name = "Cargo Throw"
dk.subactions[0x13C].friendly_name = "Cargo Throw"
dk.subactions[0x13D].friendly_name = "Cargo Throw"
dk.subactions[0x13E].friendly_name = "Cargo Throw"
dk.subactions[0x13F].friendly_name = "Giant Punch"
#dk.subactions[0x140].friendly_name = "Giant Punch"
dk.subactions[0x141].friendly_name = "Giant Punch"
dk.subactions[0x142].friendly_name = "Giant Punch"
dk.subactions[0x143].friendly_name = "Giant Punch"
dk.subactions[0x144].friendly_name = "Giant Punch"
#dk.subactions[0x145].friendly_name = "Giant Punch"
dk.subactions[0x146].friendly_name = "Giant Punch"
dk.subactions[0x147].friendly_name = "Giant Punch"
dk.subactions[0x148].friendly_name = "Giant Punch"
dk.subactions[0x149].friendly_name = "Headbutt"
dk.subactions[0x14A].friendly_name = "Headbutt"
dk.subactions[0x14B].friendly_name = "Spinning Kong"
dk.subactions[0x14C].friendly_name = "Spinning Kong"
dk.subactions[0x14D].friendly_name = "Hand Slap"
dk.subactions[0x14E].friendly_name = "Hand Slap"
dk.subactions[0x14F].friendly_name = "Hand Slap"
dk.subactions[0x150].friendly_name = "Hand Slap"

for action in dk.subactions:
    if "Nameless" not in action.friendly_name:
        action.tags.append(action.friendly_name.lower().replace(" ", ""))

attribute_data = dk.dat_file.get_special_attribute_data(dk.special_attribute_block_size)
dk.add_attribute(attribute_data, 0x20, "Cargo Hold Turn Speed", 1)
dk.add_attribute(attribute_data, 0x24, "Cargo Hold Jump Startup", 1)
dk.add_attribute(attribute_data, 0x28, "Cargo Hold Jump Landing Lag", 1)
dk.add_attribute(attribute_data, 0x2C, "Giant Punch Arm Swings Needed To Full Charge", 1)
dk.get_attribute("Giant Punch Arm Swings Needed To Full Charge").integer = True
dk.add_attribute(attribute_data, 0x30, "Giant Punch Damage Increase Per Swing", 1)
dk.get_attribute("Giant Punch Damage Increase Per Swing").integer = True
dk.add_attribute(attribute_data, 0x34, "Giant Punch Grounded Forward Velocity Charged", 1)
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