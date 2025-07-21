import fighter
from iso import DAT
from structs import hitbox

link = fighter.Fighter("Link", DAT(b'PlLk.dat'))
fighter.fighters.append(link)
link.fighter_id = 0x06

link.special_attribute_block_size = 0xDC
link.articles_sizes = [0x34, 0x64, 0x64, 0x2C]
link.articles_offsets = [0x4204, 0x40C0, 0x3E58, 0x3F48]
link.projectile_offsets = [0x3FB4, 0x4258, 0x4184]

link.subactions[295].friendly_name = "Forward Smash (Second Hit)"
link.subactions[308].friendly_name = "Spin Attack (Ground)"
link.subactions[309].friendly_name = "Spin Attack (Aerial)"
link.subactions[312].friendly_name = "Hookshot (Aerial)"

file_data = link.dat_file.file_data

offset = link.projectile_offsets[0]
arrow_hitbox = hitbox.Hitbox(file_data[offset:offset+20], offset)
arrow_hitbox.tags.append("projectile")
offset = link.projectile_offsets[1]
bomb_impact_hitbox = hitbox.Hitbox(file_data[offset:offset+20], offset)
bomb_impact_hitbox.tags.append("projectile")
offset = link.projectile_offsets[2]
bomb_explosion_hitbox = hitbox.Hitbox(file_data[offset:offset+20], offset)
bomb_explosion_hitbox.tags.append("projectile")

link.projectile_hitboxes.append(arrow_hitbox)
link.projectile_hitboxes.append(bomb_impact_hitbox)
link.projectile_hitboxes.append(bomb_explosion_hitbox)


attribute_data = link.dat_file.get_special_attribute_data(link.special_attribute_block_size)
link.add_attribute(attribute_data, 0x00, "Bow Frames For Max Charge", 1)
link.add_attribute(attribute_data, 0x04, "Bow Charge Speed", 1)
link.add_attribute(attribute_data, 0x08, "Bow Landing Lag", 1)
link.add_attribute(attribute_data, 0x18, "Boomerang Launch Angle", 1)
link.add_attribute(attribute_data, 0x20, "Boomerang Smash Launch Velocity", 1)
link.add_attribute(attribute_data, 0x24, "Boomerang Tilt Launch Velocity", 1)
link.add_attribute(attribute_data, 0x30, "Spin Attack Landing Lag", 1)
link.add_attribute(attribute_data, 0x34, "Spin Attack Horizontal Momentum", 1)
link.add_attribute(attribute_data, 0x38, "Spin Attack Aerial Mobility", 1)
link.add_attribute(attribute_data, 0x3C, "Spin Attack Momentum Preservation", 1)
link.add_attribute(attribute_data, 0x40, "Spin Attack Vertical Momentum", 1)
link.add_attribute(attribute_data, 0x44, "Spin Attack Landing Gravity", 1)
link.add_attribute(attribute_data, 0x4C, "Down Aerial Bounce Momentum", 1)
link.add_attribute(attribute_data, 0x50, "Down Aerial Hitbox Reapply Rate", 1)
link.add_attribute(attribute_data, 0x58, "Down Aerial Hitbox 0 Damage On Rehit", 1)
link.get_attribute("Down Aerial Hitbox 0 Damage On Rehit").integer = True
link.add_attribute(attribute_data, 0x5C, "Down Aerial Hitbox 1 Damage On Rehit", 1)
link.get_attribute("Down Aerial Hitbox 1 Damage On Rehit").integer = True
link.add_attribute(attribute_data, 0x60, "Down Aerial Hitbox 2 Damage On Rehit", 1)
link.get_attribute("Down Aerial Hitbox 2 Damage On Rehit").integer = True
link.add_attribute(attribute_data, 0x7C, "Sword Trail Width", 1)
link.add_attribute(attribute_data, 0x7C, "Sword Trail Height", 1)
link.add_attribute(attribute_data, 0x84, "Hookshot Grab Delay", 1)
link.get_attribute("Hookshot Grab Delay").integer = True
link.add_attribute(attribute_data, 0x88, "Hookshot Grab Chain Release Begin", 1)
link.get_attribute("Hookshot Grab Chain Release Begin").integer = True
link.add_attribute(attribute_data, 0x8C, "Hookshot Grab Chain Retract Begin", 1)
link.get_attribute("Hookshot Grab Chain Retract Begin").integer = True
link.add_attribute(attribute_data, 0x90, "Hookshot Grab Chain Retract Finish", 1)
link.get_attribute("Hookshot Grab Chain Retract Finish").integer = True
link.add_attribute(attribute_data, 0x94, "Hookshot Dash Grab Delay", 1)
link.get_attribute("Hookshot Dash Grab Delay").integer = True
link.add_attribute(attribute_data, 0x98, "Hookshot Dash Grab Chain Release Begin", 1)
link.get_attribute("Hookshot Dash Grab Chain Release Begin").integer = True
link.add_attribute(attribute_data, 0x9C, "Hookshot Dash Grab Chain Retract Begin", 1)
link.get_attribute("Hookshot Dash Grab Chain Retract Begin").integer = True
link.add_attribute(attribute_data, 0xA0, "Hookshot Dash Grab Chain Retract Finish", 1)
link.get_attribute("Hookshot Dash Grab Chain Retract Finish").integer = True
link.add_attribute(attribute_data, 0xA4, "Hookshot Air Delay", 1)
link.get_attribute("Hookshot Air Delay").integer = True
link.add_attribute(attribute_data, 0xA8, "Hookshot Air Chain Release Begin", 1)
link.get_attribute("Hookshot Air Chain Release Begin",).integer = True
link.add_attribute(attribute_data, 0xAC, "Hookshot Air Chain Retract Begin", 1)
link.get_attribute("Hookshot Air Chain Retract Begin").integer = True
link.add_attribute(attribute_data, 0xB0, "Hookshot Air Chain Retract Finish", 1)
link.get_attribute("Hookshot Air Chain Retract Finish").integer = True
link.add_attribute(attribute_data, 0xB4, "Hookshot Wall Release Jump Height", 1)
link.add_attribute(attribute_data, 0xB8, "Hookshot Hang Duration", 1)
link.get_attribute("Hookshot Hang Duration").integer = True
link.add_attribute(attribute_data, 0xD4, "Hylian Shield Collision Bubble Size", 1)
link.add_attribute(attribute_data, 0xD8, "Hylian Shield Impact Momentum Multiplier", 1)

