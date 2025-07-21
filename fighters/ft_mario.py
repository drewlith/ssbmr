import fighter
from iso import DAT
from structs import hitbox

mario = fighter.Fighter("Mario", DAT(b'PlMr.dat'))
fighter.fighters.append(mario)
mario.fighter_id = 0x08

mario.special_attribute_block_size = 0x84
mario.articles_sizes = [0x14]
mario.articles_offsets = [0x3A98]
mario.projectile_offsets = [0x3ACC]

file_data = mario.dat_file.file_data
offset = mario.projectile_offsets[0]
fireball_hitbox = hitbox.Hitbox(file_data[offset:offset+20], offset)
fireball_hitbox.tags.append("projectile")
mario.projectile_hitboxes.append(fireball_hitbox)

mario.subactions[297].friendly_name = "Cape (Ground)"
mario.subactions[298].friendly_name = "Cape (Aerial)"
mario.subactions[299].friendly_name = "Super Jump Punch (Ground)"
mario.subactions[300].friendly_name = "Super Jump Punch (Aerial)"
mario.subactions[301].friendly_name = "Tornado (Ground)"
mario.subactions[302].friendly_name = "Tornado (Aerial)"

attribute_data = mario.dat_file.get_special_attribute_data(mario.special_attribute_block_size)
mario.add_attribute(attribute_data, 0x00, "Cape Horizontal Momentum", 1)
mario.add_attribute(attribute_data, 0x04, "Cape Horizontal Velocity", 1)
mario.add_attribute(attribute_data, 0x08, "Cape Vertical Momentum", 1)
mario.add_attribute(attribute_data, 0x0C, "Cape Gravity", 1)
mario.add_attribute(attribute_data, 0x10, "Cape Max Falling Speed", 1)
mario.add_attribute(attribute_data, 0x74, "Cape Reflection Bubble Size", 1)
mario.add_attribute(attribute_data, 0x78, "Cape Reflection Damage Multiplier", 1)
mario.add_attribute(attribute_data, 0x7C, "Cape Projectile Reflection Speed Multiplier", 1)
mario.add_attribute(attribute_data, 0x18, "Super Jump Punch Freefall Mobility", 1)
mario.add_attribute(attribute_data, 0x1C, "Super Jump Punch Landing Lag", 1)
mario.add_attribute(attribute_data, 0x28, "Super Jump Punch Max Angle Change", 1)
mario.add_attribute(attribute_data, 0x2C, "Super Jump Punch Initial Horizontal Momentum", 1)
mario.add_attribute(attribute_data, 0x30, "Super Jump Punch Initial Gravity", 1)
mario.add_attribute(attribute_data, 0x34, "Super Jump Punch Initial Vertical Momentum", 1)
mario.add_attribute(attribute_data, 0x38, "Tornado Grounded Rise Resistance", 1)
mario.add_attribute(attribute_data, 0x3C, "Tornado Base Air Speed", 1)
mario.add_attribute(attribute_data, 0x40, "Tornado Horizontal Velocity Limit", 1)
mario.add_attribute(attribute_data, 0x44, "Tornado Horizontal Acceleration", 1)
mario.add_attribute(attribute_data, 0x48, "Tornado Horizontal Drift", 1)
mario.add_attribute(attribute_data, 0x4C, "Tornado Deceleration Rate", 1)
mario.add_attribute(attribute_data, 0x54, "Tornado Velocity Gain From B Press", 1)
mario.add_attribute(attribute_data, 0x58, "Tornado Terminal Velocity", 1)
mario.add_attribute(attribute_data, 0x5C, "Tornado Landing Lag", 1)
mario.get_attribute("Tornado Landing Lag").integer = True

mario.article_datas = mario.dat_file.get_article_data(mario)
fireball_data = mario.article_datas[0]
mario.add_attribute(fireball_data, 0x00, "Fire Ball Initial Velocity", 2)
mario.add_attribute(fireball_data, 0x04, "Fire Ball Angle", 2)
mario.add_attribute(fireball_data, 0x08, "Fire Ball Duration", 2)
mario.add_attribute(fireball_data, 0x10, "Fire Ball Bounce Height", 2)