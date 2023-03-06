function colorize() {
    let tableRow = Array.from(document.querySelectorAll('tr:nth-of-type(2n)'));
    tableRow.forEach(td => td.style.backgroundColor = 'teal');
}
