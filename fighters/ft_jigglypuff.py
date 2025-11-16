import fighter
from iso import DAT

jigglypuff = fighter.Fighter("Jigglypuff", DAT(b'PlPr.dat'))
fighter.fighters.append(jigglypuff)
jigglypuff.fighter_id = 0x0F

jigglypuff.special_attribute_block_size = 0x100
jigglypuff.articles_sizes = []
jigglypuff.articles_offsets = []
jigglypuff.projectile_offsets = []

jigglypuff.good_sfx = [0x3d0b5, 0x3d0a9, 0x3d0c7, 0x3d091, 0x3d0c4, 0x3d094, 0x3d0bb, 0x3d0be, 0x3d0ca, 0x3d0dc, 0x3d0cd]

jigglypuff.subactions[0x127].friendly_name = "Aerial Jump 1"
jigglypuff.subactions[0x128].friendly_name = "Aerial Jump 2"
jigglypuff.subactions[0x129].friendly_name = "Aerial Jump 3"
jigglypuff.subactions[0x12A].friendly_name = "Aerial Jump 4"
jigglypuff.subactions[0x12B].friendly_name = "Aerial Jump 5"
jigglypuff.subactions[0x12C].friendly_name = "Rollout"
jigglypuff.subactions[0x12D].friendly_name = "Rollout"
jigglypuff.subactions[0x12E].friendly_name = "Rollout"
jigglypuff.subactions[0x12F].friendly_name = "Rollout"
jigglypuff.subactions[0x130].friendly_name = "Rollout"
jigglypuff.subactions[0x131].friendly_name = "Rollout"
jigglypuff.subactions[0x132].friendly_name = "Rollout"
jigglypuff.subactions[0x133].friendly_name = "Rollout"
jigglypuff.subactions[0x134].friendly_name = "Rollout"
jigglypuff.subactions[0x135].friendly_name = "Rollout"
jigglypuff.subactions[0x136].friendly_name = "Rollout"
jigglypuff.subactions[0x137].friendly_name = "Rollout"
jigglypuff.subactions[0x138].friendly_name = "Rollout"
jigglypuff.subactions[0x139].friendly_name = "Rollout"
jigglypuff.subactions[0x13A].friendly_name = "Rollout"
jigglypuff.subactions[0x13B].friendly_name = "Rollout"
jigglypuff.subactions[0x13C].friendly_name = "Rollout"
jigglypuff.subactions[0x13D].friendly_name = "Pound"
jigglypuff.subactions[0x13E].friendly_name = "Pound"
jigglypuff.subactions[0x13F].friendly_name = "Sing"
jigglypuff.subactions[0x140].friendly_name = "Sing"
jigglypuff.subactions[0x141].friendly_name = "Sing"
jigglypuff.subactions[0x142].friendly_name = "Sing"
jigglypuff.subactions[0x143].friendly_name = "Rest"
jigglypuff.subactions[0x144].friendly_name = "Rest"
jigglypuff.subactions[0x145].friendly_name = "Rest"
jigglypuff.subactions[0x146].friendly_name = "Rest"

for action in jigglypuff.subactions:
    if "Nameless" not in action.friendly_name:
        action.tags.append(action.friendly_name.lower().replace(" ", ""))

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
jigglypuff.add_attribute(attribute_data, 0x28, "Number of Jigglypuff Jumps", 1)
jigglypuff.get_attribute("Number of Jigglypuff Jumps").integer = True
jigglypuff.add_attribute(attribute_data, 0x34, "Rollout Duration", 1)
jigglypuff.get_attribute("Rollout Duration").integer = True
jigglypuff.add_attribute(attribute_data, 0x3C, "Rollout Start Air Height Offset", 1)
jigglypuff.add_attribute(attribute_data, 0x40, "Rollout Base Bounciness", 1)
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