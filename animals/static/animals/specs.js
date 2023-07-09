// Импортируем функции из main_modal.js
import initialize from './main_modal.js';

const types_id = document.querySelector("#url-parameters").value;

function inputs(modal) {
    return {
        spec_id: modal.querySelector("#spec-id"),
        spec: modal.querySelector("#spec"),
        attribute: modal.querySelector("#attribute"),
        type: modal.querySelector("#type")
    };
}

function fullData(row) {
    return {
        spec_id: row.dataset.id,
        spec: row.querySelector("[data-label='вид']").textContent,
        attribute: row.querySelector("[data-label='характеристика']").textContent,
        type: row.querySelector("[daya-label='тип']").dataset.id
    };
}

function emptyData(modal) {
    return {
        spec_id: 0,
        type: types_id
    };
}

function action (){
    return "add_animal_type/" + types_id;
}

// Вызываем функцию initialize, передавая необходимые функции
initialize(inputs, emptyData, fullData, action);


