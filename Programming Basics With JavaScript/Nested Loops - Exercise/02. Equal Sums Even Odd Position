function equalSumsEvenOddPosition (input) {
    let n = Number(input[0]);
    let m = Number(input[1]);
    let printLine = '';

    for (let i = n; i <= m; i++) {
        let currentNum = "" + i;
        let oddSum = 0;
        let evenSum = 0;

        for (let j = 0; j < currentNum.length; j++) {
            let currentDigit = Number(currentNum.charAt(j));
            if (j % 2 === 0) {
                evenSum += currentDigit;
            } else {
                oddSum += currentDigit;
            }
        }
        if (evenSum === oddSum) {
            printLine += `${i}` + " ";
        }
    }
    console.log(printLine);
}
