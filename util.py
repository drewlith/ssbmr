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

