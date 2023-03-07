function subtract() {
    let firstNumber = document.getElementById('firstNumber');
    let firstNumAsNumber = Number(firstNumber.value);
    let secondNumber = document.getElementById('secondNumber');
    let secondNumAsNumber = Number(secondNumber.value)

    let result = firstNumAsNumber - secondNumAsNumber;
    let resultElement = document.getElementById('result');
    resultElement.textContent = result
  
}
