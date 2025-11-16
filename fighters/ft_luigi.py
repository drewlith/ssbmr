import fighter
from structs import hitbox
from iso import DAT

luigi = fighter.Fighter("Luigi", DAT(b'PlLg.dat'))
fighter.fighters.append(luigi)
luigi.fighter_id = 0x07

luigi.special_attribute_block_size = 0x98
luigi.articles_sizes = [0x84, 0x10]
luigi.articles_offsets = [0x3A3C, 0x3A74]
luigi.projectile_offsets = [0x3AA4]

luigi.good_sfx = [0x29854, 0x29839, 0x2983f, 0x29851, 0x29860, 0x29863, 0x2982d, 0x29818, 0x29830, 0x29833, 0x29836, 0x2981e, 0x2984b]

luigi.subactions[0x127].friendly_name = "Fireball"
luigi.subactions[0x128].friendly_name = "Fireball"
luigi.subactions[0x129].friendly_name = "Green Missile"
luigi.subactions[0x12A].friendly_name = "Green Missile"
luigi.subactions[0x12B].friendly_name = "Green Missile"
luigi.subactions[0x12C].friendly_name = "Green Missile"
luigi.subactions[0x12D].friendly_name = "Green Missile"
luigi.subactions[0x12E].friendly_name = "Green Missile"
luigi.subactions[0x12F].friendly_name = "Green Missile"
luigi.subactions[0x130].friendly_name = "Green Missile"
luigi.subactions[0x131].friendly_name = "Green Missile"
luigi.subactions[0x132].friendly_name = "Green Missile"
luigi.subactions[0x133].friendly_name = "Green Missile"
luigi.subactions[0x134].friendly_name = "Super Jump Punch"
luigi.subactions[0x135].friendly_name = "Super Jump Punch"
luigi.subactions[0x136].friendly_name = "Cyclone"
luigi.subactions[0x137].friendly_name = "Cyclone"

for action in luigi.subactions:
    if "Nameless" not in action.friendly_name:
        action.tags.append(action.friendly_name.lower().replace(" ", ""))

file_data = luigi.dat_file.file_data
offset = luigi.projectile_offsets[0]
fireball_hitbox = hitbox.Hitbox(file_data[offset:offset+20], offset)
fireball_hitbox.tags.append("projectile")
luigi.projectile_hitboxes.append(fireball_hitbox)

attribute_data = luigi.dat_file.get_special_attribute_data(luigi.special_attribute_block_size)
luigi.add_attribute(attribute_data, 0x8, "Green Missile Charge Rate", 1)
luigi.add_attribute(attribute_data, 0xC, "Green Missile Frames to Fully Charge", 1)
luigi.add_attribute(attribute_data, 0x10, "Green Missile Tilt Damage", 1)
luigi.add_attribute(attribute_data, 0x18, "Green Missile Traction Multiplier", 1)
luigi.add_attribute(attribute_data, 0x24, "Green Missile Horizontal Momentum", 1)
luigi.add_attribute(attribute_data, 0x28, "Green Missile Horizontal Momentum Multiplier", 1)
luigi.add_attribute(attribute_data, 0x2C, "Green Missile Vertical Momentum", 1)
luigi.add_attribute(attribute_data, 0x30, "Green Missile Vertical Momentum Multiplier", 1)
luigi.add_attribute(attribute_data, 0x34, "Green Missile Gravity on Launch", 1)
luigi.add_attribute(attribute_data, 0x38, "Green Missile Ending Friction Modifier", 1)
luigi.add_attribute(attribute_data, 0x3C, "Green Missile Launch End Horizontal Deceleration", 1)
luigi.add_attribute(attribute_data, 0x40, "Green Missile Launch End Gravity Multiplier", 1)
luigi.add_attribute(attribute_data, 0x44, "Green Missile Misfire Chance", 1)
luigi.add_attribute(attribute_data, 0x48, "Green Missile Misfire Horizontal Momentum", 1)
luigi.add_attribute(attribute_data, 0x4C, "Green Missile Misfire Vertical Momentum", 1)
luigi.add_attribute(attribute_data, 0x50, "Luigi Jump Punch Freefall Mobility", 1)
luigi.add_attribute(attribute_data, 0x54, "Luigi Jump Punch Landing Lag", 1)
luigi.add_attribute(attribute_data, 0x60, "Luigi Jump Punch Air Control During Up B", 1)
luigi.add_attribute(attribute_data, 0x64, "Luigi Jump Punch Air Control Input Modifier", 1)
luigi.add_attribute(attribute_data, 0x68, "Luigi Jump Punch Gravity", 1)
luigi.add_attribute(attribute_data, 0x6C, "Luigi Jump Punch Air Vertical Momentum", 1)
luigi.add_attribute(attribute_data, 0x70, "Cyclone Momentum From Initial B Tap", 1)
luigi.add_attribute(attribute_data, 0x74, "Cyclone Grounded Horizontal Momentum", 1)
luigi.add_attribute(attribute_data, 0x78, "Cyclone Aerial Horizontal Momentum", 1)
luigi.add_attribute(attribute_data, 0x7C, "Cyclone Grounded Momentum Modifier", 1)
luigi.add_attribute(attribute_data, 0x80, "Cyclone Aerial Momentum Modifier", 1)
luigi.add_attribute(attribute_data, 0x84, "Cyclone Ending Friction", 1)
luigi.add_attribute(attribute_data, 0x8C, "Cyclone Max Vertical Momentum From B Tap", 1)
luigi.add_attribute(attribute_data, 0x90, "Cyclone Gravity Modifier During B Tap", 1)

luigi.article_datas = luigi.dat_file.get_article_data(luigi)
fireball_data = luigi.article_datas[0]
luigi.add_attribute(fireball_data, 0xC, "Green Fireball Spin Animation Speed", 2)
luigi.add_attribute(fireball_data, 0x10, "Green Fireball Gravity", 2)
luigi.add_attribute(fireball_data, 0x14, "Green Fireball Terminal Velocity", 2)

fireball_b_data = luigi.article_datas[1]
luigi.add_attribute(fireball_b_data, 0x0, "Green Fireball Initial Velocity", 3)
luigi.add_attribute(fireball_b_data, 0x4, "Green Fireball Duration", 3)
luigi.add_attribute(fireball_b_data, 0xC, "Green Fireball Bounce Multiplier", 3)