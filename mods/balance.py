# Balance mod by drewlith. Sets whether attacks should be balanced or not.
import melee
def start_mod():
    for attack in melee.attacks:
        attack.balance = True
        for hb in attack.hitboxes:
            if hb.get_set() > 90:
                hb.set_set(90)
            if hb.get_element() == 6 or hb.get_element() == 7:
                hb.set_element(0)
    for item in melee.items:
        item.balance = True
