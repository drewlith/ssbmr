import fighter
from iso import DAT

master_hand = fighter.Fighter("Master Hand", DAT(b'PlMh.dat'))
fighter.fighters.append(master_hand)
master_hand.fighter_id = 0x1A

master_hand.good_sfx = [0x4e207, 0x4e208, 0x4e214, 0x4e213, 0x4e20f, 0x4e210, 0x4e20b, 0x4e20c, 0x4e20e, 0x4e20d, 0x4e211, 0x4e212]