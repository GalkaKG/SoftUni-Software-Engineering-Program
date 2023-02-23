function solve(num1, num2) {
    let sum = 0
    let output = ''

    for(let i = num1; i <= num2; i++) {
        output += String(i) + ' ';
        sum += i;
    }

    console.log(output);
    console.log(`Sum: ${sum}`)
}
