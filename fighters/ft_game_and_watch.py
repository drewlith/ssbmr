import fighter
from iso import DAT
from structs import hitbox

game_and_watch = fighter.Fighter("Mr. Game & Watch", DAT(b'PlGw.dat'))
fighter.fighters.append(game_and_watch)
game_and_watch.fighter_id = 0x03

game_and_watch.special_attribute_block_size = 0x94
game_and_watch.articles_sizes = [0x74]
game_and_watch.articles_offsets = [0x4378]
game_and_watch.projectile_offsets = [0x440C]

file_data = game_and_watch.dat_file.file_data
offset = game_and_watch.projectile_offsets[0]
sausage_hitbox = hitbox.Hitbox(file_data[offset:offset+20], offset)
sausage_hitbox.tags.append("projectile")
game_and_watch.projectile_hitboxes.append(sausage_hitbox)

game_and_watch.subactions[0x127].friendly_name = "Sausage"
game_and_watch.subactions[0x128].friendly_name = "Sausage"
game_and_watch.subactions[0x129].friendly_name = "Judgment 1"
game_and_watch.subactions[0x12A].friendly_name = "Judgment 2"
game_and_watch.subactions[0x12B].friendly_name = "Judgment 3"
game_and_watch.subactions[0x12C].friendly_name = "Judgment 4"
game_and_watch.subactions[0x12D].friendly_name = "Judgment 5"
game_and_watch.subactions[0x12E].friendly_name = "Judgment 6"
game_and_watch.subactions[0x12F].friendly_name = "Judgment 7"
game_and_watch.subactions[0x130].friendly_name = "Judgment 8"
game_and_watch.subactions[0x131].friendly_name = "Judgment 9"
game_and_watch.subactions[0x132].friendly_name = "Judgment 1"
game_and_watch.subactions[0x133].friendly_name = "Judgment 2"
game_and_watch.subactions[0x134].friendly_name = "Judgment 3"
game_and_watch.subactions[0x135].friendly_name = "Judgment 4"
game_and_watch.subactions[0x136].friendly_name = "Judgment 5"
game_and_watch.subactions[0x137].friendly_name = "Judgment 6"
game_and_watch.subactions[0x138].friendly_name = "Judgment 7"
game_and_watch.subactions[0x139].friendly_name = "Judgment 8"
game_and_watch.subactions[0x13A].friendly_name = "Judgment 9"
game_and_watch.subactions[0x13B].friendly_name = "Fire!"
game_and_watch.subactions[0x13C].friendly_name = "Fire!"
game_and_watch.subactions[0x13D].friendly_name = "Oil Panic"
game_and_watch.subactions[0x13E].friendly_name = "Oil Panic"
game_and_watch.subactions[0x13F].friendly_name = "Oil Panic"
game_and_watch.subactions[0x140].friendly_name = "Oil Panic"
game_and_watch.subactions[0x141].friendly_name = "Oil Panic"
game_and_watch.subactions[0x142].friendly_name = "Oil Panic"

for action in game_and_watch.subactions:
    if "Nameless" not in action.friendly_name:
        action.tags.append(action.friendly_name.lower().replace(" ", ""))

attribute_data = game_and_watch.dat_file.get_special_attribute_data(game_and_watch.special_attribute_block_size)
game_and_watch.add_attribute(attribute_data, 0x0, "Model Width", 1)
game_and_watch.add_attribute(attribute_data, 0x18, "Chef Multi Hit Begin Frame", 1)
game_and_watch.add_attribute(attribute_data, 0x1C, "Chef Max Sausages", 1)
game_and_watch.add_attribute(attribute_data, 0x20, "Judgment Momentum Preservation", 1)
game_and_watch.add_attribute(attribute_data, 0x24, "Judgment Momentum Preservation Modifier", 1)
game_and_watch.add_attribute(attribute_data, 0x58, "Fire! Launch Angle Modifier", 1)
game_and_watch.add_attribute(attribute_data, 0x5C, "Fire! Launch Angle Max Difference", 1)
game_and_watch.add_attribute(attribute_data, 0x60, "Fire! Landing Lag", 1)
game_and_watch.add_attribute(attribute_data, 0x64, "Oil Panic Momentum Preservation", 1)
game_and_watch.add_attribute(attribute_data, 0x68, "Oil Panic Momentum Preservation Modifier", 1)
game_and_watch.add_attribute(attribute_data, 0x6C, "Oil Panic Fall acceleration", 1)
game_and_watch.add_attribute(attribute_data, 0x74, "Oil Panic Base Damage", 1)
game_and_watch.add_attribute(attribute_data, 0x78, "Oil Panic Damage Multiplier", 1)
game_and_watch.add_attribute(attribute_data, 0x90, "Oil Panic Absorption Bubble Size", 1)

