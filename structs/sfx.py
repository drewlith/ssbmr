from utility import get_value, set_value, percent_chance
from random import randint as rng
import fighter

all_sfx = []

BLACKLIST = [0x0C3, 0x0C4, 0x0C5, 0x0C6, 0x0C7, 0x0C8, 0x0C9, 0x0CA, 0x0CB, 0x0CC, 0x0CD, 0x0CE, 0x0CF,
             0x0D0, 0x0D1, 0x0D2, 0x0D3, 0x0D4, 0x0D5, 0x0D6, 0x0D7, 0x0D8, 0x0D9, 0x0DA, 0x05F, 0x084,
             0x085, 0x12D]

class SFX():
    def __init__(self, data, offset):
        self.offset = offset
        self.data = data
        self.common_sfx = False
        if self.id <= 0xFFF:
            self.common_sfx = True
        all_sfx.append(self)

    @property
    def id(self): #44000000 000XXXXX 00007F40
        return get_value(self.data, 32, 20)

    @id.setter
    def id(self, value):
        self.data = set_value(self.data, 32, 20, value)

    def __str__(self):
        string = "SFX Event at offset " + str(self.offset) + " with command: " + hex(self.data[0]) + " | RAW HEX: " + self.data.hex()
        string += "\n The sound effect ID is: " + str(hex(self.id))
        return string
    
def randomize(chance):
    for _sfx in all_sfx:
        if percent_chance(chance):
            if _sfx.common_sfx:
                index = rng(0,0x20F)
                while index in BLACKLIST:
                    index = rng(0,0x20F)
                _sfx.id = index
    for _fighter in fighter.fighters:
        good_sfx = []
        for subaction in _fighter.subactions:
            for _sfx in subaction.sfx:
                if not _sfx.common_sfx:
                    if _sfx.id not in good_sfx:
                        good_sfx.append(_sfx.id)
        for subaction in _fighter.subactions:
            for _sfx in subaction.sfx:
                if not _sfx.common_sfx and "Dash" not in subaction.friendly_name:
                    if percent_chance(chance):
                        _sfx.id = good_sfx[rng(0,len(good_sfx)-1)]