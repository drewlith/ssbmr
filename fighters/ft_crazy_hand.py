import fighter
from iso import DAT

crazy_hand = fighter.Fighter("Crazy Hand", DAT(b'PlCh.dat'))
fighter.fighters.append(crazy_hand)
crazy_hand.fighter_id = 0x1E

crazy_hand.good_sfx = [0x4e208, 0x4e20f, 0x4e210, 0x4e209, 0x4e214, 0x4e213, 0x4e211, 0x4e212, 0x4e20e, 0x4e20d, 0x4e20b, 0x4e20c, 0x4e20a]