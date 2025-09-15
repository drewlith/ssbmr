ALL_CHARACTERS = ["bowser", "falcon", "dk", "dr", "falco", "fox",
    "gnw", "ganon", "popo", "nana", "jigglypuff", "kirby",
    "link", "luigi", "mario", "marth", "mewtwo", "ness", "peach", "pichu",
    "pikachu", "roy", "samus", "sheik", "yoshi", "younglink", "zelda",
    "boy", "girl", "gigabowser", "masterhand", "crazyhand"]
var flagArea = document.getElementById("flags");
flagArea.onchange = updateComponents;
var seedInput = document.getElementById("seed");
seedInput.onchange = updateFlags;
var attackGrid = document.getElementById("attack-grid");
var throwGrid = document.getElementById("throw-grid");
var attributeGrid = document.getElementById("attribute-grid");
var geckoGrid = document.getElementById("gecko-grid");
var etcGrid = document.getElementById("etc-grid");
var grids = [attackGrid, throwGrid, attributeGrid, geckoGrid, etcGrid];
var flagInput = document.getElementById("adv-entry");
var etcInput = document.getElementById("adv-etc-entry");
var geckoEntries = [];
var options = document.getElementsByClassName("menu-options");
var flagNames = [];
var tagSelect = document.getElementById("tag-entry");
var charSelect = document.getElementById("character-entry");
var filler = document.getElementById("filler");
var advancedModeFlags = "";
var lastFlagset = "";
var customFlags = "";

function addFlagEntry(grid, entryName, tooltip="") {
    newEntry = flagInput.cloneNode(true);
    let category = newEntry.children[0];
    if (entryName.includes("Attributes")) {
        category.style.display = "none";
    }
    if (entryName.includes("Throws")) {
        category.children[6].style.display = "none";
        category.children[7].style.display = "none";
        category.children[8].style.display = "none";
    }
    newEntry.style.display = "block";
    addTooltip(newEntry, tooltip);
    let selection = newEntry.children[1];
    let minInput = newEntry.children[3].children[0];
    let divider = newEntry.children[3].children[1];
    let maxInput = newEntry.children[3].children[2];
    let addButton =  newEntry.children[3].children[3];
    function updateEntry() {
        if (selection.selectedIndex == 0) {
            divider.style.visibility = "hidden";
            minInput.style.visibility = "hidden";
            minInput.children[1].innerHTML = "";
            maxInput.children[1].innerHTML = "";
        }
        else if (selection.selectedIndex == 1) {
            divider.style.visibility = "visible";
            minInput.style.visibility = "visible";
            minInput.children[1].innerHTML = "";
            maxInput.children[1].innerHTML = "";
        }
        else {
            divider.style.visibility = "visible";
            minInput.style.visibility = "visible";
            minInput.children[1].innerHTML = "%";
            maxInput.children[1].innerHTML = "%";
        }
    }
    updateEntry();
    selection.oninput = updateEntry;
    let tagSelectInput = tagSelect.children[1];
    addButton.onclick = function() {
        let flag = "";
            if (charSelectInput.selectedIndex > 0) {
                character = ALL_CHARACTERS[charSelectInput.selectedIndex - 1]
                flag += character + "_";
            }
            tag = tagSelectInput.children[tagSelectInput.selectedIndex].innerHTML;

            flag += tag;

            if (!entryName.includes("Attribute")) {
                flag += "_";
                flag += category.children[category.selectedIndex].value;
            }

            flag = flag.toLowerCase()
            flag = flag.replace(/\s/g, "");
            flag = flag.replace("(", "")
            flag = flag.replace(")", "")
            flag = flag.replace(",", "")
            flag = flag.replace("!", "")
            flag = flag.replace("-", "")
            flag = flag.replace("'", "")
            flag = flag.replace("&", "")
            flag = flag.replace(":", "")
            flag = flag.replace(".", "")

            flag += " ";
            if (selection.selectedIndex == 0) {
                flag += maxInput.children[0].value;
            }
            if (selection.selectedIndex == 1) {
                flag = "randomize_" + flag;
                flag += minInput.children[0].value;
                flag += ":";
                flag += maxInput.children[0].value;
            }
            if (selection.selectedIndex == 2) {
                flag = "randomize%_" + flag;
                flag += minInput.children[0].value;
                flag += ":";
                flag += maxInput.children[0].value;
            }
            flag = "-" + flag;
            updateFlags(flag);
            
    }
    grid.appendChild(newEntry);
    updateFlags();
}

