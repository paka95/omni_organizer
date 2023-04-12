import { buildList } from "./build-list.js";
import { getCookie } from "./get-cookie.js";

export function submitNote() {
    const csrftoken = getCookie('csrftoken');

    console.log("hejka z funkcji");
    // const title = document.getElementById
    fetch('submit/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,
        },
        // body: JSON.stringify(expenseData),
    })
    .then(()=> {
        buildList();
    })
}