import fighter
from iso import DAT
from structs import hitbox

mewtwo = fighter.Fighter("Mewtwo", DAT(b'PlMt.dat'))
fighter.fighters.append(mewtwo)
mewtwo.fighter_id = 0x0A

mewtwo.special_attribute_block_size = 0x88
mewtwo.articles_sizes = [0x8, 0x30]
mewtwo.articles_offsets = [0x3390, 0x3CD8]
mewtwo.projectile_offsets = [0x3DD4, 0x3E0C, 0x3E44, 0x3E98, 0x3D00]

file_data = mewtwo.dat_file.file_data
offset = mewtwo.projectile_offsets[0]
shadowball_a_hitbox = hitbox.Hitbox(file_data[offset:offset+20], offset)
shadowball_a_hitbox.tags.append("projectile")
mewtwo.projectile_hitboxes.append(shadowball_a_hitbox)

offset = mewtwo.projectile_offsets[1]
shadowball_b_hitbox = hitbox.Hitbox(file_data[offset:offset+20], offset)
shadowball_b_hitbox.tags.append("projectile")
mewtwo.projectile_hitboxes.append(shadowball_b_hitbox)

offset = mewtwo.projectile_offsets[2]
shadowball_c_hitbox = hitbox.Hitbox(file_data[offset:offset+20], offset)
shadowball_c_hitbox.tags.append("projectile")
mewtwo.projectile_hitboxes.append(shadowball_c_hitbox)

offset = mewtwo.projectile_offsets[3]
shadowball_d_hitbox = hitbox.Hitbox(file_data[offset:offset+20], offset)
shadowball_d_hitbox.tags.append("projectile")
mewtwo.projectile_hitboxes.append(shadowball_d_hitbox)

offset = mewtwo.projectile_offsets[4]
disable_hitbox = hitbox.Hitbox(file_data[offset:offset+20], offset)
disable_hitbox.tags.append("projectile")
mewtwo.projectile_hitboxes.append(disable_hitbox)

mewtwo.subactions[296].friendly_name = "Shadow Ball"
mewtwo.subactions[297].friendly_name = "Shadow Ball"

attribute_data = mewtwo.dat_file.get_special_attribute_data(mewtwo.special_attribute_block_size)
mewtwo.add_attribute(attribute_data, 0x0, "Shadow Ball Charge Increment", 1)
mewtwo.add_attribute(attribute_data, 0x4, "Shadow Ball Release Momentum Grounded", 1)
mewtwo.add_attribute(attribute_data, 0x8, "Shadow Ball Release Momentum Air", 1)
mewtwo.add_attribute(attribute_data, 0xC, "Shadow Ball Loops For Full Charge", 1)
mewtwo.get_attribute("Shadow Ball Loops For Full Charge").integer = True
mewtwo.add_attribute(attribute_data, 0x14, "Shadow Ball Landing Lag", 1)
mewtwo.add_attribute(attribute_data, 0x18, "Confusion Aerial Vertical Lift", 1)
mewtwo.add_attribute(attribute_data, 0x20, "Confusion Max Damage Reflectable", 1)
mewtwo.add_attribute(attribute_data, 0x30, "Confusion Reflection Bubble Size", 1)
mewtwo.add_attribute(attribute_data, 0x34, "Confusion Reflection Damage Multiplier", 1)
mewtwo.add_attribute(attribute_data, 0x38, "Confusion Reflection Speed Multiplier", 1)
mewtwo.add_attribute(attribute_data, 0x50, "Teleport Travel Time", 1)
mewtwo.get_attribute("Teleport Travel Time").integer = True
mewtwo.add_attribute(attribute_data, 0x5C, "Teleport Initial Momentum 1", 1)
mewtwo.add_attribute(attribute_data, 0x60, "Teleport Initial Momentum 2", 1)
mewtwo.add_attribute(attribute_data, 0x64, "Teleport Ending Momentum", 1)
mewtwo.add_attribute(attribute_data, 0x6C, "Teleport Ending Momentum Multiplier", 1)
mewtwo.add_attribute(attribute_data, 0x74, "Teleport Landing Lag", 1)
mewtwo.add_attribute(attribute_data, 0x78, "Disable Base Falling Acceleration", 1)
mewtwo.add_attribute(attribute_data, 0x7C, "Disable Falling Acceleration Multiplier", 1)
mewtwo.add_attribute(attribute_data, 0x80, "Disable X-Offset", 1)
mewtwo.add_attribute(attribute_data, 0x84, "Disable Y-Offset", 1)

mewtwo.article_datas = mewtwo.dat_file.get_article_data(mewtwo)
disable_data = mewtwo.article_datas[0]
mewtwo.add_attribute(disable_data, 0x0, "Disable Duration", 2)
mewtwo.add_attribute(disable_data, 0x4, "Disable Travel Speed", 2)

shadowball_data = mewtwo.article_datas[1]
mewtwo.add_attribute(shadowball_data, 0x0, "Shadow Ball Duration", 3)
mewtwo.add_attribute(shadowball_data, 0x4, "Shadow Ball Launch Angle", 3)
mewtwo.add_attribute(shadowball_data, 0x8, "Shadow Ball Uncharged Speed", 3)
mewtwo.add_attribute(shadowball_data, 0xC, "Shadow Ball Charged Speed", 3)
mewtwo.add_attribute(shadowball_data, 0x10, "Shadow Ball Uncharged Damage", 3)
mewtwo.add_attribute(shadowball_data, 0x14, "Shadow Ball Full Charge Damage", 3)
mewtwo.add_attribute(shadowball_data, 0x18, "Shadow Ball Uncharged Size", 3)
mewtwo.add_attribute(shadowball_data, 0x1C, "Shadow Ball Full Charge Size", 3)
mewtwo.add_attribute(shadowball_data, 0x20, "Shadow Ball Wiggle Intensity", 3)
mewtwo.get_attribute("Shadow Ball Wiggle Intensity").integer = True
mewtwo.add_attribute(shadowball_data, 0x28, "Shadow Ball Wiggle Modifier", 3)
mewtwo.add_attribute(shadowball_data, 0x2C, "Shadow Ball Wiggle Smoothness", 3)