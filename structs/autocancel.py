class Autocancel():
    def __init__(self, data, offset):
        self.offset = offset
        self.data = data

    def __str__(self):
        return "Autocancel Event at offset " + str(self.offset) + " with command: " + hex(self.data[0])