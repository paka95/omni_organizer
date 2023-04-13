import { deleteNote } from "./delete-note.js";
import { editNote } from "./edit-note.js";
import { loadFirstNote } from "./load-first-note.js";

export function buildList() {
    const notesList = document.querySelector('.notes-list');
    notesList.innerHTML = ''

    fetch('get-notes/')
    .then(response => response.json())
    .then(data => {
        if (data.length == 0) {
            notesList.innerHTML = `<div style="margin: 5px auto; width: 90%; height: 120px; text-align:center">You have no notes yet</div>`;
        }

        data.forEach((note, index) => {
            const dateObj = new Date(note.last_updated);
            const options = { 
                day: '2-digit', 
                month: '2-digit', 
                year: 'numeric', 
                hour: '2-digit', 
                minute: '2-digit', 
                second: '2-digit', 
                timeZone: 'UTC' 
                };
            const formattedDate = dateObj.toLocaleString(navigator.language, options)
            const noteHtml = `
                <div class="note-card" id="note-${note.id}">
                    <div class="note-card-headline">
                        <div class="note-card-title" title="${note.title}">${note.title}</div>
                        <div class="delete-btn">
                            <i class="fa-solid fa-trash-alt"></i>
                        </div>
                    </div>
                    
                    <div class="note-card-content">${note.content}</div>
                    <div class="note-card-date">Last edited on ${formattedDate}</div>
                </div>
            `;
            const noteDiv = document.createElement('div');
            noteDiv.innerHTML = noteHtml;
            notesList.appendChild(noteDiv);

            if (index !== data.length - 1) {
                const separator = document.createElement('div');
                separator.classList.add('separator');
                notesList.appendChild(separator);
            }

        });
        // loading first note's content into the form
        loadFirstNote();
        
        const deleteButtons = document.getElementsByClassName('delete-btn')
        const editCards = document.getElementsByClassName('note-card')
        deleteNote(deleteButtons);
        editNote(editCards);
    })
}