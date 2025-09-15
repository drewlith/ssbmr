import iso
import struct
from utility import to_word

class PlCo:
    def __init__(self):
        self.data = iso.find_file(b'PlCo.dat').file_data
    
    @property
    def knockback_multiplier(self): 
        return struct.unpack('>f',self.data[0xA0FC:0xA0FC+4])[0]
    
    @knockback_multiplier.setter
    def knockback_multiplier(self, value): 
        self.data[0xA0FC:0xA0FC+4] = struct.pack('>f', value)

    @property
    def hitstun_multiplier(self): 
        return struct.unpack('>f',self.data[0xA134:0xA134+4])[0]
    
    @hitstun_multiplier.setter
    def hitstun_multiplier(self, value): 
        self.data[0xA134:0xA134+4] = struct.pack('>f', value)

    @property
    def base_hitlag(self): 
        return struct.unpack('>f',self.data[0xA17C:0xA17C+4])[0]
    
    @base_hitlag.setter
    def base_hitlag(self, value): 
        self.data[0xA17C:0xA17C+4] = struct.pack('>f', value)
    
    @property
    def l_cancel_leniency(self): 
        return to_word(self.data[0xA0C4:0xA0C4+4])
    
    @l_cancel_leniency.setter
    def l_cancel_leniency(self, value): 
        self.data[0xA0C4:0xA0C4+4] = value.to_bytes(4, 'big')

    @property
    def l_cancel_divisor(self): 
        return struct.unpack('>f',self.data[0xA0C8:0xA0C8+4])[0]
    
    @l_cancel_divisor.setter
    def l_cancel_divisor(self, value): 
        self.data[0xA0C8:0xA0C8+4] = struct.pack('>f', value)

    @property
    def shield_hp(self): 
        return struct.unpack('>f',self.data[0xA240:0xA240+4])[0]
    
    @shield_hp.setter
    def shield_hp(self, value): 
        self.data[0xA240:0xA240+4] = struct.pack('>f', value)

    @property
    def shield_release(self): 
        return struct.unpack('>f',self.data[0xA248:0xA248+4])[0]
    
    @shield_release.setter
    def shield_release(self, value): 
        self.data[0xA248:0xA248+4] = struct.pack('>f', value)
    
    @property
    def shield_stun(self): 
        return struct.unpack('>f',self.data[0xA270:0xA270+4])[0]
    
    @shield_stun.setter
    def shield_stun(self, value): 
        self.data[0xA270:0xA270+4] = struct.pack('>f', value)

    @property
    def air_dodge_speed(self): 
        return struct.unpack('>f',self.data[0xA318:0xA318+4])[0]
    
    @air_dodge_speed.setter
    def air_dodge_speed(self, value): 
        self.data[0xA318:0xA318+4] = struct.pack('>f', value)

    @property
    def air_dodge_lag(self): 
        return struct.unpack('>f',self.data[0xA324:0xA324+4])[0]
    
    @air_dodge_lag.setter
    def air_dodge_lag(self, value): 
        self.data[0xA324:0xA324+4] = struct.pack('>f', value)

    @property
    def ledge_timeout(self): 
        return to_word(self.data[0xA478:0xA478+4])
    
    @ledge_timeout.setter
    def ledge_timeout(self, value):
        self.data[0xA478:0xA478+4] = value.to_bytes(4, 'big')

    @property
    def ledge_invincibility(self): 
        return to_word(self.data[0xA47C:0xA47C+4])
    
    @ledge_invincibility.setter
    def ledge_invincibility(self, value):
        self.data[0xA47C:0xA47C+4] = value.to_bytes(4, 'big')

    @property
    def respawn_timer(self): 
        return to_word(self.data[0xA4E0:0xA4E0+4])
    
    @respawn_timer.setter
    def respawn_timer(self, value):
        self.data[0xA4E0:0xA4E0+4] = value.to_bytes(4, 'big')

    

