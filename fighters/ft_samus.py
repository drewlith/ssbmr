import fighter
from iso import DAT
from structs import hitbox

samus = fighter.Fighter("Samus", DAT(b'PlSs.dat'))
fighter.fighters.append(samus)
samus.fighter_id = 0x10

samus.special_attribute_block_size = 0xD3
samus.articles_sizes = [0x10, 0x20, 0x38, 0x7C]
samus.articles_offsets = [0x4124, 0x3E90, 0x4018, 0x4210]
samus.projectile_offsets = [0x3ED4, 0x4070, 0x408C, 0x4170]

samus.good_sfx = [0x3f7c1, 0x3f7e8, 0x3f7df, 0x3f7cd, 0x3f7c7, 0x3f7ca, 0x3f7b5, 0x3f7b8, 0x3f7be, 0x3f7bb]

file_data = samus.dat_file.file_data
offset = samus.projectile_offsets[0]
chargeshot_hitbox = hitbox.Hitbox(file_data[offset:offset+20], offset)
#chargeshot_hitbox.tags.append("projectile")
samus.projectile_hitboxes.append(chargeshot_hitbox)

offset = samus.projectile_offsets[1]
homingmissile_hitbox = hitbox.Hitbox(file_data[offset:offset+20], offset)
homingmissile_hitbox.tags.append("projectile")
samus.projectile_hitboxes.append(homingmissile_hitbox)

offset = samus.projectile_offsets[2]
supermissile_hitbox = hitbox.Hitbox(file_data[offset:offset+20], offset)
#supermissile_hitbox.tags.append("projectile")
samus.projectile_hitboxes.append(supermissile_hitbox)

offset = samus.projectile_offsets[3]
bomb_hitbox = hitbox.Hitbox(file_data[offset:offset+20], offset)
bomb_hitbox.tags.append("projectile")
samus.projectile_hitboxes.append(bomb_hitbox)

samus.subactions[0x127].friendly_name = "Morph Ball Bomb"
samus.subactions[0x128].friendly_name = "Morph Ball Bomb"
samus.subactions[0x129].friendly_name = "Charge Shot"
samus.subactions[0x12A].friendly_name = "Charge Shot"
samus.subactions[0x12B].friendly_name = "Charge Shot"
samus.subactions[0x12C].friendly_name = "Charge Shot"
samus.subactions[0x12D].friendly_name = "Charge Shot"
samus.subactions[0x12E].friendly_name = "Charge Shot"
samus.subactions[0x12F].friendly_name = "Missile"
samus.subactions[0x130].friendly_name = "Missile"
samus.subactions[0x131].friendly_name = "Missile"
samus.subactions[0x132].friendly_name = "Missile"
samus.subactions[0x133].friendly_name = "Screw Attack"
samus.subactions[0x134].friendly_name = "Screw Attack"
samus.subactions[0x135].friendly_name = "Morph Ball Bomb"
samus.subactions[0x136].friendly_name = "Morph Ball Bomb"
samus.subactions[0x137].friendly_name = "Grapple Beam"
samus.subactions[0x138].friendly_name = "Grapple Beam"

for action in samus.subactions:
    if "Nameless" not in action.friendly_name:
        action.tags.append(action.friendly_name.lower().replace(" ", ""))

