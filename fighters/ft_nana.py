import fighter
from iso import DAT
from structs import hitbox

nana = fighter.Fighter("Nana", DAT(b'PlNn.dat'))
fighter.fighters.append(nana)
nana.fighter_id = 0x0E

nana.projectile_offsets = [0x1A14]

nana.subactions[295].friendly_name = "Ice Shot"
nana.subactions[316].friendly_name = "Belay"

file_data = nana.dat_file.file_data
offset = nana.projectile_offsets[0]
iceshot_hitbox = hitbox.Hitbox(file_data[offset:offset+20], offset)
iceshot_hitbox.tags.append("projectile")
nana.projectile_hitboxes.append(iceshot_hitbox)