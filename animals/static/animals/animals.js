// Импортируем функции из main_modal.js
import initialize from './main_modal.js';

const typesId = document.querySelector("#url-parameters").dataset.type;
const specsId = document.querySelector("#url-parameters").dataset.spec;

function inputs(modal) {
    return {
        specId: modal.querySelector("#spec-id"),
        name: modal.querySelector("#name"),
        date: modal.querySelector("#date"),
        spec: modal.querySelector("#spec"),
//        specLabel: modal.querySelector("label[for='spec']"),
        specAttr: modal.querySelector("#spec_attr"),
//        typeLabel: modal.querySelector("label[for='type']"),
        typeAttr: modal.querySelector("#type_attr"),
    };
}

function fullData(row) {
    return {
        specId: row.dataset.id,
        name: row.querySelector("[data-label='имя']").textContent,
        date: row.querySelector("[data-label='дата рождения']").dataset.date,
        spec: row.querySelector("[data-label='вид']").dataset.id,
//        specLabel: row.querySelector("[data-label='spec-label']").textContent,
        specAttr: row.querySelector("[data-label='характеристика вида']").textContent,
//        typeLabel: row.querySelector("[data-label='spec-label']").textContent,
        typeAttr: row.querySelector("[data-label='характеристика типа']").textContent
    };
}

function emptyData(modal) {
    return {
        specId: 0,
        spec: specsId
    };
}

// Вызываем функцию initialize, передавая необходимые функции
initialize(inputs, emptyData, fullData);


