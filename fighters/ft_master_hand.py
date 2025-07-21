import fighter
from iso import DAT

master_hand = fighter.Fighter("Master Hand", DAT(b'PlMh.dat'))
fighter.fighters.append(master_hand)
master_hand.fighter_id = 0x1A