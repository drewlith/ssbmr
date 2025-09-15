let flags = [];
let components = [];
let flagset = "";
let flagInput = document.createElement("textarea");
flagInput.classList.add("flagentry");
class Flag {
    constructor(flagName, parameters="", type="int") {
        this.flagName = flagName;
        this.parameters = parameters;
        this.type = type;
        this.active = false;
        flags.push(this);
    }
    getFlag() {
        let flag = "";
        flag += "-" + this.flagName;
        if (this.parameters.length > 0) {
            flag += " "
        }
        for (let i = 0; i < this.parameters.length; i++) {
            if (i != 0) {
                flag += ":"
            }
            flag += this.parameters[i]
        }
        return flag;
    }
    changeParameters(newParams) {
        this.parameters = newParams;
    }

    getIsString() {
        return this.isString;
    }

    getFlagName() {
        return "-" + this.flagName;
    }

    getType() {
        return this.type;
    }

    get enabled() {
        return this.active;
    }

    set enabled(bool) {
        this.active = bool; 
    }

}
class Component {
    constructor(flag, tooltip="", name="") {
        this.flag = flag
        this.div = document.createElement("div");
        this.div.classList.add("component");
        this.div.dataset.tooltip = tooltip;
        this.div.id = this.flag.flagName;
        this.innerDiv2 = document.createElement("div");
        this.innerDiv2.classList.add("innerDivText");
        this.label = document.createElement("p");
        this.label.innerHTML = name;
        this.innerDiv2.appendChild(this.label);
        this.div.appendChild(this.innerDiv2);
        components.push(this);
    }

    getFlag() {
        return this.flag;
    }

    get element() {
        return this.div;
    }
    set element(element) {
        this.div = element;
    }

}

class CheckboxInputComponent extends Component {
    constructor(flag, tooltip="", name="", left="22%") {
        super(flag, tooltip, name);
        this.checkInput = document.createElement("input");
        this.checkInput.type = "checkbox";
        this.checkInput.style = ""
        this.label.style.left = left;
        this.div.appendChild(this.checkInput);
        this.flag.component = this;
        let checkInputVar = this.checkInput;
        checkInputVar.oninput = function() {
            flag.enabled = checkInputVar.checked;
            updateFlags();
        }
    }
    get value() {
        return this.checkInput.checked;
    }
    set value(value) {
        this.flag.enabled = value;
        this.checkInput.checked = value;
        updateFlags();
    }
}

class TextInputComponent extends Component {
    constructor(flag, tooltip="", name="", left="5%") {
        super(flag, tooltip, name);
        this.divInner = document.createElement("div");
        this.divInner.classList.add("innerDiv6");
        this.textInput = document.createElement("input");
        this.textInput.type = "text";
        this.textInput.style = "left:40%;top:35%;height:30px;position: absolute;";
        this.textInput.value = "";
        this.divInner.appendChild(this.textInput);
        let textInputVar = this.textInput;
        textInputVar.oninput = function() {
            flag.changeParameters([textInputVar.value]);
            if (textInputVar.value.length > 0) {
                flag.enabled = true;
            } else {
                flag.enabled = false;
            }
            updateFlags();
        }
        this.label.style.left = left;
        this.div.appendChild(textInputVar);
        this.flag.component = this;
    }
    get value() {
        return this.textInput.value;
    }
    set value(value) {
        this.flag.parameters = [value];
        this.textInput.value = value;
        if (value.length > 0) {
            this.flag.enabled = true;
        } else {
            this.flag.enabled = false;
        }
        updateFlags();
    }
}

class NumberInputComponent extends Component {
    // constructor(flag, tooltip="", name="", left="17%", min="0", max="300", percent=true, fighterFlag=false, float=false, initial=0) {
    constructor(flag, tooltip="", name="", min="0", max="300", percent=true, fighterFlag=false, float=false, initial=0) {
        super(flag, tooltip, name);
        this.divInner = document.createElement("div");
        this.divInner.classList.add("innerDiv");
        this.numInput = document.createElement("input");
        this.numInput.type = "number";
        if (float == true) {
            this.numInput.step = "0.01";
        }
        this.numInput.min = min;
        this.numInput.max = max;
        if (percent) {
            let image = document.createElement("img");
            image.src = "static/percent.png";
            this.div.appendChild(image);
        }
        // this.label.style.left = left;
        this.divInner.appendChild(this.numInput);
        this.div.appendChild(this.divInner);
        this.flag.component = this;
        if (initial > 0) {
            this.numInput.value = initial;
        }
        let numInputVar = this.numInput;
        numInputVar.oninput = function() {
            flag.changeParameters([numInputVar.value]);
            if (fighterFlag) {
                if (numInputVar.value > 0 && numInputVar.value != 100) {
                    flag.enabled = true;
                } else {
                    flag.enabled = false;
                }
            } else {
                if (numInputVar.value > 0 && numInputVar.value != initial) {
                    flag.enabled = true;
                } else {
                    flag.enabled = false;
                }
            }
            updateFlags();
        }
        this.fighterFlag = fighterFlag;
        this.float = float;
        this.initial = initial;
    }
    get value() {
        return this.numInput.value;
    }
    set value(value) {
        this.flag.changeParameters([value]);
        this.numInput.value = value;
        if (this.fighterFlag) {
            if (value > 0 && value != 100) {
                this.flag.enabled = true;
            } else {
                this.flag.enabled = false;
            }
        } 
        else {
            if (value > 0 && value != this.initial) {
                this.flag.enabled = true;
            } else {
                this.flag.enabled = false;
            }
        }
        updateFlags();
    }
}