game_and_watch.article_datas = game_and_watch.dat_file.get_article_data(game_and_watch)
sausage_data = game_and_watch.article_datas[0]
game_and_watch.add_attribute(sausage_data, 0x4, "Sausage Wall Bounce Multiplier", 2)
game_and_watch.add_attribute(sausage_data, 0x8, "Sausage Duration", 2)
game_and_watch.add_attribute(sausage_data, 0x10, "Sausage 1 Horizontal Velocity", 2)
game_and_watch.add_attribute(sausage_data, 0x14, "Sausage 1 Vertical Velocity", 2)
game_and_watch.add_attribute(sausage_data, 0x18, "Sausage 1 Gravity Velocity", 2)
game_and_watch.add_attribute(sausage_data, 0x1C, "Sausage 1 Spin Intensity", 2)
game_and_watch.add_attribute(sausage_data, 0x20, "Sausage 1 Spin Intensity Multiplier", 2)
game_and_watch.add_attribute(sausage_data, 0x24, "Sausage 2 Horizontal Velocity", 2)
game_and_watch.add_attribute(sausage_data, 0x28, "Sausage 2 Vertical Velocity", 2)
game_and_watch.add_attribute(sausage_data, 0x2C, "Sausage 2 Gravity Velocity", 2)
game_and_watch.add_attribute(sausage_data, 0x30, "Sausage 2 Spin Intensity", 2)
game_and_watch.add_attribute(sausage_data, 0x34, "Sausage 2 Spin Intensity Multiplier", 2)
game_and_watch.add_attribute(sausage_data, 0x38, "Sausage 3 Horizontal Velocity", 2)
game_and_watch.add_attribute(sausage_data, 0x3C, "Sausage 3 Vertical Velocity", 2)
game_and_watch.add_attribute(sausage_data, 0x40, "Sausage 3 Gravity Velocity", 2)
game_and_watch.add_attribute(sausage_data, 0x44, "Sausage 3 Spin Intensity", 2)
game_and_watch.add_attribute(sausage_data, 0x48, "Sausage 3 Spin Intensity Multiplier", 2)
game_and_watch.add_attribute(sausage_data, 0x4C, "Sausage 4 Horizontal Velocity", 2)
game_and_watch.add_attribute(sausage_data, 0x50, "Sausage 4 Vertical Velocity", 2)
game_and_watch.add_attribute(sausage_data, 0x54, "Sausage 4 Gravity Velocity", 2)
game_and_watch.add_attribute(sausage_data, 0x58, "Sausage 4 Spin Intensity", 2)
game_and_watch.add_attribute(sausage_data, 0x5C, "Sausage 4 Spin Intensity Multiplier", 2)
game_and_watch.add_attribute(sausage_data, 0x60, "Sausage 5 Horizontal Velocity", 2)
game_and_watch.add_attribute(sausage_data, 0x64, "Sausage 5 Vertical Velocity", 2)
game_and_watch.add_attribute(sausage_data, 0x68, "Sausage 5 Gravity Velocity", 2)
game_and_watch.add_attribute(sausage_data, 0x6C, "Sausage 5 Spin Intensity", 2)
game_and_watch.add_attribute(sausage_data, 0x70, "Sausage 5 Spin Intensity Multiplier", 2)