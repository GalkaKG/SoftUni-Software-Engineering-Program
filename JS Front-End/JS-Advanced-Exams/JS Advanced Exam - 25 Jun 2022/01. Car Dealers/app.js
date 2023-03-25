window.addEventListener("load", solve);

// В Джъдж се качва само функцията solve()

function solve() {
  const makeEl = document.getElementById('make');
  const modelEl = document.getElementById('model');
  const yearEl = document.getElementById('year');
  const fuelEl = document.getElementById('fuel');
  const originalCostEl = document.getElementById('original-cost');
  const sellingPriceEl = document.getElementById('selling-price');
  const publishBtn = document.getElementById('publish');
  publishBtn.addEventListener('click', onPublish);
  const tableBodyEl = document.getElementById('table-body');

  let totalProfit = 0;

  function onPublish(event) {
    event.preventDefault();

    let make = makeEl.value;
    let model = modelEl.value;
    let year = yearEl.value;
    let fuel = fuelEl.value;
    let originalPrice = Number(originalCostEl.value);
    let sellingPrice = Number(sellingPriceEl.value);

    if (
      make == '' || 
      model == '' ||
      model == '' || 
      fuel == '' || 
      originalPrice == '' ||
      sellingPrice == '' ||
      originalPrice > sellingPrice
      ) {
        return
      }

      let tr = document.createElement('tr');
      tr.className = 'row';
      let td1 = document.createElement('td');
      let td2 = document.createElement('td');
      let td3 = document.createElement('td');
      let td4 = document.createElement('td');
      let td5 = document.createElement('td');
      let td6 = document.createElement('td');
      let td7 = document.createElement('td');
      let button1 = document.createElement('button');
      button1.className = 'action-btn edit';
      let button2 = document.createElement('button');
      button2.className = 'action-btn sell';

      td1.textContent = make;
      td2.textContent = model;
      td3.textContent = year;
      td4.textContent = fuel;
      td5.textContent = originalPrice;
      td6.textContent = sellingPrice;
      button1.textContent = 'Edit';
      button2.textContent = 'Sell';
      td7.appendChild(button1);
      td7.appendChild(button2);
      tr.appendChild(td1);
      tr.appendChild(td2);
      tr.appendChild(td3);
      tr.appendChild(td4);
      tr.appendChild(td5);
      tr.appendChild(td6);
      tr.appendChild(td7);
      tableBodyEl.appendChild(tr);
      
      button1.addEventListener('click', onEdit);
      button2.addEventListener('click', onSell);

      makeEl.value = '';
      modelEl.value = '';
      yearEl.value = '';
      fuelEl.value = ''
      originalCostEl.value = '';
      sellingPriceEl.value = '';

     
    function onEdit(event) {
      event.preventDefault();

      makeEl.value = make;
      modelEl.value = model;
      yearEl.value = year;
      fuelEl.value = fuel;
      originalCostEl.value = originalPrice;
      sellingPriceEl.value= sellingPrice;

      event.target.parentNode.parentNode.remove();
    }

    function onSell(event) {
      event.preventDefault();
      const carsList = document.getElementById('cars-list');
      let li = document.createElement('li');
      li.className = 'each-list';
      let span1 = document.createElement('span');
      let span2 = document.createElement('span');
      let span3 = document.createElement('span');
      li.appendChild(span1);
      li.appendChild(span2);
      li.appendChild(span3);
      carsList.appendChild(li)

      let profit = sellingPrice - originalPrice
      span1.textContent = `${make} ${model}`;
      span2.textContent = `${year}`;
      span3.textContent = `${profit}`;

      totalProfit += profit;
      event.target.parentNode.parentNode.remove()

      const totalProfitEl = document.getElementById('profit');
      totalProfitEl.textContent = totalProfit.toFixed(2);
    }
  }
}
