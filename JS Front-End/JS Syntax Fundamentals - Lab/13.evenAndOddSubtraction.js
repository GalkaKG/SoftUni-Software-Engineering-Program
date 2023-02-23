function solve(arr) {

    let evenSum = 0;
    let oddSum = 0;

    for(let i = 0; i < arr.length; i++) {
        num = Number(arr[i]);

        if (num % 2 == 0) {
            evenSum += num;
        } else {
            oddSum += num;
        }
    }

    let result = evenSum - oddSum

    console.log(result)
}
