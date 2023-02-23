function solve(num1, num2, num3) {
     let largestNum = 0

     if (num1 > num2 && num1 > num3) {
        largestNum = num1;
     } else if (num2 > num1 && num2 > num3) {
        largestNum = num2;
     } else {
        largestNum = num3;
     }

     console.log(`The largest number is ${largestNum}.`);
}