attribute_data = samus.dat_file.get_special_attribute_data(samus.special_attribute_block_size)
samus.add_attribute(attribute_data, 0x0, "Morph Ball Bomb Self Hit Animation Delay", 1)
samus.add_attribute(attribute_data, 0x4, "Morph Ball Bomb Self Hit Grounded Launch Angle", 1)
samus.add_attribute(attribute_data, 0x8, "Morph Ball Bomb Self Hit Momentum", 1)
samus.add_attribute(attribute_data, 0x10, "Morph Ball Bomb Self Hit Horizontal Velocity Multiplier", 1)
samus.add_attribute(attribute_data, 0x18, "Charge Shot Charge Time", 1)
samus.add_attribute(attribute_data, 0x1C, "Charge Shot Recoil", 1)
samus.add_attribute(attribute_data, 0x20, "Charge Shot Frames Per Charge Level", 1)
samus.get_attribute("Charge Shot Frames Per Charge Level").integer = True
samus.add_attribute(attribute_data, 0x24, "Charge Shot Landing Lag", 1)
samus.add_attribute(attribute_data, 0x28, "Missile Smash Window", 1)
samus.add_attribute(attribute_data, 0x2C, "Missile Momentum Preservation", 1)
samus.add_attribute(attribute_data, 0x30, "Missile Momentum Preservation Multiplier", 1)
samus.add_attribute(attribute_data, 0x34, "Missile Spawn X-Offset", 1)
samus.add_attribute(attribute_data, 0x38, "Screw Attack Grounded Start Horizontal Momentum", 1)
samus.add_attribute(attribute_data, 0x3C, "Screw Attack Control Variable", 1)
samus.add_attribute(attribute_data, 0x40, "Screw Attack Air Friction", 1)
samus.add_attribute(attribute_data, 0x44, "Screw Attack Aerial Vertical Momentum", 1)
samus.add_attribute(attribute_data, 0x50, "Screw Attack Landing Lag", 1)
samus.add_attribute(attribute_data, 0x54, "Morph Ball Bomb Ground Vertical Momentum", 1)
samus.add_attribute(attribute_data, 0x58, "Morph Ball Bomb Air Vertical Momentum", 1)
samus.add_attribute(attribute_data, 0x5C, "Morph Ball Bomb Ground Mobility", 1)
samus.add_attribute(attribute_data, 0x60, "Morph Ball Bomb Air Mobility", 1)
samus.add_attribute(attribute_data, 0x64, "Morph Ball Bomb Ground Acceleration Multiplier", 1)
samus.add_attribute(attribute_data, 0x68, "Morph Ball Bomb Air Acceleration Multiplier", 1)
samus.add_attribute(attribute_data, 0x6C, "Morph Ball Bomb Ground Speed Multiplier", 1)
samus.add_attribute(attribute_data, 0x70, "Morph Ball Bomb Air Speed Multiplier", 1)
samus.add_attribute(attribute_data, 0x74, "Morph Ball Bomb X-Offset", 1)
samus.add_attribute(attribute_data, 0x78, "Morph Ball Bomb Y-Offset", 1)
samus.add_attribute(attribute_data, 0x9C, "Grapple Beam Grab Delay", 1)
samus.get_attribute("Grapple Beam Grab Delay").integer = True
samus.add_attribute(attribute_data, 0xA0, "Grapple Beam Grab Chain Release Begin", 1)
samus.get_attribute("Grapple Beam Grab Chain Release Begin").integer = True
samus.add_attribute(attribute_data, 0xA4, "Grapple Beam Grab Chain Retract Begin", 1)
samus.get_attribute("Grapple Beam Grab Chain Retract Begin").integer = True
samus.add_attribute(attribute_data, 0xA8, "Grapple Beam Grab Chain Retract Finish", 1)
samus.get_attribute("Grapple Beam Grab Chain Retract Finish").integer = True
samus.add_attribute(attribute_data, 0xAC, "Grapple Beam Dash Grab Delay", 1)
samus.get_attribute("Grapple Beam Dash Grab Delay").integer = True
samus.add_attribute(attribute_data, 0xB0, "Grapple Beam Dash Grab Chain Release Begin", 1)
samus.get_attribute("Grapple Beam Dash Grab Chain Release Begin").integer = True
samus.add_attribute(attribute_data, 0xB4, "Grapple Beam Dash Grab Chain Retract Begin", 1)
samus.get_attribute("Grapple Beam Dash Grab Chain Retract Begin").integer = True
samus.add_attribute(attribute_data, 0xB8, "Grapple Beam Dash Grab Chain Retract Finish", 1)
samus.get_attribute("Grapple Beam Dash Grab Chain Retract Finish").integer = True
samus.add_attribute(attribute_data, 0xBC, "Grapple Beam Air Delay", 1)
samus.get_attribute("Grapple Beam Air Delay").integer = True
samus.add_attribute(attribute_data, 0xC0, "Grapple Beam Air Chain Release Begin", 1)
samus.get_attribute("Grapple Beam Air Chain Release Begin").integer = True
samus.add_attribute(attribute_data, 0xC4, "Grapple Beam Air Chain Retract Begin", 1)
samus.get_attribute("Grapple Beam Air Chain Retract Begin").integer = True
samus.add_attribute(attribute_data, 0xC8, "Grapple Beam Air Chain Retract Finish", 1)
samus.get_attribute("Grapple Beam Air Chain Retract Finish").integer = True
samus.add_attribute(attribute_data, 0xCC, "Grapple Beam Wall Release Jump Height", 1)
samus.add_attribute(attribute_data, 0xD0, "Grapple Beam Hang Duration", 1)
samus.get_attribute("Grapple Beam Hang Duration").integer = True