function addEtcEntry(grid, entryName, flagName, tooltip="") {
    newEntry = etcInput.cloneNode(true);
    let checkbox = newEntry.children[0];
    let label = newEntry.children[1];
    label = newEntry.children[1];
    label.innerHTML = entryName;
    label.onmousedown = function () {
        if (checkbox.checked) {
            checkbox.checked = false;
        } else {
            checkbox.checked = true;
        }
        updateFlags();
    }
    newEntry.data = flagName;
    flagNames.push(flagName);
    newEntry.id = newEntry.id + geckoEntries.length;
    newEntry.style.display = "block";
    newEntry.onchange = updateFlags;
    addTooltip(newEntry, tooltip);
    geckoEntries.push(newEntry);
    grid.appendChild(newEntry);
    updateFlags();
}

function updateFlags(flagToAdd="") {
    flagset = ""
    if (seedInput.value.length > 0) {
        flagset += "-seed " + seedInput.value + " ";
    }
    if (flagToAdd.length > 0) {
        advancedModeFlags = advancedModeFlags + flagToAdd + " ";
    }
    flagset += advancedModeFlags;
    for (let i = 0; i < geckoEntries.length; i++) {
        if (geckoEntries[i].children[0].checked) {
            flagset += geckoEntries[i].data + " ";
        }
    }
    flagset += customFlags;
    flagArea.value = flagset;
    lastFlagset = flagset;
};

function updateComponents() {
    flagset = flagArea.value + "-";
    if (flagset.includes("-seed")) {
        seedInput.value = getStringAfter(flagset, "-seed");
    }
    allFlags = geckoEntries;
    for (let i = 0; i < flagNames.length; i++) {
        if (flagset.includes(flagNames[i])) {
            allFlags[i].children[0].checked = true;
            flagParameter = getStringAfter(flagset, flagNames[i]);
            if (allFlags[i].children.length > 2) {
                allFlags[i].children[2].selectedIndex = (flagParameter - 1);
            }
        } else {
            allFlags[i].children[0].checked = false;
        }
    }
    flagset = flagset.substring(0, flagset.length - 1);
    var newCustomFlags = flagset.replace(lastFlagset, "")
    customFlags += newCustomFlags;
}

function getStringAfter(string, start) {
    new_string = string.split(start).pop().split(/-|\&/)[0];
    new_string = new_string.replace(" ", "")
    return new_string
}

addFlagEntry(attackGrid, "Attacks");
addFlagEntry(throwGrid, "Throws");
addFlagEntry(attributeGrid, "Attributes");
addEtcEntry(geckoGrid, "Air Dodge Item Catch", "-gecko_air_dodge_catch", "Credit: Uncle Punch | Air dodging into projectiles that can be caught will catch them, similar to future Smash Brothers games.");
addEtcEntry(geckoGrid, "Air Grab", "-gecko_air_grab", "Credit: Uncle Punch | Allows for grab to be performed while airborne.");
addEtcEntry(geckoGrid, "Paper Mode", "-gecko_paper_mode", "Credit: DRGN | All fighter will be flat like Game and Watch (no Z-Axis).");
addEtcEntry(geckoGrid, "All Fighters Float", "-gecko_all_float", "Credit: Uncle Punch | Every fighter can perform a float the same way Peach can.");
addEtcEntry(geckoGrid, "B Reverse", "-gecko_breverse", "Credit: Uncle Punch | Neutral B moves can be reversed by quickly moving the control stick in the opposite direction before pressing B.");
addEtcEntry(geckoGrid, "Bowser Flame Cancel", "-gecko_flame_cancel", "Credit: Achilles | Bowser's flame attack can be cancelled by landing on the ground, similar to Falco's laser.");
addEtcEntry(geckoGrid, "L to Brawl Airdodge", "-gecko_brawl_airdodge", "Credit: Uncle Punch | Pressing L results in an airdodge similar to how it works in Super Smash Bros. Brawl.");
addEtcEntry(geckoGrid, "All Fighters Walljump", "-gecko_all_walljump", "Credit: Achilles, Geuse | All fighters are able to perform a walljump similar to how characters like Fox or Mario are able to.");
addEtcEntry(geckoGrid, "Fastfall Whenever", "-gecko_fastfall_whenever", "Credit: Uncle Punch | All fighters are able to fastfall before reaching the peak of their jump.");
addEtcEntry(geckoGrid, "No Meteor Cancel", "-gecko_no_meteor", "Credit: flieskiller | Players will no longer be able to meteor cancel attacks that send straight down.");
addEtcEntry(geckoGrid, "No Shield", "-gecko_no_shield", "Credit: Achilles | Characters will be unable to use their shield.");
addEtcEntry(geckoGrid, "Perfect Shield", "-gecko_perfect_shield", "Credit: Uncle Punch | Releasing the shield button with proper timing creates an opening for counter attack, similar to in Super Smash Bros. Ultimate.");
addEtcEntry(geckoGrid, "Reverse Aerial Rush", "-gecko_rar", "Credit: MagicScrumpy | Fighters can turn around a split second before performing an aerial attack.");
addEtcEntry(geckoGrid, "Shadow Mode", "-gecko_shadow_mode", "Credit: ??? | All characters will have their models replaced with a variant that is completely black.");
addEtcEntry(geckoGrid, "Super Shine Bros.", "-gecko_shine_bros", "Credit: Uncle Punch | All characters will have their down special replaced with Shine.");