class DualNumInputComponent extends Component {
   // constructor(flag, tooltip="", name="", left="6%", min="0", max="300") {
    constructor(flag, tooltip="", name="", min="0", max="300") {

        super(flag, tooltip, name);
        this.divInner = document.createElement("div");
        this.divInner.classList.add("innerDiv");
        this.numInputA = document.createElement("input");
        this.numInputA.type = "number";
        this.numInputA.min = min;
        this.numInputA.max = max;
        this.numInputB = document.createElement("input");
        this.numInputB.type = "number";
        this.numInputB.min = min;
        this.numInputB.max = max;
        let percent = document.createElement("img");
        let hyphen = document.createElement("img");
        percent.src = "static/percent.png";
        percent.classList.add("percent");
        hyphen.src = "static/dash.png"
        hyphen.classList.add("dash");
        this.divInner.appendChild(this.numInputA);
        this.divInner.appendChild(hyphen);
        this.divInner.appendChild(this.numInputB);
        this.divInner.appendChild(percent);
        this.div.appendChild(this.divInner);

        this.flag.component = this;
        let numInputAVar = this.numInputA;
        let numInputBVar = this.numInputB;
        numInputAVar.oninput = function() {
            flag.changeParameters([numInputAVar.value, numInputBVar.value]);
            if ((numInputAVar.value > 0 || numInputBVar.value > 0) && (numInputAVar.value != 100 || numInputBVar.value != 100)) {
                flag.enabled = true;
            } else {
                flag.enabled = false;
            }
            if (parseInt(numInputAVar.value) < 0) {
                numInputAVar.value = 0;
            }
            if (!Number.isInteger(parseInt(numInputAVar.value))) {
                numInputAVar.value = 0;
            }
            updateFlags();
        }
        numInputBVar.oninput = function() {
            flag.changeParameters([numInputAVar.value, numInputBVar.value]);
            if ((numInputAVar.value > 0 || numInputBVar.value > 0) && (numInputAVar.value != 100 || numInputBVar.value != 100)) {
                flag.enabled = true;
            } else {
                flag.enabled = false;
            }
            if (parseInt(numInputBVar.value) < 0) {
                numInputBVar.value = 0;
            }
            if (!Number.isInteger(parseInt(numInputBVar.value))) {
                numInputBVar.value = 0;
            }
            updateFlags();
        }
        // this.label.style.left = left;
        this.numInputA.style = "left:50%; top:25%; width:60; height:40; font-size:20";
        this.numInputB.style = "left:72%; top:25%; width:60; height:40; font-size:20";
        percent.style = "left:88%";
        hyphen.style = "left:65.5%;top:40%;height:15;width:25";
    }
    get valueA() {
        return this.numInputA.value;
    }
    set valueA(value) {
        this.flag.changeParameters([value, this.numInputB.value]);
        this.numInputA.value = value;
        if (value > 0 && (value != 100 || this.numInputB.value != 100)) {
            this.flag.enabled = true;
        } else {
            this.flag.enabled = false;
        }
        updateFlags();
    }
    get valueB() {
        return this.numInputB.value;
    }
    set valueB(value) {
        this.flag.changeParameters([this.numInputA.value, value]);
        this.numInputB.value = value;
        if (value > 0 && (value != 100 || this.numInputA.value != 100)) {
            this.flag.enabled = true;
        } else {
            this.flag.enabled = false;
        }
        updateFlags();
    }
}
flagInput.onchange = function() {
    updateComponents();
}

function updateFlags() {
    flagset = "";
    for (let i = 0; i < flags.length; i++) {
        if (flags[i].enabled) {
            flagset += flags[i].getFlag() + " ";
        }
    }
    flagInput.value = flagset;
}

function updateComponents() {
    let newFlags = flagInput.value;
    for (let i = 0; i < components.length; i++) {
        let flag = components[i].getFlag();
        flagType = flag.getType();
        if (newFlags.includes(flag.getFlagName())) { // Flag exists
            if (flagType == "string") {
                parameters = getFlagParameters(newFlags + "-", flag.getFlagName(), true);
                components[i].value = [parameters];
            }  else if (flagType == "bool") {
                components[i].value = true;
            }  else if (flagType == "dual-int") {
                parameters = getFlagParameters(newFlags + "-", flag.getFlagName());
                components[i].valueA = parameters[0];
                components[i].valueB = parameters[1];
            }  else {
                if (components[i].float == true) {
                    parameters = getFlagParameters(newFlags + "-", flag.getFlagName(), false, true);
                } else {
                    parameters = getFlagParameters(newFlags + "-", flag.getFlagName());
                }
                components[i].value = parameters[0];
            }
        } else { // Flag doesn't exist
            if (flagType == "string") {
                components[i].value = "";                                
            } else if(flagType == "bool") {
                components[i].value = false;
            } else if (flagType == "dual-int") {
                components[i].valueA = 100;
                components[i].valueB = 100; 
            }
            else {
                if (components[i].initial > 0) {
                    components[i].value = components[i].initial;
                } 
                else if (components[i].fighterFlag) {
                    components[i].value = 100; 
                } else {
                    components[i].value = 0;   
                }          
            }
        }
    }
}

// Works the same as in util.py.
function getFlagParameters(flags, flagToRead, isString=false, isFloat=false) {
    flags = flags.replace(/\s/g, "");
    flagToRead = flagToRead.replace(/\s/g, "");
    let index = flags.search(flagToRead)
    index += flagToRead.length;
    let string = "";
    if (isString == false) {
        let parameters = [];
        param = ""
        while (true) {
            if (index > flags.length-1) {
                if (isFloat == true) {
                    parameters.push(parseFloat(param));
                } else {
                    parameters.push(parseInt(param));
                }
                break;
            }
            if (flags[index] == "&" || flags[index] == "-") {
                if (isFloat == true) {
                    parameters.push(parseFloat(param));
                } else {
                    parameters.push(parseInt(param));
                }
                break;
            }
            if (flags[index] == ":") {
                if (isFloat == true) {
                    parameters.push(parseFloat(param));
                } else {
                    parameters.push(parseInt(param));
                }
                param = ""
            } else {
                param += flags[index]
            }
            index += 1
        }
        return parameters;
    } else {
        while (true) {
            char = flags[index]
            if (char == "&" || char == "-") {
                break;
            }
            string += char;
            index += 1;
        }
        string = string.replace(" ", "");
        return string;
    }
}
function createHeader(tab, text, autoMargin = false, marginLeft="2%") {
    let h = document.createElement("h3");
    h.innerHTML = text;
    if (autoMargin) {
        h.style.margin = "auto";
        h.style.textAlign = "center";
    } else {
        h.style.marginLeft = marginLeft;
    }
    tab.after(h);
    return h;
}
function createFlag(tab, type, flagName, labelName, tooltip="", left="", min="0", max="300", percent=true, fighterFlag=false, float=false, initial=0) {
    if (type=="string") {
        newFlag = new TextInputComponent(
            new Flag(flagName, "", type),
            tooltip,
            labelName,
            left
        )
    }
    else if (type=="bool") {
        newFlag = new CheckboxInputComponent(
            new Flag(flagName, "", type),
            tooltip,
            labelName
        )
    }
    else if (type=="dual-int") {
        newFlag = new DualNumInputComponent(
            new Flag(flagName, [100,100], type),
            tooltip,
            labelName,
           // left,
            min,
            max
        )
    }
    else if (type=="int") {
        newFlag = new NumberInputComponent(
            new Flag(flagName, [0], type),
            tooltip,
            labelName,
         //   left,
            min,
            max,
            percent,
            fighterFlag,
            float,
            initial
        )
    }
    tab.appendChild(newFlag.element);
    return newFlag;
}

