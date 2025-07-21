import fighter
from iso import DAT

girl = fighter.Fighter("Female Wireframe", DAT(b'PlGl.dat'))
fighter.fighters.append(girl)
girl.fighter_id = 0x1C