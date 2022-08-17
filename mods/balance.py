# Balance mod by drewlith. Sets whether attacks should be balanced or not.
# Percent: Percent chance a move becomes balanced.
import melee
from util import percent_chance
def start_mod(percent):
    for fighter in melee.fighters:
        for attack in fighter.attacks:
            if percent_chance(percent):
                attack.balance = True