// Main
mainTab = document.getElementById("main-tab");
createFlag(mainTab, "string", "seed", "Seed", 
            "ISOs generated with the same seed/flags will be identical.",
            "5%");
createFlag(mainTab, "bool", "balance", "Balance", 
            "Groups attack into separate tiers before shuffling or applying chaos.");

// Flagset Stuff
flagHeader = createHeader(mainTab, "Flags", false, "10%");
flagHeader.after(flagInput);

// Preset Stuff
let presets = document.createElement("select");
let presetLabel = document.createElement("label");
presetLabel.htmlFor = presets;
presetLabel.style.display = "flex";
presetLabel.style.flexWrap = "wrap";
presetLabel.style.maxWidth = "80%";
presetLabel.style.height = "8%";
presetLabel.style.margin = "auto";
presetLabel.style.background = "00000000";
presets.style.display = "flex";
presets.style.flexWrap = "wrap";
presets.style.marginLeft = "10%";
presets.style.marginTop = "5px";
presets.style.marginBottom = "5px";

presets.oninput = function(e) {
    presetLabel.innerHTML = presets.options[presets.options.selectedIndex].dataset.description;
    flagInput.value = presets.options[presets.options.selectedIndex].dataset.flags;
    updateComponents();
}

function createOption(name, description, flags) {
    let option = document.createElement("option");
    option.innerHTML = name;
    option.value = name;
    option.dataset.description = description;
    option.dataset.flags = flags;
    presets.options.add(option);
}
standardFlags = "-balance -shuffle_attacks 50 -hitbox_angle 20 -hitbox_damage 90:120 -hitbox_growth 90:120 -hitbox_base 90:120 -hitbox_wdsk 80:120 -hitbox_size 100:110 -shuffle_throws 50 -throw_angle 20 -throw_damage 90:120 -throw_growth 90:120 -throw_base 90:120 -throw_wdsk 80:120 -element_percent 10 -element_normal -element_fire -element_electric -element_slash -element_coin -element_cape -element_dark -element_flower -attribute_walk 100:120 -attribute_dash 100:120 -attribute_friction 80:100 -attribute_air 100:120 -attribute_jump 90:110 -attribute_gravity 90:120 -attribute_weight 75:150 -attribute_scale 95:110 -attribute_shield_size 90:110 -attribute_landing_lag 70:100 -chaos_percent 50 -chaos_hitbox_damage 5 -chaos_hitbox_angle -chaos_hitbox_growth 5 -chaos_hitbox_base 5 -chaos_hitbox_wdsk 5 -chaos_hitbox_size 5 -chaos_throw_damage 5 -chaos_throw_angle -chaos_throw_growth 5 -chaos_throw_base 5 -chaos_throw_wdsk 5 -chaos_attribute_walk -chaos_attribute_dash -chaos_attribute_air -chaos_attribute_jump -chaos_attribute_gravity -chaos_attribute_friction -chaos_attribute_weight -chaos_attribute_landing_lag -sound";
tournamentFlags = "-balance -ledge_invincible 20 -shuffle_attacks 25 -hitbox_angle 15 -hitbox_damage 90:120 -hitbox_growth 90:120 -hitbox_base 90:120 -hitbox_wdsk 80:100 -throw_angle 15 -throw_damage 90:120 -throw_growth 90:120 -throw_base 90:120 -throw_wdsk 80:100 -element_percent 10 -element_normal -element_fire -element_electric -element_slash -element_coin -element_dark -attribute_walk 100:120 -attribute_dash 100:120 -attribute_friction 85:100 -attribute_air 100:110 -attribute_jump 90:110 -attribute_gravity 95:110 -attribute_weight 90:120 -attribute_shield_size 100:110 -attribute_landing_lag 70:100";
shuffleFlags = "-balance -shuffle_attacks 100 -shuffle_throws 100";
chaosFlags = "-balance -element_percent 100 -element_normal -element_fire -element_electric -element_slash -element_coin -element_dark -element_flower -chaos_percent 100 -chaos_hitbox_damage 5 -chaos_hitbox_angle -chaos_hitbox_growth 5 -chaos_hitbox_base 5 -chaos_hitbox_wdsk 5 -chaos_hitbox_size 5 -chaos_throw_damage 5 -chaos_throw_angle -chaos_throw_growth 5 -chaos_throw_base 5 -chaos_throw_wdsk 5";
frenchFlags = "-balance -hitbox_angle 15 -hitbox_damage 90:115 -hitbox_growth 90:115 -hitbox_base 90:115 -hitbox_wdsk 90:115 -hitbox_size 90:115 -throw_angle 15 -throw_damage 90:115 -throw_growth 90:115 -throw_base 90:115 -throw_wdsk 90:115 -attribute_walk 90:115 -attribute_dash 90:115 -attribute_friction 90:115 -attribute_air 90:115 -attribute_jump 90:115 -attribute_gravity 90:115 -attribute_weight 90:115 -attribute_scale 90:115 -attribute_shield_size 90:115 -attribute_landing_lag 90:115";
nsixfourFlags = "-balance -hitstun 0.6 -l_cancel_division 3 -shield_stun 4 -hitbox_angle 10 -hitbox_damage 90:115 -hitbox_shield_damage 100:120 -hitbox_growth 80:95 -hitbox_base 100:120 -hitbox_wdsk 80:100 -hitbox_size 100:110 -throw_angle 15 -throw_damage 90:115 -throw_growth 80:95 -throw_base 100:130 -throw_wdsk 80:100 -element_percent 10 -element_normal -element_fire -element_electric -element_slash -element_coin -element_dark -attribute_weight 100:125 -attribute_shield_size 100:120";
lightningFlags = "-balance -l_cancel_division 4 -shield_release 2 -air_dodge_speed 5 -air_dodge_lag 2 -ledge_timeout 15 -ledge_invincible 15 -respawn_timer 30 -shuffle_attacks 50 -hitbox_angle 20 -hitbox_damage 90:120 -hitbox_growth 90:120 -hitbox_base 90:120 -hitbox_wdsk 80:120 -hitbox_size 100:110 -shuffle_throws 50 -throw_angle 20 -throw_damage 90:120 -throw_growth 90:120 -throw_base 90:120 -throw_wdsk 80:120 -element_percent 10 -element_normal -element_fire -element_electric -element_slash -element_coin -element_cape -element_dark -element_flower -attribute_walk 100:150 -attribute_dash 100:150 -attribute_friction 60:100 -attribute_air 100:140 -attribute_jump 100:110 -attribute_gravity 100:150 -attribute_weight 75:120 -attribute_scale 85:105 -attribute_shield_size 90:110 -attribute_landing_lag 50:100 -chaos_percent 50 -chaos_hitbox_damage 5 -chaos_hitbox_angle -chaos_hitbox_growth 5 -chaos_hitbox_base 5 -chaos_hitbox_wdsk 5 -chaos_hitbox_size 5 -chaos_throw_damage 5 -chaos_throw_angle -chaos_throw_growth 5 -chaos_throw_base 5 -chaos_throw_wdsk 5 -fastfall_whenever";
trueShuffleFlags = "-shuffle_attacks 100 -shuffle_throws 100 -shuffle_attributes 100";
trueChaosFlags = "-element_percent 100 -element_normal -element_fire -element_electric -element_slash -element_coin -element_ice -element_sleep -element_ground -element_cape -element_disable -element_dark -element_screw_attack -element_flower -chaos_percent 100 -chaos_hitbox_damage 10 -chaos_hitbox_angle -chaos_hitbox_growth 10 -chaos_hitbox_base 10 -chaos_hitbox_wdsk 10 -chaos_hitbox_size 10 -chaos_throw_damage 10 -chaos_throw_angle -chaos_throw_growth 10 -chaos_throw_base 10 -chaos_throw_wdsk 10 -chaos_attribute_walk -chaos_attribute_dash -chaos_attribute_air -chaos_attribute_jump -chaos_attribute_gravity -chaos_attribute_friction -chaos_attribute_weight -chaos_attribute_landing_lag -sound";
birthdayBoyFlags = "-balance -hitbox_angle 60 -hitbox_damage 60:90 -hitbox_shield_damage 100:200 -hitbox_growth 100:115 -hitbox_base 90:110 -hitbox_wdsk 60:75 -hitbox_size 90:110 -shuffle_throws 25 -throw_angle 45 -throw_damage 40:80 -throw_growth 100:125 -throw_base 100:115 -throw_wdsk 60:80 -element_percent 25 -element_fire -element_electric -element_slash -element_flower -attribute_walk 100:200 -attribute_dash 90:120 -attribute_friction 50:110 -attribute_air 110:175 -attribute_gravity 90:110 -attribute_weight 90:110 -attribute_scale 80:115 -attribute_shield_size 75:125 -attribute_landing_lag 50:75 -chaos_percent 10 -chaos_hitbox_angle -chaos_hitbox_base 3 -chaos_hitbox_size 3 -chaos_throw_angle -chaos_throw_base 3 -chaos_attribute_walk -chaos_attribute_friction -chaos_attribute_weight";
cgFlags = "-balance -shuffle_attacks 25 -hitbox_angle 45 -hitbox_damage 90:110 -hitbox_growth 90:110 -hitbox_base 90:110 -hitbox_wdsk 90:110 -hitbox_size 95:110 -throw_angle 30 -throw_damage 90:110 -throw_growth 90:110 -throw_base 90:110 -throw_wdsk 90:110 -element_percent 10 -element_normal -element_fire -element_electric -element_slash -element_cape -element_dark -element_flower -attribute_walk 100:125 -attribute_dash 100:110 -attribute_friction 90:100 -attribute_air 100:110 -attribute_gravity 95:110 -attribute_weight 90:110 -attribute_scale 90:110 -attribute_shield_size 90:110 -attribute_landing_lag 75:100 -chaos_percent 10 -chaos_hitbox_damage 3 -chaos_hitbox_angle -chaos_hitbox_base 5 -chaos_throw_damage 3 -chaos_throw_angle -chaos_throw_base 5 -chaos_throw_wdsk 5 -chaos_attribute_walk -chaos_attribute_dash -chaos_attribute_weight";
createOption("Standard","A variety of flags providing a well-rounded experience.", standardFlags);
createOption("Tournament","Flags that are designed around competitive play. For tournaments or more serious matches.", tournamentFlags);
createOption("Shuffle", "Attack properties are all shuffled! Jigglypuff's rest could be Ganondorf's Warlock Punch, for example.", shuffleFlags);
createOption("Chaos", "Attacks and attributes are randomized disregarding the original properties! Things could get a bit wild, but should still be somewhat balanced.", chaosFlags);
createOption("French Vanilla", "Attacks and attributes are randomized to be close to their original values. Good for gameplay similar to the original Melee, but with slight twists.", frenchFlags);
createOption("Smash N64", "Light randomization, but certain flags will try to make the game feel closer to the original Super Smash Bros.!", nsixfourFlags);
createOption("Lightning Melee", "Everything is randomized, but the flags chosen will favor increasing speed!", lightningFlags);
createOption("Birthday Boy", "The flags used during the 'BirthdayBoy' Seed of the Week!", birthdayBoyFlags);
createOption("CGAGI 2023", "The flags used during the Conduit Gaming Annual Gold Invitational 2023 tournament!", cgFlags);
createOption("True Shuffle", "Shuffle, but without balancing, so a jab could be an instant KO! Character attributes are also shuffled, so Marth could move like Fox for example!", trueShuffleFlags);
createOption("True Chaos", "The randomizer will make no attempts to balance anything! For rowdy late night sessions.", trueChaosFlags);
presetLabel.innerHTML = presets.options[presets.options.selectedIndex].dataset.description;
mainTab.after(presetLabel);
presetHeader = createHeader(mainTab, "Preset", false, "10%");
presetHeader.after(presets);

