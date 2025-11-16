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

dr_mario.good_sfx = [0x15fd2, 0x15fb7, 0x15fcf, 0x15fde, 0x15fe1, 0x15fc9, 0x15fb4, 0x15f9c, 0x15fab, 0x15fa2, 0x15fa5]

file_data = dr_mario.dat_file.file_data
offset = dr_mario.projectile_offsets[0]
vitamin_hitbox = hitbox.Hitbox(file_data[offset:offset+20], offset)
vitamin_hitbox.tags.append("projectile")
dr_mario.projectile_hitboxes.append(vitamin_hitbox)

dr_mario.subactions[0x127].friendly_name = "Megavitamin"
dr_mario.subactions[0x128].friendly_name = "Megavitamin"
dr_mario.subactions[0x129].friendly_name = "Super Sheet"
dr_mario.subactions[0x12A].friendly_name = "Super Sheet"
dr_mario.subactions[0x12B].friendly_name = "Super Jump Punch"
dr_mario.subactions[0x12C].friendly_name = "Super Jump Punch"
dr_mario.subactions[0x12D].friendly_name = "Dr Tornado"
dr_mario.subactions[0x12E].friendly_name = "Dr Tornado"

for action in dr_mario.subactions:
    if "Nameless" not in action.friendly_name:
        action.tags.append(action.friendly_name.lower().replace(" ", ""))

attribute_data = dr_mario.dat_file.get_special_attribute_data(dr_mario.special_attribute_block_size)
dr_mario.add_attribute(attribute_data, 0x00, "Super Sheet Horizontal Momentum", 1)
dr_mario.add_attribute(attribute_data, 0x04, "Super Sheet Horizontal Velocity", 1)
dr_mario.add_attribute(attribute_data, 0x08, "Super Sheet Vertical Momentum", 1)
dr_mario.add_attribute(attribute_data, 0x0C, "Super Sheet Gravity", 1)
dr_mario.add_attribute(attribute_data, 0x10, "Super Sheet Max Falling Speed", 1)
dr_mario.add_attribute(attribute_data, 0x74, "Super Sheet Reflection Bubble Size", 1)
dr_mario.add_attribute(attribute_data, 0x78, "Super Sheet Reflection Damage Multiplier", 1)
dr_mario.add_attribute(attribute_data, 0x7C, "Super Sheet Projectile Reflection Speed Multiplier", 1)
dr_mario.add_attribute(attribute_data, 0x18, "Dr Jump Punch Freefall Mobility", 1)
dr_mario.add_attribute(attribute_data, 0x1C, "Dr Jump Punch Landing Lag", 1)
dr_mario.add_attribute(attribute_data, 0x28, "Dr Jump Punch Max Angle Change", 1)
dr_mario.add_attribute(attribute_data, 0x2C, "Dr Jump Punch Initial Horizontal Momentum", 1)
dr_mario.add_attribute(attribute_data, 0x30, "Dr Jump Punch Initial Gravity", 1)
dr_mario.add_attribute(attribute_data, 0x34, "Dr Jump Punch Initial Vertical Momentum", 1)
dr_mario.add_attribute(attribute_data, 0x38, "Dr Tornado Grounded Rise Resistance", 1)
dr_mario.add_attribute(attribute_data, 0x3C, "Dr Tornado Base Air Speed", 1)
dr_mario.add_attribute(attribute_data, 0x40, "Dr Tornado Horizontal Velocity Limit", 1)
dr_mario.add_attribute(attribute_data, 0x44, "Dr Tornado Horizontal Acceleration", 1)
dr_mario.add_attribute(attribute_data, 0x48, "Dr Tornado Horizontal Drift", 1)
dr_mario.add_attribute(attribute_data, 0x4C, "Dr Tornado Deceleration Rate", 1)
dr_mario.add_attribute(attribute_data, 0x54, "Dr Tornado Velocity Gain From B Press", 1)
dr_mario.add_attribute(attribute_data, 0x58, "Dr Tornado Terminal Velocity", 1)
dr_mario.add_attribute(attribute_data, 0x5C, "Dr Tornado Landing Lag", 1)
dr_mario.get_attribute("Dr Tornado Landing Lag").integer = True

dr_mario.article_datas = dr_mario.dat_file.get_article_data(dr_mario)
vitamin_data = dr_mario.article_datas[0]
dr_mario.add_attribute(vitamin_data, 0x00, "Megavitamin Initial Velocity", 2)
dr_mario.add_attribute(vitamin_data, 0x04, "Megavitamin Angle", 2)
dr_mario.add_attribute(vitamin_data, 0x08, "Megavitamin Duration", 2)
dr_mario.add_attribute(vitamin_data, 0x10, "Megavitamin Bounce Height", 2)