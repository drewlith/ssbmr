# Random/Shuffled Throws mod by drewlith.
# Shuffle Percent: Amount of attacks to shuffle (as opposed to randomize)
import melee, random
from util import percent_chance

throw_elements = ["Normal", "Fire", "Electric", "Ice", "Darkness"]

def randomize(throw):
    throw.set_damage(random.randint(4,11)) # Damage
    
    # Angle determination
    if percent_chance(20): # Sakurai Angle
        angle = 361
    elif percent_chance(80): # Send Forward
        angle = random.randint(2,6)*10
    elif percent_chance(80): # Send Straight Up
        angle = random.randint(8,9)*10
    else:
        angle = random.randint(0,360) # Randomize

    throw.set_growth(random.randint(5,14)*10)
    throw.set_base(random.randint(2,8)*10)
    throw.set_set(random.randint(2,10)*10)
    throw.set_element(random.randint(0,4))

def shuffle(throw):
    t = throw.get_damage()
    throw.set_damage(throw.shuffle_target.get_damage())
    throw.shuffle_target.set_damage(t)

    t = throw.get_angle()
    throw.set_angle(throw.shuffle_target.get_angle())
    throw.shuffle_target.set_angle(t)

    t = throw.get_growth()
    throw.set_growth(throw.shuffle_target.get_growth())
    throw.shuffle_target.set_growth(t)

    t = throw.get_set()
    throw.set_set(throw.shuffle_target.get_set())
    throw.shuffle_target.set_set(t)

    t = throw.get_base()
    throw.set_base(throw.shuffle_target.get_base())
    throw.shuffle_target.set_base(t)

    t = throw.get_element()
    throw.set_element(throw.shuffle_target.get_element())
    throw.shuffle_target.set_element(t)

    

def start_mod(shuffle_percent):
    for throw in melee.throws:
        if percent_chance(shuffle_percent):
            shuffle(throw)
            throw.notes.append("Shuffled with " + throw.shuffle_target.fighter.name
                               + " " + throw.shuffle_target.name + ".")
            throw.notes.append("Damage: " + str(throw.get_damage()))
            throw.notes.append("Angle: " + str(throw.get_angle()))
            throw.notes.append("Knockback Growth: " + str(throw.get_growth()))
            throw.notes.append("Base Knockback: " + str(throw.get_base()))
            throw.notes.append("WDSK: " + str(throw.get_set()))
            if throw.get_element() > 4:
                throw.notes.append("Element: Normal")
            else:
                throw.notes.append("Element: " + throw_elements[throw.get_element()])
        else:
            randomize(throw)
            throw.notes.append("Randomized.")
            throw.notes.append("Damage: " + str(throw.get_damage()))
            throw.notes.append("Angle: " + str(throw.get_angle()))
            throw.notes.append("Knockback Growth: " + str(throw.get_growth()))
            throw.notes.append("Base Knockback: " + str(throw.get_base()))
            throw.notes.append("WDSK: " + str(throw.get_set()))
            if throw.get_element() > 4:
                throw.notes.append("Element: Normal")
            else:
                throw.notes.append("Element: " + throw_elements[throw.get_element()])
        

        
