// Импортируем функции из main_modal.js
import initialize from './main_modal.js';


function inputs(modal) {
    return {
        type_id: modal.querySelector("#type-id"),
        type: modal.querySelector("#type"),
        attribute: modal.querySelector("#attribute"),
    };
}

function fullData(row) {
    return {
        type_id: row.dataset.id,
        type: row.querySelector("[data-label='тип']").textContent,
        attribute: row.querySelector("[data-label='характеристика']").textContent,
    };
}

function emptyData(modal) {
    return {
        type_id:0,
        type: '',
        attribute: ''
    };
}

function action (){
    return "add_animal_type";
}

// Вызываем функцию initialize, передавая необходимые функции
initialize(inputs, emptyData, fullData, action);


