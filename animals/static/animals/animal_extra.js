function setLabels(selectElement) {
    const selectedOption = selectElement.options[selectElement.selectedIndex];
    const specAttr = selectedOption.getAttribute('data-spec-attribute');
    const typeAttr = selectedOption.getAttribute('data-type-attribute');

    const specAttrLabel = document.querySelector("label[for='spec_attr']");
    const typeAttrLabel = document.querySelector("label[for='type_attr']");

    specAttrLabel.textContent = specAttr;
    typeAttrLabel.textContent = typeAttr;
}
