function solve() {
    const fNameEl = document.getElementById('fname');
    const lNameEl = document.getElementById('lname');
    const emailEl = document.getElementById('email');
    const birthEl = document.getElementById('birth');
    const positionEl = document.getElementById('position');
    const salaryEl = document.getElementById('salary');
    const btnHireWorker = document.getElementById('add-worker');
    btnHireWorker.addEventListener('click', onHire);
    let tbody = document.getElementById('tbody');
    let sumEl = document.getElementById('sum');

    let budget = 0;

    function onHire(e) {
        e.preventDefault();
        let fName = fNameEl.value;
        let lName = lNameEl.value;
        let email = emailEl.value;
        let birth = birthEl.value;
        let position = positionEl.value;
        let salary = Number(salaryEl.value);

        if (!fName || !lName || !email || !birth || !position || !salary) {
            return
        }

        budget += salary;
    
        let tr = document.createElement('tr');
        let td1 = document.createElement('td');
        let td2 = document.createElement('td');
        let td3 = document.createElement('td');
        let td4 = document.createElement('td');
        let td5 = document.createElement('td');
        let td6 = document.createElement('td');
        let td7 = document.createElement('td');
        let firedBtn = document.createElement('button');
        firedBtn.className = 'fired';
        firedBtn.textContent = 'Fired';
        firedBtn.addEventListener('click', onFire);
        let editBtn = document.createElement('button');
        editBtn.className = 'edit';
        editBtn.textContent = 'Edit';
        editBtn.addEventListener('click', onEdit);
        td1.textContent = fName;
        td2.textContent = lName;
        td3.textContent = email;
        td4.textContent = birth;
        td5.textContent = position;
        td6.textContent = salary;
        td7.appendChild(firedBtn);
        td7.appendChild(editBtn);
        tr.appendChild(td1);
        tr.appendChild(td2);
        tr.appendChild(td3);
        tr.appendChild(td4);
        tr.appendChild(td5);
        tr.appendChild(td6);
        tr.appendChild(td7);
        tbody.appendChild(tr);

        fNameEl.value = '';
        lNameEl.value = '';
        emailEl.value = '';
        birthEl.value = '';
        positionEl.value = '';
        salaryEl.value = '';

        sumEl.textContent = budget.toFixed(2);
        
        function onEdit(e) {
            fNameEl.value = fName;
            lNameEl.value = lName;
            emailEl.value = email;
            birthEl.value = birth;
            positionEl.value = position;
            salaryEl.value = salary;

            e.target.parentNode.parentNode.remove();
            budget -= salary;
            sumEl.textContent = budget.toFixed(2);
        }

        function onFire(e) {
            e.target.parentNode.parentNode.remove();
            budget -= salary;
            sumEl.textContent = budget.toFixed(2);
        }
    }
}

// Извикването на функцията не се подава в джъдж

solve();
