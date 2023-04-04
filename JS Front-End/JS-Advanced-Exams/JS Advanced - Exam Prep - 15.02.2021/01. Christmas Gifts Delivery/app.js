function solution() {
    const inputElement = document.querySelector('input');
    const addGiftBtn = document.querySelector('button');
    addGiftBtn.addEventListener('click', addGiftHandler);
    const listOfGiftsUL = document.querySelector('.card:nth-child(2) ul');
    const sentGiftsUl = document.querySelector('.card:nth-child(3) ul');
    const discardedGiftsUl = document.querySelector('.card:nth-child(4) ul');
    let gifts = [];

    function addGiftHandler() {
         listOfGiftsUL.innerHTML = '';
         gifts.push(inputElement.value);
         gifts.sort((a, b) => a.localeCompare(b))
         .forEach((gift) => {
            let li = document.createElement('li');
            let sendBnt = document.createElement('button');
            let discardBtn = document.createElement('button');

            li.setAttribute('class', 'gift');
            sendBnt.setAttribute('id', 'sendButton');
            discardBtn.setAttribute('id', 'discardButton');

            li.textContent = gift;
            sendBnt.textContent = 'Send';
            discardBtn.textContent = 'Discard';

            sendBnt.addEventListener('click', sendHandler);
            discardBtn.addEventListener('click', discardHandler);

            li.appendChild(sendBnt);
            li.appendChild(discardBtn);
            listOfGiftsUL.appendChild(li);
         })
         inputElement.value = '';
    }

    function sendHandler() {
        let list = this.parentNode;
        removeButtons(list);
        sentGiftsUl.appendChild(list);
        removeGift(list.textContent);
    }

    function discardHandler() {
        let list = this.parentNode;
        removeButtons(list);
        discardedGiftsUl.appendChild(list);
        removeGift(list.textContent);
    }

    function removeButtons(list) {
        Array.from(list.querySelectorAll('button')).forEach((button) => button.remove());
    }

    function removeGift(gift) {
        let idxGift = gifts.indexOf(gift);
        gifts.splice(idxGift, 1);
    }
}
