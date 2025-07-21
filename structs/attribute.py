# Custom to SSBMR for handling attributes
import struct
from utility import to_word
class Attribute():
    def __init__(self, data, name, offset, special=0): # Special 1 = Special Attribute; Special 2+ = Article
        self.data = data
        self.name = name
        self.tags = ["attribute"]
        self.offset = offset
        self.integer = False
        self.whole_number = False
        self.special = special
        self.article_number = 0
        self.original_value = 0
        self.log_notes = ""
        if special > 1:
            self.tags.append("article")
        elif special == 1:
            self.tags.append("special")
        else:
            self.tags.append("normal")
        self.tags.append(name.lower().replace(" ", ""))

    @property
    def value(self):
        if self.integer:
            return to_word(self.data)
        return struct.unpack('>f',self.data)[0]

    @value.setter
    def value(self, value):
        if self.integer:
            self.data = value.to_bytes(4, 'big')
            return
        data = struct.pack('>f', value)
        self.data = data