// Mechanics
mechTab = document.getElementById("mechanics-tab");
createFlag(mechTab, "int", "knockback", "Knockback X", 
            "Affects the multiplier for the base amount of knockback for all attacks and throws.", 
            "4%", "0.1", "2.8", false, false, true, 1.4);
createFlag(mechTab, "int", "hitstun", "Hitstun X", 
            "Affects the multiplier for the base amount of hitstun for all attacks and throws.", 
            "9%", "0.1", "1", false, false, true, 0.4);
createFlag(mechTab, "int", "hitlag", "Base Hitlag", 
            "Affects the amount of time characters are frozen when a hit is landed.", 
            "7%", "0.1", "20", false, false, true, 3);
createFlag(mechTab, "int", "l_cancel_leniency", "L Cancel Frames", 
            "Amount of frames before landing to press L/R/Z to L cancel.", 
            "-7%", "1", "21", false, false, false, 7);
createFlag(mechTab, "int", "l_cancel_division", "L Cancel Divide", 
            "Animation speed divison upon successful L Cancel.", 
            "-5%", "1", "14", false, false, true, 2);
createFlag(mechTab, "int", "shield_hp", "Shield HP", 
            "Amount of health a player's shield has.", 
            "10%", "1", "120", false, false, true, 60);
createFlag(mechTab, "int", "shield_release", "Shield Release", 
            "Amount of frames until a player can release shield.", 
            "0%", "1", "16", false, false, true, 8);
