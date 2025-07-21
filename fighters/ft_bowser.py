import fighter
from iso import DAT
from structs import hitbox

bowser = fighter.Fighter("Bowser", DAT(b'PlKp.dat'))
fighter.fighters.append(bowser)
bowser.fighter_id = 0x05

bowser.special_attribute_block_size = 0xA0
bowser.articles_sizes = [0x18]
bowser.articles_offsets = [0x40B8]
bowser.projectile_offsets = [0x4110]

file_data = bowser.dat_file.file_data
offset = bowser.projectile_offsets[0]
flame_hitbox = hitbox.Hitbox(file_data[offset:offset+20], offset)
flame_hitbox.tags.append("projectile")
bowser.projectile_hitboxes.append(flame_hitbox)

bowser.subactions[301].friendly_name = "Koopa Klaw"
bowser.subactions[311].friendly_name = "Whirling Fortress (Ground)"
bowser.subactions[312].friendly_name = "Whirling Fortress (Air)"
bowser.subactions[313].friendly_name = "Bowser Bomb (Ground)"
bowser.subactions[314].friendly_name = "Bowser Bomb (Air)"
bowser.subactions[304].friendly_name = "Koopa Klaw Forward Throw (Ground)"
bowser.subactions[305].friendly_name = "Koopa Klaw Back Throw (Ground)"
bowser.subactions[309].friendly_name = "Koopa Klaw Forward Throw (Air)"
bowser.subactions[310].friendly_name = "Koopa Klaw Back Throw (Air)"

attribute_data = bowser.dat_file.get_special_attribute_data(bowser.special_attribute_block_size)
bowser.add_attribute(attribute_data, 0x00, "Passive Super Armor", 1)
bowser.add_attribute(attribute_data, 0x08, "Flame Breath Recharge Rate: Fuel", 1)
bowser.add_attribute(attribute_data, 0x0C, "Flame Breath Recharge Rate: Flame Size", 1)
bowser.add_attribute(attribute_data, 0x10, "Flame Breath Max Fuel", 1)
bowser.add_attribute(attribute_data, 0x2C, "Koopa Klaw Bite Damage", 1)
bowser.get_attribute("Koopa Klaw Bite Damage").integer = True
bowser.add_attribute(attribute_data, 0x4C, "Koopa Klaw Grab Duration", 1)
bowser.add_attribute(attribute_data, 0x54, "Whirling Fortress Aerial Vertical Momentum", 1)
bowser.add_attribute(attribute_data, 0x58, "Whirling Fortress Gravity", 1)
bowser.add_attribute(attribute_data, 0x5C, "Whirling Fortress Aerial Vertical Momentum 2nd Half", 1)
bowser.add_attribute(attribute_data, 0x60, "Whirling Fortress Ground Speed", 1)
bowser.add_attribute(attribute_data, 0x64, "Whirling Fortress Momentum Preservation", 1)
bowser.add_attribute(attribute_data, 0x68, "Whirling Fortress Grounded Turning Speed", 1)
bowser.add_attribute(attribute_data, 0x6C, "Whirling Fortress Aerial Mobility", 1)
bowser.add_attribute(attribute_data, 0x7C, "Whirling Fortress Landing Lag", 1)
bowser.add_attribute(attribute_data, 0x80, "Bowser Bomb Aerial Horizontal Momentum Multiplier", 1)
bowser.add_attribute(attribute_data, 0x84, "Bowser Bomb Initial Aerial Vertical Momentum", 1)
bowser.add_attribute(attribute_data, 0x88, "Bowser Bomb Horizontal Momentum Preservation", 1)
bowser.add_attribute(attribute_data, 0x8C, "Bowser Bomb Vertical Momentum Deceleration Rate", 1)
bowser.add_attribute(attribute_data, 0x90, "Bowser Bomb Gravity Scale", 1)
bowser.add_attribute(attribute_data, 0x94, "Bowser Bomb Descent Speed", 1)

bowser.article_datas = bowser.dat_file.get_article_data(bowser)
flame_data = bowser.article_datas[0]
bowser.add_attribute(flame_data, 0x08, "Flame Velocity", 2)
bowser.add_attribute(flame_data, 0x0C, "Flame Acceleration", 2)
bowser.add_attribute(flame_data, 0x10, "Flame Min. Angle", 2)
bowser.add_attribute(flame_data, 0x14, "Flame Max Angle", 2)

