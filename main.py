import iso, fighter
from fighters import captain_falcon
from structs import hitbox, subaction

flags = "&shuffle 1"
#hitbox.simple(flags)
falcon = fighter.get_fighter("Captain Falcon")
subaction.shuffle_subactions(falcon.subactions[69], falcon.subactions[70])
fighter.write_fighter_data()
iso.build_iso()
