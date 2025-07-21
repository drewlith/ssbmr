import fighter
from iso import DAT

ganondorf = fighter.Fighter("Ganondorf", DAT(b'PlGn.dat'))
fighter.fighters.append(ganondorf)
ganondorf.fighter_id = 0x19

ganondorf.special_attribute_block_size = 0x8C
ganondorf.articles_sizes = []
ganondorf.articles_offsets = []
ganondorf.projectile_offsets = []

ganondorf.subactions[301].friendly_name = "Warlock Punch (Ground)"
ganondorf.subactions[302].friendly_name = "Warlock Punch (Aerial)"
ganondorf.subactions[304].friendly_name = "Gerudo Dragon (Ground)"
ganondorf.subactions[306].friendly_name = "Gerudo Dragon (Aerial)"
ganondorf.subactions[309].friendly_name = "Dark Dive"
ganondorf.subactions[311].friendly_name = "Wizard's Foot (Ground)"
ganondorf.subactions[313].friendly_name = "Wizard's Foot (Aerial)"
ganondorf.subactions[314].friendly_name = "Wizard's Foot (Landing)"


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
ganondorf.add_attribute(attribute_data, 0x74, "Wizard's Foot Speed Modifier After Hit", 1)
ganondorf.add_attribute(attribute_data, 0x7C, "Wizard's Foot Ground Lag Multiplier", 1)
ganondorf.add_attribute(attribute_data, 0x80, "Wizard's Foot Landing Lag Multiplier", 1)
ganondorf.add_attribute(attribute_data, 0x84, "Wizard's Foot Ground Traction", 1)
ganondorf.add_attribute(attribute_data, 0x88, "Wizard's Foot Landing Traction", 1)