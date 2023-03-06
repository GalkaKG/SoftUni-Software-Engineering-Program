function sumTable() {
    let costElements = document.querySelectorAll('tr td:nth-of-type(2)');

    let sum = Array.from(costElements).reduce((a, x) => {
        let currValue = Number(x.textContent) || 0;
        return a + currValue;
    }, 0);
    
    let resultElement = document.getElementById('sum');
    resultElement.textContent = sum
   
}
