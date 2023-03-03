function numberModification(num) {
    let numArr = num.toString().split('').map(x => Number(x));
    let avgNum = numArr.reduce((a, b) => a + b, 0) / numArr.length;

    if (avgNum > 5) {
        console.log(num)
    } else {
        while (avgNum < 5) {
            numArr.push(9);
            avgNum = numArr.reduce((a, b) => a + b, 0) / numArr.length;
        }
        console.log(numArr.join(''));
    }

}
