function solve(n, array) {
   let newArr = []
   for (let i = 0; i < n; i++) {
      newArr.push(array[i]);
   }

   let output = ''
   for (let i = newArr.length-1; i >= 0; i--) {
       output += String(newArr[i]) + ' ';
   }

   console.log(output);
}
