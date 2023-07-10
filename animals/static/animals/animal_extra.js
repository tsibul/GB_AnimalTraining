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
    const modal = document.getElementById("modal-training");

    const animalId = button.dataset.id;
    const animalName = button.dataset.name;
    const animalType = button.dataset.type;
    modal.querySelector("#animal-id").value = animalId;
    modal.querySelector("#training-title").textContent = (param ? "Обучить " : "Отучить ") + animalName;
    modal.querySelector("#param").value = param ? 1 : 0;
    const jsonUrl ='/animals/json-data/' + animalId +  (param ? '/0' : '/1');
    const xhr = new XMLHttpRequest();
    xhr.open('GET', jsonUrl, true);  // Используйте тот же URL-адрес
    xhr.onload = function () {
        if (xhr.status === 200) {
            const jsonData = JSON.parse(xhr.responseText);
            const options = JSON.parse(jsonData).map(function (item) {
                const pk = item.pk;
                const commandName = item.fields.command_name;
                const optionValue = pk;
                return '<option value="' + optionValue + '">' + commandName + '</option>';
            });

            const optionsString = options.join('');
            modal.querySelector("#command").innerHTML = optionsString; // использование innerHTML, а не textContent
        }
    };
    xhr.send();


    modal.style.display = "block";
}

function closeTraining() {
    const modal = document.getElementById("modal-training");
    modal.style.display = "none";
}