createFlag(mechTab, "int", "shield_stun", "Shield Stun", 
            "Amount of base shield stun.", 
            "5%", "1", "8", false, false, true, 2);
createFlag(mechTab, "int", "air_dodge_speed", "Air Dodge Speed", 
            "Units of movement when air dodging.", 
            "-8%", "1", "9", false, false, true, 3.1);
createFlag(mechTab, "int", "air_dodge_lag", "Air Dodge Lag", 
            "Amount of frames of lag after landing from an air dodge or wavedash.", 
            "0%", "1", "20", false, false, true, 10);
createFlag(mechTab, "int", "ledge_timeout", "Ledge Time-out", 
            "How many frames after letting go of the ledge before it can be grabbed again.", 
            "-4%", "10", "60", false, false, false, 30);
createFlag(mechTab, "int", "ledge_invincible", "Ledge Invincibility", 
            "How many frames after letting go of the ledge that you are invincible.", 
            "-15%", "1", "60", false, false, false, 30);
createFlag(mechTab, "int", "respawn_timer", "Respawn Timer", 
            "How many frames after dying before you are resurrected.", 
            "-5%", "1", "300", false, false, false, 60);


// Attacks
attackTab = document.getElementById("attack-tab");
hitboxFlags = ["shuffle_attacks", "angle", "damage", "shield_damage", "growth", "base", "wdsk", "size"];
hitboxNames = ["Shuffle", "Angle", "Damage", "Shield Dmg", "KB Growth", "Base KB", "Set KB", "Size"];
hitboxTooltips = [
    "Shuffles attacks to swap all their properties. The chance any attack will be shuffled is specified by the percent inputed.",
    "The angle at which an attack will launch. Angle will be adjusted by a random degrees in either direction based on the value specified.",
    "The amount of percent an attack deals. Percent also affects knockback.",
    "Damage on shields is calculated as normal damage + this value.",
    "Determines how much the knockback of an attack scales to the opponents percent.",
    "Determines a base amount of knockback, independent of other variables this will always be added to the final knockback amount after all other calculations.",
    "Only affects attacks with Set Knockback. This property will make an attack always have the same amount of knockback regardless of percent.",
    "Affects the size of all hitbox bubbles for an attack."
];
hitboxLefts = ["", "", "9%", "2%", "2%", "7%", "11%", "14%"]
for (let i = 0; i < hitboxFlags.length; i++) {
    if (hitboxFlags[i] == "shuffle_attacks") {
        createFlag(attackTab, "int", hitboxFlags[i], hitboxNames[i], hitboxTooltips[i], "12%", "0", "100");
    }
    else if (hitboxFlags[i] == "angle") {
        createFlag(attackTab, "int", "hitbox_" + hitboxFlags[i], hitboxNames[i], hitboxTooltips[i], "14%", "0", "180", false);
    } else {
        createFlag(attackTab, "dual-int", "hitbox_" + hitboxFlags[i], hitboxNames[i], hitboxTooltips[i], hitboxLefts[i], "0", "300");
    }
}

// Throws
throwTab = document.getElementById("throw-tab");
throwFlags = ["shuffle_throws", "angle", "damage", "growth", "base", "wdsk"];
throwNames = ["Shuffle", "Angle", "Damage", "KB Growth", "Base KB", "Set KB"];
throwTooltips = [
    "Shuffles throws to swap all their properties. The chance any throw will be shuffled is specified by the percent inputed.",
    "The angle at which a throw will launch. Angle will be adjusted by a random degrees in either direction based on the value specified.",
    "The amount of percent a throw deals. Percent also affects knockback.",
    "Determines how much the knockback of a throw scales to the opponents percent.",
    "Determines a base amount of knockback, independent of other variables this will always be added to the final knockback amount after all other calculations.",
    "Only affects throws with Set Knockback. This property will make a throw always have the same amount of knockback regardless of percent.",
];
throwLefts = ["", "", "9%", "2%", "8%", "11%"];
for (let i = 0; i < throwFlags.length; i++) {
    if (throwFlags[i] == "shuffle_throws") {
        createFlag(throwTab, "int", throwFlags[i], throwNames[i], throwTooltips[i], "12%", "0", "100");
    }
    else if (throwFlags[i] == "angle") {
        createFlag(throwTab, "int", "throw_" + throwFlags[i], throwNames[i], throwTooltips[i], "14%", "0", "180", false);
    } else {
        createFlag(throwTab, "dual-int", "throw_" + throwFlags[i], throwNames[i], throwTooltips[i], throwLefts[i], "0", "300");
    }
}
// Element
elementTab = document.getElementById("element-tab");
elementFlags = ["element_percent", "normal", "fire", "electric", "slash", "coin", "ice", "sleep", "ground", "cape", "disable", "dark", "screw_attack", "flower"];
elementNames = ["Elements", "Normal", "Fire", "Electric", "Slash", "Coin", "Ice", "Sleep", "Ground", "Cape", "Disable", "Dark", "Screw Attack", "Flower"];
elementTooltips = [
    "Percent chance an attack or throw will have its element changed. Will be randomly chosen from all selected elements.",
    "No additional effects are applied.",
    "Sets the opponent ablaze.",
    "Zaps the target, increasing hitlag.",
    "Clanks with swords, unless its damage far surpasses the opposing attack.",
    "Increases wealth.",
    "Chance to temporarily encase an enemy in ice and preserves their momentum for awhile.",
    "Puts target to sleep. Very unfair.",
    "Target will be smashed through the floor, making them unable to move for awhile.",
    "Turns target around.",
    "Temporarily stuns an opponent. A lot more fair than sleep.",
    "Corrupts the targets soul.",
    "Makes the target do a Screw Attack like Samus. They will be in free fall after.",
    "Adds a poison-like draining effect."
];
for (let i = 0; i < elementFlags.length; i++) {
    if (elementFlags[i] == "element_percent") {
        createFlag(elementTab, "int", elementFlags[i], elementNames[i], elementTooltips[i], "12%", "0", "100");
    } else {
        createFlag(elementTab, "bool", "element_" + elementFlags[i], elementNames[i], elementTooltips[i]);
    }
}
// Attributes
attributeTab = document.getElementById("attribute-tab");
attributeFlags = ["shuffle_attributes", "walk", "dash", "friction", "air", "jump", "gravity", "weight", "scale", "shield_size", "landing_lag"];
attributeNames = ["Shuffle", "Walk", "Dash/Run", "Friction", "Aerial", "Jump", "Gravity", "Weight", "Scale", "Shield Size", "Landing Lag"];
attributeTooltips = [
    "Shuffles all attributes with another fighter's. The chance this will occur is the percent specified.",
    "The speed at which fighters will walk.",
    "The speed at which fighters will dash or run.",
    "Controls wavedash length and jump distance. Lower values will allow a fighter to go farther.",
    "Controls aerial mobility.",
    "Changes jump heights and velocity.",
    "Affects how floaty a fighter is.",
    "Lowers the amount of knockback taken from attacks. Also affects the speed of many throws.",
    "The size of the fighter's model.",
    "The size of a fighter's shield.",
    "The amount of lag when landing after an aerial."
];
attributeLefts = ["", "13%", "8%", "10%", "13%", "12%", "11%", "13%", "12%", "2%", "-1%"]
for (let i = 0; i < attributeFlags.length; i++) {
    if (attributeFlags[i] == "shuffle_attributes") {
        createFlag(attributeTab, "int", attributeFlags[i], attributeNames[i], attributeTooltips[i], "12%", "0", "100");
    }   else {
        createFlag(attributeTab, "dual-int", "attribute_" + attributeFlags[i], attributeNames[i], attributeTooltips[i], attributeLefts[i], "0", "300");
    }
}

