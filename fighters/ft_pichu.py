import fighter
from iso import DAT
from structs import hitbox

pichu = fighter.Fighter("Pichu", DAT(b'PlPc.dat'))
fighter.fighters.append(pichu)
pichu.fighter_id = 0x18

pichu.special_attribute_block_size = 0xF8
pichu.articles_sizes = [0xC, 0xC]
pichu.articles_offsets = [0x3CBC, 0x3B34]
pichu.projectile_offsets = [0x3B64, 0x3CE8]

file_data = pichu.dat_file.file_data
offset = pichu.projectile_offsets[0]
jolt_hitbox = hitbox.Hitbox(file_data[offset:offset+20], offset)
jolt_hitbox.tags.append("projectile")
pichu.projectile_hitboxes.append(jolt_hitbox)

offset = pichu.projectile_offsets[1]
thunder_hitbox = hitbox.Hitbox(file_data[offset:offset+20], offset)
thunder_hitbox.tags.append("projectile")
pichu.projectile_hitboxes.append(thunder_hitbox)

pichu.subactions[298].friendly_name = "Skull Bash"
pichu.subactions[299].friendly_name = "Skull Bash"
pichu.subactions[314].friendly_name = "Thunder"

attribute_data = pichu.dat_file.get_special_attribute_data(pichu.special_attribute_block_size)
pichu.add_attribute(attribute_data, 0x0, "Thunder Jolt Ground Spawn X-Offset", 1)
pichu.add_attribute(attribute_data, 0x4, "Thunder Jolt Ground Spawn Y-Offset", 1)
pichu.add_attribute(attribute_data, 0x8, "Thunder Jolt Air Spawn X-Offset", 1)
pichu.add_attribute(attribute_data, 0xC, "Thunder Jolt Air Spawn Y-Offset", 1)
pichu.add_attribute(attribute_data, 0x10, "Thunder Jolt Landing Lag", 1)
pichu.add_attribute(attribute_data, 0x1C, "Skull Bash Smash Window", 1)
pichu.add_attribute(attribute_data, 0x20, "Skull Bash Charge Rate", 1)
pichu.add_attribute(attribute_data, 0x24, "Skull Bash Max Charge Duration", 1)
pichu.add_attribute(attribute_data, 0x28, "Skull Bash Tilt Damage", 1)
pichu.add_attribute(attribute_data, 0x30, "Skull Bash Traction Multiplier", 1)
pichu.add_attribute(attribute_data, 0x38, "Skull Bash Falling Speed", 1)
pichu.add_attribute(attribute_data, 0x3C, "Skull Bash Horizontal Launch Momentum", 1)
pichu.add_attribute(attribute_data, 0x40, "Skull Bash Horizontal Momentum Multiplier", 1)
pichu.add_attribute(attribute_data, 0x44, "Skull Bash Vertical Launch Momentum", 1)
pichu.add_attribute(attribute_data, 0x48, "Skull Bash Vertical Momentum Multiplier", 1)
pichu.add_attribute(attribute_data, 0x4C, "Skull Bash Gravity During Launch Animation", 1)
pichu.add_attribute(attribute_data, 0x50, "Skull Bash Ending Friction Modifier", 1)
pichu.add_attribute(attribute_data, 0x54, "Skull Bash Horizontal Deceleration", 1)
pichu.add_attribute(attribute_data, 0x58, "Skull Bash Gravity During End of Launch", 1)
pichu.add_attribute(attribute_data, 0x60, "Agility Travel Distance", 1)
pichu.get_attribute("Agility Travel Distance").integer = True
pichu.add_attribute(attribute_data, 0x64, "Agility Momentum Variable", 1)
pichu.add_attribute(attribute_data, 0x68, "Agility Grounded Model Rotation", 1)
pichu.add_attribute(attribute_data, 0x6C, "Agility Grounded Model Width Multiplier", 1)
pichu.add_attribute(attribute_data, 0x70, "Agility Grounded Model Height Multiplier", 1)
pichu.add_attribute(attribute_data, 0x74, "Agility Air Model Length Multiplier", 1)
pichu.add_attribute(attribute_data, 0x78, "Agility Air Model Rotation", 1)
pichu.add_attribute(attribute_data, 0x7C, "Agility Air Model Width Multiplier", 1)
pichu.add_attribute(attribute_data, 0x80, "Agility Air Model Height Multiplier", 1)
pichu.add_attribute(attribute_data, 0x84, "Agility Air Model Length Multiplier", 1)
pichu.add_attribute(attribute_data, 0x90, "Agility Base Dash Momentum", 1)
pichu.add_attribute(attribute_data, 0x94, "Agility Start Momentum Boost", 1)
pichu.add_attribute(attribute_data, 0x98, "Agility Second Dash Length Multiplier", 1)
pichu.add_attribute(attribute_data, 0x9C, "Agility Momentum Preservation", 1)
pichu.add_attribute(attribute_data, 0xA4, "Agility Momentum Variable 2", 1)
pichu.add_attribute(attribute_data, 0xB0, "Agility Landing Lag", 1)
pichu.add_attribute(attribute_data, 0xB4, "Thunder Vertical Momentum Gain on Strike", 1)
pichu.add_attribute(attribute_data, 0xB8, "Thunder Fall Acceleration on Strike", 1)
pichu.add_attribute(attribute_data, 0xC0, "Thunder Travel Speed", 1)
pichu.add_attribute(attribute_data, 0xCC, "Thunder Displacement of Thunder Cloud", 1)
pichu.add_attribute(attribute_data, 0xD0, "Thunder Spawn Y-Offset", 1)
pichu.add_attribute(attribute_data, 0xD4, "Thunder Number of Bursts", 1)
pichu.get_attribute("Thunder Number of Bursts").integer = True
pichu.add_attribute(attribute_data, 0xD8, "Thunder Delay Between Bursts", 1)
pichu.get_attribute("Thunder Delay Between Bursts").integer = True

pichu.article_datas = pichu.dat_file.get_article_data(pichu)
thunder_data = pichu.article_datas[0]
pichu.add_attribute(thunder_data, 0x0, "Thunder Maximum Travel Distance", 2)
pichu.add_attribute(thunder_data, 0x4, "Thunder Vertical Collision Detection", 2)
pichu.add_attribute(thunder_data, 0x8, "Thunder Size of Self-hit Collision Detection", 2)

jolt_data = pichu.article_datas[1]
pichu.add_attribute(jolt_data, 0x0, "Thunder Jolt Duration", 3)
pichu.add_attribute(jolt_data, 0x4, "Thunder Jolt Launch Angle", 3)
pichu.add_attribute(jolt_data, 0x8, "Thunder Jolt Aerial Launch Velocity", 3)