function solve(){
   const inputElements = {
      author: document.getElementById('creator'),
      title: document.getElementById('title'),
      category: document.getElementById('category'),
      content: document.getElementById('content')
   }
   const otherDOMSelectors = {
      createBtn: document.querySelector('.btn.create'),
      sectionPosts: document.querySelector('main > section'),
      form: document.querySelector('form'),
      ol: document.querySelector('.archive-section > ol')
   }
   otherDOMSelectors.createBtn.addEventListener('click', createHandler);
   let titles = [];

   function createHandler(e) {
      e.preventDefault();
      let article = createElement('article', otherDOMSelectors.sectionPosts);
      createElement('h1', article, inputElements.title.value);
      let p = createElement('p', article, 'Category:');
      createElement('strong', p, inputElements.category.value);
      let p2 = createElement('p', article, 'Creator:');
      createElement('strong', p2, inputElements.author.value);
      createElement('p', article, inputElements.content.value);
      let div = createElement('div', article, '', ['buttons']);
      let deleteBtn = createElement('button', div, 'Delete', ['btn', 'delete']);
      let archiveBtn = createElement('button', div, 'Archive', ['btn', 'archive']);
      deleteBtn.addEventListener('click', deleteHandler);
      archiveBtn.addEventListener('click', archiveHandler);
      otherDOMSelectors.form.reset();
   }

   function deleteHandler() {
       otherDOMSelectors.sectionPosts.innerHTML = `<h2>Posts</h2>`;
   }

   function archiveHandler() {
      otherDOMSelectors.ol.innerHTML = '';
      let text = this.parentNode.parentNode.querySelector('section > article > h1').textContent;
      titles.push(text);
      titles.sort((a, b) => a.localeCompare(b));
      for (let text of titles) {
         createElement('li', otherDOMSelectors.ol, text);
      }
      
      this.parentNode.parentNode.remove();
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
