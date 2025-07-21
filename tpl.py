from utility import to_word
import iso

texture_file = iso.DAT(b'PlKpNr.dat')

debug = open("debug.dat", "wb")
debug.write(texture_file.pallete_data())
debug.close()






        