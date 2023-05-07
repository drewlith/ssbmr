import random

MASK = [1, 2, 4, 8, 16, 32, 64, 128]
CLEAR_MASK = [254, 253, 251, 247, 239, 223, 191, 127]

def read_data(data, offset, length):
    new_data = bytearray()
    new_data.extend(data[offset:offset+length])
    return new_data
    
def write_data(data, offset, new_data):
    data[offset:offset+len(new_data)] = new_data

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

def get_word(data, offset=0):
    return get_value(data, offset*32, 32)

def merge(left, right):
    if len(left) == 0:
        return right

    if len(right) == 0:
        return left

    result = []
    index_left = index_right = 0

    while len(result) < len(left) + len(right):
        if left[index_left].get_file_offset() <= right[index_right].get_file_offset(): # Using index [1] to work with fst_files in melee.py
            result.append(left[index_left])
            index_left += 1
        else:
            result.append(right[index_right])
            index_right += 1

        if index_right == len(right):
            result += left[index_left:]
            break

        if index_left == len(left):
            result += right[index_right:]
            break

    return result

def merge_sort(array):
    if len(array) < 2:
        return array

    midpoint = len(array) // 2

    return merge(
        left=merge_sort(array[:midpoint]),
        right=merge_sort(array[midpoint:]))

def percent_chance(chance): # Util, enter chance in %
    rng = random.randint(0,99)
    if rng < chance:
        return True
    else:
        return False

def get_flag_params(flags, name, is_string=False):
    name = name.replace(" ", "")
    index = flags.find(name)
    index += len(name)
    string = ""
    if is_string == False:
        parameters = []
        param = ""
        while True:
            if index > len(flags)-1:
                parameters.append(int(param))
                break
            if flags[index] == "&" or flags[index] == "-": # Flag Delimiters
                parameters.append(int(param))
                break
            if flags[index] == ":": # Parameter Delimiter
                parameters.append(int(param))
                param = ""
            else:
                param += flags[index]
            index += 1
        return parameters
    else:
        while True:
            char = flags[index]
            if char == "&" or char == "-": # Flag Delimiters
                break
            string += char
            index += 1
        string = string.replace(" ", "")
        return string

def get_flag_float(flags, name):
    name = name.replace(" ", "")
    index = flags.find(name)
    index += len(name)
    parameters = []
    param = ""
    while True:
        if index > len(flags)-1:
            parameters.append(float(param))
            break
        if flags[index] == "&" or flags[index] == "-": # Flag Delimiters
            parameters.append(float(param))
            break
        if flags[index] == ":": # Parameter Delimiter
            parameters.append(float(param))
            param = ""
        else:
            param += flags[index]
        index += 1
    return parameters

def get_word_string(word):
    string = ""
    for b in word:
        value = b
        b = hex(b)
        b = str(b)
        b = b.replace("0x", "")
        b = b.upper()
        if value < 16:
            b = "0" + b
        string += b
    return string

