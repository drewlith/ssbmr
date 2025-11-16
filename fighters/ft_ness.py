import fighter
from iso import DAT
from structs import hitbox

ness = fighter.Fighter("Ness", DAT(b'PlNs.dat'))
fighter.fighters.append(ness)
ness.fighter_id = 0x0B

ness.special_attribute_block_size = 0xDC
ness.articles_sizes = [0x8, 0xC, 0x2C, 0x14, 0x14, 0x5C]
ness.articles_offsets = [0x3E48, 0x3F10, 0x3C78, 0x4024, 0x3D60, 0x4284]
ness.projectile_offsets = [0x3D94, 0x3F3C, 0x3F5C, 0x4138]

ness.good_sfx = [0x334a4, 0x3347d, 0x33456, 0x3346b, 0x33477, 0x3347a, 0x33483, 0x33480, 0x33492, 0x33489]

ness.subactions[0x127].friendly_name = "Up Smash YoYo"
ness.subactions[0x128].friendly_name = "Up Smash YoYo"
ness.subactions[0x129].friendly_name = "Down Smash YoYo"
ness.subactions[0x12A].friendly_name = "Down Smash YoYo"
ness.subactions[0x12B].friendly_name = "PK Flash"
ness.subactions[0x12C].friendly_name = "PK Flash"
ness.subactions[0x12D].friendly_name = "PK Flash"
ness.subactions[0x12E].friendly_name = "PK Flash"
ness.subactions[0x12F].friendly_name = "PK Flash"
ness.subactions[0x130].friendly_name = "PK Flash"
ness.subactions[0x131].friendly_name = "PK Flash"
ness.subactions[0x132].friendly_name = "PK Flash"
ness.subactions[0x133].friendly_name = "PK Fire"
ness.subactions[0x134].friendly_name = "PK Fire"
ness.subactions[0x135].friendly_name = "PK Thunder"
ness.subactions[0x136].friendly_name = "PK Thunder"
ness.subactions[0x137].friendly_name = "PK Thunder"
ness.subactions[0x138].friendly_name = "PK Thunder"
ness.subactions[0x139].friendly_name = "PK Thunder"
ness.subactions[0x13A].friendly_name = "PK Thunder"
ness.subactions[0x13B].friendly_name = "PK Thunder"
ness.subactions[0x13C].friendly_name = "PK Thunder"
ness.subactions[0x13E].friendly_name = "PK Magnet"
ness.subactions[0x13F].friendly_name = "PK Magnet"
ness.subactions[0x140].friendly_name = "PK Magnet"
ness.subactions[0x141].friendly_name = "PK Magnet"
ness.subactions[0x142].friendly_name = "PK Magnet"
ness.subactions[0x143].friendly_name = "PK Magnet"
ness.subactions[0x144].friendly_name = "PK Magnet"
ness.subactions[0x145].friendly_name = "PK Magnet"

for action in ness.subactions:
    if "Nameless" not in action.friendly_name:
        action.tags.append(action.friendly_name.lower().replace(" ", ""))

file_data = ness.dat_file.file_data
offset = ness.projectile_offsets[0]
pkflash_hitbox = hitbox.Hitbox(file_data[offset:offset+20], offset)
#pkflash_hitbox.tags.append("projectile")
ness.projectile_hitboxes.append(pkflash_hitbox)

offset = ness.projectile_offsets[1]
pkfire_a_hitbox = hitbox.Hitbox(file_data[offset:offset+20], offset)
pkfire_a_hitbox.tags.append("projectile")
ness.projectile_hitboxes.append(pkfire_a_hitbox)

offset = ness.projectile_offsets[2]
pkfire_b_hitbox = hitbox.Hitbox(file_data[offset:offset+20], offset)
pkfire_b_hitbox.tags.append("projectile")
ness.projectile_hitboxes.append(pkfire_b_hitbox)

offset = ness.projectile_offsets[3]
pkthunder_hitbox = hitbox.Hitbox(file_data[offset:offset+20], offset)
pkthunder_hitbox.tags.append("projectile")
ness.projectile_hitboxes.append(pkthunder_hitbox)

