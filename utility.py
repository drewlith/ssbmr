import random

MASK = [1, 2, 4, 8, 16, 32, 64, 128]
CLEAR_MASK = [254, 253, 251, 247, 239, 223, 191, 127]

def get_bit(data, bit): # lowest index = least significant. Use on Bytearray
    index = (len(data)-1) - bit // 8
    if data[index] & MASK[bit%8] == MASK[bit%8]: return 1
    else: return 0

def set_bit(data, bit):
    index = (len(data)-1) - bit // 8
    data[index] = data[index] | MASK[bit%8]
    return data

def clear_bit(data, bit):
    index = (len(data)-1) - bit // 8
    data[index] = data[index] & CLEAR_MASK[bit%8]
    return data

def get_value(data, offset, size):
    value = 0
    for i in range(size):
        if get_bit(data, offset+i) == 1:
            value += 2**i
    return value

def set_value(data, offset, size, value):
    for i in range(size):
        if value & 2**i == 2**i: data = set_bit(data,offset+i)
        else: data = clear_bit(data, offset+i)
    return data

def to_word(data, offset=0):
    return get_value(data, offset*32, 32)

def percent_chance(chance): # Util, enter chance in %
    rng = random.randint(0,99)
    if rng < chance:
        return True
    else:
        return False

class bidict(dict): # https://stackoverflow.com/questions/3318625/how-to-implement-an-efficient-bidirectional-hash-table
    def __init__(self, *args, **kwargs):
        super(bidict, self).__init__(*args, **kwargs)
        self.inverse = {}
        for key, value in self.items():
            self.inverse.setdefault(value, []).append(key) 

    def __setitem__(self, key, value):
        if key in self:
            self.inverse[self[key]].remove(key) 
        super(bidict, self).__setitem__(key, value)
        self.inverse.setdefault(value, []).append(key)        

    def __delitem__(self, key):
        self.inverse.setdefault(self[key], []).remove(key)
        if self[key] in self.inverse and not self.inverse[self[key]]: 
            del self.inverse[self[key]]
        super(bidict, self).__delitem__(key)

        