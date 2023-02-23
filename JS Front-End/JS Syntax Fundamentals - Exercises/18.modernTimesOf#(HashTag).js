function modernTimes(input) {
    let sentence = input.split(" ");

    for (let word of sentence) {
        if (word.startsWith("#") && word.length > 1) {
            let flag = true;
            let wordLower = word.toLowerCase();
            for (let i = 1; i < wordLower.length; i++) {
                if (wordLower.charCodeAt(i) < 97 || wordLower.charCodeAt(i) > 122) {
                    flag = false;
                    break;
                }
            }
            if (flag) {
                console.log(word.split("#")[1])
            }
        }
    }
}
