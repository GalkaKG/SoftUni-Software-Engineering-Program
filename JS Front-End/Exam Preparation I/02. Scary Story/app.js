window.addEventListener("load", solve);

function solve() {
  let firstName = document.getElementById('first-name');
  let lastName = document.getElementById('last-name');
  let age = document.getElementById('age');
  let storyTitle = document.getElementById('story-title');
  let genre = document.getElementById('genre');
  let story = document.getElementById('story');
  let ul = document.getElementById('preview-list');
  let mainElement = document.getElementById('main');

  let publishBtn = document.getElementById('form-btn');
  publishBtn.addEventListener('click', publishInformation);

  function publishInformation(event) {
      event.preventDefault();
     
      if (firstName.value == '' 
        || lastName.value == '' 
        || age.value == '' 
        || storyTitle.value == '' 
        || story.value == '') {
          return;
      }
       
      let li = document.createElement('li');
      li.className = 'story-info';
      let article = document.createElement('article');

      let h4 = document.createElement('h4');
      h4.textContent = `Name: ${firstName.value} ${lastName.value}`;
      let p1 = document.createElement('p');
      p1.textContent = `Age: ${age.value}`;
      let p2 = document.createElement('p');
      p2.textContent = `Title: ${storyTitle.value}`;
      let p3 = document.createElement('p');
      p3.textContent = `Genre: ${genre.value}`;
      let p4 = document.createElement('p');
      p4.textContent = `${story.value}`;

      let saveBtn = document.createElement('button');
      saveBtn.className = 'save-btn';
      saveBtn.textContent = 'Save Story';

      let editBtn = document.createElement('button');
      editBtn.className = 'edit-btn';
      editBtn.textContent = 'Edit Story';

      let deleteBtn = document.createElement('button');
      deleteBtn.className = 'delete-btn';
      deleteBtn.textContent = 'Delete Story';
      
      article.appendChild(h4);
      article.appendChild(p1);
      article.appendChild(p2);
      article.appendChild(p3);
      article.appendChild(p4);
      li.appendChild(article);
      li.appendChild(saveBtn);
      li.appendChild(editBtn);
      li.appendChild(deleteBtn);
      ul.appendChild(li);
      
      let editFirstName = firstName.value;
      let editLastName = lastName.value;
      let editAge = age.value;
      let editTitle = storyTitle.value;
      let editStory = story.value;

      firstName.value = "";
      lastName.value = "";
      age.value = "";
      storyTitle.value = "";
      story.value = "";

      publishBtn.disabled = true;

      editBtn.addEventListener('click', onEdit);

      function onEdit() {  
        firstName.value = editFirstName;
        lastName.value = editLastName;
        age.value = editAge;
        storyTitle.value = editTitle;
        story.value = editStory;

        li.remove();
        publishBtn.disabled = false;
      }

      saveBtn.addEventListener('click', onSave);

      function onSave() {
        let wrapperElement1 = document.querySelector('.form-wrapper');
        wrapperElement1.remove();
        let wrapperElement2 = document.getElementById('side-wrapper');
        wrapperElement2.remove()

        let h1 = document.createElement('h1');
        h1.textContent = "Your scary story is saved!";
        
        mainElement.appendChild(h1);
      }

      deleteBtn.addEventListener('click', onDelete);

      function onDelete() {
        li.remove();
        publishBtn.disabled = false;
      }

  }

}
