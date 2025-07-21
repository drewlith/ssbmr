import fighter
from iso import DAT
from structs import hitbox

yoshi = fighter.Fighter("Yoshi", DAT(b'PlYs.dat'))
fighter.fighters.append(yoshi)
yoshi.fighter_id = 0x11

yoshi.special_attribute_block_size = 0x138
yoshi.articles_sizes = [0x8, 0x8]
yoshi.articles_offsets = [0x3A68, 0x3B4C]
yoshi.projectile_offsets = [0x3A90, 0x3B74]

file_data = yoshi.dat_file.file_data
offset = yoshi.projectile_offsets[0]
egg_hitbox = hitbox.Hitbox(file_data[offset:offset+20], offset)
egg_hitbox.tags.append("projectile")
yoshi.projectile_hitboxes.append(egg_hitbox)

offset = yoshi.projectile_offsets[1]
stars_hitbox = hitbox.Hitbox(file_data[offset:offset+20], offset)
stars_hitbox.tags.append("projectile")
yoshi.projectile_hitboxes.append(stars_hitbox)

yoshi.subactions[302].friendly_name = "Egg Roll"
yoshi.subactions[307].friendly_name = "Egg Roll"
yoshi.subactions[310].friendly_name = "Ground Pound"
yoshi.subactions[311].friendly_name = "Ground Pound"
yoshi.subactions[313].friendly_name = "Ground Pound"

