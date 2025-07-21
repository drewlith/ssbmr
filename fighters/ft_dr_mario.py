import fighter
from iso import DAT
from structs import hitbox

dr_mario = fighter.Fighter("Dr. Mario", DAT(b'PlDr.dat'))
fighter.fighters.append(dr_mario)
dr_mario.fighter_id = 0x16

dr_mario.special_attribute_block_size = 0x84
dr_mario.articles_sizes = [0x14]
dr_mario.articles_offsets = [0x3BD4]
dr_mario.projectile_offsets = [0x3C08]

file_data = dr_mario.dat_file.file_data
offset = dr_mario.projectile_offsets[0]
vitamin_hitbox = hitbox.Hitbox(file_data[offset:offset+20], offset)
vitamin_hitbox.tags.append("projectile")
dr_mario.projectile_hitboxes.append(vitamin_hitbox)

dr_mario.subactions[297].friendly_name = "Super Sheet"
dr_mario.subactions[299].friendly_name = "Super Jump Punch (Ground)"
dr_mario.subactions[300].friendly_name = "Super Jump Punch (Aerial)"
dr_mario.subactions[301].friendly_name = "Dr. Tornado (Ground)"
dr_mario.subactions[302].friendly_name = "Dr. Tornado (Aerial)"

attribute_data = dr_mario.dat_file.get_special_attribute_data(dr_mario.special_attribute_block_size)
dr_mario.add_attribute(attribute_data, 0x00, "Super Sheet Horizontal Momentum", 1)
dr_mario.add_attribute(attribute_data, 0x04, "Super Sheet Horizontal Velocity", 1)
dr_mario.add_attribute(attribute_data, 0x08, "Super Sheet Vertical Momentum", 1)
dr_mario.add_attribute(attribute_data, 0x0C, "Super Sheet Gravity", 1)
dr_mario.add_attribute(attribute_data, 0x10, "Super Sheet Max Falling Speed", 1)
dr_mario.add_attribute(attribute_data, 0x74, "Super Sheet Reflection Bubble Size", 1)
dr_mario.add_attribute(attribute_data, 0x78, "Super Sheet Reflection Damage Multiplier", 1)
dr_mario.add_attribute(attribute_data, 0x7C, "Super Sheet Projectile Reflection Speed Multiplier", 1)
dr_mario.add_attribute(attribute_data, 0x18, "Super Jump Punch Freefall Mobility", 1)
dr_mario.add_attribute(attribute_data, 0x1C, "Super Jump Punch Landing Lag", 1)
dr_mario.add_attribute(attribute_data, 0x28, "Super Jump Punch Max Angle Change", 1)
dr_mario.add_attribute(attribute_data, 0x2C, "Super Jump Punch Initial Horizontal Momentum", 1)
dr_mario.add_attribute(attribute_data, 0x30, "Super Jump Punch Initial Gravity", 1)
dr_mario.add_attribute(attribute_data, 0x34, "Super Jump Punch Initial Vertical Momentum", 1)
dr_mario.add_attribute(attribute_data, 0x38, "Dr. Tornado Grounded Rise Resistance", 1)
dr_mario.add_attribute(attribute_data, 0x3C, "Dr. Tornado Base Air Speed", 1)
dr_mario.add_attribute(attribute_data, 0x40, "Dr. Tornado Horizontal Velocity Limit", 1)
dr_mario.add_attribute(attribute_data, 0x44, "Dr. Tornado Horizontal Acceleration", 1)
dr_mario.add_attribute(attribute_data, 0x48, "Dr. Tornado Horizontal Drift", 1)
dr_mario.add_attribute(attribute_data, 0x4C, "Dr. Tornado Deceleration Rate", 1)
dr_mario.add_attribute(attribute_data, 0x54, "Dr. Tornado Velocity Gain From B Press", 1)
dr_mario.add_attribute(attribute_data, 0x58, "Dr. Tornado Terminal Velocity", 1)
dr_mario.add_attribute(attribute_data, 0x5C, "Dr. Tornado Landing Lag", 1)
dr_mario.get_attribute("Dr. Tornado Landing Lag").integer = True

dr_mario.article_datas = dr_mario.dat_file.get_article_data(dr_mario)
vitamin_data = dr_mario.article_datas[0]
dr_mario.add_attribute(vitamin_data, 0x00, "Megavitamin Initial Velocity", 2)
dr_mario.add_attribute(vitamin_data, 0x04, "Megavitamin Angle", 2)
dr_mario.add_attribute(vitamin_data, 0x08, "Megavitamin Duration", 2)
dr_mario.add_attribute(vitamin_data, 0x10, "Megavitamin Bounce Height", 2)