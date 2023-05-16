import iso, fst, gecko, characters
from fighters import bowser

# Work out ISO source
iso_file = open('test.iso', 'rb')
iso.iso_data = bytearray(iso_file.read())
iso_file.close()

# Grab ISO Files
melee_files = fst.get_files()

# Add Fighters from .dat files
characters.add_fighters(melee_files)
bowser.add_attacks()

# Music/Textures
fst.replace_file(melee_files, b'izumi.hps', 'music/test.hps')

# Gecko Codes
gecko.activate_gecko_code('codes/code.txt')

# Flags

# Finish
fst.build_iso(melee_files)
# Clean Up
melee_files = None
