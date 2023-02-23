function pascalCaseSplit(text) {
    let pattern = '[A-Z][a-z]*';
    let matches = text.matchAll(pattern);
    let arr = [];

    for (word of matches) {
        arr.push(word[0]);
    }

    console.log(arr.join(', '));

}
