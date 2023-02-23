function revealWords(words, text) {
    let wordsArr = words.split(', ');
    let textArr = text.split(' ');

    for(let word of wordsArr) {
        for(let element of textArr) {
            if (element.includes('*') && element.length == word.length) {
                text = text.replace(element, word);
            }
        }
    }
    
    console.log(text)

}
