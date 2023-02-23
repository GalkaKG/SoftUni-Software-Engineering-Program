function solve(input) {
    let arr = [...input].sort((a,b) => a-b);
    let sortedArr = [];

    while (arr.length !== 0){
        sortedArr.push(arr.shift());
        sortedArr.push(arr.pop());
    }

    return sortedArr.filter(elem => typeof elem !== "undefined");
}
