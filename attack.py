class Attack():
    def __init__(self, fighter, attack_name):
        self.attack_name = attack_name
        self.fighter = fighter
        self.hitboxes = []
        self.strength = 0
        self.type = 0
        self.damage = 0
        self.angle = 0
        self.growth = 0
        self.base = 0
        self.set = 0
        self.element = 0
        self.sfx = 0
        #self.size = 0
        self.shield = 0
        self.balance = False
        self.random = False
        self.chaos = False
        self.empowered = False
        self.shuffled_with = self.fighter.name + " " + self.attack_name

    def get_parameters_from_reference_hitbox(self):
        if len(self.hitboxes) == 0: return
        ref = self.hitboxes[0]
        self.damage = ref.get_damage()
        self.angle = ref.get_angle()
        self.growth = ref.get_growth()
        self.base = ref.get_base()
        self.set = ref.get_set()
        self.element = ref.get_element()
        self.sfx = ref.get_sfx()
        #self.size = ref.get_size()
        self.shield = ref.get_shield()

    def set_parameters(self):
        if len(self.hitboxes) == 0: return
        for hb in self.hitboxes:
            hb.set_damage(self.damage)
            hb.set_angle(self.angle)
            hb.set_growth(self.growth)
            hb.set_base(self.base)
            hb.set_set(self.set)
            hb.set_element(self.element)
            hb.set_sfx(self.sfx)
            #hb.set_size(self.size)
            hb.set_shield(self.shield)
        
        
    


            





        


        
    
