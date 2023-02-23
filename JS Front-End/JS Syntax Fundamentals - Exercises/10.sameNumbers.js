function solve(digits) {

    let arr = Array.from(String(digits));
    let currNum = arr[0];
    let flag = true;
    let sum = 0;

    for(num of arr) {
        if (num == currNum) {
            flag = true;
        } else {
            flag = false;
        }

        sum += Number(num);
    }

    console.log(flag);
    console.log(sum);
}
