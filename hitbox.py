import util

class Hitbox():
    def __init__(self, name):
        self.name = name
        self.data = []
        self.offset = 0

    def get_damage(self): #b2 and b3 xxxxxxxD DDDDDDDD
        return util.get_value(self.data, 128, 9)

    def set_damage(self, value): 
        self.data = util.set_value(self.data, 128, 9, value)
    
    def get_angle(self): #b12 and b13 AAAAAAAA Axxxxxxx
        return util.get_value(self.data, 55, 9)
    
    def set_angle(self, value):
        self.data = util.set_value(self.data, 55, 9, value)

    def get_growth(self): #b13 and b14 xGGGGGGG GGxxxxxx
        return util.get_value(self.data, 46, 9)

    def set_growth(self, value):
        self.data = util.set_value(self.data, 46, 9, value)
        
    def get_set(self): #b14 and b15 xxWWWWWW WWWxxxxx
        return util.get_value(self.data, 37, 9)

    def set_set(self, value):
        self.data = util.set_value(self.data, 37, 9, value)

    def get_base(self): #b16 and b17 BBBBBBBB Bxxxxxxx
        return util.get_value(self.data, 23, 9)

    def set_base(self, value):
        self.data = util.set_value(self.data, 23, 9, value)
    
    def get_element(self): #b17 xEEEEExx
        return util.get_value(self.data, 18, 5)

    def set_element(self, value):
        self.data = util.set_value(self.data, 18, 5, value)

    def get_shield(self): #b17 and b18 xxxxxxxS SSSSSSxx
        return util.get_value(self.data, 10, 7)

    def set_shield(self, value):
        self.data = util.set_value(self.data, 10, 7, value)

    def get_sfx(self): #b18 and b19 xxxxxxFF FFFFFFxx
        return util.get_value(self.data, 2, 8)

    def set_sfx(self, value):
        self.data = util.set_value(self.data, 2, 8, value)

    def get_size(self): #b4 and b5 SSSSSSSS SSSSSSSS
        return util.get_value(self.data, 112, 16)

    def set_size(self, value):
        self.data = util.set_value(self.data, 112, 16, value)

