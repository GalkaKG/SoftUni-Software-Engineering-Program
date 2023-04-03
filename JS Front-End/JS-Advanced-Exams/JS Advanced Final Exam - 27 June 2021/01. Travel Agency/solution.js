window.addEventListener('load', solution);

function solution() {
  const fullNameEl = document.getElementById('fname');
  const emailEl = document.getElementById('email');
  const phoneEl = document.getElementById('phone');
  const addressEl = document.getElementById('address');
  const postalCodeEl = document.getElementById('code');
  const infoPreviewEl = document.getElementById('infoPreview');
  const mainBlock = document.getElementById('block');

  const submitBtn = document.getElementById('submitBTN');
  submitBtn.addEventListener('click', onSubmit);
  const editBtn = document.getElementById('editBTN');
  editBtn.addEventListener('click', onEdit);
  const continueBtn = document.getElementById('continueBTN');
  continueBtn.addEventListener('click', onContinue);

  let data = {};

  function onSubmit() {
    data.fullName = fullNameEl.value;
    data.email = emailEl.value;
    data.phone = phoneEl.value;
    data.address = addressEl.value;
    data.postalCode = postalCodeEl.value;

      if (!data.fullName || !data.email) {
        return
      }

      let li1 = document.createElement('li');
      let li2 = document.createElement('li');
      let li3 = document.createElement('li');
      let li4 = document.createElement('li');
      let li5 = document.createElement('li');
      li1.textContent = `Full Name: ${data.fullName}`;
      li2.textContent = `Email: ${data.email}`;
      li3.textContent = `Phone Number: ${data.phone}`;
      li4.textContent = `Address: ${data.address}`;
      li5.textContent = `Postal Code: ${data.postalCode}`;
      infoPreviewEl.appendChild(li1);
      infoPreviewEl.appendChild(li2);
      infoPreviewEl.appendChild(li3);
      infoPreviewEl.appendChild(li4);
      infoPreviewEl.appendChild(li5);
      
      submitBtn.disabled = true;
      continueBtn.disabled = false;
      editBtn.disabled = false;
      
      fullNameEl.value = '';
      emailEl.value = '';
      phoneEl.value = '';
      addressEl.value = '';
      postalCodeEl.value = '';
  }

  function onEdit() { 
      fullNameEl.value = data.fullName;
      emailEl.value = data.email;
      phoneEl.value = data.phone;
      addressEl.value = data.address;
      postalCodeEl.value = data.postalCode;

      editBtn.disabled = true;
      continueBtn.disabled = true;
      submitBtn.disabled = false;
      
      infoPreviewEl.innerHTML = '';
  }

  function onContinue() {
      mainBlock.innerHTML = `<h3>Thank you for your reservation!</h3>`
  }
}
