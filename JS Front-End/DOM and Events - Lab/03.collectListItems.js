function extractText() {
    let ulElement = document.getElementById('items');

    let textareaElement = document.getElementById('result');
    textareaElement.textContent = ulElement.textContent;
}
