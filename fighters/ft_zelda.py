import fighter
from iso import DAT
from structs import hitbox

zelda = fighter.Fighter("Zelda", DAT(b'PlZd.dat'))
fighter.fighters.append(zelda)
zelda.fighter_id = 0x12

zelda.special_attribute_block_size = 0xA8
zelda.articles_sizes = [0x30, 0x14]
zelda.articles_offsets = [0x3EC8, 0x3FA0]
zelda.projectile_offsets = [0x3FE4]

zelda.good_sfx = [0x41f72, 0x41f5a, 0x41f57, 0x41f51, 0x41f54, 0x41ed0, 0x41edc, 0x41f5d, 0x41edf, 0x41f75, 0x41f6f, 0x41f69, 0x41ec4, 0x41ec7, 0x41f63, 0x41ec1, 0x41f4e]

file_data = zelda.dat_file.file_data
offset = zelda.projectile_offsets[0]
dins_hitbox = hitbox.Hitbox(file_data[offset:offset+20], offset)
dins_hitbox.tags.append("projectile")
zelda.projectile_hitboxes.append(dins_hitbox)

zelda.subactions[0x127].friendly_name = "Nayrus Love"
zelda.subactions[0x128].friendly_name = "Nayrus Love"
zelda.subactions[0x129].friendly_name = "Dins Fire"
zelda.subactions[0x12A].friendly_name = "Dins Fire"
zelda.subactions[0x12B].friendly_name = "Dins Fire"
zelda.subactions[0x12C].friendly_name = "Dins Fire"
zelda.subactions[0x12D].friendly_name = "Dins Fire"
zelda.subactions[0x12E].friendly_name = "Dins Fire"
zelda.subactions[0x12F].friendly_name = "Farores Wind"
zelda.subactions[0x130].friendly_name = "Farores Wind"
zelda.subactions[0x131].friendly_name = "Farores Wind"
zelda.subactions[0x132].friendly_name = "Farores Wind"
zelda.subactions[0x133].friendly_name = "Transform"
zelda.subactions[0x134].friendly_name = "Transform"
zelda.subactions[0x135].friendly_name = "Transform"
zelda.subactions[0x136].friendly_name = "Transform"

for action in zelda.subactions:
    if "Nameless" not in action.friendly_name:
        action.tags.append(action.friendly_name.lower().replace(" ", ""))

attribute_data = zelda.dat_file.get_special_attribute_data(zelda.special_attribute_block_size)
zelda.add_attribute(attribute_data, 0x4, "Nayrus Love Gravity Delay", 1)
zelda.get_attribute("Nayrus Love Gravity Delay").integer = True
zelda.add_attribute(attribute_data, 0x8, "Nayrus Love Momentum Preservation", 1)
zelda.add_attribute(attribute_data, 0xC, "Nayrus Love Fall Acceleration", 1)
zelda.add_attribute(attribute_data, 0x88, "Nayrus Love Max Damage Reflectable", 1)
zelda.get_attribute("Nayrus Love Max Damage Reflectable").integer = True
zelda.add_attribute(attribute_data, 0x94, "Nayrus Love Reflection Bubble Size", 1)
zelda.add_attribute(attribute_data, 0x9C, "Nayrus Love Reflection Damage Multiplier", 1)
zelda.add_attribute(attribute_data, 0xA0, "Nayrus Love Reflection Speed Multiplier", 1)
zelda.add_attribute(attribute_data, 0x14, "Dins Fire Max Hold Time", 1)
zelda.get_attribute("Dins Fire Max Hold Time").integer = True
zelda.add_attribute(attribute_data, 0x18, "Dins Fire Gravity Delay", 1)
zelda.get_attribute("Dins Fire Gravity Delay").integer = True
zelda.add_attribute(attribute_data, 0x1C, "Dins Fire Frames for Auto Charge", 1)
zelda.get_attribute("Dins Fire Frames for Auto Charge").integer = True
zelda.add_attribute(attribute_data, 0x20, "Dins Fire X-Offset", 1)
zelda.add_attribute(attribute_data, 0x24, "Dins Fire Y-Offset", 1)
zelda.add_attribute(attribute_data, 0x2C, "Dins Fire Fall Acceleration", 1)
zelda.add_attribute(attribute_data, 0x34, "Dins Fire Landing Lag", 1)
zelda.add_attribute(attribute_data, 0x38, "Farores Wind Horizontal Momentum Preservation", 1)
zelda.add_attribute(attribute_data, 0x3C, "Farores Wind Vertical Momentum Preservation", 1)
zelda.add_attribute(attribute_data, 0x40, "Farores Wind Fall Acceleration", 1)
zelda.add_attribute(attribute_data, 0x48, "Farores Wind Travel Distance", 1)
zelda.get_attribute("Farores Wind Travel Distance").integer = True
zelda.add_attribute(attribute_data, 0x54, "Farores Wind Base Momentum", 1)
zelda.add_attribute(attribute_data, 0x58, "Farores Wind Momentum Variable", 1)
zelda.add_attribute(attribute_data, 0x5C, "Farores Wind Momentum After Warp", 1)
zelda.add_attribute(attribute_data, 0x64, "Farores Wind Momentum After Warp 2", 1)
zelda.add_attribute(attribute_data, 0x6C, "Farores Wind Momentum Landing Lag", 1)
zelda.add_attribute(attribute_data, 0x70, "Farores Wind Horizontal Momentum Modifier", 1)
zelda.add_attribute(attribute_data, 0x74, "Farores Wind Vertical Momentum Modifier", 1)

zelda.article_datas = zelda.dat_file.get_article_data(zelda)
dins_data_a = zelda.article_datas[0]
zelda.add_attribute(dins_data_a, 0x00, "Dins Fire Charge Maximum Duration", 2)
zelda.add_attribute(dins_data_a, 0x04, "Dins Fire Charge Damage Growth Window", 2)
zelda.add_attribute(dins_data_a, 0x10, "Dins Fire Charge Launch Angle", 2)
zelda.add_attribute(dins_data_a, 0x14, "Dins Fire Charge Initial Velocity", 2)
zelda.add_attribute(dins_data_a, 0x18, "Dins Fire Charge Acceleration", 2)
zelda.add_attribute(dins_data_a, 0x1C, "Dins Fire Charge Max Velocity", 2)
zelda.add_attribute(dins_data_a, 0x24, "Dins Fire Charge Vertical Meneuverability", 2)
zelda.add_attribute(dins_data_a, 0x28, "Dins Fire Charge Maximum Curve Angle", 2)
zelda.add_attribute(dins_data_a, 0x2C, "Dins Fire Charge Detonation Delay", 2)

dins_data_b = zelda.article_datas[1]
zelda.add_attribute(dins_data_b, 0x00, "Dins Fire Explosion Hitbox Size", 3)
zelda.add_attribute(dins_data_b, 0x04, "Dins Fire Explosion Initial Graphic Size", 3)
zelda.add_attribute(dins_data_b, 0x08, "Dins Fire Explosion Graphic Growth Multiplier", 3)
zelda.add_attribute(dins_data_b, 0x0C, "Dins Fire Explosion Base Damage", 3)
zelda.add_attribute(dins_data_b, 0x10, "Dins Fire Explosion Damage Multiplier", 3)