from utility import get_value, set_value

class Subroutine(): # 0x1C000000 XXXXXXXX
    def __init__(self, data, offset):
        self.offset = offset
        self.data = data

    @property
    def value(self): 
        return get_value(self.data, 0, 32)

    @value.setter
    def value(self, value):
        self.data = set_value(self.data, 0, 32, value)

    def __str__(self):
        return "Subroutine Event at offset " + str(self.offset) + " with command: " + hex(self.data[0]) + " | RAW HEX: " + self.data.hex()