samus.article_datas = samus.dat_file.get_article_data(samus)
bomb_data = samus.article_datas[0]
samus.add_attribute(bomb_data, 0x00, "Morph Ball Bomb Duration", 2)

beam_data = samus.article_datas[1]
samus.add_attribute(beam_data, 0x00, "Charge Shot Duration", 3)
samus.add_attribute(beam_data, 0x04, "Charge Shot Angle", 3)
samus.add_attribute(beam_data, 0x08, "Charge Shot Base Velocity", 3)
samus.add_attribute(beam_data, 0x0C, "Charge Shot Charged Velocity", 3)
samus.add_attribute(beam_data, 0x18, "Charge Shot Initial Size", 3)
samus.add_attribute(beam_data, 0x1C, "Charge Shot Full Charge Graphic Size", 3)

missile_data = samus.article_datas[2]
samus.add_attribute(missile_data, 0x04, "Missile Duration", 4)
samus.add_attribute(missile_data, 0x08, "Missile Deceleration Frame", 4)
samus.add_attribute(missile_data, 0x0C, "Missile Initial Velocity", 4)
samus.add_attribute(missile_data, 0x10, "Missile Velocity After Deceleration", 4)
samus.add_attribute(missile_data, 0x14, "Missile Deceleration Rate", 4)
samus.add_attribute(missile_data, 0x18, "Missile Homing Accuracy", 4)
samus.add_attribute(missile_data, 0x1C, "Missile Max Homing Angle", 4)
samus.add_attribute(missile_data, 0x20, "Missile Homing Modifier", 4)
samus.add_attribute(missile_data, 0x24, "Super Missile Duration", 4)
samus.add_attribute(missile_data, 0x28, "Super Missile Acceleration Frame", 4)
samus.add_attribute(missile_data, 0x2C, "Super Missile Initial Velocity", 4)
samus.add_attribute(missile_data, 0x30, "Super Missile Acceleration Rate", 4)
samus.add_attribute(missile_data, 0x34, "Super Missile Terminal Velocity", 4)

grapple_data = samus.article_datas[3]
samus.add_attribute(grapple_data, 0x00, "Grapple Beam Recoil On Angled Surface", 5)
samus.add_attribute(grapple_data, 0x0C, "Grapple Beam Number of Segments", 5)
samus.get_attribute("Grapple Beam Number of Segments").integer = True
samus.add_attribute(grapple_data, 0x10, "Grapple Beam Distance Between Segments", 5)
samus.add_attribute(grapple_data, 0x14, "Grapple Beam Elasticity", 5)
samus.add_attribute(grapple_data, 0x18, "Grapple Beam Launch Speed", 5)
samus.add_attribute(grapple_data, 0x1C, "Grapple Beam Gravity", 5)
samus.add_attribute(grapple_data, 0x20, "Grapple Beam Retraction Speed", 5)
samus.add_attribute(grapple_data, 0x24, "Grapple Beam End Retraction Speed", 5)
samus.add_attribute(grapple_data, 0x5C, "Grapple Beam Ground Length Modifier", 5)
samus.add_attribute(grapple_data, 0x60, "Grapple Beam Air Length Modifier", 5)