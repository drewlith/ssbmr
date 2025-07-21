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

file_data = zelda.dat_file.file_data
offset = zelda.projectile_offsets[0]
dins_hitbox = hitbox.Hitbox(file_data[offset:offset+20], offset)
dins_hitbox.tags.append("projectile")
zelda.projectile_hitboxes.append(dins_hitbox)

zelda.subactions[295].friendly_name = "Nayru's Love"
zelda.subactions[300].friendly_name = "Din's Fire"
zelda.subactions[301].friendly_name = "Din's Fire"
zelda.subactions[302].friendly_name = "Din's Fire"
zelda.subactions[303].friendly_name = "Farore's Wind"
zelda.subactions[304].friendly_name = "Farore's Wind"
zelda.subactions[305].friendly_name = "Farore's Wind"
zelda.subactions[306].friendly_name = "Farore's Wind"

attribute_data = zelda.dat_file.get_special_attribute_data(zelda.special_attribute_block_size)
zelda.add_attribute(attribute_data, 0x4, "Nayru's Love Gravity Delay", 1)
zelda.get_attribute("Nayru's Love Gravity Delay").integer = True
zelda.add_attribute(attribute_data, 0x8, "Nayru's Love Momentum Preservation", 1)
zelda.add_attribute(attribute_data, 0xC, "Nayru's Love Fall Acceleration", 1)
zelda.add_attribute(attribute_data, 0x88, "Nayru's Love Max Damage Reflectable", 1)
zelda.get_attribute("Nayru's Love Max Damage Reflectable").integer = True
zelda.add_attribute(attribute_data, 0x94, "Nayru's Love Reflection Bubble Size", 1)
zelda.add_attribute(attribute_data, 0x9C, "Nayru's Love Reflection Damage Multiplier", 1)
zelda.add_attribute(attribute_data, 0xA0, "Nayru's Love Reflection Speed Multiplier", 1)
zelda.add_attribute(attribute_data, 0x14, "Din's Fire Max Hold Time", 1)
zelda.get_attribute("Din's Fire Max Hold Time").integer = True
zelda.add_attribute(attribute_data, 0x18, "Din's Fire Gravity Delay", 1)
zelda.get_attribute("Din's Fire Gravity Delay").integer = True
zelda.add_attribute(attribute_data, 0x1C, "Din's Fire Frames for Auto Charge", 1)
zelda.get_attribute("Din's Fire Frames for Auto Charge").integer = True
zelda.add_attribute(attribute_data, 0x20, "Din's Fire X-Offset", 1)
zelda.add_attribute(attribute_data, 0x24, "Din's Fire Y-Offset", 1)
zelda.add_attribute(attribute_data, 0x2C, "Din's Fire Fall Acceleration", 1)
zelda.add_attribute(attribute_data, 0x34, "Din's Fire Landing Lag", 1)
zelda.add_attribute(attribute_data, 0x38, "Farore's Wind Horizontal Momentum Preservation", 1)
zelda.add_attribute(attribute_data, 0x3C, "Farore's Wind Vertical Momentum Preservation", 1)
zelda.add_attribute(attribute_data, 0x40, "Farore's Wind Fall Acceleration", 1)
zelda.add_attribute(attribute_data, 0x48, "Farore's Wind Travel Distance", 1)
zelda.get_attribute("Farore's Wind Travel Distance").integer = True
zelda.add_attribute(attribute_data, 0x54, "Farore's Wind Base Momentum", 1)
zelda.add_attribute(attribute_data, 0x58, "Farore's Wind Momentum Variable", 1)
zelda.add_attribute(attribute_data, 0x5C, "Farore's Wind Momentum After Warp", 1)
zelda.add_attribute(attribute_data, 0x64, "Farore's Wind Momentum After Warp 2", 1)
zelda.add_attribute(attribute_data, 0x6C, "Farore's Wind Momentum Landing Lag", 1)
zelda.add_attribute(attribute_data, 0x70, "Farore's Wind Horizontal Momentum Modifier", 1)
zelda.add_attribute(attribute_data, 0x74, "Farore's Wind Vertical Momentum Modifier", 1)

zelda.article_datas = zelda.dat_file.get_article_data(zelda)
dins_data_a = zelda.article_datas[0]
zelda.add_attribute(dins_data_a, 0x00, "Din's Fire Charge Maximum Duration", 2)
zelda.add_attribute(dins_data_a, 0x04, "Din's Fire Charge Damage Growth Window", 2)
zelda.add_attribute(dins_data_a, 0x10, "Din's Fire Charge Launch Angle", 2)
zelda.add_attribute(dins_data_a, 0x14, "Din's Fire Charge Initial Velocity", 2)
zelda.add_attribute(dins_data_a, 0x18, "Din's Fire Charge Acceleration", 2)
zelda.add_attribute(dins_data_a, 0x1C, "Din's Fire Charge Max Velocity", 2)
zelda.add_attribute(dins_data_a, 0x24, "Din's Fire Charge Vertical Meneuverability", 2)
zelda.add_attribute(dins_data_a, 0x28, "Din's Fire Charge Maximum Curve Angle", 2)
zelda.add_attribute(dins_data_a, 0x2C, "Din's Fire Charge Detonation Delay", 2)

dins_data_b = zelda.article_datas[1]
zelda.add_attribute(dins_data_b, 0x00, "Din's Fire Explosion Hitbox Size", 3)
zelda.add_attribute(dins_data_b, 0x04, "Din's Fire Explosion Initial Graphic Size", 3)
zelda.add_attribute(dins_data_b, 0x08, "Din's Fire Explosion Graphic Growth Multiplier", 3)
zelda.add_attribute(dins_data_b, 0x0C, "Din's Fire Explosion Base Damage", 3)
zelda.add_attribute(dins_data_b, 0x10, "Din's Fire Explosion Damage Multiplier", 3)