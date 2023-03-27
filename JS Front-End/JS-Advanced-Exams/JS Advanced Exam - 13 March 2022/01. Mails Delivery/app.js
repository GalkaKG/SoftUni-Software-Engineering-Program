function solve() {
    const nameEl = document.getElementById('recipientName');
    const titleEl = document.getElementById('title');
    const messageEl = document.getElementById('message');
    const addBtn= document.getElementById('add');
    const resetBtn = document.getElementById('reset');
    addBtn.addEventListener('click', onAdd);
    resetBtn.addEventListener('click', onReset);
    let ulList = document.getElementById('list');
    let deletedMails = document.querySelector('.delete-list');
    let sentMails = document.querySelector('.sent-list');

    function onAdd(event) {
        event.preventDefault();

        let name = nameEl.value;
        let title = titleEl.value;
        let message = messageEl.value;

        if (!name || !title || !message) {
            return;
        }
        
        let liSent = document.createElement('li');
        let h4First = document.createElement('h4');
        let h4Second = document.createElement('h4');
        let span = document.createElement('span');
        let div = document.createElement('div');
        div.setAttribute('id', 'list-action');
        let btn1 = document.createElement('button'); 
        btn1.setAttribute('type', 'submit');
        btn1.setAttribute('id', 'send');
        btn1.addEventListener('click', onSend);
        let btn2 = document.createElement('button');
        btn2.setAttribute('type', 'submit');
        btn2.setAttribute('id', 'delete');
        btn2.addEventListener('click', onDelete);
        h4First.textContent = `Title: ${title}`;
        h4Second.textContent = `Recipient Name: ${name}`;
        span.textContent = `${message}`;
        btn1.textContent = 'Send';
        btn2.textContent = 'Delete';
        liSent.appendChild(h4First);
        liSent.appendChild(h4Second);
        liSent.appendChild(span);
        div.appendChild(btn1);
        div.appendChild(btn2);
        liSent.appendChild(div);
        ulList.appendChild(liSent);
    
        onReset();
        
        function onSend(e) {
            let liDel = document.createElement('li');
            let span1 = document.createElement('span');
            let span2 = document.createElement('span');
            let div = document.createElement('div');
            div.className = 'btn';
            let buttonDel2 = document.createElement('button');
            buttonDel2.setAttribute('type', 'submit');
            buttonDel2.className = 'delete';
            span1.textContent = `To: ${name}`;
            span2.textContent = `Title: ${title}`;
            liDel.appendChild(span1);
            liDel.appendChild(span2);
            buttonDel2.textContent = 'Delete';
            buttonDel2.addEventListener('click', onDelete2);
            div.appendChild(buttonDel2);
            liDel.appendChild(div);
            sentMails.appendChild(liDel);
            
            e.target.parentNode.parentNode.remove();
        }

        function onDelete(e) {
            e.target.parentNode.parentNode.remove();
            create();
        }

        function onDelete2(e) {
            e.target.parentNode.parentNode.remove();
            create();
        }

        function create() {
            let liDel = document.createElement('li');
            let span1 = document.createElement('span');
            let span2 = document.createElement('span');
            span1.textContent = `To: ${name}`;
            span2.textContent = `Title: ${title}`;
            liDel.appendChild(span1);
            liDel.appendChild(span2);
            deletedMails.appendChild(liDel);
        }
    }

    function onReset(e) {
        if (e) {
            e.preventDefault();
        }
        nameEl.value = '';
        titleEl.value = '';
        messageEl.value = '';
    }
}
