function palindromeIntegers(arr) {
    for (let el of arr) {
       let reversed = String(el).split('').reverse().join('');

        if (el == reversed) {
            console.log('true')
        } else {
            console.log('false')
        }

    }
}
