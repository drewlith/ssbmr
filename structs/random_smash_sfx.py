class RandomSmashSFX():
    def __init__(self, data, offset):
        self.offset = offset
        self.data = data

    def __str__(self):
        return "Random Smash SFX Event at offset " + str(self.offset) + " with command: " + hex(self.data[0])