function numbers(input) {
    let nums = input.split(' ').sort((a, b) => b - a);
    let sumNums = nums.reduce((a, b) => +a + +b, 0);
    let averageNum = sumNums / nums.length;
    let result = nums.filter((num) => num > averageNum).slice(0, 5);
    
    if (result.length == 0) {
        console.log('No');
    } 
    
    console.log(result.join(' '));
}
