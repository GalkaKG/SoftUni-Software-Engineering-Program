function solve() {
    let firstName = document.getElementById('first-name');
    let lastName = document.getElementById('last-name');
    let checkIn = document.getElementById('date-in');
    let checkOut = document.getElementById('date-out');
    let numberOfGuests = document.getElementById('people-count');
    const ul = document.querySelector('.info-list');
    
    const btnNext = document.getElementById('next-btn');
    btnNext.addEventListener('click', onNext);
     
    function onNext(event) {
        event.preventDefault();

        if (firstName.value == '' || lastName.value == '' || numberOfGuests.value == '' || checkOut.value < checkIn.value || checkIn.value == '' || checkOut.value == '') {
            return
        }
        let firstNameContent = firstName.value;
        let lastNameContent = lastName.value;
        let checkInContent = checkIn.value;
        let checkOutContent = checkOut.value;
        let numberOfGuestsContent = numberOfGuests.value;
        let nameBtn1 = 'Edit';
        let nameBtn2 = 'Continue';
        let className1 = 'edit-btn';
        let className2 = 'continue-btn';

        ul.innerHTML = putInnerHtml(nameBtn1, nameBtn2, className1, className2);
        
        btnNext.disabled = true;

        firstName.value = '';
        lastName.value = '';
        checkIn.value = '';
        checkOut.value = '';
        numberOfGuests.value = '';

        const editBtn = document.querySelector('.edit-btn');
        editBtn.addEventListener('click', onEdit);

        function onEdit() {
            firstName.value = firstNameContent;
            lastName.value = lastNameContent;
            checkIn.value = checkInContent;
            checkOut.value = checkOutContent;
            numberOfGuests.value = numberOfGuestsContent;
            btnNext.disabled = false;
            ul.children[0].remove();
        }

        let continueBtn = document.querySelector('.continue-btn');
        continueBtn.addEventListener('click', onContinue);

        function onContinue() {
            let nameBtn1 = 'Confirm';
            let nameBtn2 = 'Cancel';
            let className1 = 'confirm-btn';
            let className2 = 'cancel-btn'; 
            const confirmUl = document.querySelector('.confirm-list');
            confirmUl.innerHTML = putInnerHtml(nameBtn1, nameBtn2, className1, className2);
            ul.innerHTML = '';
            let confirmBtn = document.querySelector('.confirm-btn');
            let cancelBtn = document.querySelector('.cancel-btn');
            confirmBtn.addEventListener('click', onConfirm);
            cancelBtn.addEventListener('click', onCancel);
            let h1Verification = document.getElementById('verification');
            
            function onConfirm() {
                const ul = document.querySelector('.confirm-list');
                ul.children[0].remove();
                btnNext.disabled = false;
                h1Verification.textContent = 'Confirmed.';
                h1Verification.className = "reservation-confirmed" ;
            }

            function onCancel() {
                const ul = document.querySelector('.confirm-list');
                ul.children[0].remove();
                btnNext.disabled = false;
                h1Verification.textContent = 'Cancelled.';
                h1Verification.className = "reservation-cancelled" ;
            }
        }

        function putInnerHtml(nameBtn1, nameBtn2, className1, className2) {
            return `<li class="reservation-content">
                        <article>
                            <h3>Name: ${firstNameContent} ${lastNameContent}</h3>
                            <p>From date: ${checkInContent}</p>
                            <p>To date: ${checkOutContent}</p>
                            <p>For ${numberOfGuestsContent} people</p>
                        </article>
                    <button class="${className1}">${nameBtn1}</button>
                    <button class="${className2}">${nameBtn2}</button>
                    </li>`
        }
    }
    }