// MENU CODE
attackRadio = document.getElementById("attack-menu");
throwRadio = document.getElementById("throw-menu");
attributeRadio = document.getElementById("attribute-menu");
geckoRadio = document.getElementById("gecko-menu");
etcRadio = document.getElementById("etc-menu");

radios = document.querySelectorAll("input[type=radio]");
options[0].style.backgroundColor = "gold";
options[0].children[1].style.color = "blue";

function disableAll() {
    for (let i = 0; i < grids.length; i++) {
        grids[i].style.display = "none";
    }
}

function resetOptionColors() {
    for (let i = 0; i < options.length; i++) {
        options[i].style.backgroundColor = "#4400BB44";
        options[i].children[1].style.color = "silver";
    }
}

for (let i = 0; i < radios.length; i++) {
    radios[i].onchange = function() {
        disableAll();
        resetOptionColors();
        if (radios[i].checked) {
            grids[i].style.display = "grid";
            options[i].style.backgroundColor = "gold";
            options[i].children[1].style.color = "blue";
            // REMOVE UI ELEMENTS IN CERTAIN MENUS
            tagSelect.style.display = "none";
            charSelect.style.display = "none";
            filler.style.display = "block";
            if (i <= 2) {
                tagSelect.style.display = "block";
                charSelect.style.display = "block";
                filler.style.display = "none";
            }
        }
        updateTags();
    }

}

for (let i = 0; i < options.length; i++) {
    options[i].onmouseover = function() {
        if (!radios[i].checked) {
            options[i].style.backgroundColor = "#8800BBA0";
        }
    }
    options[i].onmouseout = function() {
        if (!radios[i].checked) {
            options[i].style.backgroundColor = "#4400BB44";
        }
    }
}

// TOOLTIPS
tooltipDisplay = document.getElementById("tooltips");

function addTooltip(object, message) {
    object.onmouseover = function() {
        tooltipDisplay.innerHTML = message;
    }
}

// ADVANCED MODE CHARACTER/TAG SELECT
var jsonContainer = document.getElementById("adv-json");
var jsonData = jsonContainer.innerHTML;
var advDict = JSON.parse(jsonData);

var charSelectInput = charSelect.children[1];

Object.keys(advDict).forEach(function(key) {
    if (!key.includes("All")) {
        option = document.createElement("option");
        option.innerHTML = key;
        charSelectInput.appendChild(option);
    }
  });

function updateTags() {
    // ATTACK
    var charSelectInput = charSelect.children[1];
    var tagSelectInput = tagSelect.children[1];
    var dict;
    tagSelectInput.innerHTML = "";
    if (radios[0].checked) {
        if (charSelectInput.selectedIndex == 0) {
            dict = advDict["All Attacks"];
        } else {
            character = charSelectInput.children[charSelectInput.selectedIndex].innerHTML;
            charDict = advDict[character];
            dict = charDict["Attacks"];
        }
        Object.keys(dict).forEach(function(key) {
            option = document.createElement("option");
            option.innerHTML = dict[key];
            tagSelectInput.appendChild(option);
        });
    }
    if (radios[1].checked) {
        if (charSelectInput.selectedIndex == 0) {
            dict = advDict["All Throws"];
        } else {
            character = charSelectInput.children[charSelectInput.selectedIndex].innerHTML;
            charDict = advDict[character];
            dict = charDict["Throws"];
        }
        Object.keys(dict).forEach(function(key) {
            option = document.createElement("option");
            option.innerHTML = dict[key];
            tagSelectInput.appendChild(option);
        });
    }
    if (radios[2].checked) {
        if (charSelectInput.selectedIndex == 0) {
            dict = advDict["All Attributes"];
        } else {
            character = charSelectInput.children[charSelectInput.selectedIndex].innerHTML;
            charDict = advDict[character];
            dict = charDict["Attributes"];
        }
        Object.keys(dict).forEach(function(key) {
            option = document.createElement("option");
            option.innerHTML = dict[key];
            tagSelectInput.appendChild(option);
        });
    }
}

charSelectInput.onchange = updateTags;
updateTags();


