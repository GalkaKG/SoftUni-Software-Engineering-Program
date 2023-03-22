function solve() {
  let firstNameEl = document.getElementById('first-name');
  let lastNameEl = document.getElementById('last-name');
  let age = document.getElementById('age');
  let gender = document.getElementById('genderSelect');
  let dishDescription = document.getElementById('task');
  const submitBtn = document.getElementById('form-btn');
  const counterEl = document.getElementById('progress-count');
  
  submitBtn.addEventListener('click', onSubmit);
  const ulInProgress = document.getElementById('in-progress');
  const ulProgressCount = document.getElementById('finished');

  function onSubmit(event) {
    event.preventDefault();

    if (firstNameEl.value == '' || lastNameEl.value == '' || age.value == '' || dishDescription.value  == '')  {
      return
    }

    let firstName = firstNameEl.value;
    let lastName = lastNameEl.value;
    let ageContent = age.value;
    let genderContent = gender.value;
    let dishDescriptionContent = dishDescription.value;
    console.log(genderContent);
    let li = document.createElement('li');
    li.innerHTML = `<li class="each-line">
                      <article>
                        <h4>${firstNameEl.value} ${lastNameEl.value}</h4>
                        <p>${genderContent}, ${age.value}</p>
                        <p>Dish description: ${dishDescription.value}</p>
                      </article>
                      <button class="edit-btn">Edit</button>
                      <button class="complete-btn">Mark as complete</button>
                    </li>`;
    ulInProgress.appendChild(li);

    let counter = Number(counterEl.textContent);
    counter++;
    counterEl.textContent = counter;

    firstNameEl.value = '';
    lastNameEl.value = '';
    age.value = '';
    gender.value = 'Male';
    dishDescription.value = '';

    const editBtn = document.querySelector('.edit-btn');
    const completeBtn = document.querySelector('.complete-btn');

    editBtn.addEventListener('click', onEdit);
    completeBtn.addEventListener('click', onComplete);

    function onEdit() {
        firstNameEl.value = firstName;
        lastNameEl.value = lastName;
        gender.value = genderContent;
        age.value = ageContent;
        dishDescription.value = dishDescriptionContent;
        let counter = Number(counterEl.textContent);
        counter--;
        counterEl.textContent = counter;
        let li = ulInProgress.querySelector('li');
        li.remove();
    }

    function onComplete() { 
        let li = ulInProgress.querySelector('li');
        editBtn.remove();
        completeBtn.remove();
        ulProgressCount.appendChild(li);
        let counter = Number(counterEl.textContent);
        counter--;
        counterEl.textContent = counter;
    } 

    let clearBtn = document.getElementById('clear-btn');
    clearBtn.addEventListener('click', onClear);

    function onClear() {
      let li = ulProgressCount.querySelector('li');
      li.remove()
    }  
  }
}
