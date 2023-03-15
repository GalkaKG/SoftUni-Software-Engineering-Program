function editElement(element, match, replacer) {
    let text = element.textContent;
    
    while (text.includes(match)) {
        text = text.replace(match, replacer);
    }
    element.textContent = text;
}
