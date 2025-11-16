import fighter
from iso import DAT

giga_bowser = fighter.Fighter("Giga Bowser", DAT(b'PlGk.dat'))
fighter.fighters.append(giga_bowser)
giga_bowser.fighter_id = 0x1D

giga_bowser.good_sfx = [0x1d4c6, 0x1d4ff, 0x1d4d2, 0x1d4de, 0x1d4cc, 0x1d4c9, 0x1d4ea, 0x1d4fc, 0x1d4f9, 0x1d4e7, 0x1d4c0, 0x1d4f6]