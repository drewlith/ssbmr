from utility import get_value, set_value, percent_chance
from random import randint as rng
import fighter

all_sfx = []

SFX_BLACKLIST = [0x0C3, 0x0C4, 0x0C5, 0x0C6, 0x0C7, 0x0C8, 0x0C9, 0x0CA, 0x0CB, 0x0CC, 0x0CD, 0x0CE, 0x0CF,
             0x0D0, 0x0D1, 0x0D2, 0x0D3, 0x0D4, 0x0D5, 0x0D6, 0x0D7, 0x0D8, 0x0D9, 0x0DA, 0x05F, 0x084,
             0x085, 0x12D]

ACTION_WHITELIST = ["Spot Dodge", "Air Dodge", "Forward Roll", "Back Roll", "Taunt", "Grab", "Dash Grab", "Star KO", "Jab 1", 
                    "Jab 2", "Jab 3", "Dash Attack", "Forward Tilt Highest", "Forward Tilt Mid-High", "Forward Tilt Middle", 
                    "Forward Tilt Mid-Low", "Forward Tilt Lowest", "Up Tilt", "Down Tilt", "Forward Smash Highest", "Forward Smash Mid-High", 
                    "Forward Smash Middle", "Forward Smash Mid-Low", "Forward Smash Lowest", "Up Smash", "Down Smash", "Neutral Aerial", 
                    "Forward Aerial", "Back Aerial", "Up Aerial", "Down Aerial", "Get-Up Attack Up", "Get-Up Attack Down", "Ledge Attack Slow", 
                    "Ledge Attack Fast", "Pummel", "Forward Throw", "Back Throw", "Up Throw", "Down Throw",
                    "Koopa Klaw", "Flame Breath", "Whirling Fortress", "Bowser Bomb",
                    "Falcon Dive Throw", "Falcon Dive", "Falcon Punch", "Raptor Boost", "Falcon Kick"
                    "Cargo Throw", "Giant Punch", "Headbutt", "Spinning Kong", "Hand Slap",
                    "Megavitamin", "Super Sheet", "Super Jump Punch", "Dr Tornado",
                    "Blaster", "Phantasm", "Fire Bird", "Reflector",
                    "Illusion", "Fire Fox",
                    "Sausage", "Fire!", "Oil Panic",
                    "Warlock Punch", "Gerudo Dragon", "Dark Dive", "Wizards Foot",
                    "Rollout", "Pound", "Sing", "Rest",
                    "Hammer", "Final Cutter", "Stone", "Copy Mario", "Copy Link", "Copy Samus", 
                    "Copy Yoshi", "Copy Fox", "Copy Pikachu", "Copy Luigi", "Copy Captain Falcon", 
                    "Copy Ness", "Copy Bowser", "Copy Peach" , "Copy DK", "Copy Zelda", "Copy Rollout",
                    "Forward Smash Second Hit", "Fairy Bow", "Boomerang", "Spin Attack", "Link Bombs", "Hookshot",
                    "Fireball", "Green Missile", "Cyclone",
                    "Super Cape", "Mario Tornado",
                    "Shield Breaker", "Dancing Blade", "Dolphin Slash", "Counter",
                    "Shadow Ball", "Confusion", "Teleport", "Disable",
                    "Ice Shot", "Squall Hammer", "Belay", "Blizzard",
                    "Up Smash YoYo", "PK Flash", "PK Fire", "PK Thunder", "PK Magnet",
                    "Tennis Racket", "Golf Club", "Frying Pan", "Toad", "Peach Bomber", "Parasol", "Vegetable",
                    "Thunder Jolt", "Skull Bash", "Agility", "Thunder!",
                    "Quick Attack",
                    "Flare Blade", "Double Edge Dance", "Blazer",
                    "Morph Ball Bomb", "Charge Shot", "Missile", "Screw Attack", "Grapple Beam",
                    "Needle", "Chain Dance", "Vanish", "Transform",
                    "Egg Lay", "Egg Roll", "Egg Throw", "Ground Pound",
                    "Hero Bow",
                    "Nayrus Love", "Dins Fire", "Farores Wind"
                    ]

class SFX():
    def __init__(self, data, offset):
        self.offset = offset
        self.data = data
        self.common_sfx = False
        if self.id <= 0xFFF:
            self.common_sfx = True
        all_sfx.append(self)

    @property
    def id(self): #44000000 000XXXXX 00007F40
        return get_value(self.data, 32, 20)

    @id.setter
    def id(self, value):
        self.data = set_value(self.data, 32, 20, value)

    def __str__(self):
        string = "SFX Event at offset " + str(self.offset) + " with command: " + hex(self.data[0]) + " | RAW HEX: " + self.data.hex()
        string += "\n The sound effect ID is: " + str(hex(self.id))
        return string
    
def randomize(chance):
    for _fighter in fighter.fighters:
        for subaction in _fighter.subactions:
            if subaction.friendly_name in ACTION_WHITELIST:
                for _sfx in subaction.sfx:
                    if percent_chance(chance):
                        if _sfx.common_sfx:
                            index = rng(0,0x20F)
                            while index in SFX_BLACKLIST:
                                index = rng(0,0x20F)
                            if percent_chance(10) and len(fighter.good_sfx > 0):
                                _sfx.id = _fighter.good_sfx[rng(0,len(_fighter.good_sfx)-1)]
                            _sfx.id = index
                        elif len(fighter.good_sfx > 0): # Fighter Specific
                            _sfx.id = _fighter.good_sfx[rng(0,len(_fighter.good_sfx)-1)]