attribute_data = yoshi.dat_file.get_special_attribute_data(yoshi.special_attribute_block_size)
yoshi.add_attribute(attribute_data, 0x0, "Flutter Jump Turn Duration", 1)
yoshi.get_attribute("Flutter Jump Turn Duration").integer = True
yoshi.add_attribute(attribute_data, 0x8, "Flutter Jump Super Armor", 1)
yoshi.add_attribute(attribute_data, 0x10, "Egg Lay Horizontal Momentum", 1)
yoshi.add_attribute(attribute_data, 0x14, "Egg Lay Vertical Momentum", 1)
yoshi.add_attribute(attribute_data, 0x18, "Egg Lay Damage Multiplier", 1)
yoshi.add_attribute(attribute_data, 0x20, "Egg Lay Growth Time", 1)
yoshi.add_attribute(attribute_data, 0x24, "Egg Lay Base Duration", 1)
yoshi.add_attribute(attribute_data, 0x28, "Egg Lay Breakout Resistance", 1)
yoshi.add_attribute(attribute_data, 0x2C, "Egg Lay Wiggle Out", 1)
yoshi.add_attribute(attribute_data, 0x38, "Egg Lay Release Intangibility", 1)
yoshi.get_attribute("Egg Lay Release Intangibility").integer = True
yoshi.add_attribute(attribute_data, 0x3C, "Egg Lay Break Out Horizontal Velocity", 1)
yoshi.add_attribute(attribute_data, 0x40, "Egg Lay Break Out Vertical Velocity", 1)
yoshi.add_attribute(attribute_data, 0x48, "Egg Roll Max Duration", 1)
yoshi.get_attribute("Egg Roll Max Duration").integer = True
yoshi.add_attribute(attribute_data, 0x4C, "Egg Roll Minimum Duration", 1)
yoshi.get_attribute("Egg Roll Minimum Duration").integer = True
yoshi.add_attribute(attribute_data, 0x50, "Egg Roll Duration Subtraction on Hit", 1)
yoshi.get_attribute("Egg Roll Duration Subtraction on Hit").integer = True
yoshi.add_attribute(attribute_data, 0x58, "Egg Roll Horizontal Momentum", 1)
yoshi.add_attribute(attribute_data, 0x5C, "Egg Roll Vertical Momentum", 1)
yoshi.add_attribute(attribute_data, 0x60, "Egg Roll Spin Intensity", 1)
yoshi.add_attribute(attribute_data, 0x64, "Egg Roll First Land Momentum", 1)
yoshi.add_attribute(attribute_data, 0x68, "Egg Roll Smash Momentum Multiplier", 1)
yoshi.add_attribute(attribute_data, 0x6C, "Egg Roll Gravity", 1)
yoshi.add_attribute(attribute_data, 0x70, "Egg Roll Ending Gravity", 1)
yoshi.add_attribute(attribute_data, 0x74, "Egg Roll Accleration", 1)
yoshi.add_attribute(attribute_data, 0x7C, "Egg Roll Speed Modifier", 1)
yoshi.add_attribute(attribute_data, 0x8C, "Egg Roll Damage From Speed Modifier", 1)
yoshi.add_attribute(attribute_data, 0x90, "Egg Roll Air Acceleration", 1)
yoshi.add_attribute(attribute_data, 0x94, "Egg Roll Smash Window Ground", 1)
yoshi.add_attribute(attribute_data, 0x98, "Egg Roll Smash Window Air", 1)
yoshi.add_attribute(attribute_data, 0xA0, "Egg Roll Spin On Turn Modifier", 1)
yoshi.add_attribute(attribute_data, 0xAC, "Egg Roll Horizontal Recoil", 1)
yoshi.add_attribute(attribute_data, 0xB0, "Egg Roll Vertical Recoil", 1)
yoshi.add_attribute(attribute_data, 0xB4, "Egg Roll Velocity Mod On Recoil", 1)
yoshi.add_attribute(attribute_data, 0xB8, "Egg Roll Friction", 1)
yoshi.add_attribute(attribute_data, 0xBC, "Egg Roll Boost on Landing", 1)
yoshi.add_attribute(attribute_data, 0xC0, "Egg Roll Damage Modifier", 1)
yoshi.add_attribute(attribute_data, 0xC4, "Egg Roll Damage Ratio", 1)
yoshi.add_attribute(attribute_data, 0xCC, "Egg Roll Aerial Damage Reduction", 1)
yoshi.add_attribute(attribute_data, 0xD0, "Egg Roll Aerial Ending Acceleration", 1)
yoshi.add_attribute(attribute_data, 0xD4, "Egg Roll Acceleration Variable 1", 1)
yoshi.add_attribute(attribute_data, 0xD8, "Egg Roll Acceleration Variable 2", 1)
yoshi.add_attribute(attribute_data, 0xE0, "Egg Roll Ending Horizontal Velocity", 1)
yoshi.add_attribute(attribute_data, 0xE8, "Egg Roll Landing Lag", 1)
yoshi.add_attribute(attribute_data, 0xEC, "Egg Throw Angle Variable 1", 1)
yoshi.add_attribute(attribute_data, 0xF0, "Egg Throw Angle Variable 2", 1)
yoshi.add_attribute(attribute_data, 0xF4, "Egg Throw Angle Variable 3", 1)
yoshi.add_attribute(attribute_data, 0xF8, "Egg Throw Angle Variable 4", 1)
yoshi.add_attribute(attribute_data, 0xFC, "Egg Throw Base Launch Speed", 1)
yoshi.add_attribute(attribute_data, 0x100, "Egg Throw Launch Speed B Press Modifier", 1)
yoshi.add_attribute(attribute_data, 0x104, "Egg Throw X-Offset", 1)
yoshi.add_attribute(attribute_data, 0x108, "Egg Throw Y-Offset", 1)
yoshi.add_attribute(attribute_data, 0x110, "Egg Throw Spin Intensity", 1)
yoshi.add_attribute(attribute_data, 0x114, "Ground Pound Descent Speed", 1)
yoshi.add_attribute(attribute_data, 0x118, "Ground Pound Star X-Offset", 1)
yoshi.add_attribute(attribute_data, 0x11C, "Ground Pound Star Y-Offset", 1)
yoshi.add_attribute(attribute_data, 0x124, "Tongue Minimum Pull Speed", 1)
yoshi.add_attribute(attribute_data, 0x128, "Tongue Max Pull Speed", 1)

yoshi.article_datas = yoshi.dat_file.get_article_data(yoshi)
egg_data = yoshi.article_datas[0]
yoshi.add_attribute(egg_data, 0x00, "Egg Duration", 2)
star_data = yoshi.article_datas[1]
yoshi.add_attribute(star_data, 0x00, "Star Velocity", 3)
yoshi.add_attribute(star_data, 0x04, "Star Acceleration", 3)