attribute_data = ness.dat_file.get_special_attribute_data(ness.special_attribute_block_size)
ness.add_attribute(attribute_data, 0x0, "PK Flash Grounded Animation Loop Frames", 1)
ness.get_attribute("PK Flash Grounded Animation Loop Frames").integer = True
ness.add_attribute(attribute_data, 0x4, "PK Flash Air Animation Loop Frames", 1)
ness.get_attribute("PK Flash Air Animation Loop Frames").integer = True
ness.add_attribute(attribute_data, 0x8, "PK Flash Falling Acceleration Delay", 1)
ness.get_attribute("PK Flash Falling Acceleration Delay").integer = True
ness.add_attribute(attribute_data, 0xC, "PK Flash Charge Release Delay", 1)
ness.get_attribute("PK Flash Charge Release Delay").integer = True
ness.add_attribute(attribute_data, 0x14, "PK Flash Gravity", 1)
ness.add_attribute(attribute_data, 0x1C, "PK Flash Landing Lag", 1)
ness.add_attribute(attribute_data, 0x20, "PK Fire Air Launch Trajectory", 1)
ness.add_attribute(attribute_data, 0x24, "PK Fire Aerial Velocity", 1)
ness.add_attribute(attribute_data, 0x28, "PK Fire Ground Launch Trajectory", 1)
ness.add_attribute(attribute_data, 0x2C, "PK Fire Ground Velocity", 1)
ness.add_attribute(attribute_data, 0x30, "PK Fire Spawn X-Offset", 1)
ness.add_attribute(attribute_data, 0x34, "PK Fire Spawn Y-Offset", 1)
ness.add_attribute(attribute_data, 0x38, "PK Fire Landing Lag", 1)
ness.add_attribute(attribute_data, 0x44, "PK Thunder Animation Timer On Hit", 1)
ness.get_attribute("PK Thunder Animation Timer On Hit").integer = True
ness.add_attribute(attribute_data, 0x48, "PK Thunder Fall Delay", 1)
ness.get_attribute("PK Thunder Fall Delay").integer = True
ness.add_attribute(attribute_data, 0x50, "PK Thunder Fall Acceleration", 1)
ness.add_attribute(attribute_data, 0x54, "PK Thunder 2 Momentum", 1)
ness.add_attribute(attribute_data, 0x5C, "PK Thunder 2 Deceleration Rate", 1)
ness.add_attribute(attribute_data, 0x70, "PK Thunder 2 Landing Lag", 1)
ness.add_attribute(attribute_data, 0x74, "PK Magnet Initial Cooldown", 1)
ness.add_attribute(attribute_data, 0x84, "PK Magnet Fall Delay", 1)
ness.get_attribute("PK Magnet Fall Delay").integer = True
ness.add_attribute(attribute_data, 0x88, "PK Magnet Momentum Preservation", 1)
ness.add_attribute(attribute_data, 0x8C, "PK Magnet Fall Acceleration", 1)
ness.add_attribute(attribute_data, 0x94, "PK Magnet Healing Multiplier", 1)
ness.add_attribute(attribute_data, 0xA8, "PK Magnet Absorption Bubble Size", 1)
ness.add_attribute(attribute_data, 0xAC, "YoYo Smash Charge Duration", 1)
ness.add_attribute(attribute_data, 0xB0, "YoYo Smash Charge Damage Multiplier", 1)
ness.add_attribute(attribute_data, 0xB4, "YoYo Smash Charge Hitbox Rehit Rate", 1)
ness.add_attribute(attribute_data, 0xB8, "Baseball Bat Max Damage Reflectable", 1)
ness.get_attribute("Baseball Bat Max Damage Reflectable").integer = True
ness.add_attribute(attribute_data, 0xBC, "Baseball Bat Reflection Damage Multiplier", 1)
ness.add_attribute(attribute_data, 0xC0, "Baseball Bat Reflection Speed Multiplier", 1)

ness.article_datas = ness.dat_file.get_article_data(ness)
pkfire_spark_data = ness.article_datas[0]
ness.add_attribute(pkfire_spark_data, 0x0, "PK Fire Spark Duration", 2)
ness.add_attribute(pkfire_spark_data, 0x4, "PK Fire Spark Y Offset", 2)

pkfire_pillar_data = ness.article_datas[1]
ness.add_attribute(pkfire_pillar_data, 0x0, "PK Fire Pillar Duration", 3)
ness.add_attribute(pkfire_pillar_data, 0x4, "PK Fire Pillar Hurtbox Resistance", 3)
ness.add_attribute(pkfire_pillar_data, 0x8, "PK Fire Pillar Size Decay Multiplier", 3)

