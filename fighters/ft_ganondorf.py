import fighter
from iso import DAT

ganondorf = fighter.Fighter("Ganondorf", DAT(b'PlGn.dat'))
fighter.fighters.append(ganondorf)
ganondorf.fighter_id = 0x19

ganondorf.special_attribute_block_size = 0x8C
ganondorf.articles_sizes = []
ganondorf.articles_offsets = []
ganondorf.projectile_offsets = []

ganondorf.good_sfx = [0x493ea, 0x493f0, 0x493ff, 0x49411, 0x49414, 0x49405, 0x493e7, 0x49420, 0x4940e, 0x49429, 0x49438, 0x49432, 0x4942f]

ganondorf.subactions[0x12D].friendly_name = "Warlock Punch"
ganondorf.subactions[0x12E].friendly_name = "Warlock Punch"
ganondorf.subactions[0x12F].friendly_name = "Gerudo Dragon"
ganondorf.subactions[0x130].friendly_name = "Gerudo Dragon"
ganondorf.subactions[0x131].friendly_name = "Gerudo Dragon"
ganondorf.subactions[0x132].friendly_name = "Gerudo Dragon"
ganondorf.subactions[0x133].friendly_name = "Dark Dive"
ganondorf.subactions[0x134].friendly_name = "Dark Dive"
ganondorf.subactions[0x135].friendly_name = "Dark Dive"
ganondorf.subactions[0x136].friendly_name = "Dark Dive"
ganondorf.subactions[0x137].friendly_name = "Wizards Foot"
ganondorf.subactions[0x138].friendly_name = "Wizards Foot"
ganondorf.subactions[0x139].friendly_name = "Wizards Foot"
ganondorf.subactions[0x13A].friendly_name = "Wizards Foot"
ganondorf.subactions[0x13B].friendly_name = "Wizards Foot"
ganondorf.subactions[0x13C].friendly_name = "Wizards Foot"
ganondorf.subactions[0x13D].friendly_name = "Dark Dive"

for action in ganondorf.subactions:
    if "Nameless" not in action.friendly_name:
        action.tags.append(action.friendly_name.lower().replace(" ", ""))

attribute_data = ganondorf.dat_file.get_special_attribute_data(ganondorf.special_attribute_block_size)
ganondorf.add_attribute(attribute_data, 0x08, "Warlock Punch Momentum", 1)
ganondorf.add_attribute(attribute_data, 0x0C, "Aerial Warlock Punch Angle Difference", 1)
ganondorf.add_attribute(attribute_data, 0x10, "Aerial Warlock Punch Vertical Momentum", 1)
ganondorf.add_attribute(attribute_data, 0x14, "Gerudo Dragon Gravity After Hit", 1)
ganondorf.add_attribute(attribute_data, 0x18, "Gerudo Dragon Gravity After Whiff A", 1)
ganondorf.add_attribute(attribute_data, 0x1C, "Gerudo Dragon Gravity After Whiff B", 1)
ganondorf.add_attribute(attribute_data, 0x38, "Gerudo Dragon Whiff Landing Lag", 1)
ganondorf.add_attribute(attribute_data, 0x3C, "Gerudo Dragon Success Landing Lag", 1)
ganondorf.add_attribute(attribute_data, 0x40, "Dark Dive Air Friction Multiplier", 1)
ganondorf.add_attribute(attribute_data, 0x44, "Dark Dive Horizontal Momentum", 1)
ganondorf.add_attribute(attribute_data, 0x48, "Dark Dive Freefall Speed Multiplier", 1)
ganondorf.add_attribute(attribute_data, 0x4C, "Dark Dive Landing Lag", 1)
ganondorf.add_attribute(attribute_data, 0x60, "Dark Dive Gravity During Throw", 1)
ganondorf.add_attribute(attribute_data, 0x74, "Wizards Foot Speed Modifier After Hit", 1)
ganondorf.add_attribute(attribute_data, 0x7C, "Wizards Foot Ground Lag Multiplier", 1)
ganondorf.add_attribute(attribute_data, 0x80, "Wizards Foot Landing Lag Multiplier", 1)
ganondorf.add_attribute(attribute_data, 0x84, "Wizards Foot Ground Traction", 1)
ganondorf.add_attribute(attribute_data, 0x88, "Wizards Foot Landing Traction", 1)