// Chaos Percent
chaosTab = document.getElementById("chaos-tab");
chaosTabAttack = document.getElementById("chaos-tab-attack");
createFlag(chaosTab, "int", "chaos_percent", "Chaos", 
"The percent chance a property will have Chaos applied to it.", 
"10%", "0", "100");

// Chaos Attack
createHeader(chaosTab, "Attacks");
chaosHitboxFlags = ["damage", "angle", "growth", "base", "wdsk", "size"];
chaosHitboxNames = ["Damage", "Angle", "KB Growth", "Base KB", "Set KB", "Size"];
chaosHitboxTooltips = [
    "Damage will be replaced with a random value. Increase magnitude to raise the average damage.",
    "Angle will be randomly selected from a group of common angles, but there's also a chance it will be completely random.",
    "Knockback Growth will be replaced with a random value. Increase magnitude to raise the average Knockback Growth.",
    "Base Knockback will be replaced with a random value. Increase magnitude to raise the average base knockback.",
    "Set Knockback will be replaced with a random value, but only for attacks that originally have it.",
    "Hitbox size will be replaced with a random value. Increase magnitude to raise the average hitbox size."
];
chaosHitboxLefts = ["12%", "6%", "7%", "10%", "12%", "13%"]
for (let i = 0; i < chaosHitboxFlags.length; i++) {
    if (chaosHitboxFlags[i] == "angle") {
        createFlag(chaosTabAttack, "bool", "chaos_hitbox_" + chaosHitboxFlags[i], chaosHitboxNames[i], chaosHitboxTooltips[i], chaosHitboxLefts[i]);
    }   else {
        createFlag(chaosTabAttack, "int", "chaos_hitbox_" + chaosHitboxFlags[i], chaosHitboxNames[i], chaosHitboxTooltips[i], chaosHitboxLefts[i], "0", "10", false);
    }
}

// Chaos Throw
chaosTabThrow = document.getElementById("chaos-tab-throw");
createHeader(chaosTabAttack, "Throws");
chaosThrowFlags = ["damage", "angle", "growth", "base", "wdsk"];
chaosThrowNames = ["Damage", "Angle", "KB Growth", "Base KB", "Set KB"];
chaosThrowTooltips = [
    "Damage will be replaced with a random value. Increase magnitude to raise the average damage.",
    "Angle will be randomly selected from a group of common angles, but there's also a chance it will be completely random.",
    "Knockback Growth will be replaced with a random value. Increase magnitude to raise the average Knockback Growth.",
    "Base Knockback will be replaced with a random value. Increase magnitude to raise the average base knockback.",
    "Set Knockback will be replaced with a random value, but only for throws that originally have it.",
];
chaosThrowLefts = ["12%", "6%", "7%", "10%", "12%"]
for (let i = 0; i < chaosThrowFlags.length; i++) {
    if (chaosThrowFlags[i] == "angle") {
        createFlag(chaosTabThrow, "bool", "chaos_throw_" + chaosThrowFlags[i], chaosThrowNames[i], chaosThrowTooltips[i], chaosThrowLefts[i]);
    }   else {
        createFlag(chaosTabThrow, "int", "chaos_throw_" + chaosThrowFlags[i], chaosThrowNames[i], chaosThrowTooltips[i], chaosThrowLefts[i], "0", "10", false);
    }
}

// Chaos Attributes
chaosTabAttribute = document.getElementById("chaos-tab-attribute");
createHeader(chaosTabThrow, "Attributes");
chaosAttributeFlags = ["walk", "dash", "air", "jump", "gravity", "friction", "weight", "landing_lag"];
chaosAttributeNames = ["Walk", "Dash/Run", "Aerial", "Jump", "Gravity", "Friction", "Weight", "Landing Lag"];
for (let i = 0; i < chaosAttributeFlags.length; i++) {
    createFlag(chaosTabAttribute, "bool", "chaos_attribute_" + chaosAttributeFlags[i], chaosAttributeNames[i], "Values will be randomly chosen from a range between the highest and lowest of all fighters' original values.");
}

