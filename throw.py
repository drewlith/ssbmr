import util

class Throw():
    def __init__(self, name):
        self.name = name
        self.shuffled_with = self.name
        self.original_owner = ""
        self.data = []
        self.offset = 0
        self.damage = 0
        self.angle = 0
        self.growth = 0
        self.base = 0
        self.wdsk = 0
        self.element = 0
        self.random = False
        self.chaos = False
        self.balance = False

    def get_damage(self): #b2 and b3
        return util.get_value(self.data, 64, 9)

    def set_damage(self, value): 
        self.data = util.set_value(self.data, 64, 9, value)

    def get_angle(self): #b4 and b5 AAAAAAAA Axxxxxxx
        return util.get_value(self.data, 55, 9)

    def set_angle(self, value):
        self.data = util.set_value(self.data, 55, 9, value)

    def get_growth(self): #b5 and b6 xGGGGGGG GGxxxxxx
        return util.get_value(self.data, 46, 9)

    def set_growth(self, value):
        self.data = util.set_value(self.data, 46, 9, value)

    def get_set(self): #b6 and b7 xxWWWWWW WWWxxxxx
        return util.get_value(self.data, 37, 9)

    def set_set(self, value):
        self.data = util.set_value(self.data, 37, 9, value)

    def get_base(self): #b8 and b9 BBBBBBBB Bxxxxxxx
        return util.get_value(self.data, 23, 9)

    def set_base(self, value):
        self.data = util.set_value(self.data, 23, 9, value)

    def get_element(self): #b9 xEEEExxx
        return util.get_value(self.data, 19, 4)

    def set_element(self, value):
        self.data = util.set_value(self.data, 19, 4, value)

    def get_parameters(self):
        if len(self.data) == 0: return
        self.damage = self.get_damage()
        self.angle = self.get_angle()
        self.growth = self.get_growth()
        self.set = self.get_set()
        self.base = self.get_base()
        self.element = self.get_element()

    def set_parameters(self):
        if len(self.data) == 0: return
        self.set_damage(self.damage)
        self.set_angle(self.angle)
        self.set_growth(self.growth)
        self.set_set(self.set)
        self.set_base(self.base)
        self.set_element(self.element)

    def decode_throw(self):
        print("Damage: ", self.get_damage())
        print("Angle: ", self.get_angle())
        print("KBG: ", self.get_growth())
        print("Set KB: ", self.get_set())
        print("Base KB: ", self.get_base())
        print("Element: ", self.get_element())
