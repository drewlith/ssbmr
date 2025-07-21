import iso
from utility import get_value, set_value, to_word

free_space = [( 0x2C8, 0x398 ), ( 0x39C, 0x498 ), ( 0x4E4, 0x598 ),
              ( 0x5CC, 0x698 ), ( 0x6CC, 0x798 ), ( 0x8CC, 0x998 ),
              ( 0x99C, 0xA98 ), ( 0xACC, 0xB98 ), ( 0xBCC, 0xE98 ),
              ( 0xECC, 0xF98 ), ( 0xFCC, 0x1098 ), (0x10CC, 0x1198 ),
              ( 0x1220, 0x1298 ), ( 0x1308, 0x1398 ), ( 0x1408, 0x1498 ),
              ( 0x1508, 0x1598 ), ( 0x15F0, 0x1698 ), ( 0x16CC, 0x1898 ),
              ( 0x18CC, 0x1998 ), ( 0x1ECC, 0x1F98 ), 
              ( 0x1FCC, 0x2098 ), ( 0x20CC, 0x2198 ),
              ( 0x3F73E8, 0x3F92EC ), ( 0x3F9420, 0x3FAC1C )]

def hex_to_words(data):
    words = []
    i = 0
    while i < len(data) / 4:
        word = data[i*4:i*4+4]
        words.append(word)
        i += 1
    return words

def expand_dol():
    dol = iso.get_dol()
    dol[0x003C:0x003C+4] = 0x4385E0.to_bytes(4, 'big')
    dol[0x0084:0x0084+4] = 0x804DEC00.to_bytes(4, 'big')
    dol[0x00CC:0x00CC+4] = 0x20.to_bytes(4, 'big')
    iso.write_dol(dol)

def find_free_space(space_needed):
    for i in range(len(free_space)):
        size = free_space[i][1] - free_space[i][0]
        if size >= space_needed:
            free_space.append((free_space[i][0]+space_needed, free_space[i][1])) # Add leftover back to array
            return free_space.pop(i)[0]
    print("Not enough free space! Abort")


def to_dol_offset(address): # RAM > DOL
    if address <= 0x5520: # Text 0
        return address - 0x3000
    if address <= 0x5940: # Data 0&1
        return address + 0x3AE900
    if address <= 0x3B7240: # Text 1
        return address - 0x3420
    if address <= 0x4613C0: # Data 2&3&4&5
        return address - 0x3000
    if address <= 0x4D63A0: # Data 6
        return address - 0xA4FE0
    if address <= 0x4DEC00: # Data 7
        return address - 0xA6620
    if address > 0x4DEC00: # Data 8
        return address - 0xA6620

def to_ram_offset(address): # DOL > RAM
    if address <= 0x100: # Text 0
        return address + 0x3000
    if address <= 0x3B3E20: # Text 1
        return address + 0x3420
    if address <= 0x3B3FC0: # Data 0&1
        return address - 0x3AE900
    if address <= 0x42E6C0: # Data 2&3&4&5
        return address + 0x3000
    if address <= 0x4313C0: # Data 6
        return address + 0xA4FE0
    if address <= 0x4385E0: # Data 7
        return address + 0xA6620
    if address > 0x4385E0: # Data 8
        return address + 0xA6620

def determine_branch_address(start, destination):
    return (destination - start) // 4

def code_from_text(code_path):
    code_file = open(code_path, 'r')
    code = code_file.read()
    code_file.seek(0)
    number_of_bytes = len(code_file.readlines()*8)
    code_file.close()
    code = code.replace(" ", "")
    code = code.replace("\n", "")
    code = "0x" + code
    code = code.lower()
    code = int(code, 0)
    code = code.to_bytes(number_of_bytes, 'big')
    code = bytearray(code)
    code = hex_to_words(code)
    return code

def branch(address): # Branch
    instruction = bytearray(4)
    instruction = set_value(instruction, 26, 6, 18)
    instruction = set_value(instruction, 2, 24, address)
    return instruction

def activate_gecko_code(code_path):
    print(code_path)
    dol = iso.get_dol()
    code = code_from_text(code_path)
    last_instruction_count = 0
    inject_offset = find_free_space(len(code*4))
    if inject_offset == None:
        return
    i = 0
    while i < len(code)-1:
        if code[i][0] != 0x04 and code[i][0] != 0xC2:
            i += 1
        if code[i][0] == 0x04: # 32 Bits Write
            address = code[i][1:]
            address = get_value(address, 0, 24)
            address = to_dol_offset(address)
            instruction = code[i+1]
            dol[address:address+4] = instruction
            i += 1
        if code[i][0] == 0xC2: # Insert ASM
            inject_offset = inject_offset + last_instruction_count * 4 # For Multiple C2
            address = code[i][1:]
            address = get_value(address, 0, 24)
            dol_address = to_dol_offset(address)
            branch_address = determine_branch_address(address, to_ram_offset(inject_offset))
            branch_instruction = branch(branch_address)
            dol[dol_address:dol_address+4] = branch_instruction

            k = 2 # 2 To jump ahead two lines in the code to get instructions.
            num_of_lines = get_value(code[i+1], 0, 32) # This line in the code contains number of code lines
            instructions = []
            while True:
                if get_value(code[i+k], 0, 32) == 0x00000000 and len(instructions) >= (num_of_lines * 2) -1:
                    break
                instructions.append(code[i+k])
                k += 1
            # Add branch back to where we started to end of instructions.
            branch_address = determine_branch_address(to_ram_offset(inject_offset+len(instructions)*4), address)
            instructions.append(branch(branch_address+1))
    
            # Write instructions to dol
            for j in range(len(instructions)):
                offset = inject_offset + j*4
                dol[offset:offset+4] = instructions[j]
            i += k # Jump ahead to start parsing the next section of the gecko code.
            last_instruction_count = len(instructions)
    
    iso.write_dol(dol)
