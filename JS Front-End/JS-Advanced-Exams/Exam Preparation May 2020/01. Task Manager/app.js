function solve() {
    const inputElements = {
        taskEl: document.getElementById('task'),
        descriptionEl: document.getElementById('description'),
        dateEl: document.getElementById('date')
    }

    const sections = {
        openSection: document.querySelector('.wrapper section:nth-child(2) div:nth-child(2)'),
        inProgress: document.querySelector('.wrapper section:nth-child(3) div:nth-child(2)'), 
        complete: document.querySelector('.wrapper section:nth-child(4) div:nth-child(2)')
    }

    const addBtn = document.getElementById('add')
    addBtn.addEventListener('click', onAdd);

    function onAdd(e) {
        e.preventDefault();
        
        let values = {
            task: inputElements.taskEl.value,
            description: inputElements.descriptionEl.value,
            date: inputElements.dateEl.value
        }

        let valid = Object.values(values).every(el => el != '');

        if (!valid) {
            return
        }

        Object.values(inputElements).forEach(el => el.value = '');

        let article = document.createElement('article');
        let h3 = document.createElement('h3');
        h3.textContent = values.task;
        let pDescription = document.createElement('p');
        pDescription.textContent = `Description: ${values.description}`;
        let pDate = document.createElement('p');
        pDate.textContent = `Due Date: ${values.date}`;
        let div = document.createElement('div');
        div.className = 'flex';
        let startBtn = document.createElement('button');
        startBtn.className = 'green';
        startBtn.textContent = 'Start';
        startBtn.addEventListener('click', onStart);
        let deleteBtn = document.createElement('button');
        deleteBtn.className = 'red';
        deleteBtn.textContent = 'Delete';
        deleteBtn.addEventListener('click', onDelete);

        div.appendChild(startBtn);
        div.appendChild(deleteBtn);
        article.appendChild(h3);
        article.appendChild(pDescription);
        article.appendChild(pDate);
        article.appendChild(div);
        sections.openSection.appendChild(article);
    }

    function onStart() {
        let delBtn = this.parentNode.firstChild; delBtn.className = 'red';
        delBtn.textContent = 'Delete';
        delBtn.addEventListener('click', onDelete);
        let finishBtn = this.parentNode.querySelector('button:nth-child(2)');
        finishBtn.className = 'orange';
        finishBtn.textContent = 'Finish';
        finishBtn.addEventListener('click', onFinish);
        sections.inProgress.appendChild(this.parentNode.parentNode);
    }

    function onDelete() {
        this.parentNode.parentNode.remove();
    }

    function onFinish() {
        sections.complete.appendChild(this.parentNode.parentNode);
        sections.complete.querySelector('div').remove();
    }
}
