import fighter
from iso import DAT

giga_bowser = fighter.Fighter("Giga Bowser", DAT(b'PlGk.dat'))
fighter.fighters.append(giga_bowser)
giga_bowser.fighter_id = 0x1D