function stringSubstring(word, text) {
    let textArr = text.split(' ');
    flag = true;

    for(el of textArr) {
        if (el.toLowerCase() == word) {
            console.log(word);
            flag = false
            break;
        }
    }
            
    if (flag) {
        console.log(`${word} not found!`)
    }

}
