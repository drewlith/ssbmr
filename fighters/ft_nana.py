import fighter
from iso import DAT
from structs import hitbox

nana = fighter.Fighter("Nana", DAT(b'PlNn.dat'))
fighter.fighters.append(nana)
nana.fighter_id = 0x0E

nana.good_sfx = [0x1fbdc, 0x1fbe2, 0x1fc24, 0x1fbf7, 0x1fc15, 0x1fc21, 0x1fbfd, 0x1fc0c, 0x1fc33, 0x1fbf1, 0x1fbdf, 0x1fc00]

nana.projectile_offsets = [0x1A14]
nana.subactions[0x127].friendly_name = "Ice Shot"
nana.subactions[0x128].friendly_name = "Ice Shot"
nana.subactions[0x129].friendly_name = "Squall Hammer"
nana.subactions[0x12A].friendly_name = "Squall Hammer"
nana.subactions[0x12B].friendly_name = "Squall Hammer"
nana.subactions[0x12C].friendly_name = "Squall Hammer"
nana.subactions[0x12D].friendly_name = "Belay"
nana.subactions[0x12E].friendly_name = "Belay"
nana.subactions[0x12F].friendly_name = "Belay"
nana.subactions[0x130].friendly_name = "Belay"
nana.subactions[0x131].friendly_name = "Belay"
nana.subactions[0x132].friendly_name = "Belay"
nana.subactions[0x133].friendly_name = "Belay"
nana.subactions[0x134].friendly_name = "Belay"
nana.subactions[0x135].friendly_name = "Belay"
nana.subactions[0x136].friendly_name = "Belay"
nana.subactions[0x137].friendly_name = "Blizzard"
nana.subactions[0x138].friendly_name = "Blizzard"
nana.subactions[0x139].friendly_name = "Squall Hammer"
nana.subactions[0x13A].friendly_name = "Squall Hammer"
nana.subactions[0x13B].friendly_name = "Belay"
nana.subactions[0x13C].friendly_name = "Belay"
nana.subactions[0x13D].friendly_name = "Belay"
nana.subactions[0x13E].friendly_name = "Belay"
nana.subactions[0x13F].friendly_name = "Belay"
nana.subactions[0x140].friendly_name = "Belay"

for action in nana.subactions:
    if "Nameless" not in action.friendly_name:
        action.tags.append(action.friendly_name.lower().replace(" ", ""))

file_data = nana.dat_file.file_data
offset = nana.projectile_offsets[0]
iceshot_hitbox = hitbox.Hitbox(file_data[offset:offset+20], offset)
iceshot_hitbox.tags.append("projectile")
nana.projectile_hitboxes.append(iceshot_hitbox)