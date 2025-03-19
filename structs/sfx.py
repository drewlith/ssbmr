from utility import get_value, set_value
class SFX():
    def __init__(self, data, offset):
        self.offset = offset
        self.data = data
        
    @property
    def id(self): #b9 xEEEExxx
        return get_value(self.data, 32, 20)

    @id.setter
    def id(self, value):
        self.data = set_value(self.data, 32, 20, value)

    def __str__(self):
        string = "SFX Event at offset " + str(self.offset) + " with command: " + hex(self.data[0])
        string += "\n The sound effect ID is: " + str(hex(self.id))
        return string