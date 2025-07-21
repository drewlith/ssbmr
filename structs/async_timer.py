from utility import get_value, set_value

class AsyncTimer():
    def __init__(self, data, offset):
        self.offset = offset
        self.data = data

    @property
    def value(self):
        return get_value(self.data, 0, 8)

    @value.setter
    def value(self, new):
        set_value(self.data, 0, 8, new)

    def __str__(self):
        return "Asynchronized Timer Event at offset " + str(self.offset) + " with command: " + hex(self.data[0]) + " | RAW HEX: " + self.data.hex()
