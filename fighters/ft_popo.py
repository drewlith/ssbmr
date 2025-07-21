import fighter
from iso import DAT
from structs import hitbox

popo = fighter.Fighter("Popo", DAT(b'PlPp.dat'))
fighter.fighters.append(popo)
popo.fighter_id = 0x0E

popo.special_attribute_block_size = 0x15C
popo.articles_sizes = [0x34, 0x18, 0x24]
popo.articles_offsets = [0x3ADC, 0x3BB0, 0x3CA0]
popo.projectile_offsets = [0x3B30]

file_data = popo.dat_file.file_data
offset = popo.projectile_offsets[0]
iceshot_hitbox = hitbox.Hitbox(file_data[offset:offset+20], offset)
iceshot_hitbox.tags.append("projectile")
popo.projectile_hitboxes.append(iceshot_hitbox)

popo.subactions[295].friendly_name = "Ice Shot"

attribute_data = popo.dat_file.get_special_attribute_data(popo.special_attribute_block_size)
popo.add_attribute(attribute_data, 0x00, "Spawn Offset", 1)
popo.add_attribute(attribute_data, 0x04, "Ice Shot Aerial Vertical Momentum", 1)
popo.add_attribute(attribute_data, 0x08, "Ice Shot Landing Lag", 1)
popo.add_attribute(attribute_data, 0x0C, "Ice Shot Spawn X-Offset", 1)
popo.add_attribute(attribute_data, 0x10, "Ice Shot Spawn Y-Offset", 1)
popo.add_attribute(attribute_data, 0x20, "Squall Hammer Height Gain From B", 1)
popo.add_attribute(attribute_data, 0x24, "Squall Hammer Base Vertical Velocity", 1)
popo.add_attribute(attribute_data, 0x2C, "Squall Hammer Initial Horizontal Velocity", 1)
popo.add_attribute(attribute_data, 0x30, "Squall Hammer Slope Angle Modifier", 1)
popo.add_attribute(attribute_data, 0x34, "Squall Hammer Aerial Horizontal Mobility", 1)
popo.add_attribute(attribute_data, 0x38, "Squall Hammer Ground Horizontal Mobility", 1)
popo.add_attribute(attribute_data, 0x3C, "Squall Hammer Momentum Gain From B", 1)
popo.add_attribute(attribute_data, 0x44, "Squall Hammer Horizontal Wall Bounce", 1)
popo.add_attribute(attribute_data, 0x48, "Squall Hammer Vertical Wall Bounce", 1)
popo.add_attribute(attribute_data, 0x4C, "Squall Hammer Solo Gravity", 1)
popo.add_attribute(attribute_data, 0x50, "Squall Hammer Duo Gravity", 1)
popo.add_attribute(attribute_data, 0x54, "Squall Hammer Solo Terminal Velocity", 1)
popo.add_attribute(attribute_data, 0x58, "Squall Hammer Duo Terminal Velocity", 1)
popo.add_attribute(attribute_data, 0x5C, "Squall Hammer Duration of Modified Gravity", 1)
popo.add_attribute(attribute_data, 0x60, "Squall Hammer Uphill Friction", 1)
popo.add_attribute(attribute_data, 0x64, "Squall Hammer Aerial Initial Horizontal Velocity", 1)
popo.add_attribute(attribute_data, 0x6C, "Squall Hammer Ground Friction", 1)
popo.add_attribute(attribute_data, 0x70, "Squall Hammer Landing Lag", 1)
popo.add_attribute(attribute_data, 0x74, "Belay Freefall Air Speed Multiplier", 1)
popo.add_attribute(attribute_data, 0x78, "Belay Landing Lag", 1)
popo.add_attribute(attribute_data, 0x84, "Belay Horizontal Velocity Deceleration", 1)
popo.add_attribute(attribute_data, 0x8C, "Belay Fall Acceleration", 1)
popo.add_attribute(attribute_data, 0x94, "Belay Duo Positive Vertical Momentum", 1)
popo.add_attribute(attribute_data, 0x98, "Belay Duo Negative Vertical Momentum", 1)
popo.add_attribute(attribute_data, 0x9C, "Belay Gravity", 1)
popo.add_attribute(attribute_data, 0xA0, "Belay Terminal Velocity", 1)
popo.add_attribute(attribute_data, 0xA4, "Belay Solo Climber Vertical Momentum", 1)
popo.add_attribute(attribute_data, 0xA8, "Belay Solo Climber Gravity", 1)
popo.add_attribute(attribute_data, 0xAC, "Belay Solo Climber Terminal Velocity", 1)
popo.add_attribute(attribute_data, 0xB0, "Belay Air Mobility Multiplier", 1)
popo.add_attribute(attribute_data, 0xB4, "Belay Air Speed Multiplier", 1)
popo.add_attribute(attribute_data, 0xB8, "Blizzard Delay Between Shots", 1)
popo.add_attribute(attribute_data, 0xBC, "Blizzard Hitboxes X Offset", 1)
popo.add_attribute(attribute_data, 0xC0, "Blizzard Hitboxes Y Offset", 1)
popo.add_attribute(attribute_data, 0xDC, "CPU Squall Hammer Height Gain From B", 1)
popo.add_attribute(attribute_data, 0xE0, "CPU Squall Hammer Base Vertical Velocity", 1)
popo.add_attribute(attribute_data, 0xE8, "CPU Squall Hammer Initial Horizontal Velocity", 1)
popo.add_attribute(attribute_data, 0xEC, "CPU Squall Hammer Slope Angle Modifier", 1)
popo.add_attribute(attribute_data, 0xF0, "CPU Squall Hammer Aerial Horizontal Mobility", 1)
popo.add_attribute(attribute_data, 0xF4, "CPU Squall Hammer Ground Horizontal Mobility", 1)
popo.add_attribute(attribute_data, 0xF8, "CPU Squall Hammer Momentum Gain From B", 1)
popo.add_attribute(attribute_data, 0x100, "CPU Squall Hammer Horizontal Wall Bounce", 1)
popo.add_attribute(attribute_data, 0x104, "CPU Squall Hammer Vertical Wall Bounce", 1)
popo.add_attribute(attribute_data, 0x108, "CPU Squall Hammer Solo Gravity", 1)
popo.add_attribute(attribute_data, 0x10C, "CPU Squall Hammer Duo Gravity", 1)
popo.add_attribute(attribute_data, 0x110, "CPU Squall Hammer Solo Terminal Velocity", 1)
popo.add_attribute(attribute_data, 0x114, "CPU Squall Hammer Duo Terminal Velocity", 1)
popo.add_attribute(attribute_data, 0x118, "CPU Squall Hammer Duration of Modified Gravity", 1)
popo.add_attribute(attribute_data, 0x11C, "CPU Squall Hammer Uphill Friction", 1)
popo.add_attribute(attribute_data, 0x120, "CPU Squall Hammer Aerial Initial Horizontal Velocity", 1)
popo.add_attribute(attribute_data, 0x128, "CPU Squall Hammer Traction", 1)
popo.add_attribute(attribute_data, 0x12C, "CPU Squall Hammer Landing Lag", 1)
popo.add_attribute(attribute_data, 0x130, "CPU Belay Freefall Air Speed Multiplier", 1)
popo.add_attribute(attribute_data, 0x134, "CPU Belay Landing Lag", 1)
popo.add_attribute(attribute_data, 0x13C, "CPU Belay Horizontal Velocity Deceleration", 1)
popo.add_attribute(attribute_data, 0x144, "CPU Belay Gravity", 1)
popo.add_attribute(attribute_data, 0x148, "CPU Belay Terminal Velocity", 1)
popo.add_attribute(attribute_data, 0x14C, "CPU Belay Solo Climber Vertical Momentum", 1)

