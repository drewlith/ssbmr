class ModelMod():
    def __init__(self, data, offset):
        self.offset = offset
        self.data = data

    def __str__(self):
        return "Model Mod Event at offset " + str(self.offset) + " with command: " + hex(self.data[0])