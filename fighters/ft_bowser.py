import fighter
from iso import DAT
from structs import hitbox

bowser = fighter.Fighter("Bowser", DAT(b'PlKp.dat'))
fighter.fighters.append(bowser)
bowser.fighter_id = 0x05

bowser.good_sfx = [0x24a3d, 0x249fe, 0x24a37, 0x24a0a, 0x24a16, 0x24a04, 0x24a01, 0x24a22, 0x24a34, 0x24a31, 0x24a1f, 0x249f8, 0x24a2e]

bowser.special_attribute_block_size = 0xA0
bowser.articles_sizes = [0x18]
bowser.articles_offsets = [0x40D8]
bowser.projectile_offsets = [0x4110]

file_data = bowser.dat_file.file_data
offset = bowser.projectile_offsets[0]
flame_hitbox = hitbox.Hitbox(file_data[offset:offset+20], offset)
flame_hitbox.tags.append("projectile")
bowser.projectile_hitboxes.append(flame_hitbox)

bowser.subactions[0x106].friendly_name = "Koopa Klaw"
bowser.subactions[0x107].friendly_name = "Koopa Klaw"
bowser.subactions[0x108].friendly_name = "Koopa Klaw"
bowser.subactions[0x109].friendly_name = "Koopa Klaw"
bowser.subactions[0x116].friendly_name = "Koopa Klaw"
bowser.subactions[0x117].friendly_name = "Koopa Klaw"
bowser.subactions[0x118].friendly_name = "Koopa Klaw"
bowser.subactions[0x119].friendly_name = "Koopa Klaw"
bowser.subactions[0x11A].friendly_name = "Koopa Klaw"
bowser.subactions[0x11B].friendly_name = "Koopa Klaw"
bowser.subactions[0x12D].friendly_name = "Koopa Klaw"
bowser.subactions[0x12E].friendly_name = "Koopa Klaw"
bowser.subactions[0x12F].friendly_name = "Koopa Klaw"
bowser.subactions[0x130].friendly_name = "Koopa Klaw"
bowser.subactions[0x131].friendly_name = "Koopa Klaw"
bowser.subactions[0x132].friendly_name = "Koopa Klaw"
bowser.subactions[0x133].friendly_name = "Koopa Klaw"
bowser.subactions[0x134].friendly_name = "Koopa Klaw"
bowser.subactions[0x135].friendly_name = "Koopa Klaw"
bowser.subactions[0x136].friendly_name = "Koopa Klaw"
bowser.subactions[0x127].friendly_name = "Flame Breath"
bowser.subactions[0x128].friendly_name = "Flame Breath"
bowser.subactions[0x129].friendly_name = "Flame Breath"
bowser.subactions[0x12A].friendly_name = "Flame Breath"
bowser.subactions[0x12B].friendly_name = "Flame Breath"
bowser.subactions[0x12C].friendly_name = "Flame Breath"
bowser.subactions[0x137].friendly_name = "Whirling Fortress"
bowser.subactions[0x138].friendly_name = "Whirling Fortress"
bowser.subactions[0x139].friendly_name = "Bowser Bomb"
bowser.subactions[0x13A].friendly_name = "Bowser Bomb"
bowser.subactions[0x13B].friendly_name = "Bowser Bomb"

for action in bowser.subactions:
    if "Nameless" not in action.friendly_name:
        action.tags.append(action.friendly_name.lower().replace(" ", ""))

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
bowser.add_attribute(flame_data, 0x10, "Flame Min Angle", 2)
bowser.add_attribute(flame_data, 0x14, "Flame Max Angle", 2)

