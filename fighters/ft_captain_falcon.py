import fighter
from iso import DAT

falcon = fighter.Fighter("Captain Falcon", DAT(b'PlCa.dat'))
fighter.fighters.append(falcon)
falcon.fighter_id = 0x00

falcon.special_attribute_block_size = 0x8C
falcon.articles_sizes = []
falcon.articles_offsets = []
falcon.projectile_offsets = []

falcon.good_sfx = [0xea6a, 0xea7f, 0xea73, 0xea85, 0xea9a, 0xea9d, 0xea8e, 0xea79, 0xea94, 0xeaaf, 0xea6d, 0xeab2, 0xeaa6, 0xea7c, 0xeaac, 0xeaa9]

falcon.subactions[0x106].friendly_name = "Falcon Dive Throw"
falcon.subactions[0x107].friendly_name = "Falcon Dive Throw"
falcon.subactions[0x108].friendly_name = "Falcon Dive Throw"
falcon.subactions[0x109].friendly_name = "Falcon Dive Throw"
falcon.subactions[0x114].friendly_name = "Falcon Dive"
falcon.subactions[0x127].friendly_name = "Smash Item Swing"
falcon.subactions[0x128].friendly_name = "Smash Item Swing"
falcon.subactions[0x129].friendly_name = "Smash Item Swing"
falcon.subactions[0x12A].friendly_name = "Smash Item Swing"
falcon.subactions[0x12B].friendly_name = "Smash Item Swing"
falcon.subactions[0x12C].friendly_name = "Smash Item Swing"
falcon.subactions[0x12D].friendly_name = "Falcon Punch"
falcon.subactions[0x12E].friendly_name = "Falcon Punch"
falcon.subactions[0x12F].friendly_name = "Raptor Boost"
falcon.subactions[0x130].friendly_name = "Raptor Boost"
falcon.subactions[0x131].friendly_name = "Raptor Boost"
falcon.subactions[0x132].friendly_name = "Raptor Boost"
falcon.subactions[0x133].friendly_name = "Falcon Dive"
falcon.subactions[0x134].friendly_name = "Falcon Dive"
falcon.subactions[0x135].friendly_name = "Falcon Dive"
falcon.subactions[0x136].friendly_name = "Falcon Dive"
falcon.subactions[0x137].friendly_name = "Falcon Kick"
falcon.subactions[0x138].friendly_name = "Falcon Kick"
falcon.subactions[0x139].friendly_name = "Falcon Kick"
falcon.subactions[0x13A].friendly_name = "Falcon Kick"
falcon.subactions[0x13B].friendly_name = "Falcon Kick"
falcon.subactions[0x13C].friendly_name = "Falcon Kick"
falcon.subactions[0x13D].friendly_name = "Falcon Dive"

for action in falcon.subactions:
    if "Nameless" not in action.friendly_name:
        action.tags.append(action.friendly_name.lower().replace(" ", ""))

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

