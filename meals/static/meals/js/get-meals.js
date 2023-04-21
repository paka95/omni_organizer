import { addProduct } from "./add-product.js";

document.addEventListener("DOMContentLoaded", () => {
    const addProductBtn = document.getElementById("product-add-btn");
    addProductBtn.addEventListener('click', (e) => {
        e.preventDefault();
        addProduct();
    })
});