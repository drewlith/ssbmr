import fighter
from iso import DAT

jigglypuff = fighter.Fighter("Jigglypuff", DAT(b'PlPr.dat'))
fighter.fighters.append(jigglypuff)
jigglypuff.fighter_id = 0x0F

jigglypuff.special_attribute_block_size = 0x100
jigglypuff.articles_sizes = []
jigglypuff.articles_offsets = []
jigglypuff.projectile_offsets = []

jigglypuff.subactions[302].friendly_name = "Rollout 1 (Ground)"
jigglypuff.subactions[303].friendly_name = "Rollout 2 (Ground)"
jigglypuff.subactions[304].friendly_name = "Rollout 3 (Ground)"
jigglypuff.subactions[310].friendly_name = "Rollout 1 (Aerial)"
jigglypuff.subactions[311].friendly_name = "Rollout 2 (Aerial)"
jigglypuff.subactions[312].friendly_name = "Rollout 3 (Aerial)"
jigglypuff.subactions[317].friendly_name = "Pound"
jigglypuff.subactions[319].friendly_name = "Sing (Ground)"
jigglypuff.subactions[321].friendly_name = "Sing (Aerial)"
jigglypuff.subactions[320].friendly_name = "Rest 1 (Ground)"
jigglypuff.subactions[322].friendly_name = "Rest 2 (Ground)"
jigglypuff.subactions[323].friendly_name = "Rest 1 (Aerial)"
jigglypuff.subactions[325].friendly_name = "Rest 2 (Aerial)"

attribute_data = jigglypuff.dat_file.get_special_attribute_data(jigglypuff.special_attribute_block_size)
jigglypuff.add_attribute(attribute_data, 0x0, "Jumps Turn Duration", 1)
jigglypuff.get_attribute("Jumps Turn Duration").integer = True
jigglypuff.add_attribute(attribute_data, 0x4, "Jumps Horizontal Momentum Backward", 1)
jigglypuff.add_attribute(attribute_data, 0x8, "Jumps Horizontal Momentum Forward", 1)
jigglypuff.add_attribute(attribute_data, 0xC, "Jumps Turn Momentum", 1)
jigglypuff.add_attribute(attribute_data, 0x10, "Jumps Horizontal Momentum Neutral", 1)
jigglypuff.add_attribute(attribute_data, 0x14, "Jump 1 Vertical Momentum", 1)
jigglypuff.add_attribute(attribute_data, 0x18, "Jump 2 Vertical Momentum", 1)
jigglypuff.add_attribute(attribute_data, 0x1C, "Jump 3 Vertical Momentum", 1)
jigglypuff.add_attribute(attribute_data, 0x20, "Jump 4 Vertical Momentum", 1)
jigglypuff.add_attribute(attribute_data, 0x24, "Jump 5 Vertical Momentum", 1)
jigglypuff.add_attribute(attribute_data, 0x28, "Number of Jumps", 1)
jigglypuff.get_attribute("Number of Jumps").integer = True
jigglypuff.add_attribute(attribute_data, 0x34, "Rollout Duration", 1)
jigglypuff.get_attribute("Rollout Duration").integer = True
jigglypuff.add_attribute(attribute_data, 0x3C, "Rollout Start Air Height Offset", 1)
jigglypuff.add_attribute(attribute_data, 0x40, "Rollout Bounciness", 1)
jigglypuff.add_attribute(attribute_data, 0x48, "Rollout Gravity During Roll", 1)
jigglypuff.add_attribute(attribute_data, 0x4C, "Rollout Base Rolling Speed", 1)
jigglypuff.add_attribute(attribute_data, 0x50, "Rollout Max Rolling Speed", 1)
jigglypuff.add_attribute(attribute_data, 0x5C, "Rollout Aerial X-Axis Momentum Forward", 1)
jigglypuff.add_attribute(attribute_data, 0x60, "Rollout Aerial Initial Momentum", 1)
jigglypuff.add_attribute(attribute_data, 0x64, "Rollout Max Momentum", 1)
jigglypuff.add_attribute(attribute_data, 0x68, "Rollout Spinning Speed", 1)
jigglypuff.add_attribute(attribute_data, 0x6C, "Rollout Spinning Turn Speed", 1)
jigglypuff.add_attribute(attribute_data, 0x78, "Rollout Bounciness A", 1)
jigglypuff.add_attribute(attribute_data, 0x7C, "Rollout Bounciness B", 1)
jigglypuff.add_attribute(attribute_data, 0x80, "Rollout Base Damage", 1)
jigglypuff.add_attribute(attribute_data, 0x84, "Rollout Damage Multiplier", 1)
jigglypuff.add_attribute(attribute_data, 0x88, "Rollout Horizontal Bounce On Hit", 1)
jigglypuff.add_attribute(attribute_data, 0x8C, "Rollout Vertical Bounce on Hit", 1)
jigglypuff.add_attribute(attribute_data, 0x90, "Rollout Input Modifier", 1)
jigglypuff.add_attribute(attribute_data, 0xA0, "Rollout Charge Rate", 1)
jigglypuff.add_attribute(attribute_data, 0xA4, "Rollout Charge Time", 1)
jigglypuff.add_attribute(attribute_data, 0xAC, "Rollout Spin Charge Animation", 1)
jigglypuff.add_attribute(attribute_data, 0xB8, "Rollout Speed Variable", 1)
jigglypuff.add_attribute(attribute_data, 0xBC, "Rollout Spin Animation Post Hit", 1)
jigglypuff.add_attribute(attribute_data, 0xC0, "Rollout Air Speed", 1)
jigglypuff.add_attribute(attribute_data, 0xC4, "Rollout Turn Rate Variable", 1)
jigglypuff.add_attribute(attribute_data, 0xD8, "Rollout Landing Lag", 1)
jigglypuff.add_attribute(attribute_data, 0xE4, "Pound Angled Directional Difference", 1)
jigglypuff.add_attribute(attribute_data, 0xF0, "Pound Air Travel Distance", 1)
jigglypuff.add_attribute(attribute_data, 0xF4, "Pound Air Deceleration Rate", 1)