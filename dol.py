# Performs various actions on the dol like reading gecko codes and injecting ASM
# Created by drewlith. Special Thanks: ribbanya, DRGN, Vetri

import melee
from util import set_value, get_value, get_word_string
from asm import *

free_space = [( 0x2C8, 0x398 ), ( 0x39C, 0x498 ), ( 0x4E4, 0x598 ), ( 0x5CC, 0x698 ),
              ( 0x6CC, 0x798 ), ( 0x8CC, 0x998 ), ( 0x99C, 0xA98 ), ( 0xACC, 0xB98 ),
              ( 0xBCC, 0xE98 ), ( 0xECC, 0xF98 ), ( 0xFCC, 0x1098 ), (0x10CC, 0x1198 ),
              ( 0x1220, 0x1298 ), ( 0x1308, 0x1398 ), ( 0x1408, 0x1498 ), ( 0x1508, 0x1598 ),
	      ( 0x15F0, 0x1698 ), ( 0x16CC, 0x1898 ), ( 0x18CC, 0x1998 ), ( 0x19CC, 0x1E98 ),
	      ( 0x1ECC, 0x1F98 ), ( 0x1FCC, 0x2098 ), ( 0x20CC, 0x2198 )] # Thanks DRGN!
free_space.append((0x18DCC0, 0x18E8C0)) # Tournament mode, size 0xC00

def read_data(data, offset, length):
    new_data = bytearray()
    new_data.extend(data[offset:offset+length])
    return new_data
    
def write_data(data, offset, new_data):
    data[offset:offset+len(new_data)] = new_data

def find_free_space(space_needed):
    for i in range(len(free_space)):
        size = free_space[i][1] - free_space[i][0]
        if size >= space_needed:
            free_space.append((free_space[i][0]+space_needed, free_space[i][1])) # Add leftover back to array
            return free_space.pop(i)
    print("Not enough free space! Abort")
    return (0,0)

def activate_gecko_code(code_path):
    def divide_into_words(data):
        words = []
        i = 0
        while i < number_of_bytes / 4:
            word = data[i*4:i*4+4]
            words.append(word)
            i += 1
            
        return words

    # Depending on where the gecko code points in RAM, the offset in
    # the DOL will be different.
    def to_dol_offset(address): # RAM > DOL
        if address <= 0x5520: # Text 0
            address = address - 0x3000
        elif address <= 0x5940: # Data 0&1
            address = address + 0x3AE900
        elif address <= 0x3B7240: # Text 1
            address = address - 0x3420
        elif address <= 0x4613C0: # Data 2&3&4&5
            address = address - 0x3000
        elif address <= 0x4D63A0: # Data 6
            address = address - 0xA4FE0
        elif address <= 0x4DEC00: # Data 7
            address = address - 0xA6620
        return address

    def to_ram_offset(address): # DOL > RAM
        if address <= 0x100: # Text 0
            address = address + 0x3000
        elif address <= 0x3B3E20: # Text 1
            address = address + 0x3420
        elif address <= 0x3B3FC0: # Data 0&1
            address = address - 0x3AE900
        elif address <= 0x42E6C0: # Data 2&3&4&5
            address = address + 0x3000
        elif address <= 0x4313C0: # Data 6
            address = address + 0xA4FE0
        elif address <= 0x4385E0: # Data 7
            address = address + 0xA6620
        return address

    def determine_branch_address(start, destination):
        number_of_instructions = (destination - start) // 4
        return number_of_instructions

    dol = melee.dol
    file = open(code_path, 'r')
    code = file.read()
    file.seek(0)
    number_of_bytes = len(file.readlines()*8)
    file.close()
    code = code.replace(" ", "")
    code = code.replace("\n", "")
    code = "0x" + code
    code = code.lower()
    code = int(code, 0)
    code = code.to_bytes(number_of_bytes, 'big')
    code = bytearray(code)
    code = divide_into_words(code)
    total_instruction_count = 0
    inject_offset = find_free_space(number_of_bytes)[0]
    if inject_offset == 0:
        return
    for i in range(len(code)):
        if code[i][0] == 0x04: # 32 Bits Write
            address = code[i][1:]
            address = get_value(address, 0, 24)
            address = to_dol_offset(address)
            instruction = code[i+1]
            instruction = get_value(instruction, 0, 32)
            dol_data = read_data(dol, address, 4)
            dol_data = set_value(dol_data, 0, 32, instruction)
            write_data(dol, address, dol_data)
            i += 1
        if code[i][0] == 0xC2: # Insert ASM
            # Increase offset by number of instructions, in case of multiple C2 instructions in the same code.
            inject_offset = inject_offset + total_instruction_count * 4

            # Add branch to ASM
            address = code[i][1:]
            address = get_value(address, 0, 24)
            dol_address = to_dol_offset(address)
            branch_address = determine_branch_address(address, to_ram_offset(inject_offset))
            branch_instruction = B(branch_address)
            write_data(dol, dol_address, branch_instruction)

            # Determine code to inject
            k = 2
            instructions = []
            while True:
                if get_value(code[i+k], 0, 32) == 0x00000000:
                    break
                instructions.append(code[i+k])
                k += 1

            # Add branch back to where we started to end of instructions
            branch_address = determine_branch_address(to_ram_offset(inject_offset+len(instructions)*4), address)
            instructions.append(B(branch_address+1))
    
            # Write instructions to dol
            for j in range(len(instructions)):
                offset = inject_offset + j*4
                write_data(dol, offset, instructions[j])
            i += k
            total_instruction_count += len(instructions)
    
    
    

    
