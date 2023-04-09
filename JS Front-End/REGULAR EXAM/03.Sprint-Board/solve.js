function attachEvents() {
    let BASE_URL = 'http://localhost:3030/jsonstore/tasks/';
    let loadBoardBtn = document.getElementById('load-board-btn');
    loadBoardBtn.addEventListener('click', onLoadBoard);
    let addTaskBtn = document.getElementById('create-task-btn');
    addTaskBtn.addEventListener('click', onAdd);
    const titleEl = document.getElementById('title');
    const descriptionEl = document.getElementById('description');
    const toDoSection = document.querySelector('#todo-section .task-list');
    const inProgressSection = document.querySelector('#in-progress-section .task-list');
    const codeReviewSection = document.querySelector('#code-review-section .task-list');
    const doneSection = document.querySelector('#done-section .task-list');
    let dataStatuses = {};

    function onLoadBoard() {
      toDoSection.innerHTML = '';
      inProgressSection.innerHTML = '';
      codeReviewSection.innerHTML = '';
      doneSection.innerHTML = '';

        fetch(BASE_URL)
          .then((response) => response.json())
          .then((data) => {
            for (let obj of Object.values(data)) { 
              dataStatuses[obj._id] = obj.status;
              let li = document.createElement('li');
              li.className = 'task';
              createElement('h3', li, obj.title);
              createElement('p', li, obj.description);
              let button = createElement('button', li);
              button.id = obj._id;
              if (obj.status !== 'Done') {
                button.addEventListener('click', onMove);
              } else {
                button.addEventListener('click', onDelete);
              }

              if (obj.status == "ToDo") {
                button.textContent = 'Move to In Progress';
                toDoSection.appendChild(li);

              } else if (obj.status == 'In Progress') {
                button.textContent = 'Move to Code Review';
                inProgressSection.appendChild(li);

              } else if (obj.status == "Code Review") {
                button.textContent = 'Move to Done';
                codeReviewSection.appendChild(li);

              } else if (obj.status == "Done") {
                button.textContent = 'Close';
                doneSection.appendChild(li);
              }
            }
          })
          .catch((err) => console.error(err));
    }

    function onAdd() {
      let data = {  
        "title": titleEl.value,
        "description": descriptionEl.value,
        "status": "ToDo" 
      };
    
      fetch(BASE_URL, {
        method: 'POST',
        body: JSON.stringify(data)
      })
      .then(() => onLoadBoard(), titleEl.value = '', descriptionEl.value = '')
      .catch((err) => console.error(err));
    }

    function onMove(e) {
       let id = e.target.id;
       let currStatus = dataStatuses[id];
       let status = '';
       if (currStatus == 'ToDo') {
          status = 'In Progress';
       } else if (currStatus == 'In Progress') {
          status = 'Code Review';
       } else if (currStatus == 'Code Review') {
          status = 'Done';
       }

       fetch(BASE_URL + id, {
         method: 'PATCH',
         body: JSON.stringify({ "status": status })
       })
       .then(() => onLoadBoard())
       .catch((err) => console.error(err));
    }

    function onDelete(e) {
      let id = e.target.id;
      fetch(BASE_URL + id, {
        method: 'DELETE'
      })
      .then(() => onLoadBoard())
      .catch((err) => console.error(err));
    }

    function createElement(type, parentNode, content, classes, id, attributes, useInnerHtml) {
      const htmlElement = document.createElement(type);
    
      if (content && useInnerHtml) {
        htmlElement.innerHTML = content;
      } else {
        if (content && type !== 'input') {
          htmlElement.textContent = content;
        }
    
        if (content && type === 'input') {
          htmlElement.value = content;
        }
      }
    
      if (classes && classes.length > 0) {
        htmlElement.classList.add(...classes);
      }
    
      if (id) {
        htmlElement.id = id;
      }
    
      // { src: 'link', href: 'http' }
      if (attributes) {
        for (const key in attributes) {
          htmlElement.setAttribute(key, attributes[key])
        }
      }
    
      if (parentNode) {
        parentNode.appendChild(htmlElement);
      }
    
      return htmlElement;
    }
}   

attachEvents();
