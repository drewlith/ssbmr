def add_extra_credit(log, key, content):
    log[key] = content

def create_credits():
    credit_dict = {}
    drewlith_socials = {"twitter":"https://twitter.com/drewlith",
                        "twitch":"https://twitch.tv/drewlith"}
    conduit_socials = {"twitter":"https://twitter.com/Conduit_Gaming",
                       "twitch":"https://www.twitch.tv/cg_conduitgaming"}
    creestab_socials = {"twitter":"https://twitter.com/Creestab"}
    ploaj_socials = {"github":"https://github.com/Ploaj"}
    # Main Developers
    credit_dict["drewlith"] = {"socials": drewlith_socials,
                               "contributions": "SSBM Randomizer v0.4 Creator, Programmer"}
    # E Sports Partners
    credit_dict["Conduit Gaming"] = {"socials": conduit_socials,
                                     "contributions": "Seed of the Week NA"}
    # Development Helpers
    credit_dict["kielbasiago"] = {"socials": "N/A",
                                  "contributions": "Website/Xdelta help"}
    # Moderators
    credit_dict["Moz"] = {"socials": "N/A",
                            "contributions": "Discord Moderator, development helper."}
    credit_dict["Erk"] = {"socials": "N/A",
                            "contributions": "Discord Moderator, new content testing."}
    credit_dict["Creestab"] = {"socials": "N/A",
                            "contributions": "Discord Moderator, Seed of the Week NA."}
    credit_dict["AB"] = {"socials": "N/A",
                            "contributions": "Discord Moderator, Website/Dev Help."}
    credit_dict["Pelipper"] = {"socials": "N/A",
                            "contributions": "Discord Moderator, Content Creation/Dev Help."}
    # GitHub Projects Referenced
    credit_dict["kotcrab"] = {"socials": "N/A",
                            "contributions": "xdelta-wasm: https://github.com/kotcrab/xdelta-wasm"}
    credit_dict["pfirsich"] = {"socials": "N/A",
                            "contributions": "meleeDat2Json: https://github.com/pfirsich/meleeDat2Json/blob/master/meleedat2json/events.py"}
    # Special Thanks
    credit_dict["Ploaj"] = {"socials": ploaj_socials,
                            "contributions": "Music help"}
    credit_dict["DRGN"] = {"socials": "N/A",
                            "contributions": "FST/gecko help"}
    credit_dict["VetriTheRetri"] = {"socials": "N/A",
                            "contributions": "gecko code help"}
    credit_dict["ribbanya"] = {"socials": "N/A",
                            "contributions": "gecko code help"}
    return credit_dict
