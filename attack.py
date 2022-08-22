class Attack():
    def __init__(self, fighter, attack_name):
        self.attack_name = attack_name
        self.fighter = fighter
        self.hitboxes = []
        self.strength = 0
        self.type = 0
        self.balance = False
        self.shuffled = False
        self.shuffled_with = self.fighter.name + " " + self.attack_name
        self.notes = []
        self.original_stats = []
        
    def record_original_stats(self):
        self.original_stats.clear()
        self.original_stats.append(str(self.hitboxes[0].get_damage()))
        self.original_stats.append(str(self.hitboxes[0].get_angle()))
        self.original_stats.append(str(self.hitboxes[0].get_growth()))
        self.original_stats.append(str(self.hitboxes[0].get_base()))
        self.original_stats.append(str(self.hitboxes[0].get_set()))
        self.original_stats.append(str(self.hitboxes[0].get_shield()))
        self.original_stats.append(str(self.hitboxes[0].get_size()))
        self.original_stats.append(self.hitboxes[0].get_element())
        

        
        
    


            





        


        
    
