// Flags
disableTabs = false;
function enableInput(activator, activated) {
    activator.addEventListener("change", function() {
        if (activator.checked == true) {
            activated.disabled = false;
        } else {
            activated.disabled = true;
        }
    });
}
enableInput(document.getElementById("damage-check-input"), document.getElementById("chaos-damage-input"));
enableInput(document.getElementById("base-check-input"), document.getElementById("chaos-base-input"));
enableInput(document.getElementById("growth-check-input"), document.getElementById("chaos-growth-input"));
enableInput(document.getElementById("set-check-input"), document.getElementById("chaos-set-input"));
enableInput(document.getElementById("size-check-input"), document.getElementById("chaos-size-input"));
enableInput(document.getElementById("throw-damage-check-input"), document.getElementById("chaos-throw-damage-input"));
enableInput(document.getElementById("throw-base-check-input"), document.getElementById("chaos-throw-base-input"));
enableInput(document.getElementById("throw-growth-check-input"), document.getElementById("chaos-throw-growth-input"));
enableInput(document.getElementById("throw-set-check-input"), document.getElementById("chaos-throw-set-input"));
function getFlags() {
    disableTabs = true;
    document.getElementById("generating-message").style.display = "block";
    allInput = document.getElementsByTagName("input");
    for (let i = 0; i < allInput.length; i++) {
        if (allInput[i].id != "button-submit") {
            allInput[i].disabled = true;
        }
    }
    flagObj = document.getElementById("flags");
    var flags = "";
    // Seed
    value = document.getElementById("seed-input").value;
    if (value.length > 0) {
        flags += "-seed " + value;
    }
    // Balance
    value = document.getElementById("balance-input").checked;
    if (value == true) {
        flags += " -balance";
    }
    // Shuffle Attacks
    value = document.getElementById("shuffle-attack-input").value;
    if (value > 0) {
        flags += " -shuffle_attacks " + value;
    }
    // Angle
    value = document.getElementById("angle-input").value;
    if (value > 0) {
        flags += " -hitbox_angle " + value;
    }
    // Damage
    minValue = document.getElementById("damage-input-min").value;
    maxValue = document.getElementById("damage-input-max").value;
    if (!(minValue == 100 && maxValue == 100)) {
        flags += " -hitbox_damage " + minValue + "." + maxValue;
    }
    // Shield Damage
    minValue = document.getElementById("shield-input-min").value;
    maxValue = document.getElementById("shield-input-max").value;
    if (!(minValue == 100 && maxValue == 100)) {
        flags += " -hitbox_shield_damage " + minValue + "." + maxValue;
    }
    // Knockback Growth
    minValue = document.getElementById("kbg-input-min").value;
    maxValue = document.getElementById("kbg-input-max").value;
    if (!(minValue == 100 && maxValue == 100)) {
        flags += " -hitbox_growth " + minValue + "." + maxValue;
    }
    // Base KB
    minValue = document.getElementById("base-input-min").value;
    maxValue = document.getElementById("base-input-max").value;
    if (!(minValue == 100 && maxValue == 100)) {
        flags += " -hitbox_base " + minValue + "." + maxValue;
    }
    // Set KB
    minValue = document.getElementById("set-input-min").value;
    maxValue = document.getElementById("set-input-max").value;
    if (!(minValue == 100 && maxValue == 100)) {
        flags += " -hitbox_wdsk " + minValue + "." + maxValue;
    }
    // Size
    minValue = document.getElementById("size-input-min").value;
    maxValue = document.getElementById("size-input-max").value;
    if (!(minValue == 100 && maxValue == 100)) {
        flags += " -hitbox_size " + minValue + "." + maxValue;
    }
    // Shuffle Throws
    value = document.getElementById("shuffle-throw-input").value;
    if (value > 0) {
        flags += " -shuffle_throws " + value;
    }
    // Throw Angle
    value = document.getElementById("throw-angle-input").value;
    if (value > 0) {
        flags += " -throw_angle " + value;
    }
    // Throw Damage
    minValue = document.getElementById("throw-damage-input-min").value;
    maxValue = document.getElementById("throw-damage-input-max").value;
    if (!(minValue == 100 && maxValue == 100)) {
        flags += " -throw_damage " + minValue + "." + maxValue;
    }
    // Throw KB Growth
    minValue = document.getElementById("throw-kbg-input-min").value;
    maxValue = document.getElementById("throw-kbg-input-max").value;
    if (!(minValue == 100 && maxValue == 100)) {
        flags += " -throw_growth " + minValue + "." + maxValue;
    }
    // Throw Base KB
    minValue = document.getElementById("throw-base-input-min").value;
    maxValue = document.getElementById("throw-base-input-max").value;
    if (!(minValue == 100 && maxValue == 100)) {
        flags += " -throw_base " + minValue + "." + maxValue;
    }
    // Throw Set KB
    minValue = document.getElementById("throw-set-input-min").value;
    maxValue = document.getElementById("throw-set-input-max").value;
    if (!(minValue == 100 && maxValue == 100)) {
        flags += " -throw_wdsk " + minValue + "." + maxValue;
    }
    // Shuffle Attributes
    value = document.getElementById("shuffle-attribute-input").value;
    if (value > 0) {
        flags += " -shuffle_attributes " + value;
    }
    // Walk
    minValue = document.getElementById("walk-input-min").value;
    maxValue = document.getElementById("walk-input-max").value;
    if (!(minValue == 100 && maxValue == 100)) {
        flags += " -walk " + minValue + "." + maxValue;
    }
    // Dash/Run
    minValue = document.getElementById("dash-input-min").value;
    maxValue = document.getElementById("dash-input-max").value;
    if (!(minValue == 100 && maxValue == 100)) {
        flags += " -dash " + minValue + "." + maxValue;
    }
    // Friction
    minValue = document.getElementById("friction-input-min").value;
    maxValue = document.getElementById("friction-input-max").value;
    if (!(minValue == 100 && maxValue == 100)) {
        flags += " -friction " + minValue + "." + maxValue;
    }
    // Air
    minValue = document.getElementById("air-input-min").value;
    maxValue = document.getElementById("air-input-max").value;
    if (!(minValue == 100 && maxValue == 100)) {
        flags += " -air " + minValue + "." + maxValue;
    }
    // Jump
    minValue = document.getElementById("jump-input-min").value;
    maxValue = document.getElementById("jump-input-max").value;
    if (!(minValue == 100 && maxValue == 100)) {
        flags += " -jump " + minValue + "." + maxValue;
    }
    // Gravity
    minValue = document.getElementById("gravity-input-min").value;
    maxValue = document.getElementById("gravity-input-max").value;
    if (!(minValue == 100 && maxValue == 100)) {
        flags += " -gravity " + minValue + "." + maxValue;
    }
    // Weight
    minValue = document.getElementById("weight-input-min").value;
    maxValue = document.getElementById("weight-input-max").value;
    if (!(minValue == 100 && maxValue == 100)) {
        flags += " -weight " + minValue + "." + maxValue;
    }
    // Scale
    minValue = document.getElementById("scale-input-min").value;
    maxValue = document.getElementById("scale-input-max").value;
    if (!(minValue == 100 && maxValue == 100)) {
        flags += " -scale " + minValue + "." + maxValue;
    }
    // Shield Size
    minValue = document.getElementById("shieldsize-input-min").value;
    maxValue = document.getElementById("shieldsize-input-max").value;
    if (!(minValue == 100 && maxValue == 100)) {
        flags += " -shield_size " + minValue + "." + maxValue;
    }
    // Landing Lag
    minValue = document.getElementById("landing-input-min").value;
    maxValue = document.getElementById("landing-input-max").value;
    if (!(minValue == 100 && maxValue == 100)) {
        flags += " -landing_lag " + minValue + "." + maxValue;
    }
    // Chaos Percent
    obj = document.getElementById("chaos-percent-input");
    if (obj.value > 0) {
        flags += " -chaos_percent " + obj.value;
    }

    // Chaos Angle
    if (document.getElementById("angle-check-input").checked == true) {
        flags += " -chaos_hitbox_angle";
    }
    // Chaos Damage
    if (document.getElementById("damage-check-input").checked == true) {
        value = document.getElementById("chaos-damage-input").value;
        flags += " -chaos_hitbox_damage " + value;
    }
    // Chaos Base
    if (document.getElementById("base-check-input").checked == true) {
        value = document.getElementById("chaos-base-input").value;
        flags += " -chaos_hitbox_base " + value;
    }
    // Chaos Growth
    if (document.getElementById("growth-check-input").checked == true) {
        value = document.getElementById("chaos-growth-input").value;
        flags += " -chaos_hitbox_growth " + value;
    }
    // Chaos Set
    if (document.getElementById("set-check-input").checked == true) {
        value = document.getElementById("chaos-set-input").value;
        flags += " -chaos_hitbox_wdsk " + value;
    }
    // Chaos Size
    if (document.getElementById("size-check-input").checked == true) {
        value = document.getElementById("chaos-size-input").value;
        flags += " -chaos_hitbox_size " + value;
    }
    // Chaos Throw Angle
    if (document.getElementById("throw-angle-check-input").checked == true) {
        flags += " -chaos_throw_angle";
    }
    // Chaos Throw Damage
    if (document.getElementById("throw-damage-check-input").checked == true) {
        value = document.getElementById("chaos-throw-damage-input").value;
        flags += " -chaos_throw_damage " + value;
    }
    // Chaos Throw Base
    if (document.getElementById("throw-base-check-input").checked == true) {
        value = document.getElementById("chaos-throw-base-input").value;
        flags += " -chaos_throw_base " + value;
    }
    // Chaos Throw Growth
    if (document.getElementById("throw-growth-check-input").checked == true) {
        value = document.getElementById("chaos-throw-growth-input").value;
        flags += " -chaos_throw_growth " + value;
    }
    // Chaos Throw Set
    if (document.getElementById("throw-set-check-input").checked == true) {
        value = document.getElementById("chaos-throw-set-input").value;
        flags += " -chaos_throw_wdsk " + value;
    }
    // Chaos Walk
    if (document.getElementById("walk-check-input").checked == true) {
        flags += " -chaos_walk";
    }
    // Chaos Dash
    if (document.getElementById("dash-check-input").checked == true) {
        flags += " -chaos_dash";
    }
    // Chaos Friction
    if (document.getElementById("friction-check-input").checked == true) {
        flags += " -chaos_friction";
    }
    // Chaos Air
    if (document.getElementById("air-check-input").checked == true) {
        flags += " -chaos_air";
    }
    // Chaos Jump
    if (document.getElementById("jump-check-input").checked == true) {
        flags += " -chaos_jump";
    }
    // Chaos Gravity
    if (document.getElementById("gravity-check-input").checked == true) {
        flags += " -chaos_gravity";
    }
    // Chaos Weight
    if (document.getElementById("weight-check-input").checked == true) {
        flags += " -chaos_weight";
    }
    // Chaos Landing Lag
    if (document.getElementById("landing-check-input").checked == true) {
        flags += " -chaos_landing_lag";
    }
    // Adjust Fighters
    fighterNames = ["bowser", "captain_falcon", "dk", "dr_mario", "falco", "fox",
        "game_and_watch", "ganondorf", "popo", "nana", "jigglypuff",
        "kirby", "link", "luigi", "mario", "marth", "mewtwo",
        "ness", "peach", "pichu", "pikachu", "roy", "samus",
        "sheik", "yoshi", "young_link", "zelda", "boy", "girl",
        "giga_koopa", "master_hand", "crazy_hand"];
    for (let i = 0; i < fighterNames.length; i++) {
        if (fighters[fighterNames[i]][0] != 0 && fighters[fighterNames[i]][0] != 100) {
            flags += " -" + fighterNames[i] + "_hitbox_damage " + fighters[fighterNames[i]][0];
        }
        if (fighters[fighterNames[i]][1] != 0 && fighters[fighterNames[i]][1] != 100) {
            flags += " -" + fighterNames[i] + "_hitbox_base " + fighters[fighterNames[i]][1];
        }
        if (fighters[fighterNames[i]][2] != 0 && fighters[fighterNames[i]][2] != 100) {
            flags += " -" + fighterNames[i] + "_hitbox_growth " + fighters[fighterNames[i]][2];
        }
        if (fighters[fighterNames[i]][3] != 0 && fighters[fighterNames[i]][3] != 100) {
            flags += " -" + fighterNames[i] + "_hitbox_wdsk " + fighters[fighterNames[i]][3];
        }
        if (fighters[fighterNames[i]][4] != 0 && fighters[fighterNames[i]][4] != 100) {
            flags += " -" + fighterNames[i] + "_hitbox_size " + fighters[fighterNames[i]][4];
        }
        if (fighters[fighterNames[i]][5] != 0 && fighters[fighterNames[i]][5] != 100) {
            flags += " -" + fighterNames[i] + "_throw_damage " + fighters[fighterNames[i]][5];
        }
        if (fighters[fighterNames[i]][6] != 0 && fighters[fighterNames[i]][6] != 100) {
            flags += " -" + fighterNames[i] + "_throw_base " + fighters[fighterNames[i]][6];
        }
        if (fighters[fighterNames[i]][7] != 0 && fighters[fighterNames[i]][7] != 100) {
            flags += " -" + fighterNames[i] + "_throw_growth " + fighters[fighterNames[i]][7];
        }
        if (fighters[fighterNames[i]][8] != 0 && fighters[fighterNames[i]][8] != 100) {
            flags += " -" + fighterNames[i] + "_throw_wdsk " + fighters[fighterNames[i]][8];
        }
        if (fighters[fighterNames[i]][9] != 0 && fighters[fighterNames[i]][9] != 100) {
            flags += " -" + fighterNames[i] + "_walk " + fighters[fighterNames[i]][9];
        }
        if (fighters[fighterNames[i]][10] != 0 && fighters[fighterNames[i]][10] != 100) {
            flags += " -" + fighterNames[i] + "_dash " + fighters[fighterNames[i]][10];
        }
        if (fighters[fighterNames[i]][11] != 0 && fighters[fighterNames[i]][11] != 100) {
            flags += " -" + fighterNames[i] + "_air " + fighters[fighterNames[i]][11];
        }
        if (fighters[fighterNames[i]][12] != 0 && fighters[fighterNames[i]][12] != 100) {
            flags += " -" + fighterNames[i] + "_jump " + fighters[fighterNames[i]][12];
        }
        if (fighters[fighterNames[i]][13] != 0 && fighters[fighterNames[i]][13] != 100) {
            flags += " -" + fighterNames[i] + "_gravity " + fighters[fighterNames[i]][13];
        }
        if (fighters[fighterNames[i]][14] != 0 && fighters[fighterNames[i]][14] != 100) {
            flags += " -" + fighterNames[i] + "_weight " + fighters[fighterNames[i]][14];
        }
        if (fighters[fighterNames[i]][15] != 0 && fighters[fighterNames[i]][15] != 100) {
            flags += " -" + fighterNames[i] + "_scale " + fighters[fighterNames[i]][15];
        }
        if (fighters[fighterNames[i]][16] != 0 && fighters[fighterNames[i]][16] != 100) {
            flags += " -" + fighterNames[i] + "_shield_size " + fighters[fighterNames[i]][16];
        }
        if (fighters[fighterNames[i]][17] != 0 && fighters[fighterNames[i]][17] != 100) {
            flags += " -" + fighterNames[i] + "_landing_lag " + fighters[fighterNames[i]][17];
        }
    }
    //
    console.log(flags);
    flagObj.value = flags;
}


