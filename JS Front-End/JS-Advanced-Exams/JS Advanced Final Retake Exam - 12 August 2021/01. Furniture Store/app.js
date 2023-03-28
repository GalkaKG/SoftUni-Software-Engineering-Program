window.addEventListener('load', solve);

function solve() {
    const modelEl = document.getElementById('model');
    const yearEl = document.getElementById('year');
    const descriptionEl = document.getElementById('description');
    const priceEl = document.getElementById('price');
    const addBtn = document.getElementById('add');
    addBtn.addEventListener('click', onAdd);
    const tbody = document.getElementById('furniture-list');
    let totalPriceEl = document.querySelector('.total-price');
    let totalPrice = 0;

    function onAdd(e) {
        e.preventDefault();

        let model = modelEl.value;
        let year = Number(yearEl.value);
        let description = descriptionEl.value;
        let price = Number(priceEl.value);

        if (!model || !description || year < 0 || price < 0) {
            return
        }

        let tr = document.createElement('tr');
        tr.className = 'tr';
        tr.className = 'info';
        let td1 = document.createElement('td');
        let td2 = document.createElement('td');
        let td3 = document.createElement('td');
        let moreBtn = document.createElement('button');
        moreBtn.className = 'moreBtn';
        let buyBtn = document.createElement('button');
        buyBtn.className = 'buyBtn';
        let tr2 = document.createElement('tr');
        tr2.className = 'hide';
        let td4 = document.createElement('td');
        let td5 = document.createElement('td');
        td5.setAttribute('colspan', '3');

        td1.textContent = model;
        td2.textContent = price.toFixed(2);
        moreBtn.textContent = 'More Info';
        moreBtn.addEventListener('click', onMore);
        buyBtn.textContent = 'Buy it';
        buyBtn.addEventListener('click', onBuy);
        td4.textContent = `Year: ${year}`;
        td5.textContent = `Description: ${description}`;
        
        tr.appendChild(td1);
        tr.appendChild(td2);
        tr.appendChild(td3);
        td3.appendChild(moreBtn);
        td3.appendChild(buyBtn);
        tr2.appendChild(td4);
        tr2.appendChild(td5);
        tbody.appendChild(tr);
        tbody.appendChild(tr2);

        modelEl.value = '';
        yearEl.value = '';
        descriptionEl.value = '';
        priceEl.value = '';

        function onMore() {
            if (moreBtn.textContent == 'Less Info') {
                tr2.style.display = 'none';
                moreBtn.textContent = 'More Info';
            } else {
                tr2.style.display = 'contents';
                moreBtn.textContent = 'Less Info';
            }
        }

        function onBuy(e) {
           let parent = e.target.parentNode.parentNode;
           let currPrice = Number(parent.querySelector('td:nth-child(2)').textContent);
           totalPrice += currPrice;
           totalPriceEl.textContent = totalPrice.toFixed(2);
           parent.remove();
        }
    }
}
