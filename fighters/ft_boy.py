import fighter
from iso import DAT

boy = fighter.Fighter("Male Wireframe", DAT(b'PlBo.dat'))
fighter.fighters.append(boy)
boy.fighter_id = 0x1B