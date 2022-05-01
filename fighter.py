import json, sys, util, struct

class Fighter():
    def __init__(self, name, dat, properties_offset):
        self.name = name
        self.dat = dat
        self.properties_offset = properties_offset
        self.property_data = []
        self.json_data = {}
        self.attacks = []
        self.throws = []
        self.shuffled_with = self.name

        self.shield_min = 0
        self.shield_max = 0

        self.swaps = ["","","","","","",""]

    def get_json_data(self):
        f = open("data/" + self.name + "/" + self.name + ".json")
        self.json_data = json.load(f)
        return self.json_data

    def get_bytes_at_index(self, start_index):
        data = []
        i = start_index
        while i < start_index + 4:
            data.append(self.property_data[i])
            i += 1
        return bytes(data)

    def set_bytes_at_index(self, data, start_index):
        new_data = bytearray(self.property_data)
        i = start_index
        k = 0
        while i < start_index + 4:
            new_data[i] = data[k]
            i += 1
            k += 1
        self.property_data = bytes(new_data)

    def get_weight(self):
        return struct.unpack('>f',self.get_bytes_at_index(136))[0]

    def set_weight(self, float_value):
        data = struct.pack('>f', float_value)
        self.set_bytes_at_index(data, 136)

    def get_scale(self):
        return struct.unpack('>f',self.get_bytes_at_index(140))[0]

    def set_scale(self, float_value):
        data = struct.pack('>f', float_value)
        self.set_bytes_at_index(data, 140)

    def get_shield_size(self):
        return struct.unpack('>f',self.get_bytes_at_index(144))[0]

    def set_shield_size(self, float_value):
        data = struct.pack('>f', float_value)
        self.set_bytes_at_index(data, 144)

    def get_air_attributes(self): # Air mobility + falling
        data = []
        for i in range(7):
            data.append(struct.unpack('>f',self.get_bytes_at_index(92 + (i*4)))[0])
        return data

    def set_air_attributes(self, float_values):
        data = []
        for i in range(7):
            data.append(struct.pack('>f', float_values[i]))
            self.set_bytes_at_index(data[i],92+(i*4))

    def get_jump_attributes(self): 
        data = []
        for i in range(8):
            data.append(struct.unpack('>f',self.get_bytes_at_index(56 + (i*4)))[0])
        return data

    def set_jump_attributes(self, float_values):
        data = []
        for i in range(8):
            data.append(struct.pack('>f', float_values[i]))
            self.set_bytes_at_index(data[i],56+(i*4))

    def get_ground_attributes(self): 
        data = []
        for i in range(11):
            data.append(struct.unpack('>f',self.get_bytes_at_index(i*4))[0])
        return data

    def set_ground_attributes(self, float_values):
        data = []
        for i in range(11):
            data.append(struct.pack('>f', float_values[i]))
            self.set_bytes_at_index(data[i],i*4)

    def get_landing_lags(self):
        data = []
        for i in range(6):
            data.append(struct.unpack('>f',self.get_bytes_at_index(228 + (i*4)))[0])
        return data

    def set_landing_lags(self, float_values):
        data = []
        for i in range(6):
            data.append(struct.pack('>f', float_values[i]))
            self.set_bytes_at_index(data[i],228+(i*4))

    def set_thresholds(self):
        self.scale_max = self.get_scale() * 1.2
        self.scale_min = self.get_scale() * 0.8
        self.shield_max = self.get_shield_size() * 1.3
        self.shield_min = self.get_shield_size() * 0.7
        


