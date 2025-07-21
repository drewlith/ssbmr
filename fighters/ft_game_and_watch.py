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

game_and_watch.subactions[295].friendly_name = "Sausage 1"
game_and_watch.subactions[296].friendly_name = "Sausage 2"
game_and_watch.subactions[297].friendly_name = "Judgment (1) (Ground)"
game_and_watch.subactions[298].friendly_name = "Judgment (2) (Ground)"
game_and_watch.subactions[299].friendly_name = "Judgment (3) (Ground)"
game_and_watch.subactions[300].friendly_name = "Judgment (4) (Ground)"
game_and_watch.subactions[301].friendly_name = "Judgment (5) (Ground)"
game_and_watch.subactions[302].friendly_name = "Judgment (6) (Ground)"
game_and_watch.subactions[303].friendly_name = "Judgment (7) (Ground)"
game_and_watch.subactions[304].friendly_name = "Judgment (8) (Ground)"
game_and_watch.subactions[305].friendly_name = "Judgment (9) (Ground)"
game_and_watch.subactions[306].friendly_name = "Judgment (1) (Aerial)"
game_and_watch.subactions[307].friendly_name = "Judgment (2) (Aerial)"
game_and_watch.subactions[308].friendly_name = "Judgment (3) (Aerial)"
game_and_watch.subactions[309].friendly_name = "Judgment (4) (Aerial)"
game_and_watch.subactions[310].friendly_name = "Judgment (5) (Aerial)"
game_and_watch.subactions[311].friendly_name = "Judgment (6) (Aerial)"
game_and_watch.subactions[312].friendly_name = "Judgment (7) (Aerial)"
game_and_watch.subactions[313].friendly_name = "Judgment (8) (Aerial)"
game_and_watch.subactions[314].friendly_name = "Judgment (9) (Aerial)"
game_and_watch.subactions[315].friendly_name = "Fire!"

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