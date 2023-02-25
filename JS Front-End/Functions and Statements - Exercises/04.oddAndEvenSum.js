function oddAndEvenSum(input) {
    let oddSum = 0;
    let evenSum = 0;
    input = String(input);
    
    for(let char of input) {
        if (Number(char) % 2 == 0) {
            evenSum += Number(char);
        } else {
            oddSum += Number(char);
        }
    }

    console.log(`Odd sum = ${oddSum}, Even sum = ${evenSum}`)
}
