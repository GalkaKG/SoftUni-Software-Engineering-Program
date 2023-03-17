function solve() {
   const inputText = document.getElementById('text').value;
   const inputConvention = document.getElementById('naming-convention').value;
   const btn = document.querySelector('input[type="button"]');
   let resultSpan = document.getElementById('result')
   
   let text = inputText.toLowerCase().split(' ');
   let result = '';

   if (inputConvention == 'Camel Case') {
      for (let i = 0; i < text.length; i++) {
         if (i == 0) {
            result = text[0];
         } else {
            result += text[i].charAt(0).toUpperCase() + text[i].slice(1);
         }
       }
       resultSpan.textContent = result;
   } else if (inputConvention == 'Pascal Case') {
       for (let word of text) {
         result += word.charAt(0).toUpperCase() + word.slice(1);
       }
       resultSpan.textContent = result;
   } else {
      resultSpan.textContent = 'Error!'
   }

   inputText.value = '';
   inputConvention.value = '';
}
