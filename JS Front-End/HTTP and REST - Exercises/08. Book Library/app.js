function attachEvents() {
  BASE_URL = 'http://localhost:3030/jsonstore/collections/books/'
  const loadBooksBtn = document.getElementById('loadBooks');
  const tbody = document.querySelector('tbody');
  const h3 = document.querySelector('#form h3');
  loadBooksBtn.addEventListener('click', loadAllBooks);
  const titleEl = document.querySelector('input[name="title"]');
  const authorEl = document.querySelector('input[name="author"]');
  const submitBtn = document.querySelector('#form button');
  submitBtn.addEventListener('click', onSubmit);
  let id = null;
  let infoObj = {};

  function loadAllBooks() {
      tbody.innerHTML = '';

      fetch(BASE_URL)
      .then((response) => response.json())
      .then((data) => {
        for (let obj of Object.entries(data)) {
          let author = obj[1].author;
          let title = obj[1].title;
          let id = obj[0];
          infoObj[title] = id;

          let tr = document.createElement('tr');
          let td1 = document.createElement('td');
          let td2 = document.createElement('td');
          let td3 = document.createElement('td');
          let editBtn = document.createElement('button');
          let deleteBtn = document.createElement('button');
          td1.textContent = title;
          td2.textContent = author;
          editBtn.textContent = 'Edit';
          // editBtn.id = id;
          
          deleteBtn.textContent = 'Delete';
          // deleteBtn.id = id;
          editBtn.addEventListener('click', onEdit);
          deleteBtn.addEventListener('click', onDelete);
          td3.appendChild(editBtn);
          td3.appendChild(deleteBtn);
          tr.appendChild(td1);
          tr.appendChild(td2);
          tr.appendChild(td3);
          tbody.appendChild(tr);
        }
      })
      .catch((error) => console.error(error))
  }

  function onSubmit() {
    let title = titleEl.value;
    let author = authorEl.value;

      if (h3.textContent === 'FORM') {
        if (!title || !author) {
          return
        }
        fetch(BASE_URL, {
          method: 'POST',
          headers: {'Content-Type': 'application/json'},
          body: JSON.stringify({ author, title })
        })
        loadAllBooks()
      } 
      
      if (h3.textContent === 'Edit FORM') {
        let changedTitle = titleEl.value;
        let changedAuthor = authorEl.value;
        submitBtn.textContent = 'Submit';
        h3.textContent = 'FORM'; 
        fetch(`${BASE_URL}${id}`, {
          method: 'PUT',
          headers: {'Content-Type': 'application/json'},
          body: JSON.stringify({
            "author": changedAuthor,
            "title": changedTitle
          })
        })
        loadAllBooks();
      }   
    // loadAllBooks();
    titleEl.value = '';
    authorEl.value = '';
  }

  function onEdit(e) { 
    // id = e.currentTarget.id;
    submitBtn.textContent = 'Save';
    h3.textContent = 'Edit FORM';
    titleEl.value = e.target.parentNode.parentNode.querySelector('td:first-child').textContent;
    authorEl.value = e.target.parentNode.parentNode.querySelector('td:nth-child(2)').textContent;  
    id = infoObj[titleEl.value];
  }

  function onDelete(e) {
    // id = e.currentTarget.id
    let title = e.currentTarget.parentNode.parentNode.querySelector('td:first-child').textContent;
    id = infoObj[title];
    fetch(`${BASE_URL}${id}`, {
      method: 'DELETE'
    })
    e.target.parentNode.parentNode.remove();
  }
}

attachEvents()
