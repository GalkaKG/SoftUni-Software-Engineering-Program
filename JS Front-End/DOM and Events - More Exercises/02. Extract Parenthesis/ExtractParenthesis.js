function extract(content) {
    const element = document.getElementById(content);
    let contentText = element.textContent;
    let pattern = /(?<=\()[A-Za-z\s]+(?=\))/gm;
    let matchWords = contentText.match(pattern);

    console.log(matchWords.join('; '));
}