// Fighter
hitboxComponentArrays = [];
throwComponentArrays = [];
attributeComponentArrays = [];
specialComponentArrays = [];
fighters = ["bowser", "captain_falcon", "dk", "dr_mario", "falco", "fox", "game_and_watch", "ganondorf", "popo", "nana", "jigglypuff",
"kirby", "link", "luigi", "mario", "marth", "mewtwo", "ness", "peach", "pichu", "pikachu", "roy", "samus",
"sheik", "yoshi", "young_link", "zelda", "boy", "girl", "giga_koopa", "master_hand", "crazy_hand"];
fighterNames = ["Bowser", "Captain Falcon", "Donkey Kong", "Dr Mario","Falco", "Fox", "Mr. Game & Watch", "Ganondorf", "Popo",
"Nana", "Jigglypuff", "Kirby", "Link", "Luigi", "Mario","Marth", "Mewtwo", "Ness", "Peach", "Pichu", "Pikachu",
"Roy", "Samus", "Sheik", "Yoshi", "Young Link", "Zelda", "Boy", "Girl", "Giga Koopa", "Master Hand", "Crazy Hand"];
fighterSelectObj = document.getElementById("fighter-select-tab");
createHeader(fighterSelectObj, "Attacks");
fighterTabAttacks = document.getElementById("fighter-tab-attack");
createHeader(fighterTabAttacks, "Throws");
fighterHitboxFlags = ["damage", "shield_damage", "base", "growth", "wdsk", "size"];
fighterHitboxNames = ["Damage", "Shield Dmg", "Base KB", "KB Growth", "Set KB", "Size"];
fighterHitboxLefts = ["6%", "6%", "6%", "6%", "6%", "6%"];
fighterTabThrows = document.getElementById("fighter-tab-throw");
createHeader(fighterTabThrows, "Attributes");
fighterThrowFlags = ["damage", "base", "growth", "wdsk"];
fighterThrowNames = ["Damage", "Base KB", "KB Growth", "Set KB"];
fighterThrowLefts = ["6%", "6%", "6%", "6%"];
fighterTabAttributes = document.getElementById("fighter-tab-attribute");
createHeader(fighterTabAttributes, "Special");
fighterAttributeFlags = ["walk", "dash", "friction", "air", "jump", "gravity", "weight", "scale", "shield_size", "landing_lag"];
fighterAttributeNames = ["Walk", "Dash", "Friction", "Aerial", "Jump", "Gravity", "Weight", "Scale", "Shield Size", "Landing Lag"];
fighterAttributeLefts = ["6%", "6%", "6%", "6%", "6%", "6%", "6%", "6%", "6%", "2%"]

for (let k = 0; k < fighters.length; k++) {
    hitboxes = [];
    throws = [];
    attributes = [];
    for (let i = 0; i < fighterHitboxFlags.length; i++) {
        hitboxes.push(createFlag(fighterTabAttacks, "int", fighters[k] + "_hitbox_" + fighterHitboxFlags[i], fighterHitboxNames[i], 
        "Values will be multiplied by the percent specified.",
        fighterHitboxLefts[i], "0", "300", true, true));
    }
    for (let i = 0; i < fighterThrowFlags.length; i++) {
        throws.push(createFlag(fighterTabThrows, "int", fighters[k] + "_throw_" + fighterThrowFlags[i], fighterThrowNames[i], 
        "Values will be multiplied by the percent specified.",
        fighterThrowLefts[i], "0", "300", true, true));
    }
    for (let i = 0; i < fighterAttributeFlags.length; i++) {
        attributes.push(createFlag(fighterTabAttributes, "int", fighters[k] + "_attribute_" + fighterAttributeFlags[i], fighterAttributeNames[i], 
        "Values will be multiplied by the percent specified.",
        fighterAttributeLefts[i], "0", "300", true, true));
    }
    hitboxComponentArrays.push(hitboxes);
    throwComponentArrays.push(throws);
    attributeComponentArrays.push(attributes);
}
// Special Attributes
fighterTabSpecial = document.getElementById("fighter-tab-special");
bowserSpecial = []
bowserSpecial.push(createFlag(fighterTabSpecial, "dual-int", "bowser_flames", "Flames", 
"Controls recharge rate, amount of fuel, flame velocity, X/Y offset, and scale.",
"6%", "0", "300"));
bowserSpecial.push(createFlag(fighterTabSpecial, "dual-int", "koopa_klaw", "Koopa Klaw", 
"Controls bite damage and grab duration.",
"6%", "0", "300"));
bowserSpecial.push(createFlag(fighterTabSpecial, "dual-int", "whirling_fortress", "Whirling Fortress", 
"Controls movement.",
"6%", "0", "300"));
bowserSpecial.push(createFlag(fighterTabSpecial, "dual-int", "bowser_bomb", "Bowser Bomb", 
"Controls horizontal momentum and velocity.",
"6%", "0", "300"));
specialComponentArrays.push(bowserSpecial);
falconSpecial = []
falconSpecial.push(createFlag(fighterTabSpecial, "dual-int", "falcon_punch", "Falcon Punch", 
"Controls horizontal and vertical momentum.",
"6%", "0", "300"));
falconSpecial.push(createFlag(fighterTabSpecial, "dual-int", "raptor_boost", "Raptor Boost", 
"Controls gravity on hit and on whiff.",
"6%", "0", "300"));
falconSpecial.push(createFlag(fighterTabSpecial, "dual-int", "falcon_dive", "Falcon Dive", 
"Controls landing lag, friction, and horizontal momentum.",
"6%", "0", "300"));
falconSpecial.push(createFlag(fighterTabSpecial, "dual-int", "falcon_kick", "Falcon Kick", 
"Controls landing lag, traction, and speed modifier on hit.",
"6%", "0", "300"));
specialComponentArrays.push(falconSpecial);
function turnOnFighterComponent(index) {
    for (let i = 0; i < hitboxComponentArrays[index].length; i++) {
        hitboxComponentArrays[index][i].element.style.display = "block";
    }
    for (let i = 0; i < throwComponentArrays[index].length; i++) {
        throwComponentArrays[index][i].element.style.display = "block";
    }
    for (let i = 0; i < attributeComponentArrays[index].length; i++) {
        attributeComponentArrays[index][i].element.style.display = "block";
    }
    for (let i = 0; i < specialComponentArrays[index].length; i++) {
        specialComponentArrays[index][i].element.style.display = "block";
    }
}

function turnOffAllFighterComponents() {
    for (let i = 0; i < hitboxComponentArrays.length; i++) {
        for (let k = 0; k < hitboxComponentArrays[i].length; k++) {
            hitboxComponentArrays[i][k].element.style.display = "none";
        }
    }
    for (let i = 0; i < throwComponentArrays.length; i++) {
        for (let k = 0; k < throwComponentArrays[i].length; k++) {
            throwComponentArrays[i][k].element.style.display = "none";
        }
    }
    for (let i = 0; i < attributeComponentArrays.length; i++) {
        for (let k = 0; k < attributeComponentArrays[i].length; k++) {
            attributeComponentArrays[i][k].element.style.display = "none";
        }
    }
    for (let i = 0; i < specialComponentArrays.length; i++) {
        for (let k = 0; k < specialComponentArrays[i].length; k++) {
            specialComponentArrays[i][k].element.style.display = "none";
        }
    }
}

// Gecko
geckoTab = document.getElementById("gecko-tab");
createFlag(geckoTab, "bool", "all_characters_float", "Everyone Floats", 
        "Credit: UnclePunch. Same mechanics as Peach.");
