function addItem() {
    let newElement = document.getElementById('newItemText').value;
    let list = document.getElementById('items');

    if (newElement.length == 0) {
        return;
    }

    let listItem = document.createElement('li');
    listItem.textContent = newElement;

    let remove = document.createElement('a');
    let linkText = document.createTextNode('[Delete]');
    remove.appendChild(linkText);
    remove.href = '#';
    remove.addEventListener('click', deleteItem);

    listItem.appendChild(remove);
    list.appendChild(listItem);

    function deleteItem() {
        listItem.remove();
    }
}
