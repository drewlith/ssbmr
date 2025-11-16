import fighter
from iso import DAT
from structs import hitbox


peach = fighter.Fighter("Peach", DAT(b'PlPe.dat'))
fighter.fighters.append(peach)
peach.fighter_id = 0x0C

peach.special_attribute_block_size = 0xC0
peach.articles_sizes = [0x48, 0x10]
peach.articles_offsets = [0x40E8, 0x42E0]
peach.projectile_offsets = [0x4310]

peach.good_sfx = [0x35ba0, 0x35b7c, 0x35b88, 0x35b61, 0x35ba6, 0x35b76, 0x35bac, 0x35ba3, 0x35b9d]

file_data = peach.dat_file.file_data
offset = peach.projectile_offsets[0]
turnip_hitbox = hitbox.Hitbox(file_data[offset:offset+20], offset)
turnip_hitbox.tags.append("projectile")
peach.projectile_hitboxes.append(turnip_hitbox)

peach.subactions[0x12A].friendly_name = "Tennis Racket"
peach.subactions[0x12B].friendly_name = "Golf Club"
peach.subactions[0x12C].friendly_name = "Frying Pan"
peach.subactions[0x12D].friendly_name = "Toad"
peach.subactions[0x12E].friendly_name = "Peach Bomber"
peach.subactions[0x12F].friendly_name = "Peach Bomber"
peach.subactions[0x130].friendly_name = "Peach Bomber"
peach.subactions[0x131].friendly_name = "Peach Bomber"
peach.subactions[0x132].friendly_name = "Peach Bomber"
peach.subactions[0x133].friendly_name = "Peach Bomber"
peach.subactions[0x134].friendly_name = "Parasol"
peach.subactions[0x135].friendly_name = "Parasol"
peach.subactions[0x136].friendly_name = "Parasol"
peach.subactions[0x137].friendly_name = "Parasol"
peach.subactions[0x13C].friendly_name = "Parasol"
peach.subactions[0x13D].friendly_name = "Parasol"
peach.subactions[0x138].friendly_name = "Vegetable"
peach.subactions[0x139].friendly_name = "Vegetable"
peach.subactions[0x13A].friendly_name = "Vegetable"
peach.subactions[0x13B].friendly_name = "Vegetable"

for action in peach.subactions:
    if "Nameless" not in action.friendly_name:
        action.tags.append(action.friendly_name.lower().replace(" ", ""))

attribute_data = peach.dat_file.get_special_attribute_data(peach.special_attribute_block_size)
peach.add_attribute(attribute_data, 0xC, "Float Duration", 1)
peach.add_attribute(attribute_data, 0x14, "Vegetable Base Odds", 1)
peach.get_attribute("Vegetable Base Odds").integer = True
peach.add_attribute(attribute_data, 0x18, "Vegetable Item 1 Odds", 1)
peach.get_attribute("Vegetable Item 1 Odds").integer = True
peach.add_attribute(attribute_data, 0x1C, "Vegetable Item 1 ID", 1)
peach.get_attribute("Vegetable Item 1 ID").integer = True
peach.add_attribute(attribute_data, 0x20, "Vegetable Item 2 Odds", 1)
peach.get_attribute("Vegetable Item 2 Odds").integer = True
peach.add_attribute(attribute_data, 0x24, "Vegetable Item 2 ID", 1)
peach.get_attribute("Vegetable Item 2 ID").integer = True
peach.add_attribute(attribute_data, 0x28, "Vegetable Item 3 Odds", 1)
peach.get_attribute("Vegetable Item 3 Odds").integer = True
peach.add_attribute(attribute_data, 0x2C, "Vegetable Item 3 ID", 1)
peach.get_attribute("Vegetable Item 3 ID").integer = True
peach.add_attribute(attribute_data, 0x44, "Peach Bomber Tilt Horizontal Momentum", 1)
peach.add_attribute(attribute_data, 0x48, "Peach Bomber Smash Horizontal Momentum", 1)
peach.add_attribute(attribute_data, 0x4C, "Peach Bomber Vertical Momentum", 1)
peach.add_attribute(attribute_data, 0x64, "Peach Bomber Vertical Recoil", 1)
peach.add_attribute(attribute_data, 0x74, "Parasol Landing Lag", 1)
peach.add_attribute(attribute_data, 0x80, "Parasol Launch Control Modifier", 1)
peach.add_attribute(attribute_data, 0x9C, "Toad Aerial Vertical Momentum", 1)
peach.add_attribute(attribute_data, 0xA0, "Toad Fall Acceleration", 1)
peach.add_attribute(attribute_data, 0xBC, "Toad Detection Bubble Size", 1)

peach.article_datas = peach.dat_file.get_article_data(peach)
turnip_data = peach.article_datas[0]
peach.add_attribute(turnip_data, 0x8, "Turnip #1 Odds", 2)
peach.get_attribute("Turnip #1 Odds").integer = True
peach.add_attribute(turnip_data, 0xC, "Turnip #1 Damage", 2)
peach.get_attribute("Turnip #1 Damage").integer = True
peach.add_attribute(turnip_data, 0x10, "Turnip #2 Odds", 2)
peach.get_attribute("Turnip #2 Odds").integer = True
peach.add_attribute(turnip_data, 0x14, "Turnip #2 Damage", 2)
peach.get_attribute("Turnip #2 Damage").integer = True
peach.add_attribute(turnip_data, 0x18, "Turnip #3 Odds", 2)
peach.get_attribute("Turnip #3 Odds").integer = True
peach.add_attribute(turnip_data, 0x1C, "Turnip #3 Damage", 2)
peach.get_attribute("Turnip #3 Damage").integer = True
peach.add_attribute(turnip_data, 0x20, "Turnip #4 Odds", 2)
peach.get_attribute("Turnip #4 Odds").integer = True
peach.add_attribute(turnip_data, 0x24, "Turnip #4 Damage", 2)
peach.get_attribute("Turnip #4 Damage").integer = True
peach.add_attribute(turnip_data, 0x28, "Turnip #5 Odds", 2)
peach.get_attribute("Turnip #5 Odds").integer = True
peach.add_attribute(turnip_data, 0x2C, "Turnip #5 Damage", 2)
peach.get_attribute("Turnip #5 Damage").integer = True
peach.add_attribute(turnip_data, 0x30, "Turnip #6 Odds", 2)
peach.get_attribute("Turnip #6 Odds").integer = True
peach.add_attribute(turnip_data, 0x34, "Turnip #6 Damage", 2)
peach.get_attribute("Turnip #6 Damage").integer = True
peach.add_attribute(turnip_data, 0x38, "Turnip #7 Odds", 2)
peach.get_attribute("Turnip #7 Odds").integer = True
peach.add_attribute(turnip_data, 0x3C, "Turnip #7 Damage", 2)
peach.get_attribute("Turnip #7 Damage").integer = True
peach.add_attribute(turnip_data, 0x40, "Turnip #8 Odds", 2)
peach.get_attribute("Turnip #8 Odds").integer = True
peach.add_attribute(turnip_data, 0x44, "Turnip #8 Damage", 2)
peach.get_attribute("Turnip #8 Damage").integer = True

toad_data = peach.article_datas[1]
peach.add_attribute(toad_data, 0x0, "Toad Counter Velocity", 3)
peach.add_attribute(toad_data, 0x4, "Toad Counter Distance Modifier", 3)
peach.add_attribute(toad_data, 0x8, "Toad Counter Scatter Modifier", 3)
peach.add_attribute(toad_data, 0xC, "Toad Counter Angle", 3)