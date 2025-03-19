# Custom to SSBMR for handling attributes
import struct
from utility import to_word
class Attribute():
    def __init__(self, data, name, offset):
        self.data = data
        self.name = name
        self.tags = []
        self.offset = offset
        self.integer = False
        self.whole_number = False
        self.article_number = 0
        self.original_value = 0
        self.log_notes = ""

    @property
    def value(self):
        if self.integer:
            return to_word(self.data)
        return struct.unpack('>f',self.data)[0]

    @value.setter
    def value(self, value):
        if self.integer:
            data = value.to_bytes(4, 'big')
            return
        data = struct.pack('>f', value)
        self.data = data