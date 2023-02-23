function printEveryNth(input, n) {
    let newArr = [];

    for (let i = 0; i < input.length; i += n) {
        newArr.push(input[i]);
    }

    return newArr;
}
