import dat, fst

fighters = []
bosses = []
items = None

class Fighter():
    def __init__(self, name, subactions, attributes):
        self.name = name
        self.subactions = subactions
        self.attributes = attributes
        self.unique_attributes = []
        self.attacks = []
        self.item_attacks = []
        self.throws = []

    def add_attack(self, hitboxes, name, strength, tags):
        self.attacks.append(Attack(hitboxes, name, strength, tags))

    def add_item_attack(self, hitboxes, name, strength, tags):
        self.item_attacks.append(Attack(hitboxes, name, strength, tags))
           
    def show_subaction_hitboxes(self, index): # Utility for manually adding attacks
        elements = ["Normal", "Fire", "Electric", "Slash", "Coin", "Ice", "Sleep", "Sleep",
            "?", "Grounded", "Cape", "Special", "Disable", "Dark", "Screw Attack",
            "Flower", "None"]
        if len(self.subactions[index].hitboxes) > 0:
            print(index, self.subactions[index].name)
            i = 0
            for hitbox in self.subactions[index].hitboxes:
                print("Hitbox", i)
                print("Damage:", hitbox.damage)
                print("Angle:", hitbox.angle)
                print("Growth:", hitbox.growth)
                print("Set KB:", hitbox.set_kb)
                print("Base KB:", hitbox.base)
                print("Element:", elements[hitbox.element])
                print("Shield Damage:", hitbox.shield_damage)
                print("SFX:", hitbox.sfx)
                print("Size:", hitbox.size)
                print("\n")
                i += 1

class Attack():
    def __init__(self, hitboxes, name, strength, tags):
        self.hitboxes = hitboxes
        self.name = name
        self.strength = strength
        self.tags = tags

def find_fighter(name):
    for fighter in fighters:
        if name in fighter.name:
            return fighter
    print("No fighter found with name:", name)

def add_fighter(pl_dat_file, name, boss=False):
    dat.file_data = pl_dat_file.file_data
    subactions = dat.get_subactions()
    attributes = dat.get_attribute_data()
    if boss:
        bosses.append(Fighter(name, subactions, attributes))
    else:
        fighters.append(Fighter(name, subactions, attributes))

def add_fighters(melee_files):
    add_fighter(fst.find_file(melee_files, b'PlKp.dat'), "Bowser")
    add_fighter(fst.find_file(melee_files, b'PlCa.dat'), "Captain Falcon")
    add_fighter(fst.find_file(melee_files, b'PlDk.dat'), "Donkey Kong")
    add_fighter(fst.find_file(melee_files, b'PlDr.dat'), "Dr. Mario")
    add_fighter(fst.find_file(melee_files, b'PlFc.dat'), "Falco")
    add_fighter(fst.find_file(melee_files, b'PlFx.dat'), "Fox")
    add_fighter(fst.find_file(melee_files, b'PlGw.dat'), "Mr. Game & Watch")
    add_fighter(fst.find_file(melee_files, b'PlGn.dat'), "Ganondorf")
    add_fighter(fst.find_file(melee_files, b'PlPp.dat'), "Popo")
    add_fighter(fst.find_file(melee_files, b'PlNn.dat'), "Nana")
    add_fighter(fst.find_file(melee_files, b'PlPr.dat'), "Jigglypuff")
    add_fighter(fst.find_file(melee_files, b'PlKb.dat'), "Kirby")
    add_fighter(fst.find_file(melee_files, b'PlLk.dat'), "Link")
    add_fighter(fst.find_file(melee_files, b'PlLg.dat'), "Luigi")
    add_fighter(fst.find_file(melee_files, b'PlMr.dat'), "Mario")
    add_fighter(fst.find_file(melee_files, b'PlMs.dat'), "Marth")
    add_fighter(fst.find_file(melee_files, b'PlMt.dat'), "Mewtwo")
    add_fighter(fst.find_file(melee_files, b'PlNs.dat'), "Ness")
    add_fighter(fst.find_file(melee_files, b'PlPe.dat'), "Peach")
    add_fighter(fst.find_file(melee_files, b'PlPc.dat'), "Pichu")
    add_fighter(fst.find_file(melee_files, b'PlPk.dat'), "Pikachu")
    add_fighter(fst.find_file(melee_files, b'PlFe.dat'), "Roy")
    add_fighter(fst.find_file(melee_files, b'PlSs.dat'), "Samus")
    add_fighter(fst.find_file(melee_files, b'PlSk.dat'), "Sheik")
    add_fighter(fst.find_file(melee_files, b'PlYs.dat'), "Yoshi")
    add_fighter(fst.find_file(melee_files, b'PlCl.dat'), "Young Link")
    add_fighter(fst.find_file(melee_files, b'PlZd.dat'), "Zelda")
    add_fighter(fst.find_file(melee_files, b'PlBo.dat'), "Boy", True)
    add_fighter(fst.find_file(melee_files, b'PlGl.dat'), "Girl", True)
    add_fighter(fst.find_file(melee_files, b'PlGk.dat'), "Giga Bowser", True)
    add_fighter(fst.find_file(melee_files, b'PlMh.dat'), "Master Hand", True)
    add_fighter(fst.find_file(melee_files, b'PlCh.dat'), "Crazy Hand", True)
            
def get_fighters():
    return fighters

def get_bosses():
    return bosses


