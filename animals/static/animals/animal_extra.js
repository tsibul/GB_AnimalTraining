function setLabels(selectElement) {
    const selectedOption = selectElement.options[selectElement.selectedIndex];
    const specAttr = selectedOption.getAttribute('data-spec-attribute');
    const typeAttr = selectedOption.getAttribute('data-type-attribute');

    const specAttrLabel = document.querySelector("label[for='spec_attr']");
    const typeAttrLabel = document.querySelector("label[for='type_attr']");

    specAttrLabel.textContent = specAttr;
    typeAttrLabel.textContent = typeAttr;
}

function openTraining(button, param) {
    const modal = document.querySelector(".modal-training");

    const animalId = button.dataset.id;
    const animalName = button.dataset.name;
    const animalType = button.dataset.type;
    modal.querySelector("#animal-id").value = animalId;
    modal.querySelector("#training-title").textContent = (param ? "Обучить " : "Отучить ") + animalName;

    modal.style.display = "block";
}

function closeTraining() {
    const modal = document.getElementById("modal-training");
    modal.style.display = "none";
}