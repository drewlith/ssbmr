from utility import set_value, get_value

class GoTo():
    def __init__(self, data, offset): # 14000000 XXXXXXXX
        self.offset = offset
        self.data = data

    @property
    def value(self): 
        return get_value(self.data, 0, 32)

    @value.setter
    def value(self, value):
        self.data = set_value(self.data, 0, 32, value)

    def __str__(self):
        return "Go To Event at offset " + str(self.offset) + " with command: " + hex(self.data[0]) + " | RAW HEX: " + self.data.hex()