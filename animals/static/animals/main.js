function showTech(showId) {
    var techObj = document.getElementById(showId);
    techObj.style.display = (techObj.style.display === "block") ? "none" : "block";
}

function dropDownShow(showId) {
    document.getElementById(showId).classList.toggle("show");
}

function dropDownShowClass(showClass) {
    document.querySelector(showClass).classList.toggle("show_class");
}

