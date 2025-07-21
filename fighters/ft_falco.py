import fighter
from iso import DAT
from structs import hitbox

falco = fighter.Fighter("Falco", DAT(b'PlFc.dat'))
fighter.fighters.append(falco)
falco.fighter_id = 0x14

falco.special_attribute_block_size = 0xD4
falco.articles_sizes = [0x28, 0x8]
falco.articles_offsets = [0x3F50, 0x4140]
falco.projectile_offsets = [0x3F98, 0x4168, 0x4184]

file_data = falco.dat_file.file_data

offset = falco.projectile_offsets[0]
laser_hitbox = hitbox.Hitbox(file_data[offset:offset+20], offset)
laser_hitbox.tags.append("projectile")

offset = falco.projectile_offsets[1]
phantasm_g_hitbox = hitbox.Hitbox(file_data[offset:offset+20], offset)
phantasm_g_hitbox.tags.append("projectile")

offset = falco.projectile_offsets[2]
phantasm_a_hitbox = hitbox.Hitbox(file_data[offset:offset+20], offset)
phantasm_a_hitbox.tags.append("projectile")

falco.projectile_hitboxes.append(laser_hitbox)
falco.projectile_hitboxes.append(phantasm_g_hitbox)
falco.projectile_hitboxes.append(phantasm_a_hitbox)

falco.subactions[308].friendly_name = "Fire Bird"
falco.subactions[309].friendly_name = "Fire Bird"
falco.subactions[313].friendly_name = "Reflector"

attribute_data = falco.dat_file.get_special_attribute_data(falco.special_attribute_block_size)

falco.add_attribute(attribute_data, 0x10, "Blaster Launch Angle", 1)
falco.add_attribute(attribute_data, 0x14, "Blaster Launch Speed", 1)
falco.add_attribute(attribute_data, 0x18, "Blaster Landing Lag", 1)
falco.add_attribute(attribute_data, 0x24, "Phantasm Gravity Frame Delay", 1)
falco.add_attribute(attribute_data, 0x28, "Phantasm Initial Horizontal Momentum", 1)
falco.add_attribute(attribute_data, 0x38, "Phantasm Ground Friction", 1)
falco.add_attribute(attribute_data, 0x3C, "Phantasm Air Dash Speed", 1)
falco.add_attribute(attribute_data, 0x40, "Phantasm Air Dash Momentum", 1)
falco.add_attribute(attribute_data, 0x44, "Phantasm Air Dash Vertical Deceleration", 1)
falco.add_attribute(attribute_data, 0x48, "Phantasm Ending Gravity", 1)
falco.add_attribute(attribute_data, 0x50, "Phantasm Landing Lag", 1)
falco.add_attribute(attribute_data, 0x54, "Fire Bird Gravity Frame Delay", 1)
falco.add_attribute(attribute_data, 0x58, "Fire Bird Startup Horizontal Momentum", 1)
falco.add_attribute(attribute_data, 0x5C, "Fire Bird Startup Aerial Momentum Preservation", 1)
falco.add_attribute(attribute_data, 0x60, "Fire Bird Fall Acceleration", 1)
falco.add_attribute(attribute_data, 0x68, "Fire Bird Frames of Travel", 1)
falco.add_attribute(attribute_data, 0x70, "Fire Bird Aerial Ending Momentum", 1)
falco.add_attribute(attribute_data, 0x74, "Fire Bird Travel Speed", 1)
falco.add_attribute(attribute_data, 0x78, "Fire Bird Reverse Acceleration", 1)
falco.add_attribute(attribute_data, 0x7C, "Fire Bird Grounded Ending Momentum", 1)
falco.add_attribute(attribute_data, 0x84, "Fire Bird Bounce Horizontal Velocity", 1)
falco.add_attribute(attribute_data, 0x90, "Fire Bird Landing Lag", 1)
falco.add_attribute(attribute_data, 0x94, "Fire Bird Landing Lag After Bounce", 1)
falco.add_attribute(attribute_data, 0x98, "Reflector Release Frames", 1)
falco.add_attribute(attribute_data, 0x9C, "Reflector Turn Animation Frames", 1)
falco.add_attribute(attribute_data, 0xA4, "Reflector Gravity Frame Delay", 1)
falco.add_attribute(attribute_data, 0xA8, "Reflector Momentum Preservation", 1)
falco.add_attribute(attribute_data, 0xAC, "Reflector Fall Acceleration", 1)
falco.add_attribute(attribute_data, 0xB0, "Reflector Max Damage Reflectable", 1)
falco.get_attribute("Reflector Max Damage Reflectable").integer = True
falco.add_attribute(attribute_data, 0xC8, "Reflector Reflection Damage Multiplier", 1)
falco.add_attribute(attribute_data, 0xCC, "Reflector Reflection Speed Multiplier", 1)

falco.article_datas = falco.dat_file.get_article_data(falco)
laser_data = falco.article_datas[0]
falco.add_attribute(laser_data, 0x0, "Laser Duration", 2)
falco.add_attribute(laser_data, 0x4, "Laser Max Horizontal Stretch", 2)

phantasm_data = falco.article_datas[1]
falco.add_attribute(phantasm_data, 0x0, "Phantasm Duration of After Image", 3)