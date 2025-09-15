var json_container = document.getElementById("seed-json");

var json_data = json_container.innerHTML;

var log = JSON.parse(json_data);

var characters = [];

var runs = 0;

Object.keys(log).forEach(function(key) {
    if (key !== "General") {
        modified_key = key.replace("&amp;", "&");
        characters.push(modified_key)
    }
  });

let seedDisplay = document.getElementById("seed-name");
logGeneral = log["General"];
seedDisplay.innerHTML = "Seed: " + logGeneral["Seed"];

var characterSelect = document.getElementById("character-select");

for (let i = 0; i < characters.length; i++) {
    let option = document.createElement("option");
    option.innerHTML = characters[i];
    if (i == 0) {
        option.selected = true;
    }
    characterSelect.appendChild(option);
}

var categorySelect = document.getElementById("category-select");

function checkCharacter() {
    return characterSelect.children[characterSelect.selectedIndex].innerHTML;
}

function checkCategory () {
    return categorySelect.children[categorySelect.selectedIndex].innerHTML;
}

var subcategorySelect = document.getElementById("subcategory-select");

function checkSubcategory () {
    return subcategorySelect.children[subcategorySelect.selectedIndex].innerHTML;
}

function getSubcategories () {
    fighterDictionary = log[checkCharacter()];
    fighterSubCategoryDict = fighterDictionary[checkCategory()];
    let subcategories = [];
    if (fighterSubCategoryDict == undefined) {
        return;
    }
    Object.keys(fighterSubCategoryDict).forEach(function(key) {
        subcategories.push(key)
      });
    subcategorySelect.innerHTML = "";
    for (let i = 0; i < subcategories.length; i++) {
        let option = document.createElement("option");
        option.innerHTML = subcategories[i];
        if (i == 0) {
            option.selected = true;
        }
        subcategorySelect.appendChild(option);
    }
    updateLog();
}

characterSelect.onchange = getSubcategories;
categorySelect.onchange = getSubcategories;

var logDisplay = document.getElementById("log-display");

function updateLog() {
    fighterDictionary = log[checkCharacter()];
    fighterSubCategoryDict = fighterDictionary[checkCategory()];
    properties = fighterSubCategoryDict[checkSubcategory()]
    console.log(properties);
    logDisplay.innerHTML = "";
    Object.keys(properties).forEach(function(key) {
        if (key !== "Tags" && key !== "Attack Rating") {
            values = properties[key];
            propertyDisplay = document.createElement("div");
            oldValueDisplay = document.createElement("div");
            dividerDisplay = document.createElement("div");
            newValueDisplay = document.createElement("div");
            propertyDisplay.innerHTML = key;
            propertyDisplay.style.color = "gold";
            propertyDisplay.style.fontSize = "x-large";
            propertyDisplay.style.textAlign = "left";
            propertyDisplay.style.fontFamily = "FolkPro";
            oldValueDisplay.innerHTML = values["Original"];
            oldValueDisplay.style.color = "white";
            oldValueDisplay.style.fontSize = "x-large";
            dividerDisplay.innerHTML = ">>>";
            dividerDisplay.style.color = "white";
            dividerDisplay.style.fontSize = "x-large";
            newValueDisplay.innerHTML = values["New"];
            newValueDisplay.style.color = "white";
            newValueDisplay.style.fontSize = "x-large";

            if (key === "Damage" || key === "Knockback Growth"|| key === "Set Knockback" ||  key === "Base Knockback" || key == "Shield Damage" || key == "Hitbox Size") {
                if (values["New"] > values["Original"]) {
                    newValueDisplay.style.color = "#88FF88FF";
                } else if (values["New"] < values["Original"]) {
                    newValueDisplay.style.color = "#FF8888FF";
                }
            }
            logDisplay.appendChild(propertyDisplay);
            logDisplay.appendChild(oldValueDisplay);
            logDisplay.appendChild(dividerDisplay);
            logDisplay.appendChild(newValueDisplay);
        }
        if (key === "Tags") {
            tagLabelDisplay = document.createElement("div");
            filler = document.createElement("div");
            filler2 = document.createElement("div");
            tagLabelDisplay.innerHTML = key;
            tagLabelDisplay.style.color = "gold";
            tagLabelDisplay.style.fontSize = "x-large";
            tagLabelDisplay.style.textAlign = "left";
            tagLabelDisplay.style.fontFamily = "FolkPro";
            tagDisplay = document.createElement("div");
            tagDisplay.style.textAlign = "left";
            tagDisplay.innerHTML = properties["Tags"];
            tagDisplay.style.color = "white";
            tagDisplay.style.fontSize = "x-large";
            logDisplay.appendChild(tagLabelDisplay);
            logDisplay.appendChild(tagDisplay);
            logDisplay.appendChild(filler);
            logDisplay.appendChild(filler2);
        }
      });
    //logDisplay.innerHTML = JSON.stringify(fighterSubCategoryDict[checkSubcategory()]);
}

subcategorySelect.onchange = updateLog;
getSubcategories();
