import melee
elements = ["Normal", "Fire", "Electric", "Slash", "Coin", "Ice", "Sleep", "Sleep",
            "BUGGED REPORT TO DREWLITH", "Grounded", "Cape", "Special", "Disable", "Dark", "Screw Attack",
            "Flower", "None"]
throw_elements = ["Normal", "Fire", "Electric", "Ice", "Darkness"]
def start_mod(flags):
    log = {}
    log["flags"] = flags
    for fighter in melee.fighters:
        attribute_dict = {}
        attack_dict = {}
        throw_dict = {}
        if fighter.shuffled:
            attribute_dict["shuffle_target"] = fighter.shuffle_target.name
        else:
            attribute_dict["shuffle_target"] = "None"
        for attribute in fighter.attributes:
            attribute.original_value = float(attribute.original_value)
            if attribute.name != "???":
                attribute_dict[attribute.name] = {"original":attribute.original_value,"new":attribute.get_value()}
        for attack in fighter.attacks:
            damage_dict = {"original":int(attack.original_stats[0]),"new":attack.hitboxes[0].get_damage()}
            shield_dict = {"original":int(attack.original_stats[5]),"new":attack.hitboxes[0].get_shield()}
            angle_dict = {"original":int(attack.original_stats[1]),"new":attack.hitboxes[0].get_angle()}
            base_dict = {"original":int(attack.original_stats[3]),"new":attack.hitboxes[0].get_base()}
            growth_dict = {"original":int(attack.original_stats[2]),"new":attack.hitboxes[0].get_growth()}
            set_dict = {"original":int(attack.original_stats[4]),"new":attack.hitboxes[0].get_set()}
            size_dict = {"original":int(attack.original_stats[6]),"new":attack.hitboxes[0].get_size()}
            element_dict = {"original":elements[attack.original_stats[7]],"new":elements[attack.hitboxes[0].get_element()]}
            if attack.shuffled:
                shuffled_with = attack.shuffle_target.fighter.name + " " + attack.shuffle_target.name
            else:
                shuffled_with = "None"
            attack_dict[attack.name] = {"damage":damage_dict,
                                        "shield":shield_dict,
                                        "angle":angle_dict,
                                        "base":base_dict,
                                        "growth":growth_dict,
                                        "set":set_dict,
                                        "size":size_dict,
                                        "element":element_dict,
                                        "shuffled_with":shuffled_with
                                        }
        for throw in fighter.throws:
            damage_dict = {"original":int(throw.original_stats[0]),"new":throw.get_damage()}
            angle_dict = {"original":int(throw.original_stats[1]),"new":throw.get_angle()}
            base_dict = {"original":int(throw.original_stats[3]),"new":throw.get_base()}
            growth_dict = {"original":int(throw.original_stats[2]),"new":throw.get_growth()}
            set_dict = {"original":int(throw.original_stats[4]),"new":throw.get_set()}
            if throw.get_element() > 4 or throw.original_stats[5] > 4:
                element_dict = {"original":throw_elements[throw.original_stats[5]],"new":"???"}
            else:
                element_dict = {"original":throw_elements[throw.original_stats[5]],"new":throw_elements[throw.get_element()]}
            if throw.shuffled:
                shuffled_with = throw.shuffle_target.fighter.name + " " + throw.shuffle_target.name
            else:
                shuffled_with = "None"
            throw_dict[throw.name] = {"damage":damage_dict,
                                        "angle":angle_dict,
                                        "base":base_dict,
                                        "growth":growth_dict,
                                        "set":set_dict,
                                        "element":element_dict,
                                        "shuffled_with":shuffled_with}
        log[fighter.name] = {"attributes":attribute_dict,"attacks":attack_dict,"throws":throw_dict}
    return log
