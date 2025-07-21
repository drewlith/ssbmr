from utility import get_value, set_value, percent_chance
from random import randint as rng

all_hitboxes = []

ELEMENTS = ["Normal", "Fire", "Electric", "Slash", "Coin", "Ice", "Sleep", "Hibernate",
            "??????", "Grounded", "Cape", "Special", "Disable", "Dark", "Screw Attack",
            "Flower", "None"]

class Hitbox():
    def __init__(self, data, offset):
        self.data = data
        self.power_rating = 0
        self.offset = offset
        self.name = ""
        self.tags = ["hitbox"]
        self.original_values = []
        self.log_notes = []
        self.shuffled = False
        if self.element == 8 or self.element == 11:
            self.tags.append("Exclude")
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
    def setkb(self): #b14 and b15 xxWWWWWW WWWxxxxx
        return get_value(self.data, 37, 9)

    @setkb.setter
    def setkb(self, value):
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
    def shielddamage(self): #b17 and b18 xxxxxxxS SSSSSSxx
        return get_value(self.data, 10, 7)

    @shielddamage.setter
    def shielddamage(self, value):
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
        string += "\n Set KB: " + str(self.setkb)
        string += "\n Element: " + ELEMENTS[self.element]
        string += "\n Shield Damage: " + str(self.shielddamage)
        string += "\n SFX: " + str(self.sfx)
        string += "\n Size: " + str(self.size)
        string += "\n Z-Offset: " + str(self.zoffset)
        string += "\n Y-Offset: " + str(self.yoffset)
        string += "\n X-Offset: " + str(self.xoffset)
        string += "\n Bone: " + str(self.bone)
        tags = ""
        for tag in self.tags:
            tags += tag + ", " 
        string += "\n Tags: " + tags[:-2]
        string += "\n My Power rating is: " + str(self.power_rating)
        return string
    
    def check_tags(self, searching_for):
        for tag in self.tags:
            if tag.lower() in searching_for.lower():
                return True
        return False
    
    def add_tags(self, tags):
        for tag in tags:
            self.tags.append(tag)

def determine_power_ratings():
    for hitbox in all_hitboxes:
        power_rating = 0
        power_rating += hitbox.damage * 10
        power_rating += hitbox.growth
        power_rating += hitbox.base * 4
        power_rating += hitbox.size // 20
        power_rating += hitbox.shielddamage * 5
        power_rating += hitbox.setkb
        hitbox.power_rating = power_rating

def shuffle_hitboxes(hitbox, target):
    hitbox.damage, target.damage = target.damage, hitbox.damage
    hitbox.angle, target.angle = target.angle, hitbox.angle
    hitbox.growth, target.growth = target.growth, hitbox.growth
    hitbox.base, target.base = target.base, hitbox.base
    hitbox.setkb, target.setkb = target.setkb, hitbox.setkb
    hitbox.size, target.size = target.size, hitbox.size
    #hitbox.element, target.element = target.element, hitbox.element
    hitbox.shielddamage, target.shielddamage = target.shielddamage, hitbox.shielddamage
    hitbox.sfx, target.sfx = target.sfx, hitbox.sfx

def exclude_hitboxes(tag):
    for hitbox in all_hitboxes:
        if hitbox.check_tags(tag):
            hitbox.tags.append("exclude")

def unbalanced_shuffle_all(chance):
    pool = []
    for hitbox in all_hitboxes:
        if not hitbox.check_tags("exclude"):
            pool.append(hitbox)

    for hitbox in pool:
        if percent_chance(chance):
            target = pool[rng(0, len(pool) - 1)]
            shuffle_hitboxes(hitbox, target)

def balanced_shuffle_all(chance):
    number_of_tiers = 10
    tiers = []
    setkb_tiers = []
    for i in range(number_of_tiers):
        tiers.append([])
        setkb_tiers.append([])

    def add_to_tier(hitbox, tier_number):
        if hitbox.setkb > 0:
            setkb_tiers[tier_number].append(hitbox)
            return
        tiers[tier_number].append(hitbox)
        return

    for hitbox in all_hitboxes:
        if not hitbox.check_tags("exclude"):
            if hitbox.power_rating > 1000:
                add_to_tier(hitbox, 9)
            elif hitbox.power_rating > 800:
                add_to_tier(hitbox, 8)
            elif hitbox.power_rating > 700:
                add_to_tier(hitbox, 7)
            elif hitbox.power_rating > 600:
                add_to_tier(hitbox, 6)
            elif hitbox.power_rating > 500:
                add_to_tier(hitbox, 5)
            elif hitbox.power_rating > 400:
                add_to_tier(hitbox, 4)
            elif hitbox.power_rating > 300:
                add_to_tier(hitbox, 3)
            elif hitbox.power_rating > 200:
                add_to_tier(hitbox, 2)
            elif hitbox.power_rating > 100:
                add_to_tier(hitbox, 1)
            else:
                add_to_tier(hitbox, 0)
    
    for tier in tiers:
        for hitbox in tier:
            if percent_chance(chance):
                target = tier[rng(0, len(tier) - 1)]
                shuffle_hitboxes(hitbox, target)
    for tier in setkb_tiers:
        for hitbox in tier:
            if percent_chance(chance):
                target = tier[rng(0, len(tier) - 1)]
                shuffle_hitboxes(hitbox, target)