pkflash_charge_data = ness.article_datas[2]
ness.add_attribute(pkflash_charge_data, 0x0, "PK Flash Charge Duration", 4)
ness.add_attribute(pkflash_charge_data, 0x4, "PK Flash Charge Hitbox Size Modifier", 4)
ness.add_attribute(pkflash_charge_data, 0x8, "PK Flash Charge Initial Graphic Size Multiplier", 4)
ness.add_attribute(pkflash_charge_data, 0xC, "PK Flash Charge Graphic Growth Multiplier", 4)
ness.add_attribute(pkflash_charge_data, 0x10, "PK Flash Charge Horizontal Momentum", 4)
ness.add_attribute(pkflash_charge_data, 0x14, "PK Flash Charge Peak Rising Height", 4)
ness.add_attribute(pkflash_charge_data, 0x18, "PK Flash Charge Control Sensitivity", 4)
ness.add_attribute(pkflash_charge_data, 0x1C, "PK Flash Charge Projectile Gravity", 4)
ness.add_attribute(pkflash_charge_data, 0x28, "PK Flash Charge Detonation Delay", 4)

pkthunder_data = ness.article_datas[3]
ness.add_attribute(pkthunder_data, 0x0, "PK Thunder Duration", 5)
ness.add_attribute(pkthunder_data, 0x4, "PK Thunder Speed", 5)
ness.add_attribute(pkthunder_data, 0x8, "PK Thunder Initial Angle", 5)
ness.add_attribute(pkthunder_data, 0xC, "PK Thunder Turning Sensitivity", 5)
ness.add_attribute(pkthunder_data, 0x10, "PK Thunder Turning Radius", 5)

pkflash_data = ness.article_datas[4]
ness.add_attribute(pkflash_data, 0x00, "PK Flash 2 Hitbox Size Modifier", 6)
ness.add_attribute(pkflash_data, 0x04, "PK Flash 2 Graphic Size Multiplier", 6)
ness.add_attribute(pkflash_data, 0x08, "PK Flash 2 Graphic Growth Multiplier", 6)
ness.add_attribute(pkflash_data, 0x0C, "PK Flash 2 Base Damage", 6)
ness.add_attribute(pkflash_data, 0x10, "PK Flash 2 Damage Multiplier", 6)

yoyo_data = ness.article_datas[5]
ness.add_attribute(yoyo_data, 0x00, "YoYo Number of String Segments", 7)
ness.get_attribute("YoYo Number of String Segments").integer = True
ness.add_attribute(yoyo_data, 0x04, "YoYo Number of Up Smash String Segments", 7)
ness.get_attribute("YoYo Number of Up Smash String Segments").integer = True
ness.add_attribute(yoyo_data, 0x08, "YoYo Number of Down Smash String Segments", 7)
ness.get_attribute("YoYo Number of Down Smash String Segments").integer = True
ness.add_attribute(yoyo_data, 0x0C, "YoYo String Size", 7)
ness.add_attribute(yoyo_data, 0x18, "YoYo Spin Animation Speed", 7)
ness.add_attribute(yoyo_data, 0x1C, "YoYo Charge Spin Animation Speed", 7)
ness.add_attribute(yoyo_data, 0x20, "YoYo Charge Spin Animation Speed Modifier", 7)
ness.add_attribute(yoyo_data, 0x24, "YoYo Charge Horizontal Release Velocity", 7)
ness.add_attribute(yoyo_data, 0x28, "YoYo Charge Pull Acceleration", 7)
ness.add_attribute(yoyo_data, 0x2C, "YoYo Max Charge Horizontal Velocity", 7)
ness.add_attribute(yoyo_data, 0x30, "YoYo Charge Vertical Release Velocity", 7)
ness.add_attribute(yoyo_data, 0x34, "YoYo Charge Base Gravity", 7)
ness.add_attribute(yoyo_data, 0x38, "YoYo Charge Terminal Velocity", 7)
ness.add_attribute(yoyo_data, 0x3C, "YoYo Charge Horizontal Pull Strength", 7)
ness.add_attribute(yoyo_data, 0x40, "YoYo Frame for Up Smash Model Rotation Change", 7)
ness.get_attribute("YoYo Frame for Up Smash Model Rotation Change").integer = True
ness.add_attribute(yoyo_data, 0x44, "YoYo Frame for Up Smash Snap to Palm", 7)
ness.get_attribute("YoYo Frame for Up Smash Snap to Palm").integer = True
ness.add_attribute(yoyo_data, 0x48, "YoYo Frame for Down Smash Model Rotation Change", 7)
ness.get_attribute("YoYo Frame for Down Smash Model Rotation Change").integer = True
ness.add_attribute(yoyo_data, 0x4C, "YoYo Frame for Down Smash Snap to Palm", 7)
ness.get_attribute("YoYo Frame for Down Smash Snap to Palm").integer = True