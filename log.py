import fighter, json

ELEMENTS = ["Normal", "Fire", "Electric", "Slash", "Coin", "Ice", "Sleep", "Hibernate",
            "??????", "Grounded", "Cape", "Special", "Disable", "Dark", "Screw Attack",
            "Flower", "None"]

def make_log(path, seed):
    log = {}
    for _fighter in fighter.fighters:
        fighter_dict = {}
        attribute_dict = {}
        for attribute in _fighter.attributes:
            this_attribute_dict = {}
            this_attribute_dict["Value"] = round(attribute.value, 4)
            this_attribute_dict["Tags"] = attribute.tags
            attribute_dict[attribute.name] = this_attribute_dict
        subaction_dict = {}
        for subaction in _fighter.subactions:
            this_subaction_dict = {}
            this_subaction_dict["Friendly Name"] = subaction.friendly_name
            this_subaction_dict["Frame Speed Multiplier"] = round(subaction.fsm_multiplier, 4)
            this_subaction_dict["Tags"] = subaction.tags
            hitbox_num = 0
            hitboxes_dict = {}
            for hitbox in subaction.hitboxes:
                hitbox_dict = {}
                hitbox_dict["Damage"] = hitbox.damage
                hitbox_dict["Angle"] = hitbox.angle
                hitbox_dict["Knockback Growth"] = hitbox.growth
                hitbox_dict["Base Knockback"] = hitbox.base
                hitbox_dict["Set Knockback"] = hitbox.setkb
                hitbox_dict["Element"] = ELEMENTS[hitbox.element]
                hitbox_dict["Shield Damage"] = hitbox.shielddamage
                hitbox_dict["SFX"] = hitbox.sfx
                hitbox_dict["Size"] = hitbox.size
                hitbox_dict["Tags"] = hitbox.tags
                hitbox_dict["Power Rating"] = hitbox.power_rating
                hitboxes_dict["hitbox" + str(hitbox_num)] = hitbox_dict
                hitbox_num += 1
            this_subaction_dict["Hitboxes"] = hitboxes_dict
            
            throw_num = 0
            throws_dict = {}
            for throw in subaction.throws:
                throw_dict = {}
                throw_dict["Damage"] = throw.damage
                throw_dict["Angle"] = throw.angle
                throw_dict["Knockback Growth"] = throw.growth
                throw_dict["Base Knockback"] = throw.base
                throw_dict["Set Knockback"] = throw.setkb
                throw_dict["Element"] = throw.element
                throw_dict["Tags"] = throw.tags
                throws_dict["throw" + str(throw_num)] = throw_dict
                throw_num += 1
            this_subaction_dict["Throws"] = throws_dict

            gfx_num = 0
            gfx_dict = {}
            for gfx in subaction.gfx:
                gfx_dict["gfx" + str(gfx_num)] = gfx.id
                gfx_num += 1
            this_subaction_dict["GFX"] = gfx_dict

            sfx_num = 0
            sfx_dict = {}
            for sfx in subaction.sfx:
                sfx_dict["sfx" + str(sfx_num)] = sfx.id
                sfx_num += 1
            this_subaction_dict["SFX"] = sfx_dict

            aura_num = 0
            aura_dict = {}
            for aura in subaction.auras:
                aura_dict["aura" + str(aura_num)] = aura.id
                aura_num += 1
            this_subaction_dict["Auras"] = aura_dict

            subaction_dict[subaction.name.decode("ascii")] = this_subaction_dict


        fighter_dict["Attributes"] = attribute_dict
        fighter_dict["Subactions"] = subaction_dict
        log[_fighter.name] = fighter_dict

    with open(path.replace(".iso", ".json"), "w") as json_file:
        json.dump(log, json_file, indent=4)
    
