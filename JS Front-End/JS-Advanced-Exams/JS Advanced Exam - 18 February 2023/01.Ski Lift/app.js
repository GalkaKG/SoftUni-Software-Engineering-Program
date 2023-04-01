window.addEventListener('load', solve);

function solve() {
    const firstNameEl = document.getElementById('first-name');
    const lastNameEl = document.getElementById('last-name');
    const peopleCountEl = document.getElementById('people-count');
    const fromDateEl = document.getElementById('from-date');
    const daysCountEl = document.getElementById('days-count');
    const nextBtn = document.getElementById('next-btn');
    nextBtn.addEventListener('click', loadTicketInfo);
    const ticketInfoUl = document.querySelector('.ticket-info-list');
    const confirmTicketUlEl = document.querySelector('.confirm-ticket');
    const divMain = document.getElementById('main');
    const bodyEl = document.getElementById('body');

    let firstName;
    let lastName;
    let peopleCount;
    let fromDate;
    let daysCount;
   
    function loadTicketInfo(e) {
    e.preventDefault();
    firstName = firstNameEl.value;
    lastName = lastNameEl.value;
    peopleCount = peopleCountEl.value;
    fromDate = fromDateEl.value;
    daysCount = daysCountEl.value;

    if (!firstName || !lastName || !peopleCount || !fromDate || !daysCount) {
        return
    }

    let li = createElement('li', '', ticketInfoUl, '', "ticket");
    let article = createElement('article', '', li);
    createElement('h3', `Name: ${firstName} ${lastName}`, article);
    createElement('p', `From date: ${fromDate}`, article);
    createElement('p', `For ${daysCount} days`, article);
    createElement('p', `For ${peopleCount} people`, article);
    let editBtn = createElement('button', 'Edit', li, '', "edit-btn");
    let continueBtn = createElement('button', "Continue", li, '', "continue-btn");
    editBtn.addEventListener('click', onEdit);
    continueBtn.addEventListener('click', onContinue);
  
    nextBtn.disabled = true;
    firstNameEl.value = '';
    lastNameEl.value = '';
    peopleCountEl.value = '';
    fromDateEl.value = '';
    daysCountEl.value = '';
   }

   function onEdit(e) {
       nextBtn.disabled = false;
       document.querySelector('.ticket').remove();
       
       firstNameEl.value = firstName;
       lastNameEl.value = lastName;
       peopleCountEl.value = peopleCount;
       fromDateEl.value = fromDate;
       daysCountEl.value = daysCount;
   }

   function onContinue(e) {
       let liContainer = e.target.parentNode;
       confirmTicketUlEl.appendChild(liContainer);
       document.querySelector('.edit-btn').remove();
       document.querySelector('.continue-btn').remove();
       let liEl = confirmTicketUlEl.querySelector('li');
       liEl.removeAttribute('ticket');
       liEl.className = 'ticket-content'
       let confirmBtn = createElement('button', 'Confirm', liEl, '', 'confirm-btn');
       let cancelBtn = createElement('button', 'Cancel', liEl, '', 'cancel-btn');
       confirmBtn.addEventListener('click', onConfirm);
       cancelBtn.addEventListener('click', onCancel);
    }

    function onCancel(e) {
        e.target.parentNode.remove();
        nextBtn.disabled = false;
    }

    function onConfirm() {
       divMain.remove();
       createElement('h1', "Thank you, have a nice day! ", bodyEl, "thank-you");
       let backBtn = createElement('button', "Back ", bodyEl, "back-btn");
       backBtn.addEventListener('click', () => location.reload());
       
    }

    function createElement(type, content, parentNode, id, classes, attributes){
        const htmlElement = document.createElement(type)
      
        if(content && type !== 'input'){
          htmlElement.textContent = content;
        }
      
        if(content && type === 'input'){
          htmlElement.value = content;
        }
      
        if(id){
          htmlElement.id = id;
        }
      
        if (classes){
          htmlElement.classList.add(classes);
        }
      
        if (parentNode){
          parentNode.appendChild(htmlElement);
          }
      
        //{ src: 'link to img', href: 'link to site' }
        if (attributes){
          for (const key in attributes) {
            htmlElement.setAttribute(key, attributes[key]); 
          }
        } 
        return htmlElement
      }
}
