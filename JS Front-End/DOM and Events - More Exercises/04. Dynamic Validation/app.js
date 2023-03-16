function validate() {
   const inputEl = document.querySelector('#email');
   inputEl.addEventListener('change', onValidate);

   function onValidate (e) {
      let inputValue = inputEl.value;
      let pattern = /[a-z]+@[a-z]+\.[a-z]+/gm
      inputValue.match(pattern)
      if (inputValue.match(pattern)) {
        inputEl.classList.remove('error');
      } else {
        inputEl.classList = 'error';
        inputEl.value = '';
      }
   }
}
