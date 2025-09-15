from utility import get_value, set_value
class Throw(): 
    def __init__(self, data, offset):
        self.data = data
        self.offset = offset
        self.name = ""
        self.tags = ["throw"]
        self.original_values = []
        self.log_notes = []

    def get_type(self):
        return get_value(self.data, 87, 3)

    @property
    def damage(self): #b2 and b3
        return get_value(self.data, 64, 9)

    @damage.setter
    def damage(self, value): 
        self.data = set_value(self.data, 64, 9, value)

    @property
    def angle(self): #b4 and b5 AAAAAAAA Axxxxxxx
        return get_value(self.data, 55, 9)

    @angle.setter
    def angle(self, value):
        self.data = set_value(self.data, 55, 9, value)

    @property
    def growth(self): #b5 and b6 xGGGGGGG GGxxxxxx
        return get_value(self.data, 46, 9)

    @growth.setter
    def growth(self, value):
        self.data = set_value(self.data, 46, 9, value)

    @property
    def setkb(self): #b6 and b7 xxWWWWWW WWWxxxxx
        return get_value(self.data, 37, 9)

    @setkb.setter
    def setkb(self, value):
        self.data = set_value(self.data, 37, 9, value)

    @property
    def base(self): #b8 and b9 BBBBBBBB Bxxxxxxx
        return get_value(self.data, 23, 9)

    @base.setter
    def base(self, value):
        self.data = set_value(self.data, 23, 9, value)

    @property
    def element(self): #b9 xEEEExxx
        return get_value(self.data, 19, 4)

    @element.setter
    def element(self, value):
        self.data = set_value(self.data, 19, 4, value)

    def check_tags(self, searching_for):
        for tag in self.tags:
            if tag.lower() in searching_for.lower():
                return True
        return False

    def __str__(self):
        string = "Throw Event at offset " + str(self.offset) + " with command: " + hex(self.data[0])
        string += "\n Damage: " + str(self.damage)
        string += "\n Angle: " + str(self.angle)
        string += "\n Growth: " + str(self.growth)
        string += "\n Base: " + str(self.base)
        string += "\n Set KB: " + str(self.setkb)
        string += "\n Element: " + str(self.element)
        return string