import { getCookie } from "./get-cookie.js";

export function buildPreview() {
    const specifiedDate = document.getElementById("input-cell-date-sm-preview").value;
    const previewList = document.getElementById("preview-list-container");
    const previewTotals = document.getElementById("preview-total-tag-row");
    const previewTotalRow = document.getElementById("preview-total-row");
    const csrftoken = getCookie('csrftoken');
    const dateObj = {
        'specified_date' : specifiedDate
    }
    previewList.innerHTML = ''
    fetch('get-preview/', {
        method: "POST",
        body: JSON.stringify(dateObj),
        headers: { 
            "Content-Type": "application/json",
            'X-CSRFToken': csrftoken,
         }
      })
      .then(response => response.json())
      .then(data => {
        console.log(data);
        data.expenses_list.forEach(expense => {
            const previewRow = `
            <div class="content-row preview-row-sm">
                <div class="preview-cell" title="${expense[0][1] ?? ''}">${expense[0][0] ?? ''}</div>
                <div class="separator"></div>
                <div class="preview-cell" title="${expense[1][1] ?? ''}">${expense[1][0] ?? ''}</div>
                <div class="separator"></div>
                <div class="preview-cell" title="${expense[2][1] ?? ''}">${expense[2][0] ?? ''}</div>
                <div class="separator"></div>
                <div class="preview-cell" title="${expense[3][1] ?? ''}">${expense[3][0] ?? ''}</div>
                <div class="separator"></div>
                <div class="preview-cell" title="${expense[4][1] ?? ''}">${expense[4][0] ?? ''}</div>
            </div>`;
    
            const previewDiv = document.createElement('div');
            previewDiv.innerHTML = previewRow;
            previewList.appendChild(previewDiv);
        })

        previewTotals.innerHTML = `
        <div class="preview-cell">
            <div id="tag-food">${data.expenses_totals['food']}</div>
        </div>
        <div class="separator"></div>
        <div class="preview-cell">
            <div id="tag-transport">${data.expenses_totals['transport']}</div>
        </div>
        <div class="separator"></div>
        <div class="preview-cell">
            <div id="tag-bills">${data.expenses_totals['bills']}</div>
        </div>
        <div class="separator"></div>
        <div class="preview-cell">
            <div id="tag-fees">${data.expenses_totals['fees']}</div>
        </div>
        <div class="separator"></div>
        <div class="preview-cell">
            <div id="tag-misc">${data.expenses_totals['misc']}</div>
        </div>`;

        if (data.expenses_list.length == 0) {
            previewTotalRow.style.justifyContent = 'flex-start';
            previewTotalRow.innerHTML = `
            <div class="input-wrapper input-wrapper-sm total-cell">
                <div style="text-align: center; font-weight: bold; height: 20px; padding: 2px" id="total">You have no expenses this month</div>
            </div>`;
        } else {
        previewTotalRow.innerHTML = `            
            <div class="input-wrapper input-wrapper-sm title-cell">
                <div style="text-align: center; font-weight: bold; height: 20px; padding: 2px" id="total">TOTAL</div>
            </div>
            <div class="separator"></div>
            <div class="input-wrapper input-wrapper-sm amount-cell">
                <div style="font-weight: bold; height: 20px; padding: 2px" id="total-amount">${data.total_amount}</div>
            </div>`;
        }
      })
}