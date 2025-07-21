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

luigi.subactions[239].friendly_name = "Appeal"
luigi.subactions[299].friendly_name = "Green Missile (Uncharged)"
luigi.subactions[300].friendly_name = "Green Missile (Charged, Misfire)"
luigi.subactions[308].friendly_name = "Super Jump Punch (Ground)"
luigi.subactions[309].friendly_name = "Super Jump Punch (Air)"
luigi.subactions[310].friendly_name = "Cyclone"
luigi.subactions[311].friendly_name = "Cyclone"

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
luigi.add_attribute(attribute_data, 0x50, "Super Jump Punch Freefall Mobility", 1)
luigi.add_attribute(attribute_data, 0x54, "Super Jump Punch Landing Lag", 1)
luigi.add_attribute(attribute_data, 0x60, "Super Jump Punch Air Control During Up B", 1)
luigi.add_attribute(attribute_data, 0x64, "Super Jump Punch Air Control Input Modifier", 1)
luigi.add_attribute(attribute_data, 0x68, "Super Jump Punch Gravity", 1)
luigi.add_attribute(attribute_data, 0x6C, "Super Jump Punch Air Vertical Momentum", 1)
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
luigi.add_attribute(fireball_data, 0xC, "Fireball Spin Animation Speed", 2)
luigi.add_attribute(fireball_data, 0x10, "Fireball Gravity", 2)
luigi.add_attribute(fireball_data, 0x14, "Fireball Terminal Velocity", 2)

fireball_b_data = luigi.article_datas[1]
luigi.add_attribute(fireball_b_data, 0x0, "Fireball Initial Velocity", 3)
luigi.add_attribute(fireball_b_data, 0x4, "Fireball Duration", 3)
luigi.add_attribute(fireball_b_data, 0xC, "Fireball Bounce Multiplier", 3)