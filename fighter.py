from structs.attribute import Attribute
import iso

fighters = []
class Fighter():
    def __init__(self, name, dat_file):
        self.name = name
        self.dat_file = dat_file
        self.subactions = dat_file.get_subactions()
        self.attributes = []
        self.add_attributes(dat_file.get_attribute_data())
        self.special_attribute_block_size = []
        self.projectile_offsets = []
        self.projectile_hitboxes = []
        self.articles_sizes = []
        self.articles_offsets = []
        self.fighter_id = -1
        self.name_subactions()
        self.tag_subactions()

    def add_attribute(self, attribute_data, offset, name, special=0):
        attribute = Attribute(attribute_data[offset:offset+4], name, offset, special)
        self.attributes.append(attribute)

    def add_attributes(self, attribute_data):
        self.add_attribute(attribute_data, 0x0000, "Initial Walk Velocity")
        self.add_attribute(attribute_data, 0x0004, "Walk Acceleration")
        self.add_attribute(attribute_data, 0x0008, "Walk Maximum Velocity")
        self.add_attribute(attribute_data, 0x000C, "Slow Walk Max Velocity")
        self.add_attribute(attribute_data, 0x0010, "Mid Walk Threshold")
        self.add_attribute(attribute_data, 0x0014, "Fast Walk Threshold")
        self.add_attribute(attribute_data, 0x0018, "Grounded Friction")
        self.add_attribute(attribute_data, 0x001C, "Dash Initial Velocity")
        self.add_attribute(attribute_data, 0x0020, "Dash & Run Acceleration A")
        self.add_attribute(attribute_data, 0x0024, "Dash & Run Acceleration B")
        self.add_attribute(attribute_data, 0x0028, "Dash & Run Terminal Velocity")
        self.add_attribute(attribute_data, 0x002C, "Run Animation Scaling")
        self.add_attribute(attribute_data, 0x0030, "Run Acceleration")
        self.add_attribute(attribute_data, 0x0034, "Unknown Attribute 0x34")
        self.add_attribute(attribute_data, 0x0038, "Jumpsquat Frames")
        self.add_attribute(attribute_data, 0x003C, "Jump Horizontal Velocity")
        self.add_attribute(attribute_data, 0x0040, "Jump Vertical Velocity")
        self.add_attribute(attribute_data, 0x0044, "Jump Momentum Multiplier")
        self.add_attribute(attribute_data, 0x0048, "Jump Horizontal Max Velocity")
        self.add_attribute(attribute_data, 0x004C, "Shorthop Vertical Velocity")
        self.add_attribute(attribute_data, 0x0050, "Air Jump Multiplier")
        self.add_attribute(attribute_data, 0x0054, "Double Jump Momentum")
        self.add_attribute(attribute_data, 0x0058, "Number of Jumps") # Integer
        self.add_attribute(attribute_data, 0x005C, "Gravity Scale")
        self.add_attribute(attribute_data, 0x0060, "Terminal Velocity")
        self.add_attribute(attribute_data, 0x0064, "Air Mobility A")
        self.add_attribute(attribute_data, 0x0068, "Air Mobility B")
        self.add_attribute(attribute_data, 0x006C, "Aerial Horizontal Max Velocity")
        self.add_attribute(attribute_data, 0x0070, "Air Friction")
        self.add_attribute(attribute_data, 0x0074, "Fast Fall Terminal Velocity")
        self.add_attribute(attribute_data, 0x0078, "Unknown Attribute 0x78")
        self.add_attribute(attribute_data, 0x007C, "Jab 2 Frame Window")
        self.add_attribute(attribute_data, 0x0080, "Jab 3 Frame Window")
        self.add_attribute(attribute_data, 0x0084, "Turnaround Frames")
        self.add_attribute(attribute_data, 0x0088, "Weight")
        self.add_attribute(attribute_data, 0x008C, "Model Scale")
        self.add_attribute(attribute_data, 0x0090, "Shield Size")
        self.add_attribute(attribute_data, 0x0094, "Shield Break Velocity")
        self.add_attribute(attribute_data, 0x0098, "Rapid Jab Window (Frames)")
        self.add_attribute(attribute_data, 0x009C, "Unknown Attribute 0x9C")
        self.add_attribute(attribute_data, 0x00A0, "Unknown Attribute 0xA0")
        self.add_attribute(attribute_data, 0x00A4, "Unknown Attribute 0xA4")
        self.add_attribute(attribute_data, 0x00A8, "Ledgejump Horizontal Velocity")
        self.add_attribute(attribute_data, 0x00AC, "Ledgejump Vertical Velocity")
        self.add_attribute(attribute_data, 0x00B0, "Item Throw Velocity")
        self.add_attribute(attribute_data, 0x00B4, "Unknown Attribute 0xB4")
        self.add_attribute(attribute_data, 0x00B8, "Unknown Attribute 0xB8")
        self.add_attribute(attribute_data, 0x00BC, "Unknown Attribute 0xBC")
        self.add_attribute(attribute_data, 0x00C0, "Unknown Attribute 0xC0")
        self.add_attribute(attribute_data, 0x00C4, "Unknown Attribute 0xC4")
        self.add_attribute(attribute_data, 0x00C8, "Unknown Attribute 0xC8")
        self.add_attribute(attribute_data, 0x00CC, "Unknown Attribute 0xCC")
        self.add_attribute(attribute_data, 0x00D0, "Unknown Attribute 0xD0")
        self.add_attribute(attribute_data, 0x00D4, "Unknown Attribute 0xD4")
        self.add_attribute(attribute_data, 0x00D8, "Unknown Attribute 0xD8")
        self.add_attribute(attribute_data, 0x00DC, "Unknown Attribute 0xDC")
        self.add_attribute(attribute_data, 0x00E0, "Kirby Star Damage")
        self.add_attribute(attribute_data, 0x00E4, "Landing Lag Frames: Empty")
        self.add_attribute(attribute_data, 0x00E8, "Landing Lag Frames: Neutral Aerial")
        self.add_attribute(attribute_data, 0x00EC, "Landing Lag Frames: Forward Aerial")
        self.add_attribute(attribute_data, 0x00F0, "Landing Lag Frames: Back Aerial")
        self.add_attribute(attribute_data, 0x00F4, "Landing Lag Frames: Up Aerial")
        self.add_attribute(attribute_data, 0x00F8, "Landing Lag Frames: Down Aerial")
        self.add_attribute(attribute_data, 0x00FC, "Victory Screen Window Model Scale")
        self.add_attribute(attribute_data, 0x0100, "Unknown Attribute 0x100")
        self.add_attribute(attribute_data, 0x0104, "Wall Jump Horizontal Velocity")
        self.add_attribute(attribute_data, 0x0108, "Wall Jump Vertical Velocity")
        self.add_attribute(attribute_data, 0x010C, "Unknown Attribute 0x10C")
        self.add_attribute(attribute_data, 0x0110, "Unknown Attribute 0x110")
        self.add_attribute(attribute_data, 0x0114, "Unknown Attribute 0x114")
        self.add_attribute(attribute_data, 0x0118, "Unknown Attribute 0x118")
        self.add_attribute(attribute_data, 0x011C, "Unknown Attribute 0x11C")
        self.add_attribute(attribute_data, 0x0120, "Unknown Attribute 0x120")
        self.add_attribute(attribute_data, 0x0124, "Unknown Attribute 0x124")
        self.add_attribute(attribute_data, 0x0128, "Unknown Attribute 0x128")
        self.add_attribute(attribute_data, 0x012C, "Unknown Attribute 0x12C")
        self.add_attribute(attribute_data, 0x0130, "Unknown Attribute 0x130")
        self.add_attribute(attribute_data, 0x0134, "Unknown Attribute 0x134")
        self.add_attribute(attribute_data, 0x0138, "Unknown Attribute 0x138")
        self.add_attribute(attribute_data, 0x013C, "Unknown Attribute 0x13C")
        self.add_attribute(attribute_data, 0x0140, "Unknown Attribute 0x140")
        self.add_attribute(attribute_data, 0x0144, "Unknown Attribute 0x144")
        self.add_attribute(attribute_data, 0x0148, "Unknown Attribute 0x148")
        self.add_attribute(attribute_data, 0x014C, "Bubble Ratio")
        self.add_attribute(attribute_data, 0x0150, "Freeze Offset 1")
        self.add_attribute(attribute_data, 0x0154, "Freeze Offset 2")
        self.add_attribute(attribute_data, 0x0158, "Freeze Escape Height")
        self.add_attribute(attribute_data, 0x015C, "Unknown Attribute 0x15C")
        self.add_attribute(attribute_data, 0x0160, "Ice Traction")
        self.add_attribute(attribute_data, 0x0164, "Unknown Attribute 0x164")
        self.add_attribute(attribute_data, 0x0168, "Unknown Attribute 0x168")
        self.add_attribute(attribute_data, 0x016C, "Camera Zoom Bone Target")
        self.add_attribute(attribute_data, 0x0170, "Unknown Attribute 0x170")
        self.add_attribute(attribute_data, 0x0174, "Unknown Attribute 0x174")
        self.add_attribute(attribute_data, 0x0178, "Unknown Attribute 0x178")
        self.add_attribute(attribute_data, 0x017C, "Unknown Attribute 0x17C")
        # Assign special properties
        self.get_attribute("Number of Jumps").integer = True
        self.get_attribute("Rapid Jab Window (Frames)").integer = True
        self.get_attribute("Camera Zoom Bone Target").integer = True
        self.get_attribute("Jumpsquat Frames").whole_number = True
        self.get_attribute("Jab 2 Frame Window").whole_number = True
        self.get_attribute("Jab 3 Frame Window").whole_number = True
        self.get_attribute("Turnaround Frames").whole_number = True
        self.get_attribute("Weight").whole_number = True
        self.get_attribute("Kirby Star Damage").whole_number = True
        self.get_attribute("Landing Lag Frames: Empty").whole_number = True
        self.get_attribute("Landing Lag Frames: Neutral Aerial").whole_number = True
        self.get_attribute("Landing Lag Frames: Forward Aerial").whole_number = True
        self.get_attribute("Landing Lag Frames: Back Aerial").whole_number = True
        self.get_attribute("Landing Lag Frames: Up Aerial").whole_number = True
        self.get_attribute("Landing Lag Frames: Down Aerial").whole_number = True
        # Assign Tags
        self.get_attribute("Initial Walk Velocity").tags.extend(["walk", "velocity"])
        self.get_attribute("Walk Acceleration").tags.extend(["walk", "acceleration"])
        self.get_attribute("Walk Maximum Velocity").tags.extend(["walk", "velocity"])
        self.get_attribute("Slow Walk Max Velocity").tags.extend(["walk"])
        self.get_attribute("Mid Walk Threshold").tags.extend(["walk"])
        self.get_attribute("Fast Walk Threshold").tags.extend(["walk"])
        self.get_attribute("Grounded Friction").tags.extend(["ground", "friction"])
        self.get_attribute("Dash Initial Velocity").tags.extend(["dash", "velocity"])
        self.get_attribute("Dash & Run Acceleration A").tags.extend(["dash", "run", "acceleration"])
        self.get_attribute("Dash & Run Acceleration B").tags.extend(["dash", "run", "acceleration"])
        self.get_attribute("Dash & Run Terminal Velocity").tags.extend(["run", "dash", "terminal", "velocity"])
        self.get_attribute("Run Animation Scaling").tags.extend(["run", "animation"])
        self.get_attribute("Run Acceleration").tags.extend(["run", "acceleration"])
        self.get_attribute("Unknown Attribute 0x34").tags.extend(["unknown"])
        self.get_attribute("Jumpsquat Frames").tags.extend(["jumpsquat", "frame_data"])
        self.get_attribute("Jump Horizontal Velocity").tags.extend(["jump", "horizontal", "velocity"])
        self.get_attribute("Jump Vertical Velocity").tags.extend(["jump", "vertical", "velocity"])
        self.get_attribute("Jump Momentum Multiplier").tags.extend(["jump", "momentum", "multiplier"])
        self.get_attribute("Jump Horizontal Max Velocity").tags.extend(["jump", "horizontal", "velocity"])
        self.get_attribute("Shorthop Vertical Velocity").tags.extend(["shorthop", "vertical", "velocity"])
        self.get_attribute("Air Jump Multiplier").tags.extend(["jump", "air_movement"])
        self.get_attribute("Double Jump Momentum").tags.extend(["jump", "momentum"])
        self.get_attribute("Number of Jumps").tags.extend(["unknown"]) # Integer
        self.get_attribute("Gravity Scale").tags.extend(["gravity"])
        self.get_attribute("Terminal Velocity").tags.extend(["velocity", "terminal"])
        self.get_attribute("Air Mobility A").tags.extend(["air_movement"])
        self.get_attribute("Air Mobility B").tags.extend(["air_movement"])
        self.get_attribute("Aerial Horizontal Max Velocity").tags.extend(["air_movement", "horizontal", "velocity"])
        self.get_attribute("Air Friction").tags.extend(["air_movement", "friction"])
        self.get_attribute("Fast Fall Terminal Velocity").tags.extend(["fall", "velocity", "terminal"])
        self.get_attribute("Unknown Attribute 0x78").tags.extend(["unknown"])
        self.get_attribute("Jab 2 Frame Window").tags.extend(["frame_data"])
        self.get_attribute("Jab 3 Frame Window").tags.extend(["frame_data"])
        self.get_attribute("Turnaround Frames").tags.extend(["frame_data"])
        self.get_attribute("Weight").tags.extend(["weight"])
        self.get_attribute("Model Scale").tags.extend(["model_size"])
        self.get_attribute("Shield Break Velocity").tags.extend(["shield", "model_size"])
        self.get_attribute("Rapid Jab Window (Frames)").tags.extend(["frame_data"])
        self.get_attribute("Unknown Attribute 0x9C").tags.extend(["unknown"])
        self.get_attribute("Unknown Attribute 0xA0").tags.extend(["unknown"])
        self.get_attribute("Unknown Attribute 0xA4").tags.extend(["unknown"])
        self.get_attribute("Ledgejump Horizontal Velocity").tags.extend(["jump", "horizontal", "velocity"])
        self.get_attribute("Ledgejump Vertical Velocity").tags.extend(["jump", "vertical", "velocity"])
        self.get_attribute("Item Throw Velocity").tags.extend(["item", "velocity"])
        self.get_attribute("Unknown Attribute 0xB4").tags.extend(["unknown"])
        self.get_attribute("Unknown Attribute 0xB8").tags.extend(["unknown"])
        self.get_attribute("Unknown Attribute 0xBC").tags.extend(["unknown"])
        self.get_attribute("Unknown Attribute 0xC0").tags.extend(["unknown"])
        self.get_attribute("Unknown Attribute 0xC4").tags.extend(["unknown"])
        self.get_attribute("Unknown Attribute 0xC8").tags.extend(["unknown"])
        self.get_attribute("Unknown Attribute 0xCC").tags.extend(["unknown"])
        self.get_attribute("Unknown Attribute 0xD0").tags.extend(["unknown"])
        self.get_attribute("Unknown Attribute 0xD4").tags.extend(["unknown"])
        self.get_attribute("Unknown Attribute 0xD8").tags.extend(["unknown"])
        self.get_attribute("Unknown Attribute 0xDC").tags.extend(["unknown"])
        self.get_attribute("Kirby Star Damage").tags.extend(["attribute_damage"])
        self.get_attribute("Landing Lag Frames: Empty").tags.extend(["landing_lag", "frame_data"])
        self.get_attribute("Landing Lag Frames: Neutral Aerial").tags.extend(["landing_lag", "frame_data"])
        self.get_attribute("Landing Lag Frames: Forward Aerial").tags.extend(["landing_lag", "frame_data"])
        self.get_attribute("Landing Lag Frames: Back Aerial").tags.extend(["landing_lag", "frame_data"])
        self.get_attribute("Landing Lag Frames: Up Aerial").tags.extend(["landing_lag", "frame_data"])
        self.get_attribute("Landing Lag Frames: Down Aerial").tags.extend(["landing_lag", "frame_data"])
        self.get_attribute("Victory Screen Window Model Scale").tags.extend(["model_size"])
        self.get_attribute("Unknown Attribute 0x100").tags.extend(["unknown"])
        self.get_attribute("Wall Jump Horizontal Velocity").tags.extend(["wall", "jump", "horizontal", "velocity"])
        self.get_attribute("Wall Jump Vertical Velocity").tags.extend(["wall", "jump", "vertical", "velocity"])
        self.get_attribute("Unknown Attribute 0x10C").tags.extend(["unknown"])
        self.get_attribute("Unknown Attribute 0x110").tags.extend(["unknown"])
        self.get_attribute("Unknown Attribute 0x114").tags.extend(["unknown"])
        self.get_attribute("Unknown Attribute 0x118").tags.extend(["unknown"])
        self.get_attribute("Unknown Attribute 0x11C").tags.extend(["unknown"])
        self.get_attribute("Unknown Attribute 0x120").tags.extend(["unknown"])
        self.get_attribute("Unknown Attribute 0x124").tags.extend(["unknown"])
        self.get_attribute("Unknown Attribute 0x128").tags.extend(["unknown"])
        self.get_attribute("Unknown Attribute 0x12C").tags.extend(["unknown"])
        self.get_attribute("Unknown Attribute 0x130").tags.extend(["unknown"])
        self.get_attribute("Unknown Attribute 0x134").tags.extend(["unknown"])
        self.get_attribute("Unknown Attribute 0x138").tags.extend(["unknown"])
        self.get_attribute("Unknown Attribute 0x13C").tags.extend(["unknown"])
        self.get_attribute("Unknown Attribute 0x140").tags.extend(["unknown"])
        self.get_attribute("Unknown Attribute 0x144").tags.extend(["unknown"])
        self.get_attribute("Unknown Attribute 0x148").tags.extend(["unknown"])
        self.get_attribute("Bubble Ratio").tags.extend(["bubble"])
        self.get_attribute("Freeze Offset 1").tags.extend(["freeze"])
        self.get_attribute("Freeze Offset 2").tags.extend(["freeze"])
        self.get_attribute("Freeze Escape Height").tags.extend(["freeze"])
        self.get_attribute("Unknown Attribute 0x15C").tags.extend(["unknown"])
        self.get_attribute("Ice Traction").tags.extend(["ice"])
        self.get_attribute("Unknown Attribute 0x164").tags.extend(["unknown"])
        self.get_attribute("Unknown Attribute 0x168").tags.extend(["unknown"])
        self.get_attribute("Camera Zoom Bone Target").tags.extend(["camera"])
        self.get_attribute("Unknown Attribute 0x174").tags.extend(["unknown"])
        self.get_attribute("Unknown Attribute 0x170").tags.extend(["unknown"])
        self.get_attribute("Unknown Attribute 0x17C").tags.extend(["unknown"])
        self.get_attribute("Unknown Attribute 0x178").tags.extend(["unknown"])

    def get_attribute(self, name):
        for attribute in self.attributes:
            if name in attribute.name:
                return attribute
        print("No attribute found with name: ", name)

    def get_subaction(self, name):
        for subaction in self.subactions:
            if name in subaction.friendly_name:
                return subaction
        print("No subaction found with name: ", name)

    def name_subactions(self):
        actions = self.subactions
        # Normals
        actions[46].friendly_name = "Jab 1"
        actions[47].friendly_name = "Jab 2"
        actions[48].friendly_name = "Jab 3"
        actions[52].friendly_name = "Dash Attack"
        actions[53].friendly_name = "Forward Tilt (Highest)"
        actions[54].friendly_name = "Forward Tilt (Mid-High)"
        actions[55].friendly_name = "Forward Tilt (Middle)"
        actions[56].friendly_name = "Forward Tilt (Mid-Low)"
        actions[57].friendly_name = "Forward Tilt (Lowest)"
        actions[58].friendly_name = "Up Tilt"
        actions[59].friendly_name = "Down Tilt"
        actions[60].friendly_name = "Forward Smash (Highest)"
        actions[61].friendly_name = "Forward Smash (Mid-High)"
        actions[62].friendly_name = "Forward Smash (Middle)"
        actions[63].friendly_name = "Forward Smash (Mid-Low)"
        actions[64].friendly_name = "Forward Smash (Lowest)"
        actions[66].friendly_name = "Up Smash"
        actions[67].friendly_name = "Down Smash"
        actions[68].friendly_name = "Neutral Aerial"
        actions[69].friendly_name = "Forward Aerial"
        actions[70].friendly_name = "Back Aerial"
        actions[71].friendly_name = "Up Aerial"
        actions[72].friendly_name = "Down Aerial"
        actions[187].friendly_name = "Get-Up Attack (Up)"
        actions[195].friendly_name = "Get-Up Attack (Down)"
        actions[221].friendly_name = "Ledge Attack Slow"
        actions[222].friendly_name = "Ledge Attack Fast"
        actions[245].friendly_name = "Pummel"
        # Throws
        actions[247].friendly_name = "Forward Throw"
        actions[248].friendly_name = "Back Throw"
        actions[249].friendly_name = "Up Throw"
        actions[250].friendly_name = "Down Throw"
        # Items
        actions[108].friendly_name = "Beam Sword Neutral Attack"
        actions[109].friendly_name = "Beam Sword Tilt Attack"
        actions[110].friendly_name = "Beam Sword Smash Attack"
        actions[111].friendly_name = "Beam Sword Dash Attack"
        actions[112].friendly_name = "Home-run Bat Neutral Attack"
        actions[113].friendly_name = "Home-run Bat Tilt Attack"
        actions[114].friendly_name = "Home-run Bat Smash Attack"
        actions[115].friendly_name = "Home-run Bat Dash Attack"
        actions[116].friendly_name = "Parasol Neutral Attack"
        actions[117].friendly_name = "Parasol Tilt Attack"
        actions[118].friendly_name = "Parasol Smash Attack"
        actions[119].friendly_name = "Parasol Dash Attack"
        actions[120].friendly_name = "Fan Neutral Attack"
        actions[121].friendly_name = "Fan Tilt Attack"
        actions[122].friendly_name = "Fan Smash Attack"
        actions[123].friendly_name = "Fan Dash Attack"
        actions[124].friendly_name = "Star Rod Neutral Attack"
        actions[125].friendly_name = "Star Rod Tilt Attack"
        actions[126].friendly_name = "Star Rod Smash Attack"
        actions[127].friendly_name = "Star Rod Dash Attack"
        actions[128].friendly_name = "Lip's Stick Neutral Attack"
        actions[129].friendly_name = "Lip's Stick Tilt Attack"
        actions[130].friendly_name = "Lip's Stick Smash Attack"
        actions[131].friendly_name = "Lip's Stick Dash Attack"
        actions[144].friendly_name = "Screw Attack 1"
        actions[145].friendly_name = "Screw Attack 2"

    def tag_subactions(self):
        actions = self.subactions
        # Normals
        actions[46].add_hitbox_tags(["normal", "jab", "jab1"]) #Jab 1#
        actions[47].add_hitbox_tags(["normal", "jab", "jab2"]) #Jab 2#
        actions[48].add_hitbox_tags(["normal", "jab", "jab3"]) #Jab 3#
        actions[52].add_hitbox_tags(["normal", "dash"]) #Dash Attack#
        actions[53].add_hitbox_tags(["normal", "tilt", "ftilt", "angled"]) #Forward Tilt (Highest)#
        actions[54].add_hitbox_tags(["normal", "tilt", "ftilt", "angled"]) #Forward Tilt (Mid-High)#
        actions[55].add_hitbox_tags(["normal", "tilt", "ftilt"]) #Forward Tilt (Middle)#
        actions[56].add_hitbox_tags(["normal", "tilt", "ftilt", "angled"]) #Forward Tilt (Mid-Low)#
        actions[57].add_hitbox_tags(["normal", "tilt", "ftilt", "angled"]) #Forward Tilt (Lowest)#
        actions[58].add_hitbox_tags(["normal", "tilt", "utilt"]) #Up Tilt#
        actions[59].add_hitbox_tags(["normal", "tilt", "dtilt"]) #Down Tilt#
        actions[60].add_hitbox_tags(["normal", "smash", "charge", "fsmash", "angled"]) #Forward Smash (Highest)#
        actions[61].add_hitbox_tags(["normal", "smash", "charge", "fsmash", "angled"]) #Forward Smash (Mid-High)#
        actions[62].add_hitbox_tags(["normal", "smash", "charge", "fsmash"]) #Forward Smash (Middle)#
        actions[63].add_hitbox_tags(["normal", "smash", "charge", "fsmash", "angled"]) #Forward Smash (Mid-Low)#
        actions[64].add_hitbox_tags(["normal", "smash", "charge", "fsmash", "angled"]) #Forward Smash (Lowest)#
        actions[66].add_hitbox_tags(["normal", "smash", "charge", "usmash"]) #Up Smash#
        actions[67].add_hitbox_tags(["normal", "smash", "charge", "dsmash"]) #Down Smash#
        actions[68].add_hitbox_tags(["normal", "nair", "aerial"]) #Neutral Aerial#
        actions[69].add_hitbox_tags(["normal", "fair", "aerial"]) #Forward Aerial#
        actions[70].add_hitbox_tags(["normal", "bair", "aerial"]) #Back Aerial#
        actions[71].add_hitbox_tags(["normal", "uair", "aerial"]) #Up Aerial#
        actions[72].add_hitbox_tags(["normal", "dair", "aerial"]) #Down Aerial#
        actions[187].add_hitbox_tags(["normal", "tech", "getup"]) #Get-Up Attack (Up)#
        actions[195].add_hitbox_tags(["normal", "tech", "getup"]) #Get-Up Attack (Down)#
        actions[221].add_hitbox_tags(["normal", "tech", "ledge"]) #Ledge Attack Slow#
        actions[222].add_hitbox_tags(["normal", "tech", "ledge"]) #Ledge Attack Fast#
        actions[245].add_hitbox_tags(["normal", "pummel"]) #Pummel#
        actions[247].add_throw_tags(["throw", "fthrow"]) #Forward Throw#
        actions[248].add_throw_tags(["throw", "bthrow"]) #Back Throw#
        actions[249].add_throw_tags(["throw", "uthrow"]) #Up Throw#
        actions[250].add_throw_tags(["throw", "dthrow"]) #Down Throw#
        actions[108].add_hitbox_tags(["item", "beamsword", "jab"]) #Beam Sword Neutral Attack#
        actions[109].add_hitbox_tags(["item", "beamsword", "tilt"]) #Beam Sword Tilt Attack#
        actions[110].add_hitbox_tags(["item", "beamsword", "smash"]) #Beam Sword Smash Attack#
        actions[111].add_hitbox_tags(["item", "beamsword", "dash"]) #Beam Sword Dash Attack#
        actions[112].add_hitbox_tags(["item", "bat", "jab"]) #Home-run Bat Neutral Attack#
        actions[113].add_hitbox_tags(["item", "bat", "tilt"]) #Home-run Bat Tilt Attack#
        actions[114].add_hitbox_tags(["item", "bat", "ko", "smash"]) #Home-run Bat Smash Attack#
        actions[115].add_hitbox_tags(["item", "bat", "dash"]) #Home-run Bat Dash Attack#
        actions[116].add_hitbox_tags(["item", "parasol", "jab"]) #Parasol Neutral Attack#
        actions[117].add_hitbox_tags(["item", "parasol", "tilt"]) #Parasol Tilt Attack#
        actions[118].add_hitbox_tags(["item", "parasol", "smash"]) #Parasol Smash Attack#
        actions[119].add_hitbox_tags(["item", "parasol", "dash"]) #Parasol Dash Attack#
        actions[120].add_hitbox_tags(["item", "fan", "jab"]) #Fan Neutral Attack#
        actions[121].add_hitbox_tags(["item", "fan", "tilt"]) #Fan Tilt Attack#
        actions[122].add_hitbox_tags(["item", "fan", "smash"]) #Fan Smash Attack#
        actions[123].add_hitbox_tags(["item", "fan", "dash"]) #Fan Dash Attack#
        actions[124].add_hitbox_tags(["item", "starrod", "jab"]) #Star Rod Neutral Attack#
        actions[125].add_hitbox_tags(["item", "starrod", "tilt"]) #Star Rod Tilt Attack#
        actions[126].add_hitbox_tags(["item", "starrod", "smash"]) #Star Rod Smash Attack#
        actions[127].add_hitbox_tags(["item", "starrod", "dash"]) #Star Rod Dash Attack#
        actions[128].add_hitbox_tags(["item", "lipsstick", "jab"]) #Lip's Stick Neutral Attack#
        actions[129].add_hitbox_tags(["item", "lipsstick", "tilt"]) #Lip's Stick Tilt Attack#
        actions[130].add_hitbox_tags(["item", "lipsstick", "smash"]) #Lip's Stick Smash Attack#
        actions[131].add_hitbox_tags(["item", "lipsstick", "dash"]) #Lip's Stick Dash Attack#
        actions[144].add_hitbox_tags(["item", "screwattack"]) #Screw Attack 1#
        actions[145].add_hitbox_tags(["item", "screwattack"]) #Screw Attack 2#

        for action in actions:
            i = 0
            hit_number = 1
            last_offset = 0
            for hitbox in action.hitboxes: # Add tag for hitbox ID
                if (hitbox.offset - last_offset) > 20 and last_offset > 0: # Check if the attack has multiple hits
                    i = 0
                    hit_number += 1
                    action.multiple_hits = True
                last_offset = hitbox.offset
                hitbox.add_tags(["hitbox" + str(i), "hit" + str(hit_number)])
                i += 1
            
            for hitbox in action.hitboxes: 
                if hitbox.angle >= 260 and hitbox.angle <= 280: # Add tag for Meteors
                    hitbox.tags.append("meteor")
                if (hitbox.angle > 280 and hitbox.angle < 310) or (hitbox.angle < 260 and hitbox.angle > 230): # Add tag for Spikes
                    hitbox.tags.append("spike")
                if hitbox.angle == 361: # Add tag for sakurai angle
                    hitbox.tags.append("sakurai")
                if hitbox.setkb > 0: # Add tag for set knockback attacks
                    hitbox.tags.append("setknockback")

        def tag_sweetspots(hitboxes):
            def check_if_all_equal(array):
                if not array:
                    return
                first = array[0]
                for array in array:
                    if array != first:
                        return False
                return True
            
            def no_meaningful_difference(array):
                if max(array) - min(array) < 3:
                    return True
                else:
                    return False
            
            def compare_property_and_tag(property_name, hitboxes):
                property_values = []
                for hitbox in hitboxes:
                    property_values.append(getattr(hitbox, property_name))
                if check_if_all_equal(property_values):
                    return
                if no_meaningful_difference(property_values):
                    return
                highest = max(property_values)
                highest_index = property_values.index(highest)
                if not hitboxes[highest_index].check_tags("sweetspot"):
                    hitboxes[highest_index].tags.append("sweetspot")
                lowest = min(property_values)
                lowest_index = property_values.index(lowest)
                if not hitboxes[lowest_index].check_tags("sourspot"):
                    hitboxes[lowest_index].tags.append("sourspot")
                # For sweetspots/sourspots that span multiple hitboxes
                for hitbox in hitboxes:
                    if getattr(hitbox, property_name) == highest:
                        if not hitbox.check_tags("sweetspot"):
                            hitbox.tags.append("sweetspot")
                    if getattr(hitbox, property_name) == lowest:
                        if not hitbox.check_tags("sourspot"):
                            hitbox.tags.append("sourspot")

            compare_property_and_tag("damage", hitboxes)
            compare_property_and_tag("base", hitboxes)
            #compare_property_and_tag("growth", hitboxes)

        def determine_strong_hits(hits):
            if len(hits) != 2: # Probably not needed to check if it's more than 2 hits since each hit can vary wildly at that point
                return
            if hits[1][0].damage < hits[0][0].damage:
                for hitbox in hits[1]:
                    hitbox.add_tags(["latehit", "weakhit", "secondhit"])
                for hitbox in hits[0]:
                    hitbox.add_tags(["earlyhit", "stronghit", "firsthit"])
            elif hits[1][0].damage > hits[0][0].damage:
                for hitbox in hits[1]:
                    hitbox.add_tags(["stronghit", "secondhit"])
                for hitbox in hits[0]:
                    hitbox.add_tags(["weakhit", "firsthit"])

        for action in actions: # Determine Sweet Spots/Sour Spots, late hits, weak hits
            if action.multiple_hits and len(action.hitboxes) > 0: # Per Hit for Multi-hit moves
                hits = []
                last_offset = 0
                number_of_hits = 0
                for hitbox in action.hitboxes:
                    if (hitbox.offset - last_offset) > 20:
                        number_of_hits += 1
                        hits.append([])
                    hits[number_of_hits-1].append(hitbox)
                    last_offset = hitbox.offset
                for hit in hits:
                    tag_sweetspots(hit)
                determine_strong_hits(hits)
            elif len(action.hitboxes) > 0: # Not Multi-hit
                tag_sweetspots(action.hitboxes)


def get_fighter(name):
    for _fighter in fighters:
        if _fighter.name in name:
            return _fighter
    print("No fighter found with name", name)

def write_fighter_data():
    fst = iso.fst
    for _fighter in fighters:
        subaction_data = bytearray()
        for subaction in _fighter.subactions:
            subaction_data.extend(subaction.data)
            subaction.write_events()
        _fighter.dat_file.write_subaction_data(subaction_data)
        for attribute in _fighter.attributes:
            _fighter.dat_file.write_attribute_data(attribute, _fighter)
        for projectile in _fighter.projectile_hitboxes:
            offset = projectile.offset
            _fighter.dat_file.file_data[offset:offset+20] = projectile.data

    iso.find_file(_fighter.dat_file.file_name).file_data = _fighter.dat_file.file_data