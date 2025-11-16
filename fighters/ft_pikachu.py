import fighter
from iso import DAT
from structs import hitbox

pikachu = fighter.Fighter("Pikachu", DAT(b'PlPk.dat'))
fighter.fighters.append(pikachu)
pikachu.fighter_id = 0x0D

pikachu.special_attribute_block_size = 0xF8
pikachu.articles_sizes = [0xC, 0xC]
pikachu.articles_offsets = [0x3E1C, 0x3C74]
pikachu.projectile_offsets = [0x3CA4, 0x3E28]

pikachu.good_sfx = [0x3a9e4, 0x3a9e1, 0x3a9a8, 0x3a9b7, 0x3a987, 0x3a98a, 0x3a999, 0x3a9c0, 0x3a9d8, 0x3a9c3, 0x3a9de, 0x3a99c, 0x3a9d5, 0x3a99f, 0x3a9b1, 0x3a9d2]

file_data = pikachu.dat_file.file_data
offset = pikachu.projectile_offsets[0]
jolt_hitbox = hitbox.Hitbox(file_data[offset:offset+20], offset)
jolt_hitbox.tags.append("projectile")
pikachu.projectile_hitboxes.append(jolt_hitbox)

offset = pikachu.projectile_offsets[1]
thunder_hitbox = hitbox.Hitbox(file_data[offset:offset+20], offset)
thunder_hitbox.tags.append("projectile")
pikachu.projectile_hitboxes.append(thunder_hitbox)

pikachu.subactions[0x127].friendly_name = "Thunder Jolt"
pikachu.subactions[0x128].friendly_name = "Thunder Jolt"
pikachu.subactions[0x129].friendly_name = "Skull Bash"
pikachu.subactions[0x12A].friendly_name = "Skull Bash"
pikachu.subactions[0x12B].friendly_name = "Skull Bash"
pikachu.subactions[0x12C].friendly_name = "Skull Bash"
pikachu.subactions[0x12D].friendly_name = "Skull Bash"
pikachu.subactions[0x12E].friendly_name = "Skull Bash"
pikachu.subactions[0x12F].friendly_name = "Skull Bash"
pikachu.subactions[0x130].friendly_name = "Skull Bash"
pikachu.subactions[0x131].friendly_name = "Skull Bash"
pikachu.subactions[0x132].friendly_name = "Quick Attack"
pikachu.subactions[0x133].friendly_name = "Quick Attack"
pikachu.subactions[0x134].friendly_name = "Quick Attack"
pikachu.subactions[0x135].friendly_name = "Quick Attack"
pikachu.subactions[0x136].friendly_name = "Quick Attack"
pikachu.subactions[0x137].friendly_name = "Quick Attack"
pikachu.subactions[0x138].friendly_name = "Thunder!"
pikachu.subactions[0x139].friendly_name = "Thunder!"
pikachu.subactions[0x13A].friendly_name = "Thunder!"
pikachu.subactions[0x13B].friendly_name = "Thunder!"
pikachu.subactions[0x13C].friendly_name = "Thunder!"
pikachu.subactions[0x13D].friendly_name = "Thunder!"
pikachu.subactions[0x13E].friendly_name = "Thunder!"
pikachu.subactions[0x13F].friendly_name = "Thunder!"

for action in pikachu.subactions:
    if "Nameless" not in action.friendly_name:
        action.tags.append(action.friendly_name.lower().replace(" ", ""))

