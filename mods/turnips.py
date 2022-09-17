# Turnip mod by drewlith. Changes what items can be pulled, the odds of each
# pull, and the damage of turnips.

# Mode 0 = Balanced
# Mode 1 = Items only, but with non-buggy items
# Mode 2 = turnips aren't balanced and buggy items included
# Mode 3+ = Items only and can be buggy items
import melee, random, util

good_ids = [5,6,7,11,12,13,14,15,16,17,19,20,21,22,23,24,25,30,34,40,42]
meme_ids = [0,1,2,3,4,8,9,10,18,26,27,28,29,31,32,33,43,44,45,46,47,161,162,163,164,165,166,
            167,168,169,170,171,172,173,174,175,176,177,178,179,180,181,182,
            183,184,185,186,187,188,189,190,205]

def start_mod(mode = 0):
    peach = melee.find_fighter("Peach")
    if peach == None: return
    if peach.properties_offset <= 0: return
    turnip_offset = 0x3A50 - peach.properties_offset
    turnip_data = bytearray(peach.property_data[turnip_offset:turnip_offset+32])
    #util.set_value(turnip_data,192,32, random.randint(2,8)) # Odds of item 1
    #util.set_value(turnip_data,128,32, random.randint(2,8)) # Odds of item 2
    #util.set_value(turnip_data,64,32, random.randint(2,8)) # Odds of item 3
    if mode == 0 or mode == 2: # Odds of item pull
        util.set_value(turnip_data,224,32,
                        random.randint(64,128)) # Between 1/64 and 1/128
    else:
        util.set_value(turnip_data,224,32,1) # 100% Chance
    if mode < 2:
        util.set_value(turnip_data,160,32,
                       good_ids[random.randint(0,len(good_ids)-1)]) # Item 1 ID
        util.set_value(turnip_data,96,32,
                       good_ids[random.randint(0,len(good_ids)-1)]) # Item 2 ID
        util.set_value(turnip_data,32,32,
                       good_ids[random.randint(0,len(good_ids)-1)]) # Item 3 ID
    else:
        for ids in good_ids: # Combine id value arrays so you can get normal and meme items
            meme_ids.append(ids)
        util.set_value(turnip_data,160,32,
                       meme_ids[random.randint(0,len(meme_ids)-1)]) # Item 1 ID
        util.set_value(turnip_data,96,32,
                       meme_ids[random.randint(0,len(meme_ids)-1)]) # Item 2 ID
        util.set_value(turnip_data,32,32,
                       meme_ids[random.randint(0,len(meme_ids)-1)]) # Item 3 ID

    turnip_offset_b = 0x4110 - peach.properties_offset # The actual turnip info is stored much later than item
    turnip_data_b = bytearray(peach.property_data[turnip_offset_b:turnip_offset_b+64])
    if mode > 0:
        util.set_value(turnip_data_b,480,32,random.randint(2,8)) # Odds of Turnip 1
        util.set_value(turnip_data_b,416,32,random.randint(2,8)) # Odds of Turnip 2
        util.set_value(turnip_data_b,352,32,random.randint(2,8)) # Odds of Turnip 3
        util.set_value(turnip_data_b,288,32,random.randint(2,8)) # Odds of Turnip 4
        util.set_value(turnip_data_b,224,32,random.randint(2,8)) # Odds of Turnip 5
        util.set_value(turnip_data_b,160,32,random.randint(2,8)) # Odds of Turnip 6
        util.set_value(turnip_data_b,96,32,random.randint(2,8)) # Odds of Turnip 7
        util.set_value(turnip_data_b,32,32,random.randint(2,8)) # Odds of Turnip 8

    if mode < 1: # Balanced
        util.set_value(turnip_data_b,448,32,random.randint(1,4)) # Damage of Turnip 1
        util.set_value(turnip_data_b,384,32,random.randint(1,4)) # Damage of Turnip 2
        util.set_value(turnip_data_b,320,32,random.randint(1,4)) # Damage of Turnip 3
        util.set_value(turnip_data_b,256,32,random.randint(1,4)) # Damage of Turnip 4
        util.set_value(turnip_data_b,192,32,random.randint(1,4)) # Damage of Turnip 5
        util.set_value(turnip_data_b,128,32,random.randint(4,8)) # Damage of Turnip 6
        util.set_value(turnip_data_b,64,32,random.randint(8,20)) # Damage of Turnip 7
        util.set_value(turnip_data_b,0,32,random.randint(20,40)) # Damage of Turnip 8
    else: # Unbalanced
        util.set_value(turnip_data_b,448,32,random.randint(1,10)) # Damage of Turnip 1
        util.set_value(turnip_data_b,384,32,random.randint(1,10)) # Damage of Turnip 2
        util.set_value(turnip_data_b,320,32,random.randint(1,10)) # Damage of Turnip 3
        util.set_value(turnip_data_b,256,32,random.randint(1,10)) # Damage of Turnip 4
        util.set_value(turnip_data_b,192,32,random.randint(1,10)) # Damage of Turnip 5
        util.set_value(turnip_data_b,128,32,random.randint(1,20)) # Damage of Turnip 6
        util.set_value(turnip_data_b,64,32,random.randint(1,30)) # Damage of Turnip 7
        util.set_value(turnip_data_b,0,32,random.randint(1,50)) # Damage of Turnip 8
    
    new_data = bytearray(peach.property_data)
    new_data[turnip_offset:turnip_offset+32] = turnip_data
    new_data[turnip_offset_b:turnip_offset_b+64] = turnip_data_b
    peach.property_data = bytes(new_data)
