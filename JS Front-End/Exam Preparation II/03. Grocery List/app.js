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
    cleanInputs();

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

        onLoad();
        cleanInputs();
    }
}

function getId(product) {
    return productIdObjs[product];
}

function cleanInputs() {
    document.getElementById('product').value = '';
    document.getElementById('count').value = '';
    document.getElementById('price').value = '';
}



// SEcond Decision:

// function attachEvents() {
//   const BASE_URL = 'http://localhost:3030/jsonstore/grocery/';
//   const inputDOMSelectors = {
//     product: document.getElementById('product'),
//     count: document.getElementById('count'),
//     price: document.getElementById('price'),
//   }
//   const otherDOMSelectors = {
//     addBtn: document.getElementById('add-product'),
//     updateBtn: document.getElementById('update-product'),
//     loadBtn: document.getElementById('load-product'),
//     productsContainer: document.getElementById('tbody'),
//     form: document.querySelector('.list'),
//   }
//   let currentProducts = [];
//   let productToEdit = {};

//   otherDOMSelectors.loadBtn.addEventListener('click', loadAllProductsHandler);
//   otherDOMSelectors.updateBtn.addEventListener('click', updateProductHandler);
//   otherDOMSelectors.addBtn.addEventListener('click', addProductHandler);

//   function loadAllProductsHandler(event) {
//     if (event) {
//       event.preventDefault();
//     }

//     otherDOMSelectors.productsContainer.innerHTML = '';
//     fetch(BASE_URL)
//       .then((res) => res.json())
//       .then((allProductsRes) => {
//         currentProducts = Object.values(allProductsRes);
//         for (const { product, count, price, _id } of currentProducts) {
//           const tableRow = createElement('tr', otherDOMSelectors.productsContainer);
//           tableRow.id = _id;
//           createElement('td', tableRow, product, ['name']);
//           createElement('td', tableRow, count, ['count']);
//           createElement('td', tableRow, price, ['product-price']);
//           const buttonsTd = createElement('td', tableRow, null, ['btn']);
//           const updateBtn = createElement('button', buttonsTd, 'Update', ['update']);
//           const deleteBtn = createElement('button', buttonsTd, 'Delete', ['delete']);
//           updateBtn.addEventListener('click', loadUpdateFormHandler);
//           deleteBtn.addEventListener('click', deleteProductHandler);
//         }
//       })
//   }

//   function loadUpdateFormHandler() {
//     const id = this.parentNode.parentNode.id;
//     productToEdit = currentProducts.find((p) => p._id === id);
//     for (const key in inputDOMSelectors) {
//       inputDOMSelectors[key].value = productToEdit[key];
//     }
//     otherDOMSelectors.addBtn.setAttribute('disabled', true);
//     otherDOMSelectors.updateBtn.removeAttribute('disabled');
//   }

//   function updateProductHandler(event) {
//     event.preventDefault();
//     const { product, count, price } = inputDOMSelectors;
//     const payload = JSON.stringify({
//       product: product.value,
//       count: count.value,
//       price: price.value
//     });
//     const httpHeaders = {
//       method: 'PATCH',
//       body: payload
//     }

//     fetch(`${BASE_URL}${productToEdit._id}`, httpHeaders)
//       .then(() => {
//         loadAllProductsHandler();
//         otherDOMSelectors.addBtn.removeAttribute('disabled');
//         otherDOMSelectors.updateBtn.setAttribute('disabled', true);
//         otherDOMSelectors.form.reset();
//       })
//       .catch((err) => {
//         console.error(err);
//       })
//   }

//   function addProductHandler(event) {
//     event.preventDefault();
//     const { product, count, price } = inputDOMSelectors;
//     const payload = JSON.stringify({
//       product: product.value,
//       count: count.value,
//       price: price.value
//     });
//     const httpHeaders = {
//       method: 'POST',
//       body: payload
//     };

//     fetch(BASE_URL, httpHeaders)
//       .then(() => {
//         loadAllProductsHandler();
//         otherDOMSelectors.form.reset();
//       })
//       .catch((err) => {
//         console.error(err);
//       })
//   }

//   function deleteProductHandler() {
//     const id = this.parentNode.parentNode.id;
//     const httpHeaders = {
//       method: 'DELETE'
//     };

//     fetch(`${BASE_URL}${id}`, httpHeaders)
//       .then(() => loadAllProductsHandler())
//       .catch((err) => {
//         console.error(err);
//       })
//   }

//   function createElement(type, parentNode, content, classes, id, attributes, useInnerHtml) {
//     const htmlElement = document.createElement(type);
  
//     if (content && useInnerHtml) {
//       htmlElement.innerHTML = content;
//     } else {
//       if (content && type !== 'input') {
//         htmlElement.textContent = content;
//       }
  
//       if (content && type === 'input') {
//         htmlElement.value = content;
//       }
//     }
  
//     if (classes && classes.length > 0) {
//       htmlElement.classList.add(...classes);
//     }
  
//     if (id) {
//       htmlElement.id = id;
//     }
  
//     // { src: 'link', href: 'http' }
//     if (attributes) {
//       for (const key in attributes) {
//         htmlElement.setAttribute(key, attributes[key])
//       }
//     }
  
//     if (parentNode) {
//       parentNode.appendChild(htmlElement);
//     }
  
//     return htmlElement;
//   }
// }

// attachEvents();

