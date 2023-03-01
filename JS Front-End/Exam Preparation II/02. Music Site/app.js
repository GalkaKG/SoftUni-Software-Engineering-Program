// В Judge се качва само функцията solve()


window.addEventListener('load', solve);

function solve() {
    
    const inputs = {
        genre: document.getElementById('genre'),
        name: document.getElementById('name'),
        author: document.getElementById('author'),
        date: document.getElementById('date'),
      };
    
    const addBtn = document.getElementById('add-btn');
    addBtn.addEventListener('click', addInfo); 

    function addInfo(event) {
        event.preventDefault();

        if (inputs.genre.value == '' || inputs.name.value == '' || inputs.author.value == '' || inputs.date.value == '') {
           return;
        } 

        let genreValue = inputs.genre.value;
        let nameValue = inputs.name.value;
        let authorValue = inputs.author.value;
        let dateValue = inputs.date.value;

        const container = document.querySelector('.all-hits-container');
    
        const divElement = document.createElement('div');
        
        divElement.className = 'hits-info';
        divElement.innerHTML = `<img src="./static/img/img.png">
                                <h2>Genre: ${genreValue}</h2>
                                <h2>Name: ${nameValue}</h2>
                                <h2>Author: ${authorValue}</h2>
                                <h3>Date: ${dateValue}</h3>
                                <button class="save-btn">Save song</button>
                                <button class="like-btn">Like song</button>
                                <button class="delete-btn">Delete</button>`;
                        
        container.appendChild(divElement);

        inputs.genre.value = '';
        inputs.name.value = '';
        inputs.author.value = '';
        inputs.date.value = '';

        const likeBtn = divElement.querySelector('.like-btn');
        const saveBtn = divElement.querySelector('.save-btn');
        const deleteBtn = divElement.querySelector('.delete-btn');

        likeBtn.addEventListener('click', increaseLikes);
        saveBtn.addEventListener('click', saveSongs);
        deleteBtn.addEventListener('click', deleteContainer)
    
        function increaseLikes(event) {
            event.target.disabled = true;
            let likes = document.querySelector('.likes p');
            splitedElement = likes.textContent.split(': ');
            let countLikes = Number(splitedElement[1]);
            countLikes++;
            let textInfo = splitedElement[0];
            likes.textContent = textInfo + ': ' + countLikes;
           
        }

        function saveSongs() {
            let savedContainer = document.querySelector('.saved-container');
            likeBtn.remove();
            saveBtn.remove();
            savedContainer.appendChild(divElement);
        }

        function deleteContainer() {
            divElement.remove();
        }
    }

}
