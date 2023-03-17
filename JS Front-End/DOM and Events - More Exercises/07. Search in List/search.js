function search() {
   const inputText = document.getElementById('searchText').value;
   const towns = Array.from(document.querySelectorAll('#towns li'));
   let matches = 0;
   towns.forEach((li) => {
      li.style.textDecoration = 'none'; 
      li.style.fontWeight = '400';
   })
   towns.forEach((li) => {
      let pattern = new RegExp(inputText);
      if (li.textContent.match(pattern)) {
         li.style.textDecoration = 'underline';
         li.style.fontWeight = 'bold';
         matches++;
      }
   });
   document.getElementById('result').textContent = `${matches} matches found`
   document.getElementById('searchText').value = '';  
}
