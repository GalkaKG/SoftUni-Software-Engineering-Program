async function solution() {
   BASE_URL = 'http://localhost:3030/jsonstore/advanced/articles/list';
   const main = document.getElementById('main');
   
   let response = await fetch(BASE_URL);
   let data = await response.json();
   for (let obj of data) {
      let id = obj._id;
      let URL = `http://localhost:3030/jsonstore/advanced/articles/details/${id}`;
      fetch(URL)
          .then((data) => data.json())
          .then((content) => {
              let title = content.title;
              let contentText = content.content;
              let divAccordion = document.createElement('div');
              divAccordion.className = 'accordion';
              let div1 = document.createElement('div');
              div1.className = 'head';
              let div2 = document.createElement('div');
              div2.className = 'extra';
              let span = document.createElement('span');
              let button = document.createElement('button');
              button.className = 'button';
              button.setAttribute('id', `${id}`);
              let p = document.createElement('p');

              span.textContent = title;
              button.textContent = 'More';
              p.textContent = contentText;

              div1.appendChild(span);
              div1.appendChild(button);
              div2.appendChild(p);
              divAccordion.appendChild(div1);
              divAccordion.appendChild(div2);
              main.appendChild(divAccordion);
              button.addEventListener('click', onMore);
            });         
   }
   
   function onMore(e) {
      const hiddenDiv = e.target.parentNode.parentNode.querySelector('.extra');
      if (e.target.textContent == 'Less') {
         hiddenDiv.style.display = 'none';
         e.target.textContent = 'More';
      }
      else {
         hiddenDiv.style.display = 'block';
         e.target.textContent = 'Less';
      } 
   }        

}
