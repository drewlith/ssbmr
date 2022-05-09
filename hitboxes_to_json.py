import hitbox, util

path = "PlKp.dat"
elements = ["Normal", "Fire", "Electric", "Slash", "Coin", "Ice", "Sleep", "Sleep", "Grounded", "Grounded", "Cape", "None", "Disable", "Dark", "Screw Attack", "Flower", "None"]

data = bytearray(open(path, "rb").read())

hitboxes = []

last = 0
hb_count = 0


for i in range(len(data)):
    if data[i] == 0x2C or data[i] == 0x2D:
        hb = hitbox.Hitbox("")
        hb.data = data[i:i+20]
        hb.offset = i
        
        if i - last >= 20 and i % 4 == 0 and hb.get_element() < len(elements) and hb.get_damage() <= 50 and hb.get_angle() <= 362 and hb.get_growth() < 500:
            if hb.get_base() < 500 and hb.get_set() < 500 and hb.get_shield() < 200 and i < 80000:
                if i - last != 20:
                    hb_count = 0
                    print('},')
                    print()
                    print("DAM: ", str(hb.get_damage()), " | ANG: ", str(hb.get_angle()), " | KBG: ", str(hb.get_growth()), " | BKB: ", str(hb.get_base()), " | SHD: ", str(hb.get_shield()), " | ELE: ", elements[hb.get_element()])
                    print('"Attack at offset ' + str(i) + '": {')
                    print('\t"Type": 6,')
                    print('\t"Strength": 0,')
                print('\t"Hitbox ' + str(hb_count) + '": {')
                print('\t\t"Offset": ' + str(i))
                print('\t},')

                hb_count += 1
                hitboxes.append(hb)
                last = i

        
