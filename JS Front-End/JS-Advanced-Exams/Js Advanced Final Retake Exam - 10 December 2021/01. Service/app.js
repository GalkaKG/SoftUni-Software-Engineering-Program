window.addEventListener('load', solve);

// В джъдж се качва само функцията solve()

function solve() {
    const productTypeEl = document.getElementById('type-product');
    const clientNameEl = document.getElementById('client-name');
    const clientPhoneEl = document.getElementById('client-phone');
    const sendFormBtn = document.querySelector('#right button');
    const descriptionEl = document.getElementById('description');
    const receivedOrders = document.getElementById('received-orders');
    sendFormBtn.addEventListener('click', onSend);
    const completedOrders = document.getElementById('completed-orders');
    const clearBtn = document.querySelector('.clear-btn');
    clearBtn.addEventListener('click', onClear);

    function onSend(e) {
        e.preventDefault();

        let productType = productTypeEl.value;
        let clientName = clientNameEl.value;
        let clientPhone = clientPhoneEl.value;
        let description = descriptionEl.value;

        if (!productType || !clientName || !clientPhone || !description) {
            return
        }

        let div = document.createElement('div');
        div.className = 'container';
        let h2 = document.createElement('h2');
        let h3 = document.createElement('h3');
        let h4 = document.createElement('h4');
        let startBtn = document.createElement('button');
        startBtn.className = 'start-btn';
        let finishBtn = document.createElement('button');
        finishBtn.className = 'finish-btn';
        finishBtn.disabled = true;
        h2.textContent = `Product type for repair: ${productType}`;
        h3.textContent = `Client information: ${clientName}, ${clientPhone}`;
        h4.textContent = `Description of the problem: ${description}`;
        startBtn.textContent = 'Start repair';
        finishBtn.textContent = 'Finish repair';
        div.appendChild(h2);
        div.appendChild(h3);
        div.appendChild(h4);
        div.appendChild(startBtn);
        div.appendChild(finishBtn);
        receivedOrders.appendChild(div);

        productTypeEl.value = '';
        clientNameEl.value = '';
        clientPhoneEl.value = '';
        descriptionEl.value = '';

        startBtn.addEventListener('click', onStart);
        finishBtn.addEventListener('click', onFinish);

        function onStart() {
            startBtn.disabled = true;
            finishBtn.disabled = false;
        }

        function onFinish(e) {
            let div = document.createElement('div');
            div.className = 'container';
            let h2 = document.createElement('h2');
            let h3 = document.createElement('h3');
            let h4 = document.createElement('h4');
            h2.textContent = `Product type for repair: ${productType}`;
            h3.textContent = `Client information: ${clientName}, ${clientPhone}`;
            h4.textContent = `Description of the problem: ${description}`;
            div.appendChild(h2);
            div.appendChild(h3);
            div.appendChild(h4);
            completedOrders.appendChild(div);
         
            e.target.parentNode.remove();
        }
    }

    function onClear() {
        let divArr = completedOrders.querySelectorAll('div');
        for (let arr of divArr) {
            arr.remove();
        }

    }
}
