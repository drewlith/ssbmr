submitButton = document.getElementsByName("submit")[0];
submitSource = submitButton.src;
submitPressed = "static/pressed.png"
submitText = document.getElementById("overlay");
submitButton.addEventListener("mousedown", function() {
    submitButton.src = submitPressed;
    submitText.style.color = "#000000";
});
submitButton.addEventListener("mouseup", function() {
    submitButton.src = submitSource;
    submitText.style.color = "#FFCC00";
});