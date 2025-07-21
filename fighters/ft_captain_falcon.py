import fighter
from iso import DAT

falcon = fighter.Fighter("Captain Falcon", DAT(b'PlCa.dat'))
fighter.fighters.append(falcon)
falcon.fighter_id = 0x00

falcon.special_attribute_block_size = 0x8C
falcon.articles_sizes = []
falcon.articles_offsets = []
falcon.projectile_offsets = []

falcon.subactions[301].friendly_name = "Falcon Punch (Ground)"
falcon.subactions[302].friendly_name = "Falcon Punch (Aerial)"
falcon.subactions[304].friendly_name = "Raptor Boost (Ground)"
falcon.subactions[306].friendly_name = "Raptor Boost (Aerial)"
falcon.subactions[309].friendly_name = "Falcon Dive"
falcon.subactions[311].friendly_name = "Falcon Kick (Ground)"
falcon.subactions[313].friendly_name = "Falcon Kick (Aerial)"
falcon.subactions[314].friendly_name = "Falcon Kick (Landing)"

attribute_data = falcon.dat_file.get_special_attribute_data(falcon.special_attribute_block_size)
falcon.add_attribute(attribute_data, 0x08, "Falcon Punch Momentum", 1)
falcon.add_attribute(attribute_data, 0x0C, "Aerial Falcon Punch Angle Difference", 1)
falcon.add_attribute(attribute_data, 0x10, "Aerial Falcon Punch Vertical Momentum", 1)
falcon.add_attribute(attribute_data, 0x14, "Raptor Boost Gravity After Hit", 1)
falcon.add_attribute(attribute_data, 0x18, "Raptor Boost Gravity After Whiff A", 1)
falcon.add_attribute(attribute_data, 0x1C, "Raptor Boost Gravity After Whiff B", 1)
falcon.add_attribute(attribute_data, 0x38, "Raptor Boost Whiff Landing Lag", 1)
falcon.add_attribute(attribute_data, 0x3C, "Raptor Boost Success Landing Lag", 1)
falcon.add_attribute(attribute_data, 0x40, "Falcon Dive Air Friction Multiplier", 1)
falcon.add_attribute(attribute_data, 0x44, "Falcon Dive Horizontal Momentum", 1)
falcon.add_attribute(attribute_data, 0x48, "Falcon Dive Freefall Speed Multiplier", 1)
falcon.add_attribute(attribute_data, 0x4C, "Falcon Dive Landing Lag", 1)
falcon.add_attribute(attribute_data, 0x60, "Falcon Dive Gravity During Throw", 1)
falcon.add_attribute(attribute_data, 0x74, "Falcon Kick Speed Modifier After Hit", 1)
falcon.add_attribute(attribute_data, 0x7C, "Falcon Kick Ground Lag Multiplier", 1)
falcon.add_attribute(attribute_data, 0x80, "Falcon Kick Landing Lag Multiplier", 1)
falcon.add_attribute(attribute_data, 0x84, "Falcon Kick Ground Traction", 1)
falcon.add_attribute(attribute_data, 0x88, "Falcon Kick Landing Traction", 1)

