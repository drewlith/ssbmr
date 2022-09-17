import melee
from util import set_value, get_value

# For assembly stuff, if needed. By drewlith.
# https://www.ibm.com/docs/en/aix/7.1?topic=set-b-branch-instruction

def B(address): # Branch
    instruction = bytearray(4)
    instruction = set_value(instruction, 26, 6, 18)
    instruction = set_value(instruction, 2, 24, address)
    return instruction

def BA(address): # Branch absolute address
    instruction = bytearray(4)
    instruction = set_value(instruction, 26, 6, 18)
    instruction = set_value(instruction, 2, 24, address)
    instruction = set_value(instruction, 1, 1, 1)
    return instruction

def BL(address): # Branch Linked
    instruction = bytearray(4)
    instruction = set_value(instruction, 26, 6, 18)
    instruction = set_value(instruction, 2, 24, address)
    instruction = set_value(instruction, 0, 1, 1)
    return instruction

def BLR(): # Branch Linked Return?
    instruction = bytearray(4)
    instruction = set_value(instruction, 0, 32, 0x4E800020)
    return instruction