attribute_data = pikachu.dat_file.get_special_attribute_data(pikachu.special_attribute_block_size)
pikachu.add_attribute(attribute_data, 0x0, "Thunder Jolt Ground Spawn X-Offset", 1)
pikachu.add_attribute(attribute_data, 0x4, "Thunder Jolt Ground Spawn Y-Offset", 1)
pikachu.add_attribute(attribute_data, 0x8, "Thunder Jolt Air Spawn X-Offset", 1)
pikachu.add_attribute(attribute_data, 0xC, "Thunder Jolt Air Spawn Y-Offset", 1)
pikachu.add_attribute(attribute_data, 0x10, "Thunder Jolt Landing Lag", 1)
pikachu.add_attribute(attribute_data, 0x1C, "Skull Bash Smash Window", 1)
pikachu.add_attribute(attribute_data, 0x20, "Skull Bash Charge Rate", 1)
pikachu.add_attribute(attribute_data, 0x24, "Skull Bash Max Charge Duration", 1)
pikachu.add_attribute(attribute_data, 0x28, "Skull Bash Tilt Damage", 1)
pikachu.add_attribute(attribute_data, 0x30, "Skull Bash Traction Multiplier", 1)
pikachu.add_attribute(attribute_data, 0x38, "Skull Bash Falling Speed", 1)
pikachu.add_attribute(attribute_data, 0x3C, "Skull Bash Horizontal Launch Momentum", 1)
pikachu.add_attribute(attribute_data, 0x40, "Skull Bash Horizontal Momentum Multiplier", 1)
pikachu.add_attribute(attribute_data, 0x44, "Skull Bash Vertical Launch Momentum", 1)
pikachu.add_attribute(attribute_data, 0x48, "Skull Bash Vertical Momentum Multiplier", 1)
pikachu.add_attribute(attribute_data, 0x4C, "Skull Bash Gravity During Launch Animation", 1)
pikachu.add_attribute(attribute_data, 0x50, "Skull Bash Ending Friction Modifier", 1)
pikachu.add_attribute(attribute_data, 0x54, "Skull Bash Horizontal Deceleration", 1)
pikachu.add_attribute(attribute_data, 0x58, "Skull Bash Gravity During End of Launch", 1)
pikachu.add_attribute(attribute_data, 0x60, "Quick Attack Travel Distance", 1)
pikachu.get_attribute("Quick Attack Travel Distance").integer = True
pikachu.add_attribute(attribute_data, 0x64, "Quick Attack Momentum Variable", 1)
pikachu.add_attribute(attribute_data, 0x68, "Quick Attack Grounded Model Rotation", 1)
pikachu.add_attribute(attribute_data, 0x6C, "Quick Attack Grounded Model Width Multiplier", 1)
pikachu.add_attribute(attribute_data, 0x70, "Quick Attack Grounded Model Height Multiplier", 1)
pikachu.add_attribute(attribute_data, 0x74, "Quick Attack Air Model Length Multiplier", 1)
pikachu.add_attribute(attribute_data, 0x78, "Quick Attack Air Model Rotation", 1)
pikachu.add_attribute(attribute_data, 0x7C, "Quick Attack Air Model Width Multiplier", 1)
pikachu.add_attribute(attribute_data, 0x80, "Quick Attack Air Model Height Multiplier", 1)
pikachu.add_attribute(attribute_data, 0x84, "Quick Attack Air Model Length Multiplier", 1)
pikachu.add_attribute(attribute_data, 0x90, "Quick Attack Base Dash Momentum", 1)
pikachu.add_attribute(attribute_data, 0x94, "Quick Attack Start Momentum Boost", 1)
pikachu.add_attribute(attribute_data, 0x98, "Quick Attack Second Dash Length Multiplier", 1)
pikachu.add_attribute(attribute_data, 0x9C, "Quick Attack Momentum Preservation", 1)
pikachu.add_attribute(attribute_data, 0xA4, "Quick Attack Momentum Variable 2", 1)
pikachu.add_attribute(attribute_data, 0xB0, "Quick Attack Landing Lag", 1)
pikachu.add_attribute(attribute_data, 0xB4, "Thunder Vertical Momentum Gain on Strike", 1)
pikachu.add_attribute(attribute_data, 0xB8, "Thunder Fall Acceleration on Strike", 1)
pikachu.add_attribute(attribute_data, 0xC0, "Thunder Travel Speed", 1)
pikachu.add_attribute(attribute_data, 0xCC, "Thunder Displacement of Thunder Cloud", 1)
pikachu.add_attribute(attribute_data, 0xD0, "Thunder Spawn Y-Offset", 1)
pikachu.add_attribute(attribute_data, 0xD4, "Thunder Number of Bursts", 1)
pikachu.get_attribute("Thunder Number of Bursts").integer = True
pikachu.add_attribute(attribute_data, 0xD8, "Thunder Delay Between Bursts", 1)
pikachu.get_attribute("Thunder Delay Between Bursts").integer = True

pikachu.article_datas = pikachu.dat_file.get_article_data(pikachu)
thunder_data = pikachu.article_datas[0]
pikachu.add_attribute(thunder_data, 0x0, "Thunder Maximum Travel Distance", 2)
pikachu.add_attribute(thunder_data, 0x4, "Thunder Vertical Collision Detection", 2)
pikachu.add_attribute(thunder_data, 0x8, "Thunder Size of Self-hit Collision Detection", 2)

jolt_data = pikachu.article_datas[1]
pikachu.add_attribute(jolt_data, 0x0, "Thunder Jolt Duration", 3)
pikachu.add_attribute(jolt_data, 0x4, "Thunder Jolt Launch Angle", 3)
pikachu.add_attribute(jolt_data, 0x8, "Thunder Jolt Aerial Launch Velocity", 3)