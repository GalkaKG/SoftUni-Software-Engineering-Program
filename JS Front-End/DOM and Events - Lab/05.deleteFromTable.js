function deleteByEmail() {
    let email = document.getElementsByName('email')[0].value;
    let secondColumn = document.querySelectorAll('#customers tr td:nth-child(2)');

    for (let td of secondColumn) {
        if (td.textContent == email) {
            let row = td.parentNode;
            row.parentNode.removeChild(row);
            document.getElementById('result').textContent = 'Deleted.';
            return;
        }

        document.getElementById('result').textContent = 'Not found.';
    }

    console.log(secondColumn);
}
