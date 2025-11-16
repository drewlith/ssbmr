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

fox.good_sfx = [0x1adf3, 0x1addb, 0x1adf0, 0x1ade4, 0x1ae0b, 0x1ae08, 0x1adff, 0x1ae0e, 0x1ae11]

file_data = fox.dat_file.file_data

offset = fox.projectile_offsets[0]
laser_hitbox = hitbox.Hitbox(file_data[offset:offset+20], offset)
laser_hitbox.tags.append("projectile")

offset = fox.projectile_offsets[1]
illusion_g_hitbox = hitbox.Hitbox(file_data[offset:offset+20], offset)
illusion_g_hitbox.tags.append("projectile")

offset = fox.projectile_offsets[2]
illusion_a_hitbox = hitbox.Hitbox(file_data[offset:offset+20], offset)
illusion_a_hitbox.tags.append("projectile")

fox.projectile_hitboxes.append(laser_hitbox)
fox.projectile_hitboxes.append(illusion_g_hitbox)
fox.projectile_hitboxes.append(illusion_a_hitbox)

fox.subactions[0x127].friendly_name = "Blaster"
fox.subactions[0x128].friendly_name = "Blaster"
fox.subactions[0x129].friendly_name = "Blaster"
fox.subactions[0x12A].friendly_name = "Blaster"
fox.subactions[0x12B].friendly_name = "Blaster"
fox.subactions[0x12C].friendly_name = "Blaster"
fox.subactions[0x12D].friendly_name = "Illusion"
fox.subactions[0x12E].friendly_name = "Illusion"
fox.subactions[0x12F].friendly_name = "Illusion"
fox.subactions[0x130].friendly_name = "Illusion"
fox.subactions[0x131].friendly_name = "Illusion"
fox.subactions[0x132].friendly_name = "Illusion"
fox.subactions[0x133].friendly_name = "Fire Fox"
fox.subactions[0x134].friendly_name = "Fire Fox"
fox.subactions[0x135].friendly_name = "Fire Fox"
fox.subactions[0x136].friendly_name = "Fire Fox"
fox.subactions[0x137].friendly_name = "Fire Fox"
fox.subactions[0x138].friendly_name = "Fire Fox"
fox.subactions[0x139].friendly_name = "Reflector"
fox.subactions[0x13A].friendly_name = "Reflector"
fox.subactions[0x13B].friendly_name = "Reflector"
fox.subactions[0x13C].friendly_name = "Reflector"
fox.subactions[0x13D].friendly_name = "Reflector"
fox.subactions[0x13E].friendly_name = "Reflector"
fox.subactions[0x13F].friendly_name = "Reflector"
fox.subactions[0x140].friendly_name = "Reflector"
fox.subactions[0x141].friendly_name = "Taunt"
fox.subactions[0x142].friendly_name = "Taunt"
fox.subactions[0x143].friendly_name = "Taunt"
fox.subactions[0x144].friendly_name = "Taunt"
fox.subactions[0x145].friendly_name = "Taunt"
fox.subactions[0x146].friendly_name = "Taunt"

for action in fox.subactions:
    if "Nameless" not in action.friendly_name:
        action.tags.append(action.friendly_name.lower().replace(" ", ""))

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
fox.get_attribute("Reflector Gravity Frame Delay").integer = True
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