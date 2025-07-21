import fighter
from iso import DAT
from structs import hitbox

fox = fighter.Fighter("Fox", DAT(b'PlFx.dat'))
fighter.fighters.append(fox)
fox.fighter_id = 0x02

fox.special_attribute_block_size = 0xD4
fox.articles_sizes = [0x28, 0x8]
fox.articles_offsets = [0x3E94, 0x409C]
fox.projectile_offsets = [0x3EDC, 0x40C4, 0x40E0]

file_data = fox.dat_file.file_data

offset = fox.projectile_offsets[0]
laser_hitbox = hitbox.Hitbox(file_data[offset:offset+20], offset)
laser_hitbox.tags.append("projectile")

offset = fox.projectile_offsets[1]
Illusion_g_hitbox = hitbox.Hitbox(file_data[offset:offset+20], offset)
Illusion_g_hitbox.tags.append("projectile")

offset = fox.projectile_offsets[2]
Illusion_a_hitbox = hitbox.Hitbox(file_data[offset:offset+20], offset)
Illusion_a_hitbox.tags.append("projectile")

fox.projectile_hitboxes.append(laser_hitbox)
fox.projectile_hitboxes.append(Illusion_g_hitbox)
fox.projectile_hitboxes.append(Illusion_a_hitbox)

fox.subactions[307].friendly_name = "Fire Fox"
fox.subactions[308].friendly_name = "Fire Fox"
fox.subactions[309].friendly_name = "Fire Fox"
fox.subactions[313].friendly_name = "Reflector"

attribute_data = fox.dat_file.get_special_attribute_data(fox.special_attribute_block_size)

fox.add_attribute(attribute_data, 0x10, "Blaster Launch Angle", 1)
fox.add_attribute(attribute_data, 0x14, "Blaster Launch Speed", 1)
fox.add_attribute(attribute_data, 0x18, "Blaster Landing Lag", 1)
fox.add_attribute(attribute_data, 0x24, "Illusion Gravity Frame Delay", 1)
fox.add_attribute(attribute_data, 0x28, "Illusion Initial Horizontal Momentum", 1)
fox.add_attribute(attribute_data, 0x38, "Illusion Ground Friction", 1)
fox.add_attribute(attribute_data, 0x3C, "Illusion Air Dash Speed", 1)
fox.add_attribute(attribute_data, 0x40, "Illusion Air Dash Momentum", 1)
fox.add_attribute(attribute_data, 0x44, "Illusion Air Dash Vertical Deceleration", 1)
fox.add_attribute(attribute_data, 0x48, "Illusion Ending Gravity", 1)
fox.add_attribute(attribute_data, 0x50, "Illusion Landing Lag", 1)
fox.add_attribute(attribute_data, 0x54, "Fire Fox Gravity Frame Delay", 1)
fox.add_attribute(attribute_data, 0x58, "Fire Fox Startup Horizontal Momentum", 1)
fox.add_attribute(attribute_data, 0x5C, "Fire Fox Startup Aerial Momentum Preservation", 1)
fox.add_attribute(attribute_data, 0x60, "Fire Fox Fall Acceleration", 1)
fox.add_attribute(attribute_data, 0x68, "Fire Fox Frames of Travel", 1)
fox.add_attribute(attribute_data, 0x70, "Fire Fox Aerial Ending Momentum", 1)
fox.add_attribute(attribute_data, 0x74, "Fire Fox Travel Speed", 1)
fox.add_attribute(attribute_data, 0x78, "Fire Fox Reverse Acceleration", 1)
fox.add_attribute(attribute_data, 0x7C, "Fire Fox Grounded Ending Momentum", 1)
fox.add_attribute(attribute_data, 0x84, "Fire Fox Bounce Horizontal Velocity", 1)
fox.add_attribute(attribute_data, 0x90, "Fire Fox Landing Lag", 1)
fox.add_attribute(attribute_data, 0x94, "Fire Fox Landing Lag After Bounce", 1)
fox.add_attribute(attribute_data, 0x98, "Reflector Release Frames", 1)
fox.add_attribute(attribute_data, 0x9C, "Reflector Turn Animation Frames", 1)
fox.add_attribute(attribute_data, 0xA4, "Reflector Gravity Frame Delay", 1)
fox.add_attribute(attribute_data, 0xA8, "Reflector Momentum Preservation", 1)
fox.add_attribute(attribute_data, 0xAC, "Reflector Fall Acceleration", 1)
fox.add_attribute(attribute_data, 0xB0, "Reflector Max Damage Reflectable", 1)
fox.get_attribute("Reflector Max Damage Reflectable").integer = True
fox.add_attribute(attribute_data, 0xC8, "Reflector Reflection Damage Multiplier", 1)
fox.add_attribute(attribute_data, 0xCC, "Reflector Reflection Speed Multiplier", 1)

fox.article_datas = fox.dat_file.get_article_data(fox)
laser_data = fox.article_datas[0]
fox.add_attribute(laser_data, 0x0, "Laser Duration", 2)
fox.add_attribute(laser_data, 0x4, "Laser Max Horizontal Stretch", 2)

illusion_data = fox.article_datas[1]
fox.add_attribute(illusion_data, 0x0, "Illusion Duration of After Image", 3)