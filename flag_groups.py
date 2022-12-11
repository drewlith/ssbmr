from util import get_flag_params
def decode(flags):
    def replace_flags(group_name, flags, tuples):
        if group_name not in flags:
            return flags
        percent = get_flag_params(flags, group_name, True)
        percent_before_change = percent
        percent = percent.replace("%", "")
            
        new_flags = ""
        for i in range(len(tuples)):
            if tuples[i][0] not in flags: # Allow overriding
                new_flags += tuples[i][0] + percent + tuples[i][1]
        flags = flags.replace(group_name+percent_before_change, new_flags)
        return flags

    flags = replace_flags("&deviate_hitboxes", flags,
                    [("-deviate_hitbox_damage", ".5"),
                    ("-deviate_hitbox_angle", ".5"),
                    ("-deviate_hitbox_base", ".5"),
                    ("-deviate_hitbox_growth", ".5"),
                    ("-deviate_hitbox_wdsk", ".5"),
                    ("-deviate_hitbox_size", ".5")])
    
    flags = replace_flags("&deviate_throws", flags,
                    [("-deviate_throw_damage", ".5"),
                    ("-deviate_throw_angle", ".15"),
                    ("-deviate_throw_base", ".5"),
                    ("-deviate_throw_growth", ".5"),
                    ("-deviate_throw_wdsk", ".5")])
    
    flags = replace_flags("&deviate_attributes", flags,
                    [("-deviate_walk", ".15.0"),
                    ("-deviate_dash", ".15.0"),
                    ("-deviate_air", ".15.0"),
                    ("-deviate_jump", ".15.0"),
                    ("-deviate_gravity", ".15.0"),
                    ("-deviate_weight", ".15.0"),
                    ("-deviate_scale", ".15.0"),
                    ("-deviate_shield", ".15.0"),
                    ("-deviate_landing_lag", ".15.0")])
    
    return flags
        
