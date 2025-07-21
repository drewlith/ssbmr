import fighter
from iso import DAT

crazy_hand = fighter.Fighter("Crazy Hand", DAT(b'PlCh.dat'))
fighter.fighters.append(crazy_hand)
crazy_hand.fighter_id = 0x1E