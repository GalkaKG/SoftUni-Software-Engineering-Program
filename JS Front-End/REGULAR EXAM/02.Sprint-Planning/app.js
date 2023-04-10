window.addEventListener('load', solve);

function solve() {
    const titleEl = document.getElementById('title');
    const descriptionEl = document.getElementById('description');
    const labelEl = document.getElementById('label');
    const estimationPointsEl = document.getElementById('points');
    const assigneeEl = document.getElementById('assignee')
    const createBtn = document.getElementById('create-task-btn');
    const deleteTaskBtn = document.getElementById('delete-task-btn');
    createBtn.addEventListener('click', onCreate);
    deleteTaskBtn.addEventListener('click', onDeleteTask);
    let sectionTasks = document.getElementById('tasks-section');
    let pointsEl = document.getElementById('total-sprint-points');
    let taskIdEl = document.getElementById('task-id');
    let totalPoints = 0;
    let id = 0;

    let title;
    let description;
    let label;
    let estimatedPoints;
    let assignee;

    function onCreate() {
        title = titleEl.value;
        description = descriptionEl.value;
        label = labelEl.value;
        estimatedPoints = estimationPointsEl.value;
        assignee = assigneeEl.value;


        if (!title || !description || !label || !estimatedPoints || !assignee) {
            return;
        }

        id++;
        totalPoints += Number(estimatedPoints);
        let article = createElement('article', sectionTasks, '', ['task-card']);
        article.id = `task-${id}`;
        let div = createElement('div', article, `${label}`);
        if (label == 'Feature') {
            div.setAttribute('class', 'task-card-label feature');
            div.innerHTMLt = `Feature &#8865;`;
        } else if (label == 'Low Priority Bug') {
            div.setAttribute('class', 'task-card-label low-priority')
            div.innerHTML = `Low Priority Bug &#9737;`;
        } else if (label == 'High Priority Bug') {
            div.setAttribute('class', 'task-card-label high-priority');
            div.innerHTML = `High Priority Bug &#9888;`;
        }
        
        let h3 = createElement('h3', article, `${title}`, ['task-card-title']);
        let p = createElement('p', article, `${description}`, ['task-card-description']);
        let div2 = createElement('div', article, `Estimated at ${estimatedPoints} pts`, ['task-card-points']);
        let div3 = createElement('div', article, `Assigned to: ${assignee}`, ['task-card-assignee']);
        let div4 = createElement('div', article, '', ['task-card-actions']);
        let deleteBtn = createElement('button', div4, 'Delete');
        deleteBtn.addEventListener('click', onDelete);
    
        titleEl.value = '';
        descriptionEl.value = '';
        labelEl.value = '';
        estimationPointsEl.value = '';
        assigneeEl.value = '';

        pointsEl.textContent = `Total Points: ${totalPoints}pts`;
    }

    function onDelete(e) {
       taskIdEl.value = e.target.parentNode.parentNode.id;
       titleEl.value = title;
       descriptionEl.value = description;
       labelEl.value = label;
       estimationPointsEl.value = estimatedPoints;
       assigneeEl.value = assignee;

       deleteTaskBtn.disabled = false;
       createBtn.disabled = true;
       titleEl.disabled = true;
       descriptionEl.disabled = true; 
       labelEl.disabled = true;
       estimationPointsEl.disabled = true;
       assigneeEl.disabled = true;
    }

    function onDeleteTask(e) {
        let currId = taskIdEl.value;
        let articleArrs = Array.from(sectionTasks.querySelectorAll('article'));
        let articleForRemove = articleArrs.find((art) => art.id == currId);
        let currPoints = estimationPointsEl.value;
        articleForRemove.remove()
        totalPoints -= Number(currPoints);
        pointsEl.textContent = `Total Points ${totalPoints}pts`;

        titleEl.value = '';
        descriptionEl.value = '';
        labelEl.value = '';
        estimationPointsEl.value = '';
        assigneeEl.value = '';

        titleEl.disabled = false;
        descriptionEl.disabled = false; 
        labelEl.disabled = false;
        estimationPointsEl.disabled = false;
        assigneeEl.disabled = false;

        deleteTaskBtn.disabled = true;
        createBtn.disabled = false;
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