createFlag(geckoTab, "bool", "fastfall_whenever", "Fastfall Whenever", 
        "Credit: UnclePunch.");
createFlag(geckoTab, "bool", "paper_mode", "Paper Mode", 
        "Credit: DRGN. Characters will be 2D like Game & Watch. (No Z-Axis)");
createFlag(geckoTab, "bool", "airdodge_catch", "Airdodge Catch", 
        "Credit: UnclePunch. Air dodge into an item in mid air to catch it.");
createFlag(geckoTab, "bool", "air_grabs", "Air Grabs", 
        "Credit: UnclePunch. Enables grabbing in the air.");
createFlag(geckoTab, "bool", "auto_lcancel", "Auto L-Cancel", 
        "Credit: Dan Salvato. No need to L Cancel.");
createFlag(geckoTab, "bool", "b_reverse", "B Reverse", 
        "Credit: UnclePunch. Adds a Brawl style B Reverse.");
createFlag(geckoTab, "bool", "flame_cancel", "Flame Cancel", 
        "Credit: Achilles. Gives Bowser back his flame cancel from v1.00.");
createFlag(geckoTab, "bool", "brawl_airdodge", "Brawl Airdodge", 
        "Credit: UnclePunch. Use L to Brawl airdodge, or R to Melee airdodge.");
createFlag(geckoTab, "bool", "all_walljump", "All Walljump", 
        "Credit: Achilles, Geuse. Allows any Character to wall jump.");
createFlag(geckoTab, "bool", "meteors_spike", "Meteors Spike", 
        "Credit: flieskiller, Geuse. Meteor cancel is disabled.");
createFlag(geckoTab, "bool", "no_shield", "No Shield", 
        "Credit: Achilles1515. Shielding is disabled.");
createFlag(geckoTab, "bool", "perfect_shield", "Perfect Shield", 
        "Credit: UnclePunch. Adds Ultimate style Perfect Shield.");
createFlag(geckoTab, "bool", "reverse_aerial_rush", "Rev. Aerial Rush", 
        "Credit: MagicScrumpy. Adds a brawl style Reverse Aerial Rush mechanic.");
createFlag(geckoTab, "bool", "shadow_mode", "Shadow Mode", 
        "All characters become blacker than a moonless night.");
// Secret
secretTab = document.getElementById("secret-tab");
createFlag(secretTab, "bool", "sound", "SFX", 
        "Characters will make different sounds for each action, with balancing.");
createFlag(secretTab, "bool", "up_launchers", "Launchers", 
        "Up tilts and Up smashes become universal combo starters, besides Ganondorfs.");
createFlag(secretTab, "bool", "super_punch", "Super Punch", 
        "DK charges his punch very quickly and gets extra momentum on the ground.");
// Selector Event
fighterSelect = document.getElementById("fighter-select");
fighterSelect.onchange = function() {
    turnOffAllFighterComponents();
    turnOnFighterComponent(fighterSelect.selectedIndex);
};
turnOffAllFighterComponents();
turnOnFighterComponent(0);
flagInput.value = "-balance -knockback 1.4 -shuffle_attacks 50 -hitbox_angle 20 -hitbox_damage 90:120 -hitbox_growth 90:120 -hitbox_base 90:120 -hitbox_wdsk 80:120 -hitbox_size 100:110 -shuffle_throws 50 -throw_angle 20 -throw_damage 90:120 -throw_growth 90:120 -throw_base 90:120 -throw_wdsk 80:120 -element_percent 10 -element_normal -element_fire -element_electric -element_slash -element_coin -element_cape -element_dark -element_flower -attribute_walk 100:120 -attribute_dash 100:120 -attribute_friction 80:100 -attribute_air 100:120 -attribute_jump 90:110 -attribute_gravity 90:120 -attribute_weight 75:150 -attribute_scale 95:110 -attribute_shield_size 90:110 -attribute_landing_lag 70:100 -chaos_percent 50 -chaos_hitbox_damage 5 -chaos_hitbox_angle -chaos_hitbox_growth 5 -chaos_hitbox_base 5 -chaos_hitbox_wdsk 5 -chaos_hitbox_size 5 -chaos_throw_damage 5 -chaos_throw_angle -chaos_throw_growth 5 -chaos_throw_base 5 -chaos_throw_wdsk 5 -chaos_attribute_walk -chaos_attribute_dash -chaos_attribute_air -chaos_attribute_jump -chaos_attribute_gravity -chaos_attribute_friction -chaos_attribute_weight -chaos_attribute_landing_lag -sound"
updateComponents();
function uploadFlags() { // When Generate button is clicked.
    message = document.getElementById("generating-message");
    message.style.display = "block";
    flagElement = document.getElementById("flags");
    flagElement.value = flagInput.value;
}


// All this was mostly made by ChatGPT

const shrinks = document.querySelectorAll('.innerDivText');

function shrinkText() {
  shrinks.forEach((shrink) => {
    const text = shrink.querySelector('p');
    // const maxWidth = shrink.offsetWidth;
    const maxWidth = 150; // Hard coded max width since I couldn't get it to pull dynamically
    let currentFontSize = parseInt(getComputedStyle(text).getPropertyValue('font-size'));
    // create a temporary element to calculate the text width without truncating it
    const temp = document.createElement('div');
    temp.style.fontSize = `${currentFontSize}px`;
    temp.style.visibility = 'hidden';
    temp.style.position = 'absolute';
    temp.style.top = '0';
    temp.style.left = '0';
    temp.textContent = text.textContent;
    document.body.appendChild(temp);
    let textWidth = temp.offsetWidth;
    document.body.removeChild(temp);
    while (textWidth > maxWidth && currentFontSize > 8) {
      currentFontSize -= 2; // decrease the font size by 2px
      text.style.fontSize = `${currentFontSize}px`;
      // create a new temporary element with the new font size to recalculate the text width
      const newTemp = document.createElement('div');
      newTemp.style.fontSize = `${currentFontSize}px`;
      newTemp.style.visibility = 'hidden';
      newTemp.style.position = 'absolute';
      newTemp.style.top = '0';
      newTemp.style.left = '0';
      newTemp.textContent = text.textContent;
      document.body.appendChild(newTemp);
      const newWidth = newTemp.offsetWidth;
      document.body.removeChild(newTemp);

      if (newWidth <= maxWidth) {
        textWidth = newWidth;
      }
    }
  });
}

window.addEventListener('load', shrinkText);
window.addEventListener('resize', shrinkText);
