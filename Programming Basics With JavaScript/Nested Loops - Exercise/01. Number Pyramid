function solve (input) {
    let n = Number(input[0]);
    let current = 1;
    let isFinisH = false;
    let printLine = "";

    for (let i = 1; i <= n; i++) {
        for (let j = 1; j <= i; j++) {
           
            if (current > n) {
                isFinisH = true;
                break;
            }

            printLine += current + " ";
            current++;
        }
      
        console.log(printLine);

        printLine ="";

        if (isFinisH) {
            break;
        }
    }
}
