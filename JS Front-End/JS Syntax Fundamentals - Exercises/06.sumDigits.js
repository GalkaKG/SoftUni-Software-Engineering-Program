function solve(digits) {

    let sum = 0
    let arr = Array.from(String(digits))

    for (let num of arr) {
        sum += Number(num)
    }
   
    console.log(sum)

}
