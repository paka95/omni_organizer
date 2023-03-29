import { buildList } from "./build-list.js";
import { submitExpense } from "./submit-expense.js";
import { deleteExpense } from "./delete-expense.js";

document.addEventListener("DOMContentLoaded", function(event) {
    buildList();

    const specified_date = document.getElementById('input-cell-date-sm');
    specified_date.addEventListener('change', () => {
        buildList();
    })

    const expenseAddBtn = document.getElementById("expense-add-btn")
    expenseAddBtn.addEventListener("click", (e) => {
        e.preventDefault();
        submitExpense();
    })
});