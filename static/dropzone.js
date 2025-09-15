document.querySelectorAll(".drop-zone__input").forEach(inputElement => {
    const dropZoneElement = inputElement.closest(".drop-zone");

    dropZoneElement.addEventListener("click", e => {
        inputElement.click();
    });

    inputElement.addEventListener("change", e => {
        if (inputElement.files.length) {
            updateThumbnail(dropZoneElement, inputElement.files[0]);
        }
    });

    dropZoneElement.addEventListener("dragover", e => {
        e.preventDefault();
        dropZoneElement.classList.add("drop-zone--over");
    });

    ["dragleave", "dragend"].forEach(type => {
        dropZoneElement.addEventListener(type, e=> {
            dropZoneElement.classList.remove("drop-zone--over");
        })
    });

    dropZoneElement.addEventListener("drop", e => {
        e.preventDefault();
        if (e.dataTransfer.files.length) {
            if (inputElement.files.length < 1) {
                inputElement.files = e.dataTransfer.files;
                updateThumbnail(dropZoneElement, e.dataTransfer.files[0]);
            }
        }
        dropZoneElement.classList.remove("drop-zone--over");
    });
});

function getExtension(filename) {
    return filename.split('.').pop();
}

function updateThumbnail(dropZoneElement, file) {

    let thumbnailElement = dropZoneElement.querySelector("drop-zone__thumb");

    if (getExtension(file.name) != "iso") {
        dropZoneElement.querySelector(".drop-zone__prompt").innerHTML = "Invalid filetype. Please select a .iso file";
        return;
    }
    if (file.size != 1459978240) {
        console.log(file.size);
        dropZoneElement.querySelector(".drop-zone__prompt").innerHTML = "Invalid file length. Must be 1,459,978,240 bytes";
        document.getElementById("iso").files = null;
        document.getElementById("iso").value = "";
        return;
    }
    // First time, remove prompt
    if (dropZoneElement.querySelector(".drop-zone__prompt")) {
        dropZoneElement.querySelector(".drop-zone__prompt").remove();
    }
    // First time, no element. Needs to be created.
    if (!thumbnailElement) {
        thumbnailElement = document.createElement("div");
        thumbnailElement.classList.add("drop-zone__thumb");
        dropZoneElement.appendChild(thumbnailElement);
    }
    thumbnailElement.dataset.label = file.name;
    thumbnailElement.style.backgroundImage = "static/disc.png";
}