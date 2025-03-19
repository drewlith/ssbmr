from utility import get_value, set_value
from random import randint as rng

all_hitboxes = []
class Hitbox():
    def __init__(self, data, offset):
        self.data = data
        self.offset = offset
        self.tags = []
        self.original_values = []
        self.log_notes = []
        all_hitboxes.append(self)
        
    @property
    def damage(self): #b2 and b3 xxxxxxxD DDDDDDDD
        return get_value(self.data, 128, 9)
    
    @damage.setter
    def damage(self, value): 
        self.data = set_value(self.data, 128, 9, value)

    @property
    def angle(self): #b12 and b13 AAAAAAAA Axxxxxxx
        return get_value(self.data, 55, 9)

    @angle.setter
    def angle(self, value):
        self.data = set_value(self.data, 55, 9, value)

    @property
    def growth(self): #b13 and b14 xGGGGGGG GGxxxxxx
        return get_value(self.data, 46, 9)

    @growth.setter
    def growth(self, value):
        self.data = set_value(self.data, 46, 9, value)

    @property
    def set_kb(self): #b14 and b15 xxWWWWWW WWWxxxxx
        return get_value(self.data, 37, 9)

    @set_kb.setter
    def set_kb(self, value):
        self.data = set_value(self.data, 37, 9, value)

    @property
    def base(self): #b16 and b17 BBBBBBBB Bxxxxxxx
        return get_value(self.data, 23, 9)

    @base.setter
    def base(self, value):
        self.data = set_value(self.data, 23, 9, value)

    @property
    def element(self): #b17 xEEEEExx
        return get_value(self.data, 18, 5)

    @element.setter
    def element(self, value):
        self.data = set_value(self.data, 18, 5, value)

    @property
    def shield_damage(self): #b17 and b18 xxxxxxxS SSSSSSxx
        return get_value(self.data, 10, 7)

    @shield_damage.setter
    def shield_damage(self, value):
        self.data = set_value(self.data, 10, 7, value)

    @property
    def sfx(self): #b18 and b19 xxxxxxFF FFFFFFxx
        return get_value(self.data, 2, 8)

    @sfx.setter
    def sfx(self, value):
        self.data = set_value(self.data, 2, 8, value)

    @property
    def size(self): #b4 and b5 SSSSSSSS SSSSSSSS
        return get_value(self.data, 112, 16)

    @size.setter
    def size(self, value):
        self.data = set_value(self.data, 112, 16, value)

    @property
    def zoffset(self): #b6 and b7 ZZZZZZZZ ZZZZZZZZ
        return get_value(self.data, 96, 16)

    @zoffset.setter
    def zoffset(self, value):
        self.data = set_value(self.data, 96, 16, value)

    @property
    def yoffset(self): #b8 and b9 YYYYYYYY YYYYYYYY
        return get_value(self.data, 80, 16)

    @yoffset.setter
    def yoffset(self, value):
        self.data = set_value(self.data, 80, 16, value)

    @property
    def xoffset(self): #b10 and b11 XXXXXXXX XXXXXXXX
        return get_value(self.data, 64, 16)

    @xoffset.setter
    def xoffset(self, value):
        self.data = set_value(self.data, 64, 16, value)

    @property
    def bone(self): #b1 and b2 xxxxxxBB BBBBBxxx
        return get_value(self.data, 139, 7)

    @bone.setter
    def bone(self, value):
        self.data = set_value(self.data, 139, 7, value)

    def __str__(self):
        string = "Hitbox Event at offset " + str(self.offset) + " with command: " + hex(self.data[0])
        string += "\n Damage: " + str(self.damage)
        string += "\n Angle: " + str(self.angle)
        string += "\n Growth: " + str(self.growth)
        string += "\n Base: " + str(self.base)
        string += "\n Set KB: " + str(self.set_kb)
        string += "\n Element: " + str(self.element)
        string += "\n Shield Damage: " + str(self.shield_damage)
        string += "\n SFX: " + str(self.sfx)
        string += "\n Size: " + str(self.size)
        string += "\n Z-Offset: " + str(self.zoffset)
        string += "\n Y-Offset: " + str(self.yoffset)
        string += "\n X-Offset: " + str(self.xoffset)
        string += "\n Bone: " + str(self.bone)
        return string
    
def simple(flags):
    if "&shuffle 1" in flags: # Ignore consequences, shuffle everything
        for hb in all_hitboxes:
            target = rng(0, len(all_hitboxes) - 1)
            temp = hb.data
            target_hb = all_hitboxes[target]
            hb.data = target_hb.data
            target_hb.data = temp