fighterNames = ["bowser", "captain_falcon", "dk", "dr_mario", "falco", "fox", "game_and_watch",
                "ganondorf", "popo", "nana", "jigglypuff", "kirby", "link", "luigi", "mario", "marth",
                "mewtwo", "ness", "peach", "pichu", "pikachu", "roy", "samus", "sheik", "yoshi", 
                "young_link", "zelda", "boy", "girl", "giga_koopa", "master_hand", "crazy_hand"]
let fighters = {};
for (let i = 0; i < fighterNames.length; i++) {
    fighters[fighterNames[i]] = 
        {  "Damage": 100, 
            "Base Knockback": 100,
            "Knockback Growth": 100,
            "Set Knockback": 100,
            "Hitbox Size": 100,
            "Throw Damage": 100,
            "Throw Base Knockback": 100,
            "Throw Knockback Growth": 100,
            "Throw Set Knockback": 100,
            "Walk": 100,
            "Dash": 100,
            "Friction": 100,
            "Aerial": 100,
            "Jump": 100,
            "Gravity": 100,
            "Weight": 100,
            "Scale": 100,
            "Shield Size": 100,
            "Landing Lag": 100
        }
}
selector = document.getElementById("fighter-select");
damage = document.getElementById("custom-damage-input");
base = document.getElementById("custom-base-input");
growth = document.getElementById("custom-growth-input");
set = document.getElementById("custom-set-input");
size = document.getElementById("custom-size-input");
throwDamage = document.getElementById("custom-throw-damage-input");
throwBase = document.getElementById("custom-throw-base-input");
throwGrowth = document.getElementById("custom-throw-growth-input");
throwSet = document.getElementById("custom-throw-set-input");
walk = document.getElementById("custom-walk-input");
dash = document.getElementById("custom-dash-input");
friction = document.getElementById("custom-friction-input");
air = document.getElementById("custom-air-input");
jump = document.getElementById("custom-jump-input");
gravity = document.getElementById("custom-gravity-input");
weight = document.getElementById("custom-weight-input");
scale = document.getElementById("custom-scale-input");
shield = document.getElementById("custom-shield-input");
lag = document.getElementById("custom-landing-input");
elements = [damage,base,growth,set,size,throwDamage,throwBase,throwGrowth,throwSet,walk,dash,friction,air,jump,gravity,weight,scale,shield,lag]
selector.addEventListener("change", function() {
    for (let i = 0; i < elements.length; i++) {
        elements[i].value = fighters[selector.value][i]
    }
});
var change = new Event('change');
selector.dispatchEvent(change);
for (let i = 0; i < elements.length; i++) {
    elements[i].addEventListener("input", function() {
        fighters[selector.value][i] = elements[i].value;
    });
}