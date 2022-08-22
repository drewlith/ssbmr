import util

class Throw():
    def __init__(self, name, fighter):
        self.fighter = fighter
        self.name = name
        self.shuffled_with = self.fighter.name + " " + self.name
        self.data = []
        self.original_stats = []
        self.shuffled = False

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

    def record_original_stats(self):
        self.original_stats.clear()
        self.original_stats.append(str(self.get_damage()))
        self.original_stats.append(str(self.get_angle()))
        self.original_stats.append(str(self.get_growth()))
        self.original_stats.append(str(self.get_base()))
        self.original_stats.append(str(self.get_set()))
        self.original_stats.append(self.get_element())