popo.article_datas = popo.dat_file.get_article_data(popo)
iceshot_data = popo.article_datas[0]
popo.add_attribute(iceshot_data, 0x0, "Ice Shot Duration", 2)
popo.add_attribute(iceshot_data, 0x10, "Ice Shot Speed", 2)
popo.add_attribute(iceshot_data, 0x24, "Ice Shot Gravity", 2)

blizzard_data = popo.article_datas[1]
popo.add_attribute(blizzard_data, 0x0, "Blizzard Hitbox Duration", 3)
popo.add_attribute(blizzard_data, 0x4, "Blizzard Hitbox Velocity", 3)
popo.add_attribute(blizzard_data, 0x8, "Blizzard Hitbox Rise Acceleration", 3)
popo.add_attribute(blizzard_data, 0xC, "Blizzard Minimum Angle of Hitbox Spread", 3)
popo.add_attribute(blizzard_data, 0x10, "Blizzard Maximum Angle of Hitbox Spread", 3)

belay_data = popo.article_datas[2]
popo.add_attribute(belay_data, 0x0, "Belay String Length", 4)
popo.get_attribute("Belay String Length").integer = True
popo.add_attribute(belay_data, 0x4, "Belay String Retraction Speed", 4)
popo.get_attribute("Belay String Retraction Speed").integer = True
popo.add_attribute(belay_data, 0x14, "Belay String Gravity", 4)
popo.add_attribute(belay_data, 0x1C, "Belay String Length 2", 4)
popo.get_attribute("Belay String Length 2").integer = True
popo.add_attribute(belay_data, 0x20, "Belay String Elasticity", 4)
popo.get_attribute("Belay String Elasticity").integer = True