const BASE_URL = 'http://localhost:3030/jsonstore/grocery/';

let tableBody = document.getElementById('tbody');
const loadBtn = document.getElementById('load-product');
loadBtn.addEventListener('click', onLoad);
const addBtn = document.getElementById('add-product');
addBtn.addEventListener('click', onAdd);
const updateBtn = document.getElementById('update-product');

let productIdObjs = {};

async function onLoad(event) {
    if (event) {
        event.preventDefault();
    }
    tableBody.innerHTML = '';

    let response = await fetch(BASE_URL);
    let data = await response.json();
    
    for (const obj of Object.values(data)) {
        productIdObjs[obj.product] = obj._id;

        let tr = document.createElement('tr');
        let td1 = document.createElement('td');
        td1.className = 'name';
        let td2 = document.createElement('td');
        td2.className = 'count-product';
        let td3 = document.createElement('td');
        td3.className = 'product-price';
        let td4 = document.createElement('td');
        td4.className = 'btn';
        let button1 = document.createElement('button');
        button1.className = 'update';
        button1.addEventListener('click', onEdit);
        let button2 = document.createElement('button');
        button2.className = 'delete';
        button2.addEventListener('click', onDelete);

        td1.textContent = obj.product;
        td2.textContent = obj.count;
        td3.textContent = obj.price;
        button1.textContent = 'Update';
        button2.textContent = 'Delete';

        td4.appendChild(button1);
        td4.appendChild(button2);
        tr.appendChild(td1);
        tr.appendChild(td2);
        tr.appendChild(td3);
        tr.appendChild(td4);
        tableBody.appendChild(tr);
    }
}

async function onAdd(event) {
    event.preventDefault();

    let name = document.getElementById('product').value;
    let count = document.getElementById('count').value;
    let price = document.getElementById('price').value;
    let data = {product: name, count: count, price: price}

    document.getElementById('product').value = '';
    document.getElementById('count').value = '';
    document.getElementById('price').value = '';

    await fetch(BASE_URL, {
        method: 'post',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    });

    onLoad();
}

async function onDelete(event) {
    let product = event.target.parentNode.parentNode.firstChild.textContent;
    let id = getId(product);
    await fetch(BASE_URL + id, {
        method: 'delete'
    });

    onLoad();
}

function onEdit(event) {
   let product = event.target.parentNode.parentNode.querySelector('.name').textContent;
   let count = event.target.parentNode.parentNode.querySelector('.count-product').textContent;
   let price = event.target.parentNode.parentNode.querySelector('.product-price').textContent;
   
   document.getElementById('product').value = product;
   document.getElementById('count').value = count;
   document.getElementById('price').value = price;
 
   updateBtn.disabled = false;
   updateBtn.addEventListener('click', onUpdate);

   id = getId(product);

   async function onUpdate() {
    
    let editedProduct = document.getElementById('product').value;
    let editedCount =  document.getElementById('count').value;
    let editedPrice =  document.getElementById('price').value;
    let data = {product: editedProduct, count: editedCount, price: editedPrice}

    await fetch(BASE_URL + id, {
        method: 'PATCH',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })

    onLoad()

    document.getElementById('product').value = '';
    document.getElementById('count').value = '';
    document.getElementById('price').value = '';
}
}


function getId(product) {
    return productIdObjs[product];
}