link.article_datas = link.dat_file.get_article_data(link)
bomb_data = link.article_datas[0]
link.add_attribute(bomb_data, 0x00, "Bomb Duration", 2)
link.get_attribute("Bomb Duration").integer = True
link.add_attribute(bomb_data, 0x04, "Bomb Max Bounces", 2)
link.get_attribute("Bomb Max Bounces").integer = True
link.add_attribute(bomb_data, 0x08, "Bomb Bounce Rehit Rate", 2)
link.get_attribute("Bomb Bounce Rehit Rate").integer = True
link.add_attribute(bomb_data, 0x0C, "Bomb Explosion Flash Frames", 2)
link.get_attribute("Bomb Explosion Flash Frames").integer = True
link.add_attribute(bomb_data, 0x10, "Bomb HP", 2)
link.get_attribute("Bomb HP").integer = True
link.add_attribute(bomb_data, 0x24, "Bomb Horizontal Velocity to Detonate", 2)
link.add_attribute(bomb_data, 0x2C, "Bomb Base Launch Speed on Hit", 2)
link.add_attribute(bomb_data, 0x30, "Bomb Launch Speed Multiplier on Hit", 2)

link.article_datas = link.dat_file.get_article_data(link)
boomerang_data = link.article_datas[1]
link.add_attribute(boomerang_data, 0x00, "Boomerang Tilt Duration", 3)
link.get_attribute("Boomerang Tilt Duration").integer = True
link.add_attribute(boomerang_data, 0x04, "Boomerang Smash Duration", 3)
link.get_attribute("Boomerang Smash Duration").integer = True
link.add_attribute(boomerang_data, 0x0C, "Boomerang Launch Velocity", 3)
link.add_attribute(boomerang_data, 0x14, "Boomerang Release Angle Multiplier", 3)
link.add_attribute(boomerang_data, 0x18, "Boomerang Return Transition Smoothness", 3)
link.add_attribute(boomerang_data, 0x1C, "Boomerang Return Angle Modifier", 3)
link.add_attribute(boomerang_data, 0x20, "Boomerang Return Homing Accuracy 1", 3)
link.add_attribute(boomerang_data, 0x24, "Boomerang Return Homing Accuracy 2", 3)
link.add_attribute(boomerang_data, 0x28, "Boomerang Rebound Angle Modifier", 3)
link.add_attribute(boomerang_data, 0x2C, "Boomerang Return Acceleration", 3)
link.add_attribute(boomerang_data, 0x30, "Boomerang Spin Speed", 3)
link.add_attribute(boomerang_data, 0x38, "Boomerang Frame Delay Between SFX", 3)
link.add_attribute(boomerang_data, 0x3C, "Boomerang Trail Effect 1 Delay", 3)
link.add_attribute(boomerang_data, 0x40, "Boomerang Trail Effect 2 Delay", 3)

link.article_datas = link.dat_file.get_article_data(link)
hookshot_data = link.article_datas[2]
link.add_attribute(hookshot_data, 0x0C, "Hookshot Number of Chains", 4)
link.get_attribute("Hookshot Number of Chains").integer = True
link.add_attribute(hookshot_data, 0x10, "Hookshot Distance Between Chains", 4)
link.add_attribute(hookshot_data, 0x18, "Hookshot Chain Launch Speed", 4)
link.add_attribute(hookshot_data, 0x1C, "Hookshot Chain Gravity", 4)
link.add_attribute(hookshot_data, 0x20, "Hookshot Chain Retraction Speed", 4)
link.add_attribute(hookshot_data, 0x4C, "Hookshot Ground Length Modifier", 4)
link.add_attribute(hookshot_data, 0x50, "Hookshot Air Length Modifier", 4)

link.article_datas = link.dat_file.get_article_data(link)
arrow_data = link.article_datas[3]
link.add_attribute(arrow_data, 0x00, "Arrow Duration (Air)", 5)
link.add_attribute(arrow_data, 0x04, "Arrow Uncharged Velocity", 5)
link.add_attribute(arrow_data, 0x08, "Arrow Charged Velocity Multiplier", 5)
link.add_attribute(arrow_data, 0x0C, "Arrow Uncharged Damage", 5)
link.add_attribute(arrow_data, 0x10, "Arrow Full Charge Damage", 5)
link.add_attribute(arrow_data, 0x18, "Arrow Duration (Ground)", 5)
link.add_attribute(arrow_data, 0x1C, "Arrow Gravity", 5)
link.add_attribute(arrow_data, 0x20, "Arrow Arc Modifier (Cosmetic only)", 5)