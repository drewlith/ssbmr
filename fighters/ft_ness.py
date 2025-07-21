import fighter
from iso import DAT
from structs import hitbox

ness = fighter.Fighter("Ness", DAT(b'PlNs.dat'))
fighter.fighters.append(ness)
ness.fighter_id = 0x0B

ness.special_attribute_block_size = 0xDC
ness.articles_sizes = [0x8, 0xC, 0x2C, 0x14, 0x14, 0x5C]
ness.articles_offsets = [0x3E48, 0x3F10, 0x3C78, 0x4024, 0x3C7C, 0x4284]
ness.projectile_offsets = [0x3D94, 0x3F3C, 0x3F5C, 0x4138]

ness.subactions[295].friendly_name = "Up Smash Yo-Yo"
ness.subactions[296].friendly_name = "Up Smash Yo-Yo"
ness.subactions[298].friendly_name = "Down Smash Yo-Yo"
ness.subactions[312].friendly_name = "PK Thunder 2"

file_data = ness.dat_file.file_data
offset = ness.projectile_offsets[0]
pkflash_hitbox = hitbox.Hitbox(file_data[offset:offset+20], offset)
pkflash_hitbox.tags.append("projectile")
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
ness.add_attribute(attribute_data, 0xAC, "Yo-Yo Smash Charge Duration", 1)
ness.add_attribute(attribute_data, 0xB0, "Yo-Yo Smash Charge Damage Multiplier", 1)
ness.add_attribute(attribute_data, 0xB4, "Yo-Yo Smash Charge Hitbox Rehit Rate", 1)
ness.add_attribute(attribute_data, 0xB8, "Baseball Bat Max Damage Reflectable", 1)
ness.get_attribute("Baseball Bat Max Damage Reflectable").integer = True
ness.add_attribute(attribute_data, 0xB8, "Baseball Bat Reflection Damage Multiplier", 1)
ness.add_attribute(attribute_data, 0xB8, "Baseball Bat Reflection Speed Multiplier", 1)

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
ness.add_attribute(yoyo_data, 0x00, "Yo-Yo Number of String Segments", 7)
ness.get_attribute("Yo-Yo Number of String Segments").integer = True
ness.add_attribute(yoyo_data, 0x04, "Yo-Yo Number of Up-Smash String Segments", 7)
ness.get_attribute("Yo-Yo Number of Up-Smash String Segments").integer = True
ness.add_attribute(yoyo_data, 0x08, "Yo-Yo Number of Down-Smash String Segments", 7)
ness.get_attribute("Yo-Yo Number of Down-Smash String Segments").integer = True
ness.add_attribute(yoyo_data, 0x0C, "Yo-Yo String Size", 7)
ness.add_attribute(yoyo_data, 0x18, "Yo-Yo Spin Animation Speed", 7)
ness.add_attribute(yoyo_data, 0x1C, "Yo-Yo Charge Spin Animation Speed", 7)
ness.add_attribute(yoyo_data, 0x20, "Yo-Yo Charge Spin Animation Speed Modifier", 7)
ness.add_attribute(yoyo_data, 0x24, "Yo-Yo Charge Horizontal Release Velocity", 7)
ness.add_attribute(yoyo_data, 0x28, "Yo-Yo Charge Pull Acceleration", 7)
ness.add_attribute(yoyo_data, 0x2C, "Yo-Yo Max Charge Horizontal Velocity", 7)
ness.add_attribute(yoyo_data, 0x30, "Yo-Yo Charge Vertical Release Velocity", 7)
ness.add_attribute(yoyo_data, 0x34, "Yo-Yo Charge Base Gravity", 7)
ness.add_attribute(yoyo_data, 0x38, "Yo-Yo Charge Terminal Velocity", 7)
ness.add_attribute(yoyo_data, 0x3C, "Yo-Yo Charge Horizontal Pull Strength", 7)
ness.add_attribute(yoyo_data, 0x40, "Yo-Yo Frame for Up Smash Model Rotation Change", 7)
ness.get_attribute("Yo-Yo Frame for Up Smash Model Rotation Change").integer = True
ness.add_attribute(yoyo_data, 0x44, "Yo-Yo Frame for Up Smash Snap to Palm", 7)
ness.get_attribute("Yo-Yo Frame for Up Smash Snap to Palm").integer = True
ness.add_attribute(yoyo_data, 0x48, "Yo-Yo Frame for Down Smash Model Rotation Change", 7)
ness.get_attribute("Yo-Yo Frame for Down Smash Model Rotation Change").integer = True
ness.add_attribute(yoyo_data, 0x4C, "Yo-Yo Frame for Down Smash Snap to Palm", 7)
ness.get_attribute("Yo-Yo Frame for Down Smash Snap to Palm").integer = True