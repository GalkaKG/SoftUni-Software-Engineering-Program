function attachEvents() {
    BASE_URL = 'http://localhost:3030/jsonstore/tasks/';

    const titleEl = document.getElementById('title');
    const addBtn = document.getElementById('add-button');
    const loadBtn = document.getElementById('load-button');
    loadBtn.addEventListener('click', onLoad);
    addBtn.addEventListener('click', onAdd);
    const ulToDoList = document.getElementById('todo-list');

    async function onLoad(e) {
        e?.preventDefault();
        ulToDoList.innerHTML = '';
    
        let response = await fetch(BASE_URL);
        let data = await response.json();

        for (let obj of Object.values(data)) {
            let li = document.createElement('li');
            let span = document.createElement('span');
            let removeBtn = document.createElement('button');
            let editBtn = document.createElement('button');
            span.textContent = obj.name;
            removeBtn.textContent = 'Remove';
            editBtn.textContent = 'Edit';
            removeBtn.addEventListener('click', onRemove);
            editBtn.addEventListener('click', onEdit);

            li.appendChild(span);
            li.appendChild(removeBtn);
            li.appendChild(editBtn);
            ulToDoList.appendChild(li);
        }
    }

    async function onAdd(e) {
        e.preventDefault();

        let name = titleEl.value;
        await fetch(BASE_URL, {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({ name })
        });
        titleEl.value = '';
        onLoad();
    }

    async function onRemove(e) {
        e.preventDefault();
        let oldName = e.target.parentNode.querySelector('span').textContent;
        let data = await (await fetch(BASE_URL)).json();
        let obj = Object.values(data).filter((obj) => obj.name == oldName);
        let id = obj[0]._id;
        
        await fetch(`${BASE_URL}${id}`, {
            method: 'DELETE'
        })
        onLoad();
    }

    async function onEdit(e) {
        e.preventDefault();
        e.target.textContent = 'Submit';
        let parentNode = e.target.parentNode;
        let spanEl = parentNode.querySelector('span');
        let input = document.createElement('input');
        let oldName = spanEl.textContent;
        input.value = oldName;
        parentNode.replaceChild(input, spanEl);

        let data = await (await fetch(BASE_URL)).json();
        let obj = Object.values(data).filter((obj) => obj.name == oldName);
        let id = obj[0]._id;
        e.target.addEventListener('click', onSubmit);

        async function onSubmit() {
            let name = input.value;
            let res = await fetch(`${BASE_URL}${id}`, {
                method: 'PATCH',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify({ name })
            })
            onLoad();
        }   
    }
}

attachEvents();
