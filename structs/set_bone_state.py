class SetBoneState():
    def __init__(self, data, offset):
        self.offset = offset
        self.data = data

    def __str__(self):
        return "Set Specific Bone State Event at offset " + str(self.offset) + " with command: " + hex(self.data[0]) + " | RAW HEX: " + self.data.hex()