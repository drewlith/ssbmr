from utility import percent_chance
import iso
from random import randint as rng
from random import shuffle
from random import seed

GROUPS = ["Falcon Normal", "Falcon Blue"]

global_adjust = [0,0,0]
global_method_select = 0
global_swap_select = 0
global_num_methods = 2
global_fun_value = rng(0,100)
global_invert = False

class FileColorData:
    def __init__(self, file_name, group="None"):
        self.file = iso.find_file(file_name)
        self.data = self.file.file_data
        self.group = group
        self.zero_sevens = []
        self.four_two_four_eights = []
        self.cf_ones = []
        self.cf_twos = []
        self.matrices = []

    def add_zero_seven(self, offset, name="?"):
        self.zero_sevens.append(ZeroSeven(self.data[offset:offset+12], offset, name))

    def add_four_two_four_eight(self, offset, name="?"):
        self.four_two_four_eights.append(FourTwoFourEight(self.data[offset:offset+18], offset, name))

    def add_cf_one(self, offset, name="?"):
        self.cf_ones.append(CF1Color(self.data[offset:offset+5], offset, name))
    
    def add_cf_two(self, offset, name="?"):
        self.cf_twos.append(CF2Color(self.data[offset:offset+12], offset, name))

    def get_matrix_size(self, offset, dimensions):
        index_count = int.from_bytes(self.file.file_data[offset+1:offset+4], "big")
        return index_count * dimensions + 4

    def add_matrix(self, offset, dimensions=0x3, name="?"):
        self.matrices.append(Matrix(self.data[offset:offset+self.get_matrix_size(offset, dimensions)], offset, dimensions, name))

    def randomize_all(self):
        randomize_colors(self.cf_ones)
        for cf_two in self.cf_twos:
            colors = two_color_to_rgbas(cf_two)
            randomize_colors(colors)
            rgbas_to_two_colors(colors, cf_two)
        for zero_seven in self.zero_sevens:
            colors = two_color_to_rgbas(zero_seven)
            randomize_colors(colors)
            rgbas_to_two_colors(colors, zero_seven)
        for four_two in self.four_two_four_eights:
            colors = two_color_to_rgbas(four_two)
            randomize_colors(colors)
            rgbas_to_two_colors(colors, four_two)
        for matrix in self.matrices:
            randomize_colors(matrix.colors)
        for cf_two in self.cf_twos:
            self.file.file_data[cf_two.offset:cf_two.offset+len(cf_two.data)] = cf_two.data
        for zero_seven in self.zero_sevens:
            self.file.file_data[zero_seven.offset:zero_seven.offset+len(zero_seven.data)] = zero_seven.data
        for four_two in self.four_two_four_eights:
            self.file.file_data[four_two.offset:four_two.offset+len(four_two.data)] = four_two.data
        for matrix in self.matrices:
            matrix.write_color_data()
            self.file.file_data[matrix.offset:matrix.offset+len(matrix.data)] = matrix.data

def rgby_to_rgba(rgby):
    color_int = int.from_bytes(rgby, "big")
    alpha = 0x0
    if color_int & 0x8000 == 0x8000:
        color_int -= 0x8000
        alpha = 0xFF
    red = (color_int & 0x7C00) >> 10
    green = (color_int & 0x3E0) >> 5
    blue = color_int & 0x1F
    return RGBA(red, green, blue, alpha)

def rgba_to_rgby(rgba):
    color_int = 0
    if rgba.alpha > 0:
        color_int = 0x8000
    color_int += (rgba.red // 8) * 1024
    color_int += (rgba.green // 8) * 32
    color_int += rgba.blue // 8
    return color_int.to_bytes(2, "big")

class Matrix:
    def __init__(self, data, offset, dimensions = 0x3, name="?"):
        self.data = data
        self.offset = offset
        self.dimensions = dimensions
        self.name = name
        self.colors = []
        self.index_count = int.from_bytes(self.data[1:3], "big")
        self.get_color_data()
    
    def get_color_data(self):
        header_len = 4
        for i in range(self.index_count):
            offset = i*(2+self.dimensions) + header_len
            self.colors.append(rgby_to_rgba(self.data[offset:offset+2]))

    def write_color_data(self):
        header_len = 4
        for i in range(self.index_count):
            offset = i*(2+self.dimensions) + header_len
            self.data[offset:offset+2] = rgba_to_rgby(self.colors[i])

class CF1Color:
    def __init__(self, data, offset, name="?"):
            self.data = data
            self.offset = offset
            self.name = name
    
    @property
    def red(self): # CF00 RRGGBB
        return self.data[2]
    
    @red.setter
    def red(self, value): 
        self.data[2] = value

    @property
    def green(self): # CF00 RRGGBB
        return self.data[3]
    
    @green.setter
    def green(self, value): 
        self.data[3] = value

    @property
    def blue(self): # CF00 RRGGBB
        return self.data[4]
    
    @blue.setter
    def blue(self, value): 
        self.data[4] = value
    
    def __str__(self):
        string = "0xCF 1 Color Effect at offset: " + hex(self.offset) + " with name: " + self.name
        string += "\n RED A: " + str(self.red_a) + " GREEN A: " + str(self.green_a) + " BLUE A: " + str(self.blue_a)
        return string

class CF2Color:
    def __init__(self, data, offset, name="?"):
        self.data = data
        self.offset = offset
        self.name = name
    
    @property
    def red_a(self):  # CF00 RRGGBB?? ??????RR GGBB
        return self.data[2]
    
    @red_a.setter
    def red_a(self, value): 
        self.data[2] = value

    @property
    def green_a(self): # CF00 RRGGBB?? ??????RR GGBB
        return self.data[3]
    
    @green_a.setter
    def green_a(self, value): 
        self.data[3] = value

    @property
    def blue_a(self): # CF00 RRGGBB?? ??????RR GGBB
        return self.data[4]
    
    @blue_a.setter
    def blue_a(self, value): 
        self.data[4] = value

    @property
    def red_b(self): 
        return self.data[9]
    
    @red_b.setter
    def red_b(self, value): 
        self.data[9] = value

    @property
    def green_b(self): # CF00 RRGGBB?? ??????RR GGBB
        return self.data[10]
    
    @green_b.setter
    def green_b(self, value): 
        self.data[10] = value

    @property
    def blue_b(self): # CF00 RRGGBB?? ??????RR GGBB
        return self.data[11]
    
    @blue_b.setter
    def blue_b(self, value): 
        self.data[11] = value
    
    def __str__(self):
        string = "0xCF 2 Color Effect at offset: " + hex(self.offset) + " with name: " + self.name
        string += "\n RED A: " + str(self.red_a) + " GREEN A: " + str(self.green_a) + " BLUE A: " + str(self.blue_a)
        string += "\n RED B: " + str(self.red_b) + " GREEN B: " + str(self.green_b) + " BLUE B: " + str(self.blue_b)
        return string

class FourTwoFourEight:
    def __init__(self, data, offset, name="?"):
        self.data = data
        self.offset = offset
        self.name = name
    
    @property
    def red_a(self): 
        return self.data[0]
    
    @red_a.setter
    def red_a(self, value): 
        self.data[0] = value

    @property
    def green_a(self): #XX????FF ??????FF FFFFFFFF ???????? 4248
        return self.data[1]
    
    @green_a.setter
    def green_a(self, value): 
        self.data[1] = value

    @property
    def blue_a(self): #XX????FF ??????FF FFFFFFFF ???????? 4248
        return self.data[2]
    
    @blue_a.setter
    def blue_a(self, value): 
        self.data[2] = value
    
    @property
    def red_b(self): #XX????FF ??????FF FFFFFFFF ???????? 4248
        return self.data[4]
    
    @red_b.setter
    def red_b(self, value): 
        self.data[4] = value

    @property
    def green_b(self): #XX????FF ??????FF FFFFFFFF ???????? 4248
        return self.data[5]
    
    @green_b.setter
    def green_b(self, value): 
        self.data[5] = value

    @property
    def blue_b(self): #XX????FF ??????FF FFFFFFFF ???????? 4248
        return self.data[6]
    
    @blue_b.setter
    def blue_b(self, value): 
        self.data[6] = value
    
    def __str__(self):
        string = "0x4248 Color Effect at offset: " + hex(self.offset) + " with name: " + self.name
        string += "\n RED A: " + str(self.red_a) + " GREEN A: " + str(self.green_a) + " BLUE A: " + str(self.blue_a)
        string += "\n RED B: " + str(self.red_b) + " GREEN B: " + str(self.green_b) + " BLUE B: " + str(self.blue_b)
        return string

class ZeroSeven:
    def __init__(self, data, offset, name="?"):
        self.data = data
        self.offset = offset

    @property
    def transparency(self): #070707XX ???????? ????????
        return self.data[3]

    @property
    def red_a(self): #070707?? XX?????? ????????
        return self.data[4]
    
    @red_a.setter
    def red_a(self, value): 
        self.data[4] = value

    @property
    def green_a(self): #070707?? ??XX???? ????????
        return self.data[5]
    
    @green_a.setter
    def green_a(self, value): 
        self.data[5] = value

    @property
    def blue_a(self): #070707?? ????XX?? ????????
        return self.data[6]
    
    @blue_a.setter
    def blue_a(self, value): 
        self.data[6] = value
    
    @property
    def red_b(self): #070707?? ???????? XX??????
        return self.data[8]
    
    @red_b.setter
    def red_b(self, value): 
        self.data[8] = value

    @property
    def green_b(self): #070707?? ???????? ??XX????
        return self.data[9]
    
    @green_b.setter
    def green_b(self, value): 
        self.data[9] = value

    @property
    def blue_b(self): #070707?? ???????? ????XX??
        return self.data[10]
    
    @blue_b.setter
    def blue_b(self, value): 
        self.data[10] = value
    
    def __str__(self):
        string = "0x070707 Color Effect at offset: " + hex(self.offset) + " with name: " + self.name
        string += "\n RED A: " + str(self.red_a) + " GREEN A: " + str(self.green_a) + " BLUE A: " + str(self.blue_a)
        string += "\n RED B: " + str(self.red_b) + " GREEN B: " + str(self.green_b) + " BLUE B: " + str(self.blue_b)
        return string
    
class RGBA:
    def __init__(self, red, green, blue, alpha=0xFF):
        self.red = red
        self.green = green
        self.blue = blue
        self.alpha = alpha

    def __str__(self):
        return "Red: " + str(hex(self.red)) + " Green: " + str(hex(self.green)) + " Blue: " + str(hex(self.blue)) + " Alpha: " + str(hex(self.alpha))

def two_color_to_rgbas(two_color_format):
    color_a = RGBA(two_color_format.red_a, two_color_format.green_a, two_color_format.blue_a, 0xFF)
    color_b = RGBA(two_color_format.red_b, two_color_format.green_b, two_color_format.blue_b, 0xFF)
    return (color_a, color_b)

def rgbas_to_two_colors(rgbas, two_color_format):
    two_color_format.red_a = rgbas[0].red
    two_color_format.green_a = rgbas[0].green
    two_color_format.blue_a = rgbas[0].blue
    two_color_format.red_b = rgbas[1].red
    two_color_format.green_b = rgbas[1].green
    two_color_format.blue_b = rgbas[1].blue

def rgba_to_rgb565(rgba):
    red = (rgba.red // 0x8) << 11
    green = (rgba.green // 0x4) << 5
    blue = (rgba.blue // 0x8)
    data = red | green | blue
    return data.to_bytes(2, "big")

def rgb565_to_rgba(pallete_data):
    pallete_data_int = int.from_bytes(pallete_data, "big")
    red = (0x8 * (pallete_data_int & 0xF800)) >> 11
    green = (0x4 * (pallete_data_int & 0x7E0)) >> 5
    blue = 0x8 * (pallete_data_int & 0x1F)
    return RGBA(red, green, blue)

def rgba_to_rgb5a3(rgba):
    if rgba.alpha < 0xFF:
        alpha = rgba.alpha // 0x20 << 12
        red = rgba.red // 0x11 << 8
        green = rgba.green // 0x11 << 4
        blue = rgba.blue // 0x11
        data = alpha | red | green | blue
        return data.to_bytes(2, "big")
    else:
        alpha = 0x8000
        red = rgba.red // 0x8 << 10
        green = rgba.green // 0x8 << 5
        blue = rgba.blue // 0x8
        data = alpha | red | green | blue
        return data.to_bytes(2, "big")

def rgb5a3_to_rgba(pallete_data):
    pallete_data_int = int.from_bytes(pallete_data, "big")
    top_bit = pallete_data_int & 0x8000
    if top_bit == 0: # ALPHA
        alpha = 0x20 * (pallete_data_int & 0x7000) >> 12
        red = 0x11 * (pallete_data_int & 0xF00) >> 8
        green = 0x11 * (pallete_data_int & 0xF0) >> 4
        blue = 0x11 * (pallete_data_int & 0xF)
    else: # No alpha
        red = 0x8 * (pallete_data_int & 0x7C00) >> 10
        green = 0x8 * (pallete_data_int & 0x3E0) >> 5
        blue = 0x8 * (pallete_data_int & 0x1F)
        alpha = 0xFF
    return RGBA(red, green, blue, alpha)

def rgba8_to_rgba(palette_data):
    return RGBA(palette_data[1], palette_data[2], palette_data[3], palette_data[0])

def rgba_to_rgba8(rgba):
    data = bytearray()
    data.extend(rgba.alpha.to_bytes(2, "big"))
    data.extend(rgba.red.to_bytes(2, "big"))
    data.extend(rgba.green.to_bytes(2, "big"))
    data.extend(rgba.blue.to_bytes(2, "big"))
    return data

def adjust_colors(colors):
    global global_invert
    if global_method_select == 1:
        for color in colors:
            color.red = (color.red + global_adjust[0]) % 255
            color.green = (color.green + global_adjust[1]) % 255
            color.blue = (color.blue + global_adjust[2]) % 255
    if global_method_select == 0:
        swap_colors(colors)
        if global_invert:
            invert_colors(colors)
        for color in colors:
            red = color.red + global_adjust[0]
            green = color.green + global_adjust[1]
            blue = color.blue + global_adjust[2]
            if red > 255:
                red = 255
            if green > 255:
                green = 255
            if blue > 255:
                blue = 255
            if red < 0:
                red = 0
            if green < 0:
                green = 0
            if blue < 0:
                blue = 0
            color.red = red
            color.green = green
            color.blue = blue

def invert_colors(colors):
    for color in colors:
        color.red = 255 - color.red
        color.green = 255 - color.green
        color.blue = 255 - color.blue

def swap_colors(colors):
    global global_method_select
    choice = rng(0,3)
    if global_method_select == 0:
        choice = global_swap_select
    # Type 0: R > G, G > B, B > R
    if choice == 0:
        for color in colors:
            color.red, color.green, color.blue = color.green, color.blue, color.red
    # Type 1: R <> B
    if choice == 1:
        for color in colors:
            color.red, color.blue = color.blue, color.red
    # Type 2: B <> G
    if choice == 2:
        for color in colors:
            color.blue, color.green = color.green, color.blue
    # Type 3: R <> G
    if choice == 3:
        for color in colors:
            color.red, color.green = color.green, color.red

def randomize_colors(colors):
    global global_adjust
    if global_method_select <= 1:
        adjust_colors(colors)
    if global_method_select == 2:
        swap_colors(colors)
    if global_fun_value == 100 and global_method_select > 0:
        global_adjust = [rng(-128,128), rng(-128,128), rng(-128,128)]
    elif percent_chance(global_fun_value // 8) and global_method_select > 0:
        global_adjust = [rng(-10,10), rng(-10,10), rng(-10,10)]

class CMPRHandler:
    def __init__(self, color1, color2, data1, data2, image_data):
        self.color1 = color1
        self.color2 = color2
        self.colors = [self.color1, self.color2]
        self.color1_data = data1
        self.color2_data = data2
        self.image_data = int.from_bytes(image_data, "big")
        if int.from_bytes(data1, "big") < int.from_bytes(data2, "big"):
            self.transparent = True
        else:
            self.transparent = False

def randomize_texture_color(file, offset, size, texture_type):
    data = file.data[offset:offset+size]
    if texture_type == "CMPR":
        cmprs = []
        pallete_block_size = 4
        for i in range(size // pallete_block_size):
            if (i % 2) == 0: # Every other 4 byte block
                pallete_offset = i*pallete_block_size
                color1_data = data[pallete_offset:pallete_offset+2]
                color2_data = data[pallete_offset+2:pallete_offset+4]
                color1_rgba = rgb565_to_rgba(color1_data)
                color2_rgba = rgb565_to_rgba(color2_data)
                image_data = data[pallete_offset+4:pallete_offset+8]
                cmprs.append(CMPRHandler(color1_rgba, color2_rgba, color1_data, color2_data, image_data))
        for cmpr in cmprs:
            randomize_colors(cmpr.colors)
        color_index = 0
        for i in range(size // pallete_block_size):
            if (i % 2) == 0:
                pallete_offset = i*pallete_block_size
                new_color_1 = rgba_to_rgb565(cmprs[color_index].colors[0])
                new_color_2 = rgba_to_rgb565(cmprs[color_index].colors[1])
                int_color1 = int.from_bytes(new_color_1, "big")
                int_color2 = int.from_bytes(new_color_2, "big")
                if cmprs[color_index].transparent: # Preserve transparency
                    while int_color1 > int_color2:
                        if int_color1 > 0x800:
                            int_color1 -= 0x800
                        elif int_color1 > 0x20:
                            int_color1 -= 0x20
                        else:
                            int_color1 -= 0x1
                else: # Preserve Non-transparency
                    while int_color1 < int_color2:
                        if int_color1 < 0xF7FF:
                            int_color1 += 0x800
                        elif int_color1 < 0xFFDF:
                            int_color1 += 0x20
                        else:
                            int_color1 += 1
                new_color_1 = int_color1.to_bytes(2, "big")
                new_color_2 = int_color2.to_bytes(2, "big")
                data[pallete_offset:pallete_offset+2] = new_color_1
                data[pallete_offset+2:pallete_offset+4] = new_color_2
                color_index += 1
    if texture_type == "RGB5A3":
        colors = []
        for i in range(size // 2):
            data_offset = i * 2
            colors.append(rgb5a3_to_rgba(data[data_offset:data_offset + 2]))
        randomize_colors(colors)
        for i in range(size // 2):
            data_offset = i * 2
            new_color = rgba_to_rgb5a3(colors[i])
            data[data_offset:data_offset+2] = new_color
    if texture_type == "RGB565":
        colors = []
        for i in range(size // 2):
            data_offset = i * 2
            colors.append(rgb565_to_rgba(data[data_offset:data_offset + 2]))
        randomize_colors(colors)
        for i in range(size // 2):
            data_offset = i * 2
            new_color = rgba_to_rgb565(colors[i])
            data[data_offset:data_offset+2] = new_color
    if texture_type == "RGBA8":
        colors = []
        for i in range(size // 64):
            data_offset = i * 64
            j = 0
            for k in range(16):
                colors.append(RGBA(data[data_offset+j+1], data[data_offset+j+32], data[data_offset+j+33], data[data_offset+j]))
                j += 2
        randomize_colors(colors)
        color_index = 0
        for i in range(size // 64):
            data_offset = i * 64
            j = 0
            for k in range(16):
                data[data_offset+j+1] = colors[color_index].red
                data[data_offset+j+32] = colors[color_index].green
                data[data_offset+j+33] = colors[color_index].blue
                data[data_offset+j] = colors[color_index].alpha
                j += 2
                color_index += 1
    file.file.file_data[offset:offset + size] = data

def color_mod(_seed): # Use DAT Texture Wizard as a reference
    # Title Screen
    global global_adjust
    global global_method_select
    global global_swap_select
    seed(_seed)
    title_screen = FileColorData(b'GmTtAll.usd')
    global_method_select = rng(0,global_num_methods)
    global_adjust = [rng(-75,75), rng(-75,75), rng(-75,75)]
    randomize_texture_color(title_screen, 0x13980, 0x200, "CMPR")
    randomize_texture_color(title_screen, 0x15C80, 0x200, "CMPR")
    randomize_texture_color(title_screen, 0x2FC60, 0x200, "CMPR")
    randomize_texture_color(title_screen, 0x2FE60, 0x200, "CMPR")
    randomize_texture_color(title_screen, 0x30060, 0x200, "CMPR")
    randomize_texture_color(title_screen, 0x30260, 0x200, "CMPR")
    randomize_texture_color(title_screen, 0x30460, 0x200, "CMPR")
    randomize_texture_color(title_screen, 0x30660, 0x200, "CMPR")
    randomize_texture_color(title_screen, 0x30860, 0x200, "CMPR")
    randomize_texture_color(title_screen, 0x30A60, 0x200, "CMPR")
    randomize_texture_color(title_screen, 0x30C60, 0x200, "CMPR")
    randomize_texture_color(title_screen, 0x30E60, 0x200, "CMPR")
    randomize_texture_color(title_screen, 0x31060, 0x200, "CMPR")
    randomize_texture_color(title_screen, 0x31260, 0x200, "CMPR")
    randomize_texture_color(title_screen, 0x31460, 0x200, "CMPR")
    randomize_texture_color(title_screen, 0x31660, 0x200, "CMPR")
    randomize_texture_color(title_screen, 0x31860, 0x200, "CMPR")
    randomize_texture_color(title_screen, 0x31A60, 0x200, "CMPR")
    randomize_texture_color(title_screen, 0x31C60, 0x200, "CMPR")
    randomize_texture_color(title_screen, 0x31E60, 0x200, "CMPR")
    randomize_texture_color(title_screen, 0x32060, 0x200, "CMPR")
    randomize_texture_color(title_screen, 0x32260, 0x200, "CMPR")
    randomize_texture_color(title_screen, 0x32460, 0x200, "CMPR")
    randomize_texture_color(title_screen, 0x32660, 0x200, "CMPR")
    randomize_texture_color(title_screen, 0x32860, 0x200, "CMPR")
    randomize_texture_color(title_screen, 0x32A60, 0x200, "CMPR")
    randomize_texture_color(title_screen, 0x32C60, 0x200, "CMPR")
    randomize_texture_color(title_screen, 0x32E60, 0x200, "CMPR")
    randomize_texture_color(title_screen, 0x33060, 0x200, "CMPR")
    randomize_texture_color(title_screen, 0x33260, 0x200, "CMPR")
    title_screen.add_zero_seven(0x19D0)
    title_screen.add_zero_seven(0x2CA8)
    title_screen.add_zero_seven(0x2E40)
    title_screen.add_zero_seven(0x2F00)
    title_screen.add_zero_seven(0x2FC0)
    title_screen.add_zero_seven(0x3080)
    title_screen.add_four_two_four_eight(0x1740)
    title_screen.add_four_two_four_eight(0x1800)
    title_screen.add_four_two_four_eight(0x18C0)
    title_screen.add_four_two_four_eight(0x1980)
    title_screen.add_four_two_four_eight(0x1A40)
    title_screen.add_four_two_four_eight(0x1B74)
    title_screen.add_four_two_four_eight(0x1CA8)
    title_screen.add_four_two_four_eight(0x1DDC)
    title_screen.add_four_two_four_eight(0x1F10)
    title_screen.add_four_two_four_eight(0x2044)
    title_screen.add_four_two_four_eight(0x2178)
    title_screen.add_four_two_four_eight(0x22AC)
    title_screen.add_four_two_four_eight(0x23E0)
    title_screen.add_four_two_four_eight(0x2514)
    title_screen.add_four_two_four_eight(0x2648)
    title_screen.add_four_two_four_eight(0x277C)
    title_screen.add_four_two_four_eight(0x28B0)
    title_screen.add_four_two_four_eight(0x29E4)
    title_screen.add_four_two_four_eight(0x2B18)
    title_screen.add_four_two_four_eight(0x2C4C)
    title_screen.add_four_two_four_eight(0x2D18)
    title_screen.add_four_two_four_eight(0x2DC4)
    title_screen.add_four_two_four_eight(0x2DF0)
    title_screen.add_four_two_four_eight(0x2EB0)
    title_screen.add_four_two_four_eight(0x2F70)
    title_screen.add_four_two_four_eight(0x3030)
    title_screen.add_four_two_four_eight(0x30F0)
    title_screen.add_four_two_four_eight(0x3190)
    title_screen.add_four_two_four_eight(0x31BC)
    title_screen.add_four_two_four_eight(0x392F4)
    title_screen.add_four_two_four_eight(0x39448)
    title_screen.add_four_two_four_eight(0x394F4)
    title_screen.add_four_two_four_eight(0x39614)
    title_screen.add_four_two_four_eight(0x39734)
    title_screen.randomize_all()

    title_screen_b = FileColorData(b'GmTitle.usd')
    title_screen_b.add_zero_seven(0x21A8)
    title_screen_b.add_zero_seven(0x2268)
    title_screen_b.add_zero_seven(0x2334)
    title_screen_b.add_zero_seven(0x23F4)
    title_screen_b.add_zero_seven(0x24B4)
    title_screen_b.add_zero_seven(0x2754)
    title_screen_b.add_zero_seven(0x2640)
    title_screen_b.add_zero_seven(0x26D4)
    title_screen_b.add_zero_seven(0x2768)
    title_screen_b.add_zero_seven(0x2AEC)
    title_screen_b.add_four_two_four_eight(0x2218)
    title_screen_b.add_four_two_four_eight(0x22D8)
    title_screen_b.add_four_two_four_eight(0x23A4)
    title_screen_b.add_four_two_four_eight(0x2464)
    title_screen_b.add_four_two_four_eight(0x25E4)
    title_screen_b.add_four_two_four_eight(0x27D8)
    title_screen_b.add_four_two_four_eight(0x2898)
    title_screen_b.add_four_two_four_eight(0x2944)
    title_screen_b.add_four_two_four_eight(0x29F0)
    title_screen_b.add_four_two_four_eight(0x2A90)
    title_screen_b.add_four_two_four_eight(0x2BF0)
    title_screen_b.add_four_two_four_eight(0x2C90)
    title_screen_b.randomize_all()

    # Main Menu
    global_method_select = rng(0,global_num_methods)
    global_adjust = [rng(-75,75), rng(-75,75), rng(-75,75)]
    main_menu = FileColorData(b'MnMaAll.usd')
    randomize_texture_color(main_menu, 0x19C940, 0x20, "RGB5A3")
    randomize_texture_color(main_menu, 0x19D840, 0x20, "RGB5A3")
    randomize_texture_color(main_menu, 0x1BBA40, 0x20, "RGB5A3")
    randomize_texture_color(main_menu, 0x1E0060, 0x20, "RGB5A3")
    main_menu.add_zero_seven(0x109C)
    main_menu.add_zero_seven(0x115C)
    main_menu.add_zero_seven(0x2548)
    main_menu.add_zero_seven(0x3008)
    main_menu.add_zero_seven(0x43BC)
    main_menu.add_zero_seven(0x1D77C)
    main_menu.add_zero_seven(0x1D83C)
    main_menu.add_zero_seven(0x1D8FC)
    main_menu.add_zero_seven(0x1D9BC)
    main_menu.add_zero_seven(0x1DA7C)
    main_menu.add_zero_seven(0x1DB3C)
    main_menu.add_zero_seven(0x134F8)
    main_menu.add_zero_seven(0x1E85C)
    main_menu.add_zero_seven(0x1EA80)
    main_menu.add_zero_seven(0x1EB4C)
    main_menu.add_zero_seven(0x1EC18)
    main_menu.add_zero_seven(0x1ECE4)
    main_menu.add_zero_seven(0x1EDB0)
    main_menu.add_zero_seven(0x1EE7C)
    main_menu.add_zero_seven(0x1EFF4)
    main_menu.add_zero_seven(0x6B870)
    main_menu.add_zero_seven(0x6B930)
    main_menu.add_zero_seven(0x6BB3C)
    main_menu.add_zero_seven(0x6B930)
    main_menu.add_zero_seven(0x6C048)
    main_menu.add_zero_seven(0x6C114)
    main_menu.add_zero_seven(0x6C1E0)
    main_menu.add_zero_seven(0x6B930)
    main_menu.add_zero_seven(0x6C2AC)
    main_menu.add_zero_seven(0x6C378)
    main_menu.add_zero_seven(0x6B930)
    main_menu.add_zero_seven(0x6C444)
    main_menu.add_zero_seven(0x6C5A4)
    main_menu.add_zero_seven(0xB9FA8)
    main_menu.add_zero_seven(0xBA068)
    main_menu.add_zero_seven(0xBA134)
    main_menu.add_zero_seven(0xBA200)
    main_menu.add_zero_seven(0xBA524)
    main_menu.add_zero_seven(0xBA6B0)
    main_menu.add_zero_seven(0xBDEB0)
    main_menu.add_zero_seven(0xFFA0C)
    main_menu.add_zero_seven(0x10423C)
    main_menu.add_zero_seven(0x104448)
    main_menu.add_zero_seven(0x10423C)
    main_menu.add_zero_seven(0x12DCA0)
    main_menu.add_zero_seven(0x12DE00)
    main_menu.add_zero_seven(0x12E000)
    main_menu.add_zero_seven(0x12DCA0)
    main_menu.add_zero_seven(0x12E200)
    main_menu.add_zero_seven(0x12DCA0)
    main_menu.add_zero_seven(0x13082C)
    main_menu.add_zero_seven(0x135180)
    main_menu.add_zero_seven(0x198FC4)
    main_menu.add_zero_seven(0x199084)
    main_menu.add_zero_seven(0x1BDC14)
    main_menu.add_zero_seven(0x1D1D04)
    main_menu.add_zero_seven(0x1D1DC4)
    main_menu.add_zero_seven(0x1D1F50)
    main_menu.add_zero_seven(0x1D2010)
    main_menu.add_zero_seven(0x1D45EC)
    main_menu.add_zero_seven(0x1D474C)
    main_menu.add_zero_seven(0x1D48AC)
    main_menu.add_zero_seven(0x1D4A0C)
    main_menu.add_zero_seven(0x1D4B6C)
    main_menu.add_zero_seven(0x1D4CCC)
    main_menu.add_zero_seven(0x1DE30C)
    main_menu.add_zero_seven(0x1E60E4)
    main_menu.add_zero_seven(0x1E6244)
    main_menu.add_zero_seven(0x1EAEB8)
    main_menu.add_zero_seven(0x1EAF84)
    main_menu.add_zero_seven(0x1F3634)
    main_menu.add_zero_seven(0x1F8CBC)
    main_menu.add_zero_seven(0x1F8D7C)
    main_menu.add_zero_seven(0x1F8E3C)
    main_menu.add_zero_seven(0x1F8FBC)
    main_menu.add_zero_seven(0x1F907C)
    main_menu.add_zero_seven(0x1F913C)
    main_menu.add_zero_seven(0x1FD034)
    main_menu.add_four_two_four_eight(0xCD0)
    main_menu.add_four_two_four_eight(0xD70)
    main_menu.add_four_two_four_eight(0xE1C)
    main_menu.add_four_two_four_eight(0xEE8)
    main_menu.add_four_two_four_eight(0xF94)
    main_menu.add_four_two_four_eight(0x1040)
    main_menu.add_four_two_four_eight(0x110C)
    main_menu.add_four_two_four_eight(0x11CC)
    main_menu.add_four_two_four_eight(0x1278)
    main_menu.add_four_two_four_eight(0x1324)
    main_menu.add_four_two_four_eight(0x13D0)
    main_menu.add_four_two_four_eight(0x147C)
    main_menu.add_four_two_four_eight(0x1528)
    main_menu.add_four_two_four_eight(0x15D4)
    main_menu.add_four_two_four_eight(0x1680)
    main_menu.add_four_two_four_eight(0x172C)
    main_menu.add_four_two_four_eight(0x17CC)
    main_menu.add_four_two_four_eight(0x186C)
    main_menu.add_four_two_four_eight(0x190C)
    main_menu.add_four_two_four_eight(0x19AC)
    main_menu.add_four_two_four_eight(0x1A4C)
    main_menu.add_four_two_four_eight(0x1AEC)
    main_menu.add_four_two_four_eight(0x1B8C)
    main_menu.add_four_two_four_eight(0x1C2C)
    main_menu.add_four_two_four_eight(0x1CCC)
    main_menu.add_four_two_four_eight(0x1D6C)
    main_menu.add_four_two_four_eight(0x1E0C)
    main_menu.add_four_two_four_eight(0x1EAC)
    main_menu.add_four_two_four_eight(0x1F4C)
    main_menu.add_four_two_four_eight(0x1FEC)
    main_menu.add_four_two_four_eight(0x208C)
    main_menu.add_four_two_four_eight(0x2BF8)
    main_menu.add_four_two_four_eight(0x2C98)
    main_menu.add_four_two_four_eight(0x2D38)
    main_menu.add_four_two_four_eight(0x2DD8)
    main_menu.add_four_two_four_eight(0x2E78)
    main_menu.add_four_two_four_eight(0x2F18)
    main_menu.add_four_two_four_eight(0x2FB8)
    main_menu.add_four_two_four_eight(0x3078)
    main_menu.add_four_two_four_eight(0x3118)
    main_menu.add_four_two_four_eight(0x31B8)
    main_menu.add_four_two_four_eight(0x2BF8)
    main_menu.add_four_two_four_eight(0x2C98)
    main_menu.add_four_two_four_eight(0x2D38)
    main_menu.add_four_two_four_eight(0x2DD8)
    main_menu.add_four_two_four_eight(0x2E78)
    main_menu.add_four_two_four_eight(0x2F18)
    main_menu.add_four_two_four_eight(0x2FB8)
    main_menu.add_four_two_four_eight(0x3078)
    main_menu.add_four_two_four_eight(0x3118)
    main_menu.add_four_two_four_eight(0x3258)
    main_menu.add_four_two_four_eight(0x32F8)
    main_menu.add_four_two_four_eight(0x3398)
    main_menu.add_four_two_four_eight(0x3438)
    main_menu.add_four_two_four_eight(0x34D8)
    main_menu.add_four_two_four_eight(0x3578)
    main_menu.add_four_two_four_eight(0x3618)
    main_menu.add_four_two_four_eight(0x36B8)
    main_menu.add_four_two_four_eight(0x3758)
    main_menu.add_four_two_four_eight(0x37F8)
    main_menu.add_four_two_four_eight(0x3898)
    main_menu.add_four_two_four_eight(0x3938)
    main_menu.add_four_two_four_eight(0x39D8)
    main_menu.add_four_two_four_eight(0x3A98)
    main_menu.add_four_two_four_eight(0x3B38)
    main_menu.add_four_two_four_eight(0x3BF8)
    main_menu.add_four_two_four_eight(0x3C98)
    main_menu.add_four_two_four_eight(0x3D38)
    main_menu.add_four_two_four_eight(0x3DD8)
    main_menu.add_four_two_four_eight(0x3E78)
    main_menu.add_four_two_four_eight(0x3F8C)
    main_menu.add_four_two_four_eight(0x402C)
    main_menu.add_four_two_four_eight(0x40CC)
    main_menu.add_four_two_four_eight(0x416C)
    main_menu.add_four_two_four_eight(0x420C)
    main_menu.add_four_two_four_eight(0x42AC)
    main_menu.add_four_two_four_eight(0x436C)
    main_menu.add_four_two_four_eight(0x442C)
    main_menu.add_four_two_four_eight(0x436C)
    main_menu.add_four_two_four_eight(0x442C)
    main_menu.add_four_two_four_eight(0x137C0)
    main_menu.add_four_two_four_eight(0x1D7EC)
    main_menu.add_four_two_four_eight(0x1D8AC)
    main_menu.add_four_two_four_eight(0x1D96C)
    main_menu.add_four_two_four_eight(0x1DA2C)
    main_menu.add_four_two_four_eight(0x1DAEC)
    main_menu.add_four_two_four_eight(0x1DBAC)
    main_menu.add_four_two_four_eight(0x1DC4C)
    main_menu.add_four_two_four_eight(0x1DC78)
    main_menu.add_four_two_four_eight(0x1DD18)
    main_menu.add_four_two_four_eight(0x1DDB8)
    main_menu.add_four_two_four_eight(0x1DE58)
    main_menu.add_four_two_four_eight(0x1DE84)
    main_menu.add_four_two_four_eight(0x1DF24)
    main_menu.add_four_two_four_eight(0x1DF50)
    main_menu.add_four_two_four_eight(0x1DFF0)
    main_menu.add_four_two_four_eight(0x1E090)
    main_menu.add_four_two_four_eight(0x1E0BC)
    main_menu.add_four_two_four_eight(0x1E15C)
    main_menu.add_four_two_four_eight(0x1E1FC)
    main_menu.add_four_two_four_eight(0x1E29C)
    main_menu.add_four_two_four_eight(0x1E33C)
    main_menu.add_four_two_four_eight(0x1E3DC)
    main_menu.add_four_two_four_eight(0x1E49C)
    main_menu.add_four_two_four_eight(0x1E568)
    main_menu.add_four_two_four_eight(0x1E608)
    main_menu.add_four_two_four_eight(0x1E6A8)
    main_menu.add_four_two_four_eight(0x1E754)
    main_menu.add_four_two_four_eight(0x1E800)
    main_menu.add_four_two_four_eight(0x1E8CC)
    main_menu.add_four_two_four_eight(0x1E978)
    main_menu.add_four_two_four_eight(0x1EA24)
    main_menu.add_four_two_four_eight(0x1EAF0)
    main_menu.add_four_two_four_eight(0x1EBBC)
    main_menu.add_four_two_four_eight(0x1EC88)
    main_menu.add_four_two_four_eight(0x1ED54)
    main_menu.add_four_two_four_eight(0x1EE20)
    main_menu.add_four_two_four_eight(0x1EEEC)
    main_menu.add_four_two_four_eight(0x1EF98)
    main_menu.add_four_two_four_eight(0x1F064)
    main_menu.add_four_two_four_eight(0x1F110)
    main_menu.add_four_two_four_eight(0x1F1BC)
    main_menu.add_four_two_four_eight(0x1F25C)
    main_menu.add_four_two_four_eight(0x1F2FC)
    main_menu.add_four_two_four_eight(0x1F39C)
    main_menu.add_four_two_four_eight(0x6B814)
    main_menu.add_four_two_four_eight(0x6B8E0)
    main_menu.add_four_two_four_eight(0x6B9A0)
    main_menu.add_four_two_four_eight(0x6BAEC)
    main_menu.add_four_two_four_eight(0x6BBAC)
    main_menu.add_four_two_four_eight(0x6BC58)
    main_menu.add_four_two_four_eight(0x6BD04)
    main_menu.add_four_two_four_eight(0x6BDB0)
    main_menu.add_four_two_four_eight(0x6BE5C)
    main_menu.add_four_two_four_eight(0x6BE94)
    main_menu.add_four_two_four_eight(0x6BF40)
    main_menu.add_four_two_four_eight(0x6BFEC)
    main_menu.add_four_two_four_eight(0x6C0B8)
    main_menu.add_four_two_four_eight(0x6C184)
    main_menu.add_four_two_four_eight(0x6C250)
    main_menu.add_four_two_four_eight(0x6C31C)
    main_menu.add_four_two_four_eight(0x6C3E8)
    main_menu.add_four_two_four_eight(0x6C4B4)
    main_menu.add_four_two_four_eight(0x6C614)
    main_menu.add_four_two_four_eight(0xFFA7C)
    main_menu.add_four_two_four_eight(0xFFB1C)
    main_menu.add_four_two_four_eight(0xFFE14)
    main_menu.add_four_two_four_eight(0xBA018)
    main_menu.add_four_two_four_eight(0xBA0D8)
    main_menu.add_four_two_four_eight(0xBA1A4)
    main_menu.add_four_two_four_eight(0xBA270)
    main_menu.add_four_two_four_eight(0xBA33C)
    main_menu.add_four_two_four_eight(0xBA408)
    main_menu.add_four_two_four_eight(0xBA4D4)
    main_menu.add_four_two_four_eight(0xBA594)
    main_menu.add_four_two_four_eight(0xBA654)
    main_menu.add_four_two_four_eight(0xBA720)
    main_menu.add_four_two_four_eight(0xFF990)
    main_menu.add_four_two_four_eight(0xFF9BC)
    main_menu.add_four_two_four_eight(0xFFA7C)
    main_menu.add_four_two_four_eight(0xFFB1C)
    main_menu.add_four_two_four_eight(0xFFBDC)
    main_menu.add_four_two_four_eight(0xFFC7C)
    main_menu.add_four_two_four_eight(0xFFCA8)
    main_menu.add_four_two_four_eight(0xFFCD4)
    main_menu.add_four_two_four_eight(0xFFD74)
    main_menu.add_four_two_four_eight(0xFFE14)
    main_menu.add_four_two_four_eight(0x1042AC)
    main_menu.add_four_two_four_eight(0x10434C)
    main_menu.add_four_two_four_eight(0x1043EC)
    main_menu.add_four_two_four_eight(0x1044B8)
    main_menu.add_four_two_four_eight(0x104558)
    main_menu.add_four_two_four_eight(0x1045F8)
    main_menu.add_four_two_four_eight(0x1046B8)
    main_menu.add_four_two_four_eight(0x104758)
    main_menu.add_four_two_four_eight(0x10B424)
    main_menu.add_four_two_four_eight(0x10BD64)
    main_menu.add_four_two_four_eight(0x10C8CC)
    main_menu.add_four_two_four_eight(0x10D1AC)
    main_menu.add_four_two_four_eight(0x10E100)
    main_menu.add_four_two_four_eight(0x10E1A0)
    main_menu.add_four_two_four_eight(0x10E684)
    main_menu.add_four_two_four_eight(0x11002C)
    main_menu.add_four_two_four_eight(0x110804)
    main_menu.add_four_two_four_eight(0x110FC4)
    main_menu.add_four_two_four_eight(0x11178C)
    main_menu.add_four_two_four_eight(0x1126C8)
    main_menu.add_four_two_four_eight(0x112788)
    main_menu.add_four_two_four_eight(0x1127B4)
    main_menu.add_four_two_four_eight(0x119B74)
    main_menu.add_four_two_four_eight(0x119C14)
    main_menu.add_four_two_four_eight(0x119CB4)
    main_menu.add_four_two_four_eight(0x119D74)
    main_menu.add_four_two_four_eight(0x123F5A)
    main_menu.add_four_two_four_eight(0x12C518)
    main_menu.add_four_two_four_eight(0x12C984)
    main_menu.add_four_two_four_eight(0x12CA24)
    main_menu.add_four_two_four_eight(0x12DC24)
    main_menu.add_four_two_four_eight(0x12DC50)
    main_menu.add_four_two_four_eight(0x12DD10)
    main_menu.add_four_two_four_eight(0x12DDB0)
    main_menu.add_four_two_four_eight(0x12DE70)
    main_menu.add_four_two_four_eight(0x12DF10)
    main_menu.add_four_two_four_eight(0x12DFB0)
    main_menu.add_four_two_four_eight(0x12E070)
    main_menu.add_four_two_four_eight(0x12E110)
    main_menu.add_four_two_four_eight(0x12E1B0)
    main_menu.add_four_two_four_eight(0x12E270)
    main_menu.add_four_two_four_eight(0x12E310)
    main_menu.add_four_two_four_eight(0x13089C)
    main_menu.add_four_two_four_eight(0x131EDC)
    main_menu.add_four_two_four_eight(0x1320BC)
    main_menu.add_four_two_four_eight(0x17FB50)
    main_menu.add_four_two_four_eight(0x17FB7C)
    main_menu.add_four_two_four_eight(0x17FBA8)
    main_menu.add_four_two_four_eight(0x18D180)
    main_menu.add_four_two_four_eight(0x18D2EC)
    main_menu.add_four_two_four_eight(0x18D318)
    main_menu.add_four_two_four_eight(0x18D3B8)
    main_menu.add_four_two_four_eight(0x18D458)
    main_menu.add_four_two_four_eight(0x18D4F8)
    main_menu.add_four_two_four_eight(0x18D598)
    main_menu.add_four_two_four_eight(0x18D638)
    main_menu.add_four_two_four_eight(0x194CC8)
    main_menu.add_four_two_four_eight(0x194E08)
    main_menu.add_four_two_four_eight(0x194EA8)
    main_menu.add_four_two_four_eight(0x194F48)
    main_menu.add_four_two_four_eight(0x198F48)
    main_menu.add_four_two_four_eight(0x19DB78)
    main_menu.add_four_two_four_eight(0x19E1DC)
    main_menu.add_four_two_four_eight(0x19E47C)
    main_menu.add_four_two_four_eight(0x19E5BC)
    main_menu.add_four_two_four_eight(0x19E6FC)
    main_menu.add_four_two_four_eight(0x19E79C)
    main_menu.add_four_two_four_eight(0x19EBB0)
    main_menu.add_four_two_four_eight(0x1AC9E0)
    main_menu.add_four_two_four_eight(0x1ACDC0)
    main_menu.add_four_two_four_eight(0x1BD5CC)
    main_menu.add_four_two_four_eight(0x1BD70C)
    main_menu.add_four_two_four_eight(0x1D1ED4)
    main_menu.add_four_two_four_eight(0x1DE5D4)
    main_menu.add_four_two_four_eight(0x1DE600)
    main_menu.add_four_two_four_eight(0x1E5580)
    main_menu.add_four_two_four_eight(0x1E55AC)
    main_menu.add_four_two_four_eight(0x1EB2DC)
    main_menu.add_four_two_four_eight(0x1EB37C)
    main_menu.add_four_two_four_eight(0x1EB3A8)
    main_menu.add_four_two_four_eight(0x1EB3D4)
    main_menu.add_four_two_four_eight(0x1EB474)
    main_menu.add_four_two_four_eight(0x1EB514)
    main_menu.add_four_two_four_eight(0x1EB540)
    main_menu.add_four_two_four_eight(0x1EB56C)
    main_menu.add_four_two_four_eight(0x1EB60C)
    main_menu.add_four_two_four_eight(0x1EB6AC)
    main_menu.add_four_two_four_eight(0x1EB74C)
    main_menu.add_four_two_four_eight(0x1EEDE8)
    main_menu.add_four_two_four_eight(0x1EEE88)
    main_menu.add_four_two_four_eight(0x1EF2D4)
    main_menu.add_four_two_four_eight(0x1EF394)
    main_menu.add_four_two_four_eight(0x1EF3C0)
    main_menu.add_four_two_four_eight(0x1EF3EC)
    main_menu.add_four_two_four_eight(0x1F35E4)
    main_menu.add_four_two_four_eight(0x1F36A4)
    main_menu.add_four_two_four_eight(0x1F3764)
    main_menu.add_four_two_four_eight(0x1F8D2C)
    main_menu.add_four_two_four_eight(0x1F8DEC)
    main_menu.add_four_two_four_eight(0x1F8EAC)
    main_menu.add_four_two_four_eight(0x1F8F6C)
    main_menu.add_four_two_four_eight(0x1F902C)
    main_menu.add_four_two_four_eight(0x1F90EC)
    main_menu.add_four_two_four_eight(0x1F91AC)
    main_menu.add_four_two_four_eight(0x1F926C)
    main_menu.add_four_two_four_eight(0x1FD0A4)
    main_menu.add_four_two_four_eight(0x1FD144)
    main_menu.add_matrix(0xBA900)
    main_menu.randomize_all()

    # Character Select
    global_method_select = rng(0,global_num_methods)
    global_adjust = [rng(-75,75), rng(-75,75), rng(-75,75)]
    character_select = FileColorData(b'MnSlChr.usd')
    randomize_texture_color(character_select, 0x13100, 0x20, "RGB5A3")
    #randomize_texture_color(character_select, 0x14FA0, 0x200, "RGB5A3") # Falcon
    #randomize_texture_color(character_select, 0x92A20, 0x200, "RGB5A3") # Falcon
    #randomize_texture_color(character_select, 0x125420, 0x200, "RGB5A3") # Falcon
    #randomize_texture_color(character_select, 0x376220, 0x20, "RGB5A3") # Falcon
    #randomize_texture_color(character_select, 0x376640, 0x20, "RGB5A3") # Falcon
    randomize_texture_color(character_select, 0x3767A0, 0x20, "RGB5A3")
    #randomize_texture_color(character_select, 0x379640, 0x20, "RGB5A3") # Falcon?
    character_select.add_zero_seven(0x1005C)
    character_select.add_zero_seven(0x1012C)
    character_select.add_zero_seven(0x113A8)
    character_select.add_four_two_four_eight(0x948)
    character_select.add_four_two_four_eight(0x974)
    character_select.add_four_two_four_eight(0x9A0)
    character_select.add_four_two_four_eight(0x9CC)
    character_select.add_four_two_four_eight(0x9F8)
    character_select.add_four_two_four_eight(0xA24)
    character_select.add_four_two_four_eight(0xA50)
    character_select.add_four_two_four_eight(0xA7C)
    character_select.add_four_two_four_eight(0xAA8)
    character_select.add_four_two_four_eight(0xAD4)
    character_select.add_four_two_four_eight(0xB00)
    character_select.add_four_two_four_eight(0xB2C)
    character_select.add_four_two_four_eight(0xB58)
    character_select.add_four_two_four_eight(0xB84)
    character_select.add_four_two_four_eight(0xBB0)
    character_select.add_four_two_four_eight(0xBDC)
    character_select.add_four_two_four_eight(0xC08)
    character_select.add_four_two_four_eight(0xC34)
    character_select.add_four_two_four_eight(0xC60)
    character_select.add_four_two_four_eight(0xC8C)
    character_select.add_four_two_four_eight(0xCB8)
    character_select.add_four_two_four_eight(0xCE4)
    character_select.add_four_two_four_eight(0xD10)
    character_select.add_four_two_four_eight(0xD3C)
    character_select.add_four_two_four_eight(0xD68)
    character_select.add_four_two_four_eight(0xD94)
    character_select.add_four_two_four_eight(0xDC0)
    character_select.add_four_two_four_eight(0xDEC)
    character_select.add_four_two_four_eight(0xE18)
    character_select.add_four_two_four_eight(0xE44)
    character_select.add_four_two_four_eight(0xE70)
    character_select.add_four_two_four_eight(0xE9C)
    character_select.add_four_two_four_eight(0xEC8)
    character_select.add_four_two_four_eight(0xEF4)
    character_select.add_four_two_four_eight(0xF20)
    character_select.add_four_two_four_eight(0xF4C)
    character_select.add_four_two_four_eight(0xF78)
    character_select.add_four_two_four_eight(0xFA4)
    character_select.add_four_two_four_eight(0xFD0)
    character_select.add_four_two_four_eight(0xFFC)
    character_select.add_four_two_four_eight(0x1028)
    character_select.add_four_two_four_eight(0x1054)
    character_select.add_four_two_four_eight(0x1080)
    character_select.add_four_two_four_eight(0x10AC)
    character_select.add_four_two_four_eight(0x10D8)
    character_select.add_four_two_four_eight(0x1104)
    character_select.add_four_two_four_eight(0x1130)
    character_select.add_four_two_four_eight(0x115C)
    character_select.add_four_two_four_eight(0x1188)
    character_select.add_four_two_four_eight(0x11B4)
    character_select.add_four_two_four_eight(0x11E0)
    character_select.add_four_two_four_eight(0x120C)
    character_select.add_four_two_four_eight(0x1238)
    character_select.add_four_two_four_eight(0x1264)
    character_select.add_four_two_four_eight(0x1290)
    character_select.add_four_two_four_eight(0x12BC)
    character_select.add_four_two_four_eight(0x12E8)
    character_select.add_four_two_four_eight(0x1314)
    character_select.add_four_two_four_eight(0x1340)
    character_select.add_four_two_four_eight(0x136C)
    character_select.add_four_two_four_eight(0x13C4)
    character_select.add_four_two_four_eight(0x13F0)
    character_select.add_four_two_four_eight(0x141C)
    character_select.add_four_two_four_eight(0x1448)
    character_select.add_four_two_four_eight(0x1474)
    character_select.add_four_two_four_eight(0x14A0)
    character_select.add_four_two_four_eight(0x14CC)
    character_select.add_four_two_four_eight(0x14F8)
    character_select.add_four_two_four_eight(0x1524)
    character_select.add_four_two_four_eight(0x1550)
    character_select.add_four_two_four_eight(0x157C)
    character_select.add_four_two_four_eight(0x15A8)
    character_select.add_four_two_four_eight(0x15D4)
    character_select.add_four_two_four_eight(0x1600)
    character_select.add_four_two_four_eight(0x162C)
    character_select.add_four_two_four_eight(0x1658)
    character_select.add_four_two_four_eight(0x1684)
    character_select.add_four_two_four_eight(0x16B0)
    character_select.add_four_two_four_eight(0x16DC)
    character_select.add_four_two_four_eight(0x1708)
    character_select.add_four_two_four_eight(0x1734)
    character_select.add_four_two_four_eight(0x1760)
    character_select.add_four_two_four_eight(0x178C)
    character_select.add_four_two_four_eight(0x17B8)
    character_select.add_four_two_four_eight(0x17E4)
    character_select.add_four_two_four_eight(0x1810)
    character_select.add_four_two_four_eight(0x183C)
    character_select.add_four_two_four_eight(0x1868)
    character_select.add_four_two_four_eight(0x1894)
    character_select.add_four_two_four_eight(0x18C0)
    character_select.add_four_two_four_eight(0x18EC)
    character_select.add_four_two_four_eight(0x1918)
    character_select.add_four_two_four_eight(0x1944)
    character_select.add_four_two_four_eight(0x1970)
    character_select.add_four_two_four_eight(0x199C)
    character_select.add_four_two_four_eight(0x19C8)
    character_select.add_four_two_four_eight(0x100CC)
    character_select.add_four_two_four_eight(0x1019C)
    character_select.add_four_two_four_eight(0x11348)
    character_select.add_four_two_four_eight(0x11418)
    character_select.add_four_two_four_eight(0x2004F)
    character_select.add_four_two_four_eight(0x348EF8)
    character_select.add_four_two_four_eight(0x348FB8)
    character_select.add_four_two_four_eight(0x349078)
    character_select.add_four_two_four_eight(0x349138)
    character_select.add_four_two_four_eight(0x3491F8)
    character_select.add_four_two_four_eight(0x349224)
    character_select.add_four_two_four_eight(0x3492E4)
    character_select.add_four_two_four_eight(0x3493A4)
    character_select.add_four_two_four_eight(0x3493D0)
    character_select.add_four_two_four_eight(0x349490)
    character_select.add_four_two_four_eight(0x349550)
    character_select.add_four_two_four_eight(0x34957C)
    character_select.add_four_two_four_eight(0x34963C)
    character_select.add_four_two_four_eight(0x3496FC)
    character_select.add_four_two_four_eight(0x349728)
    character_select.add_four_two_four_eight(0x3497E8)
    character_select.add_four_two_four_eight(0x3498A8)
    character_select.add_four_two_four_eight(0x349968)
    character_select.add_four_two_four_eight(0x349A28)
    character_select.add_four_two_four_eight(0x349AE8)
    character_select.add_four_two_four_eight(0x349BA8)
    character_select.add_four_two_four_eight(0x349C68)
    character_select.add_four_two_four_eight(0x349D28)
    character_select.add_four_two_four_eight(0x349DE8)
    character_select.add_four_two_four_eight(0x349EA8)
    character_select.add_four_two_four_eight(0x349F68)
    character_select.add_four_two_four_eight(0x34A028)
    character_select.add_four_two_four_eight(0x34A0E8)
    character_select.add_four_two_four_eight(0x34A1A8)
    character_select.add_four_two_four_eight(0x34A268)
    character_select.add_four_two_four_eight(0x34A328)
    character_select.add_four_two_four_eight(0x34A354)
    character_select.add_four_two_four_eight(0x34A380)
    character_select.add_four_two_four_eight(0x34A3AC)
    character_select.add_four_two_four_eight(0x34A3D8)
    character_select.add_four_two_four_eight(0x34A404)
    character_select.add_four_two_four_eight(0x34A430)
    character_select.add_four_two_four_eight(0x34A45C)
    character_select.add_four_two_four_eight(0x34A488)
    character_select.add_four_two_four_eight(0x34A4B4)
    character_select.add_four_two_four_eight(0x34A4E0)
    character_select.add_four_two_four_eight(0x34A50C)
    character_select.add_four_two_four_eight(0x34A538)
    character_select.add_four_two_four_eight(0x34A590)
    character_select.add_four_two_four_eight(0x34A5BC)
    character_select.add_four_two_four_eight(0x34A5E8)
    character_select.add_four_two_four_eight(0x34A614)
    character_select.add_four_two_four_eight(0x34A640)
    character_select.add_four_two_four_eight(0x34A66C)
    character_select.add_four_two_four_eight(0x34A6C4)
    character_select.add_four_two_four_eight(0x34A6F0)
    character_select.add_four_two_four_eight(0x34A71C)
    character_select.add_four_two_four_eight(0x34A748)
    character_select.add_four_two_four_eight(0x34A774)
    character_select.add_four_two_four_eight(0x34A7A0)
    character_select.add_four_two_four_eight(0x34A7CC)
    character_select.add_four_two_four_eight(0x34A7F8)
    character_select.add_four_two_four_eight(0x34A824)
    character_select.add_four_two_four_eight(0x34A850)
    character_select.add_four_two_four_eight(0x34A87C)
    character_select.add_four_two_four_eight(0x34A8A8)
    character_select.add_four_two_four_eight(0x34A8D4)
    character_select.add_four_two_four_eight(0x34A900)
    character_select.add_four_two_four_eight(0x34A92C)
    character_select.add_four_two_four_eight(0x34A958)
    character_select.add_four_two_four_eight(0x34A984)
    character_select.add_four_two_four_eight(0x34A9B0)
    character_select.add_four_two_four_eight(0x34A9DC)
    character_select.add_four_two_four_eight(0x34AA08)
    character_select.add_four_two_four_eight(0x34AA34)
    character_select.add_four_two_four_eight(0x34AAD4)
    character_select.add_four_two_four_eight(0x34AB00)
    character_select.add_four_two_four_eight(0x34ABA0)
    character_select.add_four_two_four_eight(0x34AC60)
    character_select.add_four_two_four_eight(0x34AD20)
    character_select.add_four_two_four_eight(0x34ADE0)
    character_select.add_four_two_four_eight(0x34AE0C)
    character_select.add_four_two_four_eight(0x34AE38)
    character_select.add_four_two_four_eight(0x34AEF8)
    character_select.add_four_two_four_eight(0x34AF24)
    character_select.add_four_two_four_eight(0x34AF50)
    character_select.add_four_two_four_eight(0x34AF7C)
    character_select.add_four_two_four_eight(0x34B01C)
    character_select.add_four_two_four_eight(0x34B048)
    character_select.add_four_two_four_eight(0x34B0E8)
    character_select.add_four_two_four_eight(0x34B1A8)
    character_select.add_four_two_four_eight(0x34B268)
    character_select.add_four_two_four_eight(0x34B328)
    character_select.add_four_two_four_eight(0x34B354)
    character_select.add_four_two_four_eight(0x34B380)
    character_select.add_four_two_four_eight(0x34B440)
    character_select.add_four_two_four_eight(0x34B46C)
    character_select.add_four_two_four_eight(0x34B498)
    character_select.add_four_two_four_eight(0x34B4C4)
    character_select.add_four_two_four_eight(0x34B564)
    character_select.add_four_two_four_eight(0x34B590)
    character_select.add_four_two_four_eight(0x34B630)
    character_select.add_four_two_four_eight(0x34B6F0)
    character_select.add_four_two_four_eight(0x34B7B0)
    character_select.add_four_two_four_eight(0x34B870)
    character_select.add_four_two_four_eight(0x34B89C)
    character_select.add_four_two_four_eight(0x34B8C8)
    character_select.add_four_two_four_eight(0x34B988)
    character_select.add_four_two_four_eight(0x34B9B4)
    character_select.add_four_two_four_eight(0x34B9E0)
    character_select.add_four_two_four_eight(0x34BA0C)
    character_select.add_four_two_four_eight(0x34BAAC)
    character_select.add_four_two_four_eight(0x34BAD8)
    character_select.add_four_two_four_eight(0x34BB78)
    character_select.add_four_two_four_eight(0x34BC38)
    character_select.add_four_two_four_eight(0x34BCF8)
    character_select.add_four_two_four_eight(0x34BDB8)
    character_select.add_four_two_four_eight(0x34BDE4)
    character_select.add_four_two_four_eight(0x34BE10)
    character_select.add_four_two_four_eight(0x34BED0)
    character_select.add_four_two_four_eight(0x34BEFC)
    character_select.add_four_two_four_eight(0x34BF28)
    character_select.add_four_two_four_eight(0x34BFE8)
    character_select.add_four_two_four_eight(0x34C014)
    character_select.add_four_two_four_eight(0x34C0D4)
    character_select.add_four_two_four_eight(0x34C100)
    character_select.add_four_two_four_eight(0x34C1C0)
    character_select.add_four_two_four_eight(0x34C1EC)
    character_select.add_four_two_four_eight(0x34C2AC)
    character_select.add_four_two_four_eight(0x34C2D8)
    #character_select.add_four_two_four_eight(0x34C398)
    #character_select.add_four_two_four_eight(0x34C458)
    #character_select.add_four_two_four_eight(0x34C518)
    #character_select.add_four_two_four_eight(0x34C5D8)
    character_select.add_four_two_four_eight(0x34C698)
    character_select.add_four_two_four_eight(0x34C6C4)
    character_select.add_four_two_four_eight(0x34C784)
    character_select.add_four_two_four_eight(0x34C7B0)
    character_select.add_four_two_four_eight(0x34C870)
    character_select.add_four_two_four_eight(0x34C89C)
    character_select.add_four_two_four_eight(0x34C95C)
    character_select.add_four_two_four_eight(0x34C988)
    character_select.add_four_two_four_eight(0x34C9B4)
    character_select.add_four_two_four_eight(0x34CA74)
    character_select.add_four_two_four_eight(0x34CAA0)
    character_select.add_four_two_four_eight(0x34CB60)
    character_select.add_four_two_four_eight(0x34CB8C)
    character_select.add_four_two_four_eight(0x34CC4C)
    character_select.add_four_two_four_eight(0x34CC78)
    character_select.add_four_two_four_eight(0x34CD38)
    character_select.add_four_two_four_eight(0x34CDF8)
    character_select.add_four_two_four_eight(0x34CEB8)
    character_select.add_four_two_four_eight(0x34CF78)
    character_select.add_four_two_four_eight(0x34D038)
    character_select.add_four_two_four_eight(0x34D0D8)
    character_select.add_four_two_four_eight(0x34D198)
    character_select.add_four_two_four_eight(0x34D258)
    character_select.add_four_two_four_eight(0x34D318)
    character_select.add_four_two_four_eight(0x34D3B8)
    character_select.add_four_two_four_eight(0x34D478)
    character_select.add_four_two_four_eight(0x34D518)
    character_select.add_four_two_four_eight(0x34D5D8)
    character_select.add_four_two_four_eight(0x34D678)
    character_select.add_four_two_four_eight(0x34D738)
    character_select.add_four_two_four_eight(0x34D7D8)
    character_select.add_four_two_four_eight(0x34D898)
    character_select.add_four_two_four_eight(0x34D938)
    character_select.add_four_two_four_eight(0x34D9F8)
    character_select.add_four_two_four_eight(0x34DA98)
    character_select.add_four_two_four_eight(0x34DB58)
    character_select.add_four_two_four_eight(0x34DBF8)
    character_select.add_four_two_four_eight(0x34DCB8)
    character_select.add_four_two_four_eight(0x34DD58)
    character_select.add_four_two_four_eight(0x34DE18)
    character_select.add_four_two_four_eight(0x34DEB8)
    character_select.add_four_two_four_eight(0x34DF78)
    character_select.add_four_two_four_eight(0x34E018)
    character_select.add_four_two_four_eight(0x34E0D8)
    character_select.add_four_two_four_eight(0x34E198)
    character_select.add_four_two_four_eight(0x34E258)
    character_select.add_four_two_four_eight(0x34E2F8)
    character_select.add_four_two_four_eight(0x34E3B8)
    character_select.add_four_two_four_eight(0x34E478)
    character_select.add_four_two_four_eight(0x34E538)
    character_select.add_four_two_four_eight(0x34E5F8)
    character_select.add_four_two_four_eight(0x34E6B8)
    character_select.add_four_two_four_eight(0x34E778)
    character_select.add_four_two_four_eight(0x34E838)
    character_select.add_four_two_four_eight(0x34E8F8)
    character_select.add_four_two_four_eight(0x34E9B8)
    character_select.add_four_two_four_eight(0x34EA78)
    character_select.add_four_two_four_eight(0x34EB38)
    character_select.add_four_two_four_eight(0x34EBD8)
    character_select.add_four_two_four_eight(0x34EC98)
    character_select.add_four_two_four_eight(0x34ED38)
    character_select.add_four_two_four_eight(0x34EDF8)
    character_select.add_four_two_four_eight(0x34EE98)
    character_select.add_four_two_four_eight(0x34EF58)
    character_select.add_four_two_four_eight(0x34EFF8)
    character_select.add_four_two_four_eight(0x34F0B8)
    character_select.add_four_two_four_eight(0x34F158)
    character_select.add_four_two_four_eight(0x34F218)
    character_select.add_four_two_four_eight(0x34F2B8)
    character_select.add_four_two_four_eight(0x34F378)
    character_select.add_four_two_four_eight(0x368D88)
    character_select.add_four_two_four_eight(0x368E48)
    character_select.add_four_two_four_eight(0x368F08)
    character_select.add_four_two_four_eight(0x36DA14)
    character_select.add_four_two_four_eight(0x36DB00)
    character_select.add_four_two_four_eight(0x382EB4)
    character_select.add_four_two_four_eight(0x382F74)
    character_select.add_four_two_four_eight(0x382FA0)
    character_select.add_four_two_four_eight(0x382FCC)
    character_select.add_four_two_four_eight(0x382FF8)
    character_select.add_four_two_four_eight(0x383024)
    character_select.add_four_two_four_eight(0x383050)
    character_select.add_four_two_four_eight(0x383110)
    character_select.add_four_two_four_eight(0x3831D0)
    character_select.add_four_two_four_eight(0x383290)
    character_select.add_four_two_four_eight(0x383350)
    character_select.add_four_two_four_eight(0x3833F0)
    character_select.add_four_two_four_eight(0x38341C)
    character_select.add_four_two_four_eight(0x383448)
    character_select.add_four_two_four_eight(0x3834E8)
    character_select.add_four_two_four_eight(0x383588)
    character_select.add_four_two_four_eight(0x383648)
    character_select.add_four_two_four_eight(0x383708)
    character_select.add_four_two_four_eight(0x3837C8)
    character_select.add_four_two_four_eight(0x383888)
    character_select.add_four_two_four_eight(0x383948)
    character_select.add_four_two_four_eight(0x383A08)
    character_select.add_four_two_four_eight(0x383AC8)
    character_select.add_four_two_four_eight(0x383B88)
    character_select.add_four_two_four_eight(0x383C48)
    character_select.add_four_two_four_eight(0x383C74)
    character_select.add_four_two_four_eight(0x383CA0)
    character_select.add_four_two_four_eight(0x383CCC)
    character_select.add_four_two_four_eight(0x383D8C)
    character_select.add_four_two_four_eight(0x383E4C)
    character_select.add_four_two_four_eight(0x383E78)
    character_select.add_four_two_four_eight(0x383EA4)
    character_select.add_four_two_four_eight(0x383F64)
    character_select.add_four_two_four_eight(0x384024)
    character_select.add_four_two_four_eight(0x3840E4)
    character_select.add_four_two_four_eight(0x3841A4)
    character_select.add_four_two_four_eight(0x384264)
    character_select.add_four_two_four_eight(0x384304)
    character_select.add_four_two_four_eight(0x3843C4)
    character_select.add_four_two_four_eight(0x384484)
    character_select.add_four_two_four_eight(0x384544)
    character_select.add_four_two_four_eight(0x3845E4)
    character_select.add_four_two_four_eight(0x3846A4)
    character_select.add_four_two_four_eight(0x384744)
    character_select.add_four_two_four_eight(0x384804)
    character_select.add_four_two_four_eight(0x3848A4)
    character_select.add_four_two_four_eight(0x384964)
    character_select.add_four_two_four_eight(0x384A04)
    character_select.add_four_two_four_eight(0x384AC4)
    character_select.add_four_two_four_eight(0x384B64)
    character_select.add_four_two_four_eight(0x384C24)
    character_select.add_four_two_four_eight(0x384CC4)
    character_select.add_four_two_four_eight(0x384D84)
    character_select.add_four_two_four_eight(0x384E24)
    character_select.add_four_two_four_eight(0x384EE4)
    character_select.add_four_two_four_eight(0x384F84)
    character_select.add_four_two_four_eight(0x385044)
    character_select.add_four_two_four_eight(0x3850E4)
    character_select.add_four_two_four_eight(0x3851A4)
    character_select.add_four_two_four_eight(0x385244)
    character_select.add_four_two_four_eight(0x385304)
    character_select.add_four_two_four_eight(0x3853C4)
    character_select.add_four_two_four_eight(0x385484)
    character_select.add_four_two_four_eight(0x385524)
    character_select.add_four_two_four_eight(0x3855E4)
    character_select.add_four_two_four_eight(0x3856A4)
    character_select.add_four_two_four_eight(0x385764)
    character_select.add_four_two_four_eight(0x385824)
    character_select.add_four_two_four_eight(0x3858E4)
    character_select.add_four_two_four_eight(0x3859A4)
    character_select.add_four_two_four_eight(0x385A64)
    character_select.add_four_two_four_eight(0x385B24)
    character_select.add_four_two_four_eight(0x385BE4)
    character_select.add_four_two_four_eight(0x385CA4)
    character_select.add_four_two_four_eight(0x385D64)
    character_select.add_four_two_four_eight(0x385E04)
    character_select.add_four_two_four_eight(0x385EC4)
    character_select.add_four_two_four_eight(0x385F64)
    character_select.add_four_two_four_eight(0x386024)
    character_select.add_four_two_four_eight(0x3860C4)
    character_select.add_four_two_four_eight(0x386184)
    character_select.add_four_two_four_eight(0x386224)
    character_select.add_four_two_four_eight(0x3862E4)
    character_select.add_four_two_four_eight(0x386384)
    character_select.add_four_two_four_eight(0x386444)
    character_select.add_four_two_four_eight(0x3864E4)
    character_select.add_four_two_four_eight(0x3865A4)
    character_select.add_four_two_four_eight(0x394900)
    character_select.add_four_two_four_eight(0x39492C)
    character_select.add_four_two_four_eight(0x3949EC)
    character_select.add_four_two_four_eight(0x394AAC)
    character_select.add_four_two_four_eight(0x395A40)
    character_select.add_four_two_four_eight(0x395A6C)
    character_select.add_four_two_four_eight(0x395B2C)
    character_select.add_four_two_four_eight(0x395BEC)
    character_select.add_four_two_four_eight(0x395CAC)
    character_select.add_four_two_four_eight(0x395CD8)
    character_select.add_four_two_four_eight(0x395D04)
    character_select.add_four_two_four_eight(0x395DA4)
    character_select.add_four_two_four_eight(0x395E64)
    character_select.randomize_all()

    # Stage Select
    global_adjust = [rng(-75,75), rng(-75,75), rng(-75,75)]
    stage_select = FileColorData(b'MnSlMap.usd')
    randomize_texture_color(stage_select, 0x880, 0x2000, "CMPR")
    randomize_texture_color(stage_select, 0xBE80, 0x20, "RGB5A3")
    stage_select.add_zero_seven(0x6F08C)
    stage_select.add_zero_seven(0x95A00)
    stage_select.add_zero_seven(0x95B78)
    stage_select.add_zero_seven(0x96C44)
    stage_select.add_four_two_four_eight(0x6D1B0)
    stage_select.add_four_two_four_eight(0x6D250)
    stage_select.add_four_two_four_eight(0x6D2F0)
    stage_select.add_four_two_four_eight(0x6EE1C)
    stage_select.add_four_two_four_eight(0x6F0FC)
    stage_select.add_four_two_four_eight(0x78B24)
    stage_select.add_four_two_four_eight(0x78BC4)
    stage_select.add_four_two_four_eight(0x78C64)
    stage_select.add_four_two_four_eight(0x78D04)
    stage_select.add_four_two_four_eight(0x78DA4)
    stage_select.add_four_two_four_eight(0x78E44)
    stage_select.add_four_two_four_eight(0x78EE4)
    stage_select.add_four_two_four_eight(0x78F84)
    stage_select.add_four_two_four_eight(0x79024)
    stage_select.add_four_two_four_eight(0x790C4)
    stage_select.add_four_two_four_eight(0x79164)
    stage_select.add_four_two_four_eight(0x79204)
    stage_select.add_four_two_four_eight(0x792A4)
    stage_select.add_four_two_four_eight(0x79344)
    stage_select.add_four_two_four_eight(0x793E4)
    stage_select.add_four_two_four_eight(0x79484)
    stage_select.add_four_two_four_eight(0x79524)
    stage_select.add_four_two_four_eight(0x795C4)
    stage_select.add_four_two_four_eight(0x79664)
    stage_select.add_four_two_four_eight(0x79704)
    stage_select.add_four_two_four_eight(0x797A4)
    stage_select.add_four_two_four_eight(0x79844)
    stage_select.add_four_two_four_eight(0x798E4)
    stage_select.add_four_two_four_eight(0x79984)
    stage_select.add_four_two_four_eight(0x79A24)
    stage_select.add_four_two_four_eight(0x79AC4)
    stage_select.add_four_two_four_eight(0x79B64)
    stage_select.add_four_two_four_eight(0x79C04)
    stage_select.add_four_two_four_eight(0x79CA4)
    stage_select.add_four_two_four_eight(0x79D44)
    stage_select.add_four_two_four_eight(0x79DE4)
    stage_select.add_four_two_four_eight(0x79E84)
    stage_select.add_four_two_four_eight(0x79F24)
    stage_select.add_four_two_four_eight(0x79FC4)
    stage_select.add_four_two_four_eight(0x7A064)
    stage_select.add_four_two_four_eight(0x7A104)
    stage_select.add_four_two_four_eight(0x7A1A4)
    stage_select.add_four_two_four_eight(0x7A264)
    stage_select.add_four_two_four_eight(0x7A304)
    stage_select.add_four_two_four_eight(0x7A3A4)
    stage_select.add_four_two_four_eight(0x7A444)
    stage_select.add_four_two_four_eight(0x7A4E4)
    stage_select.add_four_two_four_eight(0x95A70)
    stage_select.add_four_two_four_eight(0x95B1C)
    stage_select.add_four_two_four_eight(0x95BE8)
    stage_select.add_four_two_four_eight(0x960D4)
    stage_select.add_four_two_four_eight(0x96174)
    stage_select.add_four_two_four_eight(0x96234)
    stage_select.add_four_two_four_eight(0x962D4)
    stage_select.add_four_two_four_eight(0x96CB4)
    stage_select.add_four_two_four_eight(0x97404)
    stage_select.add_four_two_four_eight(0x974A4)
    stage_select.add_four_two_four_eight(0x978BC)
    stage_select.add_four_two_four_eight(0x9795C)
    stage_select.add_four_two_four_eight(0x97C04)
    stage_select.add_four_two_four_eight(0x97CA4)
    stage_select.add_four_two_four_eight(0x98130)
    stage_select.add_four_two_four_eight(0x981F0)
    stage_select.randomize_all()

    

    # EfCaData.dat
    global_method_select = rng(0,global_num_methods)
    global_adjust = [rng(-128,128), rng(-128,128), rng(-128,128)]
    falcon_effects = FileColorData(b'EfCaData.dat')
    randomize_texture_color(falcon_effects, 0x12D00, 0x800, "CMPR")
    randomize_texture_color(falcon_effects, 0x13500, 0x200, "CMPR")
    randomize_texture_color(falcon_effects, 0x10D00, 0x2000, "RGB5A3")
    randomize_texture_color(falcon_effects, 0x13700, 0x1000, "RGB5A3")
    randomize_texture_color(falcon_effects, 0x14700, 0x4000, "RGB5A3")
    randomize_texture_color(falcon_effects, 0xFF00, 0x200, "RGB5A3")
    randomize_texture_color(falcon_effects, 0x10100, 0x200, "RGB5A3")
    randomize_texture_color(falcon_effects, 0x10300, 0x200, "RGB5A3")
    falcon_effects.add_cf_two(0x12D, "Down B Smoke")
    falcon_effects.add_cf_two(0x147, "Down B Smoke")
    falcon_effects.add_cf_two(0x157, "Down B Smoke")
    falcon_effects.add_cf_two(0x16A, "Down B Smoke")
    falcon_effects.add_cf_two(0x17A, "Down B Smoke")
    falcon_effects.add_cf_two(0x1D8, "Neutral B Smoke")
    falcon_effects.add_cf_two(0x1E5, "Trailing Smoke Neutral B")
    falcon_effects.add_cf_two(0x216, "Trailing Smoke Neutral B")
    falcon_effects.add_cf_two(0x29A, "Square Dots Neutral B")
    falcon_effects.add_cf_two(0x2AA, "Square Dots Neutral B")
    falcon_effects.add_cf_two(0x3AA, "Smoke on wings of Neutral B")
    falcon_effects.add_cf_two(0x3B7, "Smoke on wings of Neutral B")
    falcon_effects.add_cf_two(0x3ED, "Smoke on wings of Neutral B")
    falcon_effects.add_cf_two(0x472, "Square Dots Down B")
    falcon_effects.add_cf_two(0x482, "Square Dots Down B")
    falcon_effects.add_cf_two(0x4D7, "Circle Dots Down B")
    falcon_effects.add_cf_two(0x4E4, "Circle Dots Down B")
    falcon_effects.add_cf_two(0x537, "Circle Dots Down B")
    falcon_effects.add_cf_two(0x58D, "Trailing Smoke Down B")
    falcon_effects.add_cf_two(0x5A7, "Trailing Smoke Down B")
    falcon_effects.add_cf_two(0x5B7, "Trailing Smoke Down B")
    falcon_effects.add_cf_two(0x5CA, "Trailing Smoke Down B")
    falcon_effects.add_cf_two(0x5DA, "Trailing Smoke Down B")
    falcon_effects.add_cf_two(0x63E, "Trailing Smoke Down B and After Smoke of Over B")
    falcon_effects.add_cf_two(0x64C, "Trailing Smoke Down B and After Smoke of Over B")
    falcon_effects.add_cf_two(0x65A, "Trailing Smoke Down B and After Smoke of Over B")
    falcon_effects.add_cf_two(0x6AD, "Front of Down B")
    falcon_effects.add_cf_two(0x76D, "Smoke of Over B large")
    falcon_effects.add_cf_two(0x77D, "Smoke of Over B small")
    falcon_effects.add_cf_two(0x78D, "Smoke Behind Falcon Over B")
    falcon_effects.add_cf_two(0x79D, "Smoke Behind Falcon Over B")
    falcon_effects.add_cf_two(0x82A, "Square Dots Over B")
    falcon_effects.add_cf_two(0x83A, "Square Dots Over B")
    falcon_effects.add_cf_two(0x89E, "Square Smoke after Over B")
    falcon_effects.add_cf_two(0x8AC, "Smoke after Over B")
    falcon_effects.add_cf_two(0x8BA, "Smoke after Over B")
    falcon_effects.add_cf_two(0x918, "Smoke after neutral B")
    falcon_effects.add_cf_two(0x925, "Smoke after neutral B")
    falcon_effects.add_cf_two(0x956, "Smoke after neutral B")
    falcon_effects.add_zero_seven(0x1DE00, "Tip of the falcon kick")
    falcon_effects.add_zero_seven(0x202EC, "Tip of the falcon punch")
    falcon_effects.add_zero_seven(0x22D64, "Part of Falcon punch lens flare extending lines Beginning")
    falcon_effects.add_zero_seven(0x22E30, "Part of Falcon punch lens flare extending lines Beginning")
    falcon_effects.add_zero_seven(0x22EFC, "Part of Falcon punch lens flare extending lines Beginning")
    falcon_effects.add_zero_seven(0x22FC8, "Part of Falcon punch lens flare extending lines Beginning")
    falcon_effects.add_zero_seven(0x23094, "Part of Falcon punch lens flare extending lines Beginning")
    falcon_effects.add_zero_seven(0x23160, "Part of Falcon punch lens flare extending lines Beginning")
    falcon_effects.add_zero_seven(0x2322C, "Part of Falcon punch lens flare extending lines Beginning")
    falcon_effects.add_zero_seven(0x232F8, "Part of Falcon punch lens flare extending lines Beginning")
    falcon_effects.add_zero_seven(0x233C4, "Part of Falcon punch lens flare extending lines Beginning")
    falcon_effects.add_zero_seven(0x23490, "Part of Falcon punch lens flare extending lines Beginning")
    falcon_effects.add_zero_seven(0x24B74, "Raptor Boost Hand Lens Flare Beginning")
    falcon_effects.add_four_two_four_eight(0x22D08, "Falcon Punch Small Lens Flare Beginning")
    falcon_effects.add_four_two_four_eight(0x235CC, "Falcon Punch Big Lens Flare Beginning")
    falcon_effects.add_four_two_four_eight(0x2543C, "Part of the Raptor Boost Smoke")
    falcon_effects.randomize_all()

    # PlCaNr.dat
    #falcon_normal = FileColorData(b'PlCaNr.dat')
    #randomize_texture_color(falcon_normal, 0x21060, 0x400, "CMPR")
    #randomize_texture_color(falcon_normal, 0x21C60, 0x1000, "CMPR")
    #randomize_texture_color(falcon_normal, 0x22C60, 0x1000, "CMPR")
    #randomize_texture_color(falcon_normal, 0x24C60, 0x1000, "CMPR")
    #randomize_texture_color(falcon_normal, 0x25C60, 0x1000, "CMPR")
    #randomize_texture_color(falcon_normal, 0x2CC60, 0x2000, "CMPR")
    #randomize_texture_color(falcon_normal, 0x30C60, 0x1000, "CMPR")
    #randomize_texture_color(falcon_normal, 0x32C60, 0x1000, "CMPR")
    #randomize_texture_color(falcon_normal, 0x55C60, 0x800, "CMPR")
    #randomize_texture_color(falcon_normal, 0x56C60, 0x2000, "CMPR")
    #randomize_texture_color(falcon_normal, 0x5CC60, 0x2000, "CMPR")
    #randomize_texture_color(falcon_normal, 0x64C60, 0x2000, "CMPR")
    #randomize_texture_color(falcon_normal, 0x6AC60, 0x800, "CMPR")
    #randomize_texture_color(falcon_normal, 0x6BC60, 0x4000, "CMPR")
    #randomize_texture_color(falcon_normal, 0x76C60, 0x800, "CMPR")
    #randomize_texture_color(falcon_normal, 0x77460, 0x1000, "CMPR")
    #randomize_texture_color(falcon_normal, 0x78460, 0x800, "CMPR")
    #randomize_texture_color(falcon_normal, 0x79460, 0x800, "CMPR")

    #PlCaBu.dat
    #falcon_blue = FileColorData(b'PlCaBu.dat')
    #randomize_texture_color(falcon_blue, 0x21040, 0x400, "CMPR")
    #randomize_texture_color(falcon_blue, 0x21C40, 0x1000, "CMPR")
    #randomize_texture_color(falcon_blue, 0x22C40, 0x1000, "CMPR")
    #randomize_texture_color(falcon_blue, 0x24C40, 0x1000, "CMPR")
    #randomize_texture_color(falcon_blue, 0x25C40, 0x1000, "CMPR")
    #randomize_texture_color(falcon_blue, 0x2CC40, 0x2000, "CMPR")
    #randomize_texture_color(falcon_blue, 0x30C40, 0x1000, "CMPR")
    #randomize_texture_color(falcon_blue, 0x32C40, 0x1000, "CMPR")
    #randomize_texture_color(falcon_blue, 0x33C40, 0x2000, "CMPR")
    #randomize_texture_color(falcon_blue, 0x37C40, 0x8000, "CMPR")
    #randomize_texture_color(falcon_blue, 0x47C40, 0x2000, "CMPR")
    #randomize_texture_color(falcon_blue, 0x4FC40, 0x2000, "CMPR")
    #randomize_texture_color(falcon_blue, 0x53C40, 0x1000, "CMPR")
    #randomize_texture_color(falcon_blue, 0x55C40, 0x800, "CMPR")
    #randomize_texture_color(falcon_blue, 0x56C40, 0x2000, "CMPR")
    #randomize_texture_color(falcon_blue, 0x58C40, 0x2000, "CMPR")
    #randomize_texture_color(falcon_blue, 0x5CC40, 0x2000, "CMPR")
    #randomize_texture_color(falcon_blue, 0x60C40, 0x2000, "CMPR")
    #randomize_texture_color(falcon_blue, 0x64C40, 0x2000, "CMPR")
    #randomize_texture_color(falcon_blue, 0x6AC40, 0x800, "CMPR")
    #randomize_texture_color(falcon_blue, 0x6BC40, 0x4000, "CMPR")
    #randomize_texture_color(falcon_blue, 0x76C40, 0x800, "CMPR")
    #randomize_texture_color(falcon_blue, 0x77440, 0x1000, "CMPR")
    #randomize_texture_color(falcon_blue, 0x78440, 0x800, "CMPR")
    #randomize_texture_color(falcon_blue, 0x79440, 0x800, "CMPR")

    # Dr Mario
    global_method_select = rng(0, global_num_methods)
    global_adjust = [rng(-128,128), rng(-128,128), rng(-128,128)]
    dr_mario = FileColorData(b'PlDr.dat')
    dr_mario.add_four_two_four_eight(0x19CAC)
    dr_mario.randomize_all()

    # Fox
    global_method_select = rng(0, global_num_methods)
    global_adjust = [rng(-128,128), rng(-128,128), rng(-128,128)]
    fox = FileColorData(b'PlFx.dat')
    fox.add_four_two_four_eight(0x2204C)
    fox.add_matrix(0x13E20, 2)
    fox.add_matrix(0x13EC0, 2)
    fox.add_matrix(0x13F60, 2)
    fox.add_matrix(0x13E20, 2)
    fox.add_matrix(0x14000, 2)
    fox.add_matrix(0x14023, 2)
    fox.randomize_all()

    # Falco
    global_method_select = rng(0, global_num_methods)
    global_adjust = [rng(-128,128), rng(-128,128), rng(-128,128)]
    falco = FileColorData(b'PlFc.dat')
    falco.add_four_two_four_eight(0x1EC48)
    falco.add_matrix(0x13440, 2)
    falco.add_matrix(0x134E0, 2)
    falco.add_matrix(0x13580, 2)
    falco.add_matrix(0x13620, 2)
    falco.add_matrix(0x13643, 2)
    falco.randomize_all()

    # Fox/Falco Effects
    global_method_select = rng(0, global_num_methods)
    global_adjust = [rng(-128,128), rng(-128,128), rng(-128,128)]
    spacies_effects = FileColorData(b'EfFxData.dat')
    spacies_effects.add_cf_two(0x125)
    spacies_effects.add_cf_two(0x1DE)
    spacies_effects.add_cf_two(0x23E)
    spacies_effects.add_cf_one(0x2EE)
    spacies_effects.add_cf_one(0x2F4)
    spacies_effects.add_cf_one(0x324)
    spacies_effects.add_cf_one(0x32B)
    spacies_effects.add_cf_two(0x382)
    spacies_effects.add_cf_two(0x392)
    spacies_effects.add_cf_two(0x3A2)
    spacies_effects.add_cf_two(0x3B2)
    spacies_effects.add_cf_two(0x3C4)
    spacies_effects.add_cf_two(0x43A)
    spacies_effects.add_cf_two(0x44A)
    spacies_effects.add_cf_two(0x4A9)
    spacies_effects.add_cf_two(0x5AF)
    spacies_effects.add_cf_two(0x5BC)
    spacies_effects.add_cf_one(0x52E)
    spacies_effects.add_cf_one(0x536)
    spacies_effects.add_zero_seven(0x1A508)
    spacies_effects.add_zero_seven(0x1B454)
    spacies_effects.add_zero_seven(0x1B520)
    spacies_effects.add_zero_seven(0x1B5EC)
    spacies_effects.add_zero_seven(0x1D2F8)
    spacies_effects.add_matrix(0x1C2A0, 0x2)
    spacies_effects.add_matrix(0x1C2A0, 0x2,"Shine")
    spacies_effects.add_matrix(0x1C8E0, 0x2,"Shine")
    spacies_effects.add_matrix(0x1C91F, 0x2,"Shine")
    spacies_effects.add_matrix(0x1C95E, 0x2,"Shine")
    spacies_effects.randomize_all()

    # Peach
    global_method_select = rng(0, global_num_methods)
    global_adjust = [rng(-128,128), rng(-128,128), rng(-128,128)]
    peach = FileColorData(b'PlPe.dat')
    peach.add_four_two_four_eight(0x160E8)
    peach.add_four_two_four_eight(0x16188)
    peach.add_four_two_four_eight(0x16228)
    peach.add_four_two_four_eight(0x162C8)
    peach.add_four_two_four_eight(0x16368)
    peach.add_four_two_four_eight(0x16408)
    peach.add_four_two_four_eight(0x1653C)
    peach.add_four_two_four_eight(0x165DC)
    peach.add_four_two_four_eight(0x1D8D8)
    peach.add_four_two_four_eight(0x1D978)
    peach.add_four_two_four_eight(0x1DA18)
    peach.add_four_two_four_eight(0x1D8D8)
    peach.add_four_two_four_eight(0x1DAB8)
    peach.add_four_two_four_eight(0x1DB58)
    peach.add_four_two_four_eight(0x1FE38)
    peach.add_four_two_four_eight(0x1FED8)
    peach.add_four_two_four_eight(0x1FF98)
    peach.add_four_two_four_eight(0x20038)
    peach.add_four_two_four_eight(0x200D8)
    peach.add_four_two_four_eight(0x20178)
    peach.add_four_two_four_eight(0x20218)
    peach.add_four_two_four_eight(0x202B8)
    peach.add_four_two_four_eight(0x2B1AC)
    peach.randomize_all()

    # Pikachu
    global_method_select = rng(0, global_num_methods)
    global_adjust = [rng(-128,128), rng(-128,128), rng(-128,128)]
    pikachu = FileColorData(b'PlPk.dat')
    pikachu.add_zero_seven(0xC354)
    pikachu.add_zero_seven(0x14DFC)
    pikachu.add_zero_seven(0x14EC8)
    pikachu.add_zero_seven(0x14F94)
    pikachu.add_zero_seven(0x15060)
    pikachu.add_zero_seven(0x1512C)
    pikachu.add_zero_seven(0x151EC)
    pikachu.randomize_all()

    # Pichu
    global_method_select = rng(0, global_num_methods)
    global_adjust = [rng(-128,128), rng(-128,128), rng(-128,128)]
    pichu = FileColorData(b'PlPc.dat')
    pichu.add_zero_seven(0xBF14)
    pichu.add_zero_seven(0x149BC)
    pichu.add_zero_seven(0x14A88)
    pichu.add_zero_seven(0x14B54)
    pichu.add_zero_seven(0x14C20)
    pichu.add_zero_seven(0x14CEC)
    pichu.add_zero_seven(0x14DAC)
    pichu.randomize_all()

    # Pikachu/Pichu Effects
    global_method_select = rng(0, global_num_methods)
    global_adjust = [rng(-128,128), rng(-128,128), rng(-128,128)]
    pi_effects = FileColorData(b'EfPkData.dat')
    pi_effects.add_zero_seven(0x13EA4)
    pi_effects.add_zero_seven(0x148DC)
    pi_effects.add_zero_seven(0x14A48)
    pi_effects.add_zero_seven(0x14BB4)
    pi_effects.add_zero_seven(0x14C80)
    pi_effects.add_zero_seven(0x14D4C)
    pi_effects.add_zero_seven(0x14E0C)
    pi_effects.add_four_two_four_eight(0x13F14)
    pi_effects.add_cf_two(0x166)
    pi_effects.add_cf_two(0x1CE)
    pi_effects.add_cf_two(0x236)
    pi_effects.add_cf_two(0x29E)
    pi_effects.add_cf_two(0x35C)
    pi_effects.add_cf_two(0x369)
    pi_effects.add_cf_two(0x3D6)
    pi_effects.add_cf_two(0x3E3)
    pi_effects.add_cf_two(0x43E)
    pi_effects.add_cf_two(0x44B)
    pi_effects.add_cf_two(0x4A5)
    pi_effects.add_cf_two(0x4B2)
    pi_effects.randomize_all()

    #Yoshi's Story
    global_method_select = 0
    global_adjust = [rng(-50,50), rng(-50,50), rng(-50,50)]
    yoshis_story = FileColorData(b'GrSt.dat')
    global_invert = False
    if percent_chance(10):
        global_invert = True
    global_swap_select = rng(0,3)
    randomize_texture_color(yoshis_story, 0x2A820, 0x2AC0, "RGB5A3")
    randomize_texture_color(yoshis_story, 0x2D460, 0x2D20, "RGB5A3")
    randomize_texture_color(yoshis_story, 0x30180, 0x2AC0, "RGB5A3")
    randomize_texture_color(yoshis_story, 0x33940, 0x2000, "CMPR")
    randomize_texture_color(yoshis_story, 0x338A0, 0x80, "RGB565")
    randomize_texture_color(yoshis_story, 0x35940, 0x8000, "CMPR")
    randomize_texture_color(yoshis_story, 0x3D940, 0x400, "CMPR")
    randomize_texture_color(yoshis_story, 0x3DD40, 0xD480, "CMPR")
    randomize_texture_color(yoshis_story, 0x4B1C0, 0x8000, "CMPR")
    randomize_texture_color(yoshis_story, 0x531C0, 0xB400, "CMPR")
    randomize_texture_color(yoshis_story, 0x5E5C0, 0x800, "CMPR")
    randomize_texture_color(yoshis_story, 0x5EDC0, 0x800, "CMPR")
    randomize_texture_color(yoshis_story, 0x5F5C0, 0x800, "CMPR")
    randomize_texture_color(yoshis_story, 0x5FDC0, 0x2000, "CMPR")
    randomize_texture_color(yoshis_story, 0x61DC0, 0x800, "CMPR")
    randomize_texture_color(yoshis_story, 0x629C0, 0x200, "RGB5A3")
    randomize_texture_color(yoshis_story, 0x62FE0, 0x200, "RGB5A3")
    randomize_texture_color(yoshis_story, 0x63200, 0x2000, "CMPR")
    randomize_texture_color(yoshis_story, 0x65A00, 0x200, "RGB565")
    randomize_texture_color(yoshis_story, 0x65C20, 0x8000, "CMPR")
    randomize_texture_color(yoshis_story, 0x6DC20, 0x2000, "CMPR")
    randomize_texture_color(yoshis_story, 0x6FC20, 0x2000, "CMPR")
    randomize_texture_color(yoshis_story, 0x81C20, 0x8000, "CMPR")
    randomize_texture_color(yoshis_story, 0x8C720, 0x800, "CMPR")
    randomize_texture_color(yoshis_story, 0x8CF20, 0x2000, "CMPR")
    randomize_texture_color(yoshis_story, 0x8EF20, 0x800, "CMPR")
    randomize_texture_color(yoshis_story, 0x8CF20, 0x2000, "CMPR")
    randomize_texture_color(yoshis_story, 0x8F720, 0x200, "CMPR")
    randomize_texture_color(yoshis_story, 0x8FA20, 0x2000, "CMPR")
    randomize_texture_color(yoshis_story, 0x91A20, 0x800, "CMPR")
    randomize_texture_color(yoshis_story, 0x92220, 0x200, "CMPR")
    randomize_texture_color(yoshis_story, 0x92520, 0x2000, "CMPR")
    randomize_texture_color(yoshis_story, 0x94520, 0x2000, "CMPR")
    randomize_texture_color(yoshis_story, 0x96520, 0x2000, "CMPR")
    randomize_texture_color(yoshis_story, 0x98520, 0x2000, "CMPR")
    randomize_texture_color(yoshis_story, 0x9A520, 0x2000, "CMPR")
    randomize_texture_color(yoshis_story, 0x9C520, 0x800, "CMPR")
    randomize_texture_color(yoshis_story, 0x9CD20, 0x10000, "CMPR")
    randomize_texture_color(yoshis_story, 0xACD20, 0x2000, "CMPR")
    randomize_texture_color(yoshis_story, 0xB9820, 0x2000, "CMPR")
    randomize_texture_color(yoshis_story, 0xBB820, 0x2000, "CMPR")
    randomize_texture_color(yoshis_story, 0xBE820, 0x20, "RGB5A3")
    randomize_texture_color(yoshis_story, 0xBE880, 0x1800, "CMPR")
    randomize_texture_color(yoshis_story, 0xC0080, 0x480, "CMPR")
    randomize_texture_color(yoshis_story, 0xC0500, 0x800, "CMPR")
    randomize_texture_color(yoshis_story, 0xC0D00, 0x800, "CMPR")
    randomize_texture_color(yoshis_story, 0xC1500, 0x800, "CMPR")
    randomize_texture_color(yoshis_story, 0xC1D00, 0x800, "CMPR")
    randomize_texture_color(yoshis_story, 0xC2500, 0x4000, "CMPR")
    randomize_texture_color(yoshis_story, 0xAED20, 0x8000, "CMPR")
    randomize_texture_color(yoshis_story, 0xB6D20, 0x2000, "CMPR")
    randomize_texture_color(yoshis_story, 0xB8D20, 0x800, "CMPR")
    randomize_texture_color(yoshis_story, 0xB9520, 0x200, "CMPR")
    randomize_texture_color(yoshis_story, 0xB9720, 0x80, "CMPR")
    randomize_texture_color(yoshis_story, 0xB97A0, 0x20, "CMPR")
    randomize_texture_color(yoshis_story, 0x89C20, 0x2000, "CMPR")
    randomize_texture_color(yoshis_story, 0x8BC20, 0x800, "CMPR")
    randomize_texture_color(yoshis_story, 0x8C420, 0x200, "CMPR")
    randomize_texture_color(yoshis_story, 0x8C620, 0x80, "CMPR")
    randomize_texture_color(yoshis_story, 0x8C6A0, 0x20, "CMPR")
    randomize_texture_color(stage_select, 0x171C0, 0x200, "RGB565")

    # Pokemon Stadium
    global_adjust = [rng(-50,50), rng(-50,50), rng(-50,50)]
    pokemon_stadium = FileColorData(b'GrPs.usd')
    global_swap_select = rng(0,3)
    global_invert = False
    if percent_chance(10):
        global_invert = True
    randomize_texture_color(pokemon_stadium, 0x3E3A0, 0x800, "CMPR")
    randomize_texture_color(pokemon_stadium, 0x3EBA0, 0x8000, "CMPR")
    randomize_texture_color(pokemon_stadium, 0x57C20, 0x200, "RGB565")
    randomize_texture_color(pokemon_stadium, 0x77EA0, 0x200, "RGB565")
    randomize_texture_color(pokemon_stadium, 0x982E0, 0x200, "RGB565")
    randomize_texture_color(pokemon_stadium, 0xA8500, 0x200, "RGB565")
    randomize_texture_color(pokemon_stadium, 0xC0720, 0x200, "RGB565")
    randomize_texture_color(pokemon_stadium, 0xC5700, 0x140, "RGB5A3")
    randomize_texture_color(pokemon_stadium, 0xCBCA0, 0x200, "RGB565")
    randomize_texture_color(pokemon_stadium, 0xCFEC0, 0x200, "RGB565")
    randomize_texture_color(pokemon_stadium, 0xDB4E0, 0x200, "RGB565")
    randomize_texture_color(pokemon_stadium, 0xE4F00, 0x200, "RGB565")
    randomize_texture_color(pokemon_stadium, 0xE9120, 0x200, "RGB565")
    randomize_texture_color(pokemon_stadium, 0xFB340, 0x200, "RGB565")
    randomize_texture_color(pokemon_stadium, 0x101560, 0x20, "RGB565")
    randomize_texture_color(pokemon_stadium, 0x1055A0, 0x20, "RGB565")
    randomize_texture_color(pokemon_stadium, 0x10B120, 0x2000, "CMPR")
    randomize_texture_color(pokemon_stadium, 0x13AF60, 0x800, "CMPR")
    randomize_texture_color(pokemon_stadium, 0x12D7E0, 0x1000, "CMPR")
    randomize_texture_color(pokemon_stadium, 0x12E7E0, 0x3600, "CMPR")
    randomize_texture_color(stage_select, 0x1D280, 0x200, "RGB565")
    pokemon_stadium.randomize_all()
    
    # Dreamland N64
    global_adjust = [rng(-50,50), rng(-50,50), rng(-50,50)]
    dreamland = FileColorData(b'GrOp.dat')
    global_swap_select = rng(0,3)
    global_invert = False
    if percent_chance(10):
        global_invert = True
    randomize_texture_color(dreamland, 0x12CE0, 0x1E, "RGB5A3")
    randomize_texture_color(dreamland, 0x12D00, 0x11, "RGB5A3")
    randomize_texture_color(dreamland, 0x12D20, 0x12, "RGB5A3")
    randomize_texture_color(dreamland, 0x12D40, 0x15, "RGB5A3")
    randomize_texture_color(dreamland, 0x13EC0, 0x12, "RGB5A3")
    randomize_texture_color(dreamland, 0x14700, 0x1F, "RGB565")
    randomize_texture_color(dreamland, 0x14F40, 0x20, "RGB5A3")
    randomize_texture_color(dreamland, 0x15180, 0x20, "RGB5A3")
    randomize_texture_color(dreamland, 0x155C0, 0x20, "RGB5A3")
    randomize_texture_color(dreamland, 0x15800, 0x1D, "RGB565")
    randomize_texture_color(dreamland, 0x15840, 0x2000, "RGB5A3")
    randomize_texture_color(dreamland, 0x17840, 0x100, "RGB5A3")
    randomize_texture_color(dreamland, 0x17940, 0x100, "RGB5A3")
    randomize_texture_color(dreamland, 0x17A40, 0x100, "RGB5A3")
    randomize_texture_color(dreamland, 0x17BC0, 0x1E, "RGB565")
    randomize_texture_color(dreamland, 0x17C80, 0xE, "RGB565")
    randomize_texture_color(dreamland, 0x17CC0, 0x400, "RGB5A3")
    randomize_texture_color(dreamland, 0x180C0, 0x400, "RGB5A3")
    randomize_texture_color(dreamland, 0x184C0, 0x200, "RGB5A3")
    randomize_texture_color(dreamland, 0x186C0, 0x800, "RGB5A3")
    randomize_texture_color(dreamland, 0x18EC0, 0x1000, "RGB5A3")
    randomize_texture_color(dreamland, 0x19EC0, 0x400, "RGB5A3")
    randomize_texture_color(dreamland, 0x1A2C0, 0x400, "RGB5A3")
    randomize_texture_color(dreamland, 0x1A6C0, 0x400, "RGB5A3")
    randomize_texture_color(dreamland, 0x1AAC0, 0x80000, "RGBA8") # Might need new format
    randomize_texture_color(dreamland, 0x9AAC0, 0x600, "RGB5A3")
    randomize_texture_color(dreamland, 0x9B0C0, 0x600, "RGB5A3")
    randomize_texture_color(dreamland, 0x9B6C0, 0x600, "RGB5A3")
    randomize_texture_color(dreamland, 0x9BFE0, 0x20, "RGB5A3")
    randomize_texture_color(dreamland, 0x9C220, 0x20, "RGB565")
    randomize_texture_color(dreamland, 0x9C360, 0x20, "RGB565")
    randomize_texture_color(dreamland, 0x9C5A0, 0x1E, "RGB5A3")
    randomize_texture_color(dreamland, 0x9C5E0, 0x200, "CMPR")
    randomize_texture_color(dreamland, 0x9C7E0, 0x200, "CMPR")
    randomize_texture_color(dreamland, 0x9C9E0, 0x200, "CMPR")
    randomize_texture_color(dreamland, 0x9CBE0, 0x200, "CMPR")
    randomize_texture_color(dreamland, 0x9CE60, 0x1F, "RGB565")
    randomize_texture_color(dreamland, 0x9CF20, 0x1F, "RGB565")
    randomize_texture_color(stage_select, 0x28F00, 0x200, "RGB565")

    # Fountain of Dreams
    global_adjust = [rng(-50,50), rng(-50,50), rng(-50,50)]
    izumi = FileColorData(b'GrIz.dat')
    global_swap_select = rng(0,3)
    global_invert = False
    if percent_chance(10):
        global_invert = True
    randomize_texture_color(izumi, 0x20, 0x100, "CMPR")
    randomize_texture_color(izumi, 0x120, 0x100, "CMPR")
    randomize_texture_color(izumi, 0x220, 0x200, "CMPR")
    randomize_texture_color(izumi, 0x420, 0x2000, "CMPR")
    randomize_texture_color(izumi, 0x2420, 0x2000, "CMPR")
    randomize_texture_color(izumi, 0x4420, 0x2000, "CMPR")
    randomize_texture_color(izumi, 0x6420, 0x1000, "CMPR")
    randomize_texture_color(izumi, 0x7420, 0x4000, "CMPR")
    randomize_texture_color(izumi, 0xB420, 0x8000, "CMPR")
    randomize_texture_color(izumi, 0x13420, 0x2000, "CMPR")
    randomize_texture_color(izumi, 0x15420, 0x800, "CMPR")
    randomize_texture_color(izumi, 0x15C20, 0x800, "CMPR")
    randomize_texture_color(izumi, 0x16420, 0x4000, "CMPR")
    randomize_texture_color(izumi, 0x1A420, 0x8000, "CMPR")
    randomize_texture_color(izumi, 0x22440, 0x800, "CMPR")
    randomize_texture_color(izumi, 0x22C40, 0x200, "CMPR")
    randomize_texture_color(izumi, 0x22E40, 0x400, "CMPR")
    randomize_texture_color(izumi, 0x23240, 0x2000, "CMPR")
    randomize_texture_color(izumi, 0x25240, 0x400, "CMPR")
    randomize_texture_color(izumi, 0x25640, 0x400, "CMPR")
    randomize_texture_color(izumi, 0x25A40, 0x800, "CMPR")
    randomize_texture_color(izumi, 0x26240, 0x800, "CMPR")
    randomize_texture_color(izumi, 0x26A40, 0x800, "CMPR")
    randomize_texture_color(izumi, 0x27240, 0x800, "CMPR")
    randomize_texture_color(izumi, 0x27A40, 0x2000, "CMPR")
    randomize_texture_color(izumi, 0x29A40, 0x80, "CMPR")
    randomize_texture_color(izumi, 0x29AC0, 0x80, "CMPR")
    randomize_texture_color(izumi, 0x29B40, 0x800, "CMPR")
    randomize_texture_color(izumi, 0x3A340, 0x200, "RGB5A3")
    randomize_texture_color(izumi, 0x3A560, 0x800, "CMPR")
    randomize_texture_color(izumi, 0x3AD60, 0x800, "CMPR")
    randomize_texture_color(izumi, 0x3B560, 0x800, "CMPR")
    randomize_texture_color(izumi, 0x3BD60, 0x1000, "CMPR")
    randomize_texture_color(izumi, 0x3CD60, 0x800, "CMPR")
    randomize_texture_color(izumi, 0x41560, 0x200, "RGB5A3")
    randomize_texture_color(izumi, 0x41780, 0x800, "CMPR")
    randomize_texture_color(izumi, 0x41F80, 0x800, "CMPR")
    randomize_texture_color(izumi, 0x46780, 0x10000, "RGBA8")
    randomize_texture_color(izumi, 0x56780, 0x10000, "RGBA8")
    randomize_texture_color(izumi, 0x6C780, 0x200, "RGB5A3")
    randomize_texture_color(izumi, 0x6C9A0, 0x2000, "CMPR")
    randomize_texture_color(izumi, 0x749A0, 0x200, "RGB5A3")
    randomize_texture_color(izumi, 0x7ABC0, 0x200, "RGB5A3")
    randomize_texture_color(izumi, 0x7F5E0, 0x200, "RGB5A3")
    randomize_texture_color(izumi, 0x83800, 0x200, "RGB5A3")
    randomize_texture_color(izumi, 0x8BA20, 0x200, "RGB5A3")
    randomize_texture_color(izumi, 0x93C40, 0x200, "RGB5A3")
    randomize_texture_color(izumi, 0x97E60, 0xFC, "RGB5A3")
    randomize_texture_color(izumi, 0x9BF80, 0x200, "RGB5A3")
    randomize_texture_color(izumi, 0x9C1A0, 0x1000, "RGB5A3")
    randomize_texture_color(izumi, 0x9D1A0, 0x4000, "CMPR")
    randomize_texture_color(stage_select, 0x19200, 0x200, "RGB565")

    # Battlefield
    global_adjust = [rng(-50,50), rng(-50,50), rng(-50,50)]
    battlefield = FileColorData(b'GrNBa.dat')
    global_swap_select = rng(0,3)
    global_invert = False
    if percent_chance(10):
        global_invert = True
    randomize_texture_color(battlefield, 0x34840, 0x400, "CMPR")
    randomize_texture_color(battlefield, 0x34C40, 0x200, "CMPR")
    randomize_texture_color(battlefield, 0x34EC0, 0x40, "CMPR")
    randomize_texture_color(battlefield, 0x35700, 0x1000, "CMPR")
    randomize_texture_color(battlefield, 0x36F00, 0x200, "RGB565")
    randomize_texture_color(battlefield, 0x37120, 0x20, "CMPR")
    randomize_texture_color(battlefield, 0x37140, 0x400, "CMPR")
    randomize_texture_color(battlefield, 0x37540, 0x40, "CMPR")
    randomize_texture_color(battlefield, 0x37D80, 0x200, "RGB565")
    randomize_texture_color(battlefield, 0x37FA0, 0x2000, "CMPR")
    randomize_texture_color(battlefield, 0x39FC0, 0x200, "CMPR")
    randomize_texture_color(battlefield, 0x3A1C0, 0x20, "CMPR")
    randomize_texture_color(battlefield, 0x3A1E0, 0x40, "CMPR")
    randomize_texture_color(battlefield, 0x3E220, 0x8000, "RGB5A3")
    randomize_texture_color(battlefield, 0x46220, 0x2000, "RGB565")
    randomize_texture_color(battlefield, 0x48220, 0x2000, "RGB565")
    randomize_texture_color(battlefield, 0x4A220, 0x800, "RGB565")
    randomize_texture_color(battlefield, 0x4CA20, 0x20000, "RGB565")
    randomize_texture_color(stage_select, 0x273C0, 0x200, "RGB565")

    # Final Destination
    global_adjust = [rng(-50,50), rng(-50,50), rng(-50,50)]
    final = FileColorData(b'GrNLa.dat')
    global_swap_select = rng(0,3)
    global_invert = False
    if percent_chance(10):
        global_invert = True
    randomize_texture_color(final, 0x52420, 0x2000, "CMPR")
    randomize_texture_color(final, 0x54920, 0x2000, "CMPR")
    randomize_texture_color(final, 0x5B920, 0x8000, "CMPR")
    randomize_texture_color(final, 0x78120, 0x10000, "RGBA8")
    randomize_texture_color(stage_select, 0x283E0, 0x200, "RGB565")
    final.add_zero_seven(0xFDD8)
    final.add_zero_seven(0xFE98)
    final.add_zero_seven(0x10358)
    final.add_zero_seven(0x10418)
    final.add_zero_seven(0x13D4C)
    final.add_zero_seven(0x13E18)
    final.add_zero_seven(0x13EE4)
    final.add_zero_seven(0x1CA98)
    final.add_zero_seven(0x1CB58)
    final.add_zero_seven(0x21A48)
    final.add_zero_seven(0x21B08)
    final.add_zero_seven(0x26280)
    final.add_zero_seven(0x26340)
    final.add_zero_seven(0x26400)
    final.add_zero_seven(0x264C0)
    final.add_zero_seven(0x2FD88)
    final.add_zero_seven(0x2FE54)
    final.add_zero_seven(0x2FF20)
    final.add_zero_seven(0x2FFEC)
    final.add_zero_seven(0x300B8)
    final.add_zero_seven(0x30184)
    final.add_zero_seven(0x30250)
    final.add_zero_seven(0x3031C)
    final.add_zero_seven(0x303E8)
    final.add_zero_seven(0x304B4)
    final.add_zero_seven(0x30580)
    final.add_zero_seven(0x3064C)
    final.add_zero_seven(0x30718)
    final.add_zero_seven(0x307E4)
    final.add_zero_seven(0x308B0)
    final.add_zero_seven(0x3097C)
    final.add_zero_seven(0x30AF4)
    final.add_zero_seven(0x30BF8)
    final.add_zero_seven(0x30CC4)
    final.add_zero_seven(0x30DBC)
    final.add_zero_seven(0x45910)
    final.add_zero_seven(0x459D0)
    final.add_zero_seven(0x45A90)
    final.add_zero_seven(0x45B50)
    final.add_zero_seven(0x45C10)
    final.add_zero_seven(0x45CD0)
    final.add_zero_seven(0x45D90)
    final.add_zero_seven(0x45E50)
    final.add_zero_seven(0x45F10)
    final.add_zero_seven(0x45FD0)
    final.add_zero_seven(0x46090)
    final.add_zero_seven(0x46150)
    final.add_zero_seven(0x46210)
    final.add_zero_seven(0x462D0)
    final.add_zero_seven(0x46390)
    final.add_zero_seven(0x46450)
    final.add_zero_seven(0x46510)
    final.add_zero_seven(0x465D0)
    final.add_zero_seven(0x46690)
    final.add_four_two_four_eight(0x7820)
    final.add_four_two_four_eight(0x784C)
    final.add_four_two_four_eight(0x7878)
    final.add_four_two_four_eight(0x7944)
    final.add_four_two_four_eight(0x7970)
    final.add_four_two_four_eight(0x799C)
    final.add_four_two_four_eight(0x79C8)
    final.add_four_two_four_eight(0x79F4)
    final.add_four_two_four_eight(0x7A20)
    final.add_four_two_four_eight(0x7A4C)
    final.add_four_two_four_eight(0x7A78)
    final.add_four_two_four_eight(0x7AA4)
    final.add_four_two_four_eight(0x7AD0)
    final.add_four_two_four_eight(0x7AFC)
    final.add_four_two_four_eight(0x7B28)
    final.add_four_two_four_eight(0x7B54)
    final.add_four_two_four_eight(0x7B80)
    final.add_four_two_four_eight(0x7C20)
    final.add_four_two_four_eight(0x7CC0)
    final.add_four_two_four_eight(0x7CEC)
    final.add_four_two_four_eight(0x7DB8)
    final.add_four_two_four_eight(0x7DE4)
    final.add_four_two_four_eight(0x7EB0)
    final.add_four_two_four_eight(0xFE48)
    final.add_four_two_four_eight(0xFF08)
    final.add_four_two_four_eight(0x103C8)
    final.add_four_two_four_eight(0x10488)
    final.add_four_two_four_eight(0x13C5C)
    final.add_four_two_four_eight(0x13CFC)
    final.add_four_two_four_eight(0x13DBC)
    final.add_four_two_four_eight(0x13E88)
    final.add_four_two_four_eight(0x13F54)
    final.add_four_two_four_eight(0x13F80)
    final.add_four_two_four_eight(0x1C9A8)
    final.add_four_two_four_eight(0x1CA48)
    final.add_four_two_four_eight(0x1CB08)
    final.add_four_two_four_eight(0x1CBC8)
    #final.add_four_two_four_eight(0x21AB8)
    #final.add_four_two_four_eight(0x21B78)
    #final.add_four_two_four_eight(0x26230)
    #final.add_four_two_four_eight(0x262F0)
    #final.add_four_two_four_eight(0x263B0)
    #final.add_four_two_four_eight(0x26470)
    #final.add_four_two_four_eight(0x26530)
    #final.add_four_two_four_eight(0x2CE48)
    #final.add_four_two_four_eight(0x2CEB4)
    #final.add_four_two_four_eight(0x2FDF8)
    #final.add_four_two_four_eight(0x2FEC4)
    #final.add_four_two_four_eight(0x2FF90)
    final.add_four_two_four_eight(0x3005C)
    final.add_four_two_four_eight(0x30128)
    final.add_four_two_four_eight(0x301F4)
    final.add_four_two_four_eight(0x302C0)
    final.add_four_two_four_eight(0x3038C)
    final.add_four_two_four_eight(0x30458)
    final.add_four_two_four_eight(0x30524)
    final.add_four_two_four_eight(0x305F0)
    final.add_four_two_four_eight(0x306BC)
    final.add_four_two_four_eight(0x30788)
    final.add_four_two_four_eight(0x30854)
    final.add_four_two_four_eight(0x30920)
    final.add_four_two_four_eight(0x309EC)
    final.add_four_two_four_eight(0x30A98)
    final.add_four_two_four_eight(0x30B64)
    final.add_four_two_four_eight(0x30B9C)
    final.add_four_two_four_eight(0x30C68)
    final.add_four_two_four_eight(0x30D34)
    final.add_four_two_four_eight(0x30D6C)
    final.add_four_two_four_eight(0x30E2C)
    final.add_four_two_four_eight(0x4571C)
    final.add_four_two_four_eight(0x457E8)
    final.add_four_two_four_eight(0x458B4)
    final.add_four_two_four_eight(0x45980)
    final.add_four_two_four_eight(0x45A40)
    final.add_four_two_four_eight(0x45B00)
    final.add_four_two_four_eight(0x45BC0)
    final.add_four_two_four_eight(0x45C80)
    final.add_four_two_four_eight(0x45D40)
    final.add_four_two_four_eight(0x45E00)
    final.add_four_two_four_eight(0x45EC0)
    final.add_four_two_four_eight(0x45F80)
    final.add_four_two_four_eight(0x46040)
    final.add_four_two_four_eight(0x46100)
    final.add_four_two_four_eight(0x461C0)
    final.add_four_two_four_eight(0x46280)
    final.add_four_two_four_eight(0x46340)
    final.add_four_two_four_eight(0x46400)
    final.add_four_two_four_eight(0x464C0)
    final.add_four_two_four_eight(0x46580)
    final.add_four_two_four_eight(0x46640)
    final.add_four_two_four_eight(0x46700)
    final.add_four_two_four_eight(0x52150)
    final.add_four_two_four_eight(0x52390)
    final.randomize_all()
