def set_name(name):
    name_data = bytearray(0x40)
    name_ascii = bytearray(name + " - Melee Randomizer v1.0", 'ascii')
    name_data[0:len(name_ascii)] = name_ascii
    banner_file = open("Data/opening_ref.bnr", 'rb')
    banner_data = bytearray(banner_file.read())
    banner_file.close()
    banner_data[0x1860:0x18A0] = name_data
    new_banner_file = open("Data/opening.bnr", 'wb')
    new_banner_file.write(banner_data)
    new_banner_file.close()


