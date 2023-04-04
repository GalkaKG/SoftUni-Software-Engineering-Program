function solve() {
   const inputElements = {
    task: document.getElementById('task'),
    description: document.getElementById('description'),
    date: document.getElementById('date')
   }

   const otherDOMSelectors = {
       addBtn: document.getElementById('add'),
       open: document.querySelector('.wrapper section:nth-child(2)'),
       inProgress: document.querySelector('.wrapper section:nth-child(3)'),
       complete: document.querySelector('.wrapper section:nth-child(4)')
   }

   otherDOMSelectors.addBtn.addEventListener('click', onAdd);

   function onAdd(e) {
    e.preventDefault();

    let allAreValid = Object.values(inputElements).every((input) => input.value !== '');
    if (!allAreValid) {
        return;
    }
    
    let article = createElement('article', otherDOMSelectors.open.querySelector('div:nth-child(2)'));
    createElement('h3', article, inputElements.task.value);
    createElement('p', article, `Description: ${inputElements.description.value}`);
    createElement('p', article, `Due Date: ${inputElements.date.value}`);
    let div = createElement('div', article, '', ['flex']);
    let startBtn = createElement('button', div, 'Start', ['green']);
    let deleteBtn = createElement('button', div, 'Delete', ['red']);
    startBtn.addEventListener('click', onStart);
    deleteBtn.addEventListener('click', onDelete);

    Object.values(inputElements).forEach((input) => input.value = '');
}

function onStart() {
    let article = this.parentNode.parentNode;
    otherDOMSelectors.inProgress.querySelector('div:nth-child(2)').appendChild(article);
    article.querySelector('.green').remove();
    article.querySelector('.red').remove();
    let deleteBtn = createElement('button', article.querySelector('div'), 'Delete', ['red']);
    let finishBtn = createElement('button', article.querySelector('div'), 'Finish', ['orange']);
    deleteBtn.addEventListener('click', onDelete);
    finishBtn.addEventListener('click', onFinish);
}

function onDelete() {
    this.parentNode.parentNode.remove();
}

function onFinish() {
    let article = this.parentNode.parentNode;
    otherDOMSelectors.complete.querySelector('div:nth-child(2)').appendChild(article);
    article.querySelector('div').remove();
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
