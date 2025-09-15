var flagArea = document.getElementById("flags");
flagArea.onchange = updateComponents;
var seedInput = document.getElementById("seed");
seedInput.onchange = updateFlags;
var standardGrid = document.getElementById("standard-grid");
var shuffleGrid = document.getElementById("shuffle-grid");
var specialGrid = document.getElementById("special-grid");
var geckoGrid = document.getElementById("gecko-grid");
//var customGrid = document.getElementById("custom-grid");
var grids = [standardGrid, shuffleGrid, specialGrid, geckoGrid];
var flagInput = document.getElementById("entry");
var entries = [];
var options = document.getElementsByClassName("menu-options");
var flagNames = [];
var lastFlagset = "";
var customFlags = "";

function addFlagEntry(grid, entryName, flagName, _commands, tooltip="", _checked=false) {
    newEntry = flagInput.cloneNode(true);
    let checkbox = newEntry.children[0];
    checkbox.checked = false
    if (_checked) {
        checkbox.checked = true
    }
    let label = newEntry.children[1];
    //let selection = newEntry.children[2];
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
    newEntry.getvalue = entryName;
    newEntry.data = flagName;
    newEntry.commands = _commands
    flagNames.push(flagName);
    newEntry.id = newEntry.id + entries.length;
    newEntry.style.display = "block";
    newEntry.onchange = updateFlags;
    addTooltip(newEntry, tooltip);
    entries.push(newEntry);
    grid.appendChild(newEntry);
    updateFlags();
}

function updateFlags() {
    flagset = ""
    if (seedInput.value.length > 0) {
        flagset += "-seed " + seedInput.value + " ";
    }
    flagArea.value = flagset;

    for (let i = 0; i < entries.length; i++) {
        if (entries[i].children[0].checked) {
            flagset += entries[i].data + " ";
        }
    }
    /*
    for (let i = 0; i < geckoEntries.length; i++) {
        if (geckoEntries[i].children[0].checked) {
            flagset += geckoEntries[i].data + " ";
        }
    }
        */
    flagset += customFlags;
    flagArea.value = flagset;
    lastFlagset = flagset;
};

function updateComponents() {
    flagset = flagArea.value + "-";
    if (flagset.includes("-seed")) {
        seedInput.value = getStringAfter(flagset, "-seed");
    }
    //allFlags = entries.concat(geckoEntries);
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

for (const key in standardJson) {
        addFlagEntry(standardGrid, key, "/" + key.toLowerCase().replaceAll(" ", "_") + "/", standardJson[key]["Commands"], standardJson[key]["Description"] + " - Credit: " + standardJson[key]["Credit"], true);
    }
for (const key in shuffleJson) {
        addFlagEntry(shuffleGrid, key, "/" + key.toLowerCase().replaceAll(" ", "_") + "/", shuffleJson[key]["Commands"], shuffleJson[key]["Description"] + " - Credit: " + shuffleJson[key]["Credit"]);
    }
for (const key in specialJson) {
        addFlagEntry(specialGrid, key, "/" + key.toLowerCase().replaceAll(" ", "_") + "/", specialJson[key]["Commands"], specialJson[key]["Description"] + " - Credit: " + specialJson[key]["Credit"]);
    }
for (const key in geckoJson) {
        addFlagEntry(geckoGrid, key, "/" + key.toLowerCase().replaceAll(" ", "_") + "/", geckoJson[key]["Commands"], geckoJson[key]["Description"] + " - Credit: " + geckoJson[key]["Credit"]);
    }

// MENU CODE
var standardRadio = document.getElementById("standard-menu");
var shuffleRadio = document.getElementById("shuffle-menu");
var specialRadio = document.getElementById("special-menu");
var geckoRadio = document.getElementById("gecko-menu");
//customRadio = document.getElementById("custom-menu");

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
        options[i].style.backgroundColor = "#7700ff5d";
        options[i].children[1].style.color = "white";
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
        }
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
            options[i].style.backgroundColor = "#7700ff5d";
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

// GENERATE
// AI Generated lol
function checkFileExists(filePath) {
  return new Promise(async (resolve, reject) => {
    try {
      const response = await fetch(filePath, { method: 'HEAD' });
      if (response.ok) {
        resolve(true); // File exists
      } else {
        resolve(false); // File does not exist
      }
    } catch (error) {
      reject(error); // Error during fetch
    }
  });
}

function generateRandomString(length) {
  const characters = 'BCDFHJKLMNPQRSTVWXYZbcdfhjklmnpqrstvwxyz0123456789';
  let result = '';
  const charactersLength = characters.length;
  for (let i = 0; i < length; i++) {
    result += characters.charAt(Math.floor(Math.random() * charactersLength));
  }
  return result;
}

function send() {
    document.body.style.pointerEvents = 'none';
    document.getElementById('overlay').style.display = 'block';
    let flags = ""
    for (let i = 0; i < entries.length - 1; i++) {
        if (entries[i].children[0].checked) {
        flags += entries[i].commands
        }
    }
    var _seed = seedInput.value
    if (_seed.length < 1) {
        _seed = generateRandomString(10)
    }
        const json = {
            flags: flags,
            seed: _seed
    };
    fetch("/generate", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify(json),
    }).then(response => {
        if (!response.ok) {
            throw new Error('Network error');
        }
        return response.text()
    }).then(data => {
        window.location.replace(data);
